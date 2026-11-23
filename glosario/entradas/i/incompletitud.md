# Incompletitud

[↑ Glosario](../../README.md) · [← Inclusión](./inclusion.md) · [Independencia de fuentes →](./independencia-de-fuentes.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Ausencia de un comportamiento para una situación que el sistema podrá encontrar.

Definición de trabajo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

## Por qué importa

En [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), el tema «Incompletitud» importa porque lo no dicho se decide en el código por quien programa.

## Cómo funciona

Según [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), en la sección «Incompletitud»:

Un conjunto es incompleto si omite una situación que debería contemplar. Las tablas de estado–evento lo hacen visible: si hay 6 estados y 7 eventos, hay 42 combinaciones y cada una debe tener un comportamiento (una transición, «se ignora» o «es imposible») o una pregunta abierta. No saber qué pasa si una estudiante retira una entrega en revisión es un hueco que alguien llenará en el código sin preguntar.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md):

Un inventario de defectos del expediente, con su tipo, su técnica de hallazgo y su responsable:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)) son:

- **Dos equipos implementan la misma frase de maneras distintas** — causa: la frase admite varias lecturas. Corrección: enumerar las lecturas y preguntar al autor, o reescribir con una plantilla estructurada.
- **Los requisitos se revisaron de dos en dos y el módulo no se puede construir** — causa: hay una contradicción de orden tres o más. Corrección: buscar subconjuntos mínimos incompatibles sobre las condiciones.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los requisitos, las variables y la tabla de estados son ejemplos del autor, la búsqueda exhaustiva no escala y la traducción a lógica es una interpretación no verificada. La siguiente clase aplica todo esto a un taller: reparar requisitos que no se pueden verificar.

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
