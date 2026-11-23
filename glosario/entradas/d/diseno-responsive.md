# Diseño responsive

[↑ Glosario](../../README.md) · [← Diseño pareado](./diseno-pareado.md) · [Disparador →](./disparador.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Diseño que se ajusta de forma continua al ancho disponible.

Definición de trabajo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

## Por qué importa

En [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), el tema «Diseño responsive y adaptativo» importa porque distingue cómo se ajusta la interfaz a lo que hay.

## Cómo funciona

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

Un diseño responsive reacciona de forma continua al ancho disponible (rejillas que envuelven, unidades relativas, texto que fluye); uno adaptativo elige entre diseños predefinidos según condiciones. En la práctica se combinan: un esqueleto fluido con algunas decisiones por umbral. La ventaja de lo continuo es que no hay anchos que caigan entre dos casos; el riesgo de lo adaptativo es que aparecen huecos donde ningún diseño encaja, como los 290 px de la clase.

## Ejemplo

Caso medido en la sección «Diseño responsive y adaptativo» de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

Un diseño responsive reacciona de forma continua al ancho disponible (rejillas que envuelven, unidades relativas, texto que fluye); uno adaptativo elige entre diseños predefinidos según condiciones. En la práctica se combinan: un esqueleto fluido con algunas decisiones por umbral. La ventaja de lo continuo es que no hay anchos que caigan entre dos casos; el riesgo de lo adaptativo es que aparecen huecos donde ningún diseño encaja, como los 290 px de la clase.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md)) son:

- **Una tarjeta se corta en teléfonos pequeños** — causa: puntos de corte por dispositivo tipo. Corrección: rejilla con mínimo por columna y barrido de anchos en las pruebas.
- **Un defecto aparece solo con zoom y esquema oscuro** — causa: no se probaron combinaciones. Corrección: matriz de pares y lista de lagunas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un diseño responsive reacciona de forma continua al ancho disponible (rejillas que envuelven, unidades relativas, texto que fluye); uno adaptativo elige entre diseños predefinidos según condiciones. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Característica de preferencia](../c/caracteristica-de-preferencia.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Punto de corte](../p/punto-de-corte.md), [Srcset](../s/srcset.md).
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

[↑ Glosario](../../README.md) · [← Diseño pareado](./diseno-pareado.md) · [Disparador →](./disparador.md)
