# Clave de negocio

[↑ Glosario](../../README.md) · [← Clave de lista](./clave-de-lista.md) · [Clave del mensaje →](./clave-del-mensaje.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Identificador de la operación del dominio; reconoce repeticiones de la operación sea cual sea el mensaje que las trajo.

Definición de trabajo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md).

## Por qué importa

En [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), el tema «Clave del mensaje frente a clave de negocio» importa porque una reconoce reentregas; la otra, también las repeticiones con otro identificador.

## Cómo funciona

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

La **clave del mensaje** es el identificador que el corredor o el productor asigna al enviarlo; una tabla de mensajes vistos con esa clave reconoce cualquier **reentrega** del mismo mensaje. No reconoce un mensaje **distinto** que repite la misma operación, como el reintento del productor. La **clave de negocio** identifica la operación misma (la entrega y el intento, la calificación de una entrega): una restricción única sobre ella reconoce la repetición sea cual sea el mensaje que la trajo. La clave de negocio es más fuerte, pero exige saber qué identifica una operación, y esa es una decisión del dominio, no de la infraestructura.

## Ejemplo

Ejemplo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sección «Ejemplo mínimo»):

El fragmento prueba una defensa por clave de negocio contra un mensaje que llega dos veces con identificadores distintos. Antes de ejecutarlo, predice cuántas filas hay con y sin el índice único.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Duplicados del productor que pasan la defensa** — causa: la clave es el identificador del mensaje y el reintento trae otro. Corrección: clave de negocio única. ([SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La clave de negocio es más fuerte, pero exige saber qué identifica una operación, y esa es una decisión del dominio, no de la infraestructura. ([SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Operación](../o/operacion.md), [Repetición](../r/repeticion.md), [Actualización condicionada por versión](../a/actualizacion-condicionada-por-version.md), [Clave del mensaje](./clave-del-mensaje.md), [Plazo de visibilidad](../p/plazo-de-visibilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Amazon SQS: tiempo de visibilidad](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) — reentrega de un mensaje cuyo proceso supera el plazo; autoridad: Amazon Web Services.
- [EIP: Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html) — receptor que tolera mensajes repetidos; autoridad: autores del libro.
- [Stripe: peticiones idempotentes](https://docs.stripe.com/api/idempotent_requests) — clave reutilizada en los reintentos; autoridad: documentación oficial de Stripe.
- [SQLite: UPSERT](https://www.sqlite.org/lang_upsert.html) — inserción con conflicto y actualización condicionada; autoridad: documentación oficial de SQLite.
- [SQLite: cláusula ON CONFLICT](https://www.sqlite.org/lang_conflict.html) — `INSERT OR IGNORE` y `INSERT OR REPLACE`; autoridad: documentación oficial de SQLite.

---

[↑ Glosario](../../README.md) · [← Clave de lista](./clave-de-lista.md) · [Clave del mensaje →](./clave-del-mensaje.md)
