# Given-When-Then

[↑ Glosario](../../README.md) · [← GitOps](./gitops.md) · [Glosario →](./glosario.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Forma de escribir un ejemplo como contexto, acción y resultado observable.

Definición de trabajo de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Por qué importa

En [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el tema «Given-When-Then» importa porque estructura el ejemplo en contexto, acción y resultado y permite automatizarlo.

En [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), el tema «Given-When-Then» importa porque la estructura separa contexto, acción y resultado observable y hace que el escenario sea revisable por personas no técnicas.

## Cómo funciona

Según [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), en la sección «Given-When-Then»:

La forma Dado–Cuando–Entonces separa el contexto (dado una estudiante con sesión válida y un archivo de 10,1 MB), la acción (cuando intenta entregarlo) y el resultado observable (entonces ve el mensaje del límite y la entrega no se guarda). Gherkin la hace ejecutable. Su riesgo es la verbosidad: escenarios que describen la interfaz clic por clic en lugar del comportamiento se rompen con cada cambio visual y no aportan información.

Según [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), en la sección «Given-When-Then»:

La estructura de Gherkin ordena un escenario en contexto (`Dado`), acción (`Cuando`) y resultado observable (`Entonces`). La utilidad no es sintáctica: obliga a separar lo que ya era verdad de lo que ocurre y de lo que debe observarse. Un escenario con dos acciones o con una verificación en el contexto suele indicar que son dos escenarios. Los pasos se redactan en el lenguaje del dominio («la entrega llega 30 horas tarde») y se emparejan con código mediante expresiones; esa separación permite que cambie la implementación sin tocar el texto.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md):

Los criterios de H-12 en forma de escenarios, cada uno con su regla de origen:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son:

- **Las pruebas pasan y el cliente rechaza la entrega** — causa: el criterio solo cubría ejemplos felices. Corrección: añadir ejemplos en las fronteras y en las clases no válidas.
- **Dos personas aplican la regla de redondeo de forma distinta** — causa: no hay ejemplo en el empate. Corrección: añadir el ejemplo y registrar quién decidió la regla.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los mutantes, las fallas sembradas y las notas son supuestos del autor, la suite de pares se obtuvo con un algoritmo voraz propio y no se probó ningún sistema real. La siguiente clase ordena el conjunto de historias teniendo en cuenta sus dependencias y las negociaciones entre interesados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Resultado](../r/resultado.md), [Cobertura combinatoria](../c/cobertura-combinatoria.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Ejemplo como especificación](../e/ejemplo-como-especificacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-158 — Specification by Example y BDD](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Cucumber: Gherkin reference](https://cucumber.io/docs/gherkin/reference/) — sintaxis de Given, When y Then; autoridad: proyecto Cucumber.
- [Cucumber: Example Mapping](https://cucumber.io/blog/bdd/example-mapping-introduction/) — conversación estructurada de reglas y ejemplos; autoridad: proyecto Cucumber.
- [North: Introducing BDD](https://dannorth.net/introducing-bdd/) — origen del desarrollo guiado por comportamiento; autoridad: autor de la técnica.
- [NIST SP 800-142: Practical Combinatorial Testing](https://csrc.nist.gov/pubs/sp/800/142/final) — pruebas combinatorias; autoridad: NIST.
- [Python: `round`](https://docs.python.org/3/library/functions.html#round) — redondeo al par más cercano.

---

[↑ Glosario](../../README.md) · [← GitOps](./gitops.md) · [Glosario →](./glosario.md)
