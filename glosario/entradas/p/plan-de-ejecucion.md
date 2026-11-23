# Plan de ejecución

[↑ Glosario](../../README.md) · [← Plan adaptativo](./plan-adaptativo.md) · [Plan de salida →](./plan-de-salida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

Secuencia de operaciones que el motor elige para resolver una consulta.

Definición de trabajo de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

## Por qué importa

En [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), el tema «Plan de ejecución» importa porque dice qué hace el motor en lugar de lo que se supone.

## Cómo funciona

Según [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), en la sección «Plan de ejecución»:

El plan es la decisión del motor sobre cómo ejecutar una consulta: recorrer toda la tabla (`SCAN`), buscar con un índice (`SEARCH ... USING INDEX`), ordenar aparte, usar un índice como cobertura. Se lee con `EXPLAIN QUERY PLAN` en SQLite y `EXPLAIN` en PostgreSQL. La regla es mirar el plan antes de creer en un índice y después de crearlo: el motor puede decidir no usarlo, usarlo de forma parcial o elegir otro. Un plan cambia con las estadísticas, el volumen y la forma de los parámetros.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

El equipo de la plataforma crea un catálogo de patrones de acceso, uno por consulta frecuente, con su frecuencia, su filtro y su plazo: «mis entregas» (por estudiante, ordenadas por fecha, cada pantalla), «panel del docente» (por curso y rango de fechas) y «informe nocturno» (promedios por curso). Para cada una anota el plan antes y después, los pasos medidos y el índice que la justifica.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)) son:

- **Se crea un índice y la consulta no mejora** — causa: condición poco selectiva o forma que no coincide con el prefijo. Corrección: mirar el plan y la selectividad antes y después.
- **Las escrituras se vuelven lentas con el tiempo** — causa: índices acumulados sin consulta que los justifique. Corrección: catálogo de patrones y revisión periódica.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos en pasos y planes. No se midió tiempo de reloj ni se usó otro motor; el recorrido por saltos y las decisiones del planificador son de SQLite 3.45 tras `ANALYZE` y pueden cambiar con otra versión o sin estadísticas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Motor](../m/motor.md), [Operación](../o/operacion.md), [Resolver](../r/resolver.md), [Secuencia](../s/secuencia.md), [Índice compuesto](../i/indice-compuesto.md), [N+1](../n/n-mas-1.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md).

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

[↑ Glosario](../../README.md) · [← Plan adaptativo](./plan-adaptativo.md) · [Plan de salida →](./plan-de-salida.md)
