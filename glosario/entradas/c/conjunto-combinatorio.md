# Conjunto combinatorio

[↑ Glosario](../../README.md) · [← Conjunto](./conjunto.md) · [Conjunto curado →](./conjunto-curado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Ejemplos con todas las combinaciones de valores de varias dimensiones.

Definición de trabajo de [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

## Por qué importa

La clase donde se define, [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), existe con este propósito: la clase existe para que elijas los **ejemplos de aceptación** con el mismo cuidado con que eliges el diseño.

## Cómo funciona

Según [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md):

Combinar todos los valores de varias dimensiones cubre interacciones: una entrega entregada **y** silenciada, un aviso ya enviado **y** un curso silenciado. El conjunto combinatorio del laboratorio tiene 144 ejemplos (doce valores de tiempo por dos estados de entrega, dos de silencio y tres de avisos previos) y mata 17 de 18 mutantes. El que no mata es el que silencia a la persona en todos sus cursos, porque el conjunto usa siempre una persona y un curso: **una dimensión que no varía no se puede comprobar, por muchas combinaciones que haya de las demás**.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md)) son: Los conjuntos y los mutantes son del autor y los resultados esperados vienen de un modelo; no se midió un proceso de acuerdo con personas. El siguiente paso, `SE-546`, trata las palabras de esos ejemplos: DDD ordena el lenguaje y los contextos donde cada palabra vale, porque «entrega» no significa lo mismo en todas partes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Combinación](./combinacion.md), [Dimensión](../d/dimension.md), [Valor](../v/valor.md), [ATDD](../a/atdd.md), [Ejemplo de aceptación](../e/ejemplo-de-aceptacion.md), [Specification by Example](../s/specification-by-example.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Conjunto](./conjunto.md) · [Conjunto curado →](./conjunto-curado.md)
