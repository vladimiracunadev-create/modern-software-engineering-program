# Ejercicio de runbook

[↑ Glosario](../../README.md) · [← Ejercicio de recuperación](./ejercicio-de-recuperacion.md) · [Ejercicio previo al fallo →](./ejercicio-previo-al-fallo.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Ejecución programada de un runbook por alguien distinto de su autor para comprobar que funciona.

Definición de trabajo de [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md).

## Por qué importa

La clase donde se define, [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), existe con este propósito: la clase existe para que conviertas una página en una respuesta: un runbook que una persona cansada pueda seguir a las tres de la madrugada, una rotación de guardia con una carga que se pueda sostener y un escalamiento que llegue a alguien aunque la primera persona no conteste.

## Cómo funciona

[SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo reescribe el runbook de `EntregasConsumoRapido` con el formato anterior, lo añade al repositorio junto al código del servicio y escribe un verificador que se ejecuta en la integración continua (campos, comandos con salida esperada, reversión de lo destructivo, fecha menor de 90 días y alerta existente en el catálogo).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)) son:

- **El runbook dice «revisa los servicios»** — causa: pasos sin comando ni salida esperada. Corrección: un paso por acción, con comando y resultado esperado.
- **La guardia es siempre la misma persona** — causa: equipo pequeño o ausencias sin plan. Corrección: calcular la carga y ampliar la rotación o reducir el alcance.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Runbook](../r/runbook.md), [Causa común](../c/causa-comun.md), [Escalamiento](./escalamiento.md), [Guardia](../g/guardia.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-499 — Runbooks, on-call y escalamiento](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Being On-Call](https://sre.google/sre-book/being-on-call/) — carga y tamaño de la guardia; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE Workbook: On-Call](https://sre.google/workbook/on-call/) — medir y mejorar la guardia; autoridad: Google, SRE Workbook.
- [PagerDuty Incident Response](https://response.pagerduty.com/) — procesos públicos de guardia y respuesta; autoridad: documentación pública de PagerDuty.
- [Google SRE: Practical Alerting](https://sre.google/sre-book/practical-alerting/) — alertas con acción clara; autoridad: libro de ingeniería de confiabilidad de Google.
- [Python: datetime](https://docs.python.org/3/library/datetime.html) — fechas usadas por el verificador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ejercicio de recuperación](./ejercicio-de-recuperacion.md) · [Ejercicio previo al fallo →](./ejercicio-previo-al-fallo.md)
