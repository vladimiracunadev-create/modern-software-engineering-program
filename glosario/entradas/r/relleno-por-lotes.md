# Relleno por lotes

[↑ Glosario](../../README.md) · [← Relleno de credenciales](./relleno-de-credenciales.md) · [Reloj de pared →](./reloj-de-pared.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Actualización de una columna en muchas filas dividida en transacciones cortas e idempotentes.

Definición de trabajo de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

## Por qué importa

En [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), el tema «Relleno por lotes» importa porque el tamaño del lote decide cuánto tiempo se retiene un bloqueo.

En [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), el tema «Relleno por lotes» importa porque un lote grande bloquea y uno pequeño tarda demasiado.

## Cómo funciona

Según [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), en la sección «Relleno por lotes»:

Rellenar una columna en 100 000 filas con una sola sentencia mantiene una transacción larga: en un motor con bloqueo de escritura, los demás escritores esperan todo ese tiempo; en un motor con versiones, la transacción retiene espacio y retrasa la limpieza. El remedio es dividir en lotes: cada uno es una transacción corta que confirma y libera. El tamaño es un equilibrio: lotes pequeños reducen el bloqueo y aumentan el número de transacciones y la sobrecarga; lotes grandes lo contrario. El relleno debe ser idempotente (cada lote se puede repetir) y reanudable, para sobrevivir a un corte a mitad.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md):

El equipo de la plataforma documenta el renombrado como cuatro migraciones numeradas, cada una desplegable por separado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El panel se congela al ejecutar una migración** — causa: actualización de muchas filas en una transacción. Corrección: relleno por lotes idempotente y reanudable. ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Traslada el análisis a otro cambio (por ejemplo, partir una columna `direccion` en varias): descompónlo en fases compatibles, construye la matriz de versiones contra estados, mide un relleno por lotes y marca el punto de no retorno. ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Idempotente](../i/idempotente.md), [Transacción](../t/transaccion.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Escritura condicional](../e/escritura-condicional.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-354 — Migraciones compatibles y evolución de esquema](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — diseño evolutivo del esquema; autoridad: autores del artículo.
- [Fowler, «Parallel Change»](https://martinfowler.com/bliki/ParallelChange.html) — expandir, migrar y contraer; autoridad: autor del texto.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — cambios admitidos y reconstrucción; autoridad: documentación oficial de SQLite.
- [PostgreSQL: ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) — bloqueos y reescrituras; autoridad: documentación oficial de PostgreSQL.
- [PostgreSQL: CREATE INDEX](https://www.postgresql.org/docs/current/sql-createindex.html) — creación concurrente de índices; autoridad: documentación oficial de PostgreSQL.

---

[↑ Glosario](../../README.md) · [← Relleno de credenciales](./relleno-de-credenciales.md) · [Reloj de pared →](./reloj-de-pared.md)
