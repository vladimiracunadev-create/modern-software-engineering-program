# Descripciones no confiables

[↑ Glosario](../../README.md) · [← Descomposición por responsabilidad](./descomposicion-por-responsabilidad.md) · [Descubrimiento →](./descubrimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Son texto que el modelo lee como instrucciones potenciales.

Es uno de los temas de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), donde se enseña como «Descripciones no confiables».

## Por qué importa

En [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), el tema «Descripciones no confiables» importa porque son texto que el modelo lee como instrucciones potenciales.

En [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), el tema «Descripciones no confiables» importa porque son una vía de inyección.

## Cómo funciona

[SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus tres servidores. Clasifica las piezas: de las doce herramientas, cinco tienen efecto fuera del sistema (enviar, borrar, escribir) y quedan bajo aprobación humana; los recursos del calendario se incorporan solo por selección explícita; las plantillas del servidor propio se publican con una revisión de contenido.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) son:

- **Se ejecuta una herramienta no autorizada** — causa: cabecera y cuerpo no coinciden y nadie lo comprueba. Corrección: verificar la coherencia en el servidor y rechazar.
- **El agente actúa según instrucciones de una descripción** — causa: se trata el texto del servidor como de confianza. Corrección: huellas, revisión de cambios y aislamiento.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la validación de mensajes y las huellas son código real sobre datos sintéticos y la caché es una simulación en tiempo virtual con semilla fija.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [A2A](../a/a2a.md), [Error de herramienta](../e/error-de-herramienta.md), [Error de protocolo](../e/error-de-protocolo.md), [Herramientas](../h/herramientas.md), [Huella](../h/huella.md), [JSON-RPC 2.0](../j/json-rpc-2-0.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-595 — Interoperabilidad entre agentes: MCP y A2A](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — núcleo sin estado, cabeceras de enrutamiento, rondas múltiples, caché de listados, refuerzo de la autorización y obsolescencias; autoridad: mantenedores de MCP.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — delegado confundido, paso de tokens, minimización de alcances, SSRF y servidores locales; autoridad: mantenedores de MCP.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — forma de las peticiones; autoridad: especificación del grupo JSON-RPC.

---

[↑ Glosario](../../README.md) · [← Descomposición por responsabilidad](./descomposicion-por-responsabilidad.md) · [Descubrimiento →](./descubrimiento.md)
