# Compuerta de abandono

[↑ Glosario](../../README.md) · [← Compuerta](./compuerta.md) · [Compuerta de presupuesto →](./compuerta-de-presupuesto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Regla que detiene el proyecto en una fecha si una métrica no alcanza un umbral, con responsable.

Definición de trabajo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Por qué importa

La clase donde se define, [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), existe con este propósito: el proyecto existe para reunir modelo de negocio, costos, métricas, riesgos y reversibilidad en un caso de viabilidad que otra persona puede recalcular, cuestionar y decidir sin pedir contexto: un valor presente con rango, un supuesto dominante, una regla de abandono y una decisión con responsable y fecha.

## Cómo funciona

[SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md):

En la plataforma, `viability-case.md` contiene la tabla de supuestos (rango, fuente, estado), el modelo con código y semilla, el valor presente como p5–mediana–p95 y probabilidad de valor positivo, la oscilación por supuesto, la compuerta con su umbral y su costo, el validador con las dieciséis mutaciones, la decisión (opción, responsable, fecha, revisión) y los límites. El contrato es que ningún resultado se informa sin la tabla de supuestos que lo produjo y que la decisión no se aprueba si el validador falla.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son:

- **El caso se aprueba con un valor presente de 34 mil y falla** — causa: se informó solo el punto. Corrección: informar el intervalo y la probabilidad de valor positivo.
- **El equipo mide el costo de construcción y no el tamaño de los centros** — causa: no se calculó la oscilación por supuesto. Corrección: ordenar los supuestos por oscilación y medir el primero.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna plataforma, mercado ni empresa real; los rangos, la forma del modelo, la independencia entre supuestos, el ruido de la señal del mes 6 y las dieciséis mutaciones son supuestos o elecciones del autor, de modo que la exactitud real del validador es desconocida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Métrica](../m/metrica.md), [Regla](../r/regla.md), [Caso de viabilidad](./caso-de-viabilidad.md), [Decisión revisable](../d/decision-revisable.md), [Mutación](../m/mutacion.md), [Oscilación por supuesto](../o/oscilacion-por-supuesto.md).
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

[↑ Glosario](../../README.md) · [← Compuerta](./compuerta.md) · [Compuerta de presupuesto →](./compuerta-de-presupuesto.md)
