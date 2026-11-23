# Propiedad por carpeta

[↑ Glosario](../../README.md) · [← Propiedad del código](./propiedad-del-codigo.md) · [Propietario →](./propietario.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Asignación de cada archivo o módulo a un único agente que puede modificarlo.

Definición de trabajo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md).

## Por qué importa

La clase donde se define, [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md), existe con este propósito: la clase existe para que delegues trabajo a otros agentes por una razón que puedas medir y con un contrato que puedas comprobar.

## Cómo funciona

[SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) (sección «Caso conductor»):

El servicio *Avisos* es el caso conductor de la [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md). Esta clase deja el octavo artefacto: la descomposición con zonas, los contratos de delegación, el protocolo de escritura y el criterio de aceptación del conjunto. `SE-573` examina cuándo y cómo interviene una persona, y qué acciones se pueden deshacer. Cambia después un solo dato, el número de archivos comunes, y observa a partir de cuántos la propiedad por carpeta deja de evitar los conflictos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md)) son:

- **El sistema consume mucho más que un solo agente y no mejora** — causa: se delegó una tarea con muchas dependencias. Corrección: medir el reparto y volver a un agente si las partes no son independientes.
- **El resumen omite un detalle decisivo** — causa: contrato sin lista estructurada ni declaración de lo no hecho. Corrección: exigir hechos con evidencia y lo no comprobado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: el contexto y las colisiones son cálculos y simulaciones con semilla fija y los protocolos de escritura son código real sobre SQLite en memoria con intercalaciones deterministas. No se lanzó ningún subagente, no se invocó ningún modelo y no se observó ningún equipo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Módulo](../m/modulo.md), [Arrendamiento](../a/arrendamiento.md), [Contrato de delegación](../c/contrato-de-delegacion.md), [Resumen con pérdida](../r/resumen-con-perdida.md), [Subagente](../s/subagente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-572 — Delegación, subagentes y sistemas multiagente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-572-delegacion-subagentes-y-sistemas-multiagente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — agente principal, subagentes con contexto propio y costos en tokens; autoridad: Anthropic, artículo de ingeniería.
- [Claude Code: subagentes](https://code.claude.com/docs/en/sub-agents) — contexto, herramientas y permisos independientes por subagente; autoridad: documentación de Anthropic.
- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — patrones de flujos y agentes y recomendación de simplicidad; autoridad: Anthropic.
- [Garcia-Molina y Salem, «Sagas»](https://doi.org/10.1145/38713.38742) — operaciones largas con compensaciones; autoridad: ACM SIGMOD, 1987.

---

[↑ Glosario](../../README.md) · [← Propiedad del código](./propiedad-del-codigo.md) · [Propietario →](./propietario.md)
