# Condición de parada

[↑ Glosario](../../README.md) · [← Condición de fallo](./condicion-de-fallo.md) · [Condición de revisión →](./condicion-de-revision.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Regla explícita que detiene un bucle de agente y define qué se hace después.

Definición de trabajo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md): Regla explícita que detiene a un agente y define qué se hace después.
- En [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md): Alarma que detiene el experimento si el sistema alcanza un estado inaceptable.

## Por qué importa

En [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), el tema «Condiciones de parada» importa porque un bucle sin tope solo se detiene cuando se acaba el presupuesto.

## Cómo funciona

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), en la sección «Condiciones de parada»:

Un bucle sin condición de parada se detiene cuando se acaba el dinero o la paciencia. Las condiciones explícitas más útiles son cinco. **Convergencia**: el verificador no encuentra nada y se acaba bien. **Máximo de pasadas**: tras N pasadas se detiene aunque haya criterios abiertos; es la condición que la guía de Anthropic cita como habitual para mantener el control. **Sin progreso**: el número de criterios abiertos no baja en dos pasadas seguidas. **Presupuesto**: un tope de tokens, tiempo o dinero. **Regresión**: una pasada reabre criterios que estaban cumplidos, lo que indica que el agente está deshaciendo su propio trabajo. En todos los casos distintos de la convergencia, la acción es la misma: detener, guardar el estado y llamar a una persona con la lista de lo abierto.

## Ejemplo

Ejemplo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) (sección «Ejemplo mínimo»):

El fragmento muestra un bucle con condición de parada. Antes de ejecutarlo, predice cuántas pasadas hace.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El bucle no acaba nunca** — causa: no hay condiciones de parada. Corrección: máximo de pasadas, sin progreso, presupuesto y regresión. ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md))
- **Un agente trabaja toda la noche sin avanzar** — causa: sin condiciones de parada o solo con un máximo enorme. Corrección: añadir estado repetido y falta de avance con presupuesto por tarea. ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un bucle sin condición de parada se detiene cuando se acaba el dinero o la paciencia. ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-397](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-397-iaas-paas-saas-y-responsabilidad-compartida/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Estado](../e/estado.md), [Regla](../r/regla.md), [Cobertura del verificador](./cobertura-del-verificador.md), [Convergencia](./convergencia.md), [Orquestador de caos](../o/orquestador-de-caos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-509 — Caos en Kubernetes y en plataformas cloud](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.
- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-284](../../../classes/part-23-runtimes-y-plataformas-modernas/se-284-computacion-cuantica-para-ingenieros-de-software/README.md), [SE-506](../../../classes/part-42-ingenieria-del-caos/se-506-disenar-experimentos-de-fallo-alcance-y-radio-de-impacto/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Condiciones de parada».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.

---

[↑ Glosario](../../README.md) · [← Condición de fallo](./condicion-de-fallo.md) · [Condición de revisión →](./condicion-de-revision.md)
