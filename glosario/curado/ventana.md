# Ventana

## Definición

Una **ventana** es, en el sentido principal del programa (`SE-608`), el conjunto de observaciones recientes que se compara con una referencia, por ejemplo para detectar deriva en un modelo. `SE-362` usa el término en procesamiento de flujos: un intervalo del tiempo del evento sobre el que se agrega. En ambos, una ventana acota el tramo de datos sobre el que se calcula algo.

## Por qué importa

Un flujo de datos no tiene fin, así que cualquier medida o comparación necesita un recorte. La decisión que cambia es qué tramo se mira y de qué tamaño: una ventana corta reacciona rápido y da ruido; una larga es estable y tarda en notar el cambio.

## Cómo funciona

En monitoreo de modelos (`SE-608`), un plan debe tener tres capas, porque cada una ve lo que las otras no:

- **Calidad de entrada**: comprueba rango, nulos, esquema y unidades de cada lote. Es inmediata y barata, y detecta las fallas más frecuentes (un campo en cero, una unidad cambiada).
- **Distribución**: compara las entradas y las salidas de una **ventana** con una referencia. Tarda horas o días en acumular datos y produce falsas alarmas.
- **Métrica con etiquetas**: mide el desempeño real, pero tarda el retraso de la etiqueta (siete días en el ejemplo de la clase).

El ejemplo de *Avisos-ML* usa PSI por característica sobre ventanas diarias de 5 000 observaciones, con umbral de 0,2 como ticket de baja urgencia, y una guarda de 10 puntos sobre la tasa de marcados por segmento. A cada capa se le asigna una acción: la calidad de entrada bloquea o degrada, la distribución abre un diagnóstico, la métrica con etiquetas puede disparar un reentrenamiento.

En procesamiento de flujos (`SE-362`), la ventana se define sobre el **tiempo del evento** (cuándo ocurrió el hecho), no sobre el tiempo de llegada, lo que obliga a tratar los datos tardíos: hay que decidir cuánto esperar antes de cerrar una ventana. Los tamaños y umbrales son decisiones que dependen del volumen y de la variable observada.

## Ejemplo

Cada día se toma la ventana de las últimas 5 000 observaciones de cada característica y se compara con la referencia de entrenamiento usando PSI. Si supera 0,2, se abre un ticket de baja urgencia con dueño del equipo de datos; el bloqueo inmediato queda para fallas de calidad de entrada. Plan de monitoreo de `SE-608`.

## Errores y confusiones comunes

- **Una ventana demasiado pequeña**: el ruido genera falsas alarmas continuas.
- **Una ventana demasiado grande**: la deriva se nota tarde.
- **Confundir tiempo del evento con tiempo de llegada** al agregar flujos.
- **Usar un solo tipo de comprobación**: cada capa ve lo que las otras no.

## Límites y cuándo no aplica

`SE-608` advierte que los umbrales son convenciones, no leyes: dependen del número de tramos, del tamaño de la ventana y de la naturaleza de la variable; hay que calibrarlos con datos propios, midiendo la tasa de falsas alarmas con ventanas sin deriva y la sensibilidad con derivas que importen. Una ventana no explica la causa de un cambio, solo lo señala.
