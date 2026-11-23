# Métrica contraria

[↑ Glosario](../../README.md) · [← Métrica](./metrica.md) · [Métrica de valor →](./metrica-de-valor.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Contraparte de una meta que mide el daño posible de perseguirla.

Definición de trabajo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).

## Por qué importa

En [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), el tema «Métricas contrarias» importa porque son la otra cara de la meta: calidad frente a volumen, queja frente a uso.

## Cómo funciona

Según [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), en la sección «Métricas contrarias»:

Una métrica contraria es la contraparte directa de una meta: si la meta premia el volumen, la contraria mide la calidad; si premia la velocidad, la contraria mide los errores. Se elige preguntando cómo se cumpliría la meta sin cumplir su propósito. Se vigila a la vez que la meta, con la misma frecuencia y visibilidad.

## Ejemplo

Ejemplo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con una guarda que se cruza por un incidente ajeno al cambio, con una que no se puede medir en la ventana del experimento, con una guarda de rendimiento que depende del dispositivo y con una métrica contraria que solo se mide en un subconjunto. La estructura es adecuada cuando esas excepciones tienen regla escrita; es peligrosa cuando la decisión de ignorar una guarda no deja huella.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)) son:

- **La métrica norte sube y el producto empeora** — causa: no hay guardas. Corrección: definir guardas con umbral antes de optimizar.
- **El equipo ignora las alarmas de las guardas** — causa: hay demasiadas y sin corrección. Corrección: reducir las guardas y corregir las comparaciones múltiples.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **optimizar la métrica norte sin una métrica contraria**. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Afirmación](../a/afirmacion.md), [Daño](../d/dano.md), [Corrección por comparaciones múltiples](../c/correccion-por-comparaciones-multiples.md), [Descomposición](../d/descomposicion.md), [Guarda](../g/guarda.md), [Métrica norte](./metrica-norte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Métricas contrarias».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — dimensiones de experiencia y su traducción a objetivos y métricas; autoridad: Google Research.
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuestos de error como límite explícito al riesgo; autoridad: Google SRE.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — cómo una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — métricas equilibradas de velocidad y estabilidad; autoridad: DORA (Google Cloud).
- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — métricas guarda y comparaciones múltiples en experimentos; autoridad: Kohavi, Tang y Xu (Cambridge University Press).

---

[↑ Glosario](../../README.md) · [← Métrica](./metrica.md) · [Métrica de valor →](./metrica-de-valor.md)
