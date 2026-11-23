# Ordenamiento de tarjetas

[↑ Glosario](../../README.md) · [← Orden, duplicados e idempotencia](./orden-duplicados-e-idempotencia.md) · [Organización →](./organizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Técnica en la que participantes agrupan tarjetas con conceptos y revelan cómo los organizan.

Definición de trabajo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

## Por qué importa

La clase donde se define, [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), existe con este propósito: la clase existe para que decidas cómo se agrupa, nombra y enlaza la información de modo que una persona encuentre lo que busca y sepa dónde está, y para que midas esa decisión en vez de defenderla por intuición.

## Cómo funciona

Según [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

Una agrupación responde a un modelo mental y una etiqueta es la promesa de qué hay detrás. Las dos fallan de modos distintos: una agrupación por el organigrama interno separa lo que la persona junta, y una etiqueta propia del equipo («Gestión de artefactos») no se entiende sin su contexto. Un ordenamiento de tarjetas abierto muestra cómo agrupa la gente y un ordenamiento cerrado comprueba si una estructura propuesta encaja. Ninguno decide por sí solo: aporta evidencia que se combina con restricciones de negocio.

Según [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

En la plataforma, el equipo mantiene el esquema de información como un archivo de agrupaciones y etiquetas con la evidencia que las respalda (un ordenamiento de tarjetas abierto con participantes voluntarios, una prueba de hallazgo con tareas concretas). El grafo de enlaces se genera en cada despliegue, y una comprobación falla si aparece una página sin enlace entrante o si el alcance desde la portada baja del 100 %. Las etiquetas nuevas pasan por una revisión de personas ajenas al equipo.

## Ejemplo

Ejemplo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sección «Ejemplo profesional»):

En la plataforma, el equipo mantiene el esquema de información como un archivo de agrupaciones y etiquetas con la evidencia que las respalda (un ordenamiento de tarjetas abierto con participantes voluntarios, una prueba de hallazgo con tareas concretas). El grafo de enlaces se genera en cada despliegue, y una comprobación falla si aparece una página sin enlace entrante o si el alcance desde la portada baja del 100 %. Las etiquetas nuevas pasan por una revisión de personas ajenas al equipo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La gente pregunta por soporte dónde está algo que existe** — causa: etiqueta propia del equipo o agrupación por organigrama. Corrección: ordenamiento de tarjetas y prueba de hallazgo con etiquetas alternativas. ([SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se hizo un ordenamiento de tarjetas con personas, no se usó ninguna herramienta de análisis de sitios y el error por nivel, el ruido y el grafo son supuestos del autor. La siguiente clase pregunta cómo debe responder cada control cuando alguien lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Anchura](../a/anchura.md), [Arquitectura de información](../a/arquitectura-de-informacion.md), [Página huérfana](../p/pagina-huerfana.md), [Profundidad](../p/profundidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nielsen Norman Group: cuántos participantes en un ordenamiento de tarjetas](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/) — criterio práctico de tamaño de muestra; autoridad: Nielsen Norman Group.
- [Nielsen Norman Group: 10 heurísticas de usabilidad](https://www.nngroup.com/articles/ten-usability-heuristics/) — correspondencia con el lenguaje de la persona y visibilidad del estado; autoridad: Nielsen Norman Group.
- [Hick, «On the rate of gain of information» (QJEP, 1952)](https://doi.org/10.1080/17470215208416600) — tiempo de elección y número de alternativas; autoridad: Quarterly Journal of Experimental Psychology.
- [Miller, «The magical number seven, plus or minus two» (Psychological Review, 1956)](https://doi.org/10.1037/h0043158) — límites de capacidad de procesamiento; autoridad: Psychological Review.
- [W3C: WCAG 2.2, 2.4.1 Evitar bloques](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html) — saltar contenido repetido en la navegación; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Orden, duplicados e idempotencia](./orden-duplicados-e-idempotencia.md) · [Organización →](./organizacion.md)
