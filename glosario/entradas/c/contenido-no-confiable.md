# Contenido no confiable

[↑ Glosario](../../README.md) · [← Contenido de una especificación](./contenido-de-una-especificacion.md) · [Context engineering →](./context-engineering.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Texto que proviene de una fuente que quien opera el agente no controla.

Definición de trabajo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Por qué importa

La clase donde se define, [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), existe con este propósito: la clase existe para que dejes de pensar la seguridad de un agente como el problema de que alguien le escriba algo malicioso y la pienses como el problema de que el agente lee texto de fuentes que no controlas y puede hacer cosas con lo que lee.

## Cómo funciona

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Simon Willison propuso una regla de diseño que sirve de lista de comprobación: una configuración de agente es peligrosa cuando reúne **acceso a datos privados**, **exposición a contenido no confiable** y **capacidad de comunicación hacia fuera**. Con las tres, un texto injertado en el contenido no confiable puede hacer que el agente lea los datos privados y los envíe fuera. Con dos, el daño es menor: sin comunicación hacia fuera, los datos no salen; sin contenido no confiable, nadie inyecta; sin datos privados, no hay nada que robar. La regla no promete seguridad cuando falta una (hay otros daños posibles: acciones destructivas, manipulación del resultado) y aun así es una buena primera pregunta.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md)) son:

- **El filtro bloquea frases legítimas y deja pasar la orden** — causa: patrón amplio sin normalizar o patrón fijo. Corrección: usar el filtro como señal y no como control.
- **Una nota hace que el agente envíe un correo** — causa: las tres capacidades coinciden. Corrección: romper una o exigir aprobación en la salida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Simon Willison propuso una regla de diseño que sirve de lista de comprobación: una configuración de agente es peligrosa cuando reúne **acceso a datos privados**, **exposición a contenido no confiable** y **capacidad de comunicación hacia fuera**. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Agente en cuarentena](../a/agente-en-cuarentena.md), [Cadena de huellas](./cadena-de-huellas.md), [Inyección indirecta de instrucciones](../i/inyeccion-indirecta-de-instrucciones.md), [Referencia externa](../r/referencia-externa.md), [Registro de auditoría](../r/registro-de-auditoria.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-598](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-598-costo-latencia-y-seguridad-en-sistemas-con-llm/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-600](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-600-proyecto-sistema-con-llm-evaluado-y-operable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta en aplicaciones reales; autoridad: preimpresión en arXiv, 2023.
- [Willison, «The lethal trifecta for AI agents»](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — regla de las tres capacidades; autoridad: ensayo de un autor reconocido.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — ataques a sistemas con herramientas; autoridad: mantenedores de MCP.

---

[↑ Glosario](../../README.md) · [← Contenido de una especificación](./contenido-de-una-especificacion.md) · [Context engineering →](./context-engineering.md)
