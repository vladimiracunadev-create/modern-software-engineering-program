# Fatiga de alertas

[↑ Glosario](../../README.md) · [← Fatiga de alarmas](./fatiga-de-alarmas.md) · [Fatiga de aprobación →](./fatiga-de-aprobacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Disminución de la respuesta a las alertas por exceso o repetición.

Definición de trabajo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

## Por qué importa

La clase donde se define, [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), existe con este propósito: la clase existe para que diseñes alertas que despierten a una persona solo cuando hay algo que hacer ahora, para que las derives del consumo del presupuesto de error en lugar de umbrales arbitrarios y para que midas el ruido que generan.

## Cómo funciona

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

La **fatiga de alertas** es la disminución de la respuesta a una alerta a medida que se repite o que se acumula con muchas otras. El fenómeno está documentado en entornos clínicos, donde la probabilidad de aceptar una alerta repetida baja, y en operaciones de software se observa como guardias que silencian en bloque, que tardan más en reconocer la página o que dejan de abrir el runbook. El coste no es proporcional: una página inútil no cuesta solo su duración, cuesta credibilidad a las siguientes. La métrica de salud de un conjunto de alertas es la fracción de páginas que llevaron a una acción, y se revisa cada trimestre eliminando o degradando las que no.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reduce las 40 alertas de la API de entregas a seis páginas y cuatro tickets. Las páginas son: consumo 14,4× del SLO de entregas (1 h y 5 min), consumo 6× (6 h y 30 min, que genera ticket por la noche), cola de trabajos sin avanzar durante 15 minutos, base de datos sin réplica sana, certificado a menos de siete días de vencer y sonda externa sin respuesta durante tres lecturas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)) son:

- **Suenan muchas páginas en un incidente** — causa: una causa genera alertas en todos los servicios. Corrección: agrupar e inhibir por dependencia.
- **Despiertan de noche sin incidente** — causa: ventana corta con poco tráfico. Corrección: ventanas largas, volumen mínimo o regla de consumo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Repetición](../r/repeticion.md), [Agrupación](../a/agrupacion.md), [Alerta de varias ventanas](../a/alerta-de-varias-ventanas.md), [Página](../p/pagina.md), [Tasa de consumo](../t/tasa-de-consumo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Ancker et al., «Effects of workload, work complexity, and repeated alerts on alert fatigue»](https://doi.org/10.1186/s12911-017-0430-8) — fatiga de alertas en un entorno clínico; autoridad: BMC Medical Informatics and Decision Making, 2017.
- [Google SRE Workbook: Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) — alertas por consumo del presupuesto y ventanas; autoridad: Google, SRE Workbook.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertar sobre síntomas; autoridad: libro de ingeniería de confiabilidad de Google.
- [Prometheus: Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) — agrupación, inhibición y silenciamiento; autoridad: documentación del proyecto Prometheus.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — carga de la guardia y cómo medirla; autoridad: Google, SRE Workbook.

---

[↑ Glosario](../../README.md) · [← Fatiga de alarmas](./fatiga-de-alarmas.md) · [Fatiga de aprobación →](./fatiga-de-aprobacion.md)
