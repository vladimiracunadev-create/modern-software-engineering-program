# Profundidad

[↑ Glosario](../../README.md) · [← Producto operable](./producto-operable.md) · [Programa de experimentos →](./programa-de-experimentos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Número de niveles o clics entre un punto de partida y una página.

Definición de trabajo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md).

## Por qué importa

En [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), el tema «Profundidad y anchura» importa porque fija cuántas decisiones toma una persona y cuántas opciones ve en cada una.

## Cómo funciona

Según [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md):

Se generó un sitio de 120 páginas con una semilla: un árbol de contenido, 8 secciones enlazadas desde la portada y un 30 % de enlaces cruzados. Con el menú global, un recorrido en anchura desde la portada alcanza las 120 páginas, con 17, 47, 41 y 14 páginas a 1, 2, 3 y 4 clics. Sin el menú global, se alcanzan las mismas 120, pero la profundidad llega a 9 clics. Desde una página interna con un enlace a la portada en todas las páginas se llega a las 120 en 5 clics como máximo; sin ese enlace, solo a 16 de 120 (13 %).

## Ejemplo

Ejemplo de [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la profundidad de cada página con un recorrido en anchura sobre un grafo pequeño. Antes de ejecutarlo, predice cuál es la profundidad de `ayuda`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md)) son:

- **La gente pregunta por soporte dónde está algo que existe** — causa: etiqueta propia del equipo o agrupación por organigrama. Corrección: ordenamiento de tarjetas y prueba de hallazgo con etiquetas alternativas.
- **Una sección desaparece de la navegación tras un cambio** — causa: se movió el contenido sin comprobar alcance. Corrección: comprobar alcance y huérfanas en cada despliegue.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin el menú global, se alcanzan las mismas 120, pero la profundidad llega a 9 clics. ([SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Página](./pagina.md), [Anchura](../a/anchura.md), [Arquitectura de información](../a/arquitectura-de-informacion.md), [Ordenamiento de tarjetas](../o/ordenamiento-de-tarjetas.md), [Página huérfana](./pagina-huerfana.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-170 — Arquitectura de información y navegación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (55 clases más lo mencionan; las que más):

[SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-538](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-538-portafolio-entrevistas-y-defensa-profesional/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md), [SE-063](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md), [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Producto operable](./producto-operable.md) · [Programa de experimentos →](./programa-de-experimentos.md)
