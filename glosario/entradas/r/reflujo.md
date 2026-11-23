# Reflujo

[↑ Glosario](../../README.md) · [← Reflog](./reflog.md) · [Reformulación →](./reformulacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Adaptación del contenido al ancho disponible sin desplazamiento en dos dimensiones.

Definición de trabajo de [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md): Propiedad de un diseño que reorganiza su contenido para caber en un ancho menor sin desplazamiento en dos dimensiones.

## Por qué importa

En [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), el tema «Maquetación, zoom y reflujo» importa porque hace que el contenido se adapte al ancho disponible al ampliar.

## Cómo funciona

Según [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md):

Porque respetan el tamaño de texto que la persona eligió en el navegador y permiten el reflujo al ampliar; con píxeles fijos, esa preferencia se ignora y los contenedores desbordan.

Según [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md):

Traslada el análisis a otra interfaz (un tablero con alertas de colores o un mapa de calor): calcula los pares, simula tres visiones, decide señales redundantes y mide el reflujo. La transferencia está lograda cuando puedes explicar qué parte dependía de la plataforma de entregas y cuál no.

## Ejemplo

Ejemplo de [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sección «Caso conductor»):

La plataforma de entregas es el caso conductor de la [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md). Esta clase deja los tokens de color y tipografía, las señales redundantes de estado y las comprobaciones de contraste y reflujo. `SE-176` adaptará esa maquetación a anchos y preferencias, y `SE-177` a idiomas y formatos. Cambia después un solo token, el color de error, y revisa qué pares, qué estados y qué capturas dependían de él.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los botones de la derecha no se pueden pulsar en un teléfono** — causa: diseño de una fila pensado para ventana ancha. Corrección: diseñar a 320 píxeles y reflujo; probar a varios anchos. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- WCAG pide que el contenido reflujo a 320 píxeles CSS sin desplazamiento en dos dimensiones. ([SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Desplazamiento](../d/desplazamiento.md), [Dimensión](../d/dimension.md), [Propiedad](../p/propiedad.md), [Arranque en frío](../a/arranque-en-frio.md), [Distancia de color ΔE](../d/distancia-de-color-e.md), [Instancia](../i/instancia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-253 — Modelos de aplicación móvil y de escritorio](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Comprender 1.4.10 Reflujo](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) — contenido sin desplazamiento en dos dimensiones; autoridad: W3C.
- [Machado, Oliveira y Fernandes, «A physiologically-based model for simulation of color vision deficiency» (IEEE TVCG, 2009)](https://doi.org/10.1109/TVCG.2009.113) — matrices de simulación de deficiencias de color; autoridad: IEEE Transactions on Visualization and Computer Graphics.
- [W3C: Comprender 1.4.3 Contraste (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razones de contraste y cálculo; autoridad: W3C.
- [W3C: Comprender 1.4.1 Uso del color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) — señales no basadas solo en color; autoridad: W3C.
- [MDN: `prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — preferencia de esquema claro u oscuro; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Reflog](./reflog.md) · [Reformulación →](./reformulacion.md)
