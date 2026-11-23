# Paso ambiguo

[↑ Glosario](../../README.md) · [← Pasarela](./pasarela.md) · [Paso de comprobación →](./paso-de-comprobacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Paso de un escenario que encaja con más de una definición ejecutable.

Definición de trabajo de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Por qué importa

La clase donde se define, [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), existe con este propósito: la clase existe para convertir una regla en ejemplos concretos que negocio, desarrollo y pruebas lean igual, y para saber cuándo esos ejemplos son una especificación suficiente y cuándo solo un recuerdo del camino feliz.

## Cómo funciona

Según [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md):

**Cómo leer la figura.** A la izquierda está el ejecutor con sus cuatro escenarios y a la derecha lo que detecta en cada caso. La caja dorada es una ambigüedad (dos patrones para un paso), las coral son pasos sin definición o con ambos problemas y la gris resume los totales. Lo que une a todas es que el ejecutor mira la forma de la redacción, no su significado. **Dónde deja de valer:** el ejecutor mira forma. Un escenario sin pasos indefinidos ni ambiguos puede afirmar un resultado falso, o no afirmar nada (un `Entonces` que solo comprueba que no hubo excepción). Conviene tratar los pasos ambiguos como errores de construcción y los indefinidos como señal de redacciones que derivaron, y complementar con revisión humana.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md):

En la plataforma, los escenarios viven en el repositorio junto al código de la regla. Cada escenario tiene un título que dice la intención («Una entrega a las 24 horas exactas es de un día»), usa solo vocabulario del dominio y nombra en su `Dado` los datos relevantes y nada más. Las definiciones de pasos están en un módulo único, y un guardián de integración continua falla si hay pasos indefinidos, ambiguos o definiciones sin uso.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)) son:

- **Todos los escenarios pasan y un defecto de frontera llega a producción** — causa: los ejemplos son del camino típico y no separan las lecturas. Corrección: elegir ejemplos por las variantes que matan y añadir fronteras (24 h, 25 h, tope, nota 0).
- **Cada rediseño de la interfaz rompe veinte escenarios** — causa: los escenarios son imperativos y describen clics. Corrección: reescribirlos en lenguaje de dominio y mover el cómo a las definiciones de pasos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó Cucumber ni ningún marco de BDD, las once variantes y los fallos de 2 y 3 factores son construcciones del autor y no se midió a ningún equipo. La siguiente clase pregunta qué afirmaciones se cumplen para todos los casos y cómo se comprueban.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](../e/escenario.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Ejemplo como especificación](../e/ejemplo-como-especificacion.md), [Given-When-Then](../g/given-when-then.md), [Variante defectuosa](../v/variante-defectuosa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

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

[↑ Glosario](../../README.md) · [← Pasarela](./pasarela.md) · [Paso de comprobación →](./paso-de-comprobacion.md)
