# Inversión de prioridad

[↑ Glosario](../../README.md) · [← Inventario físico / reservado / vendible](./inventario-fisico-reservado-vendible.md) · [Invitado →](./invitado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Situación en que una tarea de alta prioridad espera por una de menor mientras una intermedia se ejecuta.

Definición de trabajo de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md): Situación en la que una tarea de alta prioridad espera por una de menor prioridad que a su vez es desplazada por otra intermedia.

## Por qué importa

En [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), el tema «Inversión de prioridad» importa porque una tarea media puede retrasar a la alta si la baja retiene un recurso.

En [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), el tema «Inversión de prioridad» importa porque retrasa a la tarea más urgente sin que haya carga alta.

## Cómo funciona

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), en la sección «Inversión de prioridad»:

Una tarea de alta prioridad que necesita un recurso que tiene una de baja queda bloqueada. Si en ese momento una tarea de prioridad media, que no necesita el recurso, se libera, expulsa a la baja y la alta espera además todo el cómputo de la media: es la inversión de prioridad sin acotar. La herencia de prioridad hace que la tarea de baja ejecute con la prioridad de la alta mientras la bloquea, de modo que la media no puede expulsarla y el bloqueo se acota a la sección crítica. Sha, Rajkumar y Lehoczky formalizaron estos protocolos.

## Ejemplo

Caso medido en la sección «La inversión de prioridad y la herencia» de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

Tres tareas: H (alta; 2 ms de trabajo y necesita un mutex al empezar), M (media; 8 ms, no usa el mutex) y L (baja; toma el mutex en t = 0 y lo retiene 6 ms de cómputo, más 2 ms después). H se libera en t = 1 ms. M se libera en un instante variable entre 2 y 10 ms. Se simula en pasos de 0,1 ms con y sin herencia de prioridad y se mide el tiempo de respuesta de H.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una tarea importante se retrasa tras añadir un mutex** — causa: inversión de prioridad. Corrección: activar herencia o techo de prioridad y acotar la sección crítica. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si en ese momento una tarea de prioridad media, que no necesita el recurso, se libera, expulsa a la baja y la alta espera además todo el cómputo de la media: es la inversión de prioridad sin acotar. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Tarea](../t/tarea.md), [Herencia de prioridad](../h/herencia-de-prioridad.md), [Peor caso de ejecución](../p/peor-caso-de-ejecucion.md), [Plazo](../p/plazo.md), [Prioridad fija](../p/prioridad-fija.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Joseph y Pandya, «Finding response times in a real-time system» (The Computer Journal, 1986)](https://doi.org/10.1093/comjnl/29.5.390) — cálculo exacto del tiempo de respuesta; autoridad: The Computer Journal.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia y techo de prioridad; autoridad: IEEE Transactions on Computers.
- [Audsley et al., «Applying new scheduling theory to static priority pre-emptive scheduling» (Software Engineering Journal, 1993)](https://doi.org/10.1049/sej.1993.0034) — análisis con bloqueo y jitter; autoridad: Software Engineering Journal.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — planificación de tiempo real en sistemas embebidos; autoridad: autores del libro (UC Berkeley).

---

[↑ Glosario](../../README.md) · [← Inventario físico / reservado / vendible](./inventario-fisico-reservado-vendible.md) · [Invitado →](./invitado.md)
