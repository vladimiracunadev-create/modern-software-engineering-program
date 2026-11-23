# Inyección de fallas

[↑ Glosario](../../README.md) · [← Inyección de dependencias](./inyeccion-de-dependencias.md) · [Inyección de fallos →](./inyeccion-de-fallos.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Introducir a propósito una falla controlada para comprobar la detección y la recuperación.

Definición de trabajo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md): Provocar a propósito caídas, duplicados, retrasos y mensajes inválidos para comprobar las invariantes.

## Por qué importa

En [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), el tema «Inyección de fallas» importa porque prueba que las alertas existen y suenan.

## Cómo funciona

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

Ensayar con inyección de fallas en un sistema que no tiene aún monitores ni runbook produce un incidente en lugar de un ensayo: primero el diseño y las pruebas por separado. En producción real, las fallas inyectadas necesitan límites (un segmento, una fracción, una hora acordada) y un acuerdo previo con quien está de guardia. Y el taller de esta clase usa un modelo y datos sintéticos en una máquina de escritorio: no sustituye un ensayo de recuperación completo con la infraestructura real (`SE-502`).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ensayar con inyección de fallas en un sistema que no tiene aún monitores ni runbook produce un incidente en lugar de un ensayo: primero el diseño y las pruebas por separado. ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Invariante](./invariante.md), [Recuperación](../r/recuperacion.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Exposición](../e/exposicion.md), [Falla inyectada](../f/falla-inyectada.md), [Horizonte de reintentos](../h/horizonte-de-reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md).

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

[↑ Glosario](../../README.md) · [← Inyección de dependencias](./inyeccion-de-dependencias.md) · [Inyección de fallos →](./inyeccion-de-fallos.md)
