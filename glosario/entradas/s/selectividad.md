# Selectividad

[↑ Glosario](../../README.md) · [← Selección por petición](./seleccion-por-peticion.md) · [Selector de patrón →](./selector-de-patron.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Fracción de las filas que cumple una condición.

Definición de trabajo de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md): Proporción de elementos que un filtro deja pasar.

## Por qué importa

En [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), el tema «Selectividad» importa porque decide si un índice ahorra trabajo o solo lo reparte.

## Cómo funciona

Según [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), en la sección «Selectividad»:

La **selectividad** de una condición es la fracción de filas que deja pasar. Un índice sobre una columna ayuda cuando la condición selecciona pocas filas: buscar un estudiante entre 2 000 devuelve una fracción mínima y el índice evita recorrer el resto. Cuando una condición selecciona la mayoría (el 90 % de las entregas están «enviadas»), recorrer el índice y luego leer casi todas las filas cuesta casi lo mismo que recorrer la tabla. Un índice sobre una columna con pocos valores distintos solo es útil para sus valores raros.

## Ejemplo

Caso medido en la sección «Selectividad» de [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md):

La **selectividad** de una condición es la fracción de filas que deja pasar. Un índice sobre una columna ayuda cuando la condición selecciona pocas filas: buscar un estudiante entre 2 000 devuelve una fracción mínima y el índice evita recorrer el resto. Cuando una condición selecciona la mayoría (el 90 % de las entregas están «enviadas»), recorrer el índice y luego leer casi todas las filas cuesta casi lo mismo que recorrer la tabla. Un índice sobre una columna con pocos valores distintos solo es útil para sus valores raros.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se crea un índice y la consulta no mejora** — causa: condición poco selectiva o forma que no coincide con el prefijo. Corrección: mirar el plan y la selectividad antes y después. ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Prueba:** mira el plan (¿usa el índice?), actualiza las estadísticas y compara los pasos con y sin índice, y calcula la fracción de filas que cumple; si el plan usa el índice, el ahorro es del 3 % y la fracción es el 90 %, la causa es la baja selectividad. ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md))

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
