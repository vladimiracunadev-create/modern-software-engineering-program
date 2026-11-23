# Clase de dios

[↑ Glosario](../../README.md) · [← Clase de cambio](./clase-de-cambio.md) · [Clase de referencia →](./clase-de-referencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md)

## Definición

Clase con muchas razones para cambiar y muchas dependencias.

Definición de trabajo de [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md).

## Por qué importa

En [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), el tema «Clase de dios y cohesión» importa porque muchas razones de cambio en un lugar

## Cómo funciona

Según [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

Un **antipatrón** es una estructura recurrente con un daño conocido (la «bola de barro» de Foote y Yoder, la clase de dios). Un **olor de código** es una señal superficial que a menudo corresponde a un problema más profundo, y a veces no (Fowler lo describe así: una indicación que merece investigarse). Una **incomodidad** es algo que molesta a quien lo lee sin costo medido. Distinguirlos importa porque piden respuestas distintas: el antipatrón se corrige con un refactor planificado, el olor se investiga con una medida, la incomodidad se deja o se arregla cuando se pasa cerca. Llamar «antipatrón» a toda incomodidad es la forma habitual de gastar tiempo de refactor sin retorno.

Según [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md):

Puede señalar candidatos, pero sin medida tiende a confirmar el nombre («esto parece una clase de dios»). La petición útil pide la medida (pares sin estado, dependencias, ciclos) y la clasificación con su límite.

## Ejemplo

Ejemplo de [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) (sección «Preguntas frecuentes»):

Puede señalar candidatos, pero sin medida tiende a confirmar el nombre («esto parece una clase de dios»). La petición útil pide la medida (pares sin estado, dependencias, ciclos) y la clasificación con su límite.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si el equipo solo vigilara la complejidad ciclomática (una práctica habitual porque se calcula fácil), la clase de dios pasaría todos los umbrales. ([SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dependencia](../d/dependencia.md), [Antipatrón](../a/antipatron.md), [Ciclo de dependencias](./ciclo-de-dependencias.md), [Cohesión](./cohesion.md), [Componente fuertemente conexo](./componente-fuertemente-conexo.md), [Deuda de diseño](../d/deuda-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-322 — Antipatrones y deuda de diseño](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Clase de cambio](./clase-de-cambio.md) · [Clase de referencia →](./clase-de-referencia.md)
