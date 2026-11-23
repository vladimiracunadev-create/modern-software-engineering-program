# Modelo conceptual

[↑ Glosario](../../README.md) · [← Modelo base](./modelo-base.md) · [Modelo conductual →](./modelo-conductual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Descripción de las entidades del dominio y sus relaciones, sin referencia a un motor.

Definición de trabajo de [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md).

## Por qué importa

La clase donde se define, [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), existe con este propósito: la clase existe para que distingas tres decisiones que suelen mezclarse en una sola: qué hechos existen en el dominio (modelo conceptual), cómo se organizan sin contradecirse (modelo lógico) y cómo se almacenan en un motor concreto (modelo físico), y para que midas qué cuesta equivocarse en cada nivel antes de que haya datos que migrar.

## Cómo funciona

Según [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md):

El **modelo conceptual** dice qué cosas existen y cómo se relacionan en lenguaje del dominio: un estudiante entrega una tarea de un curso, un docente la califica. No habla de tablas ni de tipos. El **modelo lógico** traduce esas afirmaciones a relaciones con claves y dependencias, sin decidir aún el motor. El **modelo físico** elige tipos, índices, particiones y el formato de las claves para un motor concreto. Codd defendió en 1970 que el programa no debía depender de la representación almacenada; esa separación sigue siendo la razón de tener tres niveles: cambiar el nivel físico (un índice, un tipo) no debería exigir reescribir el negocio, y cambiar el negocio no debería exigir rehacer el almacenamiento.

Según [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md):

El equipo de la plataforma dibuja primero el modelo conceptual en una página: estudiante, curso, entrega, integrante de entrega, calificación y docente, con sus cardinalidades. De ahí deriva el modelo lógico: claves sustitutas enteras, una restricción de unicidad sobre el correo y una tabla `integrante(entrega_id, estudiante_id)`. Solo entonces decide lo físico: enteros como clave, sin índices adicionales hasta que `SE-353` muestre una consulta que los pida, y un volumen declarado de 100 000 entregas por año. Cada decisión queda en `schema.sql` con un comentario que dice a qué nivel pertenece y qué medida la respalda. Se desnormaliza una sola cosa, el nombre del curso en el informe mensual, con una tarea que lo regenera y una prueba que compara el informe con las tablas.

## Ejemplo

Ejemplo de [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma dibuja primero el modelo conceptual en una página: estudiante, curso, entrega, integrante de entrega, calificación y docente, con sus cardinalidades. De ahí deriva el modelo lógico: claves sustitutas enteras, una restricción de unicidad sobre el correo y una tabla `integrante(entrega_id, estudiante_id)`. Solo entonces decide lo físico: enteros como clave, sin índices adicionales hasta que `SE-353` muestre una consulta que los pida, y un volumen declarado de 100 000 entregas por año. Cada decisión queda en `schema.sql` con un comentario que dice a qué nivel pertenece y qué medida la respalda.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md)) son:

- **El mismo curso aparece con dos nombres** — causa: hecho repetido actualizado a medias. Corrección: guardar el hecho en un solo lugar y referenciarlo.
- **Un curso desaparece al borrar sus entregas** — causa: el curso solo existe como columna de las entregas. Corrección: darle su propia tabla con clave.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún servidor de bases de datos ni datos reales: los tamaños, el corte del lote y la forma de los grupos son construcciones del autor, y los resultados no se extrapolan a otros motores ni a volúmenes de producción.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Motor](./motor.md), [Referencia](../r/referencia.md), [Relación](../r/relacion.md), [Anomalía de actualización](../a/anomalia-de-actualizacion.md), [Cardinalidad](../c/cardinalidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Codd, «A relational model of data for large shared data banks»](https://dl.acm.org/doi/10.1145/362384.362685) — modelo relacional e independencia de la representación; autoridad: artículo original (Communications of the ACM, 1970).
- [SQLite: tipos de datos](https://www.sqlite.org/datatype3.html) — afinidad y almacenamiento de valores; autoridad: documentación oficial de SQLite.
- [SQLite: WITHOUT ROWID](https://www.sqlite.org/withoutrowid.html) — tablas con la clave primaria como almacenamiento; autoridad: documentación oficial de SQLite.
- [PostgreSQL: restricciones](https://www.postgresql.org/docs/current/ddl-constraints.html) — claves y comprobaciones como parte del modelo lógico; autoridad: documentación oficial de PostgreSQL.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — interfaz usada en los experimentos; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Modelo base](./modelo-base.md) · [Modelo conductual →](./modelo-conductual.md)
