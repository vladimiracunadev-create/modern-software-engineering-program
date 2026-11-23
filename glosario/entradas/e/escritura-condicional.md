# Escritura condicional

[↑ Glosario](../../README.md) · [← Escritura atómica](./escritura-atomica.md) · [Escritura confirmada perdida →](./escritura-confirmada-perdida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Actualización que se aplica solo si la fila no cambió desde que se leyó.

Definición de trabajo de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md).

## Por qué importa

La clase donde se define, [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), existe con este propósito: la clase existe para que puedas cambiar la forma de los datos de un sistema que sigue recibiendo escrituras, sin detenerlo, sin perder una actualización y con una vuelta atrás creíble.

## Cómo funciona

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

El relleno típico hace tres pasos: leer un lote, calcular el valor nuevo y escribirlo. Entre la lectura y la escritura, la aplicación puede modificar una fila del lote. Si el relleno escribe sin condiciones, sobrescribe el valor nuevo calculado desde el texto viejo, y la columna nueva queda con un dato obsoleto aunque pasen todas las comprobaciones de recuento. Hay tres defensas combinables. La **escritura condicional** actualiza solo si la fila no cambió desde la lectura (comparando un número de versión o una marca de tiempo). La **escritura en ambos sitios desde la aplicación**, activada antes del relleno, garantiza que las escrituras nuevas van a la columna nueva; pero por sí sola no protege del relleno, que puede sobrescribirlas con valores calculados del texto antiguo.

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cinco fases y la condición de cada paso. Expandir: añadir `nota_num` nula (cambio de metadatos). Doble escritura: la aplicación escribe en `texto` y en `nota_num`, con la versión desplegada compatible con las dos formas. Relleno: lotes de 2 000 filas con escritura condicional por versión, 20 ms de pausa y reanudable por identificador; la espera p99 de una escritura queda por debajo de 50 ms. Verificación: suma de comprobación por bloques de 1 000 filas entre `texto` convertido y `nota_num`, ejecutada cada hora; el paso siguiente solo ocurre con tres comprobaciones consecutivas sin diferencias. Lectura del nuevo: bandera por docente, 5 % primero. Dejar de escribir en `texto`: solo tras dos semanas sin diferencias.

## Ejemplo

Ejemplo de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cinco fases y la condición de cada paso. Expandir: añadir `nota_num` nula (cambio de metadatos). Doble escritura: la aplicación escribe en `texto` y en `nota_num`, con la versión desplegada compatible con las dos formas. Relleno: lotes de 2 000 filas con escritura condicional por versión, 20 ms de pausa y reanudable por identificador; la espera p99 de una escritura queda por debajo de 50 ms. Verificación: suma de comprobación por bloques de 1 000 filas entre `texto` convertido y `nota_num`, ejecutada cada hora; el paso siguiente solo ocurre con tres comprobaciones consecutivas sin diferencias.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Recuentos iguales y datos obsoletos** — causa: relleno sin escritura condicional. Corrección: condicionar por versión o marca de tiempo y repasar las nulas. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **escritura condicional** actualiza solo si la fila no cambió desde la lectura (comparando un número de versión o una marca de tiempo). ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Expandir y contraer](./expandir-y-contraer.md), [Idempotencia](../i/idempotencia.md), [Relleno](../r/relleno.md), [Relleno por lotes](../r/relleno-por-lotes.md), [Suma de verificación por rango](../s/suma-de-verificacion-por-rango.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir y contraer; autoridad: autor del texto.
- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — cambios de esquema en pasos pequeños y automatizados; autoridad: autores del texto.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — qué cambios son de metadatos y cuáles reconstruyen la tabla; autoridad: documentación de SQLite.
- [SQLite: UPDATE](https://www.sqlite.org/lang_update.html) — actualización condicionada; autoridad: documentación de SQLite.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — módulo usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Escritura atómica](./escritura-atomica.md) · [Escritura confirmada perdida →](./escritura-confirmada-perdida.md)
