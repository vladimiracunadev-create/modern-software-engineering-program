# Filtro con estado

[↑ Glosario](../../README.md) · [← Filtro](./filtro.md) · [Finalización →](./finalizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Filtro que necesita retener elementos antes de emitir.

Definición de trabajo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md).

## Por qué importa

En [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), el tema «Filtros con estado» importa porque ordenar o agrupar retiene todo lo que llega.

## Cómo funciona

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

No todo filtro puede ser perezoso. Ordenar necesita ver todos los elementos antes de emitir el primero; agrupar por curso, eliminar duplicados o calcular un percentil también. Si en la misma cadena se añade un ordenamiento final, el pico de memoria pasó de 0,006 MB a 1,2 MB: unas 200 veces más, y proporcional al tamaño de lo que llega a ese filtro (aquí, los 16 259 avisos formateados). La cota no desaparece, pero deja de ser constante.

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Ejemplo

Ejemplo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La decisión de diseño es dónde poner los filtros con estado: lo más tarde posible (cuando el flujo ya está filtrado) y con un tamaño máximo declarado, y si el estado puede crecer sin límite, cambiar el algoritmo (por ejemplo, ordenar por bloques en disco) o aceptar que esa parte es un trabajo por lotes. ([SE-339](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Filtro](./filtro.md), [Cola de rechazos](../c/cola-de-rechazos.md), [Contrapresión](../c/contrapresion.md), [Flujo](./flujo.md), [Selectividad](../s/selectividad.md), [Tubería](../t/tuberia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Filtros con estado».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Filtro](./filtro.md) · [Finalización →](./finalizacion.md)
