# Transferencia de estado en el evento

[↑ Glosario](../../README.md) · [← Transferencia](./transferencia.md) · [Transición →](./transicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Diseño en el que el evento incluye los datos que los consumidores necesitan, para que no tengan que consultar al emisor.

Definición de trabajo de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md).

## Por qué importa

La clase donde se define, [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), existe con este propósito: la clase existe para que distingas cuatro cosas que se llaman «mensaje» en los equipos y se comportan de forma distinta: una orden dirigida a alguien (comando), un hecho que ya ocurrió (evento), una copia de datos (documento) y el sobre que acompaña a cualquiera de ellas, y para que midas qué cuesta equivocar el tipo o el contenido antes de que haya consumidores que dependan de él.

## Cómo funciona

Según [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md):

Un **documento** transfiere datos: «este es el estado actual de la entrega». Un evento puede incluir el estado (transferencia de estado en el evento) para que los consumidores no llamen de vuelta, o llevar solo un identificador y dejar que consulten. Cada opción tiene un costo opuesto. Con el estado dentro, los consumidores son autónomos y no cargan al emisor, pero leen la versión del instante de emisión, que puede ya no ser la vigente. Con solo el identificador, leen la versión actual, pero acoplan su disponibilidad a la del emisor y le devuelven toda la carga. No hay una respuesta correcta; hay una pregunta por consumidor: ¿necesita el valor del instante o el valor de ahora?

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md):

El equipo de la plataforma escribe el catálogo de mensajes antes de implementarlos. `CalificarEntrega` es un **comando** con un único destinatario, el calificador, que puede rechazarlo (entrega inexistente, plazo vencido). `EntregaRecibida` es un **evento** con sobre completo (identificador, tipo, origen, hora, secuencia por entrega, correlación) y un contenido mínimo: identificador de la entrega, de estudiante y de curso. `CalificacionPublicada` es un **documento** con la nota y su versión, porque el aviso y la analítica quieren el estado **del instante**.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md)) son:

- **Una acción se ejecuta varias veces** — causa: un comando se difundió a varios oyentes. Corrección: un destinatario por comando y rechazo si no hay uno.
- **Nadie reacciona a un evento y no hay error** — causa: ningún oyente registrado y el bus descarta en silencio. Corrección: alarma por eventos sin consumidor donde importe.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un evento puede incluir el estado (transferencia de estado en el evento) para que los consumidores no llamen de vuelta, o llevar solo un identificador y dejar que consulten. ([SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Comando](../c/comando.md), [Documento](../d/documento.md), [Sobre](../s/sobre.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-374 — Mensajes, eventos, comandos y documentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EIP: Command Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CommandMessage.html) — mensaje que invoca una acción en otra aplicación; autoridad: autores del libro.
- [EIP: Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) — mensaje que notifica un hecho; autoridad: autores del libro.
- [EIP: Document Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DocumentMessage.html) — mensaje que transfiere datos; autoridad: autores del libro.
- [Fowler, «What do you mean by Event-Driven?»](https://martinfowler.com/articles/201701-event-driven.html) — cuatro significados de dirigido por eventos; autoridad: autor del texto.
- [CloudEvents: especificación](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) — atributos comunes de un evento; autoridad: proyecto CloudEvents de la CNCF.

---

[↑ Glosario](../../README.md) · [← Transferencia](./transferencia.md) · [Transición →](./transicion.md)
