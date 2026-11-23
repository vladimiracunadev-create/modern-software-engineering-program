# Relevo

[↑ Glosario](../../README.md) · [← Release candidate](./release-candidate.md) · [Relleno →](./relleno.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Proceso que lee los mensajes pendientes del outbox, los publica y los marca como enviados.

Definición de trabajo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md): Proceso que lee eventos pendientes de una tabla y los publica, marcándolos como enviados.

## Por qué importa

En [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), el tema «Inbox y relevo» importa porque el relevo duplica; la inbox convierte duplicados en un solo efecto.

## Cómo funciona

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El **outbox** es una tabla en la misma base de datos del servicio. La operación de negocio inserta la entrega **y** una fila en `outbox` con el mensaje en la **misma transacción**: o ambas existen o ninguna. Un proceso aparte, el **relevo**, lee las filas no publicadas, las envía al corredor y las marca. La publicación pasa de ser parte de la petición a ser una tarea que se reintenta hasta lograrlo. El costo es una tabla más, un proceso que operar, la latencia del relevo y la necesidad de limpiar lo ya enviado. La ganancia es que ya no existen entregas sin evento ni eventos sin entrega.

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Ejemplo

Ejemplo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Entregas guardadas sin evento** — causa: se publicó después de confirmar, sin outbox. Corrección: outbox en la misma transacción y relevo. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))
- **Mensajes perdidos sin rastro** — causa: el relevo marca antes de publicar. Corrección: publicar y luego marcar; inbox en el receptor. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))
- **Cada caída del relevo duplica efectos** — causa: receptor sin inbox. Corrección: clave única por mensaje en la misma transacción del efecto. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un proceso aparte, el **relevo**, lee las filas no publicadas, las envía al corredor y las marca. ([SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bandeja de salida](../b/bandeja-de-salida.md), [Evento](../e/evento.md), [Proceso](../p/proceso.md), [Backend](../b/backend.md), [Cola larga](../c/cola-larga.md), [Compensación](../c/compensacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-580](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md), [SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md), [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

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

[↑ Glosario](../../README.md) · [← Release candidate](./release-candidate.md) · [Relleno →](./relleno.md)
