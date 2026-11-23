# Índice compuesto

[↑ Glosario](../../README.md) · [← Índice como proyección](./indice-como-proyeccion.md) · [Índice de rejilla →](./indice-de-rejilla.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Índice sobre varias columnas ordenado por la primera, luego por la segunda, y así sucesivamente.

Definición de trabajo de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

## Por qué importa

La clase donde se define, [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), existe con este propósito: la clase existe para que diseñes índices a partir de los patrones de acceso reales y los justifiques con un plan de ejecución y una medida de trabajo, no con la intuición de que «un índice acelera», y para que cuentes lo que cada índice cobra en cada escritura.

## Cómo funciona

Según [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

Traslada el análisis a otro dominio (por ejemplo, un registro de visitas a un museo): lista sus consultas, mide la selectividad de cada columna, diseña un índice compuesto y cuenta su costo de escritura. La transferencia está lograda cuando puedes explicar qué consulta ayuda cada índice y cuál no, no cuando los índices se parecen.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

El equipo de la plataforma crea un catálogo de patrones de acceso, uno por consulta frecuente, con su frecuencia, su filtro y su plazo: «mis entregas» (por estudiante, ordenadas por fecha, cada pantalla), «panel del docente» (por curso y rango de fechas) y «informe nocturno» (promedios por curso). Para cada una anota el plan antes y después, los pasos medidos y el índice que la justifica.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)) son:

- **Se crea un índice y la consulta no mejora** — causa: condición poco selectiva o forma que no coincide con el prefijo. Corrección: mirar el plan y la selectividad antes y después.
- **Las escrituras se vuelven lentas con el tiempo** — causa: índices acumulados sin consulta que los justifique. Corrección: catálogo de patrones y revisión periódica.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos en pasos y planes. No se midió tiempo de reloj ni se usó otro motor; el recorrido por saltos y las decisiones del planificador son de SQLite 3.45 tras `ANALYZE` y pueden cambiar con otra versión o sin estadísticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Índice](./indice.md), [Sobre](../s/sobre.md), [N+1](../n/n-mas-1.md), [Plan de ejecución](../p/plan-de-ejecucion.md), [Recorrido por saltos](../r/recorrido-por-saltos.md), [Selectividad](../s/selectividad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [SQLite: planificador de consultas](https://www.sqlite.org/queryplanner.html) — índices y planes; autoridad: documentación oficial de SQLite.
- [SQLite: EXPLAIN QUERY PLAN](https://www.sqlite.org/eqp.html) — lectura de un plan; autoridad: documentación oficial de SQLite.
- [SQLite: optimizador](https://www.sqlite.org/optoverview.html) — uso de índices y recorrido por saltos; autoridad: documentación oficial de SQLite.
- [SQLite: ANALYZE](https://www.sqlite.org/lang_analyze.html) — estadísticas del planificador; autoridad: documentación oficial de SQLite.
- [PostgreSQL: índices de varias columnas](https://www.postgresql.org/docs/current/indexes-multicolumn.html) — orden de columnas; autoridad: documentación oficial de PostgreSQL.

---

[↑ Glosario](../../README.md) · [← Índice como proyección](./indice-como-proyeccion.md) · [Índice de rejilla →](./indice-de-rejilla.md)
