# Dependencia funcional

[↑ Glosario](../../README.md) · [← Dependencia externa](./dependencia-externa.md) · [Dependencia nominal →](./dependencia-nominal.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Relación en la que el valor de un conjunto de columnas determina el de otra.

Definición de trabajo de [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md).

## Por qué importa

La clase donde se define, [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md), existe con este propósito: la clase existe para que distingas tres decisiones que suelen mezclarse en una sola: qué hechos existen en el dominio (modelo conceptual), cómo se organizan sin contradecirse (modelo lógico) y cómo se almacenan en un motor concreto (modelo físico), y para que midas qué cuesta equivocarse en cada nivel antes de que haya datos que migrar.

## Cómo funciona

Según [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md):

Una **dependencia funcional** dice que un dato determina otro: el identificador de un curso determina su nombre. Cuando esa dependencia se guarda en la misma tabla que las entregas, el nombre del curso se repite en cada entrega y hay que mantenerlo igual en todas. La normalización no es un ritual de formas normales sino la regla práctica de que cada hecho se guarda en un solo lugar. Produce tres **anomalías** observables: de actualización (cambiar un hecho repetido en un lugar y no en otro), de inserción (no poder registrar un curso sin una entrega) y de borrado (perder un curso al borrar su última entrega).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md):

El equipo de la plataforma dibuja primero el modelo conceptual en una página: estudiante, curso, entrega, integrante de entrega, calificación y docente, con sus cardinalidades. De ahí deriva el modelo lógico: claves sustitutas enteras, una restricción de unicidad sobre el correo y una tabla `integrante(entrega_id, estudiante_id)`. Solo entonces decide lo físico: enteros como clave, sin índices adicionales hasta que `SE-353` muestre una consulta que los pida, y un volumen declarado de 100 000 entregas por año.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md)) son:

- **El mismo curso aparece con dos nombres** — causa: hecho repetido actualizado a medias. Corrección: guardar el hecho en un solo lugar y referenciarlo.
- **Un curso desaparece al borrar sus entregas** — causa: el curso solo existe como columna de las entregas. Corrección: darle su propia tabla con clave.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **dependencia funcional** dice que un dato determina otro: el identificador de un curso determina su nombre. ([SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Relación](../r/relacion.md), [Valor](../v/valor.md), [Anomalía de actualización](../a/anomalia-de-actualizacion.md), [Cardinalidad](../c/cardinalidad.md), [Clave sustituta](../c/clave-sustituta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-349 — Modelado conceptual, lógico y físico](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

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

[↑ Glosario](../../README.md) · [← Dependencia externa](./dependencia-externa.md) · [Dependencia nominal →](./dependencia-nominal.md)
