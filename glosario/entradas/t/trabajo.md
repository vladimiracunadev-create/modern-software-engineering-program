# Trabajo

[↑ Glosario](../../README.md) · [← Trabajador](./trabajador.md) · [Trabajo diferido →](./trabajo-diferido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Unidad de procesamiento diferido con identificador, estado y plazo.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

## Por qué importa

En [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), el tema «Reintentos y cola de muertos» importa porque un trabajo que no se arregla repitiendo debe apartarse tras un número de intentos.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Una cola guarda trabajos pendientes. Cuando un trabajador toma uno no lo borra: lo oculta durante un **tiempo de visibilidad** y lo borra al confirmar. Si el trabajador cae, el tiempo vence y el trabajo reaparece para otro. Es la forma de no perder trabajo ante caídas. El tiempo de visibilidad debe superar la duración máxima razonable de un trabajo: si es menor, el trabajo reaparece mientras el primer trabajador aún lo ejecuta y se duplica sin que nadie caiga.

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Ejemplo profesional»):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))
- **Un trabajo se ejecuta dos veces sin caídas** — causa: tiempo de visibilidad menor que la duración del trabajo. Corrección: ajustar la visibilidad al máximo razonable y renovarla. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))
- **Los trabajos buenos esperan detrás de uno que falla** — causa: reintento sin límite al frente. Corrección: intentos limitados y cola de muertos. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es la forma de no perder trabajo ante caídas. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))
- Con la política de reintento sin límite al frente de la cola, introduce 10 trabajos que siempre fallan entre 1 000. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Plazo](../p/plazo.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Handler idempotente](../h/handler-idempotente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (611 clases más lo mencionan; las que más):

[SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-517](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-517-mantenimiento-correctivo-adaptativo-y-perfectivo/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, rechazo y degradación; autoridad: Google.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos con retroceso; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — tablas y transacciones del experimento; autoridad: Python Software Foundation.
- [Python: queue](https://docs.python.org/3/library/queue.html) — colas de la biblioteca estándar; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Trabajador](./trabajador.md) · [Trabajo diferido →](./trabajo-diferido.md)
