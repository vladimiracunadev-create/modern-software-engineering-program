# Herramientas

[↑ Glosario](../../README.md) · [← Herencia de prioridad](./herencia-de-prioridad.md) · [Heterogeneidad →](./heterogeneidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Función que un servidor expone y que el modelo puede invocar; es controlada por el modelo.

Definición de trabajo de [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md).

## Por qué importa

En [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), el tema «Herramientas» importa porque lo que el agente no puede hacer, no lo hará; lo que puede, lo hará sin entender.

En [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), el tema «Herramientas» importa porque TLA+, SPARK y Alloy cubren niveles distintos.

## Cómo funciona

Según [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md):

Las herramientas son las acciones que el harness acepta traducir en efectos: leer un archivo, aplicar un cambio, ejecutar pruebas. Cada una amplía lo que el agente puede lograr y lo que puede romper. Quitar la herramienta de escritura deja al agente leyendo en bucle, porque la política no tiene otra salida: el agente no «sabe» que no puede escribir hasta que lo intenta, y el harness que no lo registra deja una traza idéntica a la del contexto perdido. Esa ambigüedad vuelve en `SE-587` y se resuelve con un campo de la traza.

Según [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md):

El equipo adopta un asistente de código para el mantenimiento de *Avisos*. Durante dos semanas todo va bien; en la tercera, tres cambios llegan a revisión con las pruebas en rojo. La revisión encuentra que el asistente los dio por terminados. Tres hipótesis compiten: el modelo empeoró, el prompt cambió, el entorno cambió. La persona responsable revisa las trazas de los tres casos y encuentra que ninguno ejecutó las pruebas. Revisa el archivo de instrucciones: una reorganización había movido la línea de verificación a un archivo que el producto ya no cargaba. La corrección no toca el modelo: restaura la línea y añade una compuerta (`SE-583`) que rechaza la terminación sin pruebas en verde.

## Ejemplo

Ejemplo de [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) (sección «Ejemplo mínimo»):

La tarea `T1`: `add(a, b)` devuelve `a - b`. El harness completo hace cuatro pasos: lee `calc.py`; aplica el reemplazo `a - b` por `a + b`; ejecuta las pruebas, que pasan; y el agente declara la tarea terminada. En la traza aparecen exactamente `read`, `write`, `run_tests` y la solicitud de cierre. Quitar la herramienta de escritura produce una traza de doce lecturas; quitar el contexto, otra de doce lecturas. Las dos trazas son iguales y los fallos distintos: por eso la traza necesita más que el nombre de la herramienta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se ejecuta una herramienta no autorizada** — causa: cabecera y cuerpo no coinciden y nadie lo comprueba. Corrección: verificar la coherencia en el servidor y rechazar. ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md))
- **Una herramienta retirada sigue funcionando** — causa: caché demasiado larga. Corrección: fijar el tiempo de vida por el riesgo de la herramienta. ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Quitar la herramienta de escritura deja al agente leyendo en bucle, porque la política no tiene otra salida: el agente no «sabe» que no puede escribir hasta que lo intenta, y el harness que no lo registra deja una traza idéntica a la del contexto perdido. ([SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Modelo](../m/modelo.md), [Bloqueo](../b/bloqueo.md), [Contraejemplo](../c/contraejemplo.md), [Explosión de estados](../e/explosion-de-estados.md), [Huella](./huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-453 — Verificación formal y model checking: TLA+, SPARK y Alloy](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.
- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.
- [SE-577 — Anatomía de un harness: modelo, contexto, herramientas y bucles](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (375 clases más lo mencionan; las que más):

[SE-595](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-595-interoperabilidad-entre-agentes-mcp-y-a2a/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-218](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-218-entrada-estandar-salida-y-composicion-por-pipes/README.md), [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «herramienta».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anuncio de la especificación MCP 2026-07-28](https://blog.modelcontextprotocol.io/posts/2026-07-28/) — núcleo sin estado, cabeceras de enrutamiento, rondas múltiples, caché de listados, refuerzo de la autorización y obsolescencias; autoridad: mantenedores de MCP.
- [Especificación MCP: buenas prácticas de seguridad](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices) — delegado confundido, paso de tokens, minimización de alcances, SSRF y servidores locales; autoridad: mantenedores de MCP.
- [JSON-RPC 2.0](https://www.jsonrpc.org/specification) — forma de las peticiones; autoridad: especificación del grupo JSON-RPC.

---

[↑ Glosario](../../README.md) · [← Herencia de prioridad](./herencia-de-prioridad.md) · [Heterogeneidad →](./heterogeneidad.md)
