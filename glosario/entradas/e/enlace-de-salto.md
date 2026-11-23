# Enlace de salto

[↑ Glosario](../../README.md) · [← Enlace](./enlace.md) · [Enlace frente a evidencia →](./enlace-frente-a-evidencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Enlace al principio de una página que lleva al contenido principal para evitar bloques repetidos.

Definición de trabajo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md).

## Por qué importa

La clase donde se define, [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), existe con este propósito: la clase existe para que construyas la interfaz con los elementos y atributos que expresan su significado, de modo que el teclado, el foco y las tecnologías de apoyo tengan algo fiable que usar, y para que midas lo que cuesta y lo que se rompe cuando se imita con elementos genéricos.

## Cómo funciona

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

Se modeló una página con 40 enlaces de navegación seguidos de un formulario con dos campos, un div con clic y un botón. El orden de foco se calculó con una regla simplificada: se incluyen los elementos nativos enfocables (enlaces con `href`, botones, campos), se excluyen los desactivados y los de `tabindex` negativo, y se ordena primero por `tabindex` positivo y luego por orden del documento. Llegar a «Enviar» cuesta 43 pulsaciones de Tab. Con un enlace de salto al contenido principal, 1 Tab, Intro y 3 Tab (5 pulsaciones). De 44 controles interactivos (con clic o nativos) solo 42 son alcanzables: los dos div no reciben foco.

Según [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Ejemplo

Ejemplo de [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sección «Ejemplo profesional»):

En la plataforma, cada componente tiene una ficha con su elemento nativo, su nombre accesible, su comportamiento de teclado y su gestión de foco; una prueba recorre el árbol de la página y falla si un control interactivo no tiene nombre, si un elemento con clic no es enfocable o si el orden de foco difiere del visual. Cada página lleva un enlace de salto, una región `main` y encabezados que reflejan la estructura; el modal de confirmación lleva el foco a su primer control, cierra con Escape y devuelve el foco a quien lo abrió.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md)) son:

- **Un control funciona con ratón y no con teclado** — causa: un div con clic sin foco ni teclas. Corrección: usar el elemento nativo o reproducir rol, foco y teclas.
- **El lector anuncia «botón» sin más** — causa: falta nombre accesible. Corrección: texto visible, etiqueta nativa o `aria-label` si no hay otra opción.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Las dos primeras barras comparan el costo con y sin enlace de salto; las dos últimas, los controles que existen y los que el teclado alcanza. ([SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](./enlace.md), [Página](../p/pagina.md), [Principal](../p/principal.md), [Nombre accesible](../n/nombre-accesible.md), [Orden de foco](../o/orden-de-foco.md), [Región](../r/region.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-174 — Semántica, teclado, foco y tecnologías de asistencia](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

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

[↑ Glosario](../../README.md) · [← Enlace](./enlace.md) · [Enlace frente a evidencia →](./enlace-frente-a-evidencia.md)
