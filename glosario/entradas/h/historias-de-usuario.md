# Historias de usuario

[↑ Glosario](../../README.md) · [← Histograma](./histograma.md) · [HMAC →](./hmac.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Unidad de valor pequeña, negociable y comprobable, expresada como tarjeta, conversación y confirmación.

Definición de trabajo de [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md).

## Por qué importa

En [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), el tema «Historias de usuario» importa porque dividen el valor en incrementos pequeños que se negocian.

## Cómo funciona

Según [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), en la sección «Historias de usuario»:

Una historia es una unidad de valor lo bastante pequeña como para negociarse, estimarse y probarse. Su forma «como… quiero… para…» es una tarjeta; lo importante es la conversación que provoca y la confirmación (los criterios) que la cierra. INVEST resume qué se espera: independiente, negociable, valiosa, estimable, pequeña, comprobable. Una historia que no cumple «valiosa» (por ejemplo, «crear la tabla de borradores») es una tarea técnica; una que no cumple «pequeña» es un épico que todavía no se cortó.

## Ejemplo

Ejemplo de [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sección «Preguntas frecuentes»):

No necesariamente. Son útiles cuando el rol no explica el comportamiento o cuando el actor es el mismo en situaciones muy distintas. Para un sistema con roles bien separados y permisos distintos, la historia de usuario sigue siendo clara. La decisión es de claridad, no de moda.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md)) son:

- **Todas las historias empiezan con «Como usuario»** — causa: no se definió el catálogo de actores. Corrección: crear el catálogo con objetivo y contacto y exigir que cada historia nombre uno.
- **El caso de uso solo describe el camino feliz** — causa: las extensiones se consideraron «detalles». Corrección: enumerar las alternativas por paso y decidir cuáles se prueban.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún equipo, no se comparó la comprensión de personas con cada forma de relato y las capacidades e historias son supuestos del autor. La siguiente clase añade a cada historia los ejemplos concretos que permiten aceptar o rechazar el trabajo.

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
