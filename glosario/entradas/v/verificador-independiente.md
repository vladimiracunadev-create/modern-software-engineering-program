# Verificador independiente

[↑ Glosario](../../README.md) · [← Verificador](./verificador.md) · [Versión →](./version.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Procedimiento que juzga la implementación sin compartir el contexto ni los supuestos de quien la escribió.

Definición de trabajo de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

## Por qué importa

La clase donde se define, [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md), existe con este propósito: la clase existe para que dejes de aceptar «terminé» como una medida.

## Cómo funciona

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Converger es que un verificador independiente, aplicado al código actual, no encuentre ningún criterio de la especificación sin cumplir. La definición tiene tres partes. **Qué se verifica**: los criterios de la especificación, no las tareas ni las pruebas del agente. **Quién verifica**: un procedimiento que no comparte el contexto del implementador —otra ejecución, un conjunto de pruebas escrito antes de implementar, una persona—. **Qué produce**: una lista de criterios cumplidos y no cumplidos con la evidencia de cada uno. En `converge`, Spec Kit evalúa el código frente a especificación, plan y tareas y devuelve «convergido» o añade las tareas que faltan en una sección propia; la salida alimenta la siguiente pasada.

Según [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Traslada el análisis a otro dominio (por ejemplo, un agente que migra los textos de una intranet a otro formato): cambia los criterios y las variantes defectuosas y conserva el procedimiento de definir la convergencia con un verificador independiente, fijar condiciones de parada con su acción y medir la capacidad de detección con variantes. La transferencia está lograda cuando puedes decir qué criterios de ese dominio no detectarían una variante defectuosa concreta, no cuando la tabla se parece a la de *Avisos*.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* convierte los diecisiete criterios de su especificación en pruebas ejecutables antes de que el agente implemente la primera tarea. Fija las condiciones de parada: máximo de seis pasadas, detener si los abiertos no bajan en dos pasadas seguidas, detener si una pasada reabre más de dos criterios y presupuesto de cómputo de tres horas. Tras la primera ejecución, el verificador encuentra siete criterios abiertos; el agente corrige cinco y rompe uno.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md)) son:

- **El agente dice haber terminado y la revisión encuentra incumplimientos** — causa: verificador del propio agente o con cobertura parcial. Corrección: criterios ejecutables previos y publicar la cobertura.
- **El bucle no acaba nunca** — causa: no hay condiciones de parada. Corrección: máximo de pasadas, sin progreso, presupuesto y regresión.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Converger es que un verificador independiente, aplicado al código actual, no encuentre ningún criterio de la especificación sin cumplir. ([SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Supuestos](../s/supuestos.md), [Cobertura del verificador](../c/cobertura-del-verificador.md), [Condición de parada](../c/condicion-de-parada.md), [Convergencia](../c/convergencia.md), [Regresión](../r/regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-567 — Implementación, análisis y convergencia contra SPEC](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md), [SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — implementar por fases y converger solo añadiendo tareas; autoridad: GitHub y mantenedores de la comunidad.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno y condiciones de parada en bucles de agente; autoridad: Anthropic, artículo de ingeniería.
- [Jia y Harman](https://doi.org/10.1109/TSE.2010.62) — prueba de mutación como medida de la detección; autoridad: IEEE Transactions on Software Engineering.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) — medir y gestionar el riesgo de sistemas de IA; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Verificador](./verificador.md) · [Versión →](./version.md)
