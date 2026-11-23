# Contador

[↑ Glosario](../../README.md) · [← Consumidor idempotente](./consumidor-idempotente.md) · [Contención →](./contencion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Métrica que solo crece, salvo reinicios del proceso, y se consulta por su incremento.

Definición de trabajo de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md).

## Por qué importa

En [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), el tema «Contadores y reinicios» importa porque un contador reiniciado engaña a una resta simple.

## Cómo funciona

Según [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md):

Un **contador** solo crece (peticiones atendidas, errores) y vuelve a cero al reiniciarse el proceso; su valor absoluto no importa, sí su incremento en un intervalo, de ahí que se consulte como tasa. Un **indicador** (gauge) sube y baja y mide un estado instantáneo (conexiones abiertas, memoria usada, longitud de una cola); no se puede reconstruir lo que ocurrió entre dos lecturas. Un **histograma** cuenta observaciones en cubetas de límites fijos (≤ 100 ms, ≤ 250 ms…) y permite estimar percentiles y agregar entre instancias sumando contadores de cubeta. Un **resumen** calcula cuantiles en el proceso y es exacto allí, pero no se puede agregar entre procesos. El tipo importa porque define qué operaciones son válidas: sumar contadores de varios servidores es correcto; promediar sus p99 no lo es (`SE-436`).

Según [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo revisa las métricas de la API. El catálogo queda así: `entregas_recibidas_total` (contador) con endpoint, estado y región (45 series), `entregas_duracion_segundos` (histograma) con endpoint y estado (15 series × 14 cubetas = 210) y cubetas finas alrededor de 0,3 s, `entregas_en_cola` (indicador) sin etiquetas y `entregas_pico_cola` (máximo por intervalo) para ver picos. El curso y el cliente no se añaden como etiquetas: los diez clientes mayores tienen una métrica propia (10 series más) y el resto se consulta en los eventos de `SE-494`. Una prueba de integración arranca el servicio con datos sintéticos, cuenta las series que expone y falla si pasan de 500.

## Ejemplo

Ejemplo de [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) (sección «Ejemplo mínimo»):

El fragmento reconstruye el incremento de un contador con un reinicio. Antes de ejecutarlo, predice el resultado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El contador cae a cero tras un despliegue** — causa: reinicio del proceso. Corrección: consultar incrementos con detección de reinicios. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **contador** solo crece (peticiones atendidas, errores) y vuelve a cero al reiniciarse el proceso; su valor absoluto no importa, sí su incremento en un intervalo, de ahí que se consulte como tasa. ([SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica](../m/metrica.md), [Proceso](../p/proceso.md), [Cardinalidad](./cardinalidad.md), [Histograma](../h/histograma.md), [Indicador](../i/indicador.md), [Serie temporal](../s/serie-temporal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-495 — Métricas, dimensiones y cardinalidad](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (87 clases más lo mencionan; las que más):

[SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-272](../../../classes/part-22-embedded-iot-y-tiempo-real/se-272-identidad-de-dispositivo-y-gestion-de-claves/README.md), [SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-017](../../../classes/part-01-computadores-y-representacion-de-informacion/se-017-cpu-instrucciones-registros-y-ciclos-de-ejecucion/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Prometheus: tipos de métricas](https://prometheus.io/docs/concepts/metric_types/) — contador, indicador, histograma y resumen; autoridad: documentación del proyecto Prometheus.
- [Prometheus: modelo de datos](https://prometheus.io/docs/concepts/data_model/) — series por nombre y etiquetas; autoridad: documentación del proyecto Prometheus.
- [Prometheus: nombres y etiquetas](https://prometheus.io/docs/practices/naming/) — unidades y cardinalidad; autoridad: documentación del proyecto Prometheus.
- [Prometheus: histogramas y resúmenes](https://prometheus.io/docs/practices/histograms/) — estimación de cuantiles por cubeta; autoridad: documentación del proyecto Prometheus.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — importancia de la latencia de cola; autoridad: Communications of the ACM, 2013.

---

[↑ Glosario](../../README.md) · [← Consumidor idempotente](./consumidor-idempotente.md) · [Contención →](./contencion.md)
