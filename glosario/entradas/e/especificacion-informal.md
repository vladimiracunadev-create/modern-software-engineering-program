# Especificación informal

[↑ Glosario](../../README.md) · [← Especificación formal](./especificacion-formal.md) · [Especificación semiformal →](./especificacion-semiformal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción en lenguaje natural sin reglas de forma que permitan decidir mecánicamente si dos lecturas coinciden.

Definición de trabajo de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md).

## Por qué importa

En [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), el tema «Especificación informal» importa porque la prosa es barata y legible para todos, y es la que más lecturas admite.

## Cómo funciona

Según [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), en la sección «Especificación informal»:

La prosa es el nivel donde empieza todo y donde casi todo se queda. Su fortaleza es que cualquiera la lee, la discute y la corrige; su debilidad, que no tiene un procedimiento para decidir si dos lecturas son la misma. Una especificación informal bien hecha declara sus términos («día» significa bloque de 24 horas desde el plazo), nombra sus casos límite y trae ejemplos con valores. No se vuelve semiformal por usar viñetas: se vuelve semiformal cuando una regla de forma permite comprobar algo mecánicamente.

## Ejemplo

Caso medido en la sección «Especificación informal» de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md):

La prosa es el nivel donde empieza todo y donde casi todo se queda. Su fortaleza es que cualquiera la lee, la discute y la corrige; su debilidad, que no tiene un procedimiento para decidir si dos lecturas son la misma. Una especificación informal bien hecha declara sus términos («día» significa bloque de 24 horas desde el plazo), nombra sus casos límite y trae ejemplos con valores. No se vuelve semiformal por usar viñetas: se vuelve semiformal cuando una regla de forma permite comprobar algo mecánicamente.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)) son:

- **Dos sistemas dan notas distintas para la misma entrega y ambos «cumplen» la política** — causa: la frase admite varias lecturas y nadie ejecutó ninguna. Corrección: enumerar las lecturas, elegir una, y escribirla como predicado y como ejemplos de frontera.
- **Los ejemplos de la política son todos del camino típico y los defectos aparecen en el límite** — causa: se eligió el ejemplo más natural y no el que más separa lecturas. Corrección: añadir ejemplos en múltiplos de 24 horas, en el tope y en nota 0.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una especificación informal bien hecha declara sus términos («día» significa bloque de 24 horas desde el plazo), nombra sus casos límite y trae ejemplos con valores. ([SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Ambigüedad](../a/ambiguedad.md), [Especificación formal](./especificacion-formal.md), [Especificación semiformal](./especificacion-semiformal.md), [Mutante equivalente](../m/mutante-equivalente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Meyer, «On formalism in specifications» (IEEE Software, 1985)](https://doi.org/10.1109/MS.1985.229776) — los defectos de las especificaciones en lenguaje natural y la progresión hacia la formalidad; autoridad: IEEE Software.
- [Hall, «Seven myths of formal methods» (IEEE Software, 1990)](https://doi.org/10.1109/52.57887) — qué aportan y qué no aportan los métodos formales; autoridad: IEEE Software.
- [Newcombe et al., «How Amazon Web Services uses formal methods» (CACM, 2015)](https://doi.org/10.1145/2699417) — experiencia industrial de especificación formal para hallar defectos de diseño; autoridad: Communications of the ACM.
- [Woodcock et al., «Formal methods: practice and experience» (ACM Computing Surveys, 2009)](https://doi.org/10.1145/1592434.1592436) — estudio de uso industrial de métodos formales y de su coste; autoridad: ACM Computing Surveys.
- [Lamport, «Who builds a house without drawing blueprints?» (CACM, 2015)](https://doi.org/10.1145/2736348) — argumento a favor de especificar antes de codificar; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Especificación formal](./especificacion-formal.md) · [Especificación semiformal →](./especificacion-semiformal.md)
