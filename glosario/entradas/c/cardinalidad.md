# Cardinalidad

[↑ Glosario](../../README.md) · [← Caracterización](./caracterizacion.md) · [Carga analítica →](./carga-analitica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Número de valores distintos de una etiqueta, o número de series que resulta de combinar varias.

Definición de trabajo de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md): Número de instancias de una entidad que pueden relacionarse con una instancia de otra.

## Por qué importa

En [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), el tema «Dimensiones y cardinalidad» importa porque cada etiqueta multiplica las series.

## Cómo funciona

Según [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md):

El número de series de una métrica es el producto de las cardinalidades de sus etiquetas, no la suma. Con endpoint (5), estado (3) y región (3), son 45. Añadir curso (30) multiplica por 30 y deja 1 350; añadir cliente (40) deja 54 000; añadir un identificador de persona con 20 000 valores deja 1 080 millones. La memoria es proporcional: con 429 bytes por serie en la medición, 54 000 series son unos 23 MB y 1 080 millones serían 463 GB. Cada serie existe aunque nadie la consulte, y el coste aparece como lentitud de las consultas, memoria y, al final, series descartadas. La respuesta de diseño no es evitar dimensiones, sino presupuestarlas: cada métrica declara su máximo de series y una prueba lo comprueba en integración.

Según [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md):

Mientras sean pocos y acotados, sí; el problema es que «pocos» crece sin que nadie lo decida. Una etiqueta con valores que dependen de datos de entrada es una fuga de cardinalidad en espera. Si necesitas el detalle por persona, es un evento, no una métrica.

## Ejemplo

Ejemplo de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) (sección «Preguntas frecuentes»):

Mientras sean pocos y acotados, sí; el problema es que «pocos» crece sin que nadie lo decida. Una etiqueta con valores que dependen de datos de entrada es una fuga de cardinalidad en espera. Si necesitas el detalle por persona, es un evento, no una métrica.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md)) son:

- **El almacén de métricas se queda sin memoria** — causa: etiqueta con valores abiertos. Corrección: presupuestar series y probar el número en integración.
- **El contador cae a cero tras un despliegue** — causa: reinicio del proceso. Corrección: consultar incrementos con detección de reinicios.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El número de series de una métrica es el producto de las cardinalidades de sus etiquetas, no la suma. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))
- Una etiqueta con valores que dependen de datos de entrada es una fuga de cardinalidad en espera. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Etiqueta](../e/etiqueta.md), [Instancia](../i/instancia.md), [Valor](../v/valor.md), [Anomalía de actualización](../a/anomalia-de-actualizacion.md), [Clave sustituta](./clave-sustituta.md), [Contador](./contador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-160](../../../classes/part-13-especificaciones-contratos-y-modelos/se-160-modelos-estructurales-conductuales-y-de-informacion/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-368](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-368-warehouse-lake-lakehouse-y-formatos-columnares/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Prometheus: nombres y etiquetas](https://prometheus.io/docs/practices/naming/) — unidades y cardinalidad; autoridad: documentación del proyecto Prometheus.
- [Prometheus: modelo de datos](https://prometheus.io/docs/concepts/data_model/) — series por nombre y etiquetas; autoridad: documentación del proyecto Prometheus.
- [Prometheus: tipos de métricas](https://prometheus.io/docs/concepts/metric_types/) — contador, indicador, histograma y resumen; autoridad: documentación del proyecto Prometheus.
- [Prometheus: histogramas y resúmenes](https://prometheus.io/docs/practices/histograms/) — estimación de cuantiles por cubeta; autoridad: documentación del proyecto Prometheus.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — importancia de la latencia de cola; autoridad: Communications of the ACM, 2013.

---

[↑ Glosario](../../README.md) · [← Caracterización](./caracterizacion.md) · [Carga analítica →](./carga-analitica.md)
