# Ganancia de información

[↑ Glosario](../../README.md) · [← Fuzzing](../f/fuzzing.md) · [Gancho →](./gancho.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Reducción de la incertidumbre que produce una observación; mide cuánto separa las hipótesis restantes.

Definición de trabajo de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

## Por qué importa

La clase donde se define, [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), existe con este propósito: el taller existe para que practiques lo que ocurre en un incidente real: diagnosticar con señales que faltan, que llegan tarde o que mienten.

## Cómo funciona

Según [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md):

Cuando queda más de una candidata, hay que decidir qué mirar. Tres criterios habituales: lo **más barato** primero (porque ya está en un panel), lo que **mejor reparte** las candidatas (el que divide el conjunto lo más cerca posible de la mitad, la mayor ganancia de información), o **al azar** (lo que ocurre cuando no hay criterio). Lo más barato es una buena regla cuando todas las señales separan igual, y una mala cuando las baratas son las que menos separan, como un indicador que se desvía con casi todas las fallas. La ganancia de información exige conocer la tabla de firmas, lo que justifica construirla antes del incidente. En la práctica, el criterio combina las dos: la que más separa por unidad de coste.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo ejecuta el taller con el escenario del problema. La guardia abre la bitácora a las 14:05 y anota: 5xx desviada, p99 desviada, conexiones a la base normal, fallos de resolución normal, errores de TLS normal, caché normal, 429 normal, versión desplegada sin cambio; profundidad de la cola, reinicios, disco y memoria sin datos por la caída del agente. La función de candidatas devuelve una sola: dependencia externa caída.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md)) son:

- **El equipo actúa sobre la causa equivocada** — causa: una señal sin datos se leyó como normal. Corrección: tres estados por señal y latido por agente.
- **El diagnóstico tarda en converger** — causa: se miran primero las señales más baratas. Corrección: elegir la que más separa las candidatas, ponderada por coste.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Tres criterios habituales: lo **más barato** primero (porque ya está en un panel), lo que **mejor reparte** las candidatas (el que divide el conjunto lo más cerca posible de la mitad, la mayor ganancia de información), o **al azar** (lo que ocurre cuando no hay criterio). ([SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Hipótesis](../h/hipotesis.md), [Incertidumbre](../i/incertidumbre.md), [Observación](../o/observacion.md), [Reducción](../r/reduccion.md), [Candidata](../c/candidata.md), [Firma de una falla](../f/firma-de-una-falla.md).
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

[↑ Glosario](../../README.md) · [← Fuzzing](../f/fuzzing.md) · [Gancho →](./gancho.md)
