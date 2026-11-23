# ATDD

[↑ Glosario](../../README.md) · [← AST](./ast.md) · [Atestación →](./atestacion.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Desarrollo guiado por pruebas de aceptación; ciclo externo sobre TDD.

Definición de trabajo de [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md).

## Por qué importa

En [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), el tema «ATDD y ciclo doble» importa porque la aceptación guía; el TDD interno la cumple paso a paso.

## Cómo funciona

Según [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md):

ATDD añade a TDD un ciclo externo. Los ejemplos de aceptación se acuerdan primero, se convierten en una prueba de aceptación que falla y, mientras esa prueba está en rojo, se desarrolla el código con ciclos pequeños de rojo-verde-refactor (`SE-542`). Cuando la prueba de aceptación pasa, la funcionalidad cumple lo acordado. El ciclo externo responde «¿hicimos lo que se pidió?» y el interno, «¿cómo lo construimos?». Si solo existe el interno, el equipo puede construir con rigor algo que nadie pidió; si solo existe el externo, la construcción pierde la guía de pasos pequeños.

Según [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md):

Se solapan mucho. ATDD pone el acento en que la prueba de aceptación guía el desarrollo; BDD, en el lenguaje compartido y la conversación. Un equipo puede hacer ATDD sin Gherkin y BDD sin una prueba de aceptación automatizada.

## Ejemplo

Ejemplo de [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) (sección «Caso conductor»):

*Avisos* es el servicio de recordatorios y el silencio de un curso es el cambio. Los conjuntos de esta clase se vuelven a usar en `SE-551`, donde la tabla de ejemplos de ATDD se compara con las otras metodologías sobre el mismo cambio.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un equipo puede hacer ATDD sin Gherkin y BDD sin una prueba de aceptación automatizada. ([SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](../c/ciclo.md), [Sobre](../s/sobre.md), [Conjunto combinatorio](../c/conjunto-combinatorio.md), [Dimensión](../d/dimension.md), [Ejemplo de aceptación](../e/ejemplo-de-aceptacion.md), [Specification by Example](../s/specification-by-example.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-545 — ATDD y Specification by Example: aceptación ejecutable](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-551](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-551-taller-un-mismo-cambio-con-cinco-metodologias/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md), [SE-546](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-546-ddd-como-lenguaje-ubicuo-y-contexto-para-agentes/README.md), [SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), [SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← AST](./ast.md) · [Atestación →](./atestacion.md)
