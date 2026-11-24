# Cobertura combinatoria

[↑ Glosario](../../README.md) · [← Cobertura](./cobertura.md) · [Cobertura con umbral →](./cobertura-con-umbral.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

La **cobertura combinatoria** (de fuerza *t*) es la propiedad de un conjunto de casos de prueba por la cual cada combinación de *t* valores de factores distintos aparece al menos una vez. Es el sentido de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md). Con *t* = 2 se habla de cobertura de pares: no se prueban todas las combinaciones de todos los factores, sino todas las de cada par.

## Por qué importa

Cambia cuántas pruebas se escriben cuando intervienen muchos factores (rol, navegador, idioma, conexión, tipo de archivo, tamaño). Según [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el producto completo crece de forma multiplicativa y se vuelve impracticable; una suite de pares lo reduce a un orden de magnitud manejable sin renunciar a las interacciones más probables.

## Cómo funciona

Con *t* = 2, el número de casos necesario crece aproximadamente como el producto de los dos dominios más grandes, no de todos. Así, seis factores con varios valores cada uno pasan de miles de combinaciones a algunas decenas. Se construye con un algoritmo de generación; en [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) la suite de pares se obtuvo con un algoritmo voraz propio, que en cada paso elige el caso que cubre más pares aún no cubiertos.

El fundamento empírico es que la evidencia recopilada por NIST sugiere que la mayoría de las fallas dependen de pocos factores. La clase subraya la salvedad: «la mayoría» no es «todas». Una falla que exige tres valores simultáneos puede escapar de una suite de pares, y entonces se sube a *t* = 3 con un costo mayor.

## Ejemplo

En la plataforma de entregas de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), el criterio de aceptación de la subida de archivos depende del rol, el tipo de archivo, el tamaño y la conexión. Probar el producto completo no es práctico; una suite de pares garantiza que cada pareja (por ejemplo, «docente» con «archivo grande») se ejerce al menos una vez. La clase la contrasta con un registro de mutantes y fallas sembradas para ver cuáles detecta, y se declara que esos mutantes y notas son supuestos del autor.

## Errores y confusiones comunes

- **Creer que pares detectan todo.** Una falla de tres factores puede escapar.
- **Confundir cobertura combinatoria con cobertura de código.** Una mide combinaciones de entradas; la otra, líneas o ramas ejecutadas.
- **Elegir mal los valores.** Sin fronteras ni clases no válidas, la suite cubre pares de valores felices.
- **Pruebas que pasan y el cliente rechaza la entrega.** El criterio solo cubría ejemplos felices; corrección de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md): añadir fronteras y clases no válidas.

## Límites y cuándo no aplica

No ayuda con factores que no son discretos o independientes (restricciones entre valores deben declararse, o se generan casos imposibles). Con pocos factores, probar el producto completo es más simple. Y los resultados de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md) vienen de datos sintéticos y de un sistema de juguete: no demuestran eficacia en un sistema real. La técnica reduce número de casos; no dice si cada caso tiene un buen oráculo.

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
