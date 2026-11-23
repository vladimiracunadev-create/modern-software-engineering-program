# Valor de Shapley

[↑ Glosario](../../README.md) · [← Valor de referencia](./valor-de-referencia.md) · [Valor de vida y costo de adquisición →](./valor-de-vida-y-costo-de-adquisicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Promedio de la contribución marginal de cada participante sobre todos los órdenes de llegada.

Definición de trabajo de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md).

## Por qué importa

La clase donde se define, [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), existe con este propósito: la clase existe para que el gasto de infraestructura y operación se exprese como costo por resultado útil, se reparta con una regla que se pueda explicar y se comprometa con capacidad solo cuando la demanda lo justifica.

## Cómo funciona

Según [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md):

Cuando varios centros comparten capacidad, el costo se reparte con una regla: por partes iguales, proporcional al uso, o por contribución marginal (valor de Shapley, que promedia lo que cada uno añade en todos los órdenes de llegada). Cada regla incentiva algo distinto: el reparto igual desincentiva el ahorro, el proporcional ignora la economía de compartir, y la de Shapley es más difícil de explicar y de calcular. Una regla razonable no cobra a nadie más de lo que pagaría solo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md):

En la plataforma, `unit-cost.md` registra cada rubro de gasto con su tipo (fijo o variable), su atribución (producto, equipo o centro), la regla de reparto de lo compartido y el resultado al que se divide. El contrato es que todo gasto sin atribución figura en una lista con responsable y fecha, y que ninguna regla de reparto se adopta sin comprobar que ningún centro paga más que su costo solo. Esa estructura permite que un centro que reclama pueda ver cómo se calculó su cuota.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)) son:

- **El costo por resultado sube sin que cambie la infraestructura** — causa: subieron las fallas y los reintentos. Corrección: medir la tasa de aceptación junto con el costo.
- **La meta de costo unitario no se cumple con más volumen** — causa: el costo es mayormente variable. Corrección: separar fijo y variable antes de fijar la meta.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cuando varios centros comparten capacidad, el costo se reparte con una regla: por partes iguales, proporcional al uso, o por contribución marginal (valor de Shapley, que promedia lo que cada uno añade en todos los órdenes de llegada). ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Compromiso de capacidad](../c/compromiso-de-capacidad.md), [Costo fijo y variable](../c/costo-fijo-y-variable.md), [Costo por resultado](../c/costo-por-resultado.md), [Reparto de costo compartido](../r/reparto-de-costo-compartido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `itertools.permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations) — órdenes de llegada del valor de Shapley.
- [GOV.UK Service Manual: Measuring cost per transaction](https://www.gov.uk/service-manual/measuring-success/measuring-cost-per-transaction) — cálculo del costo por transacción completada; autoridad: Government Digital Service (Reino Unido).
- [FinOps Foundation: What is FinOps](https://www.finops.org/introduction/what-is-finops/) — práctica de gestión financiera de la nube con responsabilidad compartida; autoridad: FinOps Foundation (Linux Foundation).
- [FinOps Foundation: Allocation](https://www.finops.org/framework/capabilities/allocation/) — atribución de costos a quien los genera; autoridad: FinOps Foundation.
- [AWS Well-Architected: Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) — medición, atribución y ajuste de capacidad a la demanda; autoridad: Amazon Web Services (documentación de un proveedor).

---

[↑ Glosario](../../README.md) · [← Valor de referencia](./valor-de-referencia.md) · [Valor de vida y costo de adquisición →](./valor-de-vida-y-costo-de-adquisicion.md)
