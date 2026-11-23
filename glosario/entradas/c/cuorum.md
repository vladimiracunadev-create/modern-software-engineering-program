# Cuórum

[↑ Glosario](../../README.md) · [← Cuello de botella](./cuello-de-botella.md) · [Cuota →](./cuota.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Número mínimo de réplicas que deben responder para dar una operación por válida; R + W > N asegura el solapamiento.

Definición de trabajo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md): Número mínimo de réplicas que deben participar en una operación.

## Por qué importa

En [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), el tema «Cuórum» importa porque R + W > N garantiza que una lectura vea la última escritura.

## Cómo funciona

Según [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), en la sección «Cuórum»:

En un sistema sin líder fijo, cada dato vive en N réplicas. Una escritura se confirma al llegar a W réplicas y una lectura consulta R, y se queda con la versión más nueva. Si **R + W > N**, los conjuntos de lectura y de escritura siempre se solapan y la lectura ve la última escritura confirmada; si no, puede no verla. Con N = 3, W = 2 y R = 2 se cumple y se tolera la caída de una réplica; con W = 1 y R = 1 es el más rápido y el que más lecturas viejas devuelve. El cuórum no garantiza consistencia fuerte en todos los casos (hay detalles de escrituras parciales y relojes) pero da una condición clara y medible.

## Ejemplo

Ejemplo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la probabilidad de una lectura obsoleta en un cuórum. Antes de ejecutarlo, predice el resultado para N = 3, W = 1, R = 2.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una persona no ve su propia escritura** — causa: lectura de una réplica atrasada. Corrección: consistencia de sesión o lectura del cuórum. ([SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md))
- **El cuórum es 1/1 por «rapidez»** — causa: no se calculó lo que se pierde. Corrección: elegir (W, R) con `W + R > N` si importa lo último. ([SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El cuórum no garantiza consistencia fuerte en todos los casos (hay detalles de escrituras parciales y relojes) pero da una condición clara y medible. ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Réplica](../r/replica.md), [Clave caliente](./clave-caliente.md), [Consistencia eventual](./consistencia-eventual.md), [CRDT](./crdt.md), [Hash consistente](../h/hash-consistente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.
- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos de consistencia; autoridad: proyecto Jepsen.

---

[↑ Glosario](../../README.md) · [← Cuello de botella](./cuello-de-botella.md) · [Cuota →](./cuota.md)
