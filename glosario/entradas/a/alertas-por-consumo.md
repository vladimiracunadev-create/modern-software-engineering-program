# Alertas por consumo

[↑ Glosario](../../README.md) · [← Alerta de varias ventanas](./alerta-de-varias-ventanas.md) · [Algoritmo →](./algoritmo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Alertar cuando el error pasa de un umbral absoluto avisa tarde o con ruido. La **tasa de consumo** (burn rate) divide el error observado entre el presupuesto: una tasa de 14,4 significa que, de seguir así, el presupuesto del mes se agota en dos días. Se combinan dos ventanas (por ejemplo una hora y cinco minutos) para detectar rápido y evitar falsos positivos, y una ventana lenta para incidentes que consumen despacio. Aun así hay incidentes que ninguna alerta ve si consumen justo por debajo del umbral.

Explicación de la sección «Alertas por consumo» de [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md).

## Por qué importa

En [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), el tema «Alertas por consumo» importa porque una alerta por tasa de consumo detecta incidentes que una alerta por umbral absoluto no ve.

En [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), el tema «Alertas por consumo» importa porque convierten un objetivo en una condición verificable.

## Cómo funciona

Según [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), en la sección «Alertas por consumo»:

Alertar cuando el error pasa de un umbral absoluto avisa tarde o con ruido. La **tasa de consumo** (burn rate) divide el error observado entre el presupuesto: una tasa de 14,4 significa que, de seguir así, el presupuesto del mes se agota en dos días. Se combinan dos ventanas (por ejemplo una hora y cinco minutos) para detectar rápido y evitar falsos positivos, y una ventana lenta para incidentes que consumen despacio. Aun así hay incidentes que ninguna alerta ve si consumen justo por debajo del umbral.

## Ejemplo

Caso medido en la sección «Alertas por consumo» de [SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md):

Alertar cuando el error pasa de un umbral absoluto avisa tarde o con ruido. La **tasa de consumo** (burn rate) divide el error observado entre el presupuesto: una tasa de 14,4 significa que, de seguir así, el presupuesto del mes se agota en dos días. Se combinan dos ventanas (por ejemplo una hora y cinco minutos) para detectar rápido y evitar falsos positivos, y una ventana lenta para incidentes que consumen despacio. Aun así hay incidentes que ninguna alerta ve si consumen justo por debajo del umbral.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md)) son:

- **El contrato y el código divergen** — causa: no hay comprobación de conformidad. Corrección: comparador en la integración continua con esquema cerrado.
- **Hay entregas duplicadas o sin nota tras un reinicio** — causa: efectos fuera de la transacción y handler no idempotente. Corrección: clave, outbox y efecto idempotente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-252 — Proyecto: servicio contractual operable](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se desplegó ningún servicio ni se midió a ninguna persona: las caídas, el SLO, los incidentes y las mutaciones son construcciones del autor. La [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) lleva el producto a móviles y escritorio.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-251](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-251-taller-reparar-una-api-insegura-e-inconsistente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agrupación](./agrupacion.md), [Alerta de varias ventanas](./alerta-de-varias-ventanas.md), [Burn rate](../b/burn-rate.md), [Conformidad](../c/conformidad.md), [Fatiga de alertas](../f/fatiga-de-alertas.md), [Indicador de nivel de servicio](../i/indicador-de-nivel-de-servicio.md).
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
- [Google SRE Book: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y presupuesto de error; autoridad: Google.
- [Google SRE Book: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales y alertas sobre síntomas; autoridad: Google.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de contratos de API; autoridad: OpenAPI Initiative.
- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — esquemas cerrados de entrada y salida; autoridad: proyecto JSON Schema.

---

[↑ Glosario](../../README.md) · [← Alerta de varias ventanas](./alerta-de-varias-ventanas.md) · [Algoritmo →](./algoritmo.md)
