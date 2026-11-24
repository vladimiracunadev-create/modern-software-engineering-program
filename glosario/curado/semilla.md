# Semilla

## Definición

Una **semilla** es el valor inicial de un generador pseudoaleatorio que permite repetir su secuencia (`SE-428`, `SE-603`). Con la misma semilla, el generador produce los mismos «azares» en el mismo orden. En `SE-411` el término tiene otro sentido: los datos iniciales que se crean para que un cliente nuevo tenga algo con qué empezar (*seed data*).

## Por qué importa

Los datos aleatorios amplían los casos que se prueban, pero rompen la reproducibilidad: un fallo que no se puede repetir no se puede investigar. La decisión que cambia es que el azar se conserva, pero su origen se registra. Con la semilla impresa, un fallo intermitente se vuelve determinista.

## Cómo funciona

`SE-428` lo plantea así: la corrección no es quitar el azar sino **registrar la semilla**. Cada ejecución genera con una semilla impresa en el informe, y quien ve un fallo lo repite con ella. La clase añade un efecto de composición: una propiedad que falla con probabilidad pequeña por elemento falla con probabilidad mucho mayor con veinte elementos, de modo que un generador con muchos elementos por prueba hace aflorar casos raros a menudo y los hace parecer intermitentes.

La clase fija reglas concretas para el equipo de la plataforma: la suite se ejecuta cada noche en un orden aleatorio con semilla impresa y un fallo se repite con una opción `--semilla`; toda prueba con datos aleatorios recibe un generador con semilla de un único punto; los constructores crean datos con valores por defecto y los valores con significado se nombran. Un inventario trimestral busca usos de reloj, `uuid`, `random` y conjuntos sin orden definido, que son las fuentes habituales de no determinismo.

En `SE-603` (ML en producción), una corrida de entrenamiento es función de cinco cosas: los datos (filas y orden), las etiquetas, la configuración, el generador aleatorio con su semilla y el entorno (versiones de numpy y scikit-learn, sistema operativo, hilos). Fijar la semilla es una condición para reproducir un modelo, pero no la única.

## Ejemplo

Una prueba con datos generados al azar falla una de cada diez ejecuciones. Con la semilla impresa en el informe de la ejecución fallida, se vuelve a lanzar con `--semilla 12345` y falla siempre, lo que permite depurarla. Sin la semilla, el fallo habría parecido intermitente e inexplicable. Procedimiento de `SE-428`.

## Errores y confusiones comunes

- **Una prueba falla una vez de cada diez**: datos aleatorios sin semilla o propiedad mal enunciada; se corrige registrando la semilla y revisando la propiedad.
- **Fijar una semilla en el código y olvidarla**: se pierde la exploración de casos nuevos.
- **Creer que la semilla basta para reproducir un entrenamiento**: también cuentan los datos, la configuración y el entorno.
- **Mezclar sentidos**: la semilla de un generador no es el dato inicial de un cliente.

## Límites y cuándo no aplica

Una semilla garantiza repetir la secuencia solo si el resto del programa es determinista: relojes, orden de hilos y orden de iteración de conjuntos pueden seguir introduciendo variación. Un generador pseudoaleatorio no sirve para fines criptográficos. Y reproducir un fallo con la semilla no explica su causa: solo permite estudiarlo.
