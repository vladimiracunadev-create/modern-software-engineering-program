# Análisis de sensibilidad global

[↑ Glosario](../../README.md) · [← Análisis de sensibilidad](./analisis-de-sensibilidad.md) · [Análisis entre artefactos →](./analisis-entre-artefactos.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Estudio del efecto de variar a la vez los supuestos inciertos sobre una decisión.

Definición de trabajo de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md).

## Por qué importa

La clase donde se define, [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), existe con este propósito: el proyecto integra la parte: elegir un dominio, formular una afirmación que se pueda refutar, escribir las invariantes y un modelo de referencia, medir con experimentos reproducibles, probar cuánto depende la decisión de los supuestos y entregar un dosier que otra persona pueda verificar.

## Cómo funciona

[SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md):

La persona que elige conciliación de pagos escribe su dosier con una afirmación («el libro conserva el dinero y detecta 5 de 5 fallos inyectados en 10 000 corridas de 200 operaciones, comparado con un modelo de referencia»), tres invariantes (conservación, saldo no negativo, asientos que cuadran), un oráculo en 40 líneas y los experimentos de `SE-294` ejecutados en dos sistemas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)) son:

- **Un dosier completo con afirmaciones sin evidencia** — causa: se valida la forma y no el sentido. Corrección: revisión de contenido por una persona ajena, con enlace de cada afirmación a su experimento.
- **«Es robusto» como conclusión** — causa: afirmación no refutable. Corrección: reformular con objeto, medida, umbral y población.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)) son: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se auditó ningún sistema real, norma ni proveedor y no hubo revisión de una persona experta en ningún dominio: el dosier de ejemplo, el modelo de coste, los rangos y las mutaciones son construcciones del autor. La siguiente parte, la 24, vuelve al diseño del código con cohesión, acoplamiento y encapsulación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Sobre](../s/sobre.md), [Supuestos](../s/supuestos.md), [Afirmación refutable](./afirmacion-refutable.md), [Canonicalización](../c/canonicalizacion.md), [Manifiesto](../m/manifiesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Saltelli et al., «Global Sensitivity Analysis: The Primer» (2008)](https://doi.org/10.1002/9780470725184) — análisis de sensibilidad global; autoridad: Wiley.
- [NIST SP 800-218, «Secure Software Development Framework (SSDF)»](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro y conservación de evidencia; autoridad: NIST.
- [Architectural Decision Records](https://adr.github.io/) — registro de decisiones con contexto y consecuencias; autoridad: comunidad ADR.
- [Peng, «Reproducible Research in Computational Science» (Science, 2011)](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad; autoridad: Science.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Análisis de sensibilidad](./analisis-de-sensibilidad.md) · [Análisis entre artefactos →](./analisis-entre-artefactos.md)
