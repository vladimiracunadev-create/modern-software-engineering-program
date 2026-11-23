# Pivote

[↑ Glosario](../../README.md) · [← Pipeline](./pipeline.md) · [Plan →](./plan.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Paso de una saga a partir del cual ya no hay vuelta atrás y solo se puede avanzar.

Definición de trabajo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Por qué importa

La clase donde se define, [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), existe con este propósito: la clase existe para que resuelvas el problema de cambiar una base de datos y avisar a otros servicios sin que uno de los dos pasos quede a medias: aprenderás a medir qué inconsistencias produce escribir y publicar por separado, qué garantiza un outbox y qué le falta, y qué diferencia hay entre compensar un paso y deshacerlo, con un orden de pasos que decide cuántas operaciones terminan con un residuo irreversible.

## Cómo funciona

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

Una compensación es una acción **nueva** que contrarresta el efecto de otra, no una reversión: reembolsar un cobro no «des-cobra», y cancelar un cupo no borra que alguien lo vio ocupado. Algunas acciones no tienen compensación (un correo enviado, un archivo publicado), y esos pasos se llaman **irreversibles**. La regla de diseño es ordenar los pasos de modo que los compensables vayan primero, el irreversible lo más tarde posible (un **pivote**: tras él la saga solo puede avanzar), y los pasos posteriores al pivote puedan reintentarse hasta lograrse. Las compensaciones también fallan: deben ser idempotentes, reintentables y dejar un estado «atascado» observable si no logran terminar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Correos enviados de inscripciones revertidas** — causa: paso irreversible antes del pivote. Corrección: colocar los pasos irreversibles al final. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La regla de diseño es ordenar los pasos de modo que los compensables vayan primero, el irreversible lo más tarde posible (un **pivote**: tras él la saga solo puede avanzar), y los pasos posteriores al pivote puedan reintentarse hasta lograrse. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Saga](../s/saga.md), [Compensación](../c/compensacion.md), [Doble escritura](../d/doble-escritura.md), [Inbox](../i/inbox.md), [Outbox transaccional](../o/outbox-transaccional.md), [Relevo](../r/relevo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), [SE-521](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-521-strangler-branch-by-abstraction-y-anticorruption/README.md).

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

[↑ Glosario](../../README.md) · [← Pipeline](./pipeline.md) · [Plan →](./plan.md)
