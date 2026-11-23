# Guarda de versión

[↑ Glosario](../../README.md) · [← Guarda](./guarda.md) · [Guardia →](./guardia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Regla que aplica un mensaje solo si su versión es mayor que la ya aplicada a esa entidad.

Definición de trabajo de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Por qué importa

La clase donde se define, [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), existe con este propósito: la clase existe para que dejes de pedir «exactamente una vez» como si fuera una propiedad del transporte y lo trates como una propiedad del **efecto**: aprenderás a medir cuántos mensajes se pierden o se duplican bajo cada semántica de entrega, cuántos estados finales equivocados produce el desorden y qué ventana de deduplicación basta, antes de que un consumidor dependa de una garantía que el corredor no da.

## Cómo funciona

Según [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

Con un desplazamiento de solo 3 posiciones, 135 de las 500 entradas (27 %) terminan con un valor viejo; con 50 son 416 (83 %). La guarda de versión deja cero en todos los casos porque convierte un problema de orden en la comparación de dos enteros. El estado final es correcto aunque se hayan aplicado los mensajes desordenados; las transiciones intermedias, en cambio, no se reconstruyen.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md):

El equipo de la plataforma documenta tres consumidores. **Registro de calificaciones:** al menos una vez, acuse tras procesar, tabla `vistos` con clave del mensaje en la misma transacción que el efecto, guarda por versión de la entrega y ventana ilimitada mientras la entrega exista. **Aviso por correo:** al menos una vez con ventana de deduplicación de 24 horas, aceptando que una reentrega más tardía enviará un segundo correo, y guarda del estado «avisado» en la propia entrega.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El estado final depende del orden de llegada** — causa: se aplica el último mensaje recibido. Corrección: versión por entidad y guarda de versión. ([SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor real ni red: las tasas de pérdida, los acuses, las caídas, el desplazamiento de los mensajes y la distribución de las reentregas son construcciones del autor, y los resultados no se extrapolan a ningún producto. Solo el registro de mensajes vistos usa un motor real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Versión](../v/version.md), [A lo sumo una vez](../a/a-lo-sumo-una-vez.md), [Al menos una vez](../a/al-menos-una-vez.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Ventana de deduplicación](../v/ventana-de-deduplicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-376 — Entrega, orden, duplicación y semánticas](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

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

[↑ Glosario](../../README.md) · [← Guarda](./guarda.md) · [Guardia →](./guardia.md)
