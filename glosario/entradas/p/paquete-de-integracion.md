# Paquete de integración

[↑ Glosario](../../README.md) · [← Paquete de informe](./paquete-de-informe.md) · [Paquete de migración →](./paquete-de-migracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Documento con las nueve secciones que describen el contrato, las defensas y los límites de un flujo de mensajes.

Definición de trabajo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Por qué importa

La clase donde se define, [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), existe con este propósito: el proyecto existe para que entregues un flujo de integración completo cuyas garantías puedas defender con medidas: el paquete reúne contratos de mensaje, clave de idempotencia, política de reintentos, cola de mensajes fallidos, compatibilidad de esquemas, outbox e inbox, observabilidad, seguridad y límites, y lo acompañas de un validador cuyos puntos ciegos conoces, una simulación con fallas inyectadas que compara el flujo ingenuo con el tolerante y un cálculo de qué carga recibe un servicio cuando todos los mensajes reintentan a la vez.

## Cómo funciona

Según [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md):

El **paquete de integración** es un documento corto con nueve secciones fijas que responde, para el flujo de la plataforma, a las preguntas de la parte. El **validador** lee el paquete y comprueba lo que se puede comprobar de forma mecánica: que existan las secciones y no estén vacías, que los parámetros numéricos sean coherentes entre sí y que aparezcan los elementos mínimos (una cola de fallidos, una firma, una restricción única en la inbox, una declaración de límites). No puede comprobar si lo que el documento afirma es verdad ni si la palabra «HMAC» significa que se verifica una firma. Un validador que pasa dice que la forma es completa y las cifras coinciden; no dice que el flujo sea correcto.

## Ejemplo

Ejemplo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sección «Caso conductor»):

El flujo de entrega, calificación, aviso y registro de la plataforma es el caso conductor de la [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md) y este proyecto lo cierra. El paquete de integración conecta con la [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), que lleva estos mensajes a la concurrencia y a los sistemas distribuidos: lo que aquí fueron simulaciones de un solo proceso será allí varias máquinas con relojes distintos y particiones de red. Cambia después una sola decisión, la política de reintentos, y observa qué parámetro del paquete deja de ser coherente con otro.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son:

- **Duplicados minutos después del original** — causa: ventana de deduplicación menor que el horizonte de reintentos. Corrección: ventana mayor que el horizonte máximo, con la aleatoriedad incluida.
- **Un solo mensaje detiene el flujo** — causa: no hay cola de mensajes fallidos. Corrección: desviar tras N intentos con alarma y dueño.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún corredor, red, concurrencia ni medición de tiempo de reloj: el paquete es un texto sintético, el validador se ajustó con los mismos casos que lo evalúan, las fallas inyectadas y sus tasas son del autor y todos los mensajes fallan a la vez en el cálculo de la tormenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Documento](../d/documento.md), [Flujo](../f/flujo.md), [Límite](../l/limite.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Falla inyectada](../f/falla-inyectada.md).
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

[↑ Glosario](../../README.md) · [← Paquete de informe](./paquete-de-informe.md) · [Paquete de migración →](./paquete-de-migracion.md)
