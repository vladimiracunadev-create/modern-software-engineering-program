# Retardo de replicación

[↑ Glosario](../../README.md) · [← Retardo antes de pedir](./retardo-antes-de-pedir.md) · [Retención →](./retencion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Tiempo entre que el líder confirma una escritura y una réplica la aplica.

Definición de trabajo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

## Por qué importa

La clase donde se define, [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), existe con este propósito: la clase existe para que decidas cuándo copiar datos entre máquinas (replicar) y cuándo repartirlos (particionar), qué garantías de lectura pierdes en cada caso y cómo elegir una clave de reparto que no concentre la carga en una sola máquina.

## Cómo funciona

[SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) (sección «Caso conductor»):

La capa de datos de la plataforma de entregas sigue siendo el caso conductor. Esta clase deja el séptimo artefacto: la decisión de réplicas y partición con su garantía de lectura propia y su clave candidata. `SE-356` pregunta cómo mantener coherentes las copias que se guardan en cachés entre capas. Cambia después una sola decisión, el retardo de replicación, y observa cómo cambia la fracción de lecturas obsoletas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)) son:

- **El usuario no ve lo que acaba de guardar** — causa: lectura de una réplica con retardo. Corrección: leer lo propio: versión o líder durante unos segundos.
- **Al añadir un nodo se mueve casi todo** — causa: reparto por módulo. Corrección: anillo de hash consistente con puntos virtuales.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna base de datos distribuida ni red: el retardo exponencial, la lectura uniforme y la popularidad Zipf son supuestos del autor, el cuórum no modela fallos de nodos ni escrituras parciales y no se midió latencia ni el costo de mover datos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Réplica](./replica.md), [Clave caliente](../c/clave-caliente.md), [Cuórum](../c/cuorum.md), [Hash consistente](../h/hash-consistente.md), [Lectura de la propia escritura](../l/lectura-de-la-propia-escritura.md), [Replicación asíncrona](./replicacion-asincrona.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: replicación y servidores en espera](https://www.postgresql.org/docs/current/warm-standby.html) — replicación síncrona y asíncrona; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: particionado](https://www.postgresql.org/docs/current/ddl-partitioning.html) — particionado por rango, lista y hash; autoridad: documentación oficial de PostgreSQL.
- [Karger et al., «Consistent hashing and random trees»](https://dl.acm.org/doi/10.1145/258533.258660) — hash consistente; autoridad: artículo original (1997).
- [DeCandia et al., «Dynamo»](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html) — cuórum, nodos virtuales y reparto; autoridad: artículo de los autores.
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos de consistencia; autoridad: proyecto Jepsen.

---

[↑ Glosario](../../README.md) · [← Retardo antes de pedir](./retardo-antes-de-pedir.md) · [Retención →](./retencion.md)
