# Efecto único

[↑ Glosario](../../README.md) · [← Efecto sistémico](./efecto-sistemico.md) · [Efectos en los bordes →](./efectos-en-los-bordes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Garantía de que, aunque un mensaje se procese varias veces, su efecto sobre el estado ocurre una sola vez.

Definición de trabajo de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md).

## Por qué importa

La clase donde se define, [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), existe con este propósito: la clase existe para que sustituyas la promesa imposible de «exactamente una vez» por una que sí puedes cumplir: efecto único sobre el estado, logrado con operaciones idempotentes y con claves que permiten reconocer un duplicado, y para que diseñes el procesamiento por lotes y por mensajes de modo que un reintento sea una repetición inofensiva y no una segunda verdad.

## Cómo funciona

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

Un consumidor ejecuta dos acciones: aplicar el efecto y confirmar a la cola que terminó. Si entre ambas se cae, el resultado depende del orden. **Aplicar y luego confirmar** da *al menos una vez*: tras la caída la cola reentrega y el efecto se repite. **Confirmar y luego aplicar** da *como mucho una vez*: tras la caída la cola cree que terminó y el efecto se pierde. **Exactamente una vez** entre dos sistemas independientes no es alcanzable sin una garantía adicional, porque la caída puede ocurrir entre las dos acciones sin que ninguno de los dos lo note. Lo que se puede lograr es *efecto único* sobre el estado: que la repetición no cambie el resultado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

El equipo del panel clasifica las operaciones. «Marcar una entrega como recibida» pasa de «sumar uno» a «insertar la entrega con su identificador», con clave primaria: el contador del panel se calcula contando filas, de modo que un mensaje repetido no cambia nada. «Enviar el acuse por correo» no es idempotente por naturaleza: lleva una clave `acuse-<entrega>` guardada con el resultado en la misma transacción que marca el envío, con una retención de 7 días justificada por el retraso máximo observado de reentregas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)) son:

- **Contadores por encima de lo real** — causa: mensajes reentregados aplicados dos veces. Corrección: clave en la misma transacción que el efecto.
- **Contadores por debajo de lo real** — causa: confirmar antes de aplicar. Corrección: aplicar y recordar, luego confirmar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo que se puede lograr es *efecto único* sobre el estado: que la repetición no cambie el resultado. ([SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](./efecto.md), [Estado](./estado.md), [Garantía](../g/garantia.md), [Sobre](../s/sobre.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Huella del cuerpo](../h/huella-del-cuerpo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

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

[↑ Glosario](../../README.md) · [← Efecto sistémico](./efecto-sistemico.md) · [Efectos en los bordes →](./efectos-en-los-bordes.md)
