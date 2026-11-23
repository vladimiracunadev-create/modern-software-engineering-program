# Página

[↑ Glosario](../../README.md) · [← Page fault](./page-fault.md) · [Página huérfana →](./pagina-huerfana.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Alerta que interrumpe de inmediato a una persona porque exige acción ahora.

Definición de trabajo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md): Unidad de mapeo de memoria virtual.

## Por qué importa

En [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), el tema «Página, ticket y registro» importa porque cada urgencia merece un canal distinto.

## Cómo funciona

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Una condición puede comunicarse de tres maneras. Una **página** interrumpe a una persona de inmediato y se reserva para lo que exige acción ahora. Un **ticket** se atiende en horario laboral y sirve para lo que no puede esperar demasiado pero no justifica interrumpir. Un **registro** (o un panel) conserva el dato para quien lo consulte. Tres preguntas ordenan la decisión: ¿afecta ya o afectará pronto a quien usa el servicio?, ¿es accionable por la persona de guardia con lo que sabe?, ¿puede esperar a mañana sin consecuencias? Una página que falla alguna de las tres es ruido.

Según [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reduce las 40 alertas de la API de entregas a seis páginas y cuatro tickets. Las páginas son: consumo 14,4× del SLO de entregas (1 h y 5 min), consumo 6× (6 h y 30 min, que genera ticket por la noche), cola de trabajos sin avanzar durante 15 minutos, base de datos sin réplica sana, certificado a menos de siete días de vencer y sonda externa sin respuesta durante tres lecturas. Cada alerta enlaza con su runbook (`SE-499`), tiene propietario y una nota de «qué hacer en cinco minutos». Las alertas de causa (CPU, memoria, disco) pasan a paneles o a tickets con umbrales conservadores.

## Ejemplo

Ejemplo de [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reduce las 40 alertas de la API de entregas a seis páginas y cuatro tickets. Las páginas son: consumo 14,4× del SLO de entregas (1 h y 5 min), consumo 6× (6 h y 30 min, que genera ticket por la noche), cola de trabajos sin avanzar durante 15 minutos, base de datos sin réplica sana, certificado a menos de siete días de vencer y sonda externa sin respuesta durante tres lecturas. Cada alerta enlaza con su runbook (`SE-499`), tiene propietario y una nota de «qué hacer en cinco minutos».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Suenan muchas páginas en un incidente** — causa: una causa genera alertas en todos los servicios. Corrección: agrupar e inhibir por dependencia. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))
- **Se silencia en bloque** — causa: fatiga por páginas sin acción. Corrección: retirar o degradar las que no llevan a acción. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para degradaciones lentas se añade una tasa menor con una ventana mayor (6 veces durante 6 horas, con una corta de 30 minutos) que suele generar un ticket y no una página. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))
- No hay un número universal: en la práctica un servicio bien mantenido tiene pocas páginas (de cinco a diez) y más tickets. ([SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Memoria virtual](../m/memoria-virtual.md), [Agrupación](../a/agrupacion.md), [Alerta de varias ventanas](../a/alerta-de-varias-ventanas.md), [Ancho de banda](../a/ancho-de-banda.md), [Fatiga de alertas](../f/fatiga-de-alertas.md), [Latencia](../l/latencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-018 — Memoria, cachés, almacenamiento y jerarquías](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-498 — Alertas accionables y fatiga](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (129 clases más lo mencionan; las que más):

[SE-213](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-213-busqueda-glosarios-y-arquitectura-de-conocimiento/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), [SE-206](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-206-tutoriales-how-to-referencia-y-explicacion/README.md), [SE-238](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-238-seo-metadatos-y-descubribilidad/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-231](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-231-renderizado-cliente-servidor-estatico-e-hibrido/README.md), [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md).

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

[↑ Glosario](../../README.md) · [← Page fault](./page-fault.md) · [Página huérfana →](./pagina-huerfana.md)
