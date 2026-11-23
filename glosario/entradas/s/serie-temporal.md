# Serie temporal

[↑ Glosario](../../README.md) · [← Serialización](./serializacion.md) · [Serverless →](./serverless.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Secuencia de valores de una métrica con un nombre y un conjunto único de etiquetas.

Definición de trabajo de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md).

## Por qué importa

La clase donde se define, [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), existe con este propósito: la clase existe para que diseñes métricas que se puedan agregar, consultar y pagar: para que elijas el tipo correcto (contador, indicador o histograma), para que calcules cuántas series crea una dimensión antes de añadirla y para que sepas qué reconstruye un muestreo periódico y qué se le escapa.

## Cómo funciona

[SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo revisa las métricas de la API. El catálogo queda así: `entregas_recibidas_total` (contador) con endpoint, estado y región (45 series), `entregas_duracion_segundos` (histograma) con endpoint y estado (15 series × 14 cubetas = 210) y cubetas finas alrededor de 0,3 s, `entregas_en_cola` (indicador) sin etiquetas y `entregas_pico_cola` (máximo por intervalo) para ver picos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)) son:

- **El almacén de métricas se queda sin memoria** — causa: etiqueta con valores abiertos. Corrección: presupuestar series y probar el número en integración.
- **El contador cae a cero tras un despliegue** — causa: reinicio del proceso. Corrección: consultar incrementos con detección de reinicios.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos, salvo la memoria por serie, que es una medición de CPython.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Etiqueta](../e/etiqueta.md), [Métrica](../m/metrica.md), [Secuencia](./secuencia.md), [Cardinalidad](../c/cardinalidad.md), [Contador](../c/contador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Prometheus: modelo de datos](https://prometheus.io/docs/concepts/data_model/) — series por nombre y etiquetas; autoridad: documentación del proyecto Prometheus.
- [Prometheus: tipos de métricas](https://prometheus.io/docs/concepts/metric_types/) — contador, indicador, histograma y resumen; autoridad: documentación del proyecto Prometheus.
- [Prometheus: nombres y etiquetas](https://prometheus.io/docs/practices/naming/) — unidades y cardinalidad; autoridad: documentación del proyecto Prometheus.
- [Prometheus: histogramas y resúmenes](https://prometheus.io/docs/practices/histograms/) — estimación de cuantiles por cubeta; autoridad: documentación del proyecto Prometheus.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — importancia de la latencia de cola; autoridad: Communications of the ACM, 2013.

---

[↑ Glosario](../../README.md) · [← Serialización](./serializacion.md) · [Serverless →](./serverless.md)
