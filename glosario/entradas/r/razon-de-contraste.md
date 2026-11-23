# Razón de contraste

[↑ Glosario](../../README.md) · [← Razón de cambio](./razon-de-cambio.md) · [ReAct →](./react.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Cociente (L1 + 0,05)/(L2 + 0,05) entre las luminancias relativas del color más claro y del más oscuro.

Definición de trabajo de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md): Cociente (L1 + 0,05) / (L2 + 0,05) entre las luminancias relativas del color claro y del oscuro.
- En [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md): Cociente `(L1 + 0,05) / (L2 + 0,05)` entre las luminancias relativas del color claro y del oscuro.
- En [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md): Cociente entre las luminancias relativas del color claro y del oscuro, con un término de 0,05 sumado.

## Por qué importa

La clase donde se define, [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), existe con este propósito: la clase existe para que conviertas «que se sienta bien» en presupuestos que un equipo puede vigilar: cuánto puede pesar una página, cuánto puede tardar en mostrar lo importante, qué contraste mínimo deben tener los textos, y para que sepas qué parte de la experiencia de una persona captura cada medida y cuál se escapa.

## Cómo funciona

Según [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md):

Un **presupuesto** es un límite medible sobre una magnitud que importa: peso de la página en bytes, número de solicitudes, tiempo hasta el contenido principal, tiempo de bloqueo del hilo, razón de contraste. Tiene un dueño (alguien responde por él), un umbral con una razón, una medición automática y una acción al superarlo. El peso es una buena variable de partida porque es determinista y fácil de comprobar, pero es solo un indicador indirecto: la misma cantidad de bytes puede cargarse rápido o lento según qué sea (una imagen grande retrasa menos que el mismo peso en JavaScript que hay que ejecutar). Por eso un presupuesto de bytes se complementa con uno de tiempo medido en un perfil de dispositivo y red declarado, y con el seguimiento de campo.

Según [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md):

La razón de contraste es (L1 + 0,05) / (L2 + 0,05) con L la luminancia relativa del color más claro y del más oscuro. El mínimo es 4,5:1 para texto normal y 3:1 para texto grande y componentes de interfaz. El color no puede ser la única señal de un estado: un error solo en rojo no se distingue para personas con daltonismo ni en una impresión en gris. Elegir colores sin calcular falla a menudo: en un sorteo de pares de colores aleatorios, solo una pequeña fracción alcanza 4,5:1.

## Ejemplo

Ejemplo de [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la razón de contraste entre texto negro y fondo blanco. Antes de ejecutarlo, predice si supera 4,5 a 1.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md)) son:

- **El laboratorio dice rápido y las personas se quejan** — causa: medición con el mejor dispositivo. Corrección: perfiles de dispositivo y red modestos y datos de campo.
- **El presupuesto avisa cuando ya es tarde** — causa: solo umbral absoluto. Corrección: añadir compuerta de tendencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **presupuesto** es un límite medible sobre una magnitud que importa: peso de la página en bytes, número de solicitudes, tiempo hasta el contenido principal, tiempo de bloqueo del hilo, razón de contraste. ([SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de éxito](../c/criterio-de-exito.md), [Declaración de alcance](../d/declaracion-de-alcance.md), [Distancia de color ΔE](../d/distancia-de-color-e.md), [Reflujo](./reflujo.md), [Señal redundante](../s/senal-redundante.md), [Tecnología de apoyo](../t/tecnologia-de-apoyo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-173 — Accesibilidad perceptible, operable y comprensible](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-175 — Diseño visual, tipografía, color y contraste](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-229 — Plataforma web, HTML semántico y CSS](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-442 — Calidad de experiencia y presupuestos](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-106](../../../classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md), [SE-239](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-239-taller-construir-un-flujo-web-resiliente/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: Understanding SC 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — razón de contraste y fórmula; autoridad: W3C.
- [web.dev: Largest Contentful Paint](https://web.dev/articles/lcp) — definición del LCP y umbral recomendado; autoridad: Google, documentación de web.dev.
- [web.dev: performance budgets 101](https://web.dev/articles/performance-budgets-101) — presupuestos de rendimiento; autoridad: Google, documentación de web.dev.
- [W3C: Understanding SC 1.4.11 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) — contraste de componentes y gráficos; autoridad: W3C.
- [Nielsen Norman Group: Response Times, the 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — límites de tiempo de respuesta; autoridad: Nielsen Norman Group.

---

[↑ Glosario](../../README.md) · [← Razón de cambio](./razon-de-cambio.md) · [ReAct →](./react.md)
