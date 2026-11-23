# Clave del mensaje

[↑ Glosario](../../README.md) · [← Clave de negocio](./clave-de-negocio.md) · [Clave foránea →](./clave-foranea.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Identificador asignado a un mensaje concreto al enviarlo; reconoce reentregas de ese mensaje.

Definición de trabajo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md).

## Por qué importa

En [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), el tema «Clave del mensaje frente a clave de negocio» importa porque una reconoce reentregas; la otra, también las repeticiones con otro identificador.

## Cómo funciona

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

La **clave del mensaje** es el identificador que el corredor o el productor asigna al enviarlo; una tabla de mensajes vistos con esa clave reconoce cualquier **reentrega** del mismo mensaje. No reconoce un mensaje **distinto** que repite la misma operación, como el reintento del productor. La **clave de negocio** identifica la operación misma (la entrega y el intento, la calificación de una entrega): una restricción única sobre ella reconoce la repetición sea cual sea el mensaje que la trajo. La clave de negocio es más fuerte, pero exige saber qué identifica una operación, y esa es una decisión del dominio, no de la infraestructura.

Según [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md):

El equipo reproduce el incidente de las 87 calificaciones dobles con el taller. Primero ejecutan las cinco provocaciones y observan que la configuración del plazo de visibilidad produce más duplicados que cualquier fallo; ajustan el plazo a tres veces el percentil 99 del tiempo de proceso y añaden una extensión del plazo para tareas largas. Después aplican como defensa principal el índice único por `(entrega, intento)` sobre las calificaciones, porque el servicio de entregas puede reintentar con un nuevo identificador y la clave del mensaje no lo cubre; la tabla de mensajes vistos queda como segunda capa para los efectos externos (los correos). Guardan clave y efecto en una sola transacción, y escriben una prueba que inyecta una caída entre ambos pasos.

## Ejemplo

Ejemplo de [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) (sección «Ejemplo profesional»):

El equipo reproduce el incidente de las 87 calificaciones dobles con el taller. Primero ejecutan las cinco provocaciones y observan que la configuración del plazo de visibilidad produce más duplicados que cualquier fallo; ajustan el plazo a tres veces el percentil 99 del tiempo de proceso y añaden una extensión del plazo para tareas largas. Después aplican como defensa principal el índice único por `(entrega, intento)` sobre las calificaciones, porque el servicio de entregas puede reintentar con un nuevo identificador y la clave del mensaje no lo cubre; la tabla de mensajes vistos queda como segunda capa para los efectos externos (los correos).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md)) son:

- **Efectos que nunca se aplican, sin error** — causa: la clave se guardó antes que el efecto, en otra transacción. Corrección: clave y efecto en una sola transacción.
- **Efectos duplicados tras una caída** — causa: el efecto se aplicó antes de guardar la clave. Corrección: clave y efecto en una sola transacción.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada fila es una defensa y cada columna una causa del duplicado; cuanto más oscura la celda, más duplicados quedan, y el contorno marca el hueco de la clave del mensaje. ([SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actualización condicionada por versión](../a/actualizacion-condicionada-por-version.md), [Clave de negocio](./clave-de-negocio.md), [Plazo de visibilidad](../p/plazo-de-visibilidad.md), [Transacción única de clave y efecto](../t/transaccion-unica-de-clave-y-efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-383 — Taller: provocar y contener mensajes duplicados](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md).

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

[↑ Glosario](../../README.md) · [← Clave de negocio](./clave-de-negocio.md) · [Clave foránea →](./clave-foranea.md)
