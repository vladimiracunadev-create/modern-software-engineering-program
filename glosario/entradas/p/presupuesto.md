# Presupuesto

[↑ Glosario](../../README.md) · [← Prerelease y metadata](./prerelease-y-metadata.md) · [Presupuesto de complejidad →](./presupuesto-de-complejidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

«Presupuesto» es una palabra con varios sentidos técnicos en el programa, unidos por la idea de un **límite que se mide y tiene una acción al excederse**. El sentido principal de esta entrada es el de los agentes con modelos de lenguaje: el límite de costo (fichas, tiempo, dinero) del bucle, que [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md) amplía a un conjunto de topes de costo, tiempo y capacidades con una acción al excederlos. Los otros sentidos tienen entrada propia: el de rendimiento web ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), ver *presupuesto de rendimiento*), el de recursos de un dispositivo ([SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md)) y el de costos de plataformas de datos ([SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md)).

## Por qué importa

Un agente que decide por sí mismo cuántos pasos dar puede no parar. [SE-581](../../../classes/part-48-harness-y-agentic-engineering/se-581-loops-de-agentes-y-criterios-de-parada/README.md) (loops de agentes y criterios de parada) lo plantea así: el presupuesto acota el costo *real*, no el número de vueltas. Dos vueltas pueden costar cien veces más una que otra. En [SE-370](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-370-costos-y-operacion-de-plataformas-de-datos/README.md), los presupuestos hacen visible el desvío de costos de datos a tiempo; en [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), un número comprobable en cada cambio evita que el rendimiento se degrade sin que nadie lo decida.

## Cómo funciona

Un presupuesto de agente fija topes sobre magnitudes concretas:

- **Costo:** fichas (*tokens*) o dinero por tarea.
- **Tiempo:** duración total o por paso.
- **Capacidades:** cuántas herramientas o llamadas externas puede usar.

Y una **acción al excederlos**: parar, pedir confirmación humana o degradar a un modo más barato. El tope se calibra con datos: en [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), por ejemplo, el máximo de pasos se calibra con la cola de la distribución de las tareas buenas, no con la media.

Un presupuesto se combina con otros criterios de parada (repeticiones del mismo estado, pasos sin avance), porque un tope de costo solo detiene tarde.

## Ejemplo

Ilustración propia con el patrón de [SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md): un agente de envíos tiene presupuesto de 80 pasos, 200 000 fichas y 5 minutos por tarea. Al exceder cualquiera de los tres, para y deja un punto de control con el estado, en vez de seguir gastando. En [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), el equivalente web es un tope de 170 KB de JavaScript que hace fallar la integración.

## Errores y confusiones comunes

- **Limitar el número de vueltas** y no el costo.
- **Un presupuesto sin acción definida al excederse.**
- **Calibrarlo con la media** y cortar tareas legítimas largas.
- **Mezclar los sentidos:** el presupuesto de agente no es el de error de un SLO (`presupuesto de error`).

## Límites y cuándo no aplica

Un tope no sustituye vigilar *qué* hace el agente: puede causar daño con poco costo. Las cifras del ejemplo son ilustrativas. Un presupuesto demasiado ajustado interrumpe tareas válidas y uno demasiado holgado no protege.

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
