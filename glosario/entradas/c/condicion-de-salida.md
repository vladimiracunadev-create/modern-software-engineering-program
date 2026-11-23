# Condición de salida

[↑ Glosario](../../README.md) · [← Condición de revisión](./condicion-de-revision.md) · [Confabulación →](./confabulacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Señal medible que indica cuándo retirar o simplificar el patrón.

Definición de trabajo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md): Señal medible para retirar el patrón.

## Por qué importa

En [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), el tema «Condición de salida» importa porque un patrón que no se puede retirar acumula costo

En [SE-323 — Taller: refactorizar con patrones y medir su costo](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), el tema «Condición de salida» importa porque evita que el patrón se quede por costumbre

En [SE-324 — Proyecto: catálogo de patrones de un sistema real](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-324-proyecto-catalogo-de-patrones-de-un-sistema-real/README.md), el tema «Condición de salida» importa porque evita el patrón por costumbre

## Cómo funciona

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

Todo patrón aplicado debe tener una **condición de salida**: la señal medible que dirá que ya no compensa. Para el `Strategy` de tarifas puede ser «si quedan dos canales, volver a una función con un `if`», o «si en un año no se añadió ninguna variante». Escribirla obliga a nombrar la fuerza (si no hay forma de saber cuándo dejó de importar, probablemente nunca fue clara) y evita que el patrón se vuelva un monumento. La condición de salida se registra junto al patrón en el catálogo de `SE-324`.

Según [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md):

Puede proponer candidatos y escribir la implementación, pero la fuerza y la condición de salida dependen de un contexto que está en las personas y en el código; un agente que elige el patrón sin ese contexto reproduce la costumbre. El puente con agentes de la clase muestra cómo pedirle el criterio y no el patrón.

## Ejemplo

Ejemplo de [SE-313 — Criterios para usar un catálogo de patrones](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md) (sección «Preguntas frecuentes»):

Puede proponer candidatos y escribir la implementación, pero la fuerza y la condición de salida dependen de un contexto que está en las personas y en el código; un agente que elige el patrón sin ese contexto reproduce la costumbre. El puente con agentes de la clase muestra cómo pedirle el criterio y no el patrón.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Todo patrón aplicado debe tener una **condición de salida**: la señal medible que dirá que ya no compensa. ([SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md))

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
