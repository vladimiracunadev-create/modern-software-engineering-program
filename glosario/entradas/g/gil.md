# GIL

[↑ Glosario](../../README.md) · [← Gestor de versiones](./gestor-de-versiones.md) · [GitFlow →](./gitflow.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Mecanismo del CPython estándar que permite ejecutar bytecode de Python en un solo hilo a la vez.

Definición de trabajo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md).

## Por qué importa

En [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), el tema «Hilos, procesos y el GIL» importa porque determina si el cálculo se reparte y cuánto cuesta comunicarlo.

## Cómo funciona

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

Un hilo comparte la memoria del proceso; un proceso tiene la suya y se comunica copiando o compartiendo explícitamente. En el CPython estándar, el bloqueo global del intérprete (GIL) permite que un solo hilo ejecute bytecode de Python a la vez: los hilos sirven para solapar esperas de entrada y salida (el GIL se libera al esperar) y no aceleran un cálculo de Python puro. Para repartir cálculo entre núcleos se usan procesos (`multiprocessing`, `concurrent.futures.ProcessPoolExecutor`), pagando el costo de iniciarlos y de serializar los datos que viajan entre ellos, o bibliotecas que liberan el GIL en código nativo. Esta clase no mide esos costos porque dependen del equipo y de la versión; la documentación de Python es la referencia y la medición de tu carga, la evidencia.

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

Sirven para esperar entrada y salida, porque el GIL se libera mientras se espera. No aceleran un cálculo de Python puro porque solo un hilo ejecuta bytecode a la vez. La documentación del glosario define el GIL y las versiones recientes de Python trabajan en variantes sin él, por lo que conviene verificar la versión que usas.

## Ejemplo

Ejemplo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sección «Preguntas frecuentes»):

Sirven para esperar entrada y salida, porque el GIL se libera mientras se espera. No aceleran un cálculo de Python puro porque solo un hilo ejecuta bytecode a la vez. La documentación del glosario define el GIL y las versiones recientes de Python trabajan en variantes sin él, por lo que conviene verificar la versión que usas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Cuatro hilos no aceleran un cálculo de Python** — causa: el GIL permite un solo hilo de bytecode. Corrección: usar procesos o código nativo que libere el GIL. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el CPython estándar, el bloqueo global del intérprete (GIL) permite que un solo hilo ejecute bytecode de Python a la vez: los hilos sirven para solapar esperas de entrada y salida (el GIL se libera al esperar) y no aceleran un cálculo de Python puro. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bytecode](../b/bytecode.md), [Hilo](../h/hilo.md), [Mecanismo](../m/mecanismo.md), [Concurrencia](../c/concurrencia.md), [Corrutina](../c/corrutina.md), [Ley de Amdahl](../l/ley-de-amdahl.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «bloqueo global del intérprete».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: glosario](https://docs.python.org/3/glossary.html) — definición del bloqueo global del intérprete; autoridad: documentación de Python.
- [Python: asyncio](https://docs.python.org/3/library/asyncio.html) — bucle de eventos y corrutinas; autoridad: documentación de Python.
- [Python: desarrollo con asyncio](https://docs.python.org/3/library/asyncio-dev.html) — modo de depuración y código bloqueante; autoridad: documentación de Python.
- [Python: concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — ejecutores de hilos y procesos; autoridad: documentación de Python.
- [Amdahl, «Validity of the single processor approach…»](https://doi.org/10.1145/1465482.1465560) — límite de aceleración; autoridad: artículo original (1967).

---

[↑ Glosario](../../README.md) · [← Gestor de versiones](./gestor-de-versiones.md) · [GitFlow →](./gitflow.md)
