# Estabilidad de segmentos

[↑ Glosario](../../README.md) · [← Estabilidad](./estabilidad.md) · [Estadísticas por grupo →](./estadisticas-por-grupo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

La **estabilidad de segmentos** es el grado en que un agrupamiento se reproduce al repetirlo con otra semilla o con otra submuestra de los mismos datos. Es el sentido de [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) (segmentación, mercado y alternativas existentes). Es una prueba de reproducibilidad del análisis, no una prueba de que los grupos existan en el mundo.

## Por qué importa

Cambia si una segmentación puede usarse para decidir. Un algoritmo de agrupamiento siempre devuelve grupos; que sean estables es necesario, pero no prueba que existan. Si los «segmentos» cambian cada vez que se vuelve a ejecutar el análisis, no se puede construir una oferta ni un canal sobre ellos.

## Cómo funciona

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) usa k-means como ejemplo. El algoritmo asigna cada punto al centro más cercano y recalcula los centros; el resultado depende de dónde empiecen. Si dos ejecuciones con semillas distintas devuelven la misma partición, el agrupamiento es estable. La medida se repite también con submuestras de los datos.

El matiz esencial es que la estabilidad se puede obtener sobre datos sin estructura: con ruido uniforme y cuatro grupos, el algoritmo devuelve particiones tan reproducibles como con datos que sí tienen grupos. Por eso la estabilidad se compara con la obtenida sobre ruido. Y aun así, que supere al ruido no demuestra que los grupos signifiquen algo para el negocio. Quien segmenta debe exigir además que los grupos difieran en comportamiento o necesidad y poder describir cómo se reconocería a una persona de cada segmento.

## Ejemplo

En la plataforma de entregas, el mapa de mercado conserva por segmento: criterio de definición, trabajos, contextos, resultados insatisfechos, tamaño como rango con método y supuestos, canal de acceso y alternativas con los trabajos que cubren. El contrato es que ningún segmento se declare sin decir cómo se reconocería a una persona de él, y que ninguna cifra de mercado se publique sin su rango.

## Errores y confusiones comunes

- **Los segmentos cambian al volver a ejecutar.** El agrupamiento es inestable o depende de la semilla; medir estabilidad entre semillas y submuestras y no usarlo si es baja.
- **Segmentos estables que nadie reconoce.** Estabilidad sobre ruido o sobre variables sin significado de negocio; comparar con ruido y exigir diferencias de comportamiento o necesidad.
- **Tomar la estabilidad como prueba de existencia.** Es condición necesaria, no suficiente.
- **Elegir k sin justificación.** Cambia la partición y su estabilidad.

## Límites y cuándo no aplica

La estabilidad es una propiedad del análisis sobre unos datos concretos; no dice nada sobre otro periodo o mercado. Los experimentos de [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) usan datos sintéticos y no demuestran que los segmentos de un mercado real sean estables. Con muestras muy pequeñas, la estabilidad entre submuestras es poco informativa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Semilla](../s/semilla.md), [Alternativas existentes](../a/alternativas-existentes.md), [Segmentación por necesidad](../s/segmentacion-por-necesidad.md), [Segmento inicial](../s/segmento-inicial.md), [Tamaño del mercado](../t/tamano-del-mercado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ben-Hur, Elisseeff y Guyon (2002): A stability based method for discovering structure in clustered data](https://psb.stanford.edu/psb-online/proceedings/psb02/benhur.pdf) — estabilidad de agrupamientos ante submuestras; autoridad: Pacific Symposium on Biocomputing.
- [Strategyn: Outcome-Driven Innovation](https://strategyn.com/outcome-driven-innovation-process/) — segmentación por necesidades insatisfechas; autoridad: Strategyn (fuente del autor del método).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — rangos e incertidumbre en la estimación; autoridad: Hubbard Decision Research.
- [Strategyzer: Value Proposition Canvas](https://www.strategyzer.com/library/the-value-proposition-canvas) — ajuste entre propuesta y perfil de cliente; autoridad: Strategyzer.
- [Know Your Customers' «Jobs to Be Done» (Harvard Business Review, 2016)](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done) — trabajos como base de la competencia; autoridad: Harvard Business Review (artículo parcialmente de pago).

---

[↑ Glosario](../../README.md) · [← Estabilidad](./estabilidad.md) · [Estadísticas por grupo →](./estadisticas-por-grupo.md)
