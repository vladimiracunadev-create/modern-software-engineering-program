# Suma de verificación por rango

[↑ Glosario](../../README.md) · [← Suma de verificación](./suma-de-verificacion.md) · [Superficie compartida →](./superficie-compartida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Huella de un bloque de filas que permite comparar tablas grandes sin leer cada fila.

Definición de trabajo de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md).

## Por qué importa

La clase donde se define, [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md), existe con este propósito: la clase existe para que puedas cambiar la forma de los datos de un sistema que sigue recibiendo escrituras, sin detenerlo, sin perder una actualización y con una vuelta atrás creíble.

## Cómo funciona

Según [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

Un recuento igual de filas solo dice que se copió la misma cantidad; no dice que cada fila tenga el valor correcto. La verificación comprueba **contenido**: para cada fila, el valor nuevo equivale al antiguo según una regla de conversión escrita. En tablas grandes se hace por **sumas de verificación por rango** (una huella de cada bloque de filas, comparando bloques y entrando solo en los distintos) y por muestreo aleatorio con tasas de detección calculadas, como se verá en `SE-524`. La verificación debe ser repetible y ejecutable en cualquier momento, no solo al final: cuando hay doble escritura, una comparación periódica es la señal de que ambas columnas siguen alineadas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cinco fases y la condición de cada paso. Expandir: añadir `nota_num` nula (cambio de metadatos). Doble escritura: la aplicación escribe en `texto` y en `nota_num`, con la versión desplegada compatible con las dos formas. Relleno: lotes de 2 000 filas con escritura condicional por versión, 20 ms de pausa y reanudable por identificador; la espera p99 de una escritura queda por debajo de 50 ms.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md)) son:

- **Las escrituras se detienen durante el relleno** — causa: lote demasiado grande. Corrección: reducir el lote hasta cumplir el objetivo de espera.
- **Recuentos iguales y datos obsoletos** — causa: relleno sin escritura condicional. Corrección: condicionar por versión o marca de tiempo y repasar las nulas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En tablas grandes se hace por **sumas de verificación por rango** (una huella de cada bloque de filas, comparando bloques y entrando solo en los distintos) y por muestreo aleatorio con tasas de detección calculadas, como se verá en `SE-524`. ([SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Escritura condicional](../e/escritura-condicional.md), [Expandir y contraer](../e/expandir-y-contraer.md), [Idempotencia](../i/idempotencia.md), [Relleno](../r/relleno.md), [Relleno por lotes](../r/relleno-por-lotes.md).
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

[↑ Glosario](../../README.md) · [← Suma de verificación](./suma-de-verificacion.md) · [Superficie compartida →](./superficie-compartida.md)
