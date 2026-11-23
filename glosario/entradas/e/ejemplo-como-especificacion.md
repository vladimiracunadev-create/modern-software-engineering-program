# Ejemplo como especificación

[↑ Glosario](../../README.md) · [← Ejemplo ancla](./ejemplo-ancla.md) · [Ejemplo de aceptación →](./ejemplo-de-aceptacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Caso con valores concretos de entrada y resultado esperado que toda implementación aceptable debe satisfacer.

Definición de trabajo de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Por qué importa

En [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), el tema «Ejemplos como especificación» importa porque un ejemplo con valores concretos elimina lecturas que la prosa deja abiertas.

## Cómo funciona

Según [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), en la sección «Ejemplos como especificación»:

Un ejemplo con valores concretos (30 horas de retraso, nota 80, resultado 72) obliga a decidir los puntos que la frase deja abiertos: cómo se redondea, qué base se usa, qué pasa en el límite. Su fortaleza es que cualquiera lo verifica con una calculadora; su debilidad, que cada ejemplo cubre un punto del dominio y nada más. Un conjunto de ejemplos no es una especificación completa: es un conjunto de puntos que una buena regla debe satisfacer. La pregunta útil no es «¿cuántos ejemplos tengo?» sino «¿qué lecturas distintas de la regla pasarían todos mis ejemplos?».

Según [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md), en la sección «Ejemplo como especificación»:

Un ejemplo nombra entrada, acción y resultado observable. Primero se seleccionan particiones y fronteras; después se codifica. Un ejemplo aislado no define todo el dominio, pero varios ejemplos pueden revelar vocabulario y una interfaz incómoda.

## Ejemplo

Caso medido en la sección «Ejemplos como especificación» de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md):

Un ejemplo con valores concretos (30 horas de retraso, nota 80, resultado 72) obliga a decidir los puntos que la frase deja abiertos: cómo se redondea, qué base se usa, qué pasa en el límite. Su fortaleza es que cualquiera lo verifica con una calculadora; su debilidad, que cada ejemplo cubre un punto del dominio y nada más. Un conjunto de ejemplos no es una especificación completa: es un conjunto de puntos que una buena regla debe satisfacer. La pregunta útil no es «¿cuántos ejemplos tengo?» sino «¿qué lecturas distintas de la regla pasarían todos mis ejemplos?».

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)) son:

- **Todos los escenarios pasan y un defecto de frontera llega a producción** — causa: los ejemplos son del camino típico y no separan las lecturas. Corrección: elegir ejemplos por las variantes que matan y añadir fronteras (24 h, 25 h, tope, nota 0).
- **Cada rediseño de la interfaz rompe veinte escenarios** — causa: los escenarios son imperativos y describen clics. Corrección: reescribirlos en lenguaje de dominio y mover el cómo a las definiciones de pasos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó Cucumber ni ningún marco de BDD, las once variantes y los fallos de 2 y 3 factores son construcciones del autor y no se midió a ningún equipo. La siguiente clase pregunta qué afirmaciones se cumplen para todos los casos y cómo se comprueban.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Valor](../v/valor.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Contrato](../c/contrato.md), [Control](../c/control.md), [Doble](../d/doble.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-069 — Pruebas tempranas y diseño por ejemplos](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.
- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cucumber: Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — palabras clave y semántica de Gherkin; autoridad: proyecto Cucumber.
- [Cucumber: Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) — guía para redactar escenarios declarativos y breves; autoridad: proyecto Cucumber.
- [North, «Introducing BDD»](https://dannorth.net/introducing-bdd/) — origen del vocabulario de comportamiento; autoridad: autor del término.
- [Adzic, Specification by Example](https://gojko.net/books/specification-by-example/) — ejemplos colaborativos como especificación viva; autoridad: autor del libro.
- [NIST: Automated Combinatorial Testing for Software](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software) — prueba combinatoria y cobertura de t-factores; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Ejemplo ancla](./ejemplo-ancla.md) · [Ejemplo de aceptación →](./ejemplo-de-aceptacion.md)
