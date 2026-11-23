# A2A

[↑ Glosario](../../README.md) · [← A lo sumo una vez](./a-lo-sumo-una-vez.md) · [Abandonar y conservar →](./abandonar-y-conservar.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Protocolo para que agentes se descubran y colaboren mediante tareas.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

La clase donde se define, [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), existe con este propósito: la clase existe para que entiendas qué resuelven y qué no resuelven los protocolos que conectan agentes con herramientas (**MCP**, Model Context Protocol) y agentes con otros agentes (**A2A**, Agent2Agent).

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

En A2A, un agente descubre a otro mediante una **tarjeta de agente** (qué hace, cómo se le llama, cómo se autentica) y le encarga una **tarea** que atraviesa estados: recibida, en curso, a la espera de más información del cliente, completada, fallida o cancelada. Lo importante para el ingeniero es que una tarea entre agentes es **un proceso con estado**, no una llamada de función: puede durar, pedir información, fallar o cancelarse, y el cliente debe tratarla así (con tiempo máximo, reintentos y reconciliación; `SE-596`). En el experimento, de 12 000 transiciones al azar entre seis estados, el modelo acepta 2 754 por ser legales y rechaza 9 246: impone que una tarea completada no vuelve a estar en curso.

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

El equipo de plataforma publica un servidor con dos herramientas de *Avisos*: `get_deadline` (solo lectura) y `silence_course` (efecto reversible, con confirmación). Cada versión del servidor se firma y el asistente fija la versión. El cliente guarda un resumen de la lista de herramientas (nombres, esquemas y un hash de la descripción) y rechaza la sesión si cambia sin una revisión. Los resultados se limitan a 2 000 caracteres y se pasan al modelo dentro de un bloque marcado como datos externos. Para el calendario académico, el asistente delega a un agente de otra área por A2A: la tarea tiene un tiempo máximo de 30 segundos, y si el agente remoto pide más información, el asistente la traslada a una persona.

## Ejemplo

Ejemplo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) (sección «Ejemplo profesional»):

El equipo de plataforma publica un servidor con dos herramientas de *Avisos*: `get_deadline` (solo lectura) y `silence_course` (efecto reversible, con confirmación). Cada versión del servidor se firma y el asistente fija la versión. El cliente guarda un resumen de la lista de herramientas (nombres, esquemas y un hash de la descripción) y rechaza la sesión si cambia sin una revisión. Los resultados se limitan a 2 000 caracteres y se pasan al modelo dentro de un bloque marcado como datos externos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** doce descripciones escritas por el autor y una expresión regular simple; un atacante real elige sus palabras, y la máquina de estados es un subconjunto simplificado, no la especificación de A2A. ([SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](./agente.md), [Tarea](../t/tarea.md), [Error de herramienta](../e/error-de-herramienta.md), [Error de protocolo](../e/error-de-protocolo.md), [JSON-RPC 2.0](../j/json-rpc-2-0.md), [MCP](../m/mcp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← A lo sumo una vez](./a-lo-sumo-una-vez.md) · [Abandonar y conservar →](./abandonar-y-conservar.md)
