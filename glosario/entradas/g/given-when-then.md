# Given-When-Then

[↑ Glosario](../../README.md) · [← GitOps](./gitops.md) · [Glosario →](./glosario.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

**Given-When-Then** (Dado–Cuando–Entonces) es una forma de escribir un ejemplo como contexto, acción y resultado observable ([SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md)). Es la estructura de los escenarios del lenguaje Gherkin y de la especificación por ejemplos.

## Por qué importa

Estructura el ejemplo y permite automatizarlo. Un escenario escrito así lo puede leer una persona no técnica y ejecutar una herramienta. Cambia cómo se redactan los criterios de aceptación: de frases generales a escenarios concretos con un resultado verificable.

## Cómo funciona

La forma separa tres partes:

- **Dado** (el contexto): lo que ya era verdad, por ejemplo «una estudiante con sesión válida y un archivo de 10,1 MB».
- **Cuando** (la acción): lo que ocurre, «intenta entregarlo».
- **Entonces** (el resultado observable): lo que debe observarse, «ve el mensaje del límite y la entrega no se guarda».

[SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md) subraya que la utilidad **no es sintáctica**: obliga a separar lo que ya era verdad de lo que ocurre y de lo que debe observarse. Un escenario con dos acciones o con una verificación en el contexto suele indicar que son dos escenarios. Los pasos se redactan en el **lenguaje del dominio** («la entrega llega 30 horas tarde»), no en el de la interfaz.

Gherkin lo hace ejecutable: cada paso se vincula con código que prepara el contexto, ejecuta la acción y comprueba el resultado. Su riesgo, dice [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), es la **verbosidad**: escenarios que describen la interfaz clic por clic en lugar del comportamiento se rompen con cada cambio visual y nadie los mantiene. La corrección es escribir el comportamiento de negocio y dejar el detalle de interfaz para la implementación de los pasos.

Los escenarios sirven de criterios de aceptación y de fuente de casos de prueba. Los que se eligen deben incluir los **valores de frontera** (10 MB y 10,1 MB), no solo el camino típico.

## Ejemplo

```gherkin
Escenario: Archivo por encima del límite
  Dado una estudiante con sesión válida
  Y un archivo PDF de 10,1 MB
  Cuando intenta entregarlo
  Entonces ve un mensaje que indica el límite de 10 MB
  Y la entrega no se guarda
```

Un escenario gemelo con un archivo de exactamente 10 MB y resultado «la entrega se guarda» fija la frontera. (Escenario ilustrativo basado en el ejemplo de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).)

## Errores y confusiones comunes

- **Las pruebas pasan y el cliente rechaza la entrega**: el criterio solo cubría ejemplos felices; corrección: añadir ejemplos en las fronteras y en clases no válidas.
- **Describir la interfaz clic por clic.**
- **Varias acciones en un escenario.**
- **Confundir la forma con el valor**: escribirlo en Gherkin no mejora un ejemplo mal elegido.

## Límites y cuándo no aplica

Para reglas con muchas combinaciones, una tabla de decisión es más compacta que decenas de escenarios. El mantenimiento de las definiciones de pasos es un costo real. Si nadie de negocio lee los escenarios, parte de su valor se pierde, y entonces puede bastar con pruebas automáticas normales.

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
