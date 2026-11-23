# Muestreo y saturación

[↑ Glosario](../../README.md) · [← Muestreo de cola](./muestreo-de-cola.md) · [Multi-cloud →](./multi-cloud.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Elección de a quién entrevistar y criterio de cuándo parar, ligado a la probabilidad de encontrar los temas que importan.

Definición de trabajo de [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md).

## Por qué importa

En [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), el tema «Muestreo y saturación» importa porque la probabilidad de oír un tema depende de su prevalencia y del número de entrevistas, no de la sensación de haber oído lo mismo.

## Cómo funciona

Según [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md), en la sección «Muestreo y saturación»:

Si un tema afecta a una proporción p de las personas y se entrevistan n al azar, la probabilidad de oírlo al menos una vez es 1 − (1 − p)ⁿ. Con p = 10 % y n = 5 es 41 %: casi seis de cada diez estudios con cinco personas no lo oyen. La «saturación» (dejar de oír temas nuevos) es un criterio práctico, no una garantía: se alcanza antes con muestras homogéneas y se retrasa cuando hay subgrupos. Elegir a quién entrevistar —incluidos los casos extremos— importa tanto como cuántos son.

## Ejemplo

Caso medido en la sección «Muestreo y saturación» de [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md):

Si un tema afecta a una proporción p de las personas y se entrevistan n al azar, la probabilidad de oírlo al menos una vez es 1 − (1 − p)ⁿ. Con p = 10 % y n = 5 es 41 %: casi seis de cada diez estudios con cinco personas no lo oyen. La «saturación» (dejar de oír temas nuevos) es un criterio práctico, no una garantía: se alcanza antes con muestras homogéneas y se retrasa cuando hay subgrupos. Elegir a quién entrevistar —incluidos los casos extremos— importa tanto como cuántos son.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md)) son:

- **El informe afirma que «nadie mencionó X, así que X no importa»** — causa: se interpretó la ausencia en una muestra pequeña como ausencia en la población. Corrección: calcular la probabilidad de no oír el tema y declararla en el informe.
- **Las respuestas suenan todas iguales y amables** — causa: preguntas hipotéticas o guiadas que invitan a la cortesía. Corrección: preguntar por episodios pasados concretos y sondear con «¿y entonces qué hiciste?».

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se entrevistó a nadie, las prevalencias son supuestos y las codificadoras son simuladas. La siguiente clase convierte las citas verificadas en hipótesis y preguntas críticas que puedan refutarse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-122](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-122-usuarios-actores-trabajos-y-contextos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Codificación y acuerdo](../c/codificacion-y-acuerdo.md), [De la cita a la afirmación](../d/de-la-cita-a-la-afirmacion.md), [Entrevista como método](../e/entrevista-como-metodo.md), [Preguntas sobre el pasado](../p/preguntas-sobre-el-pasado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-123 — Investigación, entrevistas y evidencia cualitativa](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-123-investigacion-entrevistas-y-evidencia-cualitativa/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nielsen Norman Group: Why You Only Need to Test with 5 Users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) — argumento y límites de las muestras pequeñas en pruebas de usabilidad; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — introducción a la entrevista de usuario como método cualitativo; autoridad: Nielsen Norman Group.
- [McHugh: Interrater reliability, the kappa statistic (Biochemia Medica)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) — definición e interpretación de kappa frente al acuerdo bruto; autoridad: revisión indexada en PubMed Central.
- [GOV.UK Service Manual: User research](https://www.gov.uk/service-manual/user-research) — cómo planificar y conducir investigación con personas usuarias; autoridad: Government Digital Service.
- [The Mom Test](https://www.momtestbook.com/) — enfoque práctico para preguntar por hechos pasados y evitar la cortesía; autoridad: autor (guía práctica, no estudio empírico).

---

[↑ Glosario](../../README.md) · [← Muestreo de cola](./muestreo-de-cola.md) · [Multi-cloud →](./multi-cloud.md)
