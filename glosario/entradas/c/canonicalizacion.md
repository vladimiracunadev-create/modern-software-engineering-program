# Canonicalización

[↑ Glosario](../../README.md) · [← Candidatos equivalentes](./candidatos-equivalentes.md) · [Caos de seguridad →](./caos-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Transformación que lleva distintas representaciones equivalentes de un contenido a una única forma antes de calcular su huella.

Definición de trabajo de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md): Transformación de una entrada a su forma única y completa (decodificada y normalizada) antes de validarla.

## Por qué importa

La clase donde se define, [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md), existe con este propósito: el proyecto integra la parte: elegir un dominio, formular una afirmación que se pueda refutar, escribir las invariantes y un modelo de referencia, medir con experimentos reproducibles, probar cuánto depende la decisión de los supuestos y entregar un dosier que otra persona pueda verificar.

## Cómo funciona

Según [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md):

**Cómo leer la figura.** Cada fila es una alteración de tres ficheros y cada columna la forma de calcular la huella; el número es cuántos ficheros cambian de huella y el color más oscuro es más cambios. Mira la columna de la izquierda: sobre los bytes, alteraciones que no cambian el contenido (saltos de línea, espacios) disparan la alarma; tras canonicalizar queda a cero, salvo la última fila, enmarcada, el cambio de una cifra, que alarma en ambos casos. **Dónde deja de valer:** la canonicalización elimina diferencias que el autor eligió ignorar (espacios finales, orden de claves); en un lenguaje donde esos espacios importan (un fichero de configuración sensible al sangrado) esa elección sería un error. Y ninguna huella dice si el contenido es correcto: solo si cambió.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md):

La persona que elige conciliación de pagos escribe su dosier con una afirmación («el libro conserva el dinero y detecta 5 de 5 fallos inyectados en 10 000 corridas de 200 operaciones, comparado con un modelo de referencia»), tres invariantes (conservación, saldo no negativo, asientos que cuadran), un oráculo en 40 líneas y los experimentos de `SE-294` ejecutados en dos sistemas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)) son:

- **Un dosier completo con afirmaciones sin evidencia** — causa: se valida la forma y no el sentido. Corrección: revisión de contenido por una persona ajena, con enlace de cada afirmación a su experimento.
- **«Es robusto» como conclusión** — causa: afirmación no refutable. Corrección: reformular con objeto, medida, umbral y población.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la canonicalización elimina diferencias que el autor eligió ignorar (espacios finales, orden de claves); en un lenguaje donde esos espacios importan (un fichero de configuración sensible al sangrado) esa elección sería un error. ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-289](../../../classes/part-24-software-especializado-y-dominios/se-289-software-cientifico-y-reproducibilidad/README.md), [SE-298](../../../classes/part-24-software-especializado-y-dominios/se-298-low-code-no-code-y-automatizacion-visual/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Huella](../h/huella.md), [Representación](../r/representacion.md), [Afirmación refutable](../a/afirmacion-refutable.md), [Análisis de sensibilidad global](../a/analisis-de-sensibilidad-global.md), [Codificación de salida](./codificacion-de-salida.md), [Consulta parametrizada](./consulta-parametrizada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-300 — Proyecto: diseño profundo de un dominio elegido](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-460 — Validación, codificación y clases de inyección](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md) — [Parte 38](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/README.md), Seguridad, privacidad y cumplimiento.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-468](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-468-proyecto-producto-con-seguridad-verificable/README.md).

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

[↑ Glosario](../../README.md) · [← Candidatos equivalentes](./candidatos-equivalentes.md) · [Caos de seguridad →](./caos-de-seguridad.md)
