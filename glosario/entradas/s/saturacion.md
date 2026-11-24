# Saturación

[↑ Glosario](../../README.md) · [← Sandbox](./sandbox.md) · [SBOM →](./sbom.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

La **saturación** es el estado en que la utilización se acerca a 1 y la cola crece sin que aumente el trabajo útil ([SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)).

## Por qué importa

Explica por qué la latencia se dispara con una utilización que parece «razonable»: los sistemas con colas no degradan de forma lineal. Planificar con la media y no con el objetivo de percentil lleva a operar demasiado cerca del borde.

## Cómo funciona

Cuando la tasa de llegada se acerca a la capacidad, cualquier ráfaga forma cola, y la cola se vacía lentamente porque casi no hay capacidad sobrante. El tiempo de espera crece de forma no lineal al acercarse la utilización a 1. La fórmula de Pollaczek–Khinchine relaciona la espera con la variabilidad del servicio: un servicio más variable que el exponencial espera más de lo que predice la fórmula simple.

## Ejemplo

Un servicio con utilización del 70 % responde con holgura; a 95 % la cola ya es larga con ráfagas ordinarias. (Ilustración cualitativa; los experimentos de [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) son sobre la API de entregas.)

## Errores y confusiones comunes

- **La latencia se dispara con una utilización «razonable».** Se planificó con la media; calcular la utilización máxima desde el objetivo de percentil.
- **La espera es mayor de lo que predice la fórmula.** El servicio es más variable que el exponencial; medir cv² y usar Pollaczek–Khinchine.

## Límites y cuándo no aplica

Los modelos de cola suponen llegadas y servicios con ciertas distribuciones; en la práctica se miden. Más allá de la saturación, reintentos y colas pueden sostener el problema (fallo metaestable).

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Trabajo](../t/trabajo.md), [Utilización](../u/utilizacion.md), [Coeficiente de variación](../c/coeficiente-de-variacion.md), [Latencia de cola](../l/latencia-de-cola.md), [Ley de Little](../l/ley-de-little.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (36 clases más lo mencionan; las que más):

[SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Little, «A proof for the queuing formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) — ley de Little; autoridad: artículo original, Operations Research 1961.
- [Harchol-Balter, «Performance Modeling and Design of Computer Systems»](https://www.cs.cmu.edu/~harchol/PerformanceModeling/book.html) — colas M/M/1, M/G/1 y Pollaczek–Khinchine; autoridad: autora del libro.
- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — latencia de cola en sistemas distribuidos; autoridad: Communications of the ACM, 2013.
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de oro y distribuciones; autoridad: Google, libro de ingeniería de confiabilidad.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media y cuantiles usados en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Sandbox](./sandbox.md) · [SBOM →](./sbom.md)
