# Punto de control

[↑ Glosario](../../README.md) · [← Punto de compromiso](./punto-de-compromiso.md) · [Punto de corte →](./punto-de-corte.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Estado mínimo guardado en almacenamiento duradero que permite reanudar una tarea sin repetirla entera.

Definición de trabajo de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md): Registro del progreso que permite reanudar sin empezar de cero.

## Por qué importa

En [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), el tema «Puntos de control» importa porque reiniciar desde cero repite lo hecho y lo cuesta de nuevo.

En [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), el tema «Puntos de control» importa porque evitan rehacer, pero crean ventanas de duplicado o pérdida.

## Cómo funciona

Según [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

Reiniciar desde el principio es caro y, además, repite los efectos. Un **punto de control** es el estado mínimo que permite continuar: en qué paso va el agente, qué ha hecho y qué le falta. Se guarda en un almacenamiento que sobrevive a la caída (una base de datos, un archivo) y se escribe en puntos conocidos. Anthropic informa de que en su sistema de investigación no pueden reiniciar desde el principio por el costo y han construido un sistema que reanuda desde donde estaba el agente, combinando el modelo con reintentos y puntos de control deterministas. Con un punto de control se recalcula como mucho el paso en curso, no todo.

Según [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. El presupuesto se fija por tarea según su clase, no global. Al detenerse, el agente guarda su estado y notifica a una persona con la última acción, el número de pasos y el motivo.

## Ejemplo

Ejemplo de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. El presupuesto se fija por tarea según su clase, no global. Al detenerse, el agente guarda su estado y notifica a una persona con la última acción, el número de pasos y el motivo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Tras reiniciar hay avisos duplicados** — causa: efecto y punto de control no atómicos. Corrección: clave de idempotencia o transacción única. ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Anthropic informa de que en su sistema de investigación no pueden reiniciar desde el principio por el costo y han construido un sistema que reanuda desde donde estaba el agente, combinando el modelo con reintentos y puntos de control deterministas. ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Progreso](./progreso.md), [Registro](../r/registro.md), [Tarea](../t/tarea.md), [Acierto en tres de tres](../a/acierto-en-tres-de-tres.md), [Clave de idempotencia](../c/clave-de-idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Puntos de control».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno, puntos de control humanos y condiciones de parada; autoridad: Anthropic.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.
- [Patrón de bandeja de salida transaccional](https://microservices.io/patterns/data/transactional-outbox.html) — efecto y registro en una transacción; autoridad: catálogo de patrones de microservicios.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de una proporción; autoridad: Journal of the American Statistical Association.
- [POSIX: `rename`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html) — sustitución atómica del destino; autoridad: The Open Group.

---

[↑ Glosario](../../README.md) · [← Punto de compromiso](./punto-de-compromiso.md) · [Punto de corte →](./punto-de-corte.md)
