# Selectividad

[↑ Glosario](../../README.md) · [← Selección por petición](./seleccion-por-peticion.md) · [Selector de patrón →](./selector-de-patron.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

La **selectividad** de una condición es la fracción de filas que deja pasar ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md)). [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) la usa en el sentido general de la proporción de elementos que un filtro deja pasar. Una condición es muy selectiva cuando deja pasar pocas filas y poco selectiva cuando deja pasar la mayoría.

## Por qué importa

Un índice no ayuda por existir: ayuda cuando permite evitar leer la mayor parte de la tabla. Eso depende de la selectividad de las condiciones de las consultas. La decisión que cambia es dónde se crean índices: sobre condiciones que seleccionan pocas filas, y no sobre columnas con pocos valores distintos donde casi todas las filas cumplen.

## Cómo funciona

[SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) lo explica con dos casos. Buscar un estudiante entre 2 000 devuelve una fracción mínima: el índice permite ir directo a esa fila y evita recorrer el resto. En cambio, cuando una condición selecciona la mayoría (el 90 % de las entregas están «enviadas»), recorrer el índice y luego leer casi todas las filas cuesta casi lo mismo que recorrer la tabla; y puede costar más, porque cada fila exige un salto adicional desde el índice. Por eso un índice sobre una columna con pocos valores distintos solo es útil para sus valores **raros**.

La selectividad explica el síntoma más común: se crea un índice y la consulta no mejora. La clase da un procedimiento de prueba: mirar el plan (¿usa el índice?), actualizar las estadísticas, comparar los pasos con y sin índice y calcular la fracción de filas que cumple. Si el plan usa el índice, el ahorro es del 3 % y la fracción es el 90 %, la causa es la baja selectividad.

El motor decide usando estadísticas sobre la distribución de valores: por eso el plan puede cambiar al variar los datos o al actualizar las estadísticas. En [SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) el mismo concepto aparece en el diseño de filtros dentro de flujos de procesamiento: la proporción que pasa condiciona el tamaño de lo que sigue.

## Ejemplo

La tabla de entregas tiene la columna `estado`, con el 90 % de las filas en «enviada». Un índice sobre `estado` no mejora la consulta por «enviada», porque habría que leer casi toda la tabla; sí podría ayudar para el estado raro «en revisión», que selecciona una fracción pequeña. Ejemplo de [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

## Errores y confusiones comunes

- **Se crea un índice y la consulta no mejora**: condición poco selectiva o forma que no coincide con el prefijo; se corrige mirando el plan y la selectividad antes y después.
- **Indexar columnas de pocos valores** sin considerar sus valores raros.
- **Suponer que la selectividad es una propiedad de la columna**: lo es de la condición sobre los datos actuales.
- **No actualizar estadísticas** y decidir con datos viejos.

## Límites y cuándo no aplica

El umbral a partir del cual un índice deja de compensar depende del motor y de cómo están almacenadas las filas; no hay una cifra universal. Los experimentos de [SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) usan datos sintéticos y SQLite, y sus resultados no se extrapolan a otros motores. En tablas pequeñas, recorrerlas completas puede ser igual de rápido y el índice solo añade costo de escritura.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Filtro](../f/filtro.md), [Cola de rechazos](../c/cola-de-rechazos.md), [Contrapresión](../c/contrapresion.md), [Filtro con estado](../f/filtro-con-estado.md), [Flujo](../f/flujo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md).

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

[↑ Glosario](../../README.md) · [← Selección por petición](./seleccion-por-peticion.md) · [Selector de patrón →](./selector-de-patron.md)
