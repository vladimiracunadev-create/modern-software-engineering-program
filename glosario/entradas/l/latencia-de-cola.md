# Latencia de cola

[↑ Glosario](../../README.md) · [← Latencia](./latencia.md) · [Latencia de red →](./latencia-de-red.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md)

## Definición

Percentil alto de la latencia, como el p99.

Definición de trabajo de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md): Latencia de las peticiones más lentas, resumida con percentiles altos como el p99.
- En [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md): Latencia que no supera el p95 o el p99 de las peticiones.

## Por qué importa

En [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md), el tema «Latencia de cola» importa porque esperar a varias llamadas empeora el percentil alto.

## Cómo funciona

[SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

Ejemplo de [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) (sección «Caso conductor»):

*Avisos* evalúa separar su cálculo de avisos. Esta clase da el precio: más de mil veces una llamada en proceso, disponibilidad multiplicada, latencia de cola amplificada y un riesgo de acoplamiento por contrato. `SE-341` estudia qué se coloca entre los clientes y esos servicios (un BFF, un gateway, una malla) y cuánto de lo que prometen es evitable con una decisión más simple.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md)) son: El costo de HTTP es el de un servidor de la biblioteca estándar en la misma máquina; la cadena de servicios y la topología son simulaciones con parámetros del autor. No se midió ningún sistema de microservicios, ningún equipo ni el costo humano de operarlos. El siguiente paso, `SE-341`, estudia lo que se interpone entre los clientes y los servicios: el BFF, el gateway y la malla de servicios.

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
