# Invalidación

## Definición

La **invalidación** (de la caché) es la eliminación o actualización de una entrada de la caché cuando cambia el dato de origen (`SE-356`). Es la política que mantiene fresca la caché al escribir, en contraste con esperar a que las entradas expiren por su TTL.

## Por qué importa

Una caché mejora la latencia y descarga al origen, pero guarda copias que pueden quedar viejas. La decisión que cambia es cuánta obsolescencia tolera cada dato: donde el costo de un valor viejo es alto, se invalida al escribir; donde es bajo, un TTL basta. Elegir mal da o usuarios que ven datos incorrectos con la tasa de aciertos alta, o una caché que casi no ayuda.

## Cómo funciona

`SE-356` explica por qué invalidar al escribir mantiene la caché fresca sin renunciar a los aciertos, y por qué es difícil por tres razones:

1. **Una escritura puede afectar a muchas claves**: un cambio en un curso afecta a las listas de todos sus estudiantes; hay que saber cuáles invalidar.
2. **La orden de invalidación puede perderse o llegar tarde** en un sistema distribuido.
3. **La invalidación compite con las lecturas que rellenan**: un lector lento puede escribir en la caché un valor viejo después de la invalidación.

Los remedios son dos. Para la carrera con el relleno, guardar cada valor con **versión** y no pisar una mayor. Para la orden perdida, combinar la invalidación con un **TTL de respaldo**: la invalidación da frescura en el caso normal y el TTL acota el daño cuando falla. La clase resume la elección: cada política compra frescura con aciertos, o con una promesa sobre la invalidación; la figura no dice cuál usar.

La invalidación masiva (de muchas claves a la vez) puede provocar una estampida: todas se rellenan a la vez desde la base.

## Ejemplo

Un curso cambia su nombre. Se invalida la entrada del curso, pero también las listas de estudiantes que lo incluyen. Un lector que había empezado a leer antes de la escritura termina después de la invalidación y rellena la caché con el nombre viejo. Si cada valor lleva versión, el relleno de la versión vieja se descarta; si además hay TTL, el daño tiene fin aunque falle algo. Ejemplo de `SE-356`.

## Errores y confusiones comunes

- **Un valor sigue viejo tras una invalidación**: relleno tardío de un lector lento; se corrige guardando con versión y sin pisar una mayor.
- **La tasa de aciertos es alta y los usuarios se quejan**: TTL largo sin invalidación; se corrige acotando el TTL según la tolerancia e invalidando donde importe.
- **Invalidar solo la clave obvia**: las claves derivadas quedan viejas.
- **Confiar solo en la invalidación**: sin TTL, un fallo deja el valor viejo para siempre.

## Límites y cuándo no aplica

Para datos que cambian poco, o donde un valor viejo es tolerable por minutos, un TTL simple es más barato y robusto que una invalidación activa. La invalidación exige conocer qué claves dependen de qué dato, un acoplamiento que crece con el sistema. Y en sistemas distribuidos no garantiza frescura absoluta: reduce la ventana de obsolescencia, no la elimina.
