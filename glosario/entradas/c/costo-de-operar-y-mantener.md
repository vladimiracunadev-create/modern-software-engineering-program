# Costo de operar y mantener

[↑ Glosario](../../README.md) · [← Costo de demora](./costo-de-demora.md) · [Costo de oportunidad →](./costo-de-oportunidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Gasto recurrente de infraestructura, soporte, actualizaciones y correcciones mientras el producto exista.

Definición de trabajo de [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md).

## Por qué importa

En [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), el tema «Costo de operar y mantener» importa porque infraestructura, soporte, actualizaciones y deuda técnica se pagan cada año mientras el producto exista.

## Cómo funciona

Según [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), en la sección «Costo de operar y mantener»:

Un sistema en uso exige cambios por seguridad, dependencias y requisitos; consume infraestructura proporcional al uso y soporte proporcional a los usuarios. En la plataforma, el mantenimiento se modela como una fracción anual de la construcción, y la infraestructura y el soporte como montos anuales. La fracción real depende de la calidad de lo construido: lo que se entrega sin pruebas ni documentación se paga después en operación.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md):

En la plataforma, `cost-model.md` contiene una fila por rubro (construcción, mantenimiento, infraestructura, soporte, otro) con mínimo, moda, máximo, quién estimó, fecha y fuente de comparación. El contrato es que el total se calcula siempre desde las filas y que ningún total se informa sin su percentil 80. Esa estructura permite que, cuando haya costos reales, se compare cada fila con su estimación y se mejore el siguiente rango.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md)) son:

- **El presupuesto alcanza para construir y no para seguir** — causa: se aprobó solo la construcción. Corrección: aprobar un costo de propiedad a cinco años con intervalo.
- **El plan «de 100 días» se retrasa casi siempre** — causa: se sumaron medianas. Corrección: prometer el percentil 80 del plan y declarar la correlación supuesta.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió el costo de ninguna plataforma real; los rangos, la lognormal, la correlación única y la tasa de descuento son supuestos del autor, y el modelo omite desmantelamiento, cambios de alcance y costo de capital propio. La siguiente clase pregunta qué distingue un resultado de una actividad.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Costo de construir](./costo-de-construir.md), [Costo de oportunidad](./costo-de-oportunidad.md), [Estimación con incertidumbre](../e/estimacion-con-incertidumbre.md), [Valor presente neto](../v/valor-presente-neto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones, descuento y corrección del sesgo de optimismo; autoridad: HM Treasury (Reino Unido).
- [AWS Well-Architected: Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) — el costo incluye la operación continua y se gestiona con prácticas de medición; autoridad: Amazon Web Services (documentación de un proveedor).
- [FinOps Foundation: What is FinOps](https://www.finops.org/introduction/what-is-finops/) — práctica de gestión del gasto en la nube con responsabilidad compartida; autoridad: FinOps Foundation (Linux Foundation).
- [GOV.UK Service Manual: Measuring cost per transaction](https://www.gov.uk/service-manual/measuring-success/measuring-cost-per-transaction) — cómo calcular el costo por transacción incluyendo costos de operación; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Costo de demora](./costo-de-demora.md) · [Costo de oportunidad →](./costo-de-oportunidad.md)
