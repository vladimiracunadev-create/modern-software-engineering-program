# Trabajo venenoso

[↑ Glosario](../../README.md) · [← Trabajo en curso](./trabajo-en-curso.md) · [Trabajos por hacer →](./trabajos-por-hacer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Trabajo que falla en cada intento por una causa que reintentar no resuelve.

Definición de trabajo de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

## Por qué importa

En [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), el tema «Fallos y trabajos venenosos» importa porque un trabajo imposible no debe bloquear a los posibles.

## Cómo funciona

Según [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

**Cómo leer la figura.** Cada barra son los 1 000 trabajos de una política, divididos en completados (turquesa), en cola de muertos (dorado) y sin procesar (coral). Mira la barra de arriba, casi toda coral: un trabajo venenoso al frente de la cola bloquea al resto; la de abajo es la única sin trabajos sin procesar. **Dónde deja de valer:** los porcentajes (3 % y 10 %) son supuestos y el presupuesto de intentos es artificial; en una cola real el efecto depende del tamaño de la cola y de la concurrencia. Lo que generaliza es el orden: sin límite de intentos y sin un lugar donde apartar, un solo trabajo puede monopolizar el sistema.

Según [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

Reproduce el fallo clásico de la clase: **un trabajo venenoso que bloquea la cola**. Usa la política que reintenta al frente sin límite.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

`notas servir` programa tres trabajos: la sincronización cada 60 s con política de **omitir si sigue activa** y un límite de 50 s por ejecución, la exportación nocturna con un candado de archivo para que solo una instancia la ejecute, y un lote de revisiones con tamaño 200. Las consultas a la base se reparten con ocho hilos y los informes con cuatro procesos, que arrancan una vez y se reutilizan.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La cola deja de avanzar** — causa: un trabajo venenoso se reintenta sin límite. Corrección: máximo de intentos y cola de muertos. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Mira la barra de arriba, casi toda coral: un trabajo venenoso al frente de la cola bloquea al resto; la de abajo es la única sin trabajos sin procesar. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](./trabajo.md), [Cola de muertos](../c/cola-de-muertos.md), [Lote](../l/lote.md), [Planificador](../p/planificador.md), [Política de solape](../p/politica-de-solape.md), [Trabajador](./trabajador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: crontab](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html) — formato de las entradas periódicas; autoridad: The Open Group.
- [Google SRE: Distributed Periodic Scheduling with Cron](https://sre.google/sre-book/distributed-periodic-scheduling/) — fallos de la planificación periódica; autoridad: Google.
- [Python: `concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — pools de hilos y procesos; autoridad: documentación de Python.
- [Python: `multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods) — métodos de inicio de procesos; autoridad: documentación de Python.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — patrón de cola de muertos; autoridad: documentación de AWS.

---

[↑ Glosario](../../README.md) · [← Trabajo en curso](./trabajo-en-curso.md) · [Trabajos por hacer →](./trabajos-por-hacer.md)
