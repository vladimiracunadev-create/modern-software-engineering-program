# Granularidad de los enlaces

[↑ Glosario](../../README.md) · [← Granularidad](./granularidad.md) · [GraphQL →](./graphql.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **granularidad de los enlaces** es el nivel de detalle de los elementos que se enlazan en una matriz o cadena de trazabilidad: desde documentos completos hasta líneas de código ([SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)). Un enlace puede ir de un documento a otro, de un requisito a una prueba o de un criterio a una línea.

## Por qué importa

Decide si la trazabilidad es útil. Enlaces demasiado gruesos (documento con documento) no responden preguntas concretas; demasiado finos (criterio con línea de código) no se mantienen y se desactualizan con cada refactorización. Una mala elección produce una matriz que nadie consulta o que miente.

## Cómo funciona

El principio de [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) es que más fino responde preguntas más precisas y cuesta más mantener, de modo que la granularidad correcta es **la que responde las preguntas que alguien realmente hará**. Una auditoría pregunta por requisito y prueba; un cambio pregunta por requisito y módulo. Por eso la unidad habitual es el requisito, la prueba y el módulo, y no la línea.

La clase añade la razón por la que «más enlaces» no es mejor: enlazar todo con todo no aumenta la información, la diluye, porque ya no distingue lo relevante de lo incidental. Cuando casi cualquier cambio «afecta» a casi todo, el análisis de impacto deja de servir. Los síntomas y las correcciones: una auditoría que tarda un día en encontrar una prueba indica que la matriz vive en un documento que nadie actualiza, y se corrige poniendo la etiqueta en la prueba y verificándola al integrar; cuando todo afecta a todo, se reducen los enlaces a los que responden preguntas concretas.

## Ejemplo

En la cadena del requisito conductor de la plataforma, cada artefacto lleva una etiqueta (por ejemplo, el identificador del requisito en el nombre de la prueba y en un comentario del módulo) y un verificador al integrar comprueba que cada requisito tiene al menos una prueba y que cada prueba apunta a un requisito existente. La unidad es requisito-prueba-módulo: suficiente para una auditoría y para estimar el alcance de un cambio, sin enlazar cada línea. (La descripción de la etiqueta es una ilustración del mecanismo que enseña la clase.)

## Errores y confusiones comunes

- **Matriz en un documento aparte que nadie actualiza.**
- **Enlazar todo con todo**: ruido en lugar de señal.
- **Enlazar a nivel de línea**: se rompe en la primera refactorización.
- **Confundir enlace con evidencia**: que exista un enlace no prueba que la prueba verifique el requisito.

## Límites y cuándo no aplica

No hay granularidad correcta en abstracto: depende de las preguntas, del tamaño del sistema y del costo de mantenimiento. En dominios regulados, las obligaciones pueden exigir un detalle mayor del que el equipo escogería por sí solo. Para proyectos pequeños, la trazabilidad por requisito y prueba puede ser suficiente sin herramientas especiales. [SE-151](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) declara además que su traza cubre un módulo de juguete y que las tasas de deterioro son hipótesis.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Análisis de impacto](../a/analisis-de-impacto.md), [Enlace frente a evidencia](../e/enlace-frente-a-evidencia.md), [Mantenimiento y deterioro](../m/mantenimiento-y-deterioro.md), [Trazabilidad bidireccional](../t/trazabilidad-bidireccional.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gotel y Finkelstein: An analysis of the requirements traceability problem (1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE International Conference on Requirements Engineering.
- [Cleland-Huang et al.: Software traceability, trends and future directions (2014)](https://doi.org/10.1145/2593882.2593891) — estado y retos; autoridad: ACM, Future of Software Engineering.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — trazabilidad entre necesidades, requisitos y verificación; autoridad: ISO, IEC e IEEE.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de requisitos y trazabilidad; autoridad: IEEE Computer Society.
- [Python: `sys.settrace`](https://docs.python.org/3/library/sys.html#sys.settrace) — registro de llamadas durante la ejecución.

---

[↑ Glosario](../../README.md) · [← Granularidad](./granularidad.md) · [GraphQL →](./graphql.md)
