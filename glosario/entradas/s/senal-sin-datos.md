# Señal sin datos

[↑ Glosario](../../README.md) · [← Señal redundante](./senal-redundante.md) · [Señales, cancelación y atomicidad →](./senales-cancelacion-y-atomicidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Señal que no se está registrando o consultando y que no permite concluir que esté normal.

Definición de trabajo de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

## Por qué importa

La clase donde se define, [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), existe con este propósito: el taller existe para que practiques lo que ocurre en un incidente real: diagnosticar con señales que faltan, que llegan tarde o que mienten.

## Cómo funciona

[SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo ejecuta el taller con el escenario del problema. La guardia abre la bitácora a las 14:05 y anota: 5xx desviada, p99 desviada, conexiones a la base normal, fallos de resolución normal, errores de TLS normal, caché normal, 429 normal, versión desplegada sin cambio; profundidad de la cola, reinicios, disco y memoria sin datos por la caída del agente. La función de candidatas devuelve una sola: dependencia externa caída.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El equipo actúa sobre la causa equivocada** — causa: una señal sin datos se leyó como normal. Corrección: tres estados por señal y latido por agente. ([SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Señal](./senal.md), [Candidata](../c/candidata.md), [Firma de una falla](../f/firma-de-una-falla.md), [Ganancia de información](../g/ganancia-de-informacion.md), [Pérdida selectiva de telemetría](../p/perdida-selectiva-de-telemetria.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Google SRE: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) — diagnóstico como ciclo de hipótesis y descarte; autoridad: libro de ingeniería de confiabilidad de Google.
- [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de oro y síntoma frente a causa; autoridad: libro de ingeniería de confiabilidad de Google.
- [Cook, «How Complex Systems Fail»](https://how.complexsystems.fail/) — operación en modo degradado y atribución posterior; autoridad: texto del autor, Richard I. Cook.
- [Fischhoff, «Hindsight ≠ foresight»](https://doi.org/10.1037/0096-1523.1.3.288) — sesgo de retrospectiva; autoridad: Journal of Experimental Psychology, 1975.
- [OpenTelemetry: Signals](https://opentelemetry.io/docs/concepts/signals/) — señales de telemetría; autoridad: proyecto OpenTelemetry (CNCF).

---

[↑ Glosario](../../README.md) · [← Señal redundante](./senal-redundante.md) · [Señales, cancelación y atomicidad →](./senales-cancelacion-y-atomicidad.md)
