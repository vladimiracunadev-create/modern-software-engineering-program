# MCP

[↑ Glosario](../../README.md) · [← MC/DC](./mc-dc.md) · [Mecanismo →](./mecanismo.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Protocolo abierto para conectar aplicaciones de IA con herramientas y datos mediante mensajes JSON-RPC.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

La clase donde se define, [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), existe con este propósito: la clase existe para que entiendas qué resuelven y qué no resuelven los protocolos que conectan agentes con herramientas (**MCP**, Model Context Protocol) y agentes con otros agentes (**A2A**, Agent2Agent).

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

Sin un estándar, cada agente implementa a mano la llamada a cada herramienta: formato de petición, descripción para el modelo, manejo de errores. MCP define esa capa: un servidor expone herramientas (con nombre, descripción y esquema de entrada), un cliente las descubre y las invoca, y los mensajes viajan como JSON-RPC 2.0 por un transporte (entrada y salida estándar para procesos locales, HTTP para remotos). La ganancia es de integración: una herramienta escrita una vez sirve a cualquier cliente que hable el protocolo. En el experimento, para cuatro agentes y seis herramientas, los conectores bajan de 24 a 10. No es una medición de rendimiento: es aritmética, el producto frente a la suma.

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

No: resuelven capas distintas. MCP conecta un agente con herramientas y datos (llamadas relativamente cortas, con esquema); A2A conecta agentes con otros agentes (tareas con estado, posiblemente largas). Un sistema puede usar ambos.

## Ejemplo

Ejemplo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) (sección «Preguntas frecuentes»):

No: resuelven capas distintas. MCP conecta un agente con herramientas y datos (llamadas relativamente cortas, con esquema); A2A conecta agentes con otros agentes (tareas con estado, posiblemente largas). Un sistema puede usar ambos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** es un servidor de demostración con los nombres de métodos de MCP, no una implementación conforme de ninguna versión de la especificación; la mediana de 0,10 ms es de una ida y vuelta local por tuberías y no representa una red ni un servidor remoto. ([SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [A2A](../a/a2a.md), [Error de herramienta](../e/error-de-herramienta.md), [Error de protocolo](../e/error-de-protocolo.md), [JSON-RPC 2.0](../j/json-rpc-2-0.md), [Servidor MCP](../s/servidor-mcp.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← MC/DC](./mc-dc.md) · [Mecanismo →](./mecanismo.md)
