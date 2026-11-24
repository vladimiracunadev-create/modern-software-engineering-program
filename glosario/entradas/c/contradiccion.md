# Contradicción

[↑ Glosario](../../README.md) · [← Contracargo](./contracargo.md) · [Contraejemplo →](./contraejemplo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

En ingeniería de requisitos, una **contradicción** es una relación entre requisitos que no pueden cumplirse todos a la vez, directamente o a través de otros. Es el sentido de [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), que la sitúa junto a la ambigüedad y la incompletitud como los tres defectos clásicos de una especificación. [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) usa la misma idea para instrucciones dadas a un modelo: las reglas contradictorias provocan elecciones arbitrarias entre ellas.

## Por qué importa

Cambia cuándo se descubre que algo no se puede construir. Requisitos incompatibles hacen imposible cumplirlos todos, y quien implementa acabará eligiendo uno en silencio. Detectarlo al especificar cuesta una pregunta; detectarlo con el sistema construido cuesta un rediseño o una excepción permanente.

## Cómo funciona

[SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) distingue dos formas. La **contradicción directa** («guardar» frente a «no guardar») es rara y se ve a simple vista. La frecuente es la **indirecta**: requiere varias premisas para aparecer, y un conjunto puede ser inconsistente sin que ningún par lo sea. Por eso la revisión por pares, que compara requisitos de dos en dos, no encuentra las contradicciones más costosas.

La detección sistemática traduce los requisitos a una forma donde se pueda decidir si existe algún estado que los cumpla todos. Si no existe, se buscan **subconjuntos mínimos incompatibles**: los requisitos más pequeños que, juntos, no pueden satisfacerse. Eso señala qué conjunto de personas debe decidir. El hallazgo se registra como defecto con tipo, técnica y responsable, no como una observación suelta.

## Ejemplo

En [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) el inventario de defectos muestra tres casos para comparar: una ambigüedad que desaparece al añadir un ejemplo, una contradicción que solo aparece tras un cambio hecho en [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), y una celda abierta que resultó imposible por una regla de la interfaz. El inventario es útil cuando cada defecto tiene tipo, técnica y responsable; es peligroso cuando se reduce a observaciones sin dueño.

## Errores y confusiones comunes

- **Revisar de dos en dos y declarar el conjunto consistente.** Hay contradicciones de orden tres o más; buscar subconjuntos mínimos incompatibles sobre las condiciones ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)).
- **Confundir contradicción con ambigüedad.** Una contradicción persiste aunque cada requisito sea claro; una ambigüedad desaparece al precisarlo.
- **Resolverla eligiendo al azar.** Debe decidir quien tiene autoridad sobre ambos requisitos.
- **Pensar que solo existe entre requisitos funcionales.** También ocurre entre atributos de calidad.

## Límites y cuándo no aplica

La detección formal exige expresar los requisitos con precisión suficiente; con texto libre solo se encuentran contradicciones evidentes. Un conjunto consistente no es un conjunto correcto: puede ser consistente y no resolver el problema. En requisitos de calidad la incompatibilidad suele ser un compromiso a negociar más que una contradicción lógica. Y los ejemplos de [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) usan identificadores y requisitos ilustrativos.

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
