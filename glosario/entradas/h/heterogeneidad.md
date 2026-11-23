# Heterogeneidad

[↑ Glosario](../../README.md) · [← Herramientas](./herramientas.md) · [Heurística →](./heuristica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Coexistencia de segmentos con comportamientos distintos dentro de una misma curva.

Definición de trabajo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Por qué importa

En [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), el tema «Segmentos y heterogeneidad» importa porque una curva promedio puede esconder dos poblaciones con comportamientos opuestos.

## Cómo funciona

[SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md):

En la plataforma, `adoption-metrics.md` define cada métrica con población, evento, ventana y filtros: adopción es «centros con al menos una entrega aceptada en los primeros 14 días, sobre centros con cuenta activada»; retención es «estudiantes con una entrega aceptada en la semana k sobre quienes tuvieron una en la semana 0». El contrato es que ninguna cifra se publica sin n, sin edad mínima de la cohorte y sin su intervalo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son:

- **La retención «mejora» sola en las cohortes nuevas** — causa: se contó a quienes no han cumplido la ventana. Corrección: medir solo cohortes completas y rotular las parciales.
- **Dos paneles dan DAU/MAU de 28 % y 8 %** — causa: distinto evento de activo. Corrección: publicar el evento y la ventana en cada cifra.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son: Las definiciones son operativas para la plataforma de entregas y deben contrastarse con las fuentes enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió a ninguna persona; los segmentos, las tasas y las probabilidades son supuestos del autor, y el modelo omite estacionalidad y correlación entre eventos. La siguiente clase pregunta con qué consentimiento y con qué minimización se pueden recoger los eventos que estas métricas necesitan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Segmento](../s/segmento.md), [Adopción](../a/adopcion.md), [Censura](../c/censura.md), [Retención por cohorte](../r/retencion-por-cohorte.md), [Tarea útil](../t/tarea-util.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GOV.UK Service Manual: Measuring completion rate](https://www.gov.uk/service-manual/measuring-success/measuring-completion-rate) — finalización con numerador y denominador explícitos; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: Measuring digital take-up](https://www.gov.uk/service-manual/measuring-success/measuring-digital-take-up) — adopción sobre una población declarada; autoridad: Government Digital Service.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — qué medir y para qué decisión; autoridad: Government Digital Service.
- [NIST/SEMATECH e-Handbook of Statistical Methods: Proportions](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) — intervalos de confianza para proporciones; autoridad: NIST.
- [Google Research: HEART framework](https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/) — marco de métricas de experiencia de usuario (felicidad, compromiso, adopción, retención, éxito en la tarea); autoridad: Google Research.

---

[↑ Glosario](../../README.md) · [← Herramientas](./herramientas.md) · [Heurística →](./heuristica.md)
