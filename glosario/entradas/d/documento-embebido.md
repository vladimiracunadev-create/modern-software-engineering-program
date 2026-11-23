# Documento embebido

[↑ Glosario](../../README.md) · [← Documento de tarea](./documento-de-tarea.md) · [DOI →](./doi.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Entidad relacionada copiada dentro de otra para poder leerla en una sola operación.

Definición de trabajo de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md).

## Por qué importa

La clase donde se define, [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), existe con este propósito: la clase existe para que elijas un modelo de almacenamiento por las preguntas que tendrá que contestar y por los cambios que tendrá que soportar, no por la moda de un motor, y para que midas qué se gana y qué se paga al sacar los mismos datos de las tablas.

## Cómo funciona

Según [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** la pantalla de un docente muestra el nombre viejo y el nuevo según la entrega que abre. **Hipótesis rivales:** (a) la caché del navegador sirve una versión vieja; (b) hay dos estudiantes con el mismo nombre; (c) la actualización de los documentos embebidos quedó a medias. **Prueba:** busca todos los documentos con ese `estudiante.id` y cuenta cuántos tienen cada nombre; si 8 tienen el viejo, la causa es la actualización parcial. **Conclusión:** el nombre está embebido en 16 documentos y el proceso no es atómico. **Regresión:** añade una tarea idempotente que recorra y complete los documentos pendientes y una prueba que la interrumpa y la repita.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md):

El equipo de la plataforma mide antes de elegir. Mantiene el modelo relacional para entregas, estudiantes y cursos porque las preguntas son variadas y los datos repetidos cambian (un estudiante renombrado). Para la pantalla «mis entregas», que se pide miles de veces por minuto y siempre igual, construye una vista materializada que repite lo necesario y se regenera cuando cambian los datos de origen, con una prueba que compara la vista con las tablas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md)) son:

- **El mismo dato aparece con valores distintos según la pantalla** — causa: dato embebido actualizado a medias. Corrección: tarea idempotente de propagación y comprobación periódica.
- **Una entrega no se encuentra por estudiante** — causa: índice secundario manual desincronizado. Corrección: reconstruirlo desde los datos y comprobarlo con una tarea periódica.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-350 — Relacional, documental, clave-valor, grafos y series](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún motor documental, de clave-valor ni de grafos: los documentos son diccionarios de Python y los bytes son los del JSON; el fallo del 1 % entre dos escrituras y la estructura del grafo son construcciones del autor. No se midieron series temporales; el apartado correspondiente describe un criterio, no una medida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-349](../../../classes/part-29-datos-persistencia-y-recuperacion/se-349-modelado-conceptual-logico-y-fisico/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Ciclo](../c/ciclo.md), [Consulta recursiva](../c/consulta-recursiva.md), [Documento](./documento.md), [Grafo](../g/grafo.md), [Índice secundario](../i/indice-secundario.md).
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

[↑ Glosario](../../README.md) · [← Documento de tarea](./documento-de-tarea.md) · [DOI →](./doi.md)
