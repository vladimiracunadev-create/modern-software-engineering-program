# Defecto de forma

[↑ Glosario](../../README.md) · [← Deduplicación de peticiones](./deduplicacion-de-peticiones.md) · [Defecto de sentido →](./defecto-de-sentido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Defecto de una migración visible en el texto de sus sentencias.

Definición de trabajo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Por qué importa

En [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), el tema «Defectos de forma y de sentido» importa porque un analizador solo ve lo que el texto muestra.

## Cómo funciona

Según [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

Un defecto de **forma** se ve en el texto: una columna `NOT NULL` sin valor por defecto, un `UPDATE` sin `WHERE`, un índice que bloquea las escrituras, una migración sin plan de reversión, un renombrado. Un analizador de reglas los encuentra, es barato y debe ejecutarse siempre. Un defecto de **sentido** tiene la forma correcta y el contenido equivocado: un relleno que omite las filas con nota cero, que copia la columna equivocada o que corre antes de que exista la columna destino. No hay regla de texto que los vea, porque lo que está mal es la relación entre la sentencia y los datos.

Según [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

No: encuentra defectos de forma con constancia y sin cansancio, y deja pasar los de sentido. La revisión humana y el ensayo con invariantes cubren lo que el texto no muestra.

## Ejemplo

Ejemplo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sección «Preguntas frecuentes»):

No: encuentra defectos de forma con constancia y sin cansancio, y deja pasar los de sentido. La revisión humana y el ensayo con invariantes cubren lo que el texto no muestra.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md)) son:

- **La migración pasa en desarrollo y falla en producción** — causa: ensayo sin datos reales o con muestra pequeña. Corrección: ensayo en copia completa con datos sintéticos que conserven los casos raros.
- **Quedan filas sin valor tras un relleno** — causa: condición que omite casos válidos. Corrección: invariante de nulos y revisión de la condición.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un defecto de **forma** se ve en el texto: una columna `NOT NULL` sin valor por defecto, un `UPDATE` sin `WHERE`, un índice que bloquea las escrituras, una migración sin plan de reversión, un renombrado. ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))
- No: encuentra defectos de forma con constancia y sin cansancio, y deja pasar los de sentido. ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Migración](../m/migracion.md).
- **Ver también:** [DDL transaccional](./ddl-transaccional.md), [Defecto de sentido](./defecto-de-sentido.md), [Ensayo en copia](../e/ensayo-en-copia.md), [Invariante de migración](../i/invariante-de-migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [PostgreSQL: ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — bloqueos y reescrituras; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) — creación concurrente; autoridad: documentación oficial de PostgreSQL.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios admitidos; autoridad: documentación oficial de SQLite.
- [SQLite: commit atómico](https://www.sqlite.org/atomiccommit.html) — atomicidad ante cortes; autoridad: documentación oficial de SQLite.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — migración en fases; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Deduplicación de peticiones](./deduplicacion-de-peticiones.md) · [Defecto de sentido →](./defecto-de-sentido.md)
