# Oscilación por supuesto

[↑ Glosario](../../README.md) · [← Orquestador de caos](./orquestador-de-caos.md) · [Outbox transaccional →](./outbox-transaccional.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Cambio del resultado al mover un supuesto de su percentil 10 al 90 con los demás en su valor central.

Definición de trabajo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Por qué importa

La clase donde se define, [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), existe con este propósito: el proyecto existe para reunir modelo de negocio, costos, métricas, riesgos y reversibilidad en un caso de viabilidad que otra persona puede recalcular, cuestionar y decidir sin pedir contexto: un valor presente con rango, un supuesto dominante, una regla de abandono y una decisión con responsable y fecha.

## Cómo funciona

Según [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md):

En la plataforma, `viability-case.md` contiene la tabla de supuestos (rango, fuente, estado), el modelo con código y semilla, el valor presente como p5–mediana–p95 y probabilidad de valor positivo, la oscilación por supuesto, la compuerta con su umbral y su costo, el validador con las dieciséis mutaciones, la decisión (opción, responsable, fecha, revisión) y los límites. El contrato es que ningún resultado se informa sin la tabla de supuestos que lo produjo y que la decisión no se aprueba si el validador falla.

Según [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md):

Puede redactarlo y construir el modelo, pero no conoce los supuestos ni quién responde por ellos. Pídele rangos con fuente y estado, el valor presente como intervalo, la oscilación por supuesto, la regla de abandono con su costo y el validador con mutaciones, y revisa cada afirmación contra su evidencia.

## Ejemplo

Ejemplo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) (sección «Ejemplo profesional»):

En la plataforma, `viability-case.md` contiene la tabla de supuestos (rango, fuente, estado), el modelo con código y semilla, el valor presente como p5–mediana–p95 y probabilidad de valor positivo, la oscilación por supuesto, la compuerta con su umbral y su costo, el validador con las dieciséis mutaciones, la decisión (opción, responsable, fecha, revisión) y los límites. El contrato es que ningún resultado se informa sin la tabla de supuestos que lo produjo y que la decisión no se aprueba si el validador falla.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El equipo mide el costo de construcción y no el tamaño de los centros** — causa: no se calculó la oscilación por supuesto. Corrección: ordenar los supuestos por oscilación y medir el primero. ([SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Pídele rangos con fuente y estado, el valor presente como intervalo, la oscilación por supuesto, la regla de abandono con su costo y el validador con mutaciones, y revisa cada afirmación contra su evidencia. ([SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Percentil](../p/percentil.md), [Resultado](../r/resultado.md), [Supuestos](../s/supuestos.md), [Valor](../v/valor.md), [Caso de viabilidad](../c/caso-de-viabilidad.md), [Compuerta de abandono](../c/compuerta-de-abandono.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones, descuento, sensibilidad y sesgo de optimismo; autoridad: HM Treasury (Reino Unido).
- [GOV.UK Service Manual: How the beta phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — fases con puntos de decisión y evidencia; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) — probar incertidumbres antes de construir; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — indicadores con cálculo, fuente y uso; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software, riesgo e incertidumbre; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Orquestador de caos](./orquestador-de-caos.md) · [Outbox transaccional →](./outbox-transaccional.md)
