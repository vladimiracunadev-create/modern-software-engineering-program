# Peor caso de ejecución

## Definición

El **peor caso de ejecución** (*WCET*, *worst-case execution time*) es la cota superior del tiempo de cómputo de una tarea sobre todas las entradas y estados posibles. Es el sentido de `SE-268` (sistemas de tiempo real y deadlines); `SE-451` lo llama el insumo más difícil de obtener para planificar. No es el tiempo promedio ni el mayor observado en pruebas: es un límite que ninguna ejecución posible debe superar.

## Por qué importa

El análisis de planificación (si las tareas cumplen sus plazos) usa el peor caso, no el medio. Con la media, un plazo se incumple con una frecuencia que depende de la variabilidad. `SE-268` lo dice: si un trabajo se pasa de su periodo, retrasa al siguiente y la sobrecarga se encadena; por eso la utilización media no basta, importa la cola de la distribución.

## Cómo funciona

Hay dos caminos para obtenerlo, y ambos tienen incertidumbre:

- **Análisis estático:** deriva una cota a partir del código y del modelo del procesador. Es segura si el modelo es fiel, pero puede ser pesimista.
- **Medición con entradas extremas:** ejecuta la tarea con las entradas más desfavorables conocidas. Da un *límite inferior* del peor caso: lo que se observó, no lo que puede ocurrir.

Las fuentes de incertidumbre son cachés, ramas poco frecuentes y esperas de periféricos. Por eso la medición necesita un margen y el análisis estático, un modelo de hardware.

## Ejemplo

El laboratorio de `SE-268` ordena 8 elementos con salida anticipada: 56 pasos de mediana, 80 pasos como máximo observado en 1000 entradas al azar y 84 pasos en el peor caso real (entrada en orden inverso), que 1000 entradas aleatorias no generan. La marca de agua observada queda 4,8 % por debajo del peor caso real. Moraleja: el máximo observado subestima el WCET cuando el peor caso es raro.

## Errores y confusiones comunes

- **Usar el promedio o la mediana** para verificar plazos.
- **Tomar el máximo observado en pruebas como WCET.**
- **Ignorar la interferencia:** el WCET «sin interferencias» no incluye el efecto de otras tareas ni interrupciones; se suma en el análisis de planificación.
- **Confundirlo con latencia de cola:** esta es estadística sobre peticiones; el WCET es una cota para tareas de tiempo real.

## Límites y cuándo no aplica

En procesadores modernos con cachés, predicción de saltos y varios núcleos, obtener una cota ajustada es difícil. Para sistemas sin plazos duros (la mayoría del software de negocio) no se calcula; se usan percentiles. Las cifras de la clase son de un laboratorio con una ordenación pequeña, no de un procesador real.
