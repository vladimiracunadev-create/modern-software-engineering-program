# Minificación

[↑ Glosario](../../README.md) · [← Migración reversible](./migracion-reversible.md) · [Minimización →](./minimizacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Transformación del código que elimina lo que el motor no necesita sin cambiar su comportamiento.

Definición de trabajo de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md).

## Por qué importa

En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), el tema «Bytes» importa porque la compresión y la minificación dependen del tipo de activo y a veces no hacen nada.

## Cómo funciona

Según [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

Comprimir con gzip o Brotli reduce el texto (HTML, CSS, JavaScript, JSON) mucho y los formatos ya comprimidos (imágenes, vídeo, archivos) casi nada. La minificación quita lo que el motor no necesita; se suma a la compresión, pero la compresión ya elimina parte de la redundancia que la minificación quita, y por eso el beneficio combinado es menor que la suma. Las imágenes suelen dominar los bytes de una página: formato, tamaño y carga diferida pesan más que cualquier ajuste de CSS.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md):

El equipo fija presupuestos para la página de entrega: 170 KB de JavaScript comprimido en la ruta de entrada, 15 peticiones y LCP de 2,5 s en el percentil 75 de visitas reales desde un móvil de gama media. Cada cambio pasa un comprobador que falla si el paquete lo supera.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md)) son:

- **La mejora no se nota en el móvil** — causa: optimización fuera de la ruta crítica. Corrección: medir la cadena y actuar sobre su eslabón más largo.
- **Se declara que se cumple con diez mediciones** — causa: muestra pequeña con falsa conformidad frecuente. Corrección: usar datos de campo con cientos de visitas e informar el intervalo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La minificación quita lo que el motor no necesita; se suma a la compresión, pero la compresión ya elimina parte de la redundancia que la minificación quita, y por eso el beneficio combinado es menor que la suma. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Motor](./motor.md), [Byte](../b/byte.md), [Percentil 75](../p/percentil-75.md), [Precarga](../p/precarga.md), [Presupuesto](../p/presupuesto.md), [Presupuesto de rendimiento](../p/presupuesto-de-rendimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: umbrales de Core Web Vitals](https://web.dev/articles/defining-core-web-vitals-thresholds) — umbrales y percentil 75; autoridad: Google web.dev.
- [web.dev: Performance budgets 101](https://web.dev/articles/performance-budgets-101) — qué son los presupuestos y cómo comprobarlos; autoridad: Google web.dev.
- [web.dev: precargar recursos críticos](https://web.dev/articles/preload-critical-assets) — pistas de precarga; autoridad: Google web.dev.
- [MDN: ruta crítica de renderizado](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Critical_rendering_path) — pasos hasta la primera pintura; autoridad: MDN.
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113) — multiplexación de peticiones; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Migración reversible](./migracion-reversible.md) · [Minimización →](./minimizacion.md)
