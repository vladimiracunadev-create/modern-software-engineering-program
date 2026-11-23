# Regla mecanizable

[↑ Glosario](../../README.md) · [← Regla entre campos](./regla-entre-campos.md) · [Regla muerta →](./regla-muerta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md)

## Definición

Regla que un programa puede decidir sobre un cambio.

Definición de trabajo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md).

## Por qué importa

En [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md), el tema «Reglas mecanizables y semánticas» importa porque decide dónde vive cada regla.

## Cómo funciona

[SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: consulta la clase para el mecanismo completo.

## Ejemplo

Ejemplo de [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) (sección «Caso conductor»):

El arnés de *Avisos* ya sabe qué piezas tiene (`SE-577`). Esta clase recorta su archivo de instrucciones: las reglas mecanizables pasan a un comprobador compartido por el hook y por la integración, y el archivo conserva las reglas que solo una persona puede juzgar. El comprobador se reutiliza como compuerta en `SE-583`.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md)) son: Se midió un comprobador de seis reglas sobre diecisiete casos del autor, en Windows 11 con CPython 3.12.9. No se midió el cumplimiento de ningún modelo con reglas en prosa ni el efecto del tamaño del archivo de instrucciones en el comportamiento de un agente real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-577](../../../classes/part-48-harness-y-agentic-engineering/se-577-anatomia-de-un-harness-modelo-contexto-herramientas-y-bucles/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](./regla.md), [Sobre](../s/sobre.md), [Compuerta](../c/compuerta.md), [Falsa alarma](../f/falsa-alarma.md), [Hook](../h/hook.md), [Omisión](../o/omision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-578 — Instrucciones de repositorio y cumplimiento determinista](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Regla entre campos](./regla-entre-campos.md) · [Regla muerta →](./regla-muerta.md)
