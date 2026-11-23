# Casos de uso

[↑ Glosario](../../README.md) · [← Caso mínimo y representatividad](./caso-minimo-y-representatividad.md) · [Casos límite y oráculo →](./casos-limite-y-oraculo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Narración de cómo un actor alcanza un objetivo, con flujo principal, extensiones y resultado garantizado.

Definición de trabajo de [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md).

## Por qué importa

En [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), el tema «Casos de uso» importa porque muestran secuencias, variantes y fallos con alcance completo.

## Cómo funciona

Según [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), en la sección «Casos de uso»:

Un caso de uso narra cómo un actor alcanza un objetivo con el sistema: precondiciones, flujo principal numerado, extensiones (variantes que vuelven al flujo o lo terminan) y resultado garantizado. Su valor es la exhaustividad: obliga a preguntar qué pasa si el archivo es demasiado grande, si el plazo venció, si la sesión expira a mitad. Su costo es el tamaño: cada extensión multiplica o suma caminos, y no todos merecen el mismo detalle.

## Ejemplo

Ejemplo de [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) (sección «Preguntas frecuentes»):

No. Cada uno responde una pregunta distinta: el caso de uso, qué secuencia y qué variantes; la historia, qué incremento de valor; la job story, qué situación lo desencadena. Para un requisito pequeño y bien entendido basta una historia con criterios. Escribe un caso de uso cuando las variantes y los fallos sean el riesgo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El caso de uso solo describe el camino feliz** — causa: las extensiones se consideraron «detalles». Corrección: enumerar las alternativas por paso y decidir cuáles se prueban. ([SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No sustituye al caso de uso: no dice qué pasa paso a paso ni cubre las variantes. ([SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md))
- Cada uno responde una pregunta distinta: el caso de uso, qué secuencia y qué variantes; la historia, qué incremento de valor; la job story, qué situación lo desencadena. ([SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Actor](../a/actor.md), [Extensión](../e/extension.md), [Flujo](../f/flujo.md), [Principal](../p/principal.md), [Actores y objetivos](../a/actores-y-objetivos.md), [Corte vertical](./corte-vertical.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-148 — Casos de uso, historias y job stories](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-317](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-317-grasp-y-asignacion-de-responsabilidades/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

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

[↑ Glosario](../../README.md) · [← Caso mínimo y representatividad](./caso-minimo-y-representatividad.md) · [Casos límite y oráculo →](./casos-limite-y-oraculo.md)
