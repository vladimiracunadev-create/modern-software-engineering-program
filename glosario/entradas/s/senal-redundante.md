# Señal redundante

[↑ Glosario](../../README.md) · [← Señal de terminación](./senal-de-terminacion.md) · [Señal sin datos →](./senal-sin-datos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Indicador adicional al color, como texto, forma o patrón.

Definición de trabajo de [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md).

## Por qué importa

La clase donde se define, [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), existe con este propósito: la clase existe para que decidas color, tipografía y maquetación con cálculos y simulaciones (contraste, confusión de colores, reflujo) y no con una impresión, y para que sepas qué se conserva y qué se rompe cuando un tema, un zoom o una visión distinta cambian lo que se ve.

## Cómo funciona

Según [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md):

En la plataforma, los tokens de color viven en un archivo con los pares permitidos de texto sobre fondo; una prueba calcula la razón de cada par y falla si alguno baja de 4,5:1 (3:1 para componentes), y otra calcula la distancia entre los colores de estado bajo tres simulaciones de visión y exige una señal redundante cuando baja de diez. El tema oscuro se define con sus propios pares y la maquetación usa anchos relativos; una captura a 320 px CSS comprueba que no hay desplazamiento horizontal.

Según [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md):

Pocos y con una señal adicional. Cada color añadido compite con los otros por distinguibilidad y, sin una señal redundante, depende de que la persona distinga tonos; la cifra depende de la distancia mínima que exijas bajo simulación.

## Ejemplo

Ejemplo de [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sección «Ejemplo profesional»):

En la plataforma, los tokens de color viven en un archivo con los pares permitidos de texto sobre fondo; una prueba calcula la razón de cada par y falla si alguno baja de 4,5:1 (3:1 para componentes), y otra calcula la distancia entre los colores de estado bajo tres simulaciones de visión y exige una señal redundante cuando baja de diez. El tema oscuro se define con sus propios pares y la maquetación usa anchos relativos; una captura a 320 px CSS comprueba que no hay desplazamiento horizontal.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md)) son:

- **Dos estados se ven iguales a una parte de los usuarios** — causa: se codificaron solo con tono. Corrección: añadir texto, forma o patrón y comprobar la distancia.
- **El modo oscuro tiene textos ilegibles** — causa: se invirtieron los colores. Corrección: definir pares calculados para el tema oscuro.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada color añadido compite con los otros por distinguibilidad y, sin una señal redundante, depende de que la persona distinga tonos; la cifra depende de la distancia mínima que exijas bajo simulación. ([SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Indicador](../i/indicador.md), [Patrón](../p/patron.md), [Distancia de color ΔE](../d/distancia-de-color-e.md), [Razón de contraste](../r/razon-de-contraste.md), [Reflujo](../r/reflujo.md), [Token de diseño](../t/token-de-diseno.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Machado, Oliveira y Fernandes, «A physiologically-based model for simulation of color vision deficiency» (IEEE TVCG, 2009)](https://doi.org/10.1109/TVCG.2009.113) — matrices de simulación de deficiencias de color; autoridad: IEEE Transactions on Visualization and Computer Graphics.
- [W3C: Comprender 1.4.3 Contraste (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razones de contraste y cálculo; autoridad: W3C.
- [W3C: Comprender 1.4.1 Uso del color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) — señales no basadas solo en color; autoridad: W3C.
- [W3C: Comprender 1.4.10 Reflujo](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — contenido sin desplazamiento en dos dimensiones; autoridad: W3C.
- [MDN: `prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — preferencia de esquema claro u oscuro; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Señal de terminación](./senal-de-terminacion.md) · [Señal sin datos →](./senal-sin-datos.md)
