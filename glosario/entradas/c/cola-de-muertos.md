# Cola de muertos

[↑ Glosario](../../README.md) · [← Cola de mensajes fallidos](./cola-de-mensajes-fallidos.md) · [Cola de radio →](./cola-de-radio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Cola donde se apartan los trabajos que agotaron sus intentos para que una persona los revise.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md): Lugar donde se aparta un trabajo que agotó sus reintentos para su revisión.

## Por qué importa

En [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), el tema «Reintentos y cola de muertos» importa porque un trabajo que no se arregla repitiendo debe apartarse tras un número de intentos.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Un trabajo puede fallar por razones transitorias (un servicio no disponible) o permanentes (un archivo corrupto). Si se reintenta sin límite, el permanente ocupa un trabajador para siempre. La práctica es limitar los intentos (tres, por ejemplo), esperar entre ellos con retroceso y, agotados, mover el trabajo a una **cola de muertos** que una persona revisa. Esa cola es una señal operativa: su crecimiento debe alertar.

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Ejemplo profesional»):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los trabajos buenos esperan detrás de uno que falla** — causa: reintento sin límite al frente. Corrección: intentos limitados y cola de muertos. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))
- **La cola deja de avanzar** — causa: un trabajo venenoso se reintenta sin límite. Corrección: máximo de intentos y cola de muertos. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Tres políticas: reintentar sin límite devolviendo el trabajo al frente de la cola, tres intentos y cola de muertos, y tres intentos con reintento al final de la cola. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Reintentos](../r/reintentos.md), [Revisión](../r/revision.md), [Trabajo](../t/trabajo.md), [Backpressure](../b/backpressure.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Handler idempotente](../h/handler-idempotente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — patrón de cola de muertos; autoridad: documentación de AWS.
- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, rechazo y degradación; autoridad: Google.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos con retroceso; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — tablas y transacciones del experimento; autoridad: Python Software Foundation.
- [Python: queue](https://docs.python.org/3/library/queue.html) — colas de la biblioteca estándar; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Cola de mensajes fallidos](./cola-de-mensajes-fallidos.md) · [Cola de radio →](./cola-de-radio.md)
