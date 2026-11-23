# Error de protocolo

[↑ Glosario](../../README.md) · [← Error de herramienta](./error-de-herramienta.md) · [Error permanente →](./error-permanente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Respuesta con código de error JSON-RPC por una petición mal formada o inexistente.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

En [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), el tema «Errores de protocolo y de herramienta» importa porque el modelo solo puede corregir los segundos.

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

JSON-RPC define códigos para los fallos del protocolo: −32700 (JSON malformado), −32600 (petición inválida), −32601 (método inexistente), −32602 (parámetros inválidos). En el experimento, un JSON roto devuelve −32700 y el servidor sigue vivo; una petición sin el campo `jsonrpc` devuelve −32600; un método inexistente, −32601; y una herramienta desconocida, −32602. Distinto es el error **de la herramienta**: la llamada fue bien formada, pero la herramienta no pudo hacer lo pedido (faltan argumentos, el curso no existe). Se devuelve como un resultado normal con un indicador de error y un texto, **que el modelo puede leer y corregir**.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md)) son: El servidor es una demostración con nombres de métodos de MCP y no una implementación conforme; no se probó ningún servidor ni cliente de terceros, ni la autorización, los recursos o los transportes por HTTP; la máquina de estados es un subconjunto inspirado en A2A; las doce descripciones las escribió el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [A2A](../a/a2a.md), [Error de herramienta](./error-de-herramienta.md), [JSON-RPC 2.0](../j/json-rpc-2-0.md), [MCP](../m/mcp.md), [Servidor MCP](../s/servidor-mcp.md), [Tarjeta de agente](../t/tarjeta-de-agente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Error de herramienta](./error-de-herramienta.md) · [Error permanente →](./error-permanente.md)
