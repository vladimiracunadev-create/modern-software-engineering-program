# Invariante del flujo

[↑ Glosario](../../README.md) · [← Invariante de migración](./invariante-de-migracion.md) · [Invariantes alrededor de transiciones →](./invariantes-alrededor-de-transiciones.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Una **invariante del flujo** es una propiedad que debe cumplirse sin importar las fallas, por ejemplo que cada entrega tenga exactamente una calificación ([SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)). Es la afirmación contra la cual se comprueba un flujo de integración: sin ella, «el flujo funciona» no es algo que se pueda verificar.

## Por qué importa

Un flujo basado en mensajes puede perder, duplicar, retrasar o reordenar. Si no se dice qué se espera pase lo que pase, cualquier resultado parece aceptable y los fallos aparecen en producción. La decisión que cambia es el orden del trabajo: primero se escribe lo que debe ser cierto, después se diseña y se prueba que lo sea.

## Cómo funciona

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) enumera cinco invariantes del flujo de la plataforma de entregas:

1. **Cada entrega recibida tiene exactamente una calificación** (ni cero ni dos).
2. **Cada calificación publicada produce como mucho un aviso**, y eventualmente uno.
3. **Un mensaje que no se puede procesar no detiene a los demás.**
4. **El estado final de una entrega no depende del orden de llegada de sus mensajes.**
5. **Todo mensaje fallido es visible y recuperable.**

Cada una conecta con un mecanismo de las clases: la primera con el outbox, la segunda con la inbox y la política del notificador, la tercera con la cola de mensajes fallidos, la cuarta con la guarda de versión y la quinta con la observabilidad. Esa correspondencia es lo que las hace útiles: cada invariante señala qué mecanismo la sostiene y qué prueba la demostraría.

La comprobación se hace con **inyección de fallas**: se provocan caídas, duplicados, retrasos y mensajes inválidos y se mira si las cinco siguen cumpliéndose. Una invariante que se viola con una falla concreta indica qué mecanismo falta.

## Ejemplo

Se inyecta una caída del consumidor a mitad de un lote y reentregas duplicadas. Se comprueba entonces la invariante 1 contando, por cada entrega, cuántas calificaciones hay: debe ser exactamente una. Si aparece una segunda, falta idempotencia en el consumidor. Si hay cero, falta el outbox o la recuperación. Procedimiento de [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Errores y confusiones comunes

- **Duplicados minutos después del original**: ventana de deduplicación menor que el horizonte de reintentos; se corrige con una ventana mayor que el horizonte máximo, con la aleatoriedad incluida.
- **Un solo mensaje detiene el flujo**: no hay cola de mensajes fallidos; se corrige desviando tras N intentos con alarma y dueño.
- **Escribir invariantes vagas** («que funcione bien») que no se pueden comprobar.
- **Confundirlas con aserciones de una prueba unitaria**: se comprueban sobre el flujo completo bajo fallas.

## Límites y cuándo no aplica

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) aclara que sus experimentos usan datos sintéticos, sin corredor, red ni concurrencia: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, y las fallas inyectadas y sus tasas son del autor. Las cinco invariantes son las de ese flujo; otro sistema tendrá otras. Una invariante comprobada bajo las fallas que se probaron no garantiza las que no se probaron.

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
