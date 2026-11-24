# Radio de explosión

## Definición

El **radio de explosión** es el conjunto de lo que algo puede dañar si sale mal. El programa lo usa con tres matices:

- En `SE-506` (ingeniería del caos): lo que un experimento puede dañar, descrito por fracción de tráfico, alcance, duración, intensidad y profundidad. `SE-394` lo resume como el alcance máximo del daño de un experimento.
- En `SE-326` (arquitectura): el conjunto de recorridos o funciones que dejan de funcionar cuando falla un elemento.
- En `SE-403` (cloud): el conjunto de recursos que un error o una credencial comprometida puede afectar.

## Por qué importa

Un fallo, un experimento o una credencial robada tienen un daño máximo. Si ese máximo es la plataforma entera, cada error es potencialmente catastrófico. La decisión que cambia es diseñar para acotar: separar, limitar y dosificar, de modo que lo peor posible sea tolerable.

## Cómo funciona

`SE-506` plantea el radio como una responsabilidad: se admite un impacto negativo de corto plazo, pero se debe contener. No es un solo número: se controla en cinco dimensiones que se combinan:

1. **Fracción del tráfico** afectada.
2. **Alcance**: qué clientes, instancias, zonas o regiones.
3. **Duración**.
4. **Intensidad** de la falla (10 % de errores o 100 %).
5. **Profundidad**: si afecta solo a la llamada probada o a lo que depende de ella.

Herramientas como Chaos Mesh definen el alcance con selectores por espacio de nombres, etiquetas, anotaciones o nodos; la documentación lo presenta como el control del radio.

En arquitectura, `SE-326` reproduce el fallo clásico: replicar la base de datos y creer que el sistema ya no tiene un punto único de fallo, cuando la web sigue en un solo nodo; calcular el radio de explosión de la topología revela qué sigue cayendo. En cloud, `SE-403` muestra que separar por entorno y por carga reduce el máximo daño posible de una credencial robada o de un comando mal escrito.

## Ejemplo

Un experimento de caos inyecta latencia. Con el radio definido como 1 % del tráfico, una zona, 5 minutos, intensidad moderada y solo la llamada probada, el daño máximo es pequeño aunque la falla resulte peor de lo previsto. Con un radio sin acotar, la misma falla puede tumbar la plataforma. Principio de `SE-506`.

## Errores y confusiones comunes

- **El experimento no detecta nada y se declara confirmado**: radio sin potencia suficiente; se calcula la fracción mínima y se declara el efecto mínimo detectable.
- **El experimento aborta de inmediato**: condición global consumida por la falla esperada; se mide el grupo experimental y se separa el umbral de aborto del de la hipótesis.
- **Reducirlo a un porcentaje**: son cinco dimensiones.
- **Creer que replicar un componente elimina el punto único de fallo**.

## Límites y cuándo no aplica

Un radio muy pequeño reduce el daño pero también la potencia para detectar el efecto: hay un compromiso entre seguridad y capacidad de aprender del experimento. El radio describe el máximo previsto: un fallo que se propaga por dependencias no consideradas puede exceder el cálculo. Y no sustituye una condición de aborto que detenga el daño en curso.
