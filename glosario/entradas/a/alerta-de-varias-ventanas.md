# Alerta de varias ventanas

[↑ Glosario](../../README.md) · [← Alcanzabilidad](./alcanzabilidad.md) · [Alertas por consumo →](./alertas-por-consumo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Regla que exige que la condición se cumpla en una ventana larga y en una corta.

Definición de trabajo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

## Por qué importa

La clase donde se define, [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), existe con este propósito: la clase existe para que diseñes alertas que despierten a una persona solo cuando hay algo que hacer ahora, para que las derives del consumo del presupuesto de error en lugar de umbrales arbitrarios y para que midas el ruido que generan.

## Cómo funciona

[SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reduce las 40 alertas de la API de entregas a seis páginas y cuatro tickets. Las páginas son: consumo 14,4× del SLO de entregas (1 h y 5 min), consumo 6× (6 h y 30 min, que genera ticket por la noche), cola de trabajos sin avanzar durante 15 minutos, base de datos sin réplica sana, certificado a menos de siete días de vencer y sonda externa sin respuesta durante tres lecturas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)) son:

- **Suenan muchas páginas en un incidente** — causa: una causa genera alertas en todos los servicios. Corrección: agrupar e inhibir por dependencia.
- **Despiertan de noche sin incidente** — causa: ventana corta con poco tráfico. Corrección: ventanas largas, volumen mínimo o regla de consumo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Regla](../r/regla.md), [Ventana](../v/ventana.md), [Agrupación](./agrupacion.md), [Fatiga de alertas](../f/fatiga-de-alertas.md), [Página](../p/pagina.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — alertas por consumo del presupuesto y ventanas; autoridad: Google, SRE Workbook.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertar sobre síntomas; autoridad: libro de ingeniería de confiabilidad de Google.
- [Prometheus: Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) — agrupación, inhibición y silenciamiento; autoridad: documentación del proyecto Prometheus.
- [Ancker et al., «Effects of workload, work complexity, and repeated alerts on alert fatigue»](https://doi.org/10.1186/s12911-017-0430-8) — fatiga de alertas en un entorno clínico; autoridad: BMC Medical Informatics and Decision Making, 2017.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — carga de la guardia y cómo medirla; autoridad: Google, SRE Workbook.

---

[↑ Glosario](../../README.md) · [← Alcanzabilidad](./alcanzabilidad.md) · [Alertas por consumo →](./alertas-por-consumo.md)
