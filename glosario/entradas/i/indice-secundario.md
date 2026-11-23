# Índice secundario

[↑ Glosario](../../README.md) · [← Índice de rejilla](./indice-de-rejilla.md) · [Índices ordenados y consultas de rango →](./indices-ordenados-y-consultas-de-rango.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Estructura adicional que permite buscar por un atributo distinto de la clave.

Definición de trabajo de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

## Por qué importa

La clase donde se define, [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), existe con este propósito: la clase existe para que elijas un modelo de almacenamiento por las preguntas que tendrá que contestar y por los cambios que tendrá que soportar, no por la moda de un motor, y para que midas qué se gana y qué se paga al sacar los mismos datos de las tablas.

## Cómo funciona

Según [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md):

Un almacén de clave-valor devuelve el valor de una clave en un solo acceso y no sabe nada de su contenido. Para una sola pregunta («dame la entrega 123») es insuperable; para cualquier otra («las entregas del estudiante 17») hay que recorrerlo todo o mantener a mano un índice secundario. Ese índice son dos escrituras que el almacén no puede hacer atómicas, así que una interrupción en medio deja un índice que no refleja los datos. Es una buena opción para cachés y sesiones (`SE-356`) y una mala para datos que se consultan por varios atributos.

## Ejemplo

Ejemplo de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra por qué un índice secundario manual no es seguro. Antes de ejecutarlo, predice cuántas entradas faltarán si la tercera escritura se interrumpe.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una entrega no se encuentra por estudiante** — causa: índice secundario manual desincronizado. Corrección: reconstruirlo desde los datos y comprobarlo con una tarea periódica. ([SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para una sola pregunta («dame la entrega 123») es insuperable; para cualquier otra («las entregas del estudiante 17») hay que recorrerlo todo o mantener a mano un índice secundario. ([SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Estructura](../e/estructura.md), [Ciclo](../c/ciclo.md), [Consulta recursiva](../c/consulta-recursiva.md), [Documento](../d/documento.md), [Documento embebido](../d/documento-embebido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de datos y sus compromisos; autoridad: autor del libro.
- [PostgreSQL: tipos JSON](https://www.postgresql.org/docs/current/datatype-json.html) — documentos dentro de un motor relacional; autoridad: documentación oficial de PostgreSQL.
- [SQLite: WITH recursivo](https://www.sqlite.org/lang_with.html) — consultas recursivas, UNION y UNION ALL; autoridad: documentación oficial de SQLite.
- [Codd, «A relational model of data for large shared data banks»](https://dl.acm.org/doi/10.1145/362384.362685) — independencia entre datos y representación; autoridad: artículo original (1970).
- [Python: json](https://docs.python.org/3/library/json.html) — serialización usada para medir los bytes; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Índice de rejilla](./indice-de-rejilla.md) · [Índices ordenados y consultas de rango →](./indices-ordenados-y-consultas-de-rango.md)
