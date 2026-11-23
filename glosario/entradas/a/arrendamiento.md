# Arrendamiento

[↑ Glosario](../../README.md) · [← Arreglo del síntoma](./arreglo-del-sintoma.md) · [Arrepentimiento →](./arrepentimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Derecho temporal y exclusivo de escribir, con caducidad para que un titular caído no bloquee a los demás.

Definición de trabajo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Por qué importa

La clase donde se define, [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), existe con este propósito: la clase existe para que delegues trabajo a otros agentes por una razón que puedas medir y con un contrato que puedas comprobar.

## Cómo funciona

Según [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md):

Cuando varios agentes comparten un estado (una lista de tareas, un tablero, un archivo de notas), el protocolo con que escriben decide qué se pierde. La **escritura ciega** lee, modifica y guarda: si dos leen el mismo estado, el último en guardar borra la contribución del anterior. La **versión optimista** añade un número de versión y solo guarda si no cambió desde que leyó; si falló, relee y reintenta. No pierde nada y paga con reintentos. El **arrendamiento** da el derecho de escribir a uno a la vez, con caducidad para que un titular que se cae no bloquee a los demás; no pierde nada y paga con espera.

Según [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md):

El que corresponda a la operación: versión optimista cuando repetir es barato y las colisiones raras, arrendamiento cuando la operación no se puede repetir o las colisiones son frecuentes, y propiedad cuando puedas evitar el estado compartido. La escritura ciega solo es aceptable cuando perder una contribución no importa.

## Ejemplo

Ejemplo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) (sección «Preguntas frecuentes»):

El que corresponda a la operación: versión optimista cuando repetir es barato y las colisiones raras, arrendamiento cuando la operación no se puede repetir o las colisiones son frecuentes, y propiedad cuando puedas evitar el estado compartido. La escritura ciega solo es aceptable cuando perder una contribución no importa.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un agente espera indefinidamente a otro caído** — causa: arrendamiento sin caducidad. Corrección: caducidad y reintento por otro titular. ([SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **arrendamiento** da el derecho de escribir a uno a la vez, con caducidad para que un titular que se cae no bloquee a los demás; no pierde nada y paga con espera. ([SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Caducidad](../c/caducidad.md), [Derecho](../d/derecho.md), [Contrato de delegación](../c/contrato-de-delegacion.md), [Propiedad por carpeta](../p/propiedad-por-carpeta.md), [Resumen con pérdida](../r/resumen-con-perdida.md), [Subagente](../s/subagente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — agente principal, subagentes con contexto propio y costos en tokens; autoridad: Anthropic, artículo de ingeniería.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — contexto, herramientas y permisos independientes por subagente; autoridad: documentación de Anthropic.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — patrones de flujos y agentes y recomendación de simplicidad; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — operaciones largas con compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Arreglo del síntoma](./arreglo-del-sintoma.md) · [Arrepentimiento →](./arrepentimiento.md)
