# Lectura de la propia escritura

[↑ Glosario](../../README.md) · [← Lector tolerante](./lector-tolerante.md) · [Lectura estática de la configuración →](./lectura-estatica-de-la-configuracion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md)

## Definición

Garantía de que quien escribe verá su cambio en las lecturas siguientes.

Definición de trabajo de [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md).

## Por qué importa

En [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), el tema «Lectura de la propia escritura» importa porque quien escribe espera ver su dato.

## Cómo funciona

Según [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), en la sección «Lectura de la propia escritura»:

La consecuencia más visible para una persona es «subí mi entrega y no aparece». La garantía de **leer lo que uno escribió** se puede lograr de varias formas: leer del líder durante unos segundos tras escribir, leer de una réplica solo si ya aplicó la versión de la escritura (un número de versión o posición que el cliente conserva) y, si ninguna la tiene, ir al líder. Cada una cobra algo: la primera carga al líder, la segunda exige llevar la versión, la tercera sigue enviando algunas lecturas al líder.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md):

El equipo de la plataforma decide con medidas. Para «mis entregas» elige una réplica de lectura con la garantía de leer lo propio: el cliente guarda el número de versión de su última escritura y la réplica solo responde si ya lo aplicó; si no, la petición va al líder, y se vigila que esa fracción se mantenga por debajo del 10 %.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)) son:

- **El usuario no ve lo que acaba de guardar** — causa: lectura de una réplica con retardo. Corrección: leer lo propio: versión o líder durante unos segundos.
- **Al añadir un nodo se mueve casi todo** — causa: reparto por módulo. Corrección: anillo de hash consistente con puntos virtuales.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Vogels distingue la *consistencia eventual* de garantías más finas como la *lectura de la propia escritura*, que es la que la persona percibe: si acabo de subir mi entrega y no la veo, la tomo por perdida. ([SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Clave caliente](../c/clave-caliente.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Cuórum](../c/cuorum.md), [Evento de dominio](../e/evento-de-dominio.md), [Hash consistente](../h/hash-consistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-330 — Event-driven, CQRS y event sourcing](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.
- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Vogels, «Eventually consistent» (CACM, 2009)](https://doi.org/10.1145/1435417.1435432) — consistencia eventual y lectura de la propia escritura; autoridad: Communications of the ACM.
- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.

---

[↑ Glosario](../../README.md) · [← Lector tolerante](./lector-tolerante.md) · [Lectura estática de la configuración →](./lectura-estatica-de-la-configuracion.md)
