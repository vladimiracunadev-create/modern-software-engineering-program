# Valor presente con incertidumbre

[↑ Glosario](../../README.md) · [← Valor predictivo positivo](./valor-predictivo-positivo.md) · [Valor presente neto →](./valor-presente-neto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Distribución del valor presente neto resultante de muestrear los rangos de los supuestos.

Definición de trabajo de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md).

## Por qué importa

En [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), el tema «Valor presente con incertidumbre» importa porque un punto cercano a cero con una cola amplia es un caso muy distinto de uno ancho y positivo.

## Cómo funciona

Según [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), en la sección «Valor presente con incertidumbre»:

El valor presente a 36 meses es la suma de los márgenes mensuales descontados menos el costo de construcción. Con rangos, no es un número sino una distribución. Lo que se informa es su mediana, el intervalo del 5 al 95 por ciento y la probabilidad de que sea positivo; el punto con valores centrales es un caso entre muchos, y a menudo no el más representativo.

## Ejemplo

Caso medido en la sección «Valor presente con incertidumbre» de [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md):

El valor presente a 36 meses es la suma de los márgenes mensuales descontados menos el costo de construcción. Con rangos, no es un número sino una distribución. Lo que se informa es su mediana, el intervalo del 5 al 95 por ciento y la probabilidad de que sea positivo; el punto con valores centrales es un caso entre muchos, y a menudo no el más representativo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son:

- **El caso se aprueba con un valor presente de 34 mil y falla** — causa: se informó solo el punto. Corrección: informar el intervalo y la probabilidad de valor positivo.
- **El equipo mide el costo de construcción y no el tamaño de los centros** — causa: no se calculó la oscilación por supuesto. Corrección: ordenar los supuestos por oscilación y medir el primero.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se evaluó ninguna plataforma, mercado ni empresa real; los rangos, la forma del modelo, la independencia entre supuestos, el ruido de la señal del mes 6 y las dieciséis mutaciones son supuestos o elecciones del autor, de modo que la exactitud real del validador es desconocida.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor presente neto](./valor-presente-neto.md), [Rango](../r/rango.md), [Supuestos](../s/supuestos.md), [Valor](./valor.md), [Caso de viabilidad](../c/caso-de-viabilidad.md), [Compuerta de abandono](../c/compuerta-de-abandono.md).
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

[↑ Glosario](../../README.md) · [← Valor predictivo positivo](./valor-predictivo-positivo.md) · [Valor presente neto →](./valor-presente-neto.md)
