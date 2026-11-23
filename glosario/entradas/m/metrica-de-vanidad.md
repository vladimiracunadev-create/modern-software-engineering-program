# Métrica de vanidad

[↑ Glosario](../../README.md) · [← Métrica de valor](./metrica-de-valor.md) · [Métrica facturable →](./metrica-facturable.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Cifra que sube sin que ninguna decisión cambie si baja, a menudo acumulada.

Definición de trabajo de [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md).

## Por qué importa

En [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), el tema «Métricas de vanidad» importa porque son cifras que suben y favorecen la presentación sin informar una decisión.

## Cómo funciona

Según [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), en la sección «Métricas de vanidad»:

Una cifra es de vanidad cuando sube sin que ninguna decisión cambie si baja: registros acumulados, descargas, páginas vistas. Tiene dos defectos típicos: es acumulada (solo sube) y no está ligada a un comportamiento de valor. La prueba es preguntar qué se haría distinto si la cifra bajara a la mitad; si la respuesta es «nada», es de vanidad.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md):

En la plataforma, `metric-audit.md` tiene una fila por métrica con definición calculable (numerador, denominador, ventana, filtros), tipo (producción, actividad, resultado, vanidad), decisión que informa, métrica contraria y fecha de revisión. El contrato es que ninguna métrica se convierte en meta sin su métrica contraria y sin la pregunta «qué haría distinto si bajara». Esa estructura permite que otra persona detecte metas sin contrapeso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)) son:

- **La meta se cumple y nadie mejora** — causa: se premió la producción. Corrección: reemplazar o acompañar con un resultado y su métrica contraria.
- **El panel solo muestra crecimiento** — causa: la métrica es acumulada. Corrección: usar métricas por periodo (activos del mes, retenidos).

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún equipo, producto ni persona; los parámetros de cierre, reapertura, permanencia y pesos de calidad y hábito son supuestos del autor. La siguiente clase define métricas de adopción, retención y tarea útil que sí aproximan resultados.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Baja](../b/baja.md), [Actividad](../a/actividad.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Producción](../p/produccion.md), [Resultado](../r/resultado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-135 — Resultados, outputs, actividad y vanity metrics](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Métricas de vanidad».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — definir qué medir a partir de lo que se necesita saber; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring user satisfaction](https://www.gov.uk/service-manual/measuring-success/measuring-user-satisfaction) — cómo medir satisfacción como complemento de indicadores de uso; autoridad: Government Digital Service.
- [Categorizing Variants of Goodhart's Law](https://arxiv.org/abs/1803.04585) — mecanismos por los que una medida deja de informar al volverse objetivo; autoridad: investigación publicada en arXiv (D. Manheim y S. Garrabrant).
- [DORA: Software delivery performance metrics](https://dora.dev/guides/dora-metrics-four-keys/) — conjunto equilibrado de métricas de entrega; autoridad: DORA (Google Cloud).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — medición y economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Métrica de valor](./metrica-de-valor.md) · [Métrica facturable →](./metrica-facturable.md)
