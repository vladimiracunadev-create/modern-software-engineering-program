# Consumidor idempotente

[↑ Glosario](../../README.md) · [← Consulta recursiva](./consulta-recursiva.md) · [Contador →](./contador.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un **consumidor idempotente** es un consumidor de mensajes cuyo efecto no cambia si recibe el mismo mensaje más de una vez ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md)). [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) lo formula como el receptor que, ante un mensaje repetido, no repite el efecto. Es la contrapartida, en quien recibe, de la clave de idempotencia de quien envía.

## Por qué importa

Hace correcto un sistema donde los mensajes pueden llegar duplicados. En mensajería distribuida, la entrega «al menos una vez» es lo habitual y lo práctico: ante un fallo, el corredor reenvía. Si el consumidor no tolera duplicados, un contador suma de más o un correo se envía dos veces. Cambia el diseño del consumo: se asume el duplicado como caso normal.

## Cómo funciona

[SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) y [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) explican por qué no basta confiar en «exactamente una vez». Los productos que lo prometen lo hacen **dentro de un perímetro**: combinan identificadores de productor, transacciones del corredor y lectura-proceso-escritura atómica dentro de su propio almacén. Fuera de ese perímetro (un correo enviado, una nota escrita en otra base) la promesa se rompe, porque el efecto externo no participa en la transacción.

La forma práctica de lograr un efecto único es **entrega al menos una vez más consumidor idempotente**: lo que se consigue es un efecto único, no una entrega única. El consumidor lo logra con un **identificador de evento**: guarda los identificadores ya procesados (en la misma transacción que el efecto) y descarta los repetidos. Cuando la operación es naturalmente idempotente (fijar un valor, no sumarlo), basta aplicarla de nuevo.

Un segundo problema es el orden: un estado antiguo puede sobrescribir uno nuevo si los mensajes llegan desordenados. La corrección es la **secuencia por entidad**: se aplican solo los eventos con secuencia mayor a la última vista. El fragmento de [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) muestra un consumidor idempotente y con orden, y pide predecir el estado final.

## Ejemplo

Un consumidor suma cada evento `entrega_recibida` a un contador. El corredor reenvía un evento tras un fallo y el contador queda mayor que la realidad. Con idempotencia: la tabla `procesados(id_evento)` tiene una restricción única; en una sola transacción se inserta el identificador y se incrementa el contador; si el insert falla por duplicado, no se suma. (Ilustración del mecanismo de [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).)

## Errores y confusiones comunes

- **Contadores mayores que la realidad**: el consumidor suma cada mensaje; corrección: idempotencia con identificador de evento.
- **Un estado antiguo sobrescribe a uno nuevo**: desorden sin secuencia; corrección: aplicar solo eventos con secuencia mayor.
- **Registrar el identificador fuera de la transacción del efecto.**
- **Creer en «exactamente una vez» fuera del perímetro.**

## Límites y cuándo no aplica

Guardar identificadores consume espacio y exige una política de retención; pasado el plazo, un duplicado tardío se tomaría como nuevo. Para efectos externos que no participan en la transacción, la idempotencia requiere cooperación del destino (por ejemplo, una clave de idempotencia en la API externa). Algunos productos ofrecen modos transaccionales con límites que hay que leer en su documentación.

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
