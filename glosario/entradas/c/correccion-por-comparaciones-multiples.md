# Corrección por comparaciones múltiples

[↑ Glosario](../../README.md) · [← Corrección parcial](./correccion-parcial.md) · [Corrección total →](./correccion-total.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Ajuste del umbral para que la tasa global de alarmas falsas se mantenga en un nivel dado.

Definición de trabajo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).

## Por qué importa

La clase donde se define, [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), existe con este propósito: la clase existe para elegir una métrica que oriente al equipo sin que arrastre lo que no se mide, y para acompañarla de límites que no se cruzan y de métricas contrarias que avisan cuándo la mejora de una cifra se paga con el deterioro de otra.

## Cómo funciona

Según [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md):

Ambas formas se usan. Un valor fijo (tasa de quejas ≤ 3 %) es simple y exige una muestra suficiente para medirse; una guarda estadística (no peor que el control con cierta confianza) detecta degradaciones pequeñas y requiere corrección por comparaciones múltiples. Se escribe cuál se usa y por qué.

## Ejemplo

Ejemplo de [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) (sección «Preguntas frecuentes»):

Ambas formas se usan. Un valor fijo (tasa de quejas ≤ 3 %) es simple y exige una muestra suficiente para medirse; una guarda estadística (no peor que el control con cierta confianza) detecta degradaciones pequeñas y requiere corrección por comparaciones múltiples. Se escribe cuál se usa y por qué.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)) son:

- **La métrica norte sube y el producto empeora** — causa: no hay guardas. Corrección: definir guardas con umbral antes de optimizar.
- **El equipo ignora las alarmas de las guardas** — causa: hay demasiadas y sin corrección. Corrección: reducir las guardas y corregir las comparaciones múltiples.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un valor fijo (tasa de quejas ≤ 3 %) es simple y exige una muestra suficiente para medirse; una guarda estadística (no peor que el control con cierta confianza) detecta degradaciones pequeñas y requiere corrección por comparaciones múltiples. ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ajuste](../a/ajuste.md), [Descomposición](../d/descomposicion.md), [Guarda](../g/guarda.md), [Métrica contraria](../m/metrica-contraria.md), [Métrica norte](../m/metrica-norte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md).

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

[↑ Glosario](../../README.md) · [← Corrección parcial](./correccion-parcial.md) · [Corrección total →](./correccion-total.md)
