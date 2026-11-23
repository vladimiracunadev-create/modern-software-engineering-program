# Tópico

[↑ Glosario](../../README.md) · [← Tope de vueltas](./tope-de-vueltas.md) · [Tormenta de reintentos →](./tormenta-de-reintentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Canal que entrega una copia de cada mensaje publicado a cada suscripción vigente.

Definición de trabajo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md).

## Por qué importa

En [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), el tema «Tópico y suscripciones» importa porque difunde hechos a oyentes independientes sin conocerlos.

## Cómo funciona

Según [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md):

Un **tópico** difunde: cada suscripción recibe su propia copia de cada mensaje publicado, y dentro de una suscripción varios consumidores pueden competir. Es la estructura natural para eventos: se añade una suscripción nueva sin tocar al emisor ni a las demás. La pregunta que muchos equipos descubren tarde es qué ve una suscripción nueva: en la mayoría de los tópicos solo lo publicado **a partir de su creación**. Si el servicio nuevo necesita la historia, el tópico no la tiene.

Según [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** la mitad de las entregas no tiene nota y analítica no recibe la mitad que esperaba. **Hipótesis rivales:** (a) un calificador cayó; (b) se perdieron mensajes; (c) un consumidor compite por los mismos mensajes. **Prueba:** cuenta los mensajes confirmados por cada consumidor; si suman el total y están repartidos casi por mitades, la causa es la competencia. **Conclusión:** una cola reparte, no difunde. **Regresión:** analítica pasa a una suscripción propia de un tópico y una prueba publica 100 mensajes y comprueba que ambos reciben los 100. No cambies a la vez la estructura y el número de consumidores.

## Ejemplo

Ejemplo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que un tópico no entrega lo anterior a un suscriptor nuevo y un log sí. Antes de ejecutarlo, predice cuántos mensajes recibe el suscriptor tardío en cada caso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un servicio nuevo no ve datos anteriores** — causa: tópico sin retención. Corrección: un log, o cargar la historia desde otra fuente. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La pregunta que muchos equipos descubren tarde es qué ve una suscripción nueva: en la mayoría de los tópicos solo lo publicado **a partir de su creación**. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Suscripción](../s/suscripcion.md), [Cola de trabajo](../c/cola-de-trabajo.md), [Compactación](../c/compactacion.md), [Log](../l/log.md), [Partición](../p/particion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [EIP: Point-to-Point Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PointToPointChannel.html) — canal con un único receptor por mensaje; autoridad: autores del libro.
- [EIP: Publish-Subscribe Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html) — canal que entrega una copia a cada suscriptor; autoridad: autores del libro.
- [EIP: Competing Consumers](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html) — varios consumidores que reparten los mensajes de un canal; autoridad: autores del libro.
- [Apache Kafka: documentación](https://kafka.apache.org/documentation/) — particiones, desplazamientos, retención y compactación; autoridad: proyecto Apache Kafka.
- [Amazon SQS: colas estándar](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html) — entrega al menos una vez y orden de mejor esfuerzo; autoridad: Amazon Web Services.

---

[↑ Glosario](../../README.md) · [← Tope de vueltas](./tope-de-vueltas.md) · [Tormenta de reintentos →](./tormenta-de-reintentos.md)
