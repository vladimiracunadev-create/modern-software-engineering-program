# Deriva de concepto

## Definición

La **deriva de concepto** (*concept drift*) es el cambio de la relación entre las entradas de un modelo y la etiqueta que debe predecir. Es la definición de `SE-608`. Las entradas pueden verse idénticas, pero lo que significan para el resultado ya no es lo mismo: el modelo aprendió una relación que el mundo cambió.

## Por qué importa

Es la deriva que más fácil se escapa, porque no deja rastro en las entradas ni en las salidas. Cambia una decisión de monitoreo: un panel que solo vigila distribuciones de entrada y salida no está vigilando el modelo. `SE-608` lo dice sin rodeos: el monitoreo de un modelo sin etiquetas no es monitoreo del modelo; o se consiguen etiquetas (aunque sea de una muestra) o se declara que la deriva de concepto es un riesgo no vigilado.

## Cómo funciona

Un modelo aprende `P(etiqueta | entradas)`. La **deriva de covariables** cambia la distribución de las entradas; la **deriva de concepto** cambia la relación misma. Si cambia la relación pero no las entradas, las métricas basadas en distribución (por ejemplo el PSI, índice de estabilidad de población) no se mueven. Solo una métrica que compare predicción con etiqueta verdadera lo ve, y las etiquetas llegan con retraso (el pago, la devolución o el resultado final tardan en ocurrir).

El experimento de `SE-608` lo muestra: se redujo el peso del historial de tardanzas sobre la etiqueta a 0,3 de su valor (`concept=0,3`), manteniendo las entradas con la misma distribución. El PSI máximo de las entradas fue 0,002 y el PSI de la salida 0,000, pero el AUC pasó de 0,846 a 0,802, una caída de 0,044. Ninguna señal de entrada ni de salida lo vio.

## Ejemplo

El caso de `SE-608` es sintético: un modelo de riesgo cuya característica «historial de tardanzas» pierde peso real sobre el desenlace. Los clientes siguen llegando con historiales de la misma forma, el modelo puntúa igual de confiado, y el AUC cae. En la ejecución citada de `SE-611`, una deriva de este tipo se detectó con etiquetas a las 57 horas; ninguna otra señal la detectó. La respuesta de la clase ante la imposibilidad de etiquetar todo es parcial: declarar que el riesgo no está vigilado, etiquetar una muestra si se puede y limitar el uso del modelo a decisiones que toleren esa incertidumbre.

## Errores y confusiones comunes

- **«Los paneles de deriva están verdes, el modelo está sano».** Solo vigilan entradas y salidas; la deriva de concepto es invisible para ellas.
- **Confundirla con deriva de covariables.** Aquella cambia lo que llega; esta, lo que significa. Se tratan distinto: la primera puede detectarse sin etiquetas, la segunda no.
- **Esperar al retraso de la etiqueta sin plan.** Entre el cambio y la etiqueta el modelo decide con una relación obsoleta.
- **Tratarla como un fallo del código.** No hay error que reproducir: el sistema funciona como fue entrenado.

## Límites y cuándo no aplica

`SE-608` trabaja con datos sintéticos y una deriva inyectada a propósito; el tamaño de la caída del AUC y la hora de detección no se extrapolan a sistemas reales. Solo aplica a modelos supervisados con una etiqueta definida; no tiene sentido hablar de ella donde no hay relación entradas-etiqueta estable que preservar. Una muestra etiquetada pequeña da una estimación ruidosa de la degradación, y su tamaño debe elegirse según la caída que se quiere poder ver.
