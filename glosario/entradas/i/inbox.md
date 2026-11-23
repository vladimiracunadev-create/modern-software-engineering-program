# Inbox

[↑ Glosario](../../README.md) · [← Importe en unidad mínima](./importe-en-unidad-minima.md) · [Incertidumbre →](./incertidumbre.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Tabla del receptor que registra los identificadores de los mensajes aplicados, con clave única, junto con el efecto.

Definición de trabajo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Por qué importa

En [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), el tema «Inbox y relevo» importa porque el relevo duplica; la inbox convierte duplicados en un solo efecto.

## Cómo funciona

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El relevo puede caerse **entre publicar y marcar**, y entonces vuelve a publicar la misma fila: el outbox da entrega al menos una vez. La alternativa de marcar primero y publicar después convierte la caída en una pérdida silenciosa, y una pérdida no deja rastro que se pueda reparar. Por eso el relevo debe preferir **duplicar** a **perder**, y el receptor lleva una **inbox**: una tabla con el identificador del mensaje como clave primaria, insertada en la misma transacción que el efecto. El `INSERT OR IGNORE` sobre esa clave convierte el duplicado en una operación sin efecto. Es la misma defensa de `SE-376`, ahora con su pareja del lado emisor.

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Ejemplo

Ejemplo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Mensajes perdidos sin rastro** — causa: el relevo marca antes de publicar. Corrección: publicar y luego marcar; inbox en el receptor. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))
- **Cada caída del relevo duplica efectos** — causa: receptor sin inbox. Corrección: clave única por mensaje en la misma transacción del efecto. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No cambies a la vez el relevo y la inbox. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Compensación](../c/compensacion.md), [Doble escritura](../d/doble-escritura.md), [Outbox transaccional](../o/outbox-transaccional.md), [Pivote](../p/pivote.md), [Relevo](../r/relevo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [microservices.io: Transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html) — patrón del outbox y su relevo; autoridad: Chris Richardson, autor del catálogo.
- [Debezium: Outbox Event Router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html) — implementación del outbox sobre el registro de cambios; autoridad: proyecto Debezium.
- [Garcia-Molina y Salem, «Sagas»](https://dl.acm.org/doi/10.1145/38713.38742) — subtransacciones con compensaciones; autoridad: artículo original (SIGMOD 1987; metadatos verificados con Crossref, el editor bloquea las peticiones automáticas).
- [Microsoft: patrón Saga](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) — sagas coreografiadas y orquestadas; autoridad: documentación de Microsoft.
- [Microsoft: transacción compensatoria](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction) — límites de deshacer un paso; autoridad: documentación de Microsoft.

---

[↑ Glosario](../../README.md) · [← Importe en unidad mínima](./importe-en-unidad-minima.md) · [Incertidumbre →](./incertidumbre.md)
