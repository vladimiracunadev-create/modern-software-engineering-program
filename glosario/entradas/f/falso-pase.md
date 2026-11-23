# Falso pase

[↑ Glosario](../../README.md) · [← Falso negativo](./falso-negativo.md) · [Falso positivo →](./falso-positivo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

La puerta publica una versión peor.

Definición de trabajo de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md).

## Por qué importa

En [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), el tema «Falso pase y falso rechazo» importa porque son los dos errores de la puerta y tienen costos distintos.

## Cómo funciona

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

Una puerta decide con una cifra. Puede equivocarse de dos maneras: dejar pasar una versión peor (**falso pase**) o rechazar una versión sana (**falso rechazo**). El costo no es simétrico: un falso pase publica una regresión; un falso rechazo retrasa un cambio y cuesta una investigación. Un umbral de 0,825 entre una versión sana de 0,85 y una regresada de 0,80 está justo en medio, así que los dos errores son igual de probables con cualquier ruido. Mover el umbral cambia uno a costa del otro; reducir el ruido mejora ambos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo no es simétrico: un falso pase publica una regresión; un falso rechazo retrasa un cambio y cuesta una investigación. ([SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Puerta](../p/puerta.md), [Versión](../v/version.md), [Conjunto curado](../c/conjunto-curado.md), [Evaluación](../e/evaluacion.md), [Falso rechazo](./falso-rechazo.md), [Pass@k y pass^k](../p/pass-k-y-pass-k.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Falso negativo](./falso-negativo.md) · [Falso positivo →](./falso-positivo.md)
