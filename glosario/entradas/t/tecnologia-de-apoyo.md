# Tecnología de apoyo

[↑ Glosario](../../README.md) · [← Técnicas de detección](./tecnicas-de-deteccion.md) · [TEE →](./tee.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Software o dispositivo que usa una persona con discapacidad para acceder a un producto, como un lector de pantalla.

Definición de trabajo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md).

## Por qué importa

La clase donde se define, [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), existe con este propósito: la clase existe para que interpretes qué exigen las pautas de accesibilidad, calcules lo que se puede calcular (contraste, tamaño de destino) y sepas qué parte de un defecto una herramienta automática no puede ver, de modo que no declares cumplimiento por el resultado de un escáner.

## Cómo funciona

Según [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

Perceptible: la información se presenta de un modo que se puede percibir (alternativas de texto, contraste, subtítulos). Operable: los componentes se pueden usar (teclado, tiempo suficiente, destinos). Comprensible: el contenido y el funcionamiento se entienden (idioma, etiquetas, errores). Robusto: el contenido se interpreta de forma fiable por distintos agentes, incluidas las tecnologías de apoyo. Los criterios de éxito concretan cada principio con una condición comprobable y un nivel de conformidad.

Según [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

En la plataforma, la entrega se evalúa con un procedimiento de tres capas: reglas automáticas en cada cambio (idioma, etiquetas, alt, contraste de la paleta, tamaño de destinos), una revisión manual con una lista de criterios por proceso y una sesión con personas que usan tecnologías de apoyo. La declaración indica el proceso completo evaluado (abrir, completar, enviar, ver el recibo), la fecha, las herramientas y las personas, y enumera lo que no se probó.

## Ejemplo

Ejemplo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) (sección «Ejemplo profesional»):

En la plataforma, la entrega se evalúa con un procedimiento de tres capas: reglas automáticas en cada cambio (idioma, etiquetas, alt, contraste de la paleta, tamaño de destinos), una revisión manual con una lista de criterios por proceso y una sesión con personas que usan tecnologías de apoyo. La declaración indica el proceso completo evaluado (abrir, completar, enviar, ver el recibo), la fecha, las herramientas y las personas, y enumera lo que no se probó.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son:

- **Se declara «cumple AA» con un puntaje** — causa: se confundió presencia con verdad. Corrección: declarar alcance, evidencia humana y lo no cubierto.
- **Texto legible para el equipo e ilegible al sol** — causa: no se calculó el contraste. Corrección: calcular razones y fijar la paleta en un archivo comprobable.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún escáner de producción, lector de pantalla ni persona usuaria de tecnologías de apoyo, y los doce defectos, los anchos de destino y el modelo en una dimensión son construcciones del autor. La siguiente clase baja a la estructura semántica, el teclado y el foco.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Producto](../p/producto.md), [Criterio de éxito](../c/criterio-de-exito.md), [Declaración de alcance](../d/declaracion-de-alcance.md), [Razón de contraste](../r/razon-de-contraste.md), [Texto alternativo](./texto-alternativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (35 clases más lo mencionan; las que más):

[SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — criterios de éxito y niveles de conformidad; autoridad: W3C.
- [W3C: Comprender 1.4.3 Contraste (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razones de contraste y excepciones; autoridad: W3C.
- [W3C: Comprender 2.5.8 Tamaño del objetivo (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — tamaño y espacio de los destinos; autoridad: W3C.
- [W3C: Comprender 1.4.1 Uso del color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) — el color no como única señal; autoridad: W3C.
- [W3C: Comprender 1.1.1 Contenido no textual](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html) — alternativas de texto; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Técnicas de detección](./tecnicas-de-deteccion.md) · [TEE →](./tee.md)
