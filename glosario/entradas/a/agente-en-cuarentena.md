# Agente en cuarentena

[↑ Glosario](../../README.md) · [← Agente](./agente.md) · [Agentic engineering →](./agentic-engineering.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Agente que lee contenido no confiable sin acceso a datos privados ni a herramientas de salida.

Definición de trabajo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md).

## Por qué importa

La clase donde se define, [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), existe con este propósito: la clase existe para que dejes de pensar la seguridad de un agente como el problema de que alguien le escriba algo malicioso y la pienses como el problema de que el agente lee texto de fuentes que no controlas y puede hacer cosas con lo que lee.

## Cómo funciona

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

El principio de `SE-569` se aplica aquí con más fuerza. Una tarea que lee contenido no confiable (resumir tickets de usuarios) debe hacerse con un agente sin acceso a datos privados ni a herramientas de salida: devuelve un resumen estructurado. Otro agente, con acceso a datos y herramientas pero sin leer el contenido original, usa ese resumen estructurado. Esta separación (a veces descrita como un agente en cuarentena y otro con privilegios) reduce lo que una inyección puede lograr, porque el agente que fue engañado no tiene con qué dañar y el que tiene con qué dañar no leyó el texto inyectado. Tiene un costo: el resumen es una compresión (`SE-572`) y el formato estructurado debe ser tan estrecho que no pueda transportar una orden.

Según [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden. Rompe una: el resumen de notas pasa a un agente en cuarentena, sin base de datos ni correo, que devuelve un objeto con tres campos de valores acotados (tono, urgencia, un identificador de entrega); el agente con la base y el correo solo recibe ese objeto, nunca el texto de la nota. Añade un filtro normalizado que registra cada intento sospechoso sin bloquearlo, porque sirve para detectar campañas y no como defensa.

## Ejemplo

Ejemplo de [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* modela las amenazas de su agente que resume notas. Marca las capacidades: lee notas de docentes (contenido de terceros: N), accede a la base con datos de matrícula (D) y tiene una herramienta de envío de correos (E). Las tres coinciden. Rompe una: el resumen de notas pasa a un agente en cuarentena, sin base de datos ni correo, que devuelve un objeto con tres campos de valores acotados (tono, urgencia, un identificador de entrega); el agente con la base y el correo solo recibe ese objeto, nunca el texto de la nota.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md)) son:

- **El filtro bloquea frases legítimas y deja pasar la orden** — causa: patrón amplio sin normalizar o patrón fijo. Corrección: usar el filtro como señal y no como control.
- **Una nota hace que el agente envíe un correo** — causa: las tres capacidades coinciden. Corrección: romper una o exigir aprobación en la salida.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Esta separación (a veces descrita como un agente en cuarentena y otro con privilegios) reduce lo que una inyección puede lograr, porque el agente que fue engañado no tiene con qué dañar y el que tiene con qué dañar no leyó el texto inyectado. ([SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contenido no confiable](../c/contenido-no-confiable.md), [Agente](./agente.md), [Herramientas](../h/herramientas.md), [Cadena de huellas](../c/cadena-de-huellas.md), [Inyección indirecta de instrucciones](../i/inyeccion-indirecta-de-instrucciones.md), [Referencia externa](../r/referencia-externa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-574 — Seguridad agentic, prompt injection y auditoría](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Greshake et al., «Not what you've signed up for»](https://arxiv.org/abs/2302.12173) — inyección indirecta en aplicaciones reales; autoridad: preimpresión en arXiv, 2023.
- [Willison, «The lethal trifecta for AI agents»](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — regla de las tres capacidades; autoridad: ensayo de un autor reconocido.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — ataques a sistemas con herramientas; autoridad: mantenedores de MCP.

---

[↑ Glosario](../../README.md) · [← Agente](./agente.md) · [Agentic engineering →](./agentic-engineering.md)
