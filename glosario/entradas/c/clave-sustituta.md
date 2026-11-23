# Clave sustituta

[↑ Glosario](../../README.md) · [← Clave foránea](./clave-foranea.md) · [CLI →](./cli.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Identificador generado por el modelo, distinto de la clave de negocio.

Definición de trabajo de [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md): Identificador sin significado de negocio que identifica una fila de forma estable.

## Por qué importa

En [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md), el tema «Claves sustitutas» importa porque aíslan al modelo de los cambios de la clave de negocio.

## Cómo funciona

Según [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md):

La clave de negocio (el identificador del cliente en el sistema operacional) puede cambiar, repetirse entre sistemas o reutilizarse. Una clave sustituta (un entero o un hash generado por el modelo) aísla las tablas analíticas de esos cambios y permite varias versiones de la misma entidad, una por fila de la dimensión con historia. El costo es que cada carga debe resolver de clave de negocio a clave sustituta, y que los datos huérfanos (un hecho sin dimensión) deben tener una fila especial «desconocido» y no desaparecer en una unión interna.

Según [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md):

Toda fila necesita algo que la identifique y no cambie. El correo de un estudiante parece una buena clave hasta que alguien cambia de dirección: una clave **natural** que cambia obliga a actualizar cada fila que la referencia. Una clave **sustituta** (un entero secuencial o un identificador aleatorio) no significa nada y por eso no cambia, pero oculta duplicados si no se añade además una restricción de unicidad sobre el dato natural. La elección entre entero y UUID parece estética y tiene costos medibles de espacio, de orden de inserción y de exposición (un entero secuencial revela cuántas entregas hay).

## Ejemplo

Ejemplo de [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma dibuja primero el modelo conceptual en una página: estudiante, curso, entrega, integrante de entrega, calificación y docente, con sus cardinalidades. De ahí deriva el modelo lógico: claves sustitutas enteras, una restricción de unicidad sobre el correo y una tabla `integrante(entrega_id, estudiante_id)`. Solo entonces decide lo físico: enteros como clave, sin índices adicionales hasta que `SE-353` muestre una consulta que los pida, y un volumen declarado de 100 000 entregas por año. Cada decisión queda en `schema.sql` con un comentario que dice a qué nivel pertenece y qué medida la respalda.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo es que cada carga debe resolver de clave de negocio a clave sustituta, y que los datos huérfanos (un hecho sin dimensión) deben tener una fila especial «desconocido» y no desaparecer en una unión interna. ([SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Clave de negocio](./clave-de-negocio.md), [Modelo](../m/modelo.md), [Abanico de uniones](../a/abanico-de-uniones.md), [Anomalía de actualización](../a/anomalia-de-actualizacion.md), [Cardinalidad](./cardinalidad.md), [Dependencia funcional](../d/dependencia-funcional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.
- [SE-363 — Modelado analítico: hechos, dimensiones y granularidad](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Claves sustitutas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Codd, «A relational model of data for large shared data banks»](https://dl.acm.org/doi/10.1145/362384.362685) — modelo relacional e independencia de la representación; autoridad: artículo original (Communications of the ACM, 1970).
- [SQLite: tipos de datos](https://www.sqlite.org/datatype3.html) — afinidad y almacenamiento de valores; autoridad: documentación oficial de SQLite.
- [SQLite: WITHOUT ROWID](https://www.sqlite.org/withoutrowid.html) — tablas con la clave primaria como almacenamiento; autoridad: documentación oficial de SQLite.
- [PostgreSQL: restricciones](https://www.postgresql.org/docs/current/ddl-constraints.html) — claves y comprobaciones como parte del modelo lógico; autoridad: documentación oficial de PostgreSQL.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — interfaz usada en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Clave foránea](./clave-foranea.md) · [CLI →](./cli.md)
