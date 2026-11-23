# Error de herramienta

[↑ Glosario](../../README.md) · [← Errata](./errata.md) · [Error de protocolo →](./error-de-protocolo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Resultado válido que indica que la herramienta no pudo cumplir el pedido.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

La clase donde se define, [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), existe con este propósito: la clase existe para que entiendas qué resuelven y qué no resuelven los protocolos que conectan agentes con herramientas (**MCP**, Model Context Protocol) y agentes con otros agentes (**A2A**, Agent2Agent).

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

JSON-RPC define códigos para los fallos del protocolo: −32700 (JSON malformado), −32600 (petición inválida), −32601 (método inexistente), −32602 (parámetros inválidos). En el experimento, un JSON roto devuelve −32700 y el servidor sigue vivo; una petición sin el campo `jsonrpc` devuelve −32600; un método inexistente, −32601; y una herramienta desconocida, −32602. Distinto es el error **de la herramienta**: la llamada fue bien formada, pero la herramienta no pudo hacer lo pedido (faltan argumentos, el curso no existe). Se devuelve como un resultado normal con un indicador de error y un texto, **que el modelo puede leer y corregir**.

## Ejemplo

Ejemplo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) (sección «Ejemplo mínimo»):

Cada línea es un mensaje completo; la respuesta repite el `id`. Un error de herramienta tendría `isError` verdadero con un texto que explique qué faltó.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md)) son: El servidor es una demostración con nombres de métodos de MCP y no una implementación conforme; no se probó ningún servidor ni cliente de terceros, ni la autorización, los recursos o los transportes por HTTP; la máquina de estados es un subconjunto inspirado en A2A; las doce descripciones las escribió el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Resultado](../r/resultado.md), [A2A](../a/a2a.md), [Error de protocolo](./error-de-protocolo.md), [JSON-RPC 2.0](../j/json-rpc-2-0.md), [MCP](../m/mcp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Errata](./errata.md) · [Error de protocolo →](./error-de-protocolo.md)
