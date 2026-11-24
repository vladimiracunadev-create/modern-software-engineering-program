# Interferencia

## Definición

La **interferencia** es el efecto de una carga sobre la latencia o el éxito de otra que comparte recursos. Es el sentido de `SE-361` (del dato operacional al analítico): una lectura larga puede bloquear escrituras. Dos usos más del programa comparten solo el nombre: en `SE-437`, la actividad ajena al programa que contamina una medición (otro proceso, un cambio de frecuencia); en `SE-284`, en computación cuántica, la suma de amplitudes que se refuerzan o se cancelan. Esta entrada desarrolla el primero y menciona los otros para no confundirlos.

## Por qué importa

Cuando análisis y operación comparten la misma base, una consulta pesada degrada los pedidos reales. Reconocer la interferencia permite decidir si separar los sistemas vale su costo, o si basta una solución más barata.

## Cómo funciona

El mecanismo es competencia por un recurso: bloqueos, entrada/salida, memoria o CPU. Una consulta analítica que recorre muchas filas retiene recursos y retrasa las escrituras del sistema operacional.

`SE-361` ordena las soluciones por costo creciente:

1. **Réplica de lectura o vista materializada:** resuelve la interferencia sin añadir procesos. No resuelve la historia (la réplica guarda solo el estado actual) ni la forma (recorre filas completas).
2. **Separación con una plataforma de datos:** compensa cuando se cumplen a la vez tres cosas: el volumen hace que las preguntas analíticas compitan con la operación; la historia se necesita y se está perdiendo; varias personas o sistemas piden los mismos números.

Si solo ocurre una, suele bastar una solución local. Una plataforma que no se usa es un costo mensual.

En mediciones (`SE-437`), la interferencia exige aislar el entorno y repetir para distinguir el efecto del ruido.

## Ejemplo

Un sistema de entregas con pocos miles de filas, preguntas poco frecuentes y un equipo que responde a mano no necesita una plataforma de datos (`SE-361`). Ilustración propia: un informe mensual que tarda minutos y bloquea las escrituras justo al cierre de plazo se redirige a una réplica de lectura, con lo que la interferencia desaparece.

## Errores y confusiones comunes

- **Montar una plataforma analítica para un problema de interferencia pequeño.**
- **Creer que la réplica resuelve la necesidad de historia o agregados sobre años.**
- **Confundir el sentido de carga compartida con el de medición o el cuántico.**
- **Medir rendimiento mientras otra carga corre en el mismo equipo.**

## Límites y cuándo no aplica

La réplica retrasa los datos (lag) y no sirve cuando el análisis exige el último valor. Si el problema es una consulta mal escrita, separar sistemas no lo corrige. Las decisiones de `SE-361` dependen del volumen real; los umbrales de la clase son criterios, no fronteras fijas.
