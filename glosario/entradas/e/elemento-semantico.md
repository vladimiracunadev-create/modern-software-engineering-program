# Elemento semántico

[↑ Glosario](../../README.md) · [← Ejercicio previo al fallo](./ejercicio-previo-al-fallo.md) · [Elevación →](./elevacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Elemento HTML cuyo significado y comportamiento por defecto describe su función (botón, enlace, etiqueta, encabezado) y no solo su aspecto.

Definición de trabajo de [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md).

## Por qué importa

La clase donde se define, [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), existe con este propósito: la clase existe para que trates el HTML y el CSS como un contrato con el navegador y con las tecnologías de apoyo, no como una capa de decoración: un `button` real ya trae foco, teclado y rol; un `div` con `onclick` obliga a reconstruirlo, y a menudo se reconstruye mal.

## Cómo funciona

[SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md):

El formulario de entrega del caso conductor se publica con una estructura revisable: un `header` con `nav`, un `main` con un único `h1` («Entregar tarea») y `h2` por bloque, un `form` con dos campos, cada uno con su `label for`, un `button type="submit"` y un mensaje de estado en una región con `role="status"`. Los colores salen de variables CSS con la razón de contraste anotada junto a cada par. La hoja usa `@layer base, componentes, utilidades;` de modo que un ajuste puntual no necesita subir selectores.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md)) son:

- **Un lector de pantalla anuncia «campo de edición» sin nombre** — causa: campo con `placeholder` pero sin `label` asociada. Corrección: añadir `label for` con el `id` del campo; el `placeholder` no es un nombre fiable.
- **Los encabezados se eligieron por tamaño y la lista de encabezados no tiene sentido** — causa: `h3` usado porque «se ve más pequeño». Corrección: elegir el nivel por la estructura y dar tamaño con CSS.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md)) son: Las definiciones son operativas para esta clase y deben contrastarse con las especificaciones enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona ni se usó un lector de pantalla: la página, las once mutaciones, la paleta y la simulación de especificidad son construcciones del autor. La siguiente clase pregunta qué ocurre cuando el documento deja de ser estático y un programa en JavaScript lo modifica en respuesta a eventos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Enlace](./enlace.md), [Etiqueta](./etiqueta.md), [Función](../f/funcion.md), [Capa de cascada](../c/capa-de-cascada.md), [Especificidad](./especificidad.md), [Nombre accesible](../n/nombre-accesible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/) — criterios de contraste, reflujo y contenido no textual; autoridad: W3C.
- [Understanding SC 1.4.3 Contrast (Minimum) (W3C)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — fórmula de la razón de contraste y umbrales; autoridad: W3C WAI.
- [HTML Standard (WHATWG)](https://html.spec.whatwg.org/multipage/) — elementos, roles de contenido y comportamiento nativo; autoridad: WHATWG.
- [CSS Selectors Level 4: Specificity (W3C)](https://www.w3.org/TR/selectors-4/#specificity-rules) — cálculo de especificidad; autoridad: W3C.
- [CSS Cascading and Inheritance Level 5: Layering (W3C)](https://www.w3.org/TR/css-cascade-5/#layering) — orden de la cascada y capas; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Ejercicio previo al fallo](./ejercicio-previo-al-fallo.md) · [Elevación →](./elevacion.md)
