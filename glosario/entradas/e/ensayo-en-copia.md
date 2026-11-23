# Ensayo en copia

[↑ Glosario](../../README.md) · [← Ensayo de vuelta atrás](./ensayo-de-vuelta-atras.md) · [Entorno →](./entorno.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Ejecución de una migración sobre una copia de los datos con invariantes comprobadas después.

Definición de trabajo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Por qué importa

La clase donde se define, [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), existe con este propósito: el taller existe para que revises una migración antes de ejecutarla con tres instrumentos de potencia distinta (un analizador de texto, un ensayo en una copia de los datos y un plan de cortes) y para que sepas qué defectos ve cada uno, cuáles ninguno y por qué no basta con que «pase en la base de pruebas».

## Cómo funciona

[SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

El equipo de la plataforma convierte la migración del jueves en cuatro migraciones numeradas. La 0050 fija `lock_timeout`, añade `estado_v2` como nullable y crea el índice de forma concurrente; no toca datos. La 0051 rellena por lotes de 1 000 filas, con un script idempotente que registra el último lote procesado y, al final, ejecuta las invariantes: cero filas con `estado_v2` nulo salvo las que lo tenían nulo de origen, mismo conteo de entregas, mismo conjunto de correos únicos y misma suma de notas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La migración pasa en desarrollo y falla en producción** — causa: ensayo sin datos reales o con muestra pequeña. Corrección: ensayo en copia completa con datos sintéticos que conserven los casos raros. ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md)) son: Las definiciones son operativas para el taller. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Las migraciones, los defectos y las mutaciones son construcciones del autor; las reglas del analizador se ajustaron con las mismas mutaciones que lo evalúan, por lo que su exactitud real es desconocida; se usó SQLite, con DDL transaccional y sin tráfico concurrente, y no se probó ningún otro motor ni el bloqueo bajo carga.

## Relación con otros conceptos

- **Prerrequisito:** [Invariante](../i/invariante.md), [Migración](../m/migracion.md).
- **Ver también:** [Sobre](../s/sobre.md), [DDL transaccional](../d/ddl-transaccional.md), [Defecto de forma](../d/defecto-de-forma.md), [Defecto de sentido](../d/defecto-de-sentido.md), [Invariante de migración](../i/invariante-de-migracion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-558](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-558-generacion-de-pruebas-documentacion-y-migraciones/README.md).

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

[↑ Glosario](../../README.md) · [← Ensayo de vuelta atrás](./ensayo-de-vuelta-atras.md) · [Entorno →](./entorno.md)
