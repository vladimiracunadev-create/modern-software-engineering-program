# Inversión de prioridad

[↑ Glosario](../../README.md) · [← Inventario físico / reservado / vendible](./inventario-fisico-reservado-vendible.md) · [Invitado →](./invitado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

La **inversión de prioridad** es la situación en que una tarea de alta prioridad espera por una de menor prioridad que, a su vez, es desplazada por otra de prioridad intermedia. Es el sentido de [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sistemas de tiempo real y deadlines) y [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) (RTOS y planificación). No es que la alta espere un poco: es que su espera depende de una tarea que no es la más urgente ni la que la bloquea.

## Por qué importa

Retrasa a la tarea más urgente sin que haya carga alta: el sistema puede parecer holgado y aun así incumplir un plazo. Una tarea media, que ni siquiera usa el recurso, puede hacer fallar a la alta.

## Cómo funciona

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) describe la secuencia:

1. La tarea de baja prioridad L toma un recurso (un mutex).
2. La de alta prioridad H se libera, necesita el recurso y queda bloqueada.
3. Una tarea de prioridad media M, que no necesita el recurso, se libera y **expulsa a L** (tiene más prioridad que L).
4. H espera además todo el cómputo de M. Esta es la inversión *sin acotar*.

Remedio: **herencia de prioridad.** Mientras L bloquea a H, L ejecuta con la prioridad de H, de modo que M no puede expulsarla y el bloqueo se acota a la sección crítica de L. Sha, Rajkumar y Lehoczky formalizaron estos protocolos, según cita la clase.

## Ejemplo

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) plantea tres tareas: H (alta; 2 ms de trabajo y necesita un mutex al empezar), M (media; 8 ms, no usa el mutex) y L (baja; toma el mutex en t = 0 y lo retiene 6 ms de cómputo, más 2 ms después). H se libera en t = 1 ms; M, en un instante variable entre 2 y 10 ms. Sin herencia, si M llega mientras L tiene el mutex, H espera además los 8 ms de M. Con herencia, L corre con la prioridad de H y M no la interrumpe, de modo que la espera de H queda acotada a lo que le quede a L en su sección crítica.

## Errores y confusiones comunes

- **Tratar la espera de H como «solo» el tiempo de L:** M puede añadirse.
- **Confundirla con el interbloqueo:** aquí el sistema avanza, pero tarde.
- **Creer que subir prioridades a todo evita el problema:** pierde el sentido de la prioridad.
- **No probarla con la tarea media en el peor instante.**

## Límites y cuándo no aplica

La herencia de prioridad acota la inversión, no la elimina: H sigue esperando la sección crítica de L. Con un solo núcleo y recursos sin compartir, el fenómeno no se da. Las duraciones del ejemplo son de la clase, no de un sistema real.

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
