# Consulta recursiva

[↑ Glosario](../../README.md) · [← Consulta parametrizada](./consulta-parametrizada.md) · [Consumidor idempotente →](./consumidor-idempotente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Consulta que se define en términos de su propio resultado parcial y se repite hasta que no añade filas.

Definición de trabajo de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

## Por qué importa

La clase donde se define, [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), existe con este propósito: la clase existe para que elijas un modelo de almacenamiento por las preguntas que tendrá que contestar y por los cambios que tendrá que soportar, no por la moda de un motor, y para que midas qué se gana y qué se paga al sacar los mismos datos de las tablas.

## Cómo funciona

Según [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md):

Un grafo representa entidades y relaciones como ciudadanos de primera clase y es natural cuando importa seguir relaciones de profundidad variable: los prerrequisitos de un curso, las dependencias entre tareas, las recomendaciones. Una unión con profundidad fija no basta cuando el camino puede tener tres o treinta pasos. Un motor relacional con consultas recursivas resuelve muchos casos sin otro sistema; un motor de grafos especializado se justifica cuando el recorrido es la consulta dominante y su volumen lo exige. En ambos casos el recorrido necesita proteger contra ciclos.

Según [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md):

El equipo de la plataforma mide antes de elegir. Mantiene el modelo relacional para entregas, estudiantes y cursos porque las preguntas son variadas y los datos repetidos cambian (un estudiante renombrado). Para la pantalla «mis entregas», que se pide miles de veces por minuto y siempre igual, construye una vista materializada que repite lo necesario y se regenera cuando cambian los datos de origen, con una prueba que compara la vista con las tablas. Para los prerrequisitos usa una consulta recursiva con `UNION`, porque el grafo tiene cientos de cursos y no justifica otro sistema; fija un criterio de revisión: si el recorrido pasa de 100 ms o los nodos de un millón, se reevalúa.

## Ejemplo

Ejemplo de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma mide antes de elegir. Mantiene el modelo relacional para entregas, estudiantes y cursos porque las preguntas son variadas y los datos repetidos cambian (un estudiante renombrado). Para la pantalla «mis entregas», que se pide miles de veces por minuto y siempre igual, construye una vista materializada que repite lo necesario y se regenera cuando cambian los datos de origen, con una prueba que compara la vista con las tablas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La consulta recursiva no termina o crece sin control** — causa: ciclo en el grafo con `UNION ALL` sin límite. Corrección: `UNION` o un tope de profundidad y una detección de ciclos. ([SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un motor relacional con consultas recursivas resuelve muchos casos sin otro sistema; un motor de grafos especializado se justifica cuando el recorrido es la consulta dominante y su volumen lo exige. ([SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Ciclo](./ciclo.md), [Documento](../d/documento.md), [Documento embebido](../d/documento-embebido.md), [Grafo](../g/grafo.md), [Índice secundario](../i/indice-secundario.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: WITH recursivo](https://www.sqlite.org/lang_with.html) — consultas recursivas, UNION y UNION ALL; autoridad: documentación oficial de SQLite.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — modelos de datos y sus compromisos; autoridad: autor del libro.
- [PostgreSQL: tipos JSON](https://www.postgresql.org/docs/current/datatype-json.html) — documentos dentro de un motor relacional; autoridad: documentación oficial de PostgreSQL.
- [Codd, «A relational model of data for large shared data banks»](https://dl.acm.org/doi/10.1145/362384.362685) — independencia entre datos y representación; autoridad: artículo original (1970).
- [Python: json](https://docs.python.org/3/library/json.html) — serialización usada para medir los bytes; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Consulta parametrizada](./consulta-parametrizada.md) · [Consumidor idempotente →](./consumidor-idempotente.md)
