# Cobertura combinatoria

[↑ Glosario](../../README.md) · [← Cobertura](./cobertura.md) · [Cobertura con umbral →](./cobertura-con-umbral.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Conjunto de casos que garantiza que cada combinación de t valores aparece al menos una vez.

Definición de trabajo de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Por qué importa

En [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el tema «Cobertura combinatoria» importa porque reduce el número de combinaciones a probar cuando intervienen varios factores.

## Cómo funciona

Según [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), en la sección «Cobertura combinatoria»:

Cuando intervienen varios factores (rol, navegador, idioma, conexión, tipo de archivo, tamaño), el producto completo crece de forma multiplicativa. Las pruebas combinatorias de t factores garantizan que cada combinación de t valores aparece al menos una vez; con t = 2 (pares) el número de casos crece como el producto de los dos mayores dominios, no de todos. La evidencia empírica recopilada por NIST sugiere que la mayoría de las fallas dependen de pocos factores, pero «la mayoría» no es «todas»: una falla que exige tres valores simultáneos puede escapar.

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
- **Ver también:** [Al menos una vez](../a/al-menos-una-vez.md), [Combinación](./combinacion.md), [Conjunto](./conjunto.md), [Valor](../v/valor.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Ejemplos concretos](../e/ejemplos-concretos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

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

[↑ Glosario](../../README.md) · [← Cobertura](./cobertura.md) · [Cobertura con umbral →](./cobertura-con-umbral.md)
