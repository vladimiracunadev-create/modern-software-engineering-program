# Agrupación

[↑ Glosario](../../README.md) · [← Agregado](./agregado.md) · [Agrupar por necesidad →](./agrupar-por-necesidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Unión de alertas relacionadas en una sola notificación.

Definición de trabajo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

## Por qué importa

En [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), el tema «Ruido y agrupación» importa porque una causa produce muchas alertas.

## Cómo funciona

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Un incidente raramente genera una alerta: una dependencia lenta hace saltar alertas en todos los servicios que la llaman. Tres técnicas reducen ese ruido sin perder la señal. La **duración mínima** (`for`) exige que la condición se mantenga unos minutos antes de paginar, lo que descarta los destellos que se resuelven solos. La **agrupación** une en una sola notificación las alertas con un mismo contexto (el mismo servicio, la misma región). La **inhibición** silencia las alertas derivadas mientras la causa raíz está activa. Cada una cuesta algo: la duración mínima retrasa la página, la agrupación exige conocer el mapa de dependencias y la inhibición puede esconder una segunda falla detrás de la primera.

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Sí. Una página agrupada puede ocultar un segundo problema distinto. Por eso la agrupación se acompaña de un resumen de qué alertas contiene y de una revisión posterior a cada incidente que verifique si algo quedó oculto.

## Ejemplo

Ejemplo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sección «Preguntas frecuentes»):

Sí. Una página agrupada puede ocultar un segundo problema distinto. Por eso la agrupación se acompaña de un resumen de qué alertas contiene y de una revisión posterior a cada incidente que verifique si algo quedó oculto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)) son:

- **Suenan muchas páginas en un incidente** — causa: una causa genera alertas en todos los servicios. Corrección: agrupar e inhibir por dependencia.
- **Despiertan de noche sin incidente** — causa: ventana corta con poco tráfico. Corrección: ventanas largas, volumen mínimo o regla de consumo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada una cuesta algo: la duración mínima retrasa la página, la agrupación exige conocer el mapa de dependencias y la inhibición puede esconder una segunda falla detrás de la primera. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alerta de varias ventanas](./alerta-de-varias-ventanas.md), [Fatiga de alertas](../f/fatiga-de-alertas.md), [Página](../p/pagina.md), [Tasa de consumo](../t/tasa-de-consumo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (27 clases más lo mencionan; las que más):

[SE-131](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-131-taller-convertir-una-peticion-en-un-problema-investigable/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-121](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-121-problemas-sintomas-necesidades-y-oportunidades/README.md), [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md), [SE-559](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-559-revision-refactorizacion-y-explicacion-asistidas/README.md), [SE-037](../../../classes/part-03-redes-internet-y-protocolos/se-037-modelos-osi-y-tcp-ip-como-herramientas-de-diagnostico/README.md), [SE-149](../../../classes/part-12-ingenieria-de-requisitos/se-149-criterios-de-aceptacion-y-ejemplos/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md).

**Aparece en los casos de estudio:** [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Prometheus: Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) — agrupación, inhibición y silenciamiento; autoridad: documentación del proyecto Prometheus.
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — alertas por consumo del presupuesto y ventanas; autoridad: Google, SRE Workbook.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertar sobre síntomas; autoridad: libro de ingeniería de confiabilidad de Google.
- [Ancker et al., «Effects of workload, work complexity, and repeated alerts on alert fatigue»](https://doi.org/10.1186/s12911-017-0430-8) — fatiga de alertas en un entorno clínico; autoridad: BMC Medical Informatics and Decision Making, 2017.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — carga de la guardia y cómo medirla; autoridad: Google, SRE Workbook.

---

[↑ Glosario](../../README.md) · [← Agregado](./agregado.md) · [Agrupar por necesidad →](./agrupar-por-necesidad.md)
