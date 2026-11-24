# Incompletitud

[↑ Glosario](../../README.md) · [← Inclusión](./inclusion.md) · [Independencia de fuentes →](./independencia-de-fuentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **incompletitud** de un conjunto de requisitos es la ausencia de un comportamiento para una situación que el sistema podrá encontrar ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)). Un conjunto es incompleto si omite una situación que debería contemplar. Es uno de los tipos de defecto de especificación, junto con la ambigüedad y la contradicción.

## Por qué importa

Lo no dicho se decide en el código por quien programa. Cuando la especificación calla, la persona que implementa elige un comportamiento, a menudo sin saber que lo está decidiendo y sin consultar a nadie. Cambia el momento y la persona que decide: lo que debió ser una decisión de producto queda como una suposición de programación.

## Cómo funciona

[SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) propone una técnica concreta para hacer visible la incompletitud: las **tablas estado–evento**. Si hay 6 estados y 7 eventos, hay 42 combinaciones, y cada una debe tener un comportamiento (una transición, «se ignora» o «es imposible») o una pregunta abierta. Una celda vacía es un hueco. El ejemplo de la clase: no saber qué pasa si una estudiante retira una entrega en revisión es un hueco que alguien llenará en el código sin preguntar.

La técnica funciona porque convierte «pensar en todo» en un recorrido finito y mecánico: en lugar de preguntar «¿qué se me olvida?», se enumeran las combinaciones y se pregunta por cada una. Lo mismo vale para condiciones: n condiciones binarias dan 2ⁿ combinaciones (tabla de decisión). Cada celda debe resolverse como acción, decisión pendiente con responsable o imposibilidad justificada.

La incompletitud es difícil de ver sin esa enumeración porque es ausencia: la lectura revisa lo que está escrito y las ausencias no se ven. Por eso se combina con otras técnicas de detección y con la validación con quienes usan el sistema. Cada técnica encuentra el defecto para el que fue diseñada; la enumeración de combinaciones encuentra huecos, y no encuentra contradicciones ni ambigüedades.

## Ejemplo

Estados de una entrega: borrador, enviada, en revisión, calificada, devuelta, retirada (6). Eventos: enviar, editar, retirar, calificar, devolver, reabrir, vencer plazo (7). La celda (en revisión, retirar) está vacía. Se plantea la pregunta: ¿se permite retirar una entrega en revisión? Respuesta del responsable: «sí, con aviso al docente» o «no». Cualquier respuesta es mejor que dejar que el código decida. (Caso de [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) con una enumeración ilustrativa.)

## Errores y confusiones comunes

- **Dos equipos implementan la misma frase de maneras distintas**: ambigüedad, no incompletitud.
- **Contradicción** de orden tres no vista en revisión por pares.
- **Llenar las celdas vacías con «lo obvio»** sin preguntar.
- **Creer que una especificación larga es completa.**

## Límites y cuándo no aplica

La enumeración solo cubre las dimensiones que se eligieron (estados y eventos); una situación fuera de ese modelo sigue sin verse. Con muchos estados y eventos, la tabla es enorme y se reduce con agrupaciones. Una especificación nunca es totalmente completa: se declara qué queda abierto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ambigüedad](../a/ambiguedad.md), [Contradicción](../c/contradiccion.md), [Resolución](../r/resolucion.md), [Técnicas de detección](../t/tecnicas-de-deteccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Berry, Kamsties y Krieger: From contract drafting to software specification, linguistic sources of ambiguity (2003)](https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf) — tipos de ambigüedad en requisitos; autoridad: Universidad de Waterloo.
- [Mavin et al.: Easy Approach to Requirements Syntax, EARS (2009)](https://doi.org/10.1109/RE.2009.9) — plantillas de redacción; autoridad: IEEE International Requirements Engineering Conference.
- [Heitmeyer, Jeffords y Labaw: Automated consistency checking of requirements specifications (1996)](https://doi.org/10.1145/234426.234431) — verificación de consistencia y completitud; autoridad: ACM Transactions on Software Engineering and Methodology.
- [Harel: Statecharts, a visual formalism for complex systems (1987)](https://doi.org/10.1016/0167-6423%2887%2990035-9) — estados y transiciones; autoridad: Science of Computer Programming.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — requisitos, supuestos y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.

---

[↑ Glosario](../../README.md) · [← Inclusión](./inclusion.md) · [Independencia de fuentes →](./independencia-de-fuentes.md)
