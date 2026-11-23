# Contradicción

[↑ Glosario](../../README.md) · [← Contracargo](./contracargo.md) · [Contraejemplo →](./contraejemplo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Relación entre requisitos que no pueden cumplirse todos a la vez, directa o a través de otros.

Definición de trabajo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

## Por qué importa

En [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), el tema «Contradicción» importa porque requisitos incompatibles hacen imposible cumplirlos todos.

En [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md), el tema «Contradicciones» importa porque provocan elecciones arbitrarias entre reglas

## Cómo funciona

Según [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), en la sección «Contradicción»:

Dos requisitos se contradicen si no pueden cumplirse a la vez. La contradicción directa («guardar» frente a «no guardar») es rara; la frecuente es indirecta: requiere varias premisas para aparecer. Un conjunto puede ser inconsistente sin que ningún par lo sea. Por eso la revisión por pares, que compara requisitos de dos en dos, no encuentra las contradicciones más costosas. La detección sistemática traduce los requisitos a una forma donde se pueda decidir si existe algún estado que los cumpla todos.

## Ejemplo

Ejemplo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sección «Ejemplo profesional»):

Los identificadores, las fechas y los requisitos son ilustrativos. Compara con la ambigüedad que desaparece al añadir un ejemplo, la contradicción que solo aparece tras un cambio de `SE-153` y la celda abierta que resultó imposible por una regla de la interfaz. El inventario es apropiado cuando cada defecto tiene tipo, técnica y responsable; es peligroso cuando es una lista de observaciones sin dueño.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los requisitos se revisaron de dos en dos y el módulo no se puede construir** — causa: hay una contradicción de orden tres o más. Corrección: buscar subconjuntos mínimos incompatibles sobre las condiciones. ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La contradicción directa («guardar» frente a «no guardar») es rara; la frecuente es indirecta: requiere varias premisas para aparecer. ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Relación](../r/relacion.md), [Ambigüedad](../a/ambiguedad.md), [Context engineering](./context-engineering.md), [Dimensión de decisión](../d/dimension-de-decision.md), [Incompletitud](../i/incompletitud.md), [Interpretación](../i/interpretacion.md).
- **Se confunde con:** Un «no encuentro contradicciones» de un modelo no equivale a consistencia.

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-560 — Context engineering y reducción de ambigüedad](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (26 clases más lo mencionan; las que más):

[SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-152](../../../classes/part-12-ingenieria-de-requisitos/se-152-requisitos-regulatorios-de-datos-y-seguridad/README.md), [SE-201](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-201-licencias-de-software-y-obligaciones-basicas/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Contradicciones».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Berry, Kamsties y Krieger: From contract drafting to software specification, linguistic sources of ambiguity (2003)](https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf) — tipos de ambigüedad en requisitos; autoridad: Universidad de Waterloo.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Heitmeyer, Jeffords y Labaw: Automated consistency checking of requirements specifications (1996)](https://doi.org/10.1145/234426.234431) — verificación de consistencia y completitud; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Harel: Statecharts, a visual formalism for complex systems (1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones; autoridad: Science of Computer Programming.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — requisitos, supuestos y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.

---

[↑ Glosario](../../README.md) · [← Contracargo](./contracargo.md) · [Contraejemplo →](./contraejemplo.md)
