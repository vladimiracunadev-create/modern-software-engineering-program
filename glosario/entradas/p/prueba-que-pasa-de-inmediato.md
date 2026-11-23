# Prueba que pasa de inmediato

[↑ Glosario](../../README.md) · [← Prueba periódica](./prueba-periodica.md) · [Prueba unitaria →](./prueba-unitaria.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Prueba que no aporta información hasta que se demuestre lo contrario.

Definición de trabajo de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md).

## Por qué importa

La clase donde se define, [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), existe con este propósito: la clase existe para que practiques TDD como una técnica con controles y no como la consigna «escribe las pruebas primero».

## Cómo funciona

Según [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md):

Una prueba que pasa de inmediato no ha aportado información: o el comportamiento ya existía o la prueba no comprueba lo que dice. Una prueba que falla por un error ajeno al comportamiento (un nombre mal escrito, una importación) tampoco: no distingue entre «el comportamiento falta» y «la prueba está rota». El control es ver el mensaje de fallo y comprobar que describe la diferencia entre lo esperado y lo obtenido. Es el control más barato de la técnica y el que más se omite cuando quien escribe la prueba y el código es el mismo agente en el mismo paso.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una prueba que pasa de inmediato no ha aportado información: o el comportamiento ya existía o la prueba no comprueba lo que dice. ([SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Lista de escenarios](../l/lista-de-escenarios.md), [Refactor](../r/refactor.md), [Rojo](../r/rojo.md), [Triangulación](../t/triangulacion.md), [Verde](../v/verde.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Prueba periódica](./prueba-periodica.md) · [Prueba unitaria →](./prueba-unitaria.md)
