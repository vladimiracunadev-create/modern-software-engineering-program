# Lote

[↑ Glosario](../../README.md) · [← Log](./log.md) · [Lote dinámico →](./lote-dinamico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Grupo de elementos que se mueven juntos por una etapa del flujo.

Definición de trabajo de [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md): Conjunto de peticiones procesadas en una sola ejecución del modelo.

## Por qué importa

En [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md), el tema «Lote» importa porque amortiza el costo fijo de cada llamada a cambio de latencia.

En [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), el tema «Lotes» importa porque agrupar reduce coste por elemento pero aumenta la unidad de pérdida.

## Cómo funciona

Según [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

Una llamada a un cálculo tiene un costo fijo (lanzar, sincronizar, mover datos) y uno variable por elemento. Agrupar varias peticiones en un lote reparte el costo fijo, y el throughput sube; pero cada petición espera a que el lote se llene y a que termine. En la CPU del laboratorio, una capa densa de 1024×1024 en 32 bits con lotes de 1, 16, 64 y 256 tuvo estas latencias por lote y rendimientos: lote 1, 0,27 ms y unas 3 700 peticiones por segundo; lote 16, 4,8 ms y 3 300 (sin ganancia aún); lote 64, 7,9 ms y 8 100; lote 256, 14,3 ms y 17 900.

Según [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md):

**Diagnóstico paso a paso.** (1) Se mide la utilización de la unidad: promedio del 8 %, con picos cortos. (2) Se descompone el tiempo por petición: la transferencia domina porque cada petición mueve 40 registros pequeños. (3) El tamaño de lote en producción es 1, porque la política de agrupar no se configuró. (4) La latencia p99 incluye el arranque de unidades nuevas cuando la demanda sube. (5) Se corrige agrupando peticiones con un tiempo máximo de espera de 5 ms, compartiendo la unidad con la carga nocturna y manteniendo una unidad mínima caliente.

## Ejemplo

Ejemplo de [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) (sección «Ejemplo profesional»):

`notas servir` programa tres trabajos: la sincronización cada 60 s con política de **omitir si sigue activa** y un límite de 50 s por ejecución, la exportación nocturna con un candado de archivo para que solo una instancia la ejecute, y un lote de revisiones con tamaño 200. Las consultas a la base se reparten con ocho hilos y los informes con cuatro procesos, que arrancan una vez y se reutilizan. La cola permite tres intentos con espera de 1, 4 y 16 s; tras ellos el trabajo pasa a una carpeta `muertos/` con el motivo y se avisa si hay más de cinco.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se contratan personas y el plazo no mejora** — causa: la espera venía de lotes y variabilidad. Corrección: medir tamaños y lotes antes de añadir capacidad. ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con una demanda de 200 peticiones por segundo, llenar un lote de 256 tardaría más de un segundo: el lote óptimo es el que cabe en el tiempo que el objetivo de latencia permite esperar, no el que maximiza el throughput. ([SE-281](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Flujo](../f/flujo.md), [Modelo](../m/modelo.md), [Crisis del software](../c/crisis-del-software.md), [Ingeniería continua](../i/ingenieria-continua.md), [Integración continua](../i/integracion-continua.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-223 — Schedulers, workers y trabajos por lotes](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-281 — Rendimiento y costo en aceleradores](../../../classes/part-23-runtimes-y-plataformas-modernas/se-281-rendimiento-y-costo-en-aceleradores/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.
- [SE-606 — Servir modelos: latencia, lotes y GPU](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-606-servir-modelos-latencia-lotes-y-gpu/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (61 clases más lo mencionan; las que más):

[SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md), [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Lotes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [POSIX: crontab](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html) — formato de las entradas periódicas; autoridad: The Open Group.
- [Google SRE: Distributed Periodic Scheduling with Cron](https://sre.google/sre-book/distributed-periodic-scheduling/) — fallos de la planificación periódica; autoridad: Google.
- [Python: `concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html) — pools de hilos y procesos; autoridad: documentación de Python.
- [Python: `multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods) — métodos de inicio de procesos; autoridad: documentación de Python.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — patrón de cola de muertos; autoridad: documentación de AWS.

---

[↑ Glosario](../../README.md) · [← Log](./log.md) · [Lote dinámico →](./lote-dinamico.md)
