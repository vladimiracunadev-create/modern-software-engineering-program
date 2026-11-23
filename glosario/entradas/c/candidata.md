# Candidata

[↑ Glosario](../../README.md) · [← Cancelación y ciclo de vida](./cancelacion-y-ciclo-de-vida.md) · [Candidato →](./candidato.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Falla cuya firma coincide con todas las señales observadas.

Definición de trabajo de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md).

## Por qué importa

En [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md), el tema «Firmas y candidatas» importa porque convierte el diagnóstico en eliminación explícita.

## Cómo funciona

Según [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md):

Dado lo observado, una falla es **candidata** si su firma coincide con todas las señales que se han mirado: las que se observaron desviadas deben estar en su firma, y las que se observaron normales no deben estarlo. Las señales sin datos no excluyen a nadie. El diagnóstico es la reducción del conjunto de candidatas hasta que queda una o hasta que la siguiente observación decide entre las que quedan.

Según [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo ejecuta el taller con el escenario del problema. La guardia abre la bitácora a las 14:05 y anota: 5xx desviada, p99 desviada, conexiones a la base normal, fallos de resolución normal, errores de TLS normal, caché normal, 429 normal, versión desplegada sin cambio; profundidad de la cola, reinicios, disco y memoria sin datos por la caída del agente. La función de candidatas devuelve una sola: dependencia externa caída.

## Ejemplo

Ejemplo de [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) (sección «Ejemplo mínimo»):

Imprime `['dns']`: la base no tiene 5xx y la cuota no desvía p99. Registra versión de Python, comando y salida; después cambia `conexiones` a `True` y a `False` y observa qué candidatas quedan.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El diagnóstico tarda en converger** — causa: se miran primero las señales más baratas. Corrección: elegir la que más separa las candidatas, ponderada por coste. ([SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dado lo observado, una falla es **candidata** si su firma coincide con todas las señales que se han mirado: las que se observaron desviadas deben estar en su firma, y las que se observaron normales no deben estarlo. ([SE-503](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Firma de una falla](../f/firma-de-una-falla.md), [Ganancia de información](../g/ganancia-de-informacion.md), [Pérdida selectiva de telemetría](../p/perdida-selectiva-de-telemetria.md), [Señal sin datos](../s/senal-sin-datos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-503 — Taller: diagnosticar con telemetría incompleta](../../../classes/part-41-observabilidad-sre-e-incidentes/se-503-taller-diagnosticar-con-telemetria-incompleta/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md), [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-336](../../../classes/part-27-arquitectura-de-software-y-dominio/se-336-proyecto-arquitectura-defendible-y-verificable/README.md), [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-541](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-541-mapa-de-metodologias-que-decide-cada-una-y-como-elegir/README.md).

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

[↑ Glosario](../../README.md) · [← Cancelación y ciclo de vida](./cancelacion-y-ciclo-de-vida.md) · [Candidato →](./candidato.md)
