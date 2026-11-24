# Costo por resultado

[↑ Glosario](../../README.md) · [← Costo fijo y variable](./costo-fijo-y-variable.md) · [Costo por solución aceptada →](./costo-por-solucion-aceptada.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

El **costo por resultado útil** es el costo total de operar el servicio dividido por los resultados útiles logrados, por ejemplo entregas aceptadas, y no por las solicitudes recibidas. Es el sentido de [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) (FinOps de producto). Une el gasto con el valor entregado en una sola razón.

## Por qué importa

Cambia qué se optimiza. El costo por solicitud mezcla fallas y reintentos: una solicitud fallida cuesta y no produce nada. Medir por resultado hace visible el costo de la falla y evita celebrar un costo por solicitud bajo que esconde una baja tasa de aceptación. Es el puente entre la infraestructura y la decisión de producto.

## Cómo funciona

El numerador es el costo total de operar el servicio en un periodo (infraestructura, soporte, el reparto del costo compartido). El denominador es el número de resultados que cumplen el criterio de «útil», definido antes de medir. La diferencia con el costo por solicitud importa cuando hay reintentos: cada intento cuesta y solo uno produce resultado, de modo que una tasa de fallas mayor eleva el costo por resultado aunque la infraestructura no cambie.

Esto enlaza con la tasa de aceptación de [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md): si la aceptación baja, el denominador baja y el costo por resultado sube. [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) pide medir ambas juntas. El reparto del costo compartido entre centros es una regla explícita, y cambiar una sola regla de reparto modifica la cuota de cada centro, por lo que debe quedar escrita. [SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) usa estos costos para comparar iniciativas y [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) los integra en el caso de viabilidad.

## Ejemplo

En la plataforma de entregas, un mes con el mismo gasto de infraestructura pasa de 1000 a 1250 solicitudes porque el cliente reintenta más tras un cambio de red, mientras las entregas aceptadas siguen siendo 800. El costo por solicitud baja; el costo por resultado no mejora, y la causa aparece al mirar la tasa de aceptación junto al costo. (Cifras ilustrativas, para mostrar el mecanismo.)

## Errores y confusiones comunes

- **El costo por resultado sube sin que cambie la infraestructura.** Subieron las fallas y reintentos; medir la tasa de aceptación junto con el costo ([SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md)).
- **Dividir por solicitudes.** Premia el volumen, no el valor.
- **Definir «útil» después de ver los datos.** Permite ajustar el resultado a la conclusión.
- **Repartir el costo compartido sin regla escrita.** Las cuotas se vuelven discutibles.

## Límites y cuándo no aplica

Requiere una definición estable de «resultado útil»; en productos donde el valor es difuso o tardío, el denominador es discutible. Mezcla costos fijos con variables, por lo que a bajo volumen el costo por resultado es alto por razones de escala y no de eficiencia. Y no mide calidad ni valor percibido: solo cuánto cuesta cada resultado que cumple el criterio.

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
