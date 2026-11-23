# Semánticas de entrega

[↑ Glosario](../../README.md) · [← Semántica antes que sintaxis](./semantica-antes-que-sintaxis.md) · [Semiabierto →](./semiabierto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

**A lo sumo una vez**: el emisor envía y no reintenta; si el mensaje o el consumidor fallan, el mensaje se pierde, y nunca se duplica. **Al menos una vez**: el emisor reintenta hasta recibir un acuse; no se pierde, pero si se perdió el acuse y no el mensaje, el consumidor lo procesa de nuevo. Que el consumidor acuse **antes** o **después** de procesar define de qué lado cae un fallo del propio consumidor: acusar antes pierde el trabajo si cae, acusar después lo repite.

Explicación de la sección «Semánticas de entrega» de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Por qué importa

En [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), el tema «Semánticas de entrega» importa porque elegir perder o duplicar es una decisión de negocio, no de transporte.

En [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), el tema «Semánticas de entrega» importa porque decide si un fallo produce duplicados o pérdidas.

## Cómo funciona

Según [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), en la sección «Semánticas de entrega»:

**A lo sumo una vez**: el emisor envía y no reintenta; si el mensaje o el consumidor fallan, el mensaje se pierde, y nunca se duplica. **Al menos una vez**: el emisor reintenta hasta recibir un acuse; no se pierde, pero si se perdió el acuse y no el mensaje, el consumidor lo procesa de nuevo. Que el consumidor acuse **antes** o **después** de procesar define de qué lado cae un fallo del propio consumidor: acusar antes pierde el trabajo si cae, acusar después lo repite. No hay una tercera opción en el transporte: el emisor no puede distinguir «el mensaje no llegó» de «llegó y el acuse se perdió».

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), en la sección «Semánticas de entrega»:

Un consumidor ejecuta dos acciones: aplicar el efecto y confirmar a la cola que terminó. Si entre ambas se cae, el resultado depende del orden. **Aplicar y luego confirmar** da *al menos una vez*: tras la caída la cola reentrega y el efecto se repite. **Confirmar y luego aplicar** da *como mucho una vez*: tras la caída la cola cree que terminó y el efecto se pierde. **Exactamente una vez** entre dos sistemas independientes no es alcanzable sin una garantía adicional, porque la caída puede ocurrir entre las dos acciones sin que ninguno de los dos lo note. Lo que se puede lograr es *efecto único* sobre el estado: que la repetición no cambie el resultado.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

El equipo de la plataforma documenta tres consumidores. **Registro de calificaciones:** al menos una vez, acuse tras procesar, tabla `vistos` con clave del mensaje en la misma transacción que el efecto, guarda por versión de la entrega y ventana ilimitada mientras la entrega exista. **Aviso por correo:** al menos una vez con ventana de deduplicación de 24 horas, aceptando que una reentrega más tardía enviará un segundo correo, y guarda del estado «avisado» en la propia entrega.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md)) son:

- **Notas o avisos duplicados tras un incidente** — causa: entrega al menos una vez con efecto no idempotente. Corrección: clave de mensaje o forma idempotente del efecto en una transacción.
- **Mensajes que nunca se aplicaron** — causa: se acusó antes de procesar y el proceso cayó. Corrección: acusar después de procesar y hacer el efecto idempotente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor real ni red: las tasas de pérdida, los acuses, las caídas, el desplazamiento de los mensajes y la distribución de las reentregas son construcciones del autor, y los resultados no se extrapolan a ningún producto. Solo el registro de mensajes vistos usa un motor real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [A lo sumo una vez](../a/a-lo-sumo-una-vez.md), [Al menos una vez](../a/al-menos-una-vez.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Efecto único](../e/efecto-unico.md), [Guarda de versión](../g/guarda-de-version.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md).

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

[↑ Glosario](../../README.md) · [← Semántica antes que sintaxis](./semantica-antes-que-sintaxis.md) · [Semiabierto →](./semiabierto.md)
