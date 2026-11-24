# Guardia

[↑ Glosario](../../README.md) · [← Guarda de versión](./guarda-de-version.md) · [Guardrail →](./guardrail.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

La **guardia** (*on-call*) es el turno en que una persona o grupo responde a las páginas de un servicio ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)).

## Por qué importa

La guardia es un sistema con una capacidad finita. Si se diseña sin calcularla, termina siendo siempre la misma persona, con sueño interrumpido y rotación de personal. La sostenibilidad de la guardia es una condición de la fiabilidad del servicio.

## Cómo funciona

Una persona en guardia una semana de cada *n* atiende todas las páginas de esa semana, y las nocturnas interrumpen el sueño. Con pocas personas, cada una pasa muchas semanas al año en guardia, y las ausencias (vacaciones, enfermedad, formación) concentran la carga en quienes quedan. [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) cita el libro de SRE: no más del 25 % del tiempo de una persona debe ser de guardia, de lo que se deduce un mínimo de personas para una rotación continua con primaria y secundaria (ocho en un solo sitio), además de limitar las incidencias por turno. La medida concreta de sostenibilidad es el número de noches interrumpidas por persona y por periodo.

## Ejemplo

[SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) (caso hipotético): el equipo reescribe el runbook de `EntregasConsumoRapido`, lo guarda junto al código y añade un verificador de integración continua (campos, comandos con salida esperada, reversión de lo destructivo, fecha menor de 90 días y alerta existente en el catálogo). Cada trimestre una persona que no lo escribió lo ejecuta en pruebas con un despliegue defectuoso inyectado.

## Errores y confusiones comunes

**La guardia es siempre la misma persona.** Equipo pequeño o ausencias sin plan; calcular la carga y ampliar la rotación o reducir el alcance.

## Límites y cuándo no aplica

Las cifras (25 %, ocho personas) son de un modelo de operación grande; un equipo pequeño debe reducir el alcance del servicio que cubre o compartir la rotación, no copiar el número.

## Relación con otros conceptos

- **Prerrequisito:** [Página](../p/pagina.md).
- **Ver también:** [Servicio](../s/servicio.md), [Causa común](../c/causa-comun.md), [Ejercicio de runbook](../e/ejercicio-de-runbook.md), [Escalamiento](../e/escalamiento.md), [Mantenimiento](../m/mantenimiento.md), [Runbook](../r/runbook.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (37 clases más lo mencionan; las que más):

[SE-530](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-530-diseno-de-equipos-y-ownership/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), [SE-009](../../../classes/part-00-ingenieria-de-software-como-profesion/se-009-sostenibilidad-inclusion-y-responsabilidad-social/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Shopify](../../../casos/exito/shopify.md), [Discord](../../../casos/exito/discord.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «on-call».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Being On-Call](https://sre.google/sre-book/being-on-call/) — carga y tamaño de la guardia; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — medir y mejorar la guardia; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — procesos públicos de guardia y respuesta; autoridad: documentación pública de PagerDuty.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertas con acción clara; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: datetime](https://docs.python.org/3/library/datetime.html) — fechas usadas por el verificador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Guarda de versión](./guarda-de-version.md) · [Guardrail →](./guardrail.md)
