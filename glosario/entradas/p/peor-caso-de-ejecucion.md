# Peor caso de ejecución

[↑ Glosario](../../README.md) · [← Peor caso](./peor-caso.md) · [Percentil →](./percentil.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Tiempo de ejecución en el peor caso de una tarea, sin interferencias.

Definición de trabajo de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md): Cota superior del tiempo de cómputo de una tarea sobre todas las entradas y estados posibles.

## Por qué importa

En [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), el tema «WCET» importa porque es el insumo más difícil de obtener.

## Cómo funciona

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

El tiempo de cómputo del análisis es el peor caso (WCET), no el medio. Lo obtienen el análisis estático y la medición con entradas extremas, y ambos tienen incertidumbre: caches, ramas poco frecuentes, esperas de periféricos. Cuando el tiempo varía y se usa la media, un plazo se incumple con una frecuencia que depende de la variabilidad. Si un trabajo se pasa de su periodo, retrasa al siguiente y la sobrecarga se encadena. Por eso la utilización media no basta: importa la cola de la distribución.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El tiempo de cómputo del análisis es el peor caso (WCET), no el medio. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Peor caso](./peor-caso.md), [Cota](../c/cota.md), [Estado](../e/estado.md), [Interferencia](../i/interferencia.md), [Herencia de prioridad](../h/herencia-de-prioridad.md), [Inversión de prioridad](../i/inversion-de-prioridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «WCET».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Joseph y Pandya, «Finding response times in a real-time system» (The Computer Journal, 1986)](https://doi.org/10.1093/comjnl/29.5.390) — cálculo exacto del tiempo de respuesta; autoridad: The Computer Journal.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia y techo de prioridad; autoridad: IEEE Transactions on Computers.
- [Audsley et al., «Applying new scheduling theory to static priority pre-emptive scheduling» (Software Engineering Journal, 1993)](https://doi.org/10.1049/sej.1993.0034) — análisis con bloqueo y jitter; autoridad: Software Engineering Journal.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — planificación de tiempo real en sistemas embebidos; autoridad: autores del libro (UC Berkeley).

---

[↑ Glosario](../../README.md) · [← Peor caso](./peor-caso.md) · [Percentil →](./percentil.md)
