# Tarea útil

[↑ Glosario](../../README.md) · [← Tarea determinista](./tarea-determinista.md) · [Tarjeta de agente →](./tarjeta-de-agente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Evento que prueba que la persona logró lo que buscaba (en la plataforma, una entrega aceptada).

Definición de trabajo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).

## Por qué importa

En [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), el tema «Tarea útil» importa porque el evento que prueba un logro decide qué se premia; cambiarlo cambia todas las cifras posteriores.

## Cómo funciona

Según [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), en la sección «Tarea útil»:

La tarea útil es el evento que prueba que alguien obtuvo valor: en la plataforma, una entrega aceptada, no un inicio de sesión. Elegirla es una decisión de producto, no de analítica, y se valida preguntando si quien la hizo diría que logró lo que buscaba. Una tarea útil demasiado fácil de lograr se vuelve actividad; una demasiado rara no ofrece datos.

## Ejemplo

Ejemplo de [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) (sección «Caso conductor»):

La plataforma de entregas continúa como caso. Esta clase deja las definiciones calculables que `SE-139` usará para elegir una métrica norte y `SE-137` para decidir qué eventos recoger. Cambia después una sola definición —por ejemplo, el evento de tarea útil— y revisa qué conclusiones del registro cambian.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)) son:

- **La retención «mejora» sola en las cohortes nuevas** — causa: se contó a quienes no han cumplido la ventana. Corrección: medir solo cohortes completas y rotular las parciales.
- **Dos paneles dan DAU/MAU de 28 % y 8 %** — causa: distinto evento de activo. Corrección: publicar el evento y la ventana en cada cifra.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La tarea útil es el evento que prueba que alguien obtuvo valor: en la plataforma, una entrega aceptada, no un inicio de sesión. ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md))
- Traslada el experimento a otro dominio persistente (por ejemplo, un servicio de reparto con comercios): cambia la tarea útil por «pedido entregado» y los segmentos por «comercio frecuente» y «ocasional»; conserva el contrato de métrica y comprueba si la curva agregada vuelve a aplanarse sin que ninguna persona decaiga más despacio. ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Plataforma](../p/plataforma.md), [Adopción](../a/adopcion.md), [Censura](../c/censura.md), [Heterogeneidad](../h/heterogeneidad.md), [Retención por cohorte](../r/retencion-por-cohorte.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-136 — Métricas de adopción, retención y tarea útil](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-135](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-135-resultados-outputs-actividad-y-vanity-metrics/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md).

**Aparece en los casos de estudio:** [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Tarea determinista](./tarea-determinista.md) · [Tarjeta de agente →](./tarjeta-de-agente.md)
