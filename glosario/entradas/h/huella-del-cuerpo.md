# Huella del cuerpo

[↑ Glosario](../../README.md) · [← Huella de una falla](./huella-de-una-falla.md) · [Huella o digest →](./huella-o-digest.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Resumen del contenido de una petición, guardado con la clave para detectar su reutilización con otro contenido.

Definición de trabajo de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md).

## Por qué importa

La clase donde se define, [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), existe con este propósito: la clase existe para que sustituyas la promesa imposible de «exactamente una vez» por una que sí puedes cumplir: efecto único sobre el estado, logrado con operaciones idempotentes y con claves que permiten reconocer un duplicado, y para que diseñes el procesamiento por lotes y por mensajes de modo que un reintento sea una repetición inofensiva y no una segunda verdad.

## Cómo funciona

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

Una **clave de idempotencia** es un identificador que el cliente genera una vez para una intención y reutiliza en todos los reintentos; el servidor guarda la clave con la huella del cuerpo y el resultado, y si la ve de nuevo devuelve el resultado guardado sin repetir el efecto. Dos detalles la hacen segura. Primero, la **huella del cuerpo**: si llega la misma clave con otro cuerpo, es un error del cliente (reutilizó una clave) y debe rechazarse, no devolver la respuesta de otra petición. Segundo, la **atomicidad**: guardar la clave y aplicar el efecto deben ocurrir en la misma transacción; si se hacen por separado, una caída entre ambas deja un efecto sin clave o una clave sin efecto.

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

El equipo del panel clasifica las operaciones. «Marcar una entrega como recibida» pasa de «sumar uno» a «insertar la entrega con su identificador», con clave primaria: el contador del panel se calcula contando filas, de modo que un mensaje repetido no cambia nada. «Enviar el acuse por correo» no es idempotente por naturaleza: lleva una clave `acuse-<entrega>` guardada con el resultado en la misma transacción que marca el envío, con una retención de 7 días justificada por el retraso máximo observado de reentregas. La API pública acepta una cabecera de clave, guarda la huella del cuerpo y responde con error si se reutiliza con otro contenido.

## Ejemplo

Ejemplo de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) (sección «Ejemplo profesional»):

El equipo del panel clasifica las operaciones. «Marcar una entrega como recibida» pasa de «sumar uno» a «insertar la entrega con su identificador», con clave primaria: el contador del panel se calcula contando filas, de modo que un mensaje repetido no cambia nada. «Enviar el acuse por correo» no es idempotente por naturaleza: lleva una clave `acuse-<entrega>` guardada con el resultado en la misma transacción que marca el envío, con una retención de 7 días justificada por el retraso máximo observado de reentregas. La API pública acepta una cabecera de clave, guarda la huella del cuerpo y responde con error si se reutiliza con otro contenido.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una clave devuelve la respuesta de otra petición** — causa: falta la huella del cuerpo. Corrección: guardar y comparar la huella. ([SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **clave de idempotencia** es un identificador que el cliente genera una vez para una intención y reutiliza en todos los reintentos; el servidor guarda la clave con la huella del cuerpo y el resultado, y si la ve de nuevo devuelve el resultado guardado sin repetir el efecto. ([SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de idempotencia](../c/clave-de-idempotencia.md), [Efecto único](../e/efecto-unico.md), [Idempotencia](../i/idempotencia.md), [Operaciones idempotentes](../o/operaciones-idempotentes.md), [Tarea determinista](../t/tarea-determinista.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Helland, «Idempotence is not a medical condition»](https://doi.org/10.1145/2181796.2187821) — diseño de aplicaciones tolerantes a repeticiones; autoridad: artículo de ACM Queue (2012).
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes; autoridad: IETF.
- [Stripe: idempotencia](https://stripe.com/blog/idempotency) — claves enviadas por el cliente; autoridad: Stripe.
- [IETF: cabecera Idempotency-Key](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — borrador de estandarización; autoridad: IETF (borrador).
- [Dean y Ghemawat, «MapReduce»](https://doi.org/10.1145/1327452.1327492) — reintento de tareas y salida atómica; autoridad: artículo original.

---

[↑ Glosario](../../README.md) · [← Huella de una falla](./huella-de-una-falla.md) · [Huella o digest →](./huella-o-digest.md)
