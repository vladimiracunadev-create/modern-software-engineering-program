# JSON-RPC 2.0

[↑ Glosario](../../README.md) · [← Journey de desarrollador](./journey-de-desarrollador.md) · [Juez automático →](./juez-automatico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Protocolo de llamadas remotas con mensajes JSON de petición, respuesta y notificación.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

La clase donde se define, [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), existe con este propósito: la clase existe para que entiendas qué resuelven y qué no resuelven los protocolos que conectan agentes con herramientas (**MCP**, Model Context Protocol) y agentes con otros agentes (**A2A**, Agent2Agent).

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

Sin un estándar, cada agente implementa a mano la llamada a cada herramienta: formato de petición, descripción para el modelo, manejo de errores. MCP define esa capa: un servidor expone herramientas (con nombre, descripción y esquema de entrada), un cliente las descubre y las invoca, y los mensajes viajan como JSON-RPC 2.0 por un transporte (entrada y salida estándar para procesos locales, HTTP para remotos). La ganancia es de integración: una herramienta escrita una vez sirve a cualquier cliente que hable el protocolo. En el experimento, para cuatro agentes y seis herramientas, los conectores bajan de 24 a 10. No es una medición de rendimiento: es aritmética, el producto frente a la suma.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md)) son: El servidor es una demostración con nombres de métodos de MCP y no una implementación conforme; no se probó ningún servidor ni cliente de terceros, ni la autorización, los recursos o los transportes por HTTP; la máquina de estados es un subconjunto inspirado en A2A; las doce descripciones las escribió el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [A2A](../a/a2a.md), [Error de herramienta](../e/error-de-herramienta.md), [Error de protocolo](../e/error-de-protocolo.md), [MCP](../m/mcp.md), [Servidor MCP](../s/servidor-mcp.md), [Tarjeta de agente](../t/tarjeta-de-agente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Journey de desarrollador](./journey-de-desarrollador.md) · [Juez automático →](./juez-automatico.md)
