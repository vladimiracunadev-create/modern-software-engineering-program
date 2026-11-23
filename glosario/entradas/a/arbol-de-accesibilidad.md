# Árbol de accesibilidad

[↑ Glosario](../../README.md) · [← Árbol](./arbol.md) · [Árbol de búsqueda →](./arbol-de-busqueda.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Representación que la plataforma ofrece a las tecnologías de apoyo con nombre, rol y estado de cada elemento.

Definición de trabajo de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md).

## Por qué importa

En [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), el tema «Nombre, rol y estado para tecnologías de apoyo» importa porque un lector de pantalla anuncia lo que el árbol de accesibilidad contiene, no lo que se ve.

## Cómo funciona

Según [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

Un botón de icono sin nombre es silencioso; un control personalizado sin rol no es un control. Las plataformas ofrecen un árbol de accesibilidad con nombre, rol y estado, y las pruebas más fiables consisten en recorrer la interfaz con la tecnología de apoyo. Eso no se simula aquí: se declara como lo que no se midió.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md):

El equipo del cliente escribe una tabla de modos de entrada con una fila por función y una columna por entrada (tacto, teclado, puntero, lector). «Enviar entrega» se activa con un botón de 48 por 48, con la tecla Intro y con el rol de botón; «Reordenar adjuntos» deja de depender del arrastre y ofrece botones de subir y bajar.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md)) son:

- **Los botones se pulsan mal en el teléfono** — causa: objetivos pequeños o juntos. Corrección: aumentar el tamaño y la separación; medir con usuarios.
- **El teclado se queda atascado en un control** — causa: trampa de foco. Corrección: permitir salir y añadir un recorrido a las pruebas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona ni se usó un lector de pantalla: el error del dedo y los grafos de foco son construcciones del autor. La siguiente clase pregunta cómo llegan las versiones a los dispositivos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-257](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-257-permisos-sensores-y-capacidades-del-dispositivo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tecnología de apoyo](../t/tecnologia-de-apoyo.md), [Estado](../e/estado.md), [Plataforma](../p/plataforma.md), [Representación](../r/representacion.md), [Objetivo táctil](../o/objetivo-tactil.md), [Orden de foco](../o/orden-de-foco.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-258 — Interacción táctil, teclado, mouse y accesibilidad](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C, «WCAG 2.2»](https://www.w3.org/TR/WCAG22/) — pautas de accesibilidad del contenido web; autoridad: W3C.
- [W3C, «Understanding SC 2.5.8: Target Size (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — tamaño mínimo de objetivos; autoridad: W3C.
- [W3C, «Understanding SC 1.4.3: Contrast (Minimum)»](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — contraste mínimo y su fórmula; autoridad: W3C.
- [W3C, «Understanding SC 2.4.3: Focus Order»](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html) — orden de foco; autoridad: W3C.
- [Apple Developer, «Accessibility» (Human Interface Guidelines)](https://developer.apple.com/design/human-interface-guidelines/accessibility) — guía de accesibilidad de las plataformas de Apple; autoridad: Apple.

---

[↑ Glosario](../../README.md) · [← Árbol](./arbol.md) · [Árbol de búsqueda →](./arbol-de-busqueda.md)
