# Estabilidad de segmentos

[↑ Glosario](../../README.md) · [← Estabilidad](./estabilidad.md) · [Estadísticas por grupo →](./estadisticas-por-grupo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Grado en que un agrupamiento se reproduce al repetirlo con otra semilla o con otra submuestra de los mismos datos.

Definición de trabajo de [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).

## Por qué importa

En [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), el tema «Estabilidad de segmentos» importa porque un algoritmo siempre devuelve grupos; que sean estables es necesario, pero no prueba que existan.

## Cómo funciona

Según [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), en la sección «Estabilidad de segmentos»:

K-means asigna cada punto al centro más cercano y recalcula centros; el resultado depende de dónde empiecen. Si dos ejecuciones con semillas distintas devuelven la misma partición, el agrupamiento es estable. Sin embargo, la estabilidad se puede obtener sobre datos sin estructura: con ruido uniforme y cuatro grupos el algoritmo devuelve particiones tan reproducibles como con datos que sí tienen grupos. La estabilidad se compara con la obtenida sobre ruido; y aun así, los grupos deben distinguirse por comportamiento, ser identificables y tener sentido para el equipo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md):

En la plataforma de entregas, el mapa conserva por segmento: criterio de definición, trabajos, contextos, resultados insatisfechos, tamaño como rango con método y supuestos, canal de acceso y alternativas con los trabajos que cubren. El contrato es que ningún segmento se declare sin decir cómo se reconocería a una persona de él y que ninguna cifra de mercado se publique sin su rango.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md)) son:

- **Los «segmentos» cambian cuando se vuelve a ejecutar el análisis** — causa: el agrupamiento es inestable o depende de la semilla. Corrección: medir estabilidad entre semillas y submuestras y no usar el agrupamiento si es bajo.
- **Los segmentos son estables pero nadie los reconoce** — causa: estabilidad sobre ruido o variables sin significado de negocio. Corrección: comparar con ruido y exigir que los grupos difieran en comportamiento o necesidad.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-126 — Segmentación, mercado y alternativas existentes](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se segmentó ningún mercado real, los rangos son supuestos y el agrupamiento se hizo en dos dimensiones. La siguiente clase convierte el segmento y la hipótesis más sensible en prototipos y experimentos que reduzcan la incertidumbre.

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
