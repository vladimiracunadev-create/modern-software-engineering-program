# Arquitectura de información

[↑ Glosario](../../README.md) · [← Arquitectura](./arquitectura.md) · [Arquitectura MooN →](./arquitectura-moon.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Organización, etiquetado y enlazado de la información para que las personas la encuentren y la entiendan.

Definición de trabajo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

## Por qué importa

La clase donde se define, [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), existe con este propósito: la clase existe para que decidas cómo se agrupa, nombra y enlaza la información de modo que una persona encuentre lo que busca y sepa dónde está, y para que midas esa decisión en vez de defenderla por intuición.

## Cómo funciona

[SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

En la plataforma, el equipo mantiene el esquema de información como un archivo de agrupaciones y etiquetas con la evidencia que las respalda (un ordenamiento de tarjetas abierto con participantes voluntarios, una prueba de hallazgo con tareas concretas). El grafo de enlaces se genera en cada despliegue, y una comprobación falla si aparece una página sin enlace entrante o si el alcance desde la portada baja del 100 %. Las etiquetas nuevas pasan por una revisión de personas ajenas al equipo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md)) son:

- **La gente pregunta por soporte dónde está algo que existe** — causa: etiqueta propia del equipo o agrupación por organigrama. Corrección: ordenamiento de tarjetas y prueba de hallazgo con etiquetas alternativas.
- **Una sección desaparece de la navegación tras un cambio** — causa: se movió el contenido sin comprobar alcance. Corrección: comprobar alcance y huérfanas en cada despliegue.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se hizo un ordenamiento de tarjetas con personas, no se usó ninguna herramienta de análisis de sitios y el error por nivel, el ruido y el grafo son supuestos del autor. La siguiente clase pregunta cómo debe responder cada control cuando alguien lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Organización](../o/organizacion.md), [Anchura](./anchura.md), [Ordenamiento de tarjetas](../o/ordenamiento-de-tarjetas.md), [Página huérfana](../p/pagina-huerfana.md), [Profundidad](../p/profundidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Nielsen Norman Group: 10 heurísticas de usabilidad](https://www.nngroup.com/articles/ten-usability-heuristics/) — correspondencia con el lenguaje de la persona y visibilidad del estado; autoridad: Nielsen Norman Group.
- [Hick, «On the rate of gain of information» (QJEP, 1952)](https://doi.org/10.1080/17470215208416600) — tiempo de elección y número de alternativas; autoridad: Quarterly Journal of Experimental Psychology.
- [Miller, «The magical number seven, plus or minus two» (Psychological Review, 1956)](https://doi.org/10.1037/h0043158) — límites de capacidad de procesamiento; autoridad: Psychological Review.
- [Nielsen Norman Group: cuántos participantes en un ordenamiento de tarjetas](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/) — criterio práctico de tamaño de muestra; autoridad: Nielsen Norman Group.
- [W3C: WCAG 2.2, 2.4.1 Evitar bloques](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html) — saltar contenido repetido en la navegación; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Arquitectura](./arquitectura.md) · [Arquitectura MooN →](./arquitectura-moon.md)
