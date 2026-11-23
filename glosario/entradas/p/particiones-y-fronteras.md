# Particiones y fronteras

[↑ Glosario](../../README.md) · [← Partición de red](./particion-de-red.md) · [Partida doble →](./partida-doble.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Agrupación de entradas en clases tratadas igual y elección de valores en el borde de cada clase.

Definición de trabajo de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

## Por qué importa

En [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el tema «Particiones y fronteras» importa porque guían qué ejemplos tienen más probabilidad de revelar un defecto.

## Cómo funciona

Según [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), en la sección «Particiones y fronteras»:

Las clases de equivalencia agrupan entradas que el sistema debería tratar igual (archivos válidos, demasiado grandes, de extensión no permitida); basta un representante por clase si la partición es correcta. Los valores límite se eligen en el borde de cada clase (10,0 y 10,1 MB, 0 y 0,1 MB, nombres de 50 y 51 caracteres), porque los errores de «menor que» frente a «menor o igual» viven allí. Una partición incorrecta (suponer que `.PDF` y `.pdf` son la misma clase) produce un representante que no representa.

## Ejemplo

Caso medido en la sección «Particiones y fronteras» de [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md):

Las clases de equivalencia agrupan entradas que el sistema debería tratar igual (archivos válidos, demasiado grandes, de extensión no permitida); basta un representante por clase si la partición es correcta. Los valores límite se eligen en el borde de cada clase (10,0 y 10,1 MB, 0 y 0,1 MB, nombres de 50 y 51 caracteres), porque los errores de «menor que» frente a «menor o igual» viven allí. Una partición incorrecta (suponer que `.PDF` y `.pdf` son la misma clase) produce un representante que no representa.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son:

- **Las pruebas pasan y el cliente rechaza la entrega** — causa: el criterio solo cubría ejemplos felices. Corrección: añadir ejemplos en las fronteras y en las clases no válidas.
- **Dos personas aplican la regla de redondeo de forma distinta** — causa: no hay ejemplo en el empate. Corrección: añadir el ejemplo y registrar quién decidió la regla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. Los mutantes, las fallas sembradas y las notas son supuestos del autor, la suite de pares se obtuvo con un algoritmo voraz propio y no se probó ningún sistema real. La siguiente clase ordena el conjunto de historias teniendo en cuenta sus dependencias y las negociaciones entre interesados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agrupación](../a/agrupacion.md), [Borde](../b/borde.md), [Valor](../v/valor.md), [Cobertura combinatoria](../c/cobertura-combinatoria.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Ejemplos concretos](../e/ejemplos-concretos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-149 — Criterios de aceptación y ejemplos](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-069](../../../classes/part-05-fundamentos-de-programacion/se-069-pruebas-tempranas-y-diseno-por-ejemplos/README.md).

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

[↑ Glosario](../../README.md) · [← Partición de red](./particion-de-red.md) · [Partida doble →](./partida-doble.md)
