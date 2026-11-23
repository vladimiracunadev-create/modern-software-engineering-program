# Trabajador

[↑ Glosario](../../README.md) · [← Tóxico](./toxico.md) · [Trabajo →](./trabajo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Proceso que toma trabajos de una cola y los ejecuta.

Definición de trabajo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md): Componente con contexto y herramientas mínimas que resuelve una subtarea.
- En [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md): Proceso o hilo que toma trabajos de una cola y los ejecuta.

## Por qué importa

En [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), el tema «Cola y visibilidad» importa porque el tiempo de visibilidad convierte la caída de un trabajador en una repetición controlada en vez de en una pérdida.

## Cómo funciona

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

Una cola guarda trabajos pendientes. Cuando un trabajador toma uno no lo borra: lo oculta durante un **tiempo de visibilidad** y lo borra al confirmar. Si el trabajador cae, el tiempo vence y el trabajo reaparece para otro. Es la forma de no perder trabajo ante caídas. El tiempo de visibilidad debe superar la duración máxima razonable de un trabajo: si es menor, el trabajo reaparece mientras el primer trabajador aún lo ejecuta y se duplica sin que nadie caiga.

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Ejemplo profesional»):

La plataforma encola un trabajo de calificación por entrega mediante outbox (`SE-241`). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, un plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El handler registra la nota con restricción única por identificador de trabajo. Se dimensiona con λ, μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo. Compara con el original en tres casos: un trabajador que se reinicia, la hora del cierre de plazo y un archivo corrupto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md)) son:

- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo.
- **Un trabajo se ejecuta dos veces sin caídas** — causa: tiempo de visibilidad menor que la duración del trabajo. Corrección: ajustar la visibilidad al máximo razonable y renovarla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando un trabajador toma uno no lo borra: lo oculta durante un **tiempo de visibilidad** y lo borra al confirmar. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Contextos](../c/contextos.md), [Herramientas](../h/herramientas.md), [Hilo](../h/hilo.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-591 — Orquestador-trabajadores y evaluador-optimizador](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «worker».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Book: Handling Overload](https://sre.google/sre-book/handling-overload/) — sobrecarga, rechazo y degradación; autoridad: Google.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos con retroceso; autoridad: Amazon Builders' Library.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — tablas y transacciones del experimento; autoridad: Python Software Foundation.
- [Python: queue](https://docs.python.org/3/library/queue.html) — colas de la biblioteca estándar; autoridad: Python Software Foundation.
- [POSIX: crontab](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html) — formato de las entradas periódicas; autoridad: The Open Group.

---

[↑ Glosario](../../README.md) · [← Tóxico](./toxico.md) · [Trabajo →](./trabajo.md)
