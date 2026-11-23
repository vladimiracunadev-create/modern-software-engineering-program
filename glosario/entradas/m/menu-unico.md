# Menú único

[↑ Glosario](../../README.md) · [← Mentoría](./mentoria.md) · [Merge --abort →](./merge-abort.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Punto de entrada que ejecuta todas las compuertas en orden.

Definición de trabajo de [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md).

## Por qué importa

En [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md), el tema «Menú único» importa porque quita la divergencia entre lo que corre el agente, la persona y la integración.

## Cómo funciona

[SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «El menú único» de [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md):

El agente, la persona y la integración continua deben ejecutar exactamente las mismas compuertas con el mismo comando. Si cada cual ejecuta un subconjunto, un cambio puede pasar en la máquina del agente y fallar en integración, o lo contrario, y la confianza en «pasa» se erosiona. El menú es un script con un único punto de entrada (`python scripts/check.py`, `make check`) que lista las compuertas en orden, se detiene en la primera que falla, imprime su nombre y el motivo, y devuelve un código de salida que decide.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)) son: Se ejecutaron cinco compuertas sobre doce cambios del autor en un módulo de siete líneas, en Windows 11 con CPython 3.12.9. Los tiempos son de un equipo concreto. No se evaluó ninguna herramienta de integración continua ni se midió la proporción de defectos reales que atrapa cada compuerta. El siguiente paso, `SE-584`, trata qué ocurre cuando hay más de un agente trabajando sobre el mismo repositorio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Punto de entrada](../p/punto-de-entrada.md), [Compuerta](../c/compuerta.md), [Código de salida](../c/codigo-de-salida.md), [Meta-verificación](./meta-verificacion.md), [Retroalimentación](../r/retroalimentacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-582](../../../classes/part-48-harness-y-agentic-engineering/se-582-sandboxes-reversibilidad-y-control-de-dano/README.md), [SE-584](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Mentoría](./mentoria.md) · [Merge --abort →](./merge-abort.md)
