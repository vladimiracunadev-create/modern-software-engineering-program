# Planificador

[↑ Glosario](../../README.md) · [← Planificación](./planificacion.md) · [Plano de control →](./plano-de-control.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Componente que arranca trabajos en instantes o periodos dados, sin garantizar cuándo terminan.

Definición de trabajo de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md): Componente que decide en qué nodo se ejecuta cada unidad a partir de lo que pide y de lo que hay libre.

## Por qué importa

La clase donde se define, [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), existe con este propósito: la clase existe para decidir cómo se programa, se reparte y se acota el trabajo que un servicio hace por su cuenta —una ejecución periódica, un grupo de trabajadores, una cola de lotes— de modo que un trabajo lento no se pise a sí mismo, un trabajador adecuado haga cada tarea y un trabajo imposible no bloquee a los demás.

## Cómo funciona

Según [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

Con una duración media de 40 s y un periodo de 60 s «cabe de sobra»; pero si la duración varía, una fracción de ejecuciones superará los 60 s. Lo que importa para decidir no es el promedio sino la **proporción que supera el periodo** y cuánto la supera. Medir percentiles (p95, p99) y no solo la media es la base de un planificador honesto. Cuando esa proporción crece, hay que cambiar el diseño: dividir el trabajo, ampliar el periodo o poner un límite de tiempo por ejecución.

Según [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md):

El planificador de Kubernetes decide dónde va un pod en dos fases: filtra los nodos que cumplen las condiciones (hay recursos libres, las etiquetas coinciden) y puntúa los restantes con una o varias funciones. Por defecto favorece los nodos con más recursos libres tras la asignación, lo que reparte la carga, mientras que políticas de empaquetado prefieren llenar nodos y dejar otros libres para apagarlos. No hay una política mejor en abstracto: el reparto protege frente a la caída de un nodo y el empaquetado ahorra costo, y se elige según cuál de los dos riesgos pesa más. El algoritmo ve un pod a la vez, en el orden en que llegan, y esa ceguera al futuro es lo que hace que el orden importe.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md):

`notas servir` programa tres trabajos: la sincronización cada 60 s con política de **omitir si sigue activa** y un límite de 50 s por ejecución, la exportación nocturna con un candado de archivo para que solo una instancia la ejecute, y un lote de revisiones con tamaño 200. Las consultas a la base se reparten con ocho hilos y los informes con cuatro procesos, que arrancan una vez y se reutilizan.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Dos ejecuciones escriben el mismo archivo** — causa: el planificador arranca sin comprobar la anterior. Corrección: política de solape con candado y límite de tiempo. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Medir percentiles (p95, p99) y no solo la media es la base de un planificador honesto. ([SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Instante](../i/instante.md), [Trabajo](../t/trabajo.md), [Bucle de reconciliación](../b/bucle-de-reconciliacion.md), [Cola de muertos](../c/cola-de-muertos.md), [Límite de recursos](../l/limite-de-recursos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-399 — Orquestación y scheduling](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-220](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-220-codigos-de-salida-errores-y-diagnostico/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md).

**Aparece en los casos de estudio:** [Spotify](../../../casos/exito/spotify.md), [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Planificación](./planificacion.md) · [Plano de control →](./plano-de-control.md)
