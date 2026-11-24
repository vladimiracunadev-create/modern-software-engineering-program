# Estabilidad de segmentos

## Definición

La **estabilidad de segmentos** es el grado en que un agrupamiento se reproduce al repetirlo con otra semilla o con otra submuestra de los mismos datos. Es el sentido de `SE-126` (segmentación, mercado y alternativas existentes). Es una prueba de reproducibilidad del análisis, no una prueba de que los grupos existan en el mundo.

## Por qué importa

Cambia si una segmentación puede usarse para decidir. Un algoritmo de agrupamiento siempre devuelve grupos; que sean estables es necesario, pero no prueba que existan. Si los «segmentos» cambian cada vez que se vuelve a ejecutar el análisis, no se puede construir una oferta ni un canal sobre ellos.

## Cómo funciona

`SE-126` usa k-means como ejemplo. El algoritmo asigna cada punto al centro más cercano y recalcula los centros; el resultado depende de dónde empiecen. Si dos ejecuciones con semillas distintas devuelven la misma partición, el agrupamiento es estable. La medida se repite también con submuestras de los datos.

El matiz esencial es que la estabilidad se puede obtener sobre datos sin estructura: con ruido uniforme y cuatro grupos, el algoritmo devuelve particiones tan reproducibles como con datos que sí tienen grupos. Por eso la estabilidad se compara con la obtenida sobre ruido. Y aun así, que supere al ruido no demuestra que los grupos signifiquen algo para el negocio. Quien segmenta debe exigir además que los grupos difieran en comportamiento o necesidad y poder describir cómo se reconocería a una persona de cada segmento.

## Ejemplo

En la plataforma de entregas, el mapa de mercado conserva por segmento: criterio de definición, trabajos, contextos, resultados insatisfechos, tamaño como rango con método y supuestos, canal de acceso y alternativas con los trabajos que cubren. El contrato es que ningún segmento se declare sin decir cómo se reconocería a una persona de él, y que ninguna cifra de mercado se publique sin su rango.

## Errores y confusiones comunes

- **Los segmentos cambian al volver a ejecutar.** El agrupamiento es inestable o depende de la semilla; medir estabilidad entre semillas y submuestras y no usarlo si es baja.
- **Segmentos estables que nadie reconoce.** Estabilidad sobre ruido o sobre variables sin significado de negocio; comparar con ruido y exigir diferencias de comportamiento o necesidad.
- **Tomar la estabilidad como prueba de existencia.** Es condición necesaria, no suficiente.
- **Elegir k sin justificación.** Cambia la partición y su estabilidad.

## Límites y cuándo no aplica

La estabilidad es una propiedad del análisis sobre unos datos concretos; no dice nada sobre otro periodo o mercado. Los experimentos de `SE-126` usan datos sintéticos y no demuestran que los segmentos de un mercado real sean estables. Con muestras muy pequeñas, la estabilidad entre submuestras es poco informativa.
