# Historias de usuario

[↑ Glosario](../../README.md) · [← Histograma](./histograma.md) · [HMAC →](./hmac.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Una **historia de usuario** es una unidad de valor pequeña, negociable y comprobable, expresada como tarjeta, conversación y confirmación ([SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md)). La tarjeta es la frase corta «como… quiero… para…»; la conversación es el diálogo que provoca; la confirmación son los criterios que la cierran.

## Por qué importa

Divide el valor en incrementos que se pueden negociar, estimar y probar. Cambia cómo se planifica: en lugar de especificar todo por adelantado, se trabaja con piezas pequeñas cuyo detalle se acuerda cuando toca construirlas. Lo importante, dice [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), no es la plantilla de la tarjeta sino la conversación que provoca.

## Cómo funciona

El criterio de calidad más extendido es INVEST: independiente, negociable, valiosa, estimable, pequeña, comprobable. [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) lo usa para decidir si algo es una historia. Una que no cumple «valiosa» (por ejemplo, «crear la tabla de borradores») es una tarea técnica: no tiene valor visible para quien la pidió. Una que no cumple «pequeña» es un épico que todavía no se cortó.

La causa de que funcione es que la tarjeta es deliberadamente incompleta: obliga a conversar, y esa conversación hace aparecer lo que un documento exhaustivo escondería. Se cierra con la confirmación: los criterios de aceptación, preferiblemente como ejemplos ([SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md)). Y se corta en vertical (corte vertical), de modo que cada historia atraviese las capas y pueda mostrarse.

[SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) distingue historias de otras formas de contar un requisito: casos de uso (con actor, escenario principal y extensiones) y job stories (centradas en la situación y la motivación, no en el rol). Las job stories son útiles cuando el rol no explica el comportamiento o cuando el mismo actor está en situaciones muy distintas; para un sistema con roles bien separados y permisos distintos, la historia de usuario sigue siendo clara. La decisión es de claridad, no de moda.

## Ejemplo

En la plataforma de entregas: «Como estudiante, quiero subir mi entrega en PDF, para que quede registrada antes del plazo». La conversación aclara el tamaño máximo y qué ocurre tras el plazo; la confirmación se escribe como ejemplos: un PDF de 10 MB se acepta y uno de 10,1 MB se rechaza con un mensaje que indica el límite. (La historia es una ilustración; el límite viene de [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).)

## Errores y confusiones comunes

- **Todas las historias empiezan con «Como usuario»**: no se definió el catálogo de actores; corrección: crear el catálogo con objetivo y contacto y exigir que cada historia nombre uno.
- **El caso de uso solo describe el camino feliz**: las extensiones se consideraron detalles.
- **Historias como tareas técnicas** sin valor visible.
- **Tomar la tarjeta por la especificación**: la tarjeta recuerda una conversación; no la reemplaza.

## Límites y cuándo no aplica

Las historias son poco adecuadas para requisitos transversales (rendimiento, seguridad) que no encajan en un incremento de usuario; esos se expresan como escenarios de calidad. Cuando hay obligaciones legales o contratos que exigen especificación detallada y trazable, las historias solas no bastan. [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) declara que no se midió ningún equipo ni se comparó la comprensión de las personas con cada forma de relato.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confirmación](../c/confirmacion.md), [Valor](../v/valor.md), [Actores y objetivos](../a/actores-y-objetivos.md), [Casos de uso](../c/casos-de-uso.md), [Corte vertical](../c/corte-vertical.md), [Job stories](../j/job-stories.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-567](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-567-implementacion-analisis-y-convergencia-contra-spec/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Wake: INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) — criterios de una buena historia; autoridad: autor del acrónimo.
- [Klement: Replacing the User Story with the Job Story](https://medium.com/@jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27) — propuesta de job stories; autoridad: autor de la propuesta.
- [GOV.UK Service Manual: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories) — historias basadas en necesidades; autoridad: Government Digital Service.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — información sobre conceptos de operación y requisitos de las partes interesadas; autoridad: ISO, IEC e IEEE.
- [Python: `itertools`](https://docs.python.org/3/library/itertools.html) — herramientas de enumeración.

---

[↑ Glosario](../../README.md) · [← Histograma](./histograma.md) · [HMAC →](./hmac.md)
