# Herramientas

[↑ Glosario](../../README.md) · [← Herencia de prioridad](./herencia-de-prioridad.md) · [Heterogeneidad →](./heterogeneidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

En el trabajo con agentes y modelos, las **herramientas** (*tools*) son las funciones que un servidor expone y que el modelo puede invocar; las controla el modelo, no la persona ni la aplicación. [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) lo define así en el contexto del protocolo de contexto de modelos (MCP). [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) lo amplía al arnés de un agente: las herramientas son las acciones que el *harness* acepta traducir en efectos (leer un archivo, aplicar un cambio, ejecutar pruebas). El programa usa también «herramienta» en otros sentidos (las de ingeniería en general); aquí se trata el de agentes.

## Por qué importa

Las herramientas son el límite entre lo que el agente *dice* y lo que *hace*. Cada una amplía lo que el agente puede lograr y lo que puede romper. Decidir qué herramientas se exponen, con qué permisos y con qué verificación es diseñar la superficie de riesgo del agente, no un detalle de integración.

## Cómo funciona

El modelo recibe una descripción de cada herramienta (nombre, parámetros, propósito) y decide cuándo invocarla; el servidor o el arnés ejecuta la acción y devuelve el resultado. Dos consecuencias de que las controle el modelo:

- **Lo que el agente puede hacer es exactamente lo que el arnés acepta traducir**; quitar una herramienta cambia su comportamiento. [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) lo muestra: quitar la herramienta de escritura deja al agente leyendo en bucle, porque la política no tiene otra salida. El agente no «sabe» que no puede escribir hasta que lo intenta, y un arnés que no lo registra deja una traza idéntica a la del contexto perdido.
- **La decisión de usarlas es probabilística**, por lo que el servidor no debe confiar en la entrada: la autorización y la validación se hacen en el servidor, no en el prompt.

[SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) aporta dos puntos de control: verificar en el servidor la coherencia entre cabecera y cuerpo (para que no se ejecute una herramienta no autorizada), y fijar el tiempo de vida de cualquier caché de la lista de herramientas según el riesgo de la herramienta.

## Ejemplo

[SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md): el equipo adopta un asistente de código para el mantenimiento de *Avisos*. A la tercera semana, tres cambios llegan a revisión con las pruebas en rojo: el asistente los dio por terminados. Compiten tres hipótesis (el modelo empeoró, cambió el prompt, cambió el entorno). Las trazas muestran que ninguno ejecutó las pruebas; el archivo de instrucciones había perdido la línea de verificación en una reorganización. La corrección no toca el modelo: restaura la línea y añade una compuerta ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)) que rechaza la terminación sin pruebas en verde. La lección es que el comportamiento depende de las herramientas, las instrucciones y las compuertas, no solo del modelo.

## Errores y confusiones comunes

- **Se ejecuta una herramienta no autorizada.** Causa ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)): cabecera y cuerpo no coinciden y nadie lo comprueba; corrección: verificar la coherencia en el servidor y rechazar.
- **Una herramienta retirada sigue funcionando.** Caché demasiado larga; fijar el tiempo de vida por el riesgo de la herramienta.
- **Confiar en el prompt para limitar el alcance.** Un límite que solo está en el texto de instrucciones no es un control.
- **Confundirlas con recursos o prompts del protocolo.** En MCP, las herramientas son las controladas por el modelo; otros elementos los controla la aplicación o la persona.

## Límites y cuándo no aplica

Una herramienta bien definida no hace seguro a un agente: hay que acotar lo que puede tocar (confinamiento, mínimo privilegio) y poder deshacer lo que hizo. [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) es un caso de estudio sobre un asistente, no una medición de agentes reales. Y la lista de herramientas debe ser pequeña y con nombres claros: más herramientas amplían la superficie y la confusión del modelo.

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
