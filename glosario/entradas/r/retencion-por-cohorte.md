# Retención por cohorte

[↑ Glosario](../../README.md) · [← Retención legal](./retencion-legal.md) · [Retirar del reparto →](./retirar-del-reparto.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Fracción de las personas que empezaron en un periodo y repiten la tarea útil k periodos después.

Definición de trabajo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Por qué importa

En [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), el tema «Retención por cohortes» importa porque mide si quienes llegaron en un periodo vuelven; las cifras agregadas mezclan edades.

## Cómo funciona

Según [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), en la sección «Retención por cohortes»:

Una cohorte es el grupo de personas que empezaron en un mismo periodo; la retención en la semana k es la fracción de la cohorte que realiza la tarea útil en esa semana. Comparar cohortes de la misma edad evita mezclar a quien lleva dos días con quien lleva dos meses. La retención de la semana 1 en la cohorte de ayer no es comparable con la de la semana 12 de hace seis meses.

## Ejemplo

Caso medido en la sección «Retención por cohortes» de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md):

Una cohorte es el grupo de personas que empezaron en un mismo periodo; la retención en la semana k es la fracción de la cohorte que realiza la tarea útil en esa semana. Comparar cohortes de la misma edad evita mezclar a quien lleva dos días con quien lleva dos meses. La retención de la semana 1 en la cohorte de ayer no es comparable con la de la semana 12 de hace seis meses.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son:

- **La retención «mejora» sola en las cohortes nuevas** — causa: se contó a quienes no han cumplido la ventana. Corrección: medir solo cohortes completas y rotular las parciales.
- **Dos paneles dan DAU/MAU de 28 % y 8 %** — causa: distinto evento de activo. Corrección: publicar el evento y la ventana en cada cifra.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona; los segmentos, las tasas y las probabilidades son supuestos del autor, y el modelo omite estacionalidad y correlación entre eventos. La siguiente clase pregunta con qué consentimiento y con qué minimización se pueden recoger los eventos que estas métricas necesitan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea útil](../t/tarea-util.md), [Tarea](../t/tarea.md), [Adopción](../a/adopcion.md), [Censura](../c/censura.md), [Heterogeneidad](../h/heterogeneidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Retención por cohortes».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring completion rate](https://www.gov.uk/service-manual/measuring-success/measuring-completion-rate) — finalización con numerador y denominador explícitos; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring digital take-up](https://www.gov.uk/service-manual/measuring-success/measuring-digital-take-up) — adopción sobre una población declarada; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — qué medir y para qué decisión; autoridad: Government Digital Service.
- [NIST/SEMATECH e-Handbook of Statistical Methods: Proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) — intervalos de confianza para proporciones; autoridad: NIST.
- [Google Research: HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — marco de métricas de experiencia de usuario (felicidad, compromiso, adopción, retención, éxito en la tarea); autoridad: Google Research.

---

[↑ Glosario](../../README.md) · [← Retención legal](./retencion-legal.md) · [Retirar del reparto →](./retirar-del-reparto.md)
