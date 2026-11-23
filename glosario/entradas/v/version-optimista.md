# Versión optimista

[↑ Glosario](../../README.md) · [← Versión mínima soportada](./version-minima-soportada.md) · [Versionado →](./versionado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Protocolo de escritura que solo guarda si el estado no cambió desde la lectura y reintenta en caso contrario.

Definición de trabajo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Por qué importa

La clase donde se define, [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), existe con este propósito: la clase existe para que delegues trabajo a otros agentes por una razón que puedas medir y con un contrato que puedas comprobar.

## Cómo funciona

Según [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md):

Cuando varios agentes comparten un estado (una lista de tareas, un tablero, un archivo de notas), el protocolo con que escriben decide qué se pierde. La **escritura ciega** lee, modifica y guarda: si dos leen el mismo estado, el último en guardar borra la contribución del anterior. La **versión optimista** añade un número de versión y solo guarda si no cambió desde que leyó; si falló, relee y reintenta. No pierde nada y paga con reintentos. El **arrendamiento** da el derecho de escribir a uno a la vez, con caducidad para que un titular que se cae no bloquee a los demás; no pierde nada y paga con espera.

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

- La **versión optimista** añade un número de versión y solo guarda si no cambió desde que leyó; si falló, relee y reintenta. ([SE-572](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Guarda](../g/guarda.md), [Arrendamiento](../a/arrendamiento.md), [Contrato de delegación](../c/contrato-de-delegacion.md), [Propiedad por carpeta](../p/propiedad-por-carpeta.md), [Resumen con pérdida](../r/resumen-con-perdida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — agente principal, subagentes con contexto propio y costos en tokens; autoridad: Anthropic, artículo de ingeniería.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — contexto, herramientas y permisos independientes por subagente; autoridad: documentación de Anthropic.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — patrones de flujos y agentes y recomendación de simplicidad; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — operaciones largas con compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Versión mínima soportada](./version-minima-soportada.md) · [Versionado →](./versionado.md)
