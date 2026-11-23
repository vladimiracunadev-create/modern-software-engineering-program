# Cola de rechazos

[↑ Glosario](../../README.md) · [← Cola de radio](./cola-de-radio.md) · [Cola de trabajo →](./cola-de-trabajo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Destino de lo que no se pudo procesar, con su causa.

Definición de trabajo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md).

## Por qué importa

La clase donde se define, [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md), existe con este propósito: la clase existe para que reconozcas cuándo un procesamiento se entiende mejor como una cadena de transformaciones independientes y qué hay que decidir para que esa cadena sea segura: cuánta memoria retiene, en qué orden se aplican los pasos, qué pasa cuando un paso es más lento que el anterior y qué se hace con el registro que no se puede procesar.

## Cómo funciona

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

Un filtro recibe un registro malformado. Hay tres respuestas. Detener todo el flujo es lo más seguro y lo menos disponible: en el experimento, una excepción sin manejar en el registro 5 detuvo la cadena de 20. Saltar el registro y seguir sin dejar rastro es disponible y peligroso, porque los datos desaparecen en silencio. Desviarlo a una cola de rechazos con su causa permite continuar (19 procesados y 1 rechazado) y deja una lista revisable. La tercera es la que casi siempre conviene, con una condición: alguien debe mirar la cola de rechazos y se mide su tamaño; una cola de rechazos que nadie lee es un salto silencioso con pasos adicionales.

Según [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Ejemplo

Ejemplo de [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos* migra el volcado nocturno a una cadena de filtros. Al ponerla en producción descubre dos cosas. La primera: el paso de ordenar los avisos por urgencia, que alguien añadió al final «para que salgan ordenados», retiene todo el lote y es el único que escala con el volumen. Tras discutirlo se decide ordenar solo dentro de cada curso (un filtro con estado, pero de tamaño acotado por el número de entregas de un curso) y entregar el orden global como una consulta aparte. La segunda: una fila con un código de curso nulo detenía la cadena entera a las tres de la mañana.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md)) son: Los datos son sintéticos, la memoria es la de Python y los tiempos de hilo dependen del sistema; no se midió ninguna plataforma de flujo de datos ni un sistema de producción. El siguiente paso, `SE-340`, cambia de eje: separar procesos y llamarse por red, con los costos que un límite de proceso añade a cada llamada.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-338](../../../classes/part-28-estilos-arquitectonicos/se-338-microkernel-y-arquitecturas-de-plugins/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrapresión](./contrapresion.md), [Filtro](../f/filtro.md), [Filtro con estado](../f/filtro-con-estado.md), [Flujo](../f/flujo.md), [Selectividad](../s/selectividad.md), [Tubería](../t/tuberia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-339 — Pipes and filters y arquitecturas de flujo](../../../classes/part-28-estilos-arquitectonicos/se-339-pipes-and-filters-y-arquitecturas-de-flujo/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «dead letter».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cola de radio](./cola-de-radio.md) · [Cola de trabajo →](./cola-de-trabajo.md)
