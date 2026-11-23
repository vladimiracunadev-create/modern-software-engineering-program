# Escudo

[↑ Glosario](../../README.md) · [← Escritura confirmada perdida](./escritura-confirmada-perdida.md) · [Espacio de estados →](./espacio-de-estados.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Envoltura que impide que una cancelación externa interrumpa una operación interna.

Definición de trabajo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md).

## Por qué importa

La clase donde se define, [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), existe con este propósito: la clase existe para que sepas diseñar tareas concurrentes que no comparten memoria sino que se envían mensajes, que declares qué orden garantiza un buzón y qué no, que pongas un límite a la cola antes de que la memoria lo ponga por ti y que ates la vida de cada tarea al bloque que la creó, para que un error o una cancelación no dejen trabajo huérfano ni datos a medias.

## Cómo funciona

Según [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

Cancelar una corrutina lanza `CancelledError` en su siguiente punto de espera. Ese punto puede estar entre dos pasos que debían ir juntos: un descuento y un abono, un registro y su cierre. La concurrencia estructurada garantiza que la cancelación se propague; no garantiza que el estado quede coherente. Para ello se acotan las secciones indivisibles: se protege la operación con `asyncio.shield`, se hace en una transacción o se diseña como compensable. La regla es que cada operación cancelable debe declarar cuál es su estado válido tras ser interrumpida en cualquiera de sus puntos de espera.

Según [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

El equipo rediseña el actor «cupo». El buzón se acota a 200 mensajes, el pico esperado de dos segundos de la apertura de inscripción; si se llena, el manejador responde con un error reintentable y una cabecera de espera, en lugar de aceptar. Los mensajes llevan un número de secuencia por estudiante para que el actor descarte reservas duplicadas sin depender del orden entre estudiantes. Los manejadores lanzan sus tareas dentro de un `TaskGroup`, de modo que un fallo del comprobante cancela las demás y el error llega a la solicitud. La transferencia de plazas entre tutorías se envuelve en una transacción de la base y se protege con `shield` solo el tramo de confirmación; las tareas de notificación quedan fuera, porque pueden repetirse.

## Ejemplo

Ejemplo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sección «Ejemplo profesional»):

El equipo rediseña el actor «cupo». El buzón se acota a 200 mensajes, el pico esperado de dos segundos de la apertura de inscripción; si se llena, el manejador responde con un error reintentable y una cabecera de espera, en lugar de aceptar. Los mensajes llevan un número de secuencia por estudiante para que el actor descarte reservas duplicadas sin depender del orden entre estudiantes. Los manejadores lanzan sus tareas dentro de un `TaskGroup`, de modo que un fallo del comprobante cancela las demás y el error llega a la solicitud.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Estado a medias tras un tiempo límite** — causa: cancelación entre dos pasos inseparables. Corrección: transacción, compensación o `shield` en el tramo crítico. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuatro casos sobre `asyncio`: tres tareas hermanas, una de las cuales falla, con `TaskGroup` y con tareas sueltas más `gather`; y una transferencia de cuatro pasos (registrar, restar, sumar, cerrar) que se cancela en seis instantes distintos, con y sin `asyncio.shield`. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cancelación](../c/cancelacion.md), [Operación](../o/operacion.md), [Actor](../a/actor.md), [Cancelación cooperativa](../c/cancelacion-cooperativa.md), [Concurrencia estructurada](../c/concurrencia-estructurada.md), [Contrapresión](../c/contrapresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «shield».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: asyncio, tareas y grupos de tareas](https://docs.python.org/3/library/asyncio-task.html) — `TaskGroup`, cancelación y `shield`; autoridad: documentación de Python.
- [Hewitt, Bishop y Steiger, «A universal modular ACTOR formalism»](https://arxiv.org/abs/1008.1459) — el modelo de actores; autoridad: artículo original (1973).
- [Hoare, «Communicating sequential processes»](https://doi.org/10.1145/359576.359585) — procesos y canales; autoridad: artículo original (1978).
- [Python: asyncio, colas](https://docs.python.org/3/library/asyncio-queue.html) — colas acotadas; autoridad: documentación de Python.
- [Smith, «Notes on structured concurrency»](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/) — razones del diseño estructurado; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Escritura confirmada perdida](./escritura-confirmada-perdida.md) · [Espacio de estados →](./espacio-de-estados.md)
