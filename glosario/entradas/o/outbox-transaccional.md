# Outbox transaccional

[↑ Glosario](../../README.md) · [← Oscilación por supuesto](./oscilacion-por-supuesto.md) · [Overflow →](./overflow.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Tabla, en la misma base que el cambio de negocio, donde se guardan los mensajes a publicar dentro de la misma transacción.

Definición de trabajo de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md): Tabla escrita en la misma transacción que el cambio de estado, de la que un relevo lee los eventos pendientes para publicarlos después.

## Por qué importa

En [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), el tema «Outbox transaccional» importa porque convierte «publicar» en una fila de la misma transacción.

## Cómo funciona

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), en la sección «Outbox transaccional»:

El **outbox** es una tabla en la misma base de datos del servicio. La operación de negocio inserta la entrega **y** una fila en `outbox` con el mensaje en la **misma transacción**: o ambas existen o ninguna. Un proceso aparte, el **relevo**, lee las filas no publicadas, las envía al corredor y las marca. La publicación pasa de ser parte de la petición a ser una tarea que se reintenta hasta lograrlo. El costo es una tabla más, un proceso que operar, la latencia del relevo y la necesidad de limpiar lo ya enviado. La ganancia es que ya no existen entregas sin evento ni eventos sin entrega.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md):

El equipo de la plataforma diseña tres piezas. **Outbox:** tabla `outbox(id, tipo, clave, cuerpo, creado, publicado_en)` en la misma base de las entregas; la operación que registra la entrega inserta la fila en la misma transacción. **Relevo:** un proceso que lee lotes de 100 filas sin `publicado_en`, publica, marca y limpia las publicadas con más de siete días; si se cae entre publicar y marcar, el mensaje se publica de nuevo. **Inbox:** el calificador tiene `inbox(mensaje_id primary key)` y hace `INSERT OR IGNORE` en la misma transacción del efecto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)) son:

- **Entregas guardadas sin evento** — causa: se publicó después de confirmar, sin outbox. Corrección: outbox en la misma transacción y relevo.
- **Eventos de entregas que no existen** — causa: se publicó antes de confirmar la base. Corrección: publicar solo desde el outbox, tras el commit.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó corredor, red ni concurrencia de relevos: las caídas, los fallos de pasos y las compensaciones son probabilidades del autor con semilla fija, y los resultados no se extrapolan a ningún sistema. Solo el outbox y la inbox usan un motor real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Base](../b/base.md), [Estado](../e/estado.md), [Evento](../e/evento.md), [Relevo](../r/relevo.md), [Backend](../b/backend.md), [Cola larga](../c/cola-larga.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

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

[↑ Glosario](../../README.md) · [← Oscilación por supuesto](./oscilacion-por-supuesto.md) · [Overflow →](./overflow.md)
