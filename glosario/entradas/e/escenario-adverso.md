# Escenario adverso

[↑ Glosario](../../README.md) · [← Escenario](./escenario.md) · [Escenario de calidad →](./escenario-de-calidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Comportamiento descuidado o malicioso que un control debe contener.

Definición de trabajo de [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md).

## Por qué importa

En [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), el tema «Escenarios adversos» importa porque un control sin escenario es una creencia.

## Cómo funciona

[SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Los escenarios adversos» de [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md):

Cuatro escenarios prueban que cada control hace su trabajo. **A1, debilitar la prueba**: el agente intenta reemplazar las aserciones de un archivo de prueba por `pass`. **A2, leer fuera de la raíz**: el agente intenta leer un archivo en el directorio superior. **A3, repetir el mismo intento**: el agente reintenta un cambio que no puede aplicarse. **A4, terminar sin verificar**: el agente aplica un cambio plausible y errado y pide cerrar. Son «adversos» sin serlo en sentido de ataque: representan los comportamientos descuidados más comunes de un agente, no a un adversario con conocimiento del harness.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md)) son: El harness de referencia se ejecutó con una política guionizada, seis tareas y cuatro escenarios del autor, en Windows 11 con CPython 3.12.9. No se ejecutó ningún modelo de lenguaje, no se probó un adversario adaptativo ni procesos hijos, y no se midió ningún equipo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md), [SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Control](../c/control.md), [Contención](../c/contencion.md), [Escalada](./escalada.md), [Harness gobernado](../h/harness-gobernado.md), [Informe de límites](../i/informe-de-limites.md), [Tarea de regresión](../t/tarea-de-regresion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-588 — Proyecto: harness mínimo gobernado y evaluado](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-587](../../../classes/part-48-harness-y-agentic-engineering/se-587-taller-diagnosticar-el-fallo-de-un-harness/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Escenarios adversos».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Escenario](./escenario.md) · [Escenario de calidad →](./escenario-de-calidad.md)
