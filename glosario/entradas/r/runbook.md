# Runbook

[↑ Glosario](../../README.md) · [← Ruido de evaluación](./ruido-de-evaluacion.md) · [Runtime →](./runtime.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Procedimiento paso a paso para una situación operacional conocida, ejecutable sin conocer el sistema.

Definición de trabajo de [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md): Documento operativo que acompaña a una alerta y describe diagnóstico, mitigación, verificación, reversión y escalamiento.

## Por qué importa

En [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md), el tema «Runbook» importa porque reduce el tiempo de decisión.

## Cómo funciona

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

Las dos primeras son fallas de datos (de ingeniería); las otras dos, cambios del mundo. El diagnóstico y la mitigación correctos son distintos para cada una, y esa es la razón por la que el runbook pregunta primero qué clase de falla es.

Según [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Ejemplo

Ejemplo de [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) (sección «Ejemplo profesional»):

El equipo de *Avisos-ML* ejecuta el ensayo un martes con la persona de guardia sin aviso. La falla de unidad se inyecta a las 10:00. A las 10:02 llega el aviso de la validación de entrada a la persona de guardia, que abre el runbook, ve la rama «falla de calidad de entrada» y confirma que la tasa de lectura llega en porcentaje. A las 10:20 despliega una corrección de la conversión en el servicio y verifica en el tablero que la tasa de marcados vuelve a su banda. El incidente se cierra a las 10:45.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un incidente nuevo deja a la guardia sin guía** — causa: solo hay runbooks, no playbook. Corrección: escribir un playbook de preguntas y criterios de escalada. ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md))
- **El runbook dice «revisa los servicios»** — causa: pasos sin comando ni salida esperada. Corrección: un paso por acción, con comando y resultado esperado. ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md))
- **El runbook falla al ejecutarse** — causa: deriva: el sistema cambió. Corrección: fecha de verificación, ejercicio y cambio conjunto con el sistema. ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Ensayar con inyección de fallas en un sistema que no tiene aún monitores ni runbook produce un incidente en lugar de un ensayo: primero el diseño y las pruebas por separado. ([SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md))
- La transferencia está lograda cuando puedes decir qué paso del runbook sería falso con un cambio previsible del sistema y cómo te enterarías, no cuando existe un documento. ([SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Diagnóstico](../d/diagnostico.md), [Documento](../d/documento.md), [Escalamiento](../e/escalamiento.md), [Mitigación](../m/mitigacion.md), [Causa común](../c/causa-comun.md), [Ejercicio de runbook](../e/ejercicio-de-runbook.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.
- [SE-611 — Taller: degradar y recuperar un modelo](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) — [Parte 50](../../../classes/part-50-machine-learning-en-produccion-y-mlops/README.md), Machine learning en producción y MLOps.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-612](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-612-proyecto-sistema-de-ml-operable-con-evidencia/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE, «Managing Incidents»](https://sre.google/sre-book/managing-incidents/) — gestión de incidentes con roles y comunicación; autoridad: Google SRE.
- [Google SRE, «Emergency Response»](https://sre.google/sre-book/emergency-response/) — respuesta a emergencias y lecciones de casos; autoridad: Google SRE.
- [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) — ciclo de manejo de incidentes de seguridad; autoridad: NIST.
- [PagerDuty, guía de respuesta a incidentes](https://response.pagerduty.com/) — proceso de respuesta publicado en abierto; autoridad: PagerDuty.
- [RFC 9110, semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — define los métodos idempotentes y su significado; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Ruido de evaluación](./ruido-de-evaluacion.md) · [Runtime →](./runtime.md)
