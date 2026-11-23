# Defecto de sentido

[↑ Glosario](../../README.md) · [← Defecto de forma](./defecto-de-forma.md) · [Defecto dormido →](./defecto-dormido.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Defecto de una migración que solo se aprecia al comparar su efecto con los datos.

Definición de trabajo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Por qué importa

La clase donde se define, [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), existe con este propósito: el taller existe para que revises una migración antes de ejecutarla con tres instrumentos de potencia distinta (un analizador de texto, un ensayo en una copia de los datos y un plan de cortes) y para que sepas qué defectos ve cada uno, cuáles ninguno y por qué no basta con que «pase en la base de pruebas».

## Cómo funciona

Según [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

Un defecto de **forma** se ve en el texto: una columna `NOT NULL` sin valor por defecto, un `UPDATE` sin `WHERE`, un índice que bloquea las escrituras, una migración sin plan de reversión, un renombrado. Un analizador de reglas los encuentra, es barato y debe ejecutarse siempre. Un defecto de **sentido** tiene la forma correcta y el contenido equivocado: un relleno que omite las filas con nota cero, que copia la columna equivocada o que corre antes de que exista la columna destino. No hay regla de texto que los vea, porque lo que está mal es la relación entre la sentencia y los datos.

## Ejemplo

Ejemplo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un defecto de sentido que no produce error. Antes de ejecutarlo, predice cuántas filas quedan sin valor.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El analizador no vio un defecto grave** — causa: defecto de sentido, no de forma. Corrección: invariantes de datos y revisión humana. ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un defecto de **sentido** tiene la forma correcta y el contenido equivocado: un relleno que omite las filas con nota cero, que copia la columna equivocada o que corre antes de que exista la columna destino. ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Migración](../m/migracion.md).
- **Ver también:** [Efecto](../e/efecto.md), [DDL transaccional](./ddl-transaccional.md), [Defecto de forma](./defecto-de-forma.md), [Ensayo en copia](../e/ensayo-en-copia.md), [Invariante de migración](../i/invariante-de-migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md).

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

[↑ Glosario](../../README.md) · [← Defecto de forma](./defecto-de-forma.md) · [Defecto dormido →](./defecto-dormido.md)
