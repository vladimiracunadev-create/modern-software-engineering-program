# Ejemplos concretos

[↑ Glosario](../../README.md) · [← Ejemplo ejecutable](./ejemplo-ejecutable.md) · [Ejercicio de mesa →](./ejercicio-de-mesa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Casos con datos específicos que ilustran una regla y permiten distinguir interpretaciones.

Definición de trabajo de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Por qué importa

En [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el tema «Ejemplos concretos» importa porque anclan una regla abstracta en casos que distinguen implementaciones.

## Cómo funciona

Según [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), en la sección «Ejemplos concretos»:

Una regla abstracta («el archivo no debe exceder el límite») admite lecturas distintas; un ejemplo la ancla («10,0 MB se acepta; 10,1 MB se rechaza»). Example Mapping organiza la conversación en cuatro tipos de tarjeta: la historia, las reglas, los ejemplos que las ilustran y las preguntas sin respuesta. Si hay muchas preguntas, la historia aún no está lista; si hay muchas reglas, es demasiado grande. Los ejemplos son la parte que sobrevive: se convierten en pruebas y, con los años, en documentación viva.

## Ejemplo

Caso medido en la sección «Ejemplos concretos» de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md):

Una regla abstracta («el archivo no debe exceder el límite») admite lecturas distintas; un ejemplo la ancla («10,0 MB se acepta; 10,1 MB se rechaza»). Example Mapping organiza la conversación en cuatro tipos de tarjeta: la historia, las reglas, los ejemplos que las ilustran y las preguntas sin respuesta. Si hay muchas preguntas, la historia aún no está lista; si hay muchas reglas, es demasiado grande. Los ejemplos son la parte que sobrevive: se convierten en pruebas y, con los años, en documentación viva.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son:

- **Las pruebas pasan y el cliente rechaza la entrega** — causa: el criterio solo cubría ejemplos felices. Corrección: añadir ejemplos en las fronteras y en las clases no válidas.
- **Dos personas aplican la regla de redondeo de forma distinta** — causa: no hay ejemplo en el empate. Corrección: añadir el ejemplo y registrar quién decidió la regla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los mutantes, las fallas sembradas y las notas son supuestos del autor, la suite de pares se obtuvo con un algoritmo voraz propio y no se probó ningún sistema real. La siguiente clase ordena el conjunto de historias teniendo en cuenta sus dependencias y las negociaciones entre interesados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interpretación](../i/interpretacion.md), [Regla](../r/regla.md), [Cobertura combinatoria](../c/cobertura-combinatoria.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Given-When-Then](../g/given-when-then.md), [Particiones y fronteras](../p/particiones-y-fronteras.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-544](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-545](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-545-atdd-y-specification-by-example-aceptacion-ejecutable/README.md), [SE-060](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-060-proyecto-especificacion-y-solucion-contrastable/README.md), [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md), [SE-346](../../../classes/part-28-estilos-arquitectonicos/se-346-evolucion-y-migracion-entre-estilos/README.md).

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

[↑ Glosario](../../README.md) · [← Ejemplo ejecutable](./ejemplo-ejecutable.md) · [Ejercicio de mesa →](./ejercicio-de-mesa.md)
