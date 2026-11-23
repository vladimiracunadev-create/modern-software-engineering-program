# Fabricación pura

[↑ Glosario](../../README.md) · [← Extremo](../e/extremo.md) · [Facade →](./facade.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Pieza sin correspondencia con el dominio creada para sostener cohesión o bajo acoplamiento.

Definición de trabajo de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

## Por qué importa

En [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), el tema «Fabricación pura» importa porque una pieza sin correspondencia con el dominio, creada para bajar el acoplamiento

## Cómo funciona

Según [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

Los cuatro criterios restantes corrigen costos. El **Polimorfismo** reemplaza condicionales sobre el tipo con métodos del tipo (el Strategy de `SE-313`). La **Indirección** introduce un intermediario para bajar el acoplamiento directo (el Adapter de `SE-315`, el Repository de `SE-318`). La **Fabricación pura** crea una pieza sin correspondencia con el dominio para sostener alta cohesión: en el experimento, `total_puro(lineas)` calcula el total sin base de datos, sin reloj y sin dobles, y se prueba con una llamada. Las **Variaciones protegidas** envuelven un punto de cambio probable con una interfaz estable. Los cuatro tienen un costo común (una pieza más) y se justifican con la misma pregunta de `SE-313`: ¿qué dolor resuelven hoy?

## Ejemplo

Caso medido en la sección «Polimorfismo, Indirección, Fabricación pura y Variaciones protegidas» de [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md):

Los cuatro criterios restantes corrigen costos. El **Polimorfismo** reemplaza condicionales sobre el tipo con métodos del tipo (el Strategy de `SE-313`). La **Indirección** introduce un intermediario para bajar el acoplamiento directo (el Adapter de `SE-315`, el Repository de `SE-318`). La **Fabricación pura** crea una pieza sin correspondencia con el dominio para sostener alta cohesión: en el experimento, `total_puro(lineas)` calcula el total sin base de datos, sin reloj y sin dobles, y se prueba con una llamada. Las **Variaciones protegidas** envuelven un punto de cambio probable con una interfaz estable.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **Fabricación pura** crea una pieza sin correspondencia con el dominio para sostener alta cohesión: en el experimento, `total_puro(lineas)` calcula el total sin base de datos, sin reloj y sin dobles, y se prueba con una llamada. ([SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Acoplamiento](../a/acoplamiento.md), [Cohesión](../c/cohesion.md), [Dominio](../d/dominio.md), [Controlador](../c/controlador.md), [Creador](../c/creador.md), [Experto en información](../e/experto-en-informacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-317 — GRASP y asignación de responsabilidades](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Extremo](../e/extremo.md) · [Facade →](./facade.md)
