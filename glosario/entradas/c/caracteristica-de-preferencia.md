# Característica de preferencia

[↑ Glosario](../../README.md) · [← Característica de calidad](./caracteristica-de-calidad.md) · [Caracterización →](./caracterizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Consulta de medios que expresa una elección del usuario, como el movimiento reducido o el esquema oscuro.

Definición de trabajo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

## Por qué importa

La clase donde se define, [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), existe con este propósito: la clase existe para que adaptes la interfaz a anchos de pantalla, preferencias del usuario y conexiones distintas con un plan de pruebas que cubra las combinaciones que importan, y para que midas qué fallos deja cada estrategia.

## Cómo funciona

[SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

En la plataforma, la maquetación usa una rejilla que envuelve con un mínimo por columna, unidades relativas y puntos de corte donde el contenido lo exige. Una matriz de pruebas cubre los pares de cinco preferencias (movimiento reducido, esquema, contraste, colores forzados, zoom) en el proceso de entrega, con capturas a 320, 768 y 1 280 px CSS; los pares que no se prueban quedan listados con su riesgo. Las imágenes se sirven con variantes por ancho y un presupuesto de peso por página.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md)) son:

- **Una tarjeta se corta en teléfonos pequeños** — causa: puntos de corte por dispositivo tipo. Corrección: rejilla con mínimo por columna y barrido de anchos en las pruebas.
- **Un defecto aparece solo con zoom y esquema oscuro** — causa: no se probaron combinaciones. Corrección: matriz de pares y lista de lagunas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún navegador, dispositivo o red reales, y la mezcla de anchos, los 60 defectos, los bytes por píxel y el ancho de banda son supuestos del autor. La siguiente clase añade idiomas y formatos, que tensionan la misma maquetación.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Cobertura de pares](./cobertura-de-pares.md), [Diseño responsive](../d/diseno-responsive.md), [Punto de corte](../p/punto-de-corte.md), [Srcset](../s/srcset.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Media Queries Level 4](https://www.w3.org/TR/mediaqueries-4/) — características de medios y de preferencia del usuario; autoridad: W3C.
- [W3C: CSS Grid Layout Module Level 1](https://www.w3.org/TR/css-grid-1/) — rejillas con mínimos y envoltura; autoridad: W3C.
- [MDN: `prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — preferencia de movimiento reducido; autoridad: Mozilla.
- [MDN: `prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) — preferencia de esquema; autoridad: Mozilla.
- [MDN: `prefers-contrast`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-contrast) — preferencia de contraste; autoridad: Mozilla.

---

[↑ Glosario](../../README.md) · [← Característica de calidad](./caracteristica-de-calidad.md) · [Caracterización →](./caracterizacion.md)
