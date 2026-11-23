# Afirmación refutable

[↑ Glosario](../../README.md) · [← Afirmación](./afirmacion.md) · [Agencia excesiva →](./agencia-excesiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Enunciado con objeto, medida, umbral y población que un resultado concreto podría contradecir.

Definición de trabajo de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md).

## Por qué importa

En [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), el tema «Afirmación refutable» importa porque convierte un tema en algo que puede ser falso.

## Cómo funciona

Según [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), en la sección «Afirmación refutable»:

Un tema («pagos») no se puede refutar; una afirmación («el libro mayor conserva el dinero en 10 000 corridas aleatorias y detecta 5 de 5 fallos inyectados») sí: basta una corrida que la contradiga. Una buena afirmación nombra el objeto, la medida, el umbral y la población sobre la que se hace, y va acompañada de lo que la haría falsa. Evita las afirmaciones que ningún resultado podría desmentir («el diseño es robusto») y las que dependen de datos que no tienes. Cada afirmación del dosier debe enlazar con el experimento que la sostiene.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md):

La persona que elige conciliación de pagos escribe su dosier con una afirmación («el libro conserva el dinero y detecta 5 de 5 fallos inyectados en 10 000 corridas de 200 operaciones, comparado con un modelo de referencia»), tres invariantes (conservación, saldo no negativo, asientos que cuadran), un oráculo en 40 líneas y los experimentos de `SE-294` ejecutados en dos sistemas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)) son:

- **Un dosier completo con afirmaciones sin evidencia** — causa: se valida la forma y no el sentido. Corrección: revisión de contenido por una persona ajena, con enlace de cada afirmación a su experimento.
- **«Es robusto» como conclusión** — causa: afirmación no refutable. Corrección: reformular con objeto, medida, umbral y población.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)) son: Las definiciones son operativas para el proyecto. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se auditó ningún sistema real, norma ni proveedor y no hubo revisión de una persona experta en ningún dominio: el dosier de ejemplo, el modelo de coste, los rangos y las mutaciones son construcciones del autor. La siguiente parte, la 24, vuelve al diseño del código con cohesión, acoplamiento y encapsulación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Objeto](../o/objeto.md), [Resultado](../r/resultado.md), [Análisis de sensibilidad global](./analisis-de-sensibilidad-global.md), [Canonicalización](../c/canonicalizacion.md), [Manifiesto](../m/manifiesto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-218, «Secure Software Development Framework (SSDF)»](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas de desarrollo seguro y conservación de evidencia; autoridad: NIST.
- [Architectural Decision Records](https://adr.github.io/) — registro de decisiones con contexto y consecuencias; autoridad: comunidad ADR.
- [Saltelli et al., «Global Sensitivity Analysis: The Primer» (2008)](https://doi.org/10.1002/9780470725184) — análisis de sensibilidad global; autoridad: Wiley.
- [Peng, «Reproducible Research in Computational Science» (Science, 2011)](https://doi.org/10.1126/science.1213847) — espectro de reproducibilidad; autoridad: Science.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Afirmación](./afirmacion.md) · [Agencia excesiva →](./agencia-excesiva.md)
