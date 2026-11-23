# Punto de corte

[↑ Glosario](../../README.md) · [← Punto de control](./punto-de-control.md) · [Punto de decisión (PDP) y de aplicación →](./punto-de-decision-pdp-y-de-aplicacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Ancho a partir del cual cambia una regla de maquetación.

Definición de trabajo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md).

## Por qué importa

En [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), el tema «Puntos de corte y diseño intrínseco» importa porque decide dónde cambia el diseño y por qué.

## Cómo funciona

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

Un punto de corte fijado por dispositivo (768, 1 024) envejece y deja anchos intermedios sin comprobar. Un criterio más duradero es cambiar donde el contenido deja de funcionar: cuando una columna baja de un ancho útil, cuando una línea supera una longitud cómoda o cuando un título se corta. Las rejillas que envuelven con un mínimo por columna producen ese comportamiento sin escribir un punto de corte por caso.

Según [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md):

En la plataforma, la maquetación usa una rejilla que envuelve con un mínimo por columna, unidades relativas y puntos de corte donde el contenido lo exige. Una matriz de pruebas cubre los pares de cinco preferencias (movimiento reducido, esquema, contraste, colores forzados, zoom) en el proceso de entrega, con capturas a 320, 768 y 1 280 px CSS; los pares que no se prueban quedan listados con su riesgo. Las imágenes se sirven con variantes por ancho y un presupuesto de peso por página.

## Ejemplo

Ejemplo de [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) (sección «Ejemplo profesional»):

En la plataforma, la maquetación usa una rejilla que envuelve con un mínimo por columna, unidades relativas y puntos de corte donde el contenido lo exige. Una matriz de pruebas cubre los pares de cinco preferencias (movimiento reducido, esquema, contraste, colores forzados, zoom) en el proceso de entrega, con capturas a 320, 768 y 1 280 px CSS; los pares que no se prueban quedan listados con su riesgo. Las imágenes se sirven con variantes por ancho y un presupuesto de peso por página.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una tarjeta se corta en teléfonos pequeños** — causa: puntos de corte por dispositivo tipo. Corrección: rejilla con mínimo por columna y barrido de anchos en las pruebas. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un punto de corte fijado por dispositivo (768, 1 024) envejece y deja anchos intermedios sin comprobar. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))
- Un número fijado de antemano por dispositivo envejece; una rejilla con mínimo por columna reduce la necesidad de puntos de corte. ([SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Característica de preferencia](../c/caracteristica-de-preferencia.md), [Cobertura de pares](../c/cobertura-de-pares.md), [Diseño responsive](../d/diseno-responsive.md), [Srcset](../s/srcset.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-176 — Responsive, adaptativo y preferencias del usuario](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

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

[↑ Glosario](../../README.md) · [← Punto de control](./punto-de-control.md) · [Punto de decisión (PDP) y de aplicación →](./punto-de-decision-pdp-y-de-aplicacion.md)
