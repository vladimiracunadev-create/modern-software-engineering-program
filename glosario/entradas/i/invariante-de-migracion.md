# Invariante de migración

[↑ Glosario](../../README.md) · [← Invariante de clase](./invariante-de-clase.md) · [Invariante del flujo →](./invariante-del-flujo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Consulta con un resultado esperado que se ejecuta tras la migración para demostrar que los datos son correctos.

Definición de trabajo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Por qué importa

La clase donde se define, [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), existe con este propósito: el taller existe para que revises una migración antes de ejecutarla con tres instrumentos de potencia distinta (un analizador de texto, un ensayo en una copia de los datos y un plan de cortes) y para que sepas qué defectos ve cada uno, cuáles ninguno y por qué no basta con que «pase en la base de pruebas».

## Cómo funciona

[SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

El equipo de la plataforma convierte la migración del jueves en cuatro migraciones numeradas. La 0050 fija `lock_timeout`, añade `estado_v2` como nullable y crea el índice de forma concurrente; no toca datos. La 0051 rellena por lotes de 1 000 filas, con un script idempotente que registra el último lote procesado y, al final, ejecuta las invariantes: cero filas con `estado_v2` nulo salvo las que lo tenían nulo de origen, mismo conteo de entregas, mismo conjunto de correos únicos y misma suma de notas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md)) son:

- **La migración pasa en desarrollo y falla en producción** — causa: ensayo sin datos reales o con muestra pequeña. Corrección: ensayo en copia completa con datos sintéticos que conserven los casos raros.
- **Quedan filas sin valor tras un relleno** — causa: condición que omite casos válidos. Corrección: invariante de nulos y revisión de la condición.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md)) son: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las migraciones, los defectos y las mutaciones son construcciones del autor; las reglas del analizador se ajustaron con las mismas mutaciones que lo evalúan, por lo que su exactitud real es desconocida; se usó SQLite, con DDL transaccional y sin tráfico concurrente, y no se probó ningún otro motor ni el bloqueo bajo carga.

## Relación con otros conceptos

- **Prerrequisito:** [Migración](../m/migracion.md).
- **Ver también:** [Resultado](../r/resultado.md), [DDL transaccional](../d/ddl-transaccional.md), [Defecto de forma](../d/defecto-de-forma.md), [Defecto de sentido](../d/defecto-de-sentido.md), [Ensayo en copia](../e/ensayo-en-copia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Invariante de clase](./invariante-de-clase.md) · [Invariante del flujo →](./invariante-del-flujo.md)
