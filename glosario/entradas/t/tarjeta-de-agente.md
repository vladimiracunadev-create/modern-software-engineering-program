# Tarjeta de agente

[↑ Glosario](../../README.md) · [← Tarea útil](./tarea-util.md) · [Tarjeta de modelo →](./tarjeta-de-modelo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Descripción de un agente: capacidades, endpoint y autenticación.

Definición de trabajo de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md).

## Por qué importa

La clase donde se define, [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), existe con este propósito: la clase existe para que entiendas qué resuelven y qué no resuelven los protocolos que conectan agentes con herramientas (**MCP**, Model Context Protocol) y agentes con otros agentes (**A2A**, Agent2Agent).

## Cómo funciona

Según [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

En A2A, un agente descubre a otro mediante una **tarjeta de agente** (qué hace, cómo se le llama, cómo se autentica) y le encarga una **tarea** que atraviesa estados: recibida, en curso, a la espera de más información del cliente, completada, fallida o cancelada. Lo importante para el ingeniero es que una tarea entre agentes es **un proceso con estado**, no una llamada de función: puede durar, pedir información, fallar o cancelarse, y el cliente debe tratarla así (con tiempo máximo, reintentos y reconciliación; `SE-596`). En el experimento, de 12 000 transiciones al azar entre seis estados, el modelo acepta 2 754 por ser legales y rechaza 9 246: impone que una tarea completada no vuelve a estar en curso.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md)) son: El servidor es una demostración con nombres de métodos de MCP y no una implementación conforme; no se probó ningún servidor ni cliente de terceros, ni la autorización, los recursos o los transportes por HTTP; la máquina de estados es un subconjunto inspirado en A2A; las doce descripciones las escribió el autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Autenticación](../a/autenticacion.md), [Capacidad](../c/capacidad.md), [A2A](../a/a2a.md), [Error de herramienta](../e/error-de-herramienta.md), [Error de protocolo](../e/error-de-protocolo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tarea útil](./tarea-util.md) · [Tarjeta de modelo →](./tarjeta-de-modelo.md)
