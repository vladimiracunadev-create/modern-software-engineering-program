# Medición de campo

[↑ Glosario](../../README.md) · [← Medición](./medicion.md) · [Medida →](./medida.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Medición recogida de cargas reales de personas usuarias.

Definición de trabajo de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

## Por qué importa

La clase donde se define, [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), existe con este propósito: la clase existe para que conviertas «que se sienta bien» en presupuestos que un equipo puede vigilar: cuánto puede pesar una página, cuánto puede tardar en mostrar lo importante, qué contraste mínimo deben tener los textos, y para que sepas qué parte de la experiencia de una persona captura cada medida y cuál se escapa.

## Cómo funciona

Según [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md):

Una **medición de laboratorio** ejecuta la página en un entorno controlado (un dispositivo, una red simulada, una caché limpia) y es repetible; una **medición de campo** recoge los tiempos de las cargas reales de las personas usuarias y es representativa. Se necesitan las dos: el laboratorio permite depurar y comparar versiones con poco ruido; el campo dice a quién le va bien y a quién no. El laboratorio con el equipo de desarrollo es casi siempre el caso más favorable de la población, porque la persona que construye el producto usa un dispositivo potente y una red rápida. Cuando se reporta un tiempo hay que decir de dónde sale y qué segmento representa; un número de laboratorio presentado como experiencia de las personas usuarias es una afirmación sin base.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md):

El equipo escribe el presupuesto de experiencia del portal. Peso: 400 KB de recursos críticos, dueño del equipo de interfaz, comprobado en cada cambio con una compuerta de tendencia del +10 % sobre la mediana de las últimas diez fusiones. Tiempo hasta el contenido principal: p75 de campo de 2,5 s y, aparte, p75 del segmento de teléfonos modestos de 4 s, medidos con datos de las cargas reales de las personas que aceptan la medición y revisados cada semana.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)) son:

- **El laboratorio dice rápido y las personas se quejan** — causa: medición con el mejor dispositivo. Corrección: perfiles de dispositivo y red modestos y datos de campo.
- **El presupuesto avisa cuando ya es tarde** — causa: solo umbral absoluto. Corrección: añadir compuerta de tendencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **medición de laboratorio** ejecuta la página en un entorno controlado (un dispositivo, una red simulada, una caché limpia) y es repetible; una **medición de campo** recoge los tiempos de las cargas reales de las personas usuarias y es representativa. ([SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medición](./medicion.md), [Deriva](../d/deriva.md), [Percentil 75](../p/percentil-75.md), [Presupuesto de rendimiento](../p/presupuesto-de-rendimiento.md), [Razón de contraste](../r/razon-de-contraste.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) — definición del LCP y umbral recomendado; autoridad: Google, documentación de web.dev.
- [web.dev: performance budgets 101](https://web.dev/articles/performance-budgets-101) — presupuestos de rendimiento; autoridad: Google, documentación de web.dev.
- [W3C: Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razón de contraste y fórmula; autoridad: W3C.
- [W3C: Understanding SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) — contraste de componentes y gráficos; autoridad: W3C.
- [Nielsen Norman Group: Response Times, the 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — límites de tiempo de respuesta; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Medición](./medicion.md) · [Medida →](./medida.md)
