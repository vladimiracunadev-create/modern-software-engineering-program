# Actor

[↑ Glosario](../../README.md) · [← Activo](./activo.md) · [Actor, buzón y propiedad del estado →](./actor-buzon-y-propiedad-del-estado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Unidad con estado privado y buzón que procesa un mensaje por vez.

Definición de trabajo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md): Persona o sistema afectado o participante.

## Por qué importa

En [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), el tema «Actores y canales» importa porque quitan el estado compartido a cambio de razonar sobre mensajes.

## Cómo funciona

Según [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

Un **actor** posee un estado privado y un buzón; procesa un mensaje por vez, y por eso no necesita cerrojos para su propio estado. Los demás no lo tocan: le envían mensajes. Un **canal** es el conducto tipado entre tareas, con semántica de espera: enviar puede bloquear si el canal está lleno, recibir bloquea si está vacío. Hewitt formuló el actor y Hoare los procesos que se comunican por canales; ambas ideas sustituyen «proteger el dato» por «tener un dueño del dato». El costo es otro: la serialización del actor puede ser un cuello de botella, y el razonamiento sobre el estado pasa a ser un razonamiento sobre secuencias de mensajes, incluidas las respuestas que pueden llegar tarde.

Según [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md):

El equipo rediseña el actor «cupo». El buzón se acota a 200 mensajes, el pico esperado de dos segundos de la apertura de inscripción; si se llena, el manejador responde con un error reintentable y una cabecera de espera, en lugar de aceptar. Los mensajes llevan un número de secuencia por estudiante para que el actor descarte reservas duplicadas sin depender del orden entre estudiantes. Los manejadores lanzan sus tareas dentro de un `TaskGroup`, de modo que un fallo del comprobante cancela las demás y el error llega a la solicitud. La transferencia de plazas entre tutorías se envuelve en una transacción de la base y se protege con `shield` solo el tramo de confirmación; las tareas de notificación quedan fuera, porque pueden repetirse.

## Ejemplo

Ejemplo de [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sección «Ejemplo profesional»):

El equipo rediseña el actor «cupo». El buzón se acota a 200 mensajes, el pico esperado de dos segundos de la apertura de inscripción; si se llena, el manejador responde con un error reintentable y una cabecera de espera, en lugar de aceptar. Los mensajes llevan un número de secuencia por estudiante para que el actor descarte reservas duplicadas sin depender del orden entre estudiantes. Los manejadores lanzan sus tareas dentro de un `TaskGroup`, de modo que un fallo del comprobante cancela las demás y el error llega a la solicitud.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El actor es lento y todo espera** — causa: un solo dueño serializa el trabajo. Corrección: particionar por clave en varios actores. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **actor** posee un estado privado y un buzón; procesa un mensaje por vez, y por eso no necesita cerrojos para su propio estado. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))
- Eliminan las carreras de datos sobre el estado del actor, no las de lógica entre mensajes: dos mensajes de emisores distintos pueden llegar en cualquier orden, y una respuesta puede llegar después de que la situación cambió. ([SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado](../e/estado.md), [Ambigüedad](./ambiguedad.md), [Cancelación cooperativa](../c/cancelacion-cooperativa.md), [Concurrencia estructurada](../c/concurrencia-estructurada.md), [Conflicto](../c/conflicto.md), [Contrapresión](../c/contrapresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-059 — Taller: descomponer un problema ambiguo](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-387 — Actores, canales y structured concurrency](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (30 clases más lo mencionan; las que más):

[SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-123](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md).

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

[↑ Glosario](../../README.md) · [← Activo](./activo.md) · [Actor, buzón y propiedad del estado →](./actor-buzon-y-propiedad-del-estado.md)
