# Srcset

[↑ Glosario](../../README.md) · [← Squash](./squash.md) · [SSRF →](./ssrf.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Atributo que ofrece al navegador varias fuentes de una imagen para elegir según el ancho y la densidad.

Definición de trabajo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

## Por qué importa

La clase donde se define, [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), existe con este propósito: la clase existe para que adaptes la interfaz a anchos de pantalla, preferencias del usuario y conexiones distintas con un plan de pruebas que cubra las combinaciones que importan, y para que midas qué fallos deja cada estrategia.

## Cómo funciona

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

Un teléfono con una conexión lenta no necesita una imagen de 2 400 px. Las variantes por ancho (`srcset` y `sizes`) permiten al navegador elegir la adecuada, y el ahorro es proporcional a los píxeles que no se descargan. Para quien usa una conexión limitada, el peso es un criterio de accesibilidad, no solo de rendimiento: una página que no carga no es utilizable.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

En la plataforma, la maquetación usa una rejilla que envuelve con un mínimo por columna, unidades relativas y puntos de corte donde el contenido lo exige. Una matriz de pruebas cubre los pares de cinco preferencias (movimiento reducido, esquema, contraste, colores forzados, zoom) en el proceso de entrega, con capturas a 320, 768 y 1 280 px CSS; los pares que no se prueban quedan listados con su riesgo. Las imágenes se sirven con variantes por ancho y un presupuesto de peso por página.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md)) son:

- **Una tarjeta se corta en teléfonos pequeños** — causa: puntos de corte por dispositivo tipo. Corrección: rejilla con mínimo por columna y barrido de anchos en las pruebas.
- **Un defecto aparece solo con zoom y esquema oscuro** — causa: no se probaron combinaciones. Corrección: matriz de pares y lista de lagunas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las variantes por ancho (`srcset` y `sizes`) permiten al navegador elegir la adecuada, y el ahorro es proporcional a los píxeles que no se descargan. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Imagen](../i/imagen.md), [Característica de preferencia](../c/caracteristica-de-preferencia.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Diseño responsive](../d/diseno-responsive.md), [Punto de corte](../p/punto-de-corte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: imágenes responsivas](https://web.dev/articles/responsive-images) — `srcset` y `sizes`; autoridad: Google (guía de buenas prácticas).
- [W3C: Media Queries Level 4](https://www.w3.org/TR/mediaqueries-4/) — características de medios y de preferencia del usuario; autoridad: W3C.
- [W3C: CSS Grid Layout Module Level 1](https://www.w3.org/TR/css-grid-1/) — rejillas con mínimos y envoltura; autoridad: W3C.
- [MDN: `prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — preferencia de movimiento reducido; autoridad: Mozilla.
- [MDN: `prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — preferencia de esquema; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Squash](./squash.md) · [SSRF →](./ssrf.md)
