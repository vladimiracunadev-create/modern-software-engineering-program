# Métrica norte

[↑ Glosario](../../README.md) · [← Métrica facturable](./metrica-facturable.md) · [Métricas interpretadas →](./metricas-interpretadas.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

La **métrica norte** (*north star metric*) es la medida única de resultado que resume el valor entregado y orienta las decisiones del equipo ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)). Es la cifra que mejor representa que el producto está haciendo lo que debe, y que el equipo puede mover.

## Por qué importa

Orienta decisiones de todo el equipo; si no representa valor, orienta mal a todos. Una métrica norte bien elegida alinea esfuerzos; una mal elegida los dirige hacia algo que no importa. Cambia cómo se priorizan funciones y experimentos: se evalúan por cuánto mueven la métrica norte.

## Cómo funciona

[SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) pide tres propiedades. Debe ser un **resultado y no una actividad** ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)): cambio en lo que consiguen las personas, no movimiento dentro del producto. Debe ser **calculable**, con definición explícita (numerador, denominador, ventana y filtros). Y debe ser **sensible al cambio**: moverse cuando el equipo mejora algo, en un plazo útil para decidir.

En la plataforma de entregas, «entregas aceptadas a tiempo por estudiante activo de la semana» es un candidato: es resultado (la entrega fue aceptada y a tiempo), está definida con denominador explícito y responde a mejoras del flujo. «Sesiones» no lo es: es actividad, puede subir sin valor.

La clase insiste en la frase central: **una métrica norte orienta, no gobierna**; nunca debe usarse sin lo que la rodea. Eso son las **métricas contrarias** y las guardas: umbrales que no deben cruzarse mientras se optimiza. Sin ellas, el equipo puede mejorar la norte dañando otra cosa (la métrica norte sube y el producto empeora). El archivo de métricas conserva la definición, las guardas (métrica, umbral, ventana, responsable, acción) y los pares meta–contraria; la regla es que ninguna prueba arranca sin guardas y que cruzar una guarda detiene el despliegue hasta que el responsable decide.

Otro fallo que la clase señala: la métrica norte cambia de tendencia sin razón porque cambió su definición. Se corrige registrando los cambios de definición con fecha y recalculando la serie histórica.

## Ejemplo

Definición: numerador, entregas aceptadas antes del plazo en la semana; denominador, estudiantes con al menos una entrega aceptada o intento en la semana; ventana, semanal. Guardas: tasa de reclamos de nota por entrega no debe subir más de 10 %; tiempo de respuesta de la subida p95 no debe superar 3 s. Si un experimento sube la norte un 5 % pero los reclamos suben un 15 %, se detiene. (Definición ilustrativa en el estilo de [SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md).)

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora**: no hay guardas.
- **Cambiar la definición sin registrarlo.**
- **Elegir una actividad** (sesiones, clics) como norte.
- **Tener varias «norte»**: una sola es el punto.

## Límites y cuándo no aplica

Un producto con propósitos muy distintos (varios trabajos) difícilmente se resume en una sola cifra; ahí hacen falta varias métricas de resultado por segmento. Una norte mala es peor que ninguna, porque da orientación falsa. Y no sustituye el juicio cualitativo ni la investigación con personas.

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
