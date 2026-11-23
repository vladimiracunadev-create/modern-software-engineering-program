# Coeficiente de variación

[↑ Glosario](../../README.md) · [← Código no previsto](./codigo-no-previsto.md) · [Cohesión →](./cohesion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Desviación estándar dividida por la media; su cuadrado mide la variabilidad relativa del servicio.

Definición de trabajo de [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md).

## Por qué importa

La clase donde se define, [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), existe con este propósito: la clase existe para que expliques con un modelo por qué la latencia crece tanto cuando un servidor se acerca a la saturación, para que distingas qué magnitudes se pueden sumar o promediar (rendimiento, concurrencia, tiempos medios) de las que no (percentiles), y para que planifiques la capacidad desde un objetivo de cola y no desde una utilización «razonable» heredada.

## Cómo funciona

Según [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md):

La fórmula M/M/1 supone un servicio exponencial, que tiene un coeficiente de variación al cuadrado (cv²) de 1. Los servicios reales pueden ser más regulares (un cálculo fijo) o mucho más irregulares (una consulta que a veces toca disco). La fórmula de **Pollaczek–Khinchine** para una cola M/G/1 dice que la espera media es proporcional a (1 + cv²)/2: con el mismo promedio de servicio y la misma utilización, la espera se duplica de servicio constante (cv² = 0) a exponencial (cv² = 1) y se multiplica por 13 con una mezcla de 95 % de peticiones rápidas y 5 % lentas. La variabilidad entra porque una petición larga bloquea a todas las que esperan detrás.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md):

El equipo recalcula la flota para el cierre. Parte del escenario de `SE-433`: p99 ≤ 1,5 s con 1 000 solicitudes por segundo. Supón, como dato hipotético de la plataforma y no como medición, que el servicio de listado tiene 50 ms de media y un cv² de 2,1 por una consulta con cursos grandes: con la fórmula de Pollaczek–Khinchine estimaría que a una utilización del 70 % el p99 se acerca a 1,5 s, y fijaría el 70 % como límite de planificación en lugar del 80 %.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)) son:

- **La latencia se dispara con una utilización «razonable»** — causa: se planificó con la media. Corrección: calcular la utilización máxima desde el objetivo de percentil.
- **La espera es mayor de lo que predice la fórmula** — causa: servicio más variable que el exponencial. Corrección: medir cv² y usar Pollaczek–Khinchine.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos en ambos sistemas. No se midió ningún servidor real; las llegadas de Poisson, los servicios exponencial, lognormal y bimodal, los ocho servidores y la fórmula de un solo servidor son modelos del autor, no hay dependencias ni ráfagas, y cerca del 100 % de utilización la simulación no alcanza el régimen estable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Desviación](../d/desviacion.md), [Servicio](../s/servicio.md), [Variabilidad](../v/variabilidad.md), [Latencia de cola](../l/latencia-de-cola.md), [Ley de Little](../l/ley-de-little.md), [Saturación](../s/saturacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md).

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

[↑ Glosario](../../README.md) · [← Código no previsto](./codigo-no-previsto.md) · [Cohesión →](./cohesion.md)
