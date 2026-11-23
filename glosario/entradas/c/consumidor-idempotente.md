# Consumidor idempotente

[↑ Glosario](../../README.md) · [← Consulta recursiva](./consulta-recursiva.md) · [Contador →](./contador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Consumidor cuyo efecto no cambia si recibe el mismo mensaje más de una vez.

Definición de trabajo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md): Receptor que, ante un mensaje repetido, no repite el efecto.

## Por qué importa

La clase donde se define, [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), existe con este propósito: la clase existe para que decidas cuándo comunicar contextos por eventos, cuándo separar la escritura de la lectura y cuándo guardar la historia en lugar del estado, y para que midas las garantías que esa decisión exige a quien consume eventos.

## Cómo funciona

Según [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md):

Como entrega, no de forma general: se aproxima con entrega al-menos-una-vez más consumidores idempotentes. Lo que se logra es un efecto único, no una entrega única. Algunos productos ofrecen modos transaccionales con límites que hay que leer en su documentación.

Según [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

Los productos que prometen «exactamente una vez» lo hacen dentro de un perímetro: combinan identificadores de productor, transacciones del corredor y lectura-proceso-escritura atómica dentro de su propio almacén. Fuera de ese perímetro (un correo enviado, una nota escrita en otra base) la promesa se rompe, porque el efecto externo no participa en la transacción. La forma práctica de lograrlo es **entrega al menos una vez más consumidor idempotente**: el receptor reconoce un mensaje ya aplicado y no repite el efecto. Es un truco del receptor, no una propiedad del canal.

## Ejemplo

Ejemplo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un consumidor idempotente y con orden. Antes de ejecutarlo, predice el estado final.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md)) son:

- **Contadores mayores que la realidad** — causa: consumidor que suma cada mensaje con entrega al-menos-una-vez. Corrección: idempotencia con identificador de evento.
- **Un estado antiguo sobrescribe a uno nuevo** — causa: desorden sin secuencia por entidad. Corrección: aplicar solo eventos con secuencia mayor a la vista.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Como entrega, no de forma general: se aproxima con entrega al-menos-una-vez más consumidores idempotentes. ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Contrato de interfaz](./contrato-de-interfaz.md), [Evento](../e/evento.md), [Evento de dominio](../e/evento-de-dominio.md), [GraphQL](../g/graphql.md), [Instantánea](../i/instantanea.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «What do you mean by Event-Driven?»](https://martinfowler.com/articles/201701-event-driven.html) — cuatro patrones que suelen confundirse; autoridad: Martin Fowler.
- [Fowler, «CQRS»](https://martinfowler.com/bliki/CQRS.html) — separación de modelos de lectura y escritura; autoridad: Martin Fowler.
- [Fowler, «Event Sourcing»](https://martinfowler.com/eaaDev/EventSourcing.html) — estado como secuencia de eventos; autoridad: Martin Fowler.
- [Hohpe y Woolf, «Idempotent Receiver»](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera duplicados; autoridad: Enterprise Integration Patterns.
- [Vogels, «Eventually consistent» (CACM, 2009)](https://doi.org/10.1145/1435417.1435432) — consistencia eventual y lectura de la propia escritura; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Consulta recursiva](./consulta-recursiva.md) · [Contador →](./contador.md)
