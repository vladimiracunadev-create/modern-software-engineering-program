# Presupuesto

[↑ Glosario](../../README.md) · [← Prerelease y metadata](./prerelease-y-metadata.md) · [Presupuesto de complejidad →](./presupuesto-de-complejidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Límite de costo (fichas, tiempo, dinero) del bucle.

Definición de trabajo de [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md): Conjunto de topes de costo, tiempo y capacidades con una acción al excederlos.

## Por qué importa

En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), el tema «Presupuestos» importa porque un número comprobable en cada cambio evita que el rendimiento se degrade sin que nadie lo decida.

En [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md), el tema «Presupuesto» importa porque acota el costo real, no el número de vueltas.

En [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), el tema «Presupuestos» importa porque hacen visible el desvío a tiempo.

## Cómo funciona

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), en la sección «Presupuestos»:

Un presupuesto de rendimiento es un límite explícito (kilobytes de JavaScript, número de peticiones, LCP en el percentil 75) que se comprueba en cada cambio. Su valor está en que convierte una decisión implícita («añadamos esta biblioteca») en una visible («cuesta 40 KB de los 200 que tenemos»). Debe derivarse de un objetivo (un tiempo en un dispositivo y red de referencia) y revisarse; un presupuesto que nadie hace cumplir es una intención.

## Ejemplo

Ejemplo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (sección «Ejemplo profesional»):

El equipo fija presupuestos para la página de entrega: 170 KB de JavaScript comprimido en la ruta de entrada, 15 peticiones y LCP de 2,5 s en el percentil 75 de visitas reales desde un móvil de gama media. Cada cambio pasa un comprobador que falla si el paquete lo supera. El análisis de la cascada muestra que la cadena HTML → script → datos decide el tiempo, así que se envían los datos iniciales en el primer HTML y se pre-carga la fuente; el CSS en línea se descarta por no mover la ruta crítica. Los datos de campo se leen con al menos 300 visitas por segmento.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El peso de la página sube sin que nadie lo decida** — causa: sin presupuesto comprobable. Corrección: fijar límites y hacer que el cambio falle al superarlos. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un presupuesto de rendimiento es un límite explícito (kilobytes de JavaScript, número de peticiones, LCP en el percentil 75) que se comprueba en cada cambio. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Conjunto](../c/conjunto.md), [Costo](../c/costo.md), [Límite](../l/limite.md), [Atribución de costos](../a/atribucion-de-costos.md), [Byte](../b/byte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-370 — Costos y operación de plataformas de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-581 — Loops de agentes y criterios de parada](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.
- [SE-598 — Costo, latencia y seguridad en sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (146 clases más lo mencionan; las que más):

[SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-513](../../../classes/part-42-ingenieria-del-caos/se-513-seguridad-y-gobernanza-de-los-experimentos-abortar-autorizar-y-registrar/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-293](../../../classes/part-24-software-especializado-y-dominios/se-293-graficos-audio-xr-y-experiencias-inmersivas/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md).

**Aparece en los casos de estudio:** [Stripe](../../../casos/exito/stripe.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Presupuestos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: Performance budgets 101](https://web.dev/articles/performance-budgets-101) — qué son los presupuestos y cómo comprobarlos; autoridad: Google web.dev.
- [web.dev: umbrales de Core Web Vitals](https://web.dev/articles/defining-core-web-vitals-thresholds) — umbrales y percentil 75; autoridad: Google web.dev.
- [web.dev: precargar recursos críticos](https://web.dev/articles/preload-critical-assets) — pistas de precarga; autoridad: Google web.dev.
- [MDN: ruta crítica de renderizado](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) — pasos hasta la primera pintura; autoridad: MDN.
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — multiplexación de peticiones; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Prerelease y metadata](./prerelease-y-metadata.md) · [Presupuesto de complejidad →](./presupuesto-de-complejidad.md)
