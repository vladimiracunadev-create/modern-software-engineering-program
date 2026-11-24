# Presupuesto de rendimiento

[↑ Glosario](../../README.md) · [← Presupuesto de reintentos](./presupuesto-de-reintentos.md) · [Prevalencia →](./prevalencia.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md)

## Definición

Un **presupuesto de rendimiento** es un límite medible sobre una magnitud de la experiencia, con dueño y una acción al superarse. [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) (rendimiento web y presupuestos) lo define como un límite explícito y comprobable sobre una métrica o un tamaño que el equipo se compromete a no superar; [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) (calidad de experiencia y presupuestos) lo amplía con las partes que lo hacen operable.

## Por qué importa

Convierte una aspiración («que cargue rápido») en una restricción comprobable. Su valor, según [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md), es hacer visible una decisión implícita: «añadamos esta biblioteca» se vuelve «cuesta 40 KB de los 200 que tenemos». Sin presupuesto, el rendimiento se degrada sin que nadie lo decida.

## Cómo funciona

[SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) lista las cinco partes de un presupuesto:

1. **Una magnitud que importa:** peso de la página en bytes, número de solicitudes, tiempo hasta el contenido principal (LCP), tiempo de bloqueo del hilo, razón de contraste.
2. **Un dueño** que responde por él.
3. **Un umbral con una razón.**
4. **Una medición automática.**
5. **Una acción al superarlo.**

El peso es buena variable de partida porque es determinista y fácil de comprobar, pero es un indicador indirecto: la misma cantidad de bytes puede cargarse rápido o lento según qué sea (una imagen grande retrasa menos que el mismo peso en JavaScript, que hay que ejecutar). Por eso se complementa con uno de tiempo medido en un perfil de dispositivo y red declarado, y con seguimiento de campo (datos reales de usuarios, como el percentil 75). [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) pide derivar el presupuesto de un objetivo, un tiempo en un dispositivo y red de referencia, y revisarlo.

## Ejemplo

El equipo de [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md) fija para la página de entrega: 170 KB de JavaScript comprimido en la ruta de entrada, 15 peticiones y LCP de 2,5 s en el percentil 75 de visitas reales desde un móvil de gama media. Cada cambio pasa un comprobador que falla si el paquete lo supera. En [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), el portal fija 400 KB de recursos críticos, dueño del equipo de interfaz, comprobado en cada cambio con una compuerta de tendencia del +10 % sobre la mediana de las últimas diez fusiones.

## Errores y confusiones comunes

- **Un presupuesto que nadie hace cumplir** es una intención ([SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md)).
- **Presupuestar solo bytes** y no tiempo.
- **Fijar un umbral sin razón,** que se discute y se relaja.
- **Confundirlo con un SLO:** el presupuesto limita un tamaño o métrica de construcción; el SLO es un compromiso de servicio medido en producción.

## Límites y cuándo no aplica

Un presupuesto limita lo medido, no la experiencia entera: una página puede cumplir y sentirse lenta por algo no presupuestado. Los umbrales de los ejemplos son del escenario de la clase. Se vuelve burocracia si no tiene dueño que lo revise.

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
