# Recorrido por saltos

[↑ Glosario](../../README.md) · [← Recorrido crítico](./recorrido-critico.md) · [Recorridos y serialización →](./recorridos-y-serializacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Técnica que usa un índice compuesto sin condición sobre su primera columna recorriendo cada uno de sus valores.

Definición de trabajo de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

## Por qué importa

La clase donde se define, [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), existe con este propósito: la clase existe para que diseñes índices a partir de los patrones de acceso reales y los justifiques con un plan de ejecución y una medida de trabajo, no con la intuición de que «un índice acelera», y para que cuentes lo que cada índice cobra en cada escritura.

## Cómo funciona

Según [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

Un índice sobre `(curso, estudiante)` ordena las entradas primero por curso y, dentro, por estudiante. Resuelve bien `curso = ? AND estudiante = ?` y `curso = ?`, porque el prefijo coincide; resuelve mal `estudiante = ?` solo, porque las entradas de un estudiante están dispersas entre los cursos. El orden inverso hace lo contrario. Como regla, se ponen primero las columnas de igualdad más selectivas o las que siempre aparecen, y después las de rango. SQLite, con estadísticas, puede usar un recorrido por saltos sobre el primer prefijo cuando tiene pocos valores, algo que otros motores no hacen: verificar el plan en el motor propio es parte del trabajo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

El equipo de la plataforma crea un catálogo de patrones de acceso, uno por consulta frecuente, con su frecuencia, su filtro y su plazo: «mis entregas» (por estudiante, ordenadas por fecha, cada pantalla), «panel del docente» (por curso y rango de fechas) y «informe nocturno» (promedios por curso). Para cada una anota el plan antes y después, los pasos medidos y el índice que la justifica.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)) son:

- **Se crea un índice y la consulta no mejora** — causa: condición poco selectiva o forma que no coincide con el prefijo. Corrección: mirar el plan y la selectividad antes y después.
- **Las escrituras se vuelven lentas con el tiempo** — causa: índices acumulados sin consulta que los justifique. Corrección: catálogo de patrones y revisión periódica.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- SQLite, con estadísticas, puede usar un recorrido por saltos sobre el primer prefijo cuando tiene pocos valores, algo que otros motores no hacen: verificar el plan en el motor propio es parte del trabajo. ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Índice compuesto](../i/indice-compuesto.md), [Condición](../c/condicion.md), [Índice](../i/indice.md), [Sobre](../s/sobre.md), [N+1](../n/n-mas-1.md), [Plan de ejecución](../p/plan-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «skip scan».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: optimizador](https://www.sqlite.org/optoverview.html) — uso de índices y recorrido por saltos; autoridad: documentación oficial de SQLite.
- [SQLite: planificador de consultas](https://www.sqlite.org/queryplanner.html) — índices y planes; autoridad: documentación oficial de SQLite.
- [SQLite: EXPLAIN QUERY PLAN](https://www.sqlite.org/eqp.html) — lectura de un plan; autoridad: documentación oficial de SQLite.
- [SQLite: ANALYZE](https://www.sqlite.org/lang_analyze.html) — estadísticas del planificador; autoridad: documentación oficial de SQLite.
- [PostgreSQL: índices de varias columnas](https://www.postgresql.org/docs/current/indexes-multicolumn.html) — orden de columnas; autoridad: documentación oficial de PostgreSQL.

---

[↑ Glosario](../../README.md) · [← Recorrido crítico](./recorrido-critico.md) · [Recorridos y serialización →](./recorridos-y-serializacion.md)
