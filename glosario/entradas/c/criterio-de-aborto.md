# Criterio de aborto

[↑ Glosario](../../README.md) · [← Criterio de abandono](./criterio-de-abandono.md) · [Criterio de aceptación →](./criterio-de-aceptacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Condición, escrita antes, que detiene el experimento.

Definición de trabajo de [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md).

## Por qué importa

La clase donde se define, [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md), existe con este propósito: el taller existe para que ejecutes una prueba de presión controlada sobre un sistema: formules una hipótesis sobre su comportamiento estable, inyectes un fallo con un radio de impacto acotado, observes con criterios de aborto definidos de antemano y concluyas qué defensa funcionó y cuál era una creencia.

## Cómo funciona

Según [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md):

El **radio de impacto** es la fracción del sistema o del tráfico afectada por el experimento. Empezar con el más pequeño que permita detectar el efecto reduce el daño de aprender. Hay una relación directa entre el radio y la capacidad de detección: un fallo fuerte se ve con una fracción mínima del tráfico y uno sutil necesita más solicitudes. El **criterio de aborto** es la condición, escrita antes, que detiene el experimento (por ejemplo, «si la tasa de errores de las solicitudes no afectadas supera el 2 % durante 10 s») y el **plan de recuperación** dice cómo se vuelve al estado anterior. Sin esas dos cosas, un experimento de caos es un incidente provocado.

Según [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md):

El equipo planifica un día de simulacro sobre el entorno de ensayo con una copia anonimizada. El plan dice: hipótesis (p95 por ventana de 10 s menor de 94 ms y errores menores del 0,5 %, con el umbral calculado con 30 ejecuciones base y verificado con una prueba A/A), cuatro fallos (latencia, errores, caída de la base y pico de tráfico) ejecutados de uno en uno con 30 s cada uno, radio inicial del 5 % del tráfico del entorno de ensayo, criterio de aborto (errores en solicitudes no afectadas mayor del 2 % durante 10 s o cualquier pérdida de datos), plan de recuperación (quitar la inyección y reiniciar los clientes) y responsables (una persona dirige, otra observa y otra puede abortar).

## Ejemplo

Ejemplo de [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) (sección «Ejemplo profesional»):

El equipo planifica un día de simulacro sobre el entorno de ensayo con una copia anonimizada.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Hubo daño a las personas usuarias** — causa: sin criterio de aborto ni radio acotado. Corrección: escribirlos antes y ensayar en entorno de ensayo. ([SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **criterio de aborto** es la condición, escrita antes, que detiene el experimento (por ejemplo, «si la tasa de errores de las solicitudes no afectadas supera el 2 % durante 10 s») y el **plan de recuperación** dice cómo se vuelve al estado anterior. ([SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md))
- Los principios lo recomiendan cuando es posible porque es el único entorno realmente representativo, y exigen mucha madurez: hipótesis, radio mínimo, criterio de aborto automático y comunicación. ([SE-443](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](./condicion.md), [Día de práctica](../d/dia-de-practica.md), [Hipótesis de estado estable](../h/hipotesis-de-estado-estable.md), [Inyección de fallos](../i/inyeccion-de-fallos.md), [Radio de impacto](../r/radio-de-impacto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-514](../../../classes/part-42-ingenieria-del-caos/se-514-aprender-de-los-experimentos-hallazgos-metricas-y-mejora/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md), [SE-516](../../../classes/part-42-ingenieria-del-caos/se-516-proyecto-programa-de-caos-de-un-servicio-con-evidencia-y-remediacion/README.md), [SE-444](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-444-proyecto-informe-reproducible-de-calidad/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Basiri et al., «Chaos Engineering»](https://doi.org/10.1109/MS.2016.60) — experimentación sobre sistemas para ganar confianza; autoridad: IEEE Software, 2016.
- [Principios del caos](https://principlesofchaos.org/) — hipótesis, variación de eventos y radio mínimo; autoridad: comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — pruebas de estrés y de recuperación; autoridad: Google, libro de ingeniería de confiabilidad.
- [AWS Well-Architected: probar la fiabilidad](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html) — pruebas de fallo y días de simulacro; autoridad: Amazon Web Services.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de eventos del modelo; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Criterio de abandono](./criterio-de-abandono.md) · [Criterio de aceptación →](./criterio-de-aceptacion.md)
