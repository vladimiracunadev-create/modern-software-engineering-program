# Condición de salida

[↑ Glosario](../../README.md) · [← Condición de revisión](./condicion-de-revision.md) · [Confabulación →](./confabulacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Una **condición de salida** es la señal medible que indica cuándo retirar o simplificar un patrón de diseño ([SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md)). Se escribe en el momento de aplicar el patrón, no cuando ya molesta, y responde a la pregunta «¿qué tendría que ocurrir para que esto ya no compense?».

## Por qué importa

Un patrón aplicado tiene un costo estructural permanente: clases, indirección, nombres que aprender. Se justifica mientras la fuerza que lo motivó siga presente. Sin una condición de salida, el patrón sobrevive a su razón y se vuelve, en palabras de la clase, un monumento. La decisión que cambia es tratar un patrón como una apuesta con fecha de revisión, no como una mejora definitiva.

## Cómo funciona

[SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) pide que todo patrón aplicado lleve su condición de salida. Para el `Strategy` de tarifas, ejemplos de la clase: «si quedan dos canales, volver a una función con un `if`», o «si en un año no se añadió ninguna variante». Dos rasgos las hacen útiles:

1. **Es medible**: se puede comprobar con un conteo o una observación del repositorio, no con una impresión.
2. **Está atada a la fuerza**: la fuerza es la presión de diseño que justificó el patrón (por ejemplo, variantes que se añaden con frecuencia). Escribir la condición obliga a nombrarla. Si no hay forma de saber cuándo dejó de importar la fuerza, probablemente nunca fue clara.

La condición se registra junto al patrón en el catálogo de [SE-324](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), de modo que quien lea el patrón dentro de un año sepa qué comprobar. [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) la retoma con patrones de resiliencia: también ahí se define la señal que indica retirar el patrón.

El puente con agentes de [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) añade un matiz: un agente puede proponer candidatos y escribir la implementación, pero la fuerza y la condición de salida dependen de un contexto que está en las personas y en el código; un agente que elige el patrón sin ese contexto reproduce la costumbre.

## Ejemplo

Se aplica `Strategy` para calcular tarifas por canal de venta, con la condición de salida «si quedan dos canales o si en un año no se añade ninguna variante, se vuelve a una función con un `if`». Un año después se revisa el repositorio: no hubo variantes nuevas y solo quedan dos canales. La condición se cumple y se simplifica el código, con la red de pruebas existente. Ejemplo tomado de los casos que cita [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md).

## Errores y confusiones comunes

- **Aplicar el patrón sin escribir cuándo retirarlo**: nadie revisa y el patrón persiste.
- **Condición vaga** («cuando ya no haga falta»): no es medible.
- **Confundirla con la condición de aborto o de parada** de otros contextos: aquí se trata de retirar una decisión de diseño, no de detener un experimento.
- **Dejarla solo en la cabeza de quien aplicó el patrón**: debe quedar en el catálogo.

## Límites y cuándo no aplica

La señal no decide por sí sola: es el disparador de una revisión, no una orden automática de retirar. Lo que se mide puede ser un mal indicador de la fuerza, y la clase no ofrece umbrales universales: los ejemplos son del caso de tarifas. Para decisiones muy pequeñas y locales, escribir una condición puede costar más que el patrón mismo.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Patrón](../p/patron.md), [Señal](../s/senal.md), [Consecuencia](./consecuencia.md), [Costo estructural](./costo-estructural.md), [Entradas de frontera](../e/entradas-de-frontera.md), [Fuerza](../f/fuerza.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-054](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Condición de revisión](./condicion-de-revision.md) · [Confabulación →](./confabulacion.md)
