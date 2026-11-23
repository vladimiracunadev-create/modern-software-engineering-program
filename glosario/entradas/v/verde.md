# Verde

[↑ Glosario](../../README.md) · [← Verdad de referencia](./verdad-de-referencia.md) · [Veredicto de corrección →](./veredicto-de-correccion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Estado en que todas las pruebas pasan.

Definición de trabajo de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md).

## Por qué importa

En [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md), el tema «Verde antes de refactor» importa porque refactorizar con una prueba en rojo mezcla dos cambios.

## Cómo funciona

Según [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md):

El refactor ocurre solo con todas las pruebas en verde y se detiene si alguna falla: si falla, el cambio no era un refactor. Es el momento del diseño: nombres, duplicación, una función extraída. Es también el punto donde la afirmación más repetida sobre TDD («produce mejor diseño») se pone a prueba, y es donde los profesionales discrepan. Las pruebas protegen el refactor, pero no lo guían: el diseño que sale depende de quien refactoriza. Esta clase no mide ese efecto.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El refactor ocurre solo con todas las pruebas en verde y se detiene si alguna falla: si falla, el cambio no era un refactor. ([SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Lista de escenarios](../l/lista-de-escenarios.md), [Prueba que pasa de inmediato](../p/prueba-que-pasa-de-inmediato.md), [Refactor](../r/refactor.md), [Rojo](../r/rojo.md), [Triangulación](../t/triangulacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (333 clases más lo mencionan; las que más):

[SE-430](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-430-flakiness-diagnostico-y-mantenimiento/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-550](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-550-odd-desarrollo-organico-y-su-contraste-con-sdd/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Verdad de referencia](./verdad-de-referencia.md) · [Veredicto de corrección →](./veredicto-de-correccion.md)
