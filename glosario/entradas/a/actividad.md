# Actividad

[↑ Glosario](../../README.md) · [← Active Record](./active-record.md) · [Activo →](./activo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

En el programa, **actividad** es lo que ocurre dentro del producto: inicios de sesión, vistas, clics, mensajes. Es la definición de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md): mide movimiento, no logro. Una persona puede generar mucha actividad sin conseguir nada de lo que vino a hacer, y puede conseguir su objetivo con muy poca. Por eso la clase la sitúa entre la producción del equipo (lo que se entrega) y el resultado (lo que cambia para quien usa el producto).

## Por qué importa

Cambia la decisión de qué número se convierte en meta. Según [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), la actividad es el primer indicio de que algo se usa, pero puede crecer por razones ajenas al valor: una notificación, o un cambio de diseño que obliga a más clics. Un equipo que persigue actividad puede «mejorar» el panel empeorando el producto. En el experimento de los equipos de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), la actividad correlaciona apenas 0,20 con el resultado: informa algo, pero no lo bastante para ser meta.

## Cómo funciona

La actividad se cuenta fácil porque el producto ya la registra. Esa facilidad es su trampa: lo que se mide sin esfuerzo tiende a sustituir a lo que importa. [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) propone clasificar cada métrica de una auditoría en cuatro tipos (producción, actividad, resultado, vanidad) y exigir para cada una la decisión que informa y una métrica contraria. La actividad no se descarta: sirve como señal temprana y para diagnosticar. Lo que no sirve es premiarla.

La diferencia útil está dentro de la propia actividad. Enviar una entrega aceptada es actividad cercana al valor; abrir la aplicación no lo es. [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) desarrolla esa distinción con la «tarea útil»: el evento que prueba que la persona logró algo. Además, una cifra acumulada («sesiones totales») solo crece y esconde el estancamiento; por eso [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) recomienda métricas por periodo (activos del mes, retenidos).

## Ejemplo

En la plataforma de entregas de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), `metric-audit.md` tiene una fila por métrica: definición calculable (numerador, denominador, ventana, filtros), tipo, decisión que informa, métrica contraria y fecha de revisión. «Sesiones por semana» queda tipificada como actividad. Si el equipo quisiera elevarla como meta, la regla del contrato exige emparejarla con una métrica de resultado y responder «qué haría distinto si bajara». Sin ese contrapeso, la meta no se acepta.

## Errores y confusiones comunes

- **La meta se cumple y nadie mejora.** Se premió la producción o la actividad; corrección de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md): sustituirla o acompañarla con un resultado y su métrica contraria.
- **El panel solo muestra crecimiento.** La métrica es acumulada; usar cifras por periodo.
- **Confundir actividad con uso valioso.** Que alguien abra la aplicación no prueba que consiga lo que necesita ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)).
- **Tratarla como vanidad sin matiz.** Una métrica de vanidad no informa ninguna decisión; la actividad sí puede informar, si se declara para qué.

## Límites y cuándo no aplica

La actividad es valiosa cuando todavía no hay un resultado medible: informa de adopción inicial. Deja de valer como meta en cuanto puede subir sin que suba el resultado. Y no es un defecto del concepto sino de la evidencia: la correlación de 0,20 de [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) proviene de un experimento con datos sintéticos, no de un hallazgo general sobre productos reales. El criterio sigue siendo comprobar, en cada producto, qué tan cerca del valor está el evento que se cuenta.

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
