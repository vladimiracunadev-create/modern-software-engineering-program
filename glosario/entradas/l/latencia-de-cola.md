# Latencia de cola

[↑ Glosario](../../README.md) · [← Latencia](./latencia.md) · [Latencia de red →](./latencia-de-red.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

La **latencia de cola** (*tail latency*) es la latencia de las peticiones más lentas, resumida con un percentil alto como el p99. [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (latencia, throughput, saturación y capacidad) la define así; [SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) la usa para los aceleradores: la latencia que no supera el p95 o el p99 de las peticiones. «Cola» alude a la cola derecha de la distribución de tiempos, no a una cola de espera.

## Por qué importa

El promedio oculta a quienes más sufren. Si el p99 es diez veces la mediana, una de cada cien peticiones es mucho más lenta, y en sistemas con muchas peticiones por persona esa fracción se alcanza pronto. Es lo que se compromete en un SLO de latencia, no el promedio.

## Cómo funciona

Una distribución de latencias suele tener una masa grande de peticiones rápidas y una cola larga de lentas (por esperas en cola, recolección de basura, reintentos, fallos de caché). Se resume con percentiles: p50 (mediana), p95, p99.

[SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (microservicios y sus costos reales) añade la **amplificación**: si una petición del usuario espera a varias llamadas internas, basta que una caiga en la cola para que toda la petición sea lenta. Con *n* llamadas independientes, la probabilidad de que al menos una supere su p99 es 1 − 0,99ⁿ; con 100 llamadas, ronda el 63 %. Por eso la latencia de cola de la petición completa empeora con cada servicio añadido, junto con la disponibilidad multiplicada.

## Ejemplo

*Avisos*, en [SE-340](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), evalúa separar el cálculo de avisos. La clase da el precio: más de mil veces una llamada en proceso, disponibilidad multiplicada, latencia de cola amplificada y un riesgo de acoplamiento por contrato. Ilustración numérica propia: una página que llama a 20 servicios con p99 de 200 ms cada uno tiene aproximadamente 18 % de probabilidad de que al menos una llamada pase de 200 ms.

## Errores y confusiones comunes

- **Reportar solo el promedio o la mediana.**
- **Promediar percentiles de varios servicios:** no se pueden combinar así.
- **Creer que los percentiles se suman:** el p99 de un flujo no es la suma de los p99 de sus pasos.
- **Confundirla con el tiempo en cola de espera:** la espera puede causarla, pero no es lo mismo.

## Límites y cuándo no aplica

El p99 solo describe bien con muchas observaciones; con pocas, es ruidoso. La cuenta de amplificación supone llamadas independientes y en paralelo; con dependencias correlacionadas (una causa común) el cálculo cambia. Para sistemas por lotes, donde importa el tiempo total y no cada petición, el percentil por petición es menos relevante.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-280](../../../classes/part-23-runtimes-y-plataformas-modernas/se-280-gpu-y-aceleradores-modelo-de-ejecucion/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Latencia](./latencia.md), [Percentil](../p/percentil.md), [Camino crítico](../c/camino-critico.md), [Contrato compatible](../c/contrato-compatible.md), [Lector tolerante](./lector-tolerante.md), [Ley de Amdahl](./ley-de-amdahl.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Dean y Barroso, «The tail at scale»](https://doi.org/10.1145/2408776.2408794) — latencia de cola en sistemas distribuidos; autoridad: Communications of the ACM, 2013.
- [Little, «A proof for the queuing formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) — ley de Little; autoridad: artículo original, Operations Research 1961.
- [Harchol-Balter, «Performance Modeling and Design of Computer Systems»](https://www.cs.cmu.edu/~harchol/PerformanceModeling/book.html) — colas M/M/1, M/G/1 y Pollaczek–Khinchine; autoridad: autora del libro.
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de oro y distribuciones; autoridad: Google, libro de ingeniería de confiabilidad.
- [Python: statistics](https://docs.python.org/3/library/statistics.html) — media y cuantiles usados en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Latencia](./latencia.md) · [Latencia de red →](./latencia-de-red.md)
