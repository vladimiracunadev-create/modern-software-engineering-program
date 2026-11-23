# Convergencia

[↑ Glosario](../../README.md) · [← Convención de mensajes](./convencion-de-mensajes.md) · [Copia consistente →](./copia-consistente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Estado en que un verificador independiente no encuentra ningún criterio de la especificación sin cumplir.

Definición de trabajo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

## Por qué importa

En [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), el tema «Declaración propia frente a verificación» importa porque un verificador parcial produce convergencias falsas.

## Cómo funciona

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Un bucle sin condición de parada se detiene cuando se acaba el dinero o la paciencia. Las condiciones explícitas más útiles son cinco. **Convergencia**: el verificador no encuentra nada y se acaba bien. **Máximo de pasadas**: tras N pasadas se detiene aunque haya criterios abiertos; es la condición que la guía de Anthropic cita como habitual para mantener el control. **Sin progreso**: el número de criterios abiertos no baja en dos pasadas seguidas. **Presupuesto**: un tope de tokens, tiempo o dinero. **Regresión**: una pasada reabre criterios que estaban cumplidos, lo que indica que el agente está deshaciendo su propio trabajo. En todos los casos distintos de la convergencia, la acción es la misma: detener, guardar el estado y llamar a una persona con la lista de lo abierto.

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Traslada el análisis a otro dominio (por ejemplo, un agente que migra los textos de una intranet a otro formato): cambia los criterios y las variantes defectuosas y conserva el procedimiento de definir la convergencia con un verificador independiente, fijar condiciones de parada con su acción y medir la capacidad de detección con variantes. La transferencia está lograda cuando puedes decir qué criterios de ese dominio no detectarían una variante defectuosa concreta, no cuando la tabla se parece a la de *Avisos*.

## Ejemplo

Ejemplo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) (sección «Caso conductor»):

El servicio *Avisos* es el caso conductor de la [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md). Esta clase deja el tercer artefacto: los criterios ejecutables, las condiciones de parada y la medida de su capacidad de detección. `SE-568` repetirá el recorrido en proyectos con código previo, en arreglos de errores y en la evaluación de ideas, y `SE-569` fijará con qué permisos trabaja el agente mientras converge. Cambia después un solo dato, la tasa de regresión, y observa a partir de qué valor tu condición de máximo de pasadas se activa más a menudo que la de convergencia.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)) son:

- **El agente dice haber terminado y la revisión encuentra incumplimientos** — causa: verificador del propio agente o con cobertura parcial. Corrección: criterios ejecutables previos y publicar la cobertura.
- **El bucle no acaba nunca** — causa: no hay condiciones de parada. Corrección: máximo de pasadas, sin progreso, presupuesto y regresión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Convergencia**: el verificador no encuentra nada y se acaba bien. ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Verificador independiente](../v/verificador-independiente.md), [Especificación](../e/especificacion.md), [Estado](../e/estado.md), [Verificador](../v/verificador.md), [Cobertura del verificador](./cobertura-del-verificador.md), [Condición de parada](./condicion-de-parada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Convención de mensajes](./convencion-de-mensajes.md) · [Copia consistente →](./copia-consistente.md)
