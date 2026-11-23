# Cola de mensajes fallidos

[↑ Glosario](../../README.md) · [← Cola de integración](./cola-de-integracion.md) · [Cola de muertos →](./cola-de-muertos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Destino de los mensajes que no se pudieron procesar tras un número de intentos, para su revisión.

Definición de trabajo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Por qué importa

La clase donde se define, [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), existe con este propósito: el proyecto existe para que entregues un flujo de integración completo cuyas garantías puedas defender con medidas: el paquete reúne contratos de mensaje, clave de idempotencia, política de reintentos, cola de mensajes fallidos, compatibilidad de esquemas, outbox e inbox, observabilidad, seguridad y límites, y lo acompañas de un validador cuyos puntos ciegos conoces, una simulación con fallas inyectadas que compara el flujo ingenuo con el tolerante y un cálculo de qué carga recibe un servicio cuando todos los mensajes reintentan a la vez.

## Cómo funciona

[SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md):

El equipo de la plataforma cierra el proyecto con cuatro entregables. **`PAQUETE-INTEGRACION.md`:** nueve secciones; los contratos de `EntregaRecibida` y `CalificacionPublicada` con su sobre; la clave de idempotencia `(entrega, intento)`; cinco intentos con esperas de 1, 5, 30, 120 y 600 s con aleatoriedad completa (horizonte máximo 756 s); la cola `entregas_fallidas` con alarma y dueño; reglas de evolución compatibles hacia atrás y hacia adelante; outbox e inbox con clave única; señales de profundidad, edad, procesados y errores; firma con marca de tiempo y registros con lista de permitidos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un solo mensaje detiene el flujo** — causa: no hay cola de mensajes fallidos. Corrección: desviar tras N intentos con alarma y dueño. ([SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red, concurrencia ni medición de tiempo de reloj: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, las fallas inyectadas y sus tasas son del autor y todos los mensajes fallan a la vez en el cálculo de la tormenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Revisión](../r/revision.md), [Falla inyectada](../f/falla-inyectada.md), [Horizonte de reintentos](../h/horizonte-de-reintentos.md), [Invariante del flujo](../i/invariante-del-flujo.md), [Inyección de fallas](../i/inyeccion-de-fallas.md), [Paquete de integración](../p/paquete-de-integracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md), [SE-375](../../../classes/part-31-integracion-eventos-y-mensajeria/se-375-brokers-colas-topics-y-logs-distribuidos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — apartar mensajes que no se pueden procesar; autoridad: Amazon Web Services.
- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y aleatoriedad; autoridad: Amazon Web Services.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — outbox y relevo; autoridad: Chris Richardson, autor del catálogo.
- [EIP: Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) — canal de mensajes no procesables; autoridad: autores del libro.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Cola de integración](./cola-de-integracion.md) · [Cola de muertos →](./cola-de-muertos.md)
