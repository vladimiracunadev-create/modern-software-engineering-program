# Métrica contraria

[↑ Glosario](../../README.md) · [← Métrica](./metrica.md) · [Métrica de valor →](./metrica-de-valor.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Una **métrica contraria** es la contraparte de una meta que mide el daño posible de perseguirla ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)). Si la meta premia el volumen, la contraria mide la calidad; si premia la velocidad, mide los errores. En el vocabulario del programa se emparejan «meta–contraria» y, cuando son umbrales que no deben cruzarse durante un experimento, se llaman guardas.

## Por qué importa

Toda meta se puede cumplir sin cumplir su propósito. Una métrica contraria hace visible esa vía de escape y detiene la optimización ciega. Cambia el diseño de un panel y de un experimento: nunca se optimiza un número solo.

## Cómo funciona

[SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) da el procedimiento de elección: se pregunta **cómo se cumpliría la meta sin cumplir su propósito**, y la respuesta indica qué medir. Si la meta es aumentar las entregas procesadas por hora, se cumple a costa de procesar mal: la contraria será la tasa de reclamos o de errores. Si la meta es reducir el tiempo de respuesta del soporte, se cumple cerrando tickets sin resolver: la contraria será la reapertura.

Las contrarias se **vigilan a la vez que la meta**, con la misma frecuencia y visibilidad. De otro modo, se vuelven una nota al pie que nadie mira. En un experimento, se definen **guardas** con umbral, ventana, responsable y acción antes de arrancar: cruzar una guarda detiene el despliegue hasta que el responsable decide. Esto evita el síntoma de que la métrica norte suba y el producto empeore por falta de guardas.

Dos riesgos: demasiadas guardas producen alarmas que el equipo ignora (con comparaciones múltiples, alguna se cruzará por azar), y las excepciones (una guarda que se cruza por un incidente ajeno al cambio, una que no se puede medir en la ventana del experimento, una de rendimiento que depende del dispositivo) necesitan **regla escrita**; la decisión de ignorar una guarda no debe dejar de dejar huella.

El archivo de métricas de la plataforma define la métrica norte (numerador, denominador, ventana, filtros), las guardas (métrica, umbral, ventana, responsable, acción) y los pares meta–contraria. La regla de la clase: ninguna prueba arranca sin guardas.

## Ejemplo

Meta: «aumentar el número de entregas aceptadas por docente y semana». Contraria: «porcentaje de entregas reabiertas tras la aceptación» y «tiempo medio de revisión por entrega». Si la meta sube un 20 % y las reaperturas se duplican, el equipo detiene el despliegue y revisa: probablemente se aceptó sin revisar bien. (Ilustración del método de [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).)

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora**: no hay guardas; corrección: definirlas con umbral antes de optimizar.
- **El equipo ignora las alarmas**: hay demasiadas; corrección: reducirlas y corregir las comparaciones múltiples.
- **Contraria que se mide menos que la meta.**
- **Contraria que no es realmente contraria**: mide lo mismo.

## Límites y cuándo no aplica

Una contraria no previene todos los daños: solo el que se pensó. No sustituye el juicio sobre el propósito de la meta. Optimizar la métrica norte sin una métrica contraria es el caso que la clase señala como práctica peligrosa.

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
