# Anchura

[↑ Glosario](../../README.md) · [← Ancho en pantalla](./ancho-en-pantalla.md) · [Ancla →](./ancla.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Número de opciones que se ofrecen en un nivel de navegación.

Definición de trabajo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

## Por qué importa

En [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), el tema «Profundidad y anchura» importa porque fija cuántas decisiones toma una persona y cuántas opciones ve en cada una.

## Cómo funciona

Según [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

Un árbol de N destinos con b opciones por nivel tiene log_b(N) niveles. Menos niveles significa menos decisiones, pero más opciones por decisión, y esa anchura cuesta tiempo de elección (la ley de Hick: logarítmico en el número de opciones) y errores de lectura. Más niveles significa decisiones simples pero más oportunidades de equivocarse de rama, y el error se multiplica por nivel. El óptimo depende de cuánto crece el error con la anchura, que es un dato que hay que medir en el contenido real.

Según [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

Traslada el análisis a otra estructura (la ayuda de una aplicación bancaria o el catálogo de una tienda): calcula la anchura que minimiza el tiempo por éxito con un error que crece con las opciones y mide alcance y huérfanas de un grafo propio. La transferencia está lograda cuando puedes explicar qué parte dependía de la plataforma de entregas y cuál no.

## Ejemplo

Ejemplo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la profundidad de cada página con un recorrido en anchura sobre un grafo pequeño. Antes de ejecutarlo, predice cuál es la profundidad de `ayuda`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se elige la anchura por una regla de «tres clics»** — causa: no se midió el error por nivel. Corrección: medir el error con árboles reales y decidir con tiempo por éxito. ([SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El óptimo depende de cuánto crece el error con la anchura, que es un dato que hay que medir en el contenido real. ([SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Opción](../o/opcion.md), [Arquitectura de información](./arquitectura-de-informacion.md), [Ordenamiento de tarjetas](../o/ordenamiento-de-tarjetas.md), [Página huérfana](../p/pagina-huerfana.md), [Profundidad](../p/profundidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-051](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-051-conjuntos-relaciones-funciones-y-grafos/README.md), [SE-089](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md).

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

[↑ Glosario](../../README.md) · [← Ancho en pantalla](./ancho-en-pantalla.md) · [Ancla →](./ancla.md)
