# Cancelación cooperativa

[↑ Glosario](../../README.md) · [← Cancelación](./cancelacion.md) · [Cancelación y ciclo de vida →](./cancelacion-y-ciclo-de-vida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Interrupción que se entrega en el siguiente punto de espera de la tarea, no en cualquier instrucción.

Definición de trabajo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md).

## Por qué importa

La clase donde se define, [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), existe con este propósito: la clase existe para que sepas diseñar tareas concurrentes que no comparten memoria sino que se envían mensajes, que declares qué orden garantiza un buzón y qué no, que pongas un límite a la cola antes de que la memoria lo ponga por ti y que ates la vida de cada tarea al bloque que la creó, para que un error o una cancelación no dejen trabajo huérfano ni datos a medias.

## Cómo funciona

[SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

El equipo rediseña el actor «cupo». El buzón se acota a 200 mensajes, el pico esperado de dos segundos de la apertura de inscripción; si se llena, el manejador responde con un error reintentable y una cabecera de espera, en lugar de aceptar. Los mensajes llevan un número de secuencia por estudiante para que el actor descarte reservas duplicadas sin depender del orden entre estudiantes.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)) son:

- **La memoria crece durante una ráfaga y el proceso muere** — causa: buzón sin límite. Corrección: cola acotada con rechazo o espera.
- **Tareas que escriben después de un error** — causa: tareas sueltas sin dueño. Corrección: `TaskGroup` o un bloque que las espere.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos deterministas sobre el bucle de eventos de `asyncio` en Windows y Ubuntu (WSL2) con resultados idénticos. No se probó una cola distribuida, un sistema de actores real, procesos múltiples ni caídas de proceso: las tasas de 3 y 1 mensajes por turno y los pasos de la transferencia son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Instrucción](../i/instruccion.md), [Interrupción](../i/interrupcion.md), [Tarea](../t/tarea.md), [Actor](../a/actor.md), [Concurrencia estructurada](./concurrencia-estructurada.md).
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

[↑ Glosario](../../README.md) · [← Cancelación](./cancelacion.md) · [Cancelación y ciclo de vida →](./cancelacion-y-ciclo-de-vida.md)
