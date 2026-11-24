# Tarea útil

[↑ Glosario](../../README.md) · [← Tarea determinista](./tarea-determinista.md) · [Tarjeta de agente →](./tarjeta-de-agente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

La **tarea útil** es el evento que prueba que la persona logró lo que buscaba; en la plataforma de entregas, una entrega aceptada ([SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md)). No es un inicio de sesión ni una visita: es el evento que representa un logro real. Es la base con la que se definen la retención y la adopción.

## Por qué importa

El evento que prueba un logro decide qué se premia; cambiarlo cambia todas las cifras posteriores. Si la «tarea útil» es abrir la aplicación, la retención mide hábito de abrir; si es una entrega aceptada, mide si la gente consigue lo que vino a hacer. Cambia qué significa «activo» en todo el panel.

## Cómo funciona

[SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) dice que la tarea útil es el evento que prueba que alguien **obtuvo valor**. Elegirla es **una decisión de producto, no de analítica**, y se valida preguntando si quien la hizo **diría que logró lo que buscaba**. Si la respuesta es «no necesariamente», el evento es una actividad, no una tarea útil.

Dos riesgos opuestos. Una tarea útil **demasiado fácil de lograr** se vuelve actividad: casi todo el mundo la realiza y no distingue a quien obtiene valor. Una **demasiado rara** no ofrece datos: la mayoría nunca la alcanza y las cifras tienen ruido. El punto medio es un evento frecuente entre quienes consiguen valor y poco frecuente entre quienes no.

Sobre ella se construyen la **adopción** (centros con al menos una tarea útil en los primeros 14 días sobre centros con cuenta activada) y la **retención por cohorte** (fracción de la cohorte que repite la tarea útil en la semana k). Por eso «dos paneles dan DAU/MAU de 28 % y 8 %» cuando usan distinto evento de activo; la corrección es publicar el evento y la ventana en cada cifra. Otro error: la retención «mejora» sola en las cohortes nuevas porque se contó a quienes no cumplieron la ventana; se miden cohortes completas.

[SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md) propone transferirlo a otro dominio: en un servicio de reparto con comercios, la tarea útil sería «pedido entregado» y los segmentos «comercio frecuente» y «ocasional»; se conserva el contrato de la métrica y se comprueba si la curva agregada vuelve a aplanarse sin que ninguna persona decaiga más despacio.

## Ejemplo

Plataforma de entregas. Candidatas: «iniciar sesión» (demasiado fácil: casi toda la base lo hace; es actividad), «subir un archivo» (cercana pero incluye intentos fallidos) y «entrega aceptada» (la persona logró lo que buscaba). Se elige la tercera, y la retención de la semana 4 se define como la fracción de la cohorte con una entrega aceptada en esa semana. (Ejemplo ilustrativo en la línea de [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md).)

## Errores y confusiones comunes

- **Elegir un evento que es actividad.**
- **Cambiar la tarea útil sin avisar**: se rompen las series.
- **Paneles con distinto evento de activo.**
- **Tarea tan rara que no da datos.**

## Límites y cuándo no aplica

Para productos con múltiples trabajos, una sola tarea útil no los representa; se define una por trabajo o segmento. Algunos logros no se observan como evento (un beneficio indirecto) y se aproximan con encuestas. La tarea útil sigue siendo un proxy del valor, no el valor.

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
