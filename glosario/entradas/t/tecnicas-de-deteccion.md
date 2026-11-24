# Técnicas de detección

[↑ Glosario](../../README.md) · [← Teclado y foco](./teclado-y-foco.md) · [Tecnología de apoyo →](./tecnologia-de-apoyo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Las **técnicas de detección** (de defectos de especificación) son procedimientos para buscar un tipo de defecto, cada uno ciego a los demás ([SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)). El término agrupa la caja de herramientas de revisión de requisitos: no existe una técnica universal, sino una por tipo de defecto.

## Por qué importa

Cada defecto se busca de forma distinta y ninguna técnica encuentra todos. Si un equipo revisa solo leyendo, encontrará lo que la lectura permite y declarará limpio un documento con contradicciones de orden tres. Cambia la planificación de una revisión: se escoge la técnica por el defecto que se quiere descartar y se declara cuáles quedaron sin cubrir.

## Cómo funciona

[SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) empareja tipos de defecto con técnicas:

- **Ambigüedad estructural** (una frase con varias lecturas): enumerar las lecturas y comparar sus resultados.
- **Ambigüedad léxica** (una palabra vaga): un glosario y una lista de términos prohibidos sin criterio («rápido», «fácil»).
- **Contradicción**: convertir los requisitos en condiciones sobre variables y buscar un estado que los cumpla todos; si no existe, hallar los subconjuntos mínimos que lo impiden.
- **Incompletitud**: enumerar combinaciones de estado y evento, o de condiciones (tablas de decisión).

La causa de que ninguna sirva para todo es que cada una opera sobre una representación distinta: la lectura detecta lo que se ve en el texto; la traducción a condiciones detecta lo que se ve en la lógica; la enumeración de combinaciones detecta lo que falta. Un defecto de un tipo es invisible para la técnica de otro.

El resultado se organiza en un inventario del expediente con tipo de defecto, técnica de hallazgo y responsable. La clase advierte que el inventario es apropiado cuando cada defecto tiene tipo, técnica y responsable, y peligroso cuando es una lista de observaciones sin dueño.

## Ejemplo

Tres requisitos de plazos que se revisan de dos en dos pasan la inspección. Traducidos a condiciones sobre variables (hora de cierre, hora de entrega, estado de la tarea), un resolutor encuentra que no existe ninguna asignación que los cumpla todos: hay una contradicción de orden tres que ninguna revisión por pares podía ver. Con una frase como «el sistema responderá rápido», en cambio, la técnica útil es la léxica: una lista de términos vagos la marca para reescribirla con un número. (Ilustración del mecanismo de [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).)

## Errores y confusiones comunes

- **Dos equipos implementan la misma frase distinto**: la frase admite varias lecturas; corrección: enumerarlas y preguntar al autor, o reescribir con una plantilla estructurada.
- **Requisitos revisados de dos en dos que no se pueden construir**: hay una contradicción de orden tres o más; corrección: buscar subconjuntos mínimos incompatibles.
- **Aplicar una sola técnica y declarar el documento limpio.**
- **Inventario sin dueño.**

## Límites y cuándo no aplica

Las técnicas formales exigen que los requisitos se expresen como condiciones decidibles, lo que no siempre es posible ni rentable. Una técnica no sustituye la validación con las personas que usarán el sistema: detecta defectos del texto, no necesidades ausentes. Para un conjunto pequeño y de bajo riesgo, la lectura cuidadosa suele bastar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tipo](./tipo.md), [Ambigüedad](../a/ambiguedad.md), [Contradicción](../c/contradiccion.md), [Incompletitud](../i/incompletitud.md), [Resolución](../r/resolucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

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

[↑ Glosario](../../README.md) · [← Teclado y foco](./teclado-y-foco.md) · [Tecnología de apoyo →](./tecnologia-de-apoyo.md)
