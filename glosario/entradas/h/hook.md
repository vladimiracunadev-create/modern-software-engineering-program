# Hook

[↑ Glosario](../../README.md) · [← Holgura](./holgura.md) · [Hora civil →](./hora-civil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Comando que el harness ejecuta en un punto del ciclo y que puede bloquear una acción.

Definición de trabajo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md).

## Por qué importa

En [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), el tema «Hook previo a la escritura» importa porque impide la acción en vez de reprobarla después.

## Cómo funciona

Según [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md):

Un **hook** es un comando que el harness ejecuta en un punto del ciclo (antes de usar una herramienta, después de editar) y que puede bloquear la acción. La documentación de Claude Code lo describe así y es un ejemplo: no toda herramienta de agentes ofrece lo mismo. Un hook previo impide que la regla se infrinja y muestra el motivo al agente en el mismo paso; es el control más barato en retroalimentación. Una **compuerta de integración** (`SE-583`) rechaza el cambio completo en la integración continua; no depende de que el hook exista en la máquina de cada persona. Lo robusto es poner la misma comprobación en ambos sitios: el hook para la retroalimentación temprana, la compuerta como red final.

Según [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md):

El equipo revisa su archivo de instrucciones de cuarenta líneas. Clasifica: veinticinco reglas son mecanizables, quince son semánticas o contextuales. Escribe comprobadores para las ocho más infringidas, los pone como hook previo a la escritura y como paso de la integración continua, y recorta el archivo a las quince reglas semánticas más los comandos de preparación. El archivo queda en tres cuartas partes de su tamaño y las infracciones mecánicas llegan a revisión muy pocas veces. El hallazgo inesperado son dos falsas alarmas semanales de la regla de rutas, causadas por comentarios; las resuelven pasando esa regla a un análisis de cadenas con el árbol. La lección es que mecanizar una regla abre un trabajo de mantenimiento: casos de prueba para la regla y revisión de sus falsas alarmas.

## Ejemplo

Ejemplo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) (sección «Ejemplo profesional»):

El equipo revisa su archivo de instrucciones de cuarenta líneas. Clasifica: veinticinco reglas son mecanizables, quince son semánticas o contextuales. Escribe comprobadores para las ocho más infringidas, los pone como hook previo a la escritura y como paso de la integración continua, y recorta el archivo a las quince reglas semánticas más los comandos de preparación. El archivo queda en tres cuartas partes de su tamaño y las infracciones mecánicas llegan a revisión muy pocas veces. El hallazgo inesperado son dos falsas alarmas semanales de la regla de rutas, causadas por comentarios; las resuelven pasando esa regla a un análisis de cadenas con el árbol.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **compuerta de integración** (`SE-583`) rechaza el cambio completo en la integración continua; no depende de que el hook exista en la máquina de cada persona. ([SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Harness](./harness.md).
- **Ver también:** [Ciclo](../c/ciclo.md), [Comando](../c/comando.md), [Compuerta](../c/compuerta.md), [Falsa alarma](../f/falsa-alarma.md), [Omisión](../o/omision.md), [Regla mecanizable](../r/regla-mecanizable.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-115](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-115-plugins-extensiones-y-puntos-de-integracion/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Holgura](./holgura.md) · [Hora civil →](./hora-civil.md)
