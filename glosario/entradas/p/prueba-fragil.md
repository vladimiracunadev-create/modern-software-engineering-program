# Prueba frágil

[↑ Glosario](../../README.md) · [← Prueba discriminante](./prueba-discriminante.md) · [Prueba inestable →](./prueba-inestable.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Prueba que falla ante un cambio que no altera el comportamiento observable.

Definición de trabajo de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md).

## Por qué importa

La clase donde se define, [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md), existe con este propósito: la clase es un taller: parte de una suite de catorce pruebas que «pasan» y exige demostrar, para cada una, qué defecto detecta, que falla con él y pasa sin él, y que no se rompe ante un refactor que conserva el comportamiento.

## Cómo funciona

Según [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md):

Una prueba frágil falla cuando el código cambia sin cambiar su comportamiento observable: se compara el texto exacto de un mensaje de error, el orden de las claves de un diccionario, el número de llamadas a una dependencia. La fragilidad se mide con refactorizaciones neutras: renombrar variables, extraer una función, cambiar el orden de las claves, reescribir un mensaje. Cada falla es un costo de mantenimiento y un incentivo a no refactorizar. Una prueba puede tener alto poder de detección y ser frágil a la vez; el veredicto debe nombrar ambas cosas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md):

El equipo de la plataforma exige que toda prueba nueva de un módulo crítico llegue con su demostración: una línea en `evidencia.json` con el defecto que detecta (un mutante o un caso histórico), la confirmación de que falla con él y pasa sin él, y el resultado de las refactorizaciones del repositorio. Un trabajo de la integración continua re-ejecuta el paquete en cada cambio del módulo y falla si una prueba deja de matar su defecto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md)) son:

- **Una prueba «mata» mutantes y no afirma ningún valor** — causa: muertes por excepción. Corrección: reforzar con aserciones sobre valores y etiquetar las de humo.
- **Una prueba pasa con y sin el defecto** — causa: pasa por una razón distinta de la que declara. Corrección: caso que solo el defecto rompa.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una prueba frágil falla cuando el código cambia sin cambiar su comportamiento observable: se compara el texto exacto de un mensaje de error, el orden de las claves de un diccionario, el número de llamadas a una dependencia. ([SE-431](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-422](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-422-pruebas-unitarias-y-diseno-testable/README.md), [SE-426](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-426-mutacion-fuzzing-y-generacion-de-casos/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Muerte por aserción](../m/muerte-por-asercion.md), [Muerte por excepción](../m/muerte-por-excepcion.md), [Paquete de evidencia](./paquete-de-evidencia.md), [Rojo, verde, refactor](../r/rojo-verde-refactor.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-431 — Taller: demostrar que una prueba detecta defectos](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-431-taller-demostrar-que-una-prueba-detecta-defectos/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [DeMillo, Lipton y Sayward, «Hints on test data selection»](https://doi.org/10.1109/C-M.1978.218136) — origen de los mutantes para evaluar pruebas; autoridad: artículo original de 1978.
- [Google Testing Blog: Mutation Testing](https://testing.googleblog.com/2021/04/mutation-testing.html) — mutantes en la revisión de código; autoridad: equipo de pruebas de Google.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.
- [Martin Fowler, «SelfTestingCode»](https://martinfowler.com/bliki/SelfTestingCode.html) — código que se comprueba a sí mismo; autoridad: autor del texto.
- [Martin Fowler, «TestDrivenDevelopment»](https://martinfowler.com/bliki/TestDrivenDevelopment.html) — ciclo rojo-verde; autoridad: autor del texto.

---

[↑ Glosario](../../README.md) · [← Prueba discriminante](./prueba-discriminante.md) · [Prueba inestable →](./prueba-inestable.md)
