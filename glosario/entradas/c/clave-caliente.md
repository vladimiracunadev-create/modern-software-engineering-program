# Clave caliente

[↑ Glosario](../../README.md) · [← Clausura transitiva](./clausura-transitiva.md) · [Clave de caché →](./clave-de-cache.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Clave que recibe una fracción desproporcionada de las peticiones.

Definición de trabajo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md).

## Por qué importa

En [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), el tema «Clave caliente» importa porque una clave muy popular no se reparte con ninguna función.

## Cómo funciona

Según [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), en la sección «Clave caliente»:

Si la popularidad de las claves no es uniforme (unos pocos estudiantes o cursos concentran muchas peticiones), una sola partición recibe una fracción desproporcionada, y añadir nodos no la alivia. Las salidas son cambiar la clave (repartir por un campo más fino), dividir la clave caliente en subclaves (lecturas a todas, a costa de complejidad) o servirla desde una caché (`SE-356`). Un rango contiguo de identificadores es la peor opción cuando los identificadores recientes son los populares, porque todo el tráfico va a la última partición.

## Ejemplo

Ejemplo de [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma decide con medidas. Para «mis entregas» elige una réplica de lectura con la garantía de leer lo propio: el cliente guarda el número de versión de su última escritura y la réplica solo responde si ya lo aplicó; si no, la petición va al líder, y se vigila que esa fracción se mantenga por debajo del 10 %.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un nodo está saturado y los demás ociosos** — causa: clave caliente o rango contiguo. Corrección: cambiar la clave, repartir en subclaves o usar caché. ([SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con semilla fija en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna base de datos distribuida ni red: el retardo exponencial, la lectura uniforme y la popularidad Zipf son supuestos del autor, el cuórum no modela fallos de nodos ni escrituras parciales y no se midió latencia ni el costo de mover datos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuórum](./cuorum.md), [Hash consistente](../h/hash-consistente.md), [Lectura de la propia escritura](../l/lectura-de-la-propia-escritura.md), [Replicación asíncrona](../r/replicacion-asincrona.md), [Retardo de replicación](../r/retardo-de-replicacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-355 — Replicación, partición y distribución](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

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

[↑ Glosario](../../README.md) · [← Clausura transitiva](./clausura-transitiva.md) · [Clave de caché →](./clave-de-cache.md)
