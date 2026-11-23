# Tasa de consumo

[↑ Glosario](../../README.md) · [← Tasa de aciertos](./tasa-de-aciertos.md) · [Tasa de fallos de los cambios →](./tasa-de-fallos-de-los-cambios.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Cuántas veces más rápido que el ritmo normal se gasta el presupuesto de error.

Definición de trabajo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md): Cociente entre el error observado y el presupuesto; mide la velocidad a la que se agota.

## Por qué importa

La clase donde se define, [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), existe con este propósito: la clase existe para que diseñes alertas que despierten a una persona solo cuando hay algo que hacer ahora, para que las derives del consumo del presupuesto de error en lugar de umbrales arbitrarios y para que midas el ruido que generan.

## Cómo funciona

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Con un SLO se puede alertar por **tasa de consumo** (burn rate): cuántas veces más rápido que el ritmo normal se gasta el presupuesto. Con un SLO de 99,9 % el presupuesto se gasta en 28 días a una tasa de 1; una tasa de error de 1,44 % es una tasa de consumo de 14,4, y agota el presupuesto del mes en unas 47 horas. La regla de consumo exige además **dos ventanas**: una larga (una hora) que confirma que el consumo es sostenido, y una corta (cinco minutos) que confirma que sigue ocurriendo ahora y permite que la alerta se apague pronto cuando el problema se arregla.

Según [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md):

Alertar cuando el error pasa de un umbral absoluto avisa tarde o con ruido. La **tasa de consumo** (burn rate) divide el error observado entre el presupuesto: una tasa de 14,4 significa que, de seguir así, el presupuesto del mes se agota en dos días. Se combinan dos ventanas (por ejemplo una hora y cinco minutos) para detectar rápido y evitar falsos positivos, y una ventana lenta para incidentes que consumen despacio. Aun así hay incidentes que ninguna alerta ve si consumen justo por debajo del umbral.

## Ejemplo

Ejemplo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la tasa de consumo y el tiempo que tardaría en agotarse el presupuesto. Antes de ejecutarlo, predice el resultado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los docentes avisan antes que las alertas** — causa: alertas solo por umbral absoluto. Corrección: alertas por tasa de consumo con dos ventanas. ([SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las reglas por umbral en ventanas cortas generan cientos o miles de páginas, la mayoría sin incidente; las reglas por tasa de consumo del presupuesto generan decenas y ninguna sin incidente. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Presupuesto de error](../p/presupuesto-de-error.md), [Presupuesto](../p/presupuesto.md), [Agrupación](../a/agrupacion.md), [Alerta de varias ventanas](../a/alerta-de-varias-ventanas.md), [Burn rate](../b/burn-rate.md), [Conformidad](../c/conformidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
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

[↑ Glosario](../../README.md) · [← Tasa de aciertos](./tasa-de-aciertos.md) · [Tasa de fallos de los cambios →](./tasa-de-fallos-de-los-cambios.md)
