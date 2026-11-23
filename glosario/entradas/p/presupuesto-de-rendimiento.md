# Presupuesto de rendimiento

[↑ Glosario](../../README.md) · [← Presupuesto de reintentos](./presupuesto-de-reintentos.md) · [Prevalencia →](./prevalencia.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Límite medible sobre una magnitud de la experiencia, con dueño y acción al superarse.

Definición de trabajo de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md): Límite explícito y comprobable sobre una métrica o un tamaño que el equipo se compromete a no superar.

## Por qué importa

En [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), el tema «Presupuestos de rendimiento» importa porque convierten una aspiración en una restricción comprobable.

## Cómo funciona

Según [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), en la sección «Presupuestos de rendimiento»:

Un **presupuesto** es un límite medible sobre una magnitud que importa: peso de la página en bytes, número de solicitudes, tiempo hasta el contenido principal, tiempo de bloqueo del hilo, razón de contraste. Tiene un dueño (alguien responde por él), un umbral con una razón, una medición automática y una acción al superarlo. El peso es una buena variable de partida porque es determinista y fácil de comprobar, pero es solo un indicador indirecto: la misma cantidad de bytes puede cargarse rápido o lento según qué sea (una imagen grande retrasa menos que el mismo peso en JavaScript que hay que ejecutar). Por eso un presupuesto de bytes se complementa con uno de tiempo medido en un perfil de dispositivo y red declarado, y con el seguimiento de campo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md):

El equipo escribe el presupuesto de experiencia del portal. Peso: 400 KB de recursos críticos, dueño del equipo de interfaz, comprobado en cada cambio con una compuerta de tendencia del +10 % sobre la mediana de las últimas diez fusiones. Tiempo hasta el contenido principal: p75 de campo de 2,5 s y, aparte, p75 del segmento de teléfonos modestos de 4 s, medidos con datos de las cargas reales de las personas que aceptan la medición y revisados cada semana.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)) son:

- **El laboratorio dice rápido y las personas se quejan** — causa: medición con el mejor dispositivo. Corrección: perfiles de dispositivo y red modestos y datos de campo.
- **El presupuesto avisa cuando ya es tarde** — causa: solo umbral absoluto. Corrección: añadir compuerta de tendencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un presupuesto de rendimiento es un límite explícito (kilobytes de JavaScript, número de peticiones, LCP en el percentil 75) que se comprueba en cada cambio. ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Límite](../l/limite.md), [Métrica](../m/metrica.md), [Sobre](../s/sobre.md), [Byte](../b/byte.md), [Deriva](../d/deriva.md), [Medición de campo](../m/medicion-de-campo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-235 — Rendimiento web y presupuestos](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Presupuestos de rendimiento».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: performance budgets 101](https://web.dev/articles/performance-budgets-101) — presupuestos de rendimiento; autoridad: Google, documentación de web.dev.
- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) — definición del LCP y umbral recomendado; autoridad: Google, documentación de web.dev.
- [W3C: Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razón de contraste y fórmula; autoridad: W3C.
- [W3C: Understanding SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) — contraste de componentes y gráficos; autoridad: W3C.
- [Nielsen Norman Group: Response Times, the 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — límites de tiempo de respuesta; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Presupuesto de reintentos](./presupuesto-de-reintentos.md) · [Prevalencia →](./prevalencia.md)
