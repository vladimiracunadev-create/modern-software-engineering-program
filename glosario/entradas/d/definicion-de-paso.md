# Definición de paso

[↑ Glosario](../../README.md) · [← Definición de listo](./definicion-de-listo.md) · [Definición de terminado →](./definicion-de-terminado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Enlace entre una frase de un escenario y el código que la ejecuta.

Definición de trabajo de [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md).

## Por qué importa

En [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md), el tema «Definiciones de paso» importa porque reutilizarlas reduce costo; abusar de la reutilización oculta el significado.

## Cómo funciona

Según [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md):

Cada paso de un escenario se enlaza con código mediante una **definición de paso**, que en el laboratorio es una expresión regular y una función. «El reloj marca la hora 76» se enlaza con una función que llama al servicio con esa hora. Las definiciones se reutilizan: nueve escenarios con 32 pasos necesitan solo 10 definiciones, 3,2 pasos por definición. La reutilización tiene un límite: una definición con demasiados parámetros opcionales deja de significar algo y el escenario se lee peor que el código.

Según [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md):

Antes de implementar el silencio, el equipo hace una sesión de descubrimiento de media hora con una docente. Sobre una pared de papel pone la regla («un curso silenciado no recibe avisos molestos»), un ejemplo por situación (el de 72 horas, el de 24, el de la última hora, otro curso, un estudiante con dos cursos) y una pregunta abierta («¿el silencio vale para siempre o hasta el vencimiento?»). La docente descubre que el silencio por defecto debería terminar con la entrega. Ese descubrimiento no estaba en ninguna especificación previa. Se formulan siete escenarios, uno por ejemplo, y se acuerda con ella que el de la última hora se mantiene aunque el curso esté silenciado.

## Ejemplo

Ejemplo de [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) (sección «Ejemplo mínimo»):

Tres definiciones de paso bastan: una crea la entrega, otra llama al servicio con la hora y otra compara el resultado con la lista vacía. El escenario mata un solo mutante, el que invierte el signo del tiempo restante: a la hora 101 el tiempo restante es −1 y con el signo invertido sería 1, así que el servicio avisaría. No mata `remaining < 0` (con −1 ambos se comportan igual). Es poco, y por eso su valor está en la documentación: el negocio lee la regla con sus palabras.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md)) son: El ejecutor es un intérprete mínimo y los escenarios y mutantes son del autor; no se midió ninguna sesión de descubrimiento con personas ni el efecto de BDD en defectos. El siguiente paso, `SE-545`, trata la pregunta que queda: qué ejemplos elegir, porque más ejemplos no es mejor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-543](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-543-tdd-en-la-practica-escuelas-de-londres-y-clasica-y-sus-limites/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](../e/enlace.md), [Escenario](../e/escenario.md), [Contribución única](../c/contribucion-unica.md), [Descubrimiento, formulación, automatización](./descubrimiento-formulacion-automatizacion.md), [Documentación viva](./documentacion-viva.md), [Escenario decorativo](../e/escenario-decorativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-544 — BDD: ejemplos, conversación y lenguaje compartido](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-544-bdd-ejemplos-conversacion-y-lenguaje-compartido/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Definiciones de paso».

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Definición de listo](./definicion-de-listo.md) · [Definición de terminado →](./definicion-de-terminado.md)
