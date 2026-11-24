# Guarda

[↑ Glosario](../../README.md) · [← Grupo de control](./grupo-de-control.md) · [Guarda de versión →](./guarda-de-version.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Una **guarda** es, en producto ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)), un límite de una métrica que no debe empeorar al perseguir la métrica norte, con umbral, responsable y acción. El programa usa la palabra con sentidos emparentados:

- **Guarda de métrica** ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md), [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md)): métrica con umbral cuyo incumplimiento detiene o revierte un cambio o despliegue.
- **Guarda de código** ([SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)): comprobación temprana que protege el camino principal.
- **Guarda de transición** ([SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md)): condición para habilitar una transición en un modelo de estados.

## Por qué importa

Optimizar una sola métrica daña lo que no se mide: si la métrica norte sube y el producto empeora, faltan guardas ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)). Las guardas convierten «tener cuidado» en una regla ejecutable. El presupuesto de error del enfoque de fiabilidad es una guarda: fija cuánto riesgo se acepta para ir más rápido.

## Cómo funciona

Una guarda de métrica tiene tres piezas ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)): **umbral** (fijado antes de optimizar, sin él es una opinión), **responsable** (quién decide) y **acción** (detener el despliegue, revertir o convocar revisión). Ejemplos: tasa de quejas, tiempo de carga, tasa de errores, baja del servicio. En [SE-607](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md), la métrica con umbral detiene o revierte el despliegue de un modelo. Hay que cuidar la cantidad: con demasiadas, el equipo ignora las alarmas y aparecen comparaciones múltiples (falsas alarmas por azar). En código ([SE-062](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md)), una cláusula de guarda sale temprano del camino principal ante una entrada inválida, de modo que el resto de la función asume lo ya comprobado. En modelos de estados ([SE-057](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md)), una transición solo se habilita si su condición se cumple.

## Ejemplo

[SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) hace un experimento con un optimizador de recordatorios: sin guarda de bajas de notificación, el optimizador sube el envío hasta cruzar el umbral de quejas. Con guarda, el experimento se detiene. Ilustración:

```python
def desplegar(m):
    if m["bajas"] > 0.02: return revertir()    # guarda: umbral, acción y dueño documentados
    return publicar()
```

## Errores y confusiones comunes

- **La métrica norte sube y el producto empeora.** Causa: no hay guardas; corrección: definirlas con umbral antes de optimizar ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)).
- **El equipo ignora las alarmas.** Causa: hay demasiadas y sin corrección por comparaciones múltiples; corrección: reducirlas ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)).
- **Una guarda se cruza y nadie actúa.** Causa: sin responsable ni acción; corrección: escribir quién decide y qué ocurre ([SE-139](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md)).

## Límites y cuándo no aplica

Una guarda protege lo que se midió: no detecta daños no medidos. Un umbral mal elegido bloquea cambios buenos o deja pasar malos. Y los tres sentidos no son intercambiables: una guarda de métrica opera sobre agregados y con retraso; una guarda de código, sobre una entrada concreta y de inmediato.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Métrica norte](../m/metrica-norte.md), [Condición](../c/condicion.md), [Límite](../l/limite.md), [Métrica](../m/metrica.md), [Contrato](../c/contrato.md), [Control](../c/control.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-057 — Modelado de estado, transiciones y eventos](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-057-modelado-de-estado-transiciones-y-eventos/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-062 — Control de flujo y decisiones](../../../classes/part-05-fundamentos-de-programacion/se-062-control-de-flujo-y-decisiones/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-139 — North Star, guardrails y métricas contrarias](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-139-north-star-guardrails-y-metricas-contrarias/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.
- [SE-607 — Despliegue seguro de modelos: shadow, canary y rollback](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-607-despliegue-seguro-de-modelos-shadow-canary-y-rollback/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (235 clases más lo mencionan; las que más):

[SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-254](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-254-ciclo-de-vida-suspension-y-reanudacion/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-406](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-406-plataformas-internas-y-golden-paths/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Slack](../../../casos/exito/slack.md), [Discord](../../../casos/exito/discord.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Guardas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Trustworthy Online Controlled Experiments](https://experimentguide.com/) — métricas guarda y comparaciones múltiples en experimentos; autoridad: Kohavi, Tang y Xu (Cambridge University Press).
- [Measuring the User Experience on a Large Scale: HEART (Google Research)](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — dimensiones de experiencia y su traducción a objetivos y métricas; autoridad: Google Research.
- [Google SRE Book: Embracing Risk](https://sre.google/sre-book/embracing-risk/) — presupuestos de error como límite explícito al riesgo; autoridad: Google SRE.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — cómo una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv.
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — métricas equilibradas de velocidad y estabilidad; autoridad: DORA (Google Cloud).

---

[↑ Glosario](../../README.md) · [← Grupo de control](./grupo-de-control.md) · [Guarda de versión →](./guarda-de-version.md)
