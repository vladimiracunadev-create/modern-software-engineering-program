# Tramo revisable

[↑ Glosario](../../README.md) · [← Trama](./trama.md) · [Tramos graduales / por volumen →](./tramos-graduales-por-volumen.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Commit de un tamaño que una persona puede leer con atención (unas 400 líneas modificadas, según la documentación).

Definición de trabajo de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md).

## Por qué importa

La clase donde se define, [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), existe con este propósito: la clase existe para que sepas leer un **flujo de trabajo para agentes de código** como lo que es: un conjunto de reglas con una razón cada una y con evidencia de distinta calidad.

## Cómo funciona

Según [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

El flujo pide confirmar las unidades de trabajo en la rama de la funcionalidad en tramos revisables de unas 400 líneas modificadas, y que una unidad de alto riesgo vaya en su propio commit. El número es una convención, y su razón es de revisión: una persona (o un agente revisor) puede leer 400 líneas con atención; 463 de una vez, con reorganizaciones mezcladas, no. El tamaño se puede medir con `git log --numstat`. Lo que no se puede medir es si un commit pequeño es coherente.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md)) son: No se ejecutó Gentle AI ni se midió el efecto de ODD en equipos; los historiales son sintéticos y las reglas son las que la documentación declara. El siguiente paso, `SE-551`, es el taller: el mismo cambio, silenciar un curso, con cinco metodologías, medido con los mismos mutantes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Decisión de entrega](../d/decision-de-entrega.md), [Documento de tarea](../d/documento-de-tarea.md), [ODD](../o/odd.md), [Rojo y verde](../r/rojo-y-verde.md), [Siguiente paso](../s/siguiente-paso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-550 — ODD: desarrollo orgánico y su contraste con SDD](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Trama](./trama.md) · [Tramos graduales / por volumen →](./tramos-graduales-por-volumen.md)
