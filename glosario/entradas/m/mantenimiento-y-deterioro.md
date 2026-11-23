# Mantenimiento y deterioro

[↑ Glosario](../../README.md) · [← Mantenimiento preventivo](./mantenimiento-preventivo.md) · [Mapa →](./mapa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Esfuerzo necesario para que los enlaces sigan siendo ciertos y su pérdida por cambios no registrados.

Definición de trabajo de [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md).

## Por qué importa

En [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), el tema «Mantenimiento y deterioro» importa porque una matriz manual se degrada; hay que detectarlo o mantenerla automáticamente.

## Cómo funciona

Según [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md), en la sección «Mantenimiento y deterioro»:

Los enlaces cambian porque cambian los nombres, los documentos y las personas. Una matriz en una hoja de cálculo depende de que alguien recuerde actualizarla; cada sprint pierde una fracción de enlaces válidos, y el efecto se compone. Las defensas son tres: poner el enlace donde cambia el artefacto (la etiqueta en la prueba), verificar la matriz automáticamente al integrar, y reducir el número de enlaces a los que responden preguntas reales.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md):

La cadena del requisito conductor, con una etiqueta en cada artefacto y un verificador al integrar:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son:

- **Una auditoría tarda un día en encontrar una prueba** — causa: la matriz está en un documento que nadie actualiza. Corrección: poner la etiqueta en la prueba y verificarla al integrar.
- **Casi todo cambio «afecta» a casi todo** — causa: se enlazó todo con todo. Corrección: reducir los enlaces a los que responden preguntas concretas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-151 — Trazabilidad desde necesidad hasta evidencia](../../../classes/part-12-ingenieria-de-requisitos/se-151-trazabilidad-desde-necesidad-hasta-evidencia/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se analizó ningún repositorio real, las tasas de deterioro son hipótesis y la traza cubre un módulo de juguete. La siguiente clase cruza la matriz con obligaciones externas: datos personales, seguridad y regulación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis de impacto](../a/analisis-de-impacto.md), [Enlace frente a evidencia](../e/enlace-frente-a-evidencia.md), [Granularidad de los enlaces](../g/granularidad-de-los-enlaces.md), [Trazabilidad bidireccional](../t/trazabilidad-bidireccional.md).
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

[↑ Glosario](../../README.md) · [← Mantenimiento preventivo](./mantenimiento-preventivo.md) · [Mapa →](./mapa.md)
