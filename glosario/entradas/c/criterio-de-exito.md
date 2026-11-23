# Criterio de éxito

[↑ Glosario](../../README.md) · [← Criterio de aceptación](./criterio-de-aceptacion.md) · [Criterio de parada →](./criterio-de-parada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Condición verificable de una pauta de accesibilidad con un nivel de conformidad.

Definición de trabajo de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md).

## Por qué importa

La clase donde se define, [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), existe con este propósito: la clase existe para que interpretes qué exigen las pautas de accesibilidad, calcules lo que se puede calcular (contraste, tamaño de destino) y sepas qué parte de un defecto una herramienta automática no puede ver, de modo que no declares cumplimiento por el resultado de un escáner.

## Cómo funciona

Según [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

Perceptible: la información se presenta de un modo que se puede percibir (alternativas de texto, contraste, subtítulos). Operable: los componentes se pueden usar (teclado, tiempo suficiente, destinos). Comprensible: el contenido y el funcionamiento se entienden (idioma, etiquetas, errores). Robusto: el contenido se interpreta de forma fiable por distintos agentes, incluidas las tecnologías de apoyo. Los criterios de éxito concretan cada principio con una condición comprobable y un nivel de conformidad.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

En la plataforma, la entrega se evalúa con un procedimiento de tres capas: reglas automáticas en cada cambio (idioma, etiquetas, alt, contraste de la paleta, tamaño de destinos), una revisión manual con una lista de criterios por proceso y una sesión con personas que usan tecnologías de apoyo. La declaración indica el proceso completo evaluado (abrir, completar, enviar, ver el recibo), la fecha, las herramientas y las personas, y enumera lo que no se probó.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son:

- **Se declara «cumple AA» con un puntaje** — causa: se confundió presencia con verdad. Corrección: declarar alcance, evidencia humana y lo no cubierto.
- **Texto legible para el equipo e ilegible al sol** — causa: no se calculó el contraste. Corrección: calcular razones y fijar la paleta en un archivo comprobable.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún escáner de producción, lector de pantalla ni persona usuaria de tecnologías de apoyo, y los doce defectos, los anchos de destino y el modelo en una dimensión son construcciones del autor. La siguiente clase baja a la estructura semántica, el teclado y el foco.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Conformidad](./conformidad.md), [Declaración de alcance](../d/declaracion-de-alcance.md), [Razón de contraste](../r/razon-de-contraste.md), [Tecnología de apoyo](../t/tecnologia-de-apoyo.md), [Texto alternativo](../t/texto-alternativo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md), [SE-058](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-058-resolucion-sistematica-y-registro-de-hipotesis/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md).

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

[↑ Glosario](../../README.md) · [← Criterio de aceptación](./criterio-de-aceptacion.md) · [Criterio de parada →](./criterio-de-parada.md)
