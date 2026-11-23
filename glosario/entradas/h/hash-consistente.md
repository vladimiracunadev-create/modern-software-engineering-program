# Hash consistente

[↑ Glosario](../../README.md) · [← Harness gobernado](./harness-gobernado.md) · [Hash por encuentro →](./hash-por-encuentro.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Función de reparto en un círculo en la que cambiar el número de nodos mueve solo una fracción de las claves.

Definición de trabajo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

## Por qué importa

La clase donde se define, [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), existe con este propósito: la clase existe para que decidas cuándo copiar datos entre máquinas (replicar) y cuándo repartirlos (particionar), qué garantías de lectura pierdes en cada caso y cómo elegir una clave de reparto que no concentre la carga en una sola máquina.

## Cómo funciona

Según [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md):

Para particionar hay que decidir una **clave** (qué campo decide dónde va una fila) y una **función** (cómo se traduce la clave en un nodo). El reparto por **módulo** (`hash(clave) mod N`) es sencillo y tiene un defecto grave: al cambiar N, casi todas las claves cambian de nodo, y mover los datos es costoso. Un **anillo de hash consistente** coloca nodos y claves en un círculo; al añadir un nodo, solo se mueven las claves que caen en su tramo. Con pocos puntos por nodo el reparto es desigual; con puntos virtuales (muchos por nodo) se equilibra. La clave decide además qué consultas tocan un solo nodo y cuáles hay que lanzar a todos.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md):

El equipo de la plataforma decide con medidas. Para «mis entregas» elige una réplica de lectura con la garantía de leer lo propio: el cliente guarda el número de versión de su última escritura y la réplica solo responde si ya lo aplicó; si no, la petición va al líder, y se vigila que esa fracción se mantenga por debajo del 10 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Al añadir un nodo se mueve casi todo** — causa: reparto por módulo. Corrección: anillo de hash consistente con puntos virtuales. ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **anillo de hash consistente** coloca nodos y claves en un círculo; al añadir un nodo, solo se mueven las claves que caen en su tramo. ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Clave caliente](../c/clave-caliente.md), [Cuórum](../c/cuorum.md), [Lectura de la propia escritura](../l/lectura-de-la-propia-escritura.md), [Replicación asíncrona](../r/replicacion-asincrona.md), [Retardo de replicación](../r/retardo-de-replicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-393](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-393-replicacion-sharding-y-balanceo/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Slack](../../../casos/exito/slack.md), [Discord](../../../casos/exito/discord.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos de consistencia; autoridad: proyecto Jepsen.

---

[↑ Glosario](../../README.md) · [← Harness gobernado](./harness-gobernado.md) · [Hash por encuentro →](./hash-por-encuentro.md)
