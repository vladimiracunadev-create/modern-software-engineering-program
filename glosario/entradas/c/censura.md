# Censura

[↑ Glosario](../../README.md) · [← Celda](./celda.md) · [Ceremonia ritual →](./ceremonia-ritual.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Ausencia de datos porque el tiempo de observación aún no alcanzó la ventana medida.

Definición de trabajo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Por qué importa

En [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), el tema «Censura e incertidumbre» importa porque una cohorte reciente no ha tenido tiempo; una pequeña tiene un intervalo ancho.

## Cómo funciona

Según [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md):

Una cohorte de hace 10 días no puede mostrar retención a 30 días: la información aún no existe (censura por la derecha). Contar a esas personas como «no retenidas» sesga hacia abajo. Y una cohorte pequeña tiene un intervalo ancho: con 50 personas, una retención de 34 % es compatible con valores entre 22 % y 48 %.

Según [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md):

Puede escribir el código, pero debes dar la definición de población, evento y ventana, y comprobar que respeta la censura. Un cálculo generado sin esa especificación suele usar «usuarios con algún evento» como denominador, que es otra cohorte.

## Ejemplo

Ejemplo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sección «Preguntas frecuentes»):

Puede escribir el código, pero debes dar la definición de población, evento y ventana, y comprobar que respeta la censura. Un cálculo generado sin esa especificación suele usar «usuarios con algún evento» como denominador, que es otra cohorte.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son:

- **La retención «mejora» sola en las cohortes nuevas** — causa: se contó a quienes no han cumplido la ventana. Corrección: medir solo cohortes completas y rotular las parciales.
- **Dos paneles dan DAU/MAU de 28 % y 8 %** — causa: distinto evento de activo. Corrección: publicar el evento y la ventana en cada cifra.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una cohorte de hace 10 días no puede mostrar retención a 30 días: la información aún no existe (censura por la derecha). ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Medida](../m/medida.md), [Observación](../o/observacion.md), [Ventana](../v/ventana.md), [Adopción](../a/adopcion.md), [Heterogeneidad](../h/heterogeneidad.md), [Retención por cohorte](../r/retencion-por-cohorte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

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

[↑ Glosario](../../README.md) · [← Celda](./celda.md) · [Ceremonia ritual →](./ceremonia-ritual.md)
