# Falla inyectada

[↑ Glosario](../../README.md) · [← Fake / doble con estado](./fake-doble-con-estado.md) · [Fallo espurio →](./fallo-espurio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Condición adversa introducida de forma deliberada y controlada para observar el comportamiento del sistema.

Definición de trabajo de [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md).

## Por qué importa

En [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), el tema «Fallas inyectadas» importa porque muestran qué defensa falta cuando varias fallas se combinan.

## Cómo funciona

Según [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), en la sección «Fallas inyectadas»:

La prueba que sustituye a la fe en el documento es **inyectar fallas** al flujo completo y comprobar las invariantes: caídas del relevo entre publicar y marcar, duplicados y desorden del corredor, caídas del consumidor antes de acusar, mensajes venenosos y un servicio de avisos caído durante parte del flujo. Comparar un flujo **ingenuo** (publicación directa tras confirmar, consumidor sin deduplicación ni versión, sin cola de fallidos, avisos sin control) con el **tolerante** (outbox, inbox, versión, cola de fallidos, avisos reconciliados) muestra qué defensa evita qué daño. Cada falla inyectada es una hipótesis sobre el mundo; las que no se inyectaron quedan fuera de la conclusión y se anotan.

## Ejemplo

Ejemplo de [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sección «Preguntas frecuentes»):

No. La simulación demuestra que las defensas funcionan juntas bajo las fallas inyectadas en un proceso, sin concurrencia, red ni carga. Antes de producción hacen falta pruebas con el corredor real, con concurrencia y con volúmenes, y un ensayo de recuperación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md)) son:

- **Duplicados minutos después del original** — causa: ventana de deduplicación menor que el horizonte de reintentos. Corrección: ventana mayor que el horizonte máximo, con la aleatoriedad incluida.
- **Un solo mensaje detiene el flujo** — causa: no hay cola de mensajes fallidos. Corrección: desviar tras N intentos con alarma y dueño.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada falla inyectada es una hipótesis sobre el mundo; las que no se inyectaron quedan fuera de la conclusión y se anotan. ([SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Cola de mensajes fallidos](../c/cola-de-mensajes-fallidos.md), [Desfase de reloj](../d/desfase-de-reloj.md), [Horizonte de reintentos](../h/horizonte-de-reintentos.md), [Huella de una falla](../h/huella-de-una-falla.md), [Invariante del flujo](../i/invariante-del-flujo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-384 — Proyecto: flujo integrado tolerante a reintentos](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-508 — Fallos de recursos e infraestructura: CPU, memoria, disco y nodos](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-507](../../../classes/part-42-ingenieria-del-caos/se-507-inyeccion-de-fallos-de-red-latencia-y-dependencias/README.md), [SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Fallas inyectadas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — retroceso exponencial y aleatoriedad; autoridad: Amazon Web Services.
- [Amazon SQS: colas de mensajes fallidos](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html) — apartar mensajes que no se pueden procesar; autoridad: Amazon Web Services.
- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — outbox y relevo; autoridad: Chris Richardson, autor del catálogo.
- [EIP: Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) — canal de mensajes no procesables; autoridad: autores del libro.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.

---

[↑ Glosario](../../README.md) · [← Fake / doble con estado](./fake-doble-con-estado.md) · [Fallo espurio →](./fallo-espurio.md)
