# Característica

## Definición

En aprendizaje automático, una **característica** (*feature*) es una variable de entrada calculada a partir de eventos anteriores a la decisión (`SE-602`). Las características son lo que el modelo ve; el valor que debe predecir es la etiqueta.

## Por qué importa

La condición «anteriores a la decisión» es el punto de la definición. Una característica que contiene información que no estará disponible en el momento de decidir produce una **fuga**: el modelo parece excelente fuera de línea y falla en producción.

## Cómo funciona

`SE-602` explica que la causa más frecuente de fuga no es un descuido grande sino una **ventana mal cortada**: un agregado que incluye el día de la decisión, una normalización calculada con todo el conjunto, un identificador que codifica el resultado. En su medición, un modelo con una característica contaminada («entregas tardías de la semana» que incluye la entrega misma) alcanzó un AUC de 0,987 frente a 0,851 sin ella: 0,136 de mejora ficticia.

## Ejemplo

El equipo de *Avisos* descubre que su AUC de 0,98 era fuga. Define una regla: toda característica nueva se documenta con su fuente, su ventana y su «disponible desde», y una prueba recalcula la característica sobre un historial truncado en el instante de decisión; si el valor cambia al añadir el futuro, la prueba falla.

## Errores y confusiones comunes

Medir calidad con la característica contaminada; calcular normalizaciones con todo el conjunto; olvidar guardar con cada predicción las entradas y la versión del modelo.

## Límites y cuándo no aplica

La prueba de truncamiento detecta fugas temporales, no sesgos de otra naturaleza. Los números de la clase son de un laboratorio con datos sintéticos.
