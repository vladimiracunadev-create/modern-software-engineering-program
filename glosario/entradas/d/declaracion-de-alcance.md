# Declaración de alcance

[↑ Glosario](../../README.md) · [← Decisión revisable](./decision-revisable.md) · [Declaración de conformidad →](./declaracion-de-conformidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Texto que dice qué se evaluó, cómo, con qué criterios y qué quedó fuera.

Definición de trabajo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md).

## Por qué importa

La clase donde se define, [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), existe con este propósito: la clase existe para que interpretes qué exigen las pautas de accesibilidad, calcules lo que se puede calcular (contraste, tamaño de destino) y sepas qué parte de un defecto una herramienta automática no puede ver, de modo que no declares cumplimiento por el resultado de un escáner.

## Cómo funciona

[SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Ejemplo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md). Esta clase deja los criterios aplicables a la entrega, el auditor de reglas y la declaración de alcance. `SE-174` baja a la estructura semántica, el teclado y el foco; `SE-175` a la tipografía y el color. Cambia después un solo criterio, el tamaño de destino, y revisa qué controles y qué evidencia dependían de él.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son:

- **Se declara «cumple AA» con un puntaje** — causa: se confundió presencia con verdad. Corrección: declarar alcance, evidencia humana y lo no cubierto.
- **Texto legible para el equipo e ilegible al sol** — causa: no se calculó el contraste. Corrección: calcular razones y fijar la paleta en un archivo comprobable.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún escáner de producción, lector de pantalla ni persona usuaria de tecnologías de apoyo, y los doce defectos, los anchos de destino y el modelo en una dimensión son construcciones del autor. La siguiente clase baja a la estructura semántica, el teclado y el foco.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de éxito](../c/criterio-de-exito.md), [Razón de contraste](../r/razon-de-contraste.md), [Tecnología de apoyo](../t/tecnologia-de-apoyo.md), [Texto alternativo](../t/texto-alternativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md).

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

[↑ Glosario](../../README.md) · [← Decisión revisable](./decision-revisable.md) · [Declaración de conformidad →](./declaracion-de-conformidad.md)
