# Validador de estructura

[↑ Glosario](../../README.md) · [← Validador de especificaciones](./validador-de-especificaciones.md) · [Validador de forma →](./validador-de-forma.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Programa que comprueba propiedades mecánicas de la especificación y falla con un mensaje identificable.

Definición de trabajo de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).

## Por qué importa

En [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), el tema «Validador de estructura» importa porque detecta defectos mecánicos y barre lo repetitivo antes de la revisión humana.

## Cómo funciona

Según [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), en la sección «Validador de estructura»:

Un validador comprueba lo que una máquina puede decidir: identificadores únicos, referencias que existen, campos obligatorios, valores de una escala, ausencia de ciclos, marcadores como «por definir». Su valor es liberar a las personas de lo mecánico para que lean lo que importa; su límite es que no entiende el contenido. Una especificación que pasa el validador no está bien: está bien formada. Las pruebas del validador, con defectos inyectados, son la forma de saber qué cubre.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md):

El encabezado de la especificación entregada y el registro de revisión que la acompaña:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son:

- **La lectora tarda un día en entender qué falta** — causa: el expediente no responde sin su autor. Corrección: revisar el contenido contra la lista de elementos obligatorios.
- **El validador pasa y la especificación tiene errores graves** — causa: solo comprueba estructura. Corrección: documentar su cobertura con mutaciones y completar con revisión humana.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La especificación base, las 16 mutaciones, los costos y las probabilidades de detección son supuestos del autor, la lista de palabras vagas es un ejemplo mínimo y no participó ninguna revisora real. La [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md) toma este expediente y estudia cómo expresarlo con mayor formalidad: especificaciones, contratos y modelos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-155](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Especificación](../e/especificacion.md), [Propiedad](../p/propiedad.md), [Camino crítico](../c/camino-critico.md), [Contenido de una especificación](../c/contenido-de-una-especificacion.md), [Decisión de entrega](../d/decision-de-entrega.md), [Revisión por pares](../r/revision-por-pares.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-156 — Proyecto: especificación de requisitos revisable](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — contenido de una especificación y características de los requisitos; autoridad: ISO, IEC e IEEE.
- [Fagan: Design and code inspections to reduce errors in program development (1976)](https://doi.org/10.1147/sj.153.0182) — inspecciones con roles; autoridad: IBM Systems Journal.
- [Eick et al.: Estimating software fault content before coding (1992)](https://doi.org/10.1145/143062.143090) — captura–recaptura aplicada a revisiones; autoridad: ACM, International Conference on Software Engineering.
- [Zave y Jackson: Four dark corners of requirements engineering (1997)](https://doi.org/10.1145/237432.237434) — requisitos, supuestos y especificación; autoridad: ACM Transactions on Software Engineering and Methodology.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — revisión y gestión de requisitos; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Validador de especificaciones](./validador-de-especificaciones.md) · [Validador de forma →](./validador-de-forma.md)
