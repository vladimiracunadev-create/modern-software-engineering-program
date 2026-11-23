# Escenario

[↑ Glosario](../../README.md) · [← Escape hatch y ownership](./escape-hatch-y-ownership.md) · [Escenario adverso →](./escenario-adverso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Ejemplo estructurado en contexto, acción y resultado observable, escrito en el lenguaje del dominio.

Definición de trabajo de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md): Ejemplo concreto con contexto, acción y resultado observable.

## Por qué importa

En [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), el tema «Given-When-Then» importa porque la estructura separa contexto, acción y resultado observable y hace que el escenario sea revisable por personas no técnicas.

## Cómo funciona

Según [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md):

La estructura de Gherkin ordena un escenario en contexto (`Dado`), acción (`Cuando`) y resultado observable (`Entonces`). La utilidad no es sintáctica: obliga a separar lo que ya era verdad de lo que ocurre y de lo que debe observarse. Un escenario con dos acciones o con una verificación en el contexto suele indicar que son dos escenarios. Los pasos se redactan en el lenguaje del dominio («la entrega llega 30 horas tarde») y se emparejan con código mediante expresiones; esa separación permite que cambie la implementación sin tocar el texto.

Según [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md):

En la plataforma, los escenarios viven en el repositorio junto al código de la regla. Cada escenario tiene un título que dice la intención («Una entrega a las 24 horas exactas es de un día»), usa solo vocabulario del dominio y nombra en su `Dado` los datos relevantes y nada más. Las definiciones de pasos están en un módulo único, y un guardián de integración continua falla si hay pasos indefinidos, ambiguos o definiciones sin uso. La tabla de ejemplos del escenario con esquema cubre los pares de los cuatro factores y una lista aparte de combinaciones sospechosas elegidas por el equipo.

## Ejemplo

Ejemplo de [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) (sección «Ejemplo mínimo»):

El escenario siguiente describe una entrega con retraso de un día y se verifica con una función. Antes de ejecutarlo, predice si el límite de 24 horas exactas da el mismo resultado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Todos los escenarios pasan y un defecto de frontera llega a producción** — causa: los ejemplos son del camino típico y no separan las lecturas. Corrección: elegir ejemplos por las variantes que matan y añadir fronteras (24 h, 25 h, tope, nota 0). ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))
- **Cada rediseño de la interfaz rompe veinte escenarios** — causa: los escenarios son imperativos y describen clics. Corrección: reescribirlos en lenguaje de dominio y mover el cómo a las definiciones de pasos. ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))
- **Los escenarios no se actualizaron tras un cambio de política** — causa: nadie era responsable de la documentación viva. Corrección: asignar un responsable y ejecutar los escenarios en cada cambio de regla. ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un escenario escrito solo por pruebas a partir de un documento no cumple esa función: transcribe una lectura. ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))
- La transferencia está lograda cuando puedes explicar qué parte del método dependía de la regla y cuál no, no cuando el formato de los escenarios se parece. ([SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ejemplos concretos](./ejemplos-concretos.md), [Contextos](../c/contextos.md), [Dominio](../d/dominio.md), [Resultado](../r/resultado.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Contribución única](../c/contribucion-unica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (253 clases más lo mencionan; las que más):

[SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-588](../../../classes/part-48-harness-y-agentic-engineering/se-588-proyecto-harness-minimo-gobernado-y-evaluado/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-433](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-433-modelos-de-calidad-y-atributos-medibles/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md), [SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cucumber: Better Gherkin](https://cucumber.io/docs/bdd/better-gherkin/) — guía para redactar escenarios declarativos y breves; autoridad: proyecto Cucumber.
- [Cucumber: Gherkin Reference](https://cucumber.io/docs/gherkin/reference/) — palabras clave y semántica de Gherkin; autoridad: proyecto Cucumber.
- [North, «Introducing BDD»](https://dannorth.net/introducing-bdd/) — origen del vocabulario de comportamiento; autoridad: autor del término.
- [Adzic, Specification by Example](https://gojko.net/books/specification-by-example/) — ejemplos colaborativos como especificación viva; autoridad: autor del libro.
- [NIST: Automated Combinatorial Testing for Software](https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software) — prueba combinatoria y cobertura de t-factores; autoridad: NIST.

---

[↑ Glosario](../../README.md) · [← Escape hatch y ownership](./escape-hatch-y-ownership.md) · [Escenario adverso →](./escenario-adverso.md)
