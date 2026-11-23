# Táctica

[↑ Glosario](../../README.md) · [← Tablas de decisión](./tablas-de-decision.md) · [Tail latency →](./tail-latency.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Técnica puntual que mueve un atributo, independiente del estilo.

Definición de trabajo de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

## Por qué importa

En [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), el tema «Táctica y estilo» importa porque confundirlos lleva a adoptar un estilo entero para obtener una táctica.

## Cómo funciona

Según [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

Una táctica es una técnica puntual que mueve un atributo: una caché baja la latencia, una réplica sube la disponibilidad, una cola desacopla en el tiempo. Un estilo agrupa tácticas que se refuerzan y deja fuera las que lo contradicen. La confusión frecuente es adoptar un estilo completo por una táctica: se separa el sistema en servicios para poder escalar un módulo, cuando bastaba con ejecutar varias copias del monolito detrás de un balanceador. La pregunta de control es: ¿qué táctica específica necesito y qué estilo mínimo la hace posible?

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md)) son: La matriz, los pesos y los cuatro contextos son construcciones del autor; los resultados muestran el mecanismo de decisión y no recomiendan ningún estilo para un sistema real. No se midió ningún sistema, equipo ni producto. El siguiente paso, `SE-338`, estudia el primer estilo concreto: el microkernel, que compra extensión por terceros y paga con un contrato que hay que mantener.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Escenario de calidad](../e/escenario-de-calidad.md), [Estilo arquitectónico](../e/estilo-arquitectonico.md), [Margen](../m/margen.md), [Matriz de decisión](../m/matriz-de-decision.md), [Punto de compromiso](../p/punto-de-compromiso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-337 — Estilos como respuestas a fuerzas de calidad](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-416](../../../classes/part-34-saas-y-plataformas-de-producto/se-416-marketplaces-y-plataformas-de-dos-lados/README.md), [SE-529](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-529-liderazgo-tecnico-sin-autoridad-formal/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tablas de decisión](./tablas-de-decision.md) · [Tail latency →](./tail-latency.md)
