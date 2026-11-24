# Compromiso de capacidad

[↑ Glosario](../../README.md) · [← Compromiso](./compromiso.md) · [Compromiso probabilístico →](./compromiso-probabilistico.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Un **compromiso de capacidad** es un acuerdo de pagar por una cantidad de capacidad durante un periodo, se use o no ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)). [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) lo formula como el acuerdo de pagar una cantidad de capacidad por un plazo a cambio de un precio unitario menor. En la nube corresponde a las instancias o planes reservados y a los compromisos de gasto.

## Por qué importa

Cambia el costo de la parte estable de la demanda y expone a un riesgo si la demanda cae. Comprometer ahorra si la demanda se mantiene por encima de lo comprometido; cuesta si baja, porque se paga igual. Es una decisión de costos con incertidumbre, no una oferta que convenga aceptar por defecto.

## Cómo funciona

El proveedor cobra menos por unidad a cambio de certeza: sabe que cierta cantidad se pagará. [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) lo describe como **una opción vendida al proveedor**: el cliente cede flexibilidad y obtiene un precio menor. Ahorra si la demanda se mantiene por encima de lo comprometido y cuesta si cae.

El nivel que conviene comprometer está **cerca de la demanda esperada**; [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) afina: cerca de la **mediana** de la demanda, no del promedio ni del máximo, y precisa la lógica de asimetría: comprometer de más cuesta más que no comprometer, porque lo comprometido se paga siempre, mientras que lo que queda bajo demanda solo se paga si se usa. Se compromete la parte de la demanda que casi siempre está presente (la base) y el resto se deja bajo demanda. FinOps incluye esta optimización de tarifas como una de sus prácticas.

El riesgo se mide, no se intuye: con el **percentil alto del costo** y con **escenarios de caída persistente** de la demanda. Si el compromiso es por tres años y la demanda cae a la mitad en el segundo, el ahorro unitario puede ser menor que el costo de la capacidad ociosa.

Se complementa con el costo por resultado y la atribución del gasto: un compromiso compartido entre equipos exige una regla de reparto, y cada centro no debe pagar más que su costo solo.

## Ejemplo

Con cifras ilustrativas: la demanda diaria de cómputo fluctúa entre 40 y 100 unidades con mediana 60. El proveedor ofrece 30 % de descuento por comprometer. Comprometer 60 (la mediana) cubre la base casi siempre y el resto se paga bajo demanda; comprometer 100 (el máximo) paga 40 unidades ociosas la mayor parte del tiempo y puede costar más que no comprometer. Si la demanda cae a 45 de forma persistente, incluso el compromiso de 60 deja capacidad ociosa. (Valores de ejemplo para mostrar la lógica de [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) y [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md).)

## Errores y confusiones comunes

- **Comprometer el máximo** o el promedio en vez de la base estable.
- **No simular una caída persistente**: el ahorro se convierte en pérdida.
- **Olvidar que se paga se use o no.**
- **Confundirlo con un descuento por volumen**: aquí hay plazo y obligación de pago.

## Límites y cuándo no aplica

Con demanda muy variable o incierta, no hay base estable que comprometer. Si la arquitectura puede cambiar de proveedor o de tipo de recurso, el compromiso limita esa libertad. Para proyectos de vida corta el plazo del compromiso puede superar la vida del proyecto.

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
