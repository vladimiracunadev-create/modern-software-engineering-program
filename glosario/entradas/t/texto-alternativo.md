# Texto alternativo

[↑ Glosario](../../README.md) · [← Términos, hechos y consultas](./terminos-hechos-y-consultas.md) · [Throttle →](./throttle.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Texto que sustituye a una imagen para quien no la percibe y que describe su función o contenido.

Definición de trabajo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md).

## Por qué importa

La clase donde se define, [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), existe con este propósito: la clase existe para que interpretes qué exigen las pautas de accesibilidad, calcules lo que se puede calcular (contraste, tamaño de destino) y sepas qué parte de un defecto una herramienta automática no puede ver, de modo que no declares cumplimiento por el resultado de un escáner.

## Cómo funciona

Según [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

Una regla ve presencia: un atributo, un elemento, una razón de contraste. No ve verdad: que el texto alternativo describa la imagen, que la etiqueta corresponda al campo, que el título sea informativo o que el idioma declarado sea el del texto. Por eso una herramienta automática encuentra una parte de los problemas y el resto exige revisión humana y personas. Ese límite se mide: con defectos conocidos se cuenta qué detecta la regla.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

En la plataforma, la entrega se evalúa con un procedimiento de tres capas: reglas automáticas en cada cambio (idioma, etiquetas, alt, contraste de la paleta, tamaño de destinos), una revisión manual con una lista de criterios por proceso y una sesión con personas que usan tecnologías de apoyo. La declaración indica el proceso completo evaluado (abrir, completar, enviar, ver el recibo), la fecha, las herramientas y las personas, y enumera lo que no se probó.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son:

- **Se declara «cumple AA» con un puntaje** — causa: se confundió presencia con verdad. Corrección: declarar alcance, evidencia humana y lo no cubierto.
- **Texto legible para el equipo e ilegible al sol** — causa: no se calculó el contraste. Corrección: calcular razones y fijar la paleta en un archivo comprobable.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No ve verdad: que el texto alternativo describa la imagen, que la etiqueta corresponda al campo, que el título sea informativo o que el idioma declarado sea el del texto. ([SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Imagen](../i/imagen.md), [Criterio de éxito](../c/criterio-de-exito.md), [Declaración de alcance](../d/declaracion-de-alcance.md), [Razón de contraste](../r/razon-de-contraste.md), [Tecnología de apoyo](./tecnologia-de-apoyo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (221 clases más lo mencionan; las que más):

[SE-209](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-209-diagramas-modelos-y-documentacion-visual/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md), [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md).

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

[↑ Glosario](../../README.md) · [← Términos, hechos y consultas](./terminos-hechos-y-consultas.md) · [Throttle →](./throttle.md)
