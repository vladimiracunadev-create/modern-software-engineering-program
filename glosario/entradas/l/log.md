# Log

[↑ Glosario](../../README.md) · [← Lockfile](./lockfile.md) · [Lote →](./lote.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Secuencia ordenada de mensajes que se conserva tras leerse y se consume mediante desplazamientos.

Definición de trabajo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md).

## Por qué importa

En [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md), el tema «Log y desplazamientos» importa porque conserva la historia y permite releer y reprocesar.

## Cómo funciona

Según [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md):

Un **log** es una secuencia ordenada de mensajes que no se borra al leerse; cada consumidor (o grupo) recuerda un **desplazamiento** (offset), la posición hasta la que leyó. Eso cambia tres cosas: un suscriptor nuevo puede empezar en cero y ver toda la historia retenida; dos grupos leen lo mismo sin interferirse; y reprocesar es mover el desplazamiento hacia atrás. El precio es que la estructura retiene datos, con costo de almacenamiento y de privacidad, y que quien lee debe gestionar su posición.

Según [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md):

El equipo asigna cada flujo de la plataforma a una estructura. **Calificar entregas:** cola de trabajo con tres consumidores, tiempo máximo de edad de 24 horas y una cola de mensajes fallidos. **Eventos de entrega** (`EntregaRecibida`, `CalificacionPublicada`): un log por particiones con clave `estudiante_id`, para que los eventos de cada estudiante lleguen en orden, con ocho particiones y retención de 14 días; las suscripciones de avisos y analítica son dos grupos. **Estado de cursos para el portal:** log compactado por `curso_id`, para reconstruir el portal desde cero. Antes de fijar ocho particiones miden cuánto concentra el estudiante más activo y descubren que una cuenta de pruebas genera un tercio del tráfico: la excluyen de la clave.

## Ejemplo

Ejemplo de [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra que un tópico no entrega lo anterior a un suscriptor nuevo y un log sí. Antes de ejecutarlo, predice cuántos mensajes recibe el suscriptor tardío en cada caso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un servicio nuevo no ve datos anteriores** — causa: tópico sin retención. Corrección: un log, o cargar la historia desde otra fuente. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **log** es una secuencia ordenada de mensajes que no se borra al leerse; cada consumidor (o grupo) recuerda un **desplazamiento** (offset), la posición hasta la que leyó. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))
- La transferencia está lograda cuando puedes justificar por qué un flujo no necesita log, no cuando todo termina en el mismo corredor. ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-374](../../../classes/part-31-integracion-eventos-y-mensajeria/se-374-mensajes-eventos-comandos-y-documentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Desplazamiento](../d/desplazamiento.md), [Secuencia](../s/secuencia.md), [Cola de trabajo](../c/cola-de-trabajo.md), [Compactación](../c/compactacion.md), [Partición](../p/particion.md), [Tópico](../t/topico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-375 — Brokers, colas, topics y logs distribuidos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

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

[↑ Glosario](../../README.md) · [← Lockfile](./lockfile.md) · [Lote →](./lote.md)
