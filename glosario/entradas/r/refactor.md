# Refactor

[↑ Glosario](../../README.md) · [← Reescritura por estructura](./reescritura-por-estructura.md) · [Refactorización →](./refactorizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Un **refactor** es un cambio de estructura que conserva el comportamiento, hecho con todas las pruebas en verde ([SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md)).

## Por qué importa

La definición contiene su propia señal de alarma: si una prueba falla, el cambio no era un refactor. Esa regla distingue mejorar el diseño de cambiar el comportamiento por accidente, y separa los dos tipos de trabajo en commits y revisiones distintos.

## Cómo funciona

En el ciclo de TDD, el refactor es el tercer paso (rojo, verde, refactor): ocurre solo con las pruebas en verde y se detiene si alguna falla. Es el momento del diseño: nombres, eliminación de duplicación, una función extraída. Las pruebas **protegen** el refactor, pero no lo **guían**: el diseño que sale depende de quien refactoriza.

## Ejemplo

Extraer el cálculo del promedio a una función con nombre propio, renombrar variables y quitar un bloque duplicado, ejecutando la suite después de cada paso pequeño; si un paso la rompe, se revierte.

## Errores y confusiones comunes

Mezclar refactor con cambios de comportamiento en un mismo cambio; refactorizar sin pruebas que fijen el comportamiento; creer que TDD garantiza buen diseño.

## Límites y cuándo no aplica

[SE-542](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) señala que la afirmación de que TDD «produce mejor diseño» es donde los profesionales discrepan, y que la clase no mide ese efecto. Sin pruebas de caracterización, en código heredado, el refactor se hace después de fijar el comportamiento actual.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estructura](../e/estructura.md), [Hecho](../h/hecho.md), [Verde](../v/verde.md), [Lista de escenarios](../l/lista-de-escenarios.md), [Prueba que pasa de inmediato](../p/prueba-que-pasa-de-inmediato.md), [Rojo](./rojo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-542 — TDD: ciclo rojo-verde-refactor y diseño emergente](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-542-tdd-ciclo-rojo-verde-refactor-y-diseno-emergente/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md), [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), [SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), [SE-070](../../../classes/part-05-fundamentos-de-programacion/se-070-legibilidad-nombres-y-mantenimiento-basico/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), [SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Reescritura por estructura](./reescritura-por-estructura.md) · [Refactorización →](./refactorizacion.md)
