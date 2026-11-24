# Validador de estructura

[↑ Glosario](../../README.md) · [← Validador de especificaciones](./validador-de-especificaciones.md) · [Validador de forma →](./validador-de-forma.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Un **validador de estructura** es un programa que comprueba propiedades mecánicas de una especificación y falla con un mensaje identificable ([SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md)). Comprueba lo que una máquina puede decidir, sin entender el contenido.

## Por qué importa

Detecta defectos mecánicos y barre lo repetitivo antes de la revisión humana, de modo que las personas lean lo que importa. Cambia la división del trabajo de revisión: la máquina garantiza que la especificación esté bien formada; las personas juzgan si es correcta.

## Cómo funciona

El validador comprueba propiedades que se pueden decidir mecánicamente: **identificadores únicos**, **referencias que existen** (un requisito que cita otro inexistente), **campos obligatorios** (origen, criterio, dueño, prioridad), **valores de una escala**, **ausencia de ciclos** en las dependencias y **marcadores** como «por definir». Cada fallo se acompaña de un mensaje identificable (qué requisito, qué regla), para que se corrija sin buscar.

El límite está en la primera frase de la clase: no entiende el contenido. **Una especificación que pasa el validador no está bien: está bien formada.** Puede contener contradicciones, ambigüedades o requisitos equivocados con todos los campos llenos. Por eso [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) propone medir qué cubre el validador con **mutaciones**: se inyectan defectos conocidos en una especificación base (la clase usa 16) y se cuenta cuántos detecta. Los que sobreviven revelan qué no ve, y eso se documenta y se completa con revisión humana. La clase lo conecta con el contenido de una especificación: el validador comprueba que estén los elementos, no que sean buenos.

Los datos de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) son supuestos del autor (la especificación base, las 16 mutaciones, los costos y las probabilidades de detección), y la lista de palabras vagas es un ejemplo mínimo.

## Ejemplo

Una especificación con 20 requisitos. El validador comprueba que cada uno tenga identificador único, origen, criterio de aceptación, dueño y prioridad; que las referencias de dependencia apunten a requisitos existentes; que no haya ciclos; y que ningún texto contenga «por definir». Si un requisito cita `REQ-31` y no existe, falla con «REQ-14: dependencia REQ-31 inexistente». Si dos requisitos son contradictorios pero bien formados, pasa. (Ilustración del tipo de comprobaciones de [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md).)

## Errores y confusiones comunes

- **El validador pasa y hay errores graves**: solo comprueba estructura; corrección: documentar su cobertura con mutaciones y completar con revisión humana.
- **Pensar que «verde» significa «correcta».**
- **Mensajes de fallo ambiguos** que obligan a buscar.
- **Confundirlo con un linter de estilo de prosa**: este comprueba la estructura formal, no la redacción.

## Límites y cuándo no aplica

No detecta contradicciones, ambigüedades ni huecos de contenido (para eso hay técnicas de detección específicas). Requiere que la especificación tenga una estructura regular (formato legible por máquina). En especificaciones muy breves o informales, el costo de mantener el validador supera su beneficio.

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
