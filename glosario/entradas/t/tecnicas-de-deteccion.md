# Técnicas de detección

[↑ Glosario](../../README.md) · [← Teclado y foco](./teclado-y-foco.md) · [Tecnología de apoyo →](./tecnologia-de-apoyo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Procedimientos para buscar un tipo de defecto, cada uno ciego a los demás.

Definición de trabajo de [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md).

## Por qué importa

En [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), el tema «Técnicas de detección» importa porque cada defecto se busca de forma distinta y ninguna técnica encuentra todos.

## Cómo funciona

Según [SE-154 — Ambigüedad, contradicción e incompletitud](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), en la sección «Técnicas de detección»:

Para la ambigüedad estructural, enumerar las lecturas y comparar sus resultados; para la léxica, un glosario y una lista de términos prohibidos sin criterio. Para la contradicción, convertir los requisitos en condiciones sobre variables y buscar un estado que los cumpla todos o, si no existe, los subconjuntos mínimos que lo impiden. Para la incompletitud, enumerar combinaciones de estado y evento o de condiciones. Cada técnica encuentra el defecto para el que fue diseñada; ninguna encuentra uno de otro tipo.

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
