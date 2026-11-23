# Subagente

[↑ Glosario](../../README.md) · [← STRIDE](./stride.md) · [Subcarga →](./subcarga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Agente lanzado por otro, con su propio contexto, instrucciones, herramientas y permisos, que devuelve un resultado a quien lo invocó.

Definición de trabajo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Por qué importa

En [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), el tema «El contrato de delegación» importa porque un subagente sin objetivo, formato y límites devuelve lo que le parece.

## Cómo funciona

Según [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md):

Un subagente ofrece tres cosas. **Contexto limpio**: trabaja con su propia ventana, sin arrastrar lo que el agente principal ha leído, y devuelve un resumen en lugar de todo lo que exploró. **Paralelismo**: varios subagentes avanzan a la vez en partes independientes. **Separación de responsabilidades**: cada uno puede tener sus propias instrucciones, herramientas y permisos, de modo que el que revisa no es el que escribe. La contraparte la describe el equipo que construyó el sistema de investigación multiagente de Anthropic con cifras de su caso: los agentes usaron unas cuatro veces más tokens que una conversación y los sistemas multiagente unas quince veces más, y los dominios donde todos los agentes necesitan el mismo contexto o hay muchas dependencias entre ellos no encajan bien.

Según [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* descompone la migración en cuatro partes y revisa si el reparto es real: el cálculo de umbrales y el historial casi no se tocan entre sí, la interfaz depende del cálculo y las pruebas dependen de los tres. Decide delegar solo las dos primeras, con un agente cada una, y dejar la interfaz y las pruebas al agente principal. Cada subagente recibe un contrato de cinco partes y devuelve una lista estructurada de hechos (el valor por defecto de cada umbral, las migraciones aplicadas, los archivos tocados, lo que no pudo comprobar); el principal comprueba cada hecho contra el código.

## Ejemplo

Ejemplo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* descompone la migración en cuatro partes y revisa si el reparto es real: el cálculo de umbrales y el historial casi no se tocan entre sí, la interfaz depende del cálculo y las pruebas dependen de los tres. Decide delegar solo las dos primeras, con un agente cada una, y dejar la interfaz y las pruebas al agente principal.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md)) son:

- **El sistema consume mucho más que un solo agente y no mejora** — causa: se delegó una tarea con muchas dependencias. Corrección: medir el reparto y volver a un agente si las partes no son independientes.
- **El resumen omite un detalle decisivo** — causa: contrato sin lista estructurada ni declaración de lo no hecho. Corrección: exigir hechos con evidencia y lo no comprobado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un subagente no sabe lo que sabe el principal, de modo que lo que recibe debe bastar. ([SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Herramientas](../h/herramientas.md).
- **Ver también:** [Agente](../a/agente.md), [Contextos](../c/contextos.md), [Instrucción](../i/instruccion.md), [Permiso](../p/permiso.md), [Arrendamiento](../a/arrendamiento.md), [Contrato de delegación](../c/contrato-de-delegacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — agente principal, subagentes con contexto propio y costos en tokens; autoridad: Anthropic, artículo de ingeniería.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — contexto, herramientas y permisos independientes por subagente; autoridad: documentación de Anthropic.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — patrones de flujos y agentes y recomendación de simplicidad; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — operaciones largas con compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← STRIDE](./stride.md) · [Subcarga →](./subcarga.md)
