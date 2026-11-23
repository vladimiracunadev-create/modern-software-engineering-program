# Métrica norte

[↑ Glosario](../../README.md) · [← Métrica facturable](./metrica-facturable.md) · [Métricas interpretadas →](./metricas-interpretadas.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Medida única de resultado que resume el valor entregado y orienta las decisiones del equipo.

Definición de trabajo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).

## Por qué importa

En [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), el tema «Métrica norte» importa porque orienta decisiones de todo el equipo; si no representa valor, orienta mal a todos.

## Cómo funciona

Según [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), en la sección «Métrica norte»:

Una métrica norte es la medida única que mejor resume el valor que el producto entrega y que el equipo puede mover. Debe ser un resultado y no una actividad (`SE-135`), calculable y sensible al cambio. En la plataforma, «entregas aceptadas a tiempo por estudiante activo de la semana» es un candidato; «sesiones» no lo es. Una métrica norte orienta, no gobierna: nunca debe usarse sin lo que la rodea.

## Ejemplo

Ejemplo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sección «Ejemplo profesional»):

En la plataforma, `metric-guardrails.md` define la métrica norte (numerador, denominador, ventana, filtros), las guardas (métrica, umbral, ventana, responsable, acción) y los pares meta–contraria. El contrato es que ninguna prueba arranca sin guardas y que cruzar una guarda detiene el despliegue hasta que el responsable decide. Esa estructura permite que una revisión externa verifique que el equipo no podía optimizar sin frenos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La métrica norte sube y el producto empeora** — causa: no hay guardas. Corrección: definir guardas con umbral antes de optimizar. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))
- **La métrica norte cambia de tendencia sin razón** — causa: cambió su definición. Corrección: registrar cambios de definición con fecha y recalcular. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una métrica norte orienta, no gobierna: nunca debe usarse sin lo que la rodea. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))
- **optimizar la métrica norte sin una métrica contraria**. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](./medida.md), [Resultado](../r/resultado.md), [Valor](../v/valor.md), [Corrección por comparaciones múltiples](../c/correccion-por-comparaciones-multiples.md), [Descomposición](../d/descomposicion.md), [Guarda](../g/guarda.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — dimensiones de experiencia y su traducción a objetivos y métricas; autoridad: Google Research.
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuestos de error como límite explícito al riesgo; autoridad: Google SRE.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — cómo una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — métricas equilibradas de velocidad y estabilidad; autoridad: DORA (Google Cloud).
- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — métricas guarda y comparaciones múltiples en experimentos; autoridad: Kohavi, Tang y Xu (Cambridge University Press).

---

[↑ Glosario](../../README.md) · [← Métrica facturable](./metrica-facturable.md) · [Métricas interpretadas →](./metricas-interpretadas.md)
