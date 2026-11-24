# Runbook

[↑ Glosario](../../README.md) · [← Ruido de evaluación](./ruido-de-evaluacion.md) · [Runtime →](./runtime.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Un **runbook** es un procedimiento paso a paso para una situación operacional conocida, ejecutable sin conocer el sistema ([SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md)). [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) lo precisa como el documento operativo que acompaña a una alerta y describe diagnóstico, mitigación, verificación, reversión y escalamiento. Se distingue del *playbook*, que da preguntas y criterios para situaciones no previstas.

## Por qué importa

Reduce el tiempo de decisión. Quien está de guardia a las tres de la mañana no debe razonar desde cero ni conocer el sistema a fondo: sigue pasos comprobados. Cambia el diseño de una alerta: toda alerta que despierta a alguien debe tener un runbook enlazado.

## Cómo funciona

El runbook es una receta operativa. Cada **paso** es una acción única con un **comando** y un **resultado esperado** («ejecuta `kubectl get pods`; deben aparecer 3 pods en estado Running»). La estructura de [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) tiene cinco partes: **diagnóstico** (cómo confirmar qué pasa), **mitigación** (cómo limitar el daño), **verificación** (cómo saber que funcionó), **reversión** (cómo deshacer si empeora) y **escalamiento** (a quién avisar y cuándo).

[SE-611](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-611-taller-degradar-y-recuperar-un-modelo/README.md) lo aplica a la operación de modelos de ML. El runbook **pregunta primero qué clase de falla es**: dos clases son fallas de datos (de ingeniería, como un cambio de unidad en la entrada) y otras dos son cambios del mundo (deriva real). El diagnóstico y la mitigación correctos son distintos para cada una, y esa es la razón por la que el runbook pregunta primero la clase. En el ensayo de la clase, la persona de guardia, sin aviso previo, recibe a los dos minutos el aviso de la validación de entrada, abre el runbook, sigue la rama «falla de calidad de entrada», confirma que la tasa de lectura llega en porcentaje y a los veinte minutos despliega una corrección de la conversión.

Dos fallos con corrección conocida: el runbook que dice «revisa los servicios» tiene pasos sin comando ni salida esperada (un paso por acción, con comando y resultado esperado); y el runbook que falla al ejecutarse se desactualizó (se ensaya y se versiona junto al sistema). Un incidente nuevo deja a la guardia sin guía cuando solo hay runbooks y no playbook: se complementa con preguntas y criterios de escalada.

## Ejemplo

Runbook «Cola de entregas creciendo». 1) Diagnóstico: `consultar-cola` debe devolver menos de 500 elementos; si devuelve más, continuar. 2) Mitigación: escalar consumidores a 6 con `escalar --consumidores 6`; resultado esperado: la cola baja en 10 minutos. 3) Verificación: la latencia p95 vuelve por debajo de 2 s. 4) Reversión: volver a 3 consumidores si hay errores de base de datos. 5) Escalamiento: si no baja en 30 minutos, avisar al equipo de datos. (Runbook ilustrativo en la estructura de [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md).)

## Errores y confusiones comunes

- **«Revisa los servicios»**: pasos vagos sin comando ni resultado.
- **Runbook desactualizado** que falla al ejecutarse.
- **Solo runbooks, sin playbook** para lo imprevisto.
- **No ensayarlo.**

## Límites y cuándo no aplica

Un runbook solo cubre situaciones conocidas; ante un incidente nuevo no basta. Para incidentes raros, el costo de mantenerlo puede superar su uso. Los runbooks excesivamente detallados se vuelven frágiles; los mejores se automatizan cuando el paso es mecánico.

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

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

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
