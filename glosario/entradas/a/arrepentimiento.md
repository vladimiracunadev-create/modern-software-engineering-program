# Arrepentimiento

[↑ Glosario](../../README.md) · [← Arrendamiento](./arrendamiento.md) · [Artefacto →](./artefacto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Diferencia entre el valor de la mejor decisión en un futuro realizado y el de la elegida.

Definición de trabajo de [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md).

## Por qué importa

En [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), el tema «Retorno esperado y arrepentimiento» importa porque el valor esperado resume, pero no dice cuán a menudo se acierta ni cuánto se pierde al errar.

## Cómo funciona

Según [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md):

El retorno esperado promedia futuros posibles. Dos medidas lo complementan: la fracción de futuros en que la cartera elegida es la mejor de todas, y el arrepentimiento, la diferencia entre el valor de la mejor cartera de ese futuro y el de la elegida. Una cartera puede ser excelente en promedio y rara vez la mejor: eso describe el riesgo de decidir sin saber, no un error de selección.

Según [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md):

En la plataforma, `portfolio-log.md` registra cada iniciativa con costo, rango de retorno, dependencias y responsable, la cartera elegida con las alternativas descartadas, la medida de robustez (veces que es la mejor, arrepentimiento) y la regla de revisión. El contrato es que ninguna cartera se aprueba sin sus alternativas y sin la fecha en que se revisará. Esa estructura permite que otra persona vea qué se descartó y por qué.

## Ejemplo

Ejemplo de [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) (sección «Ejemplo profesional»):

En la plataforma, `portfolio-log.md` registra cada iniciativa con costo, rango de retorno, dependencias y responsable, la cartera elegida con las alternativas descartadas, la medida de robustez (veces que es la mejor, arrepentimiento) y la regla de revisión. El contrato es que ninguna cartera se aprueba sin sus alternativas y sin la fecha en que se revisará. Esa estructura permite que otra persona vea qué se descartó y por qué.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El comité cree que la cartera «ganará»** — causa: se informó solo el valor esperado. Corrección: informar arrepentimiento y retorno neto p5. ([SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Es la mejor en 7,5 % de los 400 futuros; el arrepentimiento medio frente a la mejor de cada uno es 36,4 y el del percentil 95, 84,0. ([SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Dependencia](../d/dependencia.md), [Opción](../o/opcion.md), [Portafolio](../p/portafolio.md), [Secuencia](../s/secuencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) — prototipos para probar incertidumbres antes de construir y decisión de continuar; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: How the beta phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — construcción por etapas con evidencia de cada una; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — fase inicial que decide si avanzar; autoridad: Government Digital Service.
- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones y sensibilidad; autoridad: HM Treasury (Reino Unido).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Arrendamiento](./arrendamiento.md) · [Artefacto →](./artefacto.md)
