# Compromiso de capacidad

[↑ Glosario](../../README.md) · [← Compromiso](./compromiso.md) · [Compromiso probabilístico →](./compromiso-probabilistico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Acuerdo de pagar por una cantidad de capacidad durante un periodo, se use o no.

Definición de trabajo de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md): Acuerdo de pagar una cantidad de capacidad por un plazo a cambio de un precio unitario menor.

## Por qué importa

En [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), el tema «Compromiso de capacidad» importa porque comprometer ahorra con demanda estable y cuesta con demanda que cae.

En [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), el tema «Compromiso de capacidad» importa porque una base reservada abarata lo constante.

## Cómo funciona

Según [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), en la sección «Compromiso de capacidad»:

Comprometer una cantidad de capacidad por un periodo da un precio unitario menor y se paga haya o no uso. Es una opción vendida al proveedor: ahorra si la demanda se mantiene por encima de lo comprometido y cuesta si cae. El nivel óptimo está cerca de la demanda esperada, y el riesgo se mide con el percentil alto del costo y con escenarios de caída persistente.

Según [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), en la sección «Compromiso de capacidad»:

Los proveedores ofrecen un precio menor por unidad si te comprometes a pagar una cantidad durante un plazo. Pagas lo comprometido lo uses o no, así que conviene comprometer la parte de la demanda que casi siempre está presente y dejar el resto bajo demanda. El nivel óptimo está cerca de la mediana de la demanda, no del promedio ni del máximo: comprometer de más cuesta más que no comprometer. FinOps incluye esta optimización de tarifas como práctica, y la acompaña de una advertencia: el patrón debe repetirse durante todo el plazo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md):

En la plataforma, `unit-cost.md` registra cada rubro de gasto con su tipo (fijo o variable), su atribución (producto, equipo o centro), la regla de reparto de lo compartido y el resultado al que se divide. El contrato es que todo gasto sin atribución figura en una lista con responsable y fecha, y que ninguna regla de reparto se adopta sin comprobar que ningún centro paga más que su costo solo. Esa estructura permite que un centro que reclama pueda ver cómo se calculó su cuota.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El compromiso de capacidad cuesta más que no comprometer** — causa: la demanda cayó por debajo de lo comprometido. Corrección: comprometer por debajo del mínimo esperado y revisar cada trimestre. ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ninguna factura ni precio real; la estructura de costos, la tasa de reintentos y la trayectoria de demanda son supuestos del autor en unidades ficticias. La siguiente clase pasa de cuánto cuesta cada iniciativa a cómo elegir un conjunto de ellas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](./capacidad.md), [Plazo](../p/plazo.md), [Costo fijo y variable](./costo-fijo-y-variable.md), [Costo por resultado](./costo-por-resultado.md), [Escalado programado](../e/escalado-programado.md), [Escalado reactivo](../e/escalado-reactivo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

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

[↑ Glosario](../../README.md) · [← Compromiso](./compromiso.md) · [Compromiso probabilístico →](./compromiso-probabilistico.md)
