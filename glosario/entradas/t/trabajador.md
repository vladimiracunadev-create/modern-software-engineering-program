# Trabajador

[↑ Glosario](../../README.md) · [← Tóxico](./toxico.md) · [Trabajo →](./trabajo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Un **trabajador** (*worker*) es un proceso o hilo que toma trabajos de una cola y los ejecuta. Es el sentido de [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) (schedulers, workers y trabajos por lotes) y de [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (jobs, colas y procesamiento diferido). [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md) (orquestador-trabajadores y evaluador-optimizador) le da un sentido propio en sistemas de agentes: un componente con contexto y herramientas mínimas que resuelve una subtarea. En ambos, el trabajador hace la unidad de trabajo que otro le asigna.

## Por qué importa

Separa *recibir* una petición de *ejecutarla*: la petición responde rápido y el trabajo pesado ocurre aparte. Pero introduce una pregunta de fiabilidad: ¿qué pasa si el trabajador cae a mitad de un trabajo? [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) responde con el tiempo de visibilidad.

## Cómo funciona

[SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md): una cola guarda trabajos pendientes. Cuando un trabajador toma uno, **no lo borra**: lo oculta durante un **tiempo de visibilidad** y lo borra al confirmar. Si el trabajador cae, el tiempo vence y el trabajo reaparece para otro. Así no se pierde trabajo ante caídas.

La condición crítica: el tiempo de visibilidad debe superar la duración máxima razonable de un trabajo. Si es menor, el trabajo reaparece mientras el primer trabajador aún lo ejecuta, y se duplica sin que nadie haya caído. Por eso el efecto debe ser idempotente.

En [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), un trabajador de agentes recibe del orquestador una subtarea con el contexto y las herramientas mínimas necesarias; esto limita su radio de acción y facilita evaluar su resultado.

## Ejemplo

La plataforma de [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) encola un trabajo de calificación por entrega mediante outbox ([SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md)). El trabajo tiene identificador, estados consultables en `/trabajos/{id}`, plazo máximo de 10 minutos, tres intentos con retroceso y jitter, y una cola de muertos con alerta cuando crece. El manejador registra la nota con restricción única por identificador de trabajo, de modo que una repetición no duplica. Se dimensiona con la tasa de llegada λ, la de servicio μ y un objetivo de utilización máxima de 0,7 en el cierre de plazo.

## Errores y confusiones comunes

- **Un tiempo de visibilidad menor que la duración del trabajo,** que causa duplicados sin caída.
- **Confirmar el trabajo antes de terminarlo:** se pierde si cae.
- **Efectos no idempotentes en el manejador.**
- **Confundirlo con un hilo del servidor web** o con un trabajador de agentes: el contexto cambia.

## Límites y cuándo no aplica

Para tareas rápidas que el usuario espera, una cola añade complejidad innecesaria. El tamaño del grupo de trabajadores sigue las leyes de colas (utilización alta dispara la espera). Un trabajador envenenado por un trabajo que siempre falla requiere una cola de muertos.

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

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Discord](../../../casos/exito/discord.md), [Cloudflare](../../../casos/exito/cloudflare.md).

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
