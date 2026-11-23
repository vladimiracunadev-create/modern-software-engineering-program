# Actividad

[↑ Glosario](../../README.md) · [← Active Record](./active-record.md) · [Activo →](./activo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Lo que ocurre dentro del producto (sesiones, vistas), sin garantizar que alguien logre algo.

Definición de trabajo de [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md).

## Por qué importa

En [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), el tema «Actividad» importa porque es lo que ocurre en el producto: sesiones, clics, mensajes; mide movimiento, no logro.

## Cómo funciona

Según [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), en la sección «Actividad»:

La actividad es lo que ocurre dentro del producto: inicios de sesión, vistas, mensajes. Es el primer indicio de que algo se usa y puede crecer por razones ajenas al valor (una notificación, un cambio de diseño que obliga a más clics). La actividad que se acerca al valor (enviar una entrega aceptada) se distingue de la que no (abrir la aplicación), y `SE-136` desarrolla esa diferencia con la tarea útil.

## Ejemplo

Ejemplo de [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sección «Ejemplo profesional»):

En la plataforma, `metric-audit.md` tiene una fila por métrica con definición calculable (numerador, denominador, ventana, filtros), tipo (producción, actividad, resultado, vanidad), decisión que informa, métrica contraria y fecha de revisión. El contrato es que ninguna métrica se convierte en meta sin su métrica contraria y sin la pregunta «qué haría distinto si bajara». Esa estructura permite que otra persona detecte metas sin contrapeso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)) son:

- **La meta se cumple y nadie mejora** — causa: se premió la producción. Corrección: reemplazar o acompañar con un resultado y su métrica contraria.
- **El panel solo muestra crecimiento** — causa: la métrica es acumulada. Corrección: usar métricas por periodo (activos del mes, retenidos).

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La actividad que se acerca al valor (enviar una entrega aceptada) se distingue de la que no (abrir la aplicación), y `SE-136` desarrolla esa diferencia con la tarea útil. ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md))
- En el experimento de los equipos, la actividad correlaciona 0,20 con el resultado: informa algo, pero no lo suficiente para ser meta. ([SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](../p/producto.md), [Vista](../v/vista.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Métrica de vanidad](../m/metrica-de-vanidad.md), [Producción](../p/produccion.md), [Resultado](../r/resultado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (43 clases más lo mencionan; las que más):

[SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md), [SE-129](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-129-etica-del-descubrimiento-y-proteccion-de-participantes/README.md), [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-488](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-488-entornos-preview-y-datos-seguros/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Airbnb](../../../casos/exito/airbnb.md), [Slack](../../../casos/exito/slack.md), [Discord](../../../casos/exito/discord.md), [Knight Capital](../../../casos/fallo/knight-capital.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir qué medir a partir de lo que se necesita saber; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) — cómo medir satisfacción como complemento de indicadores de uso; autoridad: Government Digital Service.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — mecanismos por los que una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv (D. Manheim y S. Garrabrant).
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas de entrega; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Active Record](./active-record.md) · [Activo →](./activo.md)
