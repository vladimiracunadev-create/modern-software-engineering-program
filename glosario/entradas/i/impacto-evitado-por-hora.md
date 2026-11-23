# Impacto evitado por hora

[↑ Glosario](../../README.md) · [← Impacto escapado](./impacto-escapado.md) · [Impacto habilitado →](./impacto-habilitado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Impacto que se evita respecto de no hacer nada, dividido por el costo.

Definición de trabajo de [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md).

## Por qué importa

La clase donde se define, [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md), existe con este propósito: el proyecto existe para que conviertas lo medido en las once clases anteriores en **una política de equipo**: una tabla que dice qué evidencia se exige a cada clase de cambio, quién la produce, dónde se ejecuta y cuándo se revisa la propia política.

## Cómo funciona

Según [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md):

La simulación aplica cinco políticas a 300 cambios sintéticos con riesgos bajo, medio y alto (50 %, 35 % y 15 %), el 55 % con reglas deterministas y el 35 % ambiguos. «Nada» deja un impacto escapado de 1 157. «TDD en todo» cuesta 232 horas y deja 745. «Todo en todo» cuesta 1 240 y deja 489. «Por riesgo» cuesta 482 y deja 532. «Por riesgo y ambigüedad» cuesta 485 y deja 499. En impacto evitado por hora, TDD en todo evita 1,77; por riesgo y ambigüedad, 1,36; por riesgo, 1,29; todo en todo, 0,54.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md)) son: La simulación usa supuestos del autor salvo las tasas de detección, y estas salen de una función pequeña con defectos sembrados; no se midió ningún equipo. La [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md) (`SE-577` en adelante) estudia el harness que hace cumplir políticas como esta a un agente: instrucciones de repositorio, herramientas, permisos, contexto y bucles.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Impacto](./impacto.md), [Clase de cambio](../c/clase-de-cambio.md), [Excepción](../e/excepcion.md), [Impacto escapado](./impacto-escapado.md), [Política metodológica](../p/politica-metodologica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-552 — Proyecto: política metodológica de equipo con evidencia](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-552-proyecto-politica-metodologica-de-equipo-con-evidencia/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Impacto escapado](./impacto-escapado.md) · [Impacto habilitado →](./impacto-habilitado.md)
