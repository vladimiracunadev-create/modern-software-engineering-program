# Clave sustituta

[↑ Glosario](../../README.md) · [← Clave foránea](./clave-foranea.md) · [CLI →](./cli.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Una **clave sustituta** es un identificador generado por el modelo, distinto de la clave de negocio, que identifica una fila de forma estable y no tiene significado de negocio ([SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), [SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md)). Puede ser un entero secuencial, un identificador aleatorio o un hash. Se contrapone a la clave **natural**, que sale de los datos del dominio.

## Por qué importa

Toda fila necesita algo que la identifique y no cambie. El correo de un estudiante parece una buena clave hasta que alguien cambia de dirección: entonces hay que actualizar cada fila que lo referencia. La decisión que cambia es qué se usa para relacionar tablas: una identidad estable e interna, en vez de un dato del mundo que puede cambiar, repetirse o reutilizarse.

## Cómo funciona

[SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) explica por qué funciona: la clave sustituta no significa nada, y por eso no tiene motivo para cambiar. El dato natural puede modificarse sin tocar las referencias. El costo es doble: oculta duplicados si no se añade además una **restricción de unicidad** sobre el dato natural, y su elección entre entero y UUID, que parece estética, tiene costos medibles de espacio, de orden de inserción y de exposición (un entero secuencial revela cuántas entregas hay).

[SE-363](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-363-modelado-analitico-hechos-dimensiones-y-granularidad/README.md) lleva la idea a la ingeniería de datos. La clave de negocio del sistema operacional puede cambiar, repetirse entre sistemas o reutilizarse. Una clave sustituta aísla las tablas analíticas de esos cambios y permite **varias versiones de la misma entidad**, una por fila de la dimensión con historia. Ese aislamiento tiene un costo operativo: cada carga debe resolver de clave de negocio a clave sustituta, y los hechos sin dimensión (huérfanos) necesitan una fila especial «desconocido» para no desaparecer en una unión interna.

## Ejemplo

Una tabla de estudiantes usa `id` entero como clave sustituta y mantiene el correo con una restricción de unicidad. Si el estudiante cambia de correo, se actualiza una sola fila. En un almacén analítico, la dimensión de estudiantes guarda una fila por versión del estudiante, cada una con su clave sustituta; un hecho cuyo estudiante no se encuentra apunta a la fila «desconocido» en lugar de perderse.

## Errores y confusiones comunes

- **Quitar la clave natural**: sin unicidad sobre el dato natural, la clave sustituta permite filas duplicadas que parecen distintas.
- **Elegir entre entero y UUID por estética**: tiene costos de espacio, orden de inserción y exposición.
- **Exponer el entero secuencial hacia fuera**: revela cuántos registros existen.
- **Perder hechos huérfanos**: sin fila «desconocido», una unión interna los descarta.

## Límites y cuándo no aplica

No siempre hace falta: cuando existe una clave natural verdaderamente estable y única, añadir una sustituta suma una columna y una resolución en cada carga sin un beneficio claro. En el modelado con historia, la clave sustituta es necesaria, pero no resuelve por sí sola la semántica de los cambios; esa decisión (qué versión corresponde a un hecho) es aparte. Y aporta estabilidad interna, no identidad ante terceros: otros sistemas seguirán usando la clave de negocio.

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
