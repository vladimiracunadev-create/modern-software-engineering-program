# Cola de trabajo

[↑ Glosario](../../README.md) · [← Cola de rechazos](./cola-de-rechazos.md) · [Cola justa →](./cola-justa.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Una **cola de trabajo** es un canal en el que varios consumidores compiten por los mensajes: cada mensaje se entrega a uno solo y se borra al confirmarse ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)). Su propósito es repartir carga, no difundir información.

## Por qué importa

Elegir entre una cola de trabajo y un log o un tópico con suscripciones decide qué se puede hacer después. En una cola, un mensaje confirmado deja de existir: no se puede reprocesar tras un defecto ni mostrar a un segundo interesado. Quien necesita que varios servicios reaccionen al mismo hecho, o que un servicio nuevo vea la historia, no puede apoyarse en una cola de trabajo.

## Cómo funciona

Varios **consumidores competidores** leen del mismo canal. El corredor entrega cada mensaje a uno de ellos; cuando ese consumidor lo confirma, el mensaje se borra. Por eso añadir consumidores acelera el vaciado: el trabajo se divide entre más manos. [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) subraya que la limitación es **estructural**, no un defecto de configuración: el mensaje confirmado no existe. Un segundo consumidor que lee de la misma cola no recibe una copia, sino que toma otra parte del trabajo.

Contrasta con el **log**, donde los mensajes se conservan por retención o compactación y cada consumidor mantiene su propia posición de lectura, de modo que muchos pueden leer lo mismo y un consumidor nuevo puede empezar desde el principio. Y con la difusión por suscripciones separadas, donde cada suscriptor recibe su copia. La clase obliga a decidir según el consumidor: ¿necesita repartir trabajo, difundir un hecho o reconstruir estado?

## Ejemplo

Un servicio recibe entregas y las manda a una cola para generar miniaturas. Tres procesos trabajadores compiten por los mensajes: si la cola se acumula, se añaden más procesos. Pero si un servicio de estadísticas también necesita ver cada entrega y se conecta a la misma cola, recibirá solo una parte de los mensajes y a los trabajadores les faltará esa parte. Para que ambos vean todo hace falta una suscripción por consumidor o un log.

## Errores y confusiones comunes

- **La mitad de los mensajes no llega a un consumidor**: dos consumidores comparten una cola; se corrige con suscripciones separadas para difundir ([SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md)).
- **Un servicio nuevo no ve datos anteriores**: el tópico no tiene retención; se corrige con un log o cargando la historia de otra fuente.
- **Esperar reprocesar tras confirmar**: el mensaje confirmado ya no existe.
- **Confundir competir con difundir**: son dos semánticas de entrega distintas.

## Límites y cuándo no aplica

No sirve cuando varios consumidores independientes necesitan cada mensaje, cuando hay que auditar o reproducir la historia, ni para reconstruir un estado: ahí corresponde un log, con retención o compactación. Tampoco garantiza por sí sola orden ni ausencia de duplicados; eso depende de la semántica de entrega y de que el consumidor sea idempotente. Para trabajo que cabe en una llamada síncrona corta, la cola añade complejidad innecesaria.

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
