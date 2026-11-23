# Descomponer la petición

[↑ Glosario](../../README.md) · [← Descarte de carga](./descarte-de-carga.md) · [Descomposición →](./descomposicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Separación de una petición en quién la hace, qué intenta lograr, qué hace hoy, qué consecuencia sufre y qué solución propone.

Definición de trabajo de [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md).

## Por qué importa

En [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), el tema «Descomponer la petición» importa porque una petición mezcla un actor, una intención, una solución y una consecuencia; separarlos revela qué falta.

## Cómo funciona

Según [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), en la sección «Descomponer la petición»:

«Un panel para ver quién no entregó» contiene un actor (docente), una solución (panel), una información deseada (quién no entregó) y una intención implícita (hacer algo con esa información). Lo que falta: qué hace hoy el docente con esa información, qué le cuesta, qué pasa si no la tiene y qué considera éxito. Descomponer no es cuestionar a la persona: es identificar qué partes son observación (tarda 40 minutos), cuáles son inferencia (quiere recordar a quienes no entregaron) y cuáles son solución (panel). Esas tres columnas ordenan la investigación.

## Ejemplo

Caso medido en la sección «Descomponer la petición» de [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md):

«Un panel para ver quién no entregó» contiene un actor (docente), una solución (panel), una información deseada (quién no entregó) y una intención implícita (hacer algo con esa información). Lo que falta: qué hace hoy el docente con esa información, qué le cuesta, qué pasa si no la tiene y qué considera éxito. Descomponer no es cuestionar a la persona: es identificar qué partes son observación (tarda 40 minutos), cuáles son inferencia (quiere recordar a quienes no entregaron) y cuáles son solución (panel). Esas tres columnas ordenan la investigación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)) son:

- **Los docentes dicen «sí» a todo y el panel no se usa** — causa: las preguntas eran guiadas o hipotéticas. Corrección: preguntar por episodios pasados concretos y revisar la guía con una segunda persona.
- **El backlog crece con peticiones que parecen distintas y resultan iguales** — causa: no se agruparon por necesidad. Corrección: agrupar por necesidad con criterio explícito y contar necesidades, no peticiones.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con peticiones, preguntas y enunciados sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. Las etiquetas son de una sola persona, las reglas se afinaron con pocos ejemplos y las pruebas con casos nuevos son de seis y tres elementos. El proyecto final reúne todo en un brief respaldado por evidencia.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consecuencia](../c/consecuencia.md), [Evidencia](../e/evidencia.md), [Agrupar por necesidad](../a/agrupar-por-necesidad.md), [Preguntas de investigación](../p/preguntas-de-investigacion.md), [Reformular como problema](../r/reformular-como-problema.md), [Rúbrica de investigabilidad](../r/rubrica-de-investigabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-131 — Taller: convertir una petición en un problema investigable](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — reformular una solución dada como problema; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) — formato y validación de necesidades; autoridad: Government Digital Service.
- [The Mom Test](https://www.momtestbook.com/) — preguntar por hechos pasados; autoridad: autor (guía práctica, no estudio empírico).
- [Nielsen Norman Group: User Interviews 101](https://www.nngroup.com/articles/user-interviews/) — introducción a la entrevista de usuario; autoridad: Nielsen Norman Group.
- [McHugh: Interrater reliability, the kappa statistic](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/) — kappa frente al acuerdo bruto; autoridad: revisión indexada en PubMed Central.

---

[↑ Glosario](../../README.md) · [← Descarte de carga](./descarte-de-carga.md) · [Descomposición →](./descomposicion.md)
