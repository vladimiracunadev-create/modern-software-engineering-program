# A lo sumo una vez

[↑ Glosario](../../README.md) · [← 429](../0-9/429.md) · [A2A →](./a2a.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Semántica en la que cada mensaje se entrega cero o una vez; puede perderse y no se duplica.

Definición de trabajo de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Por qué importa

La clase donde se define, [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), existe con este propósito: la clase existe para que dejes de pedir «exactamente una vez» como si fuera una propiedad del transporte y lo trates como una propiedad del **efecto**: aprenderás a medir cuántos mensajes se pierden o se duplican bajo cada semántica de entrega, cuántos estados finales equivocados produce el desorden y qué ventana de deduplicación basta, antes de que un consumidor dependa de una garantía que el corredor no da.

## Cómo funciona

Según [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

**A lo sumo una vez**: el emisor envía y no reintenta; si el mensaje o el consumidor fallan, el mensaje se pierde, y nunca se duplica. **Al menos una vez**: el emisor reintenta hasta recibir un acuse; no se pierde, pero si se perdió el acuse y no el mensaje, el consumidor lo procesa de nuevo. Que el consumidor acuse **antes** o **después** de procesar define de qué lado cae un fallo del propio consumidor: acusar antes pierde el trabajo si cae, acusar después lo repite. No hay una tercera opción en el transporte: el emisor no puede distinguir «el mensaje no llegó» de «llegó y el acuse se perdió».

Según [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

El equipo de la plataforma documenta tres consumidores. **Registro de calificaciones:** al menos una vez, acuse tras procesar, tabla `vistos` con clave del mensaje en la misma transacción que el efecto, guarda por versión de la entrega y ventana ilimitada mientras la entrega exista. **Aviso por correo:** al menos una vez con ventana de deduplicación de 24 horas, aceptando que una reentrega más tardía enviará un segundo correo, y guarda del estado «avisado» en la propia entrega. **Estadísticas de uso:** a lo sumo una vez, con la regla de que perder el 0,1 % es aceptable. Para cada consumidor escriben qué ocurre si cae a mitad, si el mensaje llega dos veces y si llega después de uno más nuevo.

## Ejemplo

Ejemplo de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma documenta tres consumidores. **Registro de calificaciones:** al menos una vez, acuse tras procesar, tabla `vistos` con clave del mensaje en la misma transacción que el efecto, guarda por versión de la entrega y ventana ilimitada mientras la entrega exista. **Aviso por correo:** al menos una vez con ventana de deduplicación de 24 horas, aceptando que una reentrega más tardía enviará un segundo correo, y guarda del estado «avisado» en la propia entrega. **Estadísticas de uso:** a lo sumo una vez, con la regla de que perder el 0,1 % es aceptable.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md)) son:

- **Notas o avisos duplicados tras un incidente** — causa: entrega al menos una vez con efecto no idempotente. Corrección: clave de mensaje o forma idempotente del efecto en una transacción.
- **Mensajes que nunca se aplicaron** — causa: se acusó antes de procesar y el proceso cayó. Corrección: acusar después de procesar y hacer el efecto idempotente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **A lo sumo una vez**: el emisor envía y no reintenta; si el mensaje o el consumidor fallan, el mensaje se pierde, y nunca se duplica. ([SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Semántica](../s/semantica.md), [Al menos una vez](./al-menos-una-vez.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Guarda de versión](../g/guarda-de-version.md), [Ventana de deduplicación](../v/ventana-de-deduplicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Apache Kafka: semántica de entrega](https://kafka.apache.org/documentation/#semantics) — a lo sumo, al menos y exactamente una vez; autoridad: proyecto Apache Kafka.
- [Amazon SQS: colas estándar](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) — entrega al menos una vez y orden de mejor esfuerzo; autoridad: Amazon Web Services.
- [EIP: Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: autores del libro.
- [Lamport, «Time, clocks, and the ordering of events in a distributed system»](https://dl.acm.org/doi/10.1145/359545.359563) — orden causal entre procesos; autoridad: artículo original (Communications of the ACM, 1978; metadatos verificados con Crossref, el editor bloquea las peticiones automáticas).
- [Stripe: peticiones idempotentes](https://docs.stripe.com/api/idempotent_requests) — clave de idempotencia reutilizada en los reintentos; autoridad: documentación oficial de Stripe.

---

[↑ Glosario](../../README.md) · [← 429](../0-9/429.md) · [A2A →](./a2a.md)
