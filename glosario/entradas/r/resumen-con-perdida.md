# Resumen con pérdida

[↑ Glosario](../../README.md) · [← Resultados deseados](./resultados-deseados.md) · [Retardo antes de pedir →](./retardo-antes-de-pedir.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Compresión del trabajo de un subagente que omite parte de lo explorado.

Definición de trabajo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Por qué importa

En [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md), el tema «Resumen con pérdidas» importa porque comprime a costa de omitir cambios.

## Cómo funciona

[SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Resumen con pérdidas: lo que no se resume no existe» de [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md):

Un resumen comprime el historial en pocos tokens (aquí 150) y recupera el 74,8 % de los hechos vigentes porque se supone que conserva cada cambio con probabilidad del 75 %. Dos fallos distintos se ocultan en esa cifra. Uno es el hecho omitido: el resumen no lo mencionó y se pierde. El otro es más dañino: la **actualización omitida**, donde el resumen conserva el valor viejo y omite el nuevo, y el sistema responde con seguridad algo que fue verdad. Un resumen que se vuelve a resumir pierde más con cada compactación.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md)) son: Las conversaciones, la fracción de turnos con hechos, el acierto del extractor y la retención del resumen son parámetros del autor; no se midió ningún modelo ni ningún producto de memoria. El siguiente paso, `SE-594`, trata la lectura cuando no se conoce la clave: qué es un embedding, cómo se recupera por similitud y qué cambia cuando el agente decide cuándo y qué recuperar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Subagente](../s/subagente.md), [Trabajo](../t/trabajo.md), [Arrendamiento](../a/arrendamiento.md), [Caducidad](../c/caducidad.md), [Compactación](../c/compactacion.md), [Contexto de trabajo](../c/contexto-de-trabajo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-593 — Memoria y gestión de estado de agentes](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Resumen con pérdidas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — agente principal, subagentes con contexto propio y costos en tokens; autoridad: Anthropic, artículo de ingeniería.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — contexto, herramientas y permisos independientes por subagente; autoridad: documentación de Anthropic.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — patrones de flujos y agentes y recomendación de simplicidad; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — operaciones largas con compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Resultados deseados](./resultados-deseados.md) · [Retardo antes de pedir →](./retardo-antes-de-pedir.md)
