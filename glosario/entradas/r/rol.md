# Rol

[↑ Glosario](../../README.md) · [← Rojo, verde, refactor](./rojo-verde-refactor.md) · [Roofline →](./roofline.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Conjunto contextual de responsabilidades.

Definición de trabajo de [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md): Categoría semántica de un elemento (botón, enlace, campo de texto) que determina su comportamiento esperado.

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md):

Un **rol** agrupa responsabilidades necesarias en un contexto: quien facilita una retrospectiva o responde por un servicio puede cambiar sin que cambie su cargo. Una **especialidad** expresa profundidad de conocimiento y juicio. La **responsabilidad** se refiere a un resultado; la **autoridad**, a la capacidad legítima de decidir. Un cargo organizativo puede combinar varios roles o no describirlos con precisión.

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

Un `button` es enfocable, se activa con Intro y Espacio, anuncia su rol y su nombre y se desactiva con `disabled`. Un `a` con `href` navega y se abre en otra pestaña. Un `input` con `label` asocia el nombre al control. Todo esto viene sin escribir código. Imitarlo con un `div` obliga a reproducir el rol, el foco, las dos teclas y el estado, y es fácil olvidar uno. La primera regla de ARIA es la de no usar ARIA si un elemento nativo sirve.

## Ejemplo

Ejemplo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sección «Preguntas frecuentes»):

Se puede, y rara vez compensa: hay que reproducir rol, foco, dos teclas, estado y nombre, y cada navegador y lector los trata distinto. Un `button` ya lo trae y está probado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un control funciona con ratón y no con teclado** — causa: un div con clic sin foco ni teclas. Corrección: usar el elemento nativo o reproducir rol, foco y teclas. ([SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **rol** agrupa responsabilidades necesarias en un contexto: quien facilita una retrospectiva o responde por un servicio puede cambiar sin que cambie su cargo. ([SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Enlace](../e/enlace.md), [Responsabilidad](./responsabilidad.md), [Semántica](../s/semantica.md), [Enlace de salto](../e/enlace-de-salto.md), [Escalamiento](../e/escalamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-005 — Roles, especialidades y colaboración interdisciplinaria](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Comprender 4.1.2 Nombre, función, valor](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) — rol, nombre y estado de los componentes; autoridad: W3C.
- [W3C: Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) — cálculo del nombre accesible; autoridad: W3C.
- [W3C: ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — patrones de interacción y regla de usar HTML nativo primero; autoridad: W3C.
- [W3C: Comprender 2.1.1 Teclado](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) — funcionalidad operable con teclado; autoridad: W3C.
- [W3C: Comprender 2.4.3 Orden del foco](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden del foco con sentido; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Rojo, verde, refactor](./rojo-verde-refactor.md) · [Roofline →](./roofline.md)
