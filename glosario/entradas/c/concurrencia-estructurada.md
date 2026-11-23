# Concurrencia estructurada

[↑ Glosario](../../README.md) · [← Concurrencia](./concurrencia.md) · [Concurrencia, paralelismo e intercalación →](./concurrencia-paralelismo-e-intercalacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Disciplina por la que toda tarea hija vive dentro de un bloque que la espera, propaga sus errores y la cancela al salir.

Definición de trabajo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md).

## Por qué importa

En [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), el tema «Concurrencia estructurada» importa porque ata la vida y los errores de las tareas a un bloque.

## Cómo funciona

Según [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), en la sección «Concurrencia estructurada»:

La **concurrencia estructurada** exige que toda tarea hija viva dentro de un bloque que la espera: el bloque no termina hasta que todas terminan, un error de una hija cancela a las hermanas y se propaga al padre. `asyncio.TaskGroup` (Python 3.11) lo ofrece. Frente a ello, lanzar tareas sueltas (`create_task` sin esperarlas, o `gather` que propaga el primer error sin cancelar al resto) deja trabajo huérfano: tareas que siguen escribiendo, con sus efectos, sin dueño que las vea o las espere. La propiedad que se gana es de razonamiento: cuando el bloque termina, no queda nada en vuelo que haya nacido dentro de él.

## Ejemplo

Caso medido en la sección «Concurrencia estructurada» de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

La **concurrencia estructurada** exige que toda tarea hija viva dentro de un bloque que la espera: el bloque no termina hasta que todas terminan, un error de una hija cancela a las hermanas y se propaga al padre. `asyncio.TaskGroup` (Python 3.11) lo ofrece. Frente a ello, lanzar tareas sueltas (`create_task` sin esperarlas, o `gather` que propaga el primer error sin cancelar al resto) deja trabajo huérfano: tareas que siguen escribiendo, con sus efectos, sin dueño que las vea o las espere.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)) son:

- **La memoria crece durante una ráfaga y el proceso muere** — causa: buzón sin límite. Corrección: cola acotada con rechazo o espera.
- **Tareas que escriben después de un error** — causa: tareas sueltas sin dueño. Corrección: `TaskGroup` o un bloque que las espere.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **concurrencia estructurada** exige que toda tarea hija viva dentro de un bloque que la espera: el bloque no termina hasta que todas terminan, un error de una hija cancela a las hermanas y se propaga al padre. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Tarea](../t/tarea.md), [Actor](../a/actor.md), [Cancelación cooperativa](./cancelacion-cooperativa.md), [Contrapresión](./contrapresion.md), [Escudo](../e/escudo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hewitt, Bishop y Steiger, «A universal modular ACTOR formalism»](https://arxiv.org/abs/1008.1459) — el modelo de actores; autoridad: artículo original (1973).
- [Hoare, «Communicating sequential processes»](https://doi.org/10.1145/359576.359585) — procesos y canales; autoridad: artículo original (1978).
- [Python: asyncio, tareas y grupos de tareas](https://docs.python.org/3/library/asyncio-task.html) — `TaskGroup`, cancelación y `shield`; autoridad: documentación de Python.
- [Python: asyncio, colas](https://docs.python.org/3/library/asyncio-queue.html) — colas acotadas; autoridad: documentación de Python.
- [Smith, «Notes on structured concurrency»](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) — razones del diseño estructurado; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Concurrencia](./concurrencia.md) · [Concurrencia, paralelismo e intercalación →](./concurrencia-paralelismo-e-intercalacion.md)
