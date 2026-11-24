# Corrida

## Definición

Una **corrida** (de entrenamiento) es una ejecución de entrenamiento con datos, configuración, semilla y entorno determinados (`SE-603`).

## Por qué importa

Si no se puede reconstruir una corrida, no se puede explicar por qué un modelo es como es ni comparar dos modelos con honestidad. El costo de guardar el registro es despreciable frente al de no poder reconstruirlo.

## Cómo funciona

`SE-603` la describe como una función de cinco cosas: los datos (filas y orden), las etiquetas, la configuración (hiperparámetros, preprocesamiento), el generador aleatorio con su semilla y el entorno (versiones de las bibliotecas, sistema operativo, hilos). Si una cambia, el modelo puede cambiar. Reproducir significa poder fijar las cinco y comprobarlo; por eso el registro guarda una huella de los datos y las etiquetas, una huella de la configuración serializada, la semilla, las versiones y el valor de la métrica. En el laboratorio, ese registro ocupa 209 bytes.

## Ejemplo

`SE-603`: el equipo de *Avisos-ML* promueve un candidato solo si, sobre cinco muestras de entrenamiento y tres semillas por muestra, su AUC pareado mejora en promedio y el intervalo de las diferencias no incluye el cero. Una tarea de integración continua falla si falta el `run.json` con las huellas. Un cambio con un AUC un punto mayor en una sola corrida es rechazado: la diferencia pareada no supera el ruido.

## Errores y confusiones comunes

Comparar dos modelos con una corrida cada uno: la variación por semilla puede explicar la diferencia. No registrar el orden de las filas.

## Límites y cuándo no aplica

La reproducibilidad exacta puede romperse por hardware o bibliotecas no deterministas aunque las cinco cosas se fijen; en ese caso se compara con repeticiones y se reporta dispersión.
