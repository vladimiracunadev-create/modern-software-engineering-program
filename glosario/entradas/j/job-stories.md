# Job stories

[↑ Glosario](../../README.md) · [← Job](./job.md) · [Journal y rollback →](./journal-y-rollback.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Una **job story** es un relato que parte de una situación, una motivación y un resultado esperado, sin depender de un rol ([SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md)). Es una alternativa a la historia de usuario cuando el rol no explica el comportamiento.

## Por qué importa

El mismo rol se comporta de formas muy distintas según la situación, y esa situación es lo que determina la necesidad. Una job story obliga a nombrar el desencadenante, la motivación y el resultado, en lugar de describir a un tipo de usuario. Cambia el punto de partida del requisito: la situación en lugar de la persona.

## Cómo funciona

La plantilla es «**Cuando** [situación], **quiero** [motivación], **para** [resultado esperado]». [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) da el ejemplo: «Cuando mi sesión expira mientras escribo, quiero recuperar lo que escribí para no repetir el trabajo». No dice «como estudiante»: el rol es irrelevante, porque lo mismo le ocurre a un docente que redacta un comentario.

Es útil en dos casos. Cuando el **rol no explica el comportamiento**: la misma estudiante se comporta distinto desde el móvil en el bus que desde un escritorio. Y cuando el **actor es el mismo en situaciones muy distintas**. Se relaciona con los trabajos por hacer (jobs to be done), de donde toma la idea de que la gente «contrata» un producto para progresar en una situación.

[SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) aclara sus límites: **no sustituye al caso de uso**, que dice quién interactúa con qué, paso a paso, con alternativas. Las tres formas del requisito conductor (caso de uso, historia de usuario y job story) responden a preguntas distintas: el caso de uso, qué pasos y qué alternativas; la historia, qué valor y para quién; la job story, en qué situación y por qué. Y no hay moda que seguir: para un sistema con roles bien separados y permisos distintos, la historia de usuario sigue siendo clara. La decisión es de claridad.

## Ejemplo

Historia de usuario: «Como estudiante quiero recuperar mi borrador para no perder mi trabajo». Job story: «Cuando mi sesión expira mientras escribo la entrega desde el móvil, quiero recuperar lo que escribí para no repetir el trabajo». La segunda incluye la situación (expiración, móvil) que orienta el diseño: guardado automático local y recuperación al volver a entrar. (Ejemplo derivado del de [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md).)

## Errores y confusiones comunes

- **Todas las historias empiezan con «Como usuario»**: no se definió el catálogo de actores; corrección: crear el catálogo con objetivo y contacto.
- **El caso de uso solo describe el camino feliz.**
- **Usar job stories como disfraz** de la misma historia con otro formato.
- **Omitir la motivación o el resultado.**

## Límites y cuándo no aplica

Cuando los permisos y funciones dependen del rol (administrar, calificar), el rol sí importa y la historia de usuario es más clara. [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) declara que no comparó la comprensión de las personas con cada forma de relato. Las job stories no incluyen criterios de aceptación; hay que añadirlos con ejemplos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Resultado](../r/resultado.md), [Actores y objetivos](../a/actores-y-objetivos.md), [Casos de uso](../c/casos-de-uso.md), [Corte vertical](../c/corte-vertical.md), [Historias de usuario](../h/historias-de-usuario.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md).

**Aparece en los casos de estudio:** [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Klement: Replacing the User Story with the Job Story](https://medium.com/@jtbd.info/replacing-the-user-story-with-the-job-story-af7cdee10c27) — propuesta de job stories; autoridad: autor de la propuesta.
- [Wake: INVEST in Good Stories, and SMART Tasks](https://xp123.com/articles/invest-in-good-stories-and-smart-tasks/) — criterios de una buena historia; autoridad: autor del acrónimo.
- [GOV.UK Service Manual: Writing user stories](https://www.gov.uk/service-manual/agile-delivery/writing-user-stories) — historias basadas en necesidades; autoridad: Government Digital Service.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) — información sobre conceptos de operación y requisitos de las partes interesadas; autoridad: ISO, IEC e IEEE.
- [Python: `itertools`](https://docs.python.org/3/library/itertools.html) — herramientas de enumeración.

---

[↑ Glosario](../../README.md) · [← Job](./job.md) · [Journal y rollback →](./journal-y-rollback.md)
