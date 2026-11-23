# DDL transaccional

[↑ Glosario](../../README.md) · [← Dato tardío](./dato-tardio.md) · [De la cita a la afirmación →](./de-la-cita-a-la-afirmacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Propiedad de un motor en la que los cambios de esquema pueden confirmarse o revertirse junto con una transacción.

Definición de trabajo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

## Por qué importa

La clase donde se define, [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), existe con este propósito: el taller existe para que revises una migración antes de ejecutarla con tres instrumentos de potencia distinta (un analizador de texto, un ensayo en una copia de los datos y un plan de cortes) y para que sepas qué defectos ve cada uno, cuáles ninguno y por qué no basta con que «pase en la base de pruebas».

## Cómo funciona

Según [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

Una migración de cinco pasos puede interrumpirse en cualquiera: un fallo de red, un tiempo de espera, un reinicio. Si cada paso se confirma por separado, un corte deja un estado intermedio (con las dos columnas, o solo con la nueva) en el que ni el código viejo ni el nuevo saben funcionar. Si todo va en una transacción y el motor admite el DDL transaccional, el corte deja el estado anterior intacto. No todos los motores lo admiten: en los que confirman cada sentencia de definición de forma implícita, hay que diseñar cada paso como idempotente y reanudable.

Según [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md):

El equipo de la plataforma convierte la migración del jueves en cuatro migraciones numeradas. La 0050 fija `lock_timeout`, añade `estado_v2` como nullable y crea el índice de forma concurrente; no toca datos. La 0051 rellena por lotes de 1 000 filas, con un script idempotente que registra el último lote procesado y, al final, ejecuta las invariantes: cero filas con `estado_v2` nulo salvo las que lo tenían nulo de origen, mismo conteo de entregas, mismo conjunto de correos únicos y misma suma de notas. La 0052 despliega el código que usa solo la columna nueva, y la 0053 quita la vieja, marcada como punto de no retorno: exige un respaldo verificado (`SE-357`) de menos de 24 horas y la firma de la persona responsable.

## Ejemplo

Ejemplo de [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma convierte la migración del jueves en cuatro migraciones numeradas. La 0050 fija `lock_timeout`, añade `estado_v2` como nullable y crea el índice de forma concurrente; no toca datos. La 0051 rellena por lotes de 1 000 filas, con un script idempotente que registra el último lote procesado y, al final, ejecuta las invariantes: cero filas con `estado_v2` nulo salvo las que lo tenían nulo de origen, mismo conteo de entregas, mismo conjunto de correos únicos y misma suma de notas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md)) son:

- **La migración pasa en desarrollo y falla en producción** — causa: ensayo sin datos reales o con muestra pequeña. Corrección: ensayo en copia completa con datos sintéticos que conserven los casos raros.
- **Quedan filas sin valor tras un relleno** — causa: condición que omite casos válidos. Corrección: invariante de nulos y revisión de la condición.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** SQLite y PostgreSQL permiten DDL transaccional; ([SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md), [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-357](../../../classes/part-29-datos-persistencia-y-recuperacion/se-357-backups-restauracion-y-pruebas-de-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Motor](../m/motor.md), [Propiedad](../p/propiedad.md), [Transacción](../t/transaccion.md), [Defecto de forma](./defecto-de-forma.md), [Defecto de sentido](./defecto-de-sentido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-359 — Taller: corregir una migración peligrosa](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

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

[↑ Glosario](../../README.md) · [← Dato tardío](./dato-tardio.md) · [De la cita a la afirmación →](./de-la-cita-a-la-afirmacion.md)
