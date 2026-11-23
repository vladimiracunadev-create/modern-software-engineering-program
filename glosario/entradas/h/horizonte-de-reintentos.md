# Horizonte de reintentos

[↑ Glosario](../../README.md) · [← Horizonte de predictibilidad](./horizonte-de-predictibilidad.md) · [Hot path →](./hot-path.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Tiempo total durante el cual un emisor puede reenviar un mensaje, la suma de sus esperas.

Definición de trabajo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Por qué importa

La clase donde se define, [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), existe con este propósito: el proyecto existe para que entregues un flujo de integración completo cuyas garantías puedas defender con medidas: el paquete reúne contratos de mensaje, clave de idempotencia, política de reintentos, cola de mensajes fallidos, compatibilidad de esquemas, outbox e inbox, observabilidad, seguridad y límites, y lo acompañas de un validador cuyos puntos ciegos conoces, una simulación con fallas inyectadas que compara el flujo ingenuo con el tolerante y un cálculo de qué carga recibe un servicio cuando todos los mensajes reintentan a la vez.

## Cómo funciona

Según [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md):

Las defensas tienen parámetros que se condicionan entre sí. La **ventana de deduplicación** debe ser mayor que el **horizonte de reintentos** (la suma de las esperas): si el emisor puede reintentar durante 756 segundos y la inbox olvida los identificadores a los 60, los reintentos tardíos pasan. El **número de esperas** debe coincidir con el **número de intentos**: un calendario de tres esperas con cinco intentos deja dos sin definir. El **plazo de visibilidad** debe superar el percentil 99 del tiempo de proceso (`SE-383`). El **jitter** extiende el horizonte real por encima del nominal. Estas relaciones se comprueban con aritmética y por eso un validador puede verificarlas; lo que no puede verificar es si los valores son los correctos para la carga real.

Según [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md):

Reproduce el fallo clásico del proyecto: **una ventana de deduplicación menor que el horizonte de reintentos**. Configura la inbox para olvidar los identificadores a los 60 segundos con reintentos que se extienden hasta 756.

## Ejemplo

Ejemplo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sección «Ejemplo mínimo»):

El fragmento comprueba la coherencia entre la ventana de deduplicación y el horizonte de reintentos. Antes de ejecutarlo, predice qué ocurre si la ventana es de 600 s.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Duplicados minutos después del original** — causa: ventana de deduplicación menor que el horizonte de reintentos. Corrección: ventana mayor que el horizonte máximo, con la aleatoriedad incluida. ([SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red, concurrencia ni medición de tiempo de reloj: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, las fallas inyectadas y sus tasas son del autor y todos los mensajes fallan a la vez en el cálculo de la tormenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Falla inyectada](../f/falla-inyectada.md), [Invariante del flujo](../i/invariante-del-flujo.md), [Inyección de fallas](../i/inyeccion-de-fallas.md), [Paquete de integración](../p/paquete-de-integracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y aleatoriedad; autoridad: Amazon Web Services.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — apartar mensajes que no se pueden procesar; autoridad: Amazon Web Services.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — outbox y relevo; autoridad: Chris Richardson, autor del catálogo.
- [EIP: Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) — canal de mensajes no procesables; autoridad: autores del libro.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Horizonte de predictibilidad](./horizonte-de-predictibilidad.md) · [Hot path →](./hot-path.md)
