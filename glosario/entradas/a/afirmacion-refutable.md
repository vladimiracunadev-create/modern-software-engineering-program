# Afirmación refutable

[↑ Glosario](../../README.md) · [← Afirmación](./afirmacion.md) · [Agencia excesiva →](./agencia-excesiva.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md)

## Definición

Una **afirmación refutable** es un enunciado con objeto, medida, umbral y población, de modo que un resultado concreto podría contradecirlo. [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) la usa en el proyecto de diseño profundo de un dominio: la unidad de lo que el dosier declara es una afirmación que puede resultar falsa, no un tema. El sentido es el del método científico aplicado al diseño: lo que no puede ser falso no informa.

## Por qué importa

Un dosier puede estar completo en forma y vacío en sentido. [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) lo nombra como error: validar la forma y no el sentido. Exigir afirmaciones refutables cambia la revisión: en lugar de preguntar «¿tiene la sección?», se pregunta «¿qué resultado me haría cambiar de opinión, y dónde está el experimento?».

## Cómo funciona

[SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) contrasta un tema con una afirmación. «Pagos» es un tema: nada puede contradecirlo. «El libro mayor conserva el dinero en 10 000 corridas aleatorias y detecta 5 de 5 fallos inyectados» es una afirmación: una sola corrida que pierda dinero, o un fallo inyectado no detectado, la refuta.

Una buena afirmación nombra cuatro cosas:

1. **Objeto:** qué se examina (el libro mayor).
2. **Medida:** qué se observa (conserva el dinero; detecta fallos).
3. **Umbral:** a partir de cuánto se cumple (10 000 corridas; 5 de 5).
4. **Población:** sobre qué casos vale (corridas aleatorias, fallos inyectados).

Y viene con lo que la haría falsa. Cada afirmación del dosier se enlaza con el experimento que la sostiene; sin enlace, es una opinión.

## Ejemplo

Reformulación basada en [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md): «el diseño es robusto» no se puede desmentir. Se reescribe como «ante 10 000 corridas con orden de mensajes aleatorio, el saldo total no cambia y cada una de 5 mutaciones del código es detectada por al menos una prueba». Ahora hay objeto (saldo total), medida, umbral y población, y existe un resultado que la derriba.

## Errores y confusiones comunes

- **«Es robusto» como conclusión:** afirmación no refutable; se reformula con objeto, medida, umbral y población ([SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md)).
- **Dosier completo con afirmaciones sin evidencia:** se validó la forma. La corrección que propone la clase es la revisión de contenido por una persona ajena, con enlace de cada afirmación a su experimento.
- **Confundir refutable con refutada:** una afirmación refutable que sobrevive a su prueba no queda demostrada para siempre; solo no ha sido contradicha en esa población.

## Límites y cuándo no aplica

Refutable no significa importante: se puede formular una afirmación precisa y trivial. Tampoco todo lo valioso en diseño se expresa así (una decisión de estilo o de legibilidad). Y depende de datos que se tengan: [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md) pide evitar afirmaciones que dependan de datos que no tienes. El dosier de ejemplo, el modelo de costo y las mutaciones de la clase son construcciones del autor, sin revisión de una persona experta en el dominio.

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
