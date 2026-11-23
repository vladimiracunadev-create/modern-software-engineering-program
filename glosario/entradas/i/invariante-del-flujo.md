# Invariante del flujo

[↑ Glosario](../../README.md) · [← Invariante de migración](./invariante-de-migracion.md) · [Invariantes alrededor de transiciones →](./invariantes-alrededor-de-transiciones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Propiedad que debe cumplirse sin importar las fallas, como que cada entrega tenga exactamente una calificación.

Definición de trabajo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Por qué importa

En [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), el tema «Invariantes del flujo» importa porque definen qué significa «correcto» antes de provocar fallas.

## Cómo funciona

Según [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), en la sección «Invariantes del flujo»:

Antes de probar hay que decir qué se espera. Las invariantes del flujo de la plataforma son cinco: **cada entrega recibida tiene exactamente una calificación** (ni cero ni dos), **cada calificación publicada produce como mucho un aviso** y eventualmente uno, **un mensaje que no se puede procesar no detiene a los demás**, **el estado final de una entrega no depende del orden de llegada de sus mensajes** y **todo mensaje fallido es visible y recuperable**. Cada invariante conecta con una clase: la primera con el outbox, la segunda con la inbox y la política del notificador, la tercera con la cola de fallidos, la cuarta con la guarda de versión y la quinta con la observabilidad. Sin invariantes escritas, «el flujo funciona» no es una afirmación comprobable.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md):

El equipo de la plataforma cierra el proyecto con cuatro entregables. **`PAQUETE-INTEGRACION.md`:** nueve secciones; los contratos de `EntregaRecibida` y `CalificacionPublicada` con su sobre; la clave de idempotencia `(entrega, intento)`; cinco intentos con esperas de 1, 5, 30, 120 y 600 s con aleatoriedad completa (horizonte máximo 756 s); la cola `entregas_fallidas` con alarma y dueño; reglas de evolución compatibles hacia atrás y hacia adelante; outbox e inbox con clave única; señales de profundidad, edad, procesados y errores; firma con marca de tiempo y registros con lista de permitidos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son:

- **Duplicados minutos después del original** — causa: ventana de deduplicación menor que el horizonte de reintentos. Corrección: ventana mayor que el horizonte máximo, con la aleatoriedad incluida.
- **Un solo mensaje detiene el flujo** — causa: no hay cola de mensajes fallidos. Corrección: desviar tras N intentos con alarma y dueño.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red, concurrencia ni medición de tiempo de reloj: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, las fallas inyectadas y sus tasas son del autor y todos los mensajes fallan a la vez en el cálculo de la tormenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propiedad](../p/propiedad.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Falla inyectada](../f/falla-inyectada.md), [Horizonte de reintentos](../h/horizonte-de-reintentos.md), [Inyección de fallas](./inyeccion-de-fallas.md), [Paquete de integración](../p/paquete-de-integracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Invariantes del flujo».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y aleatoriedad; autoridad: Amazon Web Services.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — apartar mensajes que no se pueden procesar; autoridad: Amazon Web Services.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — outbox y relevo; autoridad: Chris Richardson, autor del catálogo.
- [EIP: Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) — canal de mensajes no procesables; autoridad: autores del libro.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Invariante de migración](./invariante-de-migracion.md) · [Invariantes alrededor de transiciones →](./invariantes-alrededor-de-transiciones.md)
