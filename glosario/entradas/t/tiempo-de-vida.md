# Tiempo de vida

[↑ Glosario](../../README.md) · [← Tiempo de respuesta](./tiempo-de-respuesta.md) · [Tiempo de visibilidad →](./tiempo-de-visibilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Intervalo durante el cual un cliente puede reutilizar un resultado de listado sin volver a pedirlo.

Definición de trabajo de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Por qué importa

La clase donde se define, [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), existe con este propósito: la clase existe para que dejes de tratar a un servidor de herramientas como una extensión inofensiva del agente.

## Cómo funciona

Según [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md):

Los resultados de listado (herramientas, recursos, plantillas) llevan en la versión 2026-07-28 un tiempo de vida (`ttlMs`) y un alcance de caché (`cacheScope`), para que el cliente decida cuándo volver a pedirlos y evite reconsultar innecesariamente. La decisión del tiempo de vida tiene tres costos que se compensan. Un tiempo corto aumenta las lecturas al servidor; uno largo mantiene al cliente creyendo un catálogo que ya no existe; y una herramienta retirada, restringida o modificada por razones de seguridad sigue disponible para el cliente hasta que expire la caché. La elección depende de la rapidez con que un cambio debe surtir efecto, no de la comodidad. Los listados de herramientas que gobiernan acciones con consecuencias merecen un tiempo corto; los de recursos estáticos pueden vivir mucho más.

Según [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus tres servidores. Clasifica las piezas: de las doce herramientas, cinco tienen efecto fuera del sistema (enviar, borrar, escribir) y quedan bajo aprobación humana; los recursos del calendario se incorporan solo por selección explícita; las plantillas del servidor propio se publican con una revisión de contenido. Para cada servidor escribe una política de confianza: el propio, confiado con revisión de cada cambio; el del proveedor de calendario, confiado en lo que publica y no en sus anotaciones; el de utilidades de texto, sin confianza, ejecutado en un entorno aislado y con sus herramientas fijadas por huella.

## Ejemplo

Ejemplo de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* revisa sus tres servidores. Clasifica las piezas: de las doce herramientas, cinco tienen efecto fuera del sistema (enviar, borrar, escribir) y quedan bajo aprobación humana; los recursos del calendario se incorporan solo por selección explícita; las plantillas del servidor propio se publican con una revisión de contenido.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una herramienta retirada sigue funcionando** — causa: caché demasiado larga. Corrección: fijar el tiempo de vida por el riesgo de la herramienta. ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: la validación de mensajes y las huellas son código real sobre datos sintéticos y la caché es una simulación en tiempo virtual con semilla fija.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo](../i/intervalo.md), [Resultado](../r/resultado.md), [Herramientas](../h/herramientas.md), [Huella](../h/huella.md), [Plantilla de petición](../p/plantilla-de-peticion.md), [Recurso](../r/recurso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-249](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-249-caching-rate-limiting-y-proteccion/README.md), [SE-020](../../../classes/part-01-computadores-y-representacion-de-informacion/se-020-compilacion-interpretacion-bytecode-y-jit/README.md), [SE-304](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-304-patrones-creacionales-estructurales-y-conductuales/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «ttlMs».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — núcleo sin estado, cabeceras de enrutamiento, rondas múltiples, caché de listados, refuerzo de la autorización y obsolescencias; autoridad: mantenedores de MCP.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — delegado confundido, paso de tokens, minimización de alcances, SSRF y servidores locales; autoridad: mantenedores de MCP.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — forma de las peticiones; autoridad: especificación del grupo JSON-RPC.

---

[↑ Glosario](../../README.md) · [← Tiempo de respuesta](./tiempo-de-respuesta.md) · [Tiempo de visibilidad →](./tiempo-de-visibilidad.md)
