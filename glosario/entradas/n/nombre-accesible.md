# Nombre accesible

[↑ Glosario](../../README.md) · [← Noindex](./noindex.md) · [Nonce →](./nonce.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Texto con el que una tecnología de apoyo anuncia un control, calculado a partir de sus atributos y contenido.

Definición de trabajo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md): Texto que una tecnología de apoyo anuncia para un control, derivado de su etiqueta, su `alt`, su contenido o un atributo ARIA.

## Por qué importa

La clase donde se define, [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), existe con este propósito: la clase existe para que construyas la interfaz con los elementos y atributos que expresan su significado, de modo que el teclado, el foco y las tecnologías de apoyo tengan algo fiable que usar, y para que midas lo que cuesta y lo que se rompe cuando se imita con elementos genéricos.

## Cómo funciona

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

Una tecnología de apoyo anuncia rol (qué es), nombre (cómo se llama) y valor o estado (en qué situación). El nombre accesible se calcula con un orden de prioridad: la relación `aria-labelledby`, el `aria-label`, la etiqueta nativa (`label`), el contenido y, como último recurso, el título; un `placeholder` no es una etiqueta fiable porque desaparece al escribir. Un control sin nombre se anuncia como «botón» o «cuadro de edición» y no dice para qué sirve.

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Ejemplo

Ejemplo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El lector anuncia «botón» sin más** — causa: falta nombre accesible. Corrección: texto visible, etiqueta nativa o `aria-label` si no hay otra opción. ([SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El nombre accesible se calcula con un orden de prioridad: la relación `aria-labelledby`, el `aria-label`, la etiqueta nativa (`label`), el contenido y, como último recurso, el título; un `placeholder` no es una etiqueta fiable porque desaparece al escribir. ([SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md))
- No: un validador comprueba que el documento sea conforme a la sintaxis, no que tenga etiquetas, encabezados con sentido ni nombres accesibles. ([SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Tecnología de apoyo](../t/tecnologia-de-apoyo.md).
- **Ver también:** [Atributo](../a/atributo.md), [Control](../c/control.md), [Etiqueta](../e/etiqueta.md), [Capa de cascada](../c/capa-de-cascada.md), [Elemento semántico](../e/elemento-semantico.md), [Enlace de salto](../e/enlace-de-salto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Accessible Name and Description Computation 1.2](https://www.w3.org/TR/accname-1.2/) — cálculo del nombre accesible; autoridad: W3C.
- [W3C: ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — patrones de interacción y regla de usar HTML nativo primero; autoridad: W3C.
- [W3C: Comprender 2.1.1 Teclado](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) — funcionalidad operable con teclado; autoridad: W3C.
- [W3C: Comprender 2.4.3 Orden del foco](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden del foco con sentido; autoridad: W3C.
- [W3C: Comprender 4.1.2 Nombre, función, valor](https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html) — rol, nombre y estado de los componentes; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Noindex](./noindex.md) · [Nonce →](./nonce.md)
