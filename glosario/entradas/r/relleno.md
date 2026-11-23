# Relleno

[↑ Glosario](../../README.md) · [← Relevo](./relevo.md) · [Relleno de credenciales →](./relleno-de-credenciales.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Proceso que calcula y escribe en la estructura nueva los valores de los datos históricos.

Definición de trabajo de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md).

## Por qué importa

En [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), el tema «Relleno por lotes» importa porque un lote grande bloquea y uno pequeño tarda demasiado.

## Cómo funciona

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

El relleno convierte los datos históricos al formato nuevo. Hacerlo en una sola sentencia sobre toda la tabla mantiene bloqueos o transacciones largas durante todo el tiempo de la operación, y cualquier escritura concurrente espera. Hacerlo por **lotes** pequeños limita cada bloqueo al tiempo de un lote y deja entre lotes un hueco para que pasen las demás escrituras. El tamaño de lote es un compromiso: el bloqueo por lote crece con el número de filas, la duración total crece con el número de lotes por su sobrecosto fijo (abrir transacción, confirmar, esperar). Un lote muy grande da una espera larga pero un relleno rápido; uno muy pequeño da casi ninguna espera y un relleno interminable.

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cinco fases y la condición de cada paso. Expandir: añadir `nota_num` nula (cambio de metadatos). Doble escritura: la aplicación escribe en `texto` y en `nota_num`, con la versión desplegada compatible con las dos formas. Relleno: lotes de 2 000 filas con escritura condicional por versión, 20 ms de pausa y reanudable por identificador; la espera p99 de una escritura queda por debajo de 50 ms. Verificación: suma de comprobación por bloques de 1 000 filas entre `texto` convertido y `nota_num`, ejecutada cada hora; el paso siguiente solo ocurre con tres comprobaciones consecutivas sin diferencias. Lectura del nuevo: bandera por docente, 5 % primero. Dejar de escribir en `texto`: solo tras dos semanas sin diferencias.

## Ejemplo

Ejemplo de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cinco fases y la condición de cada paso. Expandir: añadir `nota_num` nula (cambio de metadatos). Doble escritura: la aplicación escribe en `texto` y en `nota_num`, con la versión desplegada compatible con las dos formas. Relleno: lotes de 2 000 filas con escritura condicional por versión, 20 ms de pausa y reanudable por identificador; la espera p99 de una escritura queda por debajo de 50 ms. Verificación: suma de comprobación por bloques de 1 000 filas entre `texto` convertido y `nota_num`, ejecutada cada hora; el paso siguiente solo ocurre con tres comprobaciones consecutivas sin diferencias.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Las escrituras se detienen durante el relleno** — causa: lote demasiado grande. Corrección: reducir el lote hasta cumplir el objetivo de espera. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))
- **Recuentos iguales y datos obsoletos** — causa: relleno sin escritura condicional. Corrección: condicionar por versión o marca de tiempo y repasar las nulas. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))
- **El relleno tarda días** — causa: lote demasiado pequeño o pausas excesivas. Corrección: medir el costo fijo por lote y aumentar el tamaño. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El relleno convierte los datos históricos al formato nuevo. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))
- Traslada el análisis a otro dominio (por ejemplo, una tabla de pedidos con un campo de dirección que se divide en calle y ciudad): cambia la conversión y el volumen y conserva el procedimiento de expandir, doble escritura, relleno condicional por lotes, verificación de contenido y contracción tras un reposo. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Proceso](../p/proceso.md), [Valor](../v/valor.md), [Escritura condicional](../e/escritura-condicional.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Idempotencia](../i/idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-458](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-458-identidad-autenticacion-y-sesiones/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-489](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-489-developer-portals-y-capacidades-de-plataforma/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md), [SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Stripe](../../../casos/exito/stripe.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «backfill».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Fowler, «ParallelChange»](https://martinfowler.com/bliki/ParallelChange.html) — patrón expandir y contraer; autoridad: autor del texto.
- [Fowler y Sadalage, «Evolutionary Database Design»](https://martinfowler.com/articles/evodb.html) — cambios de esquema en pasos pequeños y automatizados; autoridad: autores del texto.
- [SQLite: ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — qué cambios son de metadatos y cuáles reconstruyen la tabla; autoridad: documentación de SQLite.
- [SQLite: UPDATE](https://www.sqlite.org/lang_update.html) — actualización condicionada; autoridad: documentación de SQLite.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — módulo usado en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Relevo](./relevo.md) · [Relleno de credenciales →](./relleno-de-credenciales.md)
