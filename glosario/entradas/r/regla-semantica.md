# Regla semántica

[↑ Glosario](../../README.md) · [← Regla muerta](./regla-muerta.md) · [Reglas de parada →](./reglas-de-parada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Regla que exige juicio humano o de un modelo.

Definición de trabajo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md).

## Por qué importa

La clase donde se define, [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), existe con este propósito: la clase existe para que escribas las instrucciones de un repositorio sabiendo qué parte de ellas es una petición y qué parte es una garantía.

## Cómo funciona

Según [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md):

El equipo revisa su archivo de instrucciones de cuarenta líneas. Clasifica: veinticinco reglas son mecanizables, quince son semánticas o contextuales. Escribe comprobadores para las ocho más infringidas, los pone como hook previo a la escritura y como paso de la integración continua, y recorta el archivo a las quince reglas semánticas más los comandos de preparación. El archivo queda en tres cuartas partes de su tamaño y las infracciones mecánicas llegan a revisión muy pocas veces. El hallazgo inesperado son dos falsas alarmas semanales de la regla de rutas, causadas por comentarios; las resuelven pasando esa regla a un análisis de cadenas con el árbol. La lección es que mecanizar una regla abre un trabajo de mantenimiento: casos de prueba para la regla y revisión de sus falsas alarmas.

## Ejemplo

Ejemplo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) (sección «Ejemplo profesional»):

El equipo revisa su archivo de instrucciones de cuarenta líneas. Clasifica: veinticinco reglas son mecanizables, quince son semánticas o contextuales. Escribe comprobadores para las ocho más infringidas, los pone como hook previo a la escritura y como paso de la integración continua, y recorta el archivo a las quince reglas semánticas más los comandos de preparación. El archivo queda en tres cuartas partes de su tamaño y las infracciones mecánicas llegan a revisión muy pocas veces. El hallazgo inesperado son dos falsas alarmas semanales de la regla de rutas, causadas por comentarios; las resuelven pasando esa regla a un análisis de cadenas con el árbol.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md)) son: Se midió un comprobador de seis reglas sobre diecisiete casos del autor, en Windows 11 con CPython 3.12.9. No se midió el cumplimiento de ningún modelo con reglas en prosa ni el efecto del tamaño del archivo de instrucciones en el comportamiento de un agente real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Regla](./regla.md), [Compuerta](../c/compuerta.md), [Falsa alarma](../f/falsa-alarma.md), [Hook](../h/hook.md), [Omisión](../o/omision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Regla muerta](./regla-muerta.md) · [Reglas de parada →](./reglas-de-parada.md)
