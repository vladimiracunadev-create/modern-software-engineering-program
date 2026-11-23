# Backlog

[↑ Glosario](../../README.md) · [← Backfill](./backfill.md) · [Backoff →](./backoff.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Conjunto de mensajes aceptados y no procesados; crece a la diferencia entre llegada y capacidad.

Definición de trabajo de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md).

## Por qué importa

La clase donde se define, [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md), existe con este propósito: la clase existe para que elijas entre esperar la respuesta de otro componente y dejarle un mensaje con criterios medibles, en lugar de por costumbre o por moda: cuánto baja la disponibilidad cuando una petición cruza varias dependencias, cuánta carga añaden los reintentos apilados y cuánto tarda en recuperarse una cola después de una caída.

## Cómo funciona

Según [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

Una cola absorbe una diferencia temporal entre la llegada y el procesamiento. Mientras el consumidor está caído, el backlog crece a la tasa de llegada; cuando vuelve, se vacía a la diferencia entre su capacidad y la llegada. Si la capacidad es igual a la llegada, **no se vacía nunca**; si la supera por poco, tarda mucho. La cola necesita además un límite o una señal de contrapresión: sin ellos, una caída larga produce un backlog que supera la memoria o la utilidad de los mensajes (una nota que llega tres horas tarde puede ya no importar). Decidir qué hacer cuando la cola se llena (rechazar, descartar los más viejos, degradar) es parte del diseño.

Según [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md):

No. Mejora la disponibilidad **del emisor** frente a la caída de un receptor, pero añade un componente que también falla y exige operar el backlog. La clase mide que el límite de éxito pasa a ser el de la propia cola; lo que gana el usuario es no ver errores por fallos de otros servicios, a cambio de resultados con retraso.

## Ejemplo

Ejemplo de [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) (sección «Preguntas frecuentes»):

No. Mejora la disponibilidad **del emisor** frente a la caída de un receptor, pero añade un componente que también falla y exige operar el backlog. La clase mide que el límite de éxito pasa a ser el de la propia cola; lo que gana el usuario es no ver errores por fallos de otros servicios, a cambio de resultados con retraso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La cola nunca se vacía después de una caída** — causa: capacidad igual a la llegada media. Corrección: dimensionar con holgura para recuperar el backlog en un tiempo objetivo. ([SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La cola necesita además un límite o una señal de contrapresión: sin ellos, una caída larga produce un backlog que supera la memoria o la utilidad de los mensajes (una nota que llega tres horas tarde puede ya no importar). ([SE-373](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-360](../../../classes/part-29-datos-persistencia-y-recuperacion/se-360-proyecto-capa-de-datos-recuperable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Conjunto](../c/conjunto.md), [Acoplamiento temporal](../a/acoplamiento-temporal.md), [Amplificación de reintentos](../a/amplificacion-de-reintentos.md), [Disponibilidad en cadena](../d/disponibilidad-en-cadena.md), [Presupuesto de reintentos](../p/presupuesto-de-reintentos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-373 — Integración síncrona y asíncrona](../../../classes/part-31-integracion-eventos-y-mensajeria/se-373-integracion-sincrona-y-asincrona/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md), [SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Hohpe y Woolf, «Enterprise Integration Patterns»](https://www.enterpriseintegrationpatterns.com/) — catálogo de patrones de mensajería frente a invocación remota; autoridad: autores del libro.
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes y reintentos automáticos; autoridad: IETF.
- [AWS Builders' Library: timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — amplificación de reintentos y retroceso con aleatoriedad; autoridad: Amazon Web Services.
- [Google SRE: addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/) — reintentos y fallos en cascada; autoridad: Google.
- [Helland, «Life beyond distributed transactions»](https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf) — diseño con mensajes entre entidades sin transacción compartida; autoridad: artículo del autor (CIDR 2007).

---

[↑ Glosario](../../README.md) · [← Backfill](./backfill.md) · [Backoff →](./backoff.md)
