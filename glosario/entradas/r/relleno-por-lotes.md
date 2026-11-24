# Relleno por lotes

[↑ Glosario](../../README.md) · [← Relleno de credenciales](./relleno-de-credenciales.md) · [Reloj de pared →](./reloj-de-pared.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

El **relleno por lotes** es la actualización de una columna en muchas filas dividida en transacciones cortas e idempotentes ([SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md)). Es el paso de una migración que lleva los datos existentes a la estructura nueva sin bloquear el sistema.

## Por qué importa

Actualizar cien mil filas con una sola sentencia parece lo más simple, pero mantiene una transacción larga que puede congelar la aplicación. La decisión que cambia es cómo se migran los datos de un sistema en uso: poco a poco, de forma que se pueda interrumpir y reanudar, y no de una sola vez.

## Cómo funciona

[SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md) explica el daño de la transacción larga según el motor. En uno con **bloqueo de escritura**, los demás escritores esperan todo ese tiempo. En uno con **versiones**, la transacción retiene espacio y retrasa la limpieza. En ambos, la aplicación se degrada mientras dura la migración.

El remedio es **dividir en lotes**: cada uno es una transacción corta que confirma y libera. El tamaño es un equilibrio: lotes pequeños reducen el bloqueo pero aumentan el número de transacciones y la sobrecarga; lotes grandes hacen lo contrario. La clase lo mide en un experimento y propone elegir según el tiempo de bloqueo tolerable.

Dos propiedades hacen seguro el procedimiento:

- **Idempotente**: cada lote se puede repetir sin efecto adicional. Por ejemplo, un `UPDATE ... WHERE columna_nueva IS NULL` solo toca lo que falta.
- **Reanudable**: tras un corte a mitad, se continúa donde quedó (por ejemplo, avanzando por un rango de identificadores), sin empezar de nuevo.

Es la fase de «migrar» del patrón de expandir y contraer: la estructura nueva ya existe y se rellena mientras ambas versiones de la aplicación siguen funcionando. Termina antes del punto de no retorno.

## Ejemplo

Para rellenar `calificacion` desde `nota` en 100 000 filas, un trabajo procesa 1 000 filas por transacción, actualizando solo las que tienen `calificacion` nula, y avanza por identificador. Si se interrumpe, al relanzarlo solo procesa lo que falta. La aplicación sigue respondiendo porque ninguna transacción dura mucho. Ejemplo de la línea de [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md).

## Errores y confusiones comunes

- **El panel se congela al ejecutar una migración**: actualización de muchas filas en una transacción; se corrige con relleno por lotes idempotente y reanudable.
- **Lotes no idempotentes**: un reintento duplica el efecto.
- **No poder reanudar**: obliga a empezar de cero.
- **Elegir el tamaño sin medir** el bloqueo real.

## Límites y cuándo no aplica

Para tablas pequeñas, una sola sentencia puede ser aceptable y más simple. El relleno por lotes no protege contra escrituras concurrentes que cambian la columna origen durante el proceso: requiere mantener sincronizadas ambas columnas (doble escritura) mientras dura. El tamaño óptimo de lote depende del motor y de la carga; el experimento de la clase usa datos sintéticos.

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
