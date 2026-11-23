# Costo fijo y variable

[↑ Glosario](../../README.md) · [← Costo fijo por ejecución](./costo-fijo-por-ejecucion.md) · [Costo por resultado →](./costo-por-resultado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

El primero no cambia con el uso en el rango de operación; el segundo crece con él.

Definición de trabajo de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md).

## Por qué importa

En [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), el tema «Costos fijos y variables» importa porque los fijos se diluyen con el volumen y los variables no; confundirlos produce metas imposibles.

## Cómo funciona

Según [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), en la sección «Costos fijos y variables»:

Los costos fijos (el equipo, una base de datos mínima, licencias) no cambian con el uso en el rango de operación; los variables (cómputo, almacenamiento, transferencia) crecen con él. El costo unitario baja con el volumen porque el fijo se reparte entre más resultados, hasta acercarse al variable. Una meta de reducción de costo unitario sin volumen creciente exige reducir el fijo o el variable, y son esfuerzos distintos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md):

En la plataforma, `unit-cost.md` registra cada rubro de gasto con su tipo (fijo o variable), su atribución (producto, equipo o centro), la regla de reparto de lo compartido y el resultado al que se divide. El contrato es que todo gasto sin atribución figura en una lista con responsable y fecha, y que ninguna regla de reparto se adopta sin comprobar que ningún centro paga más que su costo solo. Esa estructura permite que un centro que reclama pueda ver cómo se calculó su cuota.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)) son:

- **El costo por resultado sube sin que cambie la infraestructura** — causa: subieron las fallas y los reintentos. Corrección: medir la tasa de aceptación junto con el costo.
- **La meta de costo unitario no se cumple con más volumen** — causa: el costo es mayormente variable. Corrección: separar fijo y variable antes de fijar la meta.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna factura ni precio real; la estructura de costos, la tasa de reintentos y la trayectoria de demanda son supuestos del autor en unidades ficticias. La siguiente clase pasa de cuánto cuesta cada iniciativa a cómo elegir un conjunto de ellas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Rango](../r/rango.md), [Compromiso de capacidad](./compromiso-de-capacidad.md), [Costo por resultado](./costo-por-resultado.md), [Reparto de costo compartido](../r/reparto-de-costo-compartido.md), [Valor de Shapley](../v/valor-de-shapley.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring cost per transaction](https://www.gov.uk/service-manual/measuring-success/measuring-cost-per-transaction) — cálculo del costo por transacción completada; autoridad: Government Digital Service (Reino Unido).
- [FinOps Foundation: What is FinOps](https://www.finops.org/introduction/what-is-finops/) — práctica de gestión financiera de la nube con responsabilidad compartida; autoridad: FinOps Foundation (Linux Foundation).
- [FinOps Foundation: Allocation](https://www.finops.org/framework/capabilities/allocation/) — atribución de costos a quien los genera; autoridad: FinOps Foundation.
- [AWS Well-Architected: Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) — medición, atribución y ajuste de capacidad a la demanda; autoridad: Amazon Web Services (documentación de un proveedor).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Costo fijo por ejecución](./costo-fijo-por-ejecucion.md) · [Costo por resultado →](./costo-por-resultado.md)
