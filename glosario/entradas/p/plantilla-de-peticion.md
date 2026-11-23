# Plantilla de petición

[↑ Glosario](../../README.md) · [← Plantilla de experimento](./plantilla-de-experimento.md) · [Plantillas y ast →](./plantillas-y-ast.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Texto parametrizado que la persona selecciona explícitamente.

Definición de trabajo de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Por qué importa

La clase donde se define, [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), existe con este propósito: la clase existe para que dejes de tratar a un servidor de herramientas como una extensión inofensiva del agente.

## Cómo funciona

Según [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md):

MCP ofrece tres tipos de pieza, y la especificación distingue quién decide cuándo se usan. Las **herramientas** son funciones que el servidor expone y que el modelo puede descubrir e invocar por su cuenta; son «controladas por el modelo». Los **recursos** son datos (archivos, filas, documentos) que la aplicación anfitriona decide cómo incorporar al contexto; son «dirigidos por la aplicación». Las **plantillas de petición** son textos que la persona selecciona explícitamente, por ejemplo con una orden; son «controladas por el usuario». La distinción no es administrativa: decide quién es el último control.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus tres servidores. Clasifica las piezas: de las doce herramientas, cinco tienen efecto fuera del sistema (enviar, borrar, escribir) y quedan bajo aprobación humana; los recursos del calendario se incorporan solo por selección explícita; las plantillas del servidor propio se publican con una revisión de contenido.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) son:

- **Se ejecuta una herramienta no autorizada** — causa: cabecera y cuerpo no coinciden y nadie lo comprueba. Corrección: verificar la coherencia en el servidor y rechazar.
- **El agente actúa según instrucciones de una descripción** — causa: se trata el texto del servidor como de confianza. Corrección: huellas, revisión de cambios y aislamiento.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la validación de mensajes y las huellas son código real sobre datos sintéticos y la caché es una simulación en tiempo virtual con semilla fija.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Huella](../h/huella.md), [Recurso](../r/recurso.md), [Servidor MCP](../s/servidor-mcp.md), [Tiempo de vida](../t/tiempo-de-vida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — núcleo sin estado, cabeceras de enrutamiento, rondas múltiples, caché de listados, refuerzo de la autorización y obsolescencias; autoridad: mantenedores de MCP.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — delegado confundido, paso de tokens, minimización de alcances, SSRF y servidores locales; autoridad: mantenedores de MCP.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — forma de las peticiones; autoridad: especificación del grupo JSON-RPC.

---

[↑ Glosario](../../README.md) · [← Plantilla de experimento](./plantilla-de-experimento.md) · [Plantillas y ast →](./plantillas-y-ast.md)
