# Cola de trabajo

[↑ Glosario](../../README.md) · [← Cola de rechazos](./cola-de-rechazos.md) · [Cola justa →](./cola-justa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Canal en el que varios consumidores compiten y cada mensaje se entrega a uno y se borra al confirmarse.

Definición de trabajo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md).

## Por qué importa

En [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), el tema «Cola de trabajo» importa porque reparte trabajo: cada mensaje se procesa una vez y desaparece.

## Cómo funciona

Según [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), en la sección «Cola de trabajo»:

En una **cola de trabajo** varios consumidores competidores toman mensajes de un mismo canal; cada mensaje lo recibe uno y, al confirmarse, se borra. Sirve para repartir carga: se agregan consumidores y la cola se vacía más rápido. Su limitación es estructural: el mensaje confirmado no existe, de modo que no se puede reprocesar ni mostrar a un segundo interesado. Un segundo consumidor que lee de la misma cola no ve una copia: toma una parte del trabajo.

## Ejemplo

Ejemplo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sección «Ejemplo profesional»):

El equipo asigna cada flujo de la plataforma a una estructura. **Calificar entregas:** cola de trabajo con tres consumidores, tiempo máximo de edad de 24 horas y una cola de mensajes fallidos. **Eventos de entrega** (`EntregaRecibida`, `CalificacionPublicada`): un log por particiones con clave `estudiante_id`, para que los eventos de cada estudiante lleguen en orden, con ocho particiones y retención de 14 días; las suscripciones de avisos y analítica son dos grupos. **Estado de cursos para el portal:** log compactado por `curso_id`, para reconstruir el portal desde cero.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)) son:

- **La mitad de los mensajes no llega a un consumidor** — causa: dos consumidores comparten una cola. Corrección: suscripciones separadas para difundir.
- **Un servicio nuevo no ve datos anteriores** — causa: tópico sin retención. Corrección: un log, o cargar la historia desde otra fuente.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En una **cola de trabajo** varios consumidores competidores toman mensajes de un mismo canal; cada mensaje lo recibe uno y, al confirmarse, se borra. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compactación](./compactacion.md), [Log](../l/log.md), [Partición](../p/particion.md), [Tópico](../t/topico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-410](../../../classes/part-34-saas-y-plataformas-de-producto/se-410-aislamiento-multi-inquilino-y-vecino-ruidoso/README.md), [SE-086](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-086-pilas-colas-deques-y-prioridades/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-399](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-399-orquestacion-y-scheduling/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-495](../../../classes/part-41-observabilidad-sre-e-incidentes/se-495-metricas-dimensiones-y-cardinalidad/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

**Aparece en los casos de estudio:** [Slack](../../../casos/exito/slack.md).

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

[↑ Glosario](../../README.md) · [← Cola de rechazos](./cola-de-rechazos.md) · [Cola justa →](./cola-justa.md)
