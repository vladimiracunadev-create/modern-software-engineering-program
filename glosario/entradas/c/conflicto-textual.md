# Conflicto textual

[↑ Glosario](../../README.md) · [← Conflicto semántico](./conflicto-semantico.md) · [Conflictos entre atributos →](./conflictos-entre-atributos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Dos ramas modifican las mismas líneas.

Definición de trabajo de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md).

## Por qué importa

En [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md), el tema «Conflicto textual y semántico» importa porque la fusión limpia no es una integración correcta.

## Cómo funciona

Según [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

Un **conflicto textual** ocurre cuando dos ramas modifican las mismas líneas: Git lo detecta y obliga a decidir. En el experimento, «mismas líneas» termina en conflicto, y es el caso bien resuelto por la herramienta. Un **conflicto semántico** ocurre cuando los cambios son compatibles para Git e incompatibles para el programa: un renombre y un uso del nombre antiguo, un cambio de firma y una llamada con la firma anterior, dos funciones que asumen invariantes opuestos. En el experimento, esa fusión es limpia y las pruebas fallan. La defensa es ejecutar el menú completo (`SE-583`) después de cada fusión, no solo en cada rama.

## Ejemplo

Caso medido en la sección «Conflicto textual y conflicto semántico» de [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md):

Un **conflicto textual** ocurre cuando dos ramas modifican las mismas líneas: Git lo detecta y obliga a decidir. En el experimento, «mismas líneas» termina en conflicto, y es el caso bien resuelto por la herramienta. Un **conflicto semántico** ocurre cuando los cambios son compatibles para Git e incompatibles para el programa: un renombre y un uso del nombre antiguo, un cambio de firma y una llamada con la firma anterior, dos funciones que asumen invariantes opuestos. En el experimento, esa fusión es limpia y las pruebas fallan.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md)) son: Se ejecutaron cuatro fusiones con ramas reales de Git y una simulación de solapamiento con parámetros del autor, en Windows 11 con CPython 3.12.9 y Git 2.55. Los agentes son ediciones guionizadas: no se midió ningún sistema multiagente real ni su beneficio frente a un solo agente. El siguiente paso, `SE-585`, trata cómo saber qué hace el harness: trazas, métricas y evaluaciones del propio harness.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol de trabajo](../a/arbol-de-trabajo.md), [Canal de coordinación](./canal-de-coordinacion.md), [Conflicto semántico](./conflicto-semantico.md), [Integrador](../i/integrador.md), [Propiedad de archivos](../p/propiedad-de-archivos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-584 — Multiagente y coordinación dentro del harness](../../../classes/part-48-harness-y-agentic-engineering/se-584-multiagente-y-coordinacion-dentro-del-harness/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Conflicto semántico](./conflicto-semantico.md) · [Conflictos entre atributos →](./conflictos-entre-atributos.md)
