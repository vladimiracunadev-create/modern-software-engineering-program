# Política de solape

[↑ Glosario](../../README.md) · [← Política de seguridad de contenido](./politica-de-seguridad-de-contenido.md) · [Política metodológica →](./politica-metodologica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Decisión sobre qué hacer cuando una ejecución arranca mientras la anterior sigue activa.

Definición de trabajo de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

## Por qué importa

La clase donde se define, [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), existe con este propósito: la clase existe para decidir cómo se programa, se reparte y se acota el trabajo que un servicio hace por su cuenta —una ejecución periódica, un grupo de trabajadores, una cola de lotes— de modo que un trabajo lento no se pise a sí mismo, un trabajador adecuado haga cada tarea y un trabajo imposible no bloquee a los demás.

## Cómo funciona

Según [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

Traslada el experimento a otro trabajo periódico (por ejemplo, una limpieza nocturna de archivos temporales): mide la distribución de su duración, decide la política de solape y diseña su cola de fallos. La transferencia está lograda cuando puedes explicar qué parte de la decisión dependía de la distribución de duraciones y cuál del tipo de carga, no cuando las tablas se parecen.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

`notas servir` programa tres trabajos: la sincronización cada 60 s con política de **omitir si sigue activa** y un límite de 50 s por ejecución, la exportación nocturna con un candado de archivo para que solo una instancia la ejecute, y un lote de revisiones con tamaño 200. Las consultas a la base se reparten con ocho hilos y los informes con cuatro procesos, que arrancan una vez y se reutilizan.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos ejecuciones escriben el mismo archivo** — causa: el planificador arranca sin comprobar la anterior. Corrección: política de solape con candado y límite de tiempo. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md)) son: Las definiciones son operativas para la herramienta `notas`. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2): las simulaciones fueron idénticas y los tiempos variaron entre ejecuciones. No se usó cron, ningún orquestador ni una cola real; las duraciones, las tasas de fallo y el presupuesto de intentos son supuestos del autor. La siguiente clase pregunta cómo hacer que cada operación pueda repetirse y reanudarse sin duplicar efectos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Cola de muertos](../c/cola-de-muertos.md), [Lote](../l/lote.md), [Planificador](./planificador.md), [Trabajador](../t/trabajador.md), [Trabajo venenoso](../t/trabajo-venenoso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.

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

[↑ Glosario](../../README.md) · [← Política de seguridad de contenido](./politica-de-seguridad-de-contenido.md) · [Política metodológica →](./politica-metodologica.md)
