# Propiedad de archivos

[↑ Glosario](../../README.md) · [← Propiedad](./propiedad.md) · [Propiedad de seguridad →](./propiedad-de-seguridad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Asignación exclusiva de quién puede modificar cada archivo.

Definición de trabajo de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Por qué importa

En [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), el tema «Propiedad de archivos» importa porque evita que dos agentes editen lo mismo.

## Cómo funciona

[SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Propiedad de archivos: dividir para no pisarse» de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

La forma más eficaz de evitar conflictos es no producirlos: asignar a cada agente un conjunto de archivos o módulos de los que es propietario y prohibir a los demás modificarlos. Si una tarea exige tocar un archivo ajeno, se pide al propietario (o al coordinador) y se registra. La simulación muestra por qué es necesario: con 40 archivos y 3 por tarea, la probabilidad de que dos agentes toquen algún archivo en común es del 21,3 %; con cuatro agentes, 79,9 %; con seis, 98,4 %.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md)) son: Se ejecutaron cuatro fusiones con ramas reales de Git y una simulación de solapamiento con parámetros del autor, en Windows 11 con CPython 3.12.9 y Git 2.55. Los agentes son ediciones guionizadas: no se midió ningún sistema multiagente real ni su beneficio frente a un solo agente. El siguiente paso, `SE-585`, trata cómo saber qué hace el harness: trazas, métricas y evaluaciones del propio harness.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol de trabajo](../a/arbol-de-trabajo.md), [Canal de coordinación](../c/canal-de-coordinacion.md), [Conflicto semántico](../c/conflicto-semantico.md), [Conflicto textual](../c/conflicto-textual.md), [Integrador](../i/integrador.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-032](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-032-instalacion-de-software-y-gestores-de-paquetes-del-sistema/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Propiedad](./propiedad.md) · [Propiedad de seguridad →](./propiedad-de-seguridad.md)
