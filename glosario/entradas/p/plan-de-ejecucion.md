# Plan de ejecución

[↑ Glosario](../../README.md) · [← Plan adaptativo](./plan-adaptativo.md) · [Plan de salida →](./plan-de-salida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md)

## Definición

El **plan de ejecución** es la secuencia de operaciones que el motor de base de datos elige para resolver una consulta ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)): recorrer toda la tabla, buscar con un índice, ordenar aparte, usar un índice como cobertura. No es lo que el programador escribe en SQL, sino lo que el motor decide hacer con ello.

## Por qué importa

SQL declara qué se quiere, no cómo obtenerlo. Por eso una consulta correcta puede ser rápida o lenta según el plan que el motor elija, y el programador no lo ve salvo que lo pida. La decisión que cambia es cómo se justifica un índice o una reescritura: mirando el plan, no confiando en que «debería ayudar».

## Cómo funciona

[SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) enumera las decisiones que el plan refleja: `SCAN` (recorrer toda la tabla), `SEARCH ... USING INDEX` (buscar con un índice), ordenar aparte, usar un índice como cobertura (la consulta se responde solo con el índice). Se lee con `EXPLAIN QUERY PLAN` en SQLite y con `EXPLAIN` en PostgreSQL.

La regla central de la clase: **mirar el plan antes de creer en un índice y después de crearlo**. El motor puede decidir no usarlo, usarlo de forma parcial o elegir otro. Y el plan no es estable: cambia con las estadísticas, el volumen y la forma de los parámetros. La clase da los motivos por los que un índice recién creado puede no mejorar la consulta: la condición es poco selectiva (casi todas las filas cumplen), o la forma de la consulta no coincide con el prefijo del índice compuesto.

El plan también sirve para detectar problemas de patrón, como el N+1, y para contar el costo de los índices: cada uno acelera lecturas pero encarece escrituras, de modo que acumular índices sin una consulta que los justifique vuelve lentas las escrituras con el tiempo; se corrige con un catálogo de patrones y revisión periódica.

## Ejemplo

Se crea un índice sobre `estado` en una tabla de entregas donde el 95 % de las filas tienen el mismo estado. `EXPLAIN QUERY PLAN` muestra que el motor sigue haciendo un `SCAN`, porque usar el índice no compensa con una condición tan poco selectiva. Con un índice compuesto que coincide con el filtro y el orden de la consulta, el plan pasa a `SEARCH ... USING INDEX`. Caso en la línea de [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

## Errores y confusiones comunes

- **Se crea un índice y la consulta no mejora**: condición poco selectiva o forma que no coincide con el prefijo; se corrige mirando el plan y la selectividad antes y después.
- **Las escrituras se vuelven lentas con el tiempo**: índices acumulados sin consulta que los justifiquen.
- **Dar por hecho que el plan es estable**: cambia con las estadísticas y el volumen.
- **Optimizar sin mirar el plan**.

## Límites y cuándo no aplica

[SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) precisa que sus experimentos usan datos sintéticos, no miden tiempo de reloj ni usan otro motor: los recorridos y las decisiones del planificador son de SQLite 3.45 tras `ANALYZE` y pueden cambiar con otra versión o sin estadísticas. Cada motor tiene su propio planificador y su propia notación. El plan dice qué hace el motor, no cuánto tarda en tu hardware: para eso hace falta medir.

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
