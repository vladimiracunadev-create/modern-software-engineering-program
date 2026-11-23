# Costo por resultado

[↑ Glosario](../../README.md) · [← Costo fijo y variable](./costo-fijo-y-variable.md) · [Costo por solución aceptada →](./costo-por-solucion-aceptada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Costo total de operar el servicio dividido por los resultados útiles logrados.

Definición de trabajo de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md).

## Por qué importa

En [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), el tema «Costo por resultado» importa porque une el gasto con el valor entregado; el costo por solicitud mezcla fallas y reintentos.

## Cómo funciona

Según [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), en la sección «Costo por resultado»:

El costo por resultado útil es el costo total de operar el servicio dividido por los resultados logrados (entregas aceptadas), no por las solicitudes. La diferencia importa cuando hay fallas y reintentos: cada intento cuesta y solo uno produce resultado. Medirlo por resultado hace visible el costo de la falla, lo que enlaza con la tasa de aceptación de `SE-139`.

## Ejemplo

Ejemplo de [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) (sección «Caso conductor»):

La plataforma de entregas continúa como caso. Esta clase deja el costo por resultado, el reparto del costo compartido y una evaluación de compromiso. `SE-141` usará esos costos para comparar iniciativas y `SE-144` los integrará en el caso de viabilidad. Cambia después una sola regla de reparto y revisa qué centro cambia de cuota.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El costo por resultado sube sin que cambie la infraestructura** — causa: subieron las fallas y los reintentos. Corrección: medir la tasa de aceptación junto con el costo. ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo por resultado útil es el costo total de operar el servicio dividido por los resultados logrados (entregas aceptadas), no por las solicitudes. ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](./costo.md), [Resultado](../r/resultado.md), [Servicio](../s/servicio.md), [Compromiso de capacidad](./compromiso-de-capacidad.md), [Costo fijo y variable](./costo-fijo-y-variable.md), [Reparto de costo compartido](../r/reparto-de-costo-compartido.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-140 — FinOps de producto y costo por resultado](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-415](../../../classes/part-34-saas-y-plataformas-de-producto/se-415-precios-empaquetado-y-limites-por-plan/README.md).

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

[↑ Glosario](../../README.md) · [← Costo fijo y variable](./costo-fijo-y-variable.md) · [Costo por solución aceptada →](./costo-por-solucion-aceptada.md)
