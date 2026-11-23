# Doble escritura

[↑ Glosario](../../README.md) · [← Doble de prueba](./doble-de-prueba.md) · [Doble validez →](./doble-validez.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Escritura del mismo dato en dos almacenes mediante operaciones independientes.

Definición de trabajo de [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

## Por qué importa

En [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), el tema «Doble escritura» importa porque sin transacción común, cualquier orden deja una escritura huérfana.

## Cómo funciona

Según [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), en la sección «Doble escritura»:

Guardar en la base y publicar en el corredor son dos operaciones en dos sistemas que no comparten transacción. Si se confirma la base y luego se publica, una caída entre ambas deja un cambio sin aviso; si se publica y luego se confirma, deja un aviso de algo que no ocurrió. No existe un tercer orden: el problema es la falta de atomicidad entre los dos, no el orden. Un reintento tras el fallo tampoco ayuda por sí solo, porque el proceso reiniciado no sabe qué escribió antes de caer. La solución estructural es que **un solo sistema** guarde ambas cosas.

## Ejemplo

Ejemplo de [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo sustituye la doble escritura de mejor esfuerzo por una bandeja de salida: la aplicación escribe la nota y, en la misma transacción, un evento con la clave y un número de secuencia; un reproductor aplica los eventos al almacén nuevo con reintentos y descarta los de secuencia menor.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md)) son:

- **Entregas guardadas sin evento** — causa: se publicó después de confirmar, sin outbox. Corrección: outbox en la misma transacción y relevo.
- **Eventos de entregas que no existen** — causa: se publicó antes de confirmar la base. Corrección: publicar solo desde el outbox, tras el commit.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Prueba:** cuenta cuántas claves difieren por fallo (la segunda escritura no ocurrió) y cuántas por orden (el valor está presente pero es antiguo); si el reintento reduce las primeras y no las segundas, la causa es la doble escritura sin reparación. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Bandeja de salida](../b/bandeja-de-salida.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md), [Compensación](../c/compensacion.md), [Inbox](../i/inbox.md), [Lector tolerante](../l/lector-tolerante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-377 — Outbox, inbox, sagas y compensación](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-492](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-492-proyecto-camino-a-produccion-con-rollback/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Discord](../../../casos/exito/discord.md), [TSB Bank](../../../casos/fallo/tsb.md).

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

[↑ Glosario](../../README.md) · [← Doble de prueba](./doble-de-prueba.md) · [Doble validez →](./doble-validez.md)
