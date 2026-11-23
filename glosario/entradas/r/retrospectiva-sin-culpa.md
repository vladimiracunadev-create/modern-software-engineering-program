# Retrospectiva sin culpa

[↑ Glosario](../../README.md) · [← Retrospectiva basada en evidencia](./retrospectiva-basada-en-evidencia.md) · [Retry y operaciones inciertas →](./retry-y-operaciones-inciertas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Análisis de lo ocurrido centrado en factores del sistema y no en personas.

Definición de trabajo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md).

## Por qué importa

La clase donde se define, [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), existe con este propósito: la clase existe para que diseñes y conduzcas un **día de práctica (game day)**: un ejercicio programado donde un equipo responde a una falla inyectada con sus propios procedimientos, herramientas y comunicación.

## Cómo funciona

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

El ejercicio no termina al restaurar el sistema. La **retrospectiva sin culpa** reconstruye la línea de tiempo con el observador (cuándo se inyectó, cuándo saltó la alerta, quién la vio, qué decidió y por qué), identifica los factores (la alerta sin destinatario, el comando que ya no existe) y no personas, y escribe **acciones verificables** con responsable y fecha: «corregir el comando y probarlo en el próximo ejercicio» y no «mejorar los runbooks». `SE-501` desarrolla ese formato. AWS lista entre los antipatrones no incorporar lo aprendido en los procesos de recuperación y culpar a los equipos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Supón, como caso hipotético y no como medición, que el equipo planifica su primer día de práctica de tres horas para el tercer martes del mes, fuera de cierres de plazo. Escenario:

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El equipo teme participar** — causa: se culpa a personas por lo hallado. Corrección: retrospectiva sin culpa y hallazgos como factores del sistema. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **retrospectiva sin culpa** reconstruye la línea de tiempo con el observador (cuándo se inyectó, cuándo saltó la alerta, quién la vio, qué decidió y por qué), identifica los factores (la alerta sin destinatario, el comando que ya no existe) y no personas, y escribe **acciones verificables** con responsable y fecha: ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis](../a/analisis.md), [Acción verificable](../a/accion-verificable.md), [Defecto latente](../d/defecto-latente.md), [Día de práctica](../d/dia-de-practica.md), [Ejercicio de mesa](../e/ejercicio-de-mesa.md), [Guion de inyección](../g/guion-de-inyeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Well-Architected: REL12-BP05 Conduct game days regularly](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_game_days_resiliency.html) — definición, buenas prácticas y antipatrones; autoridad: documentación de Amazon Web Services.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — ejecución en horario laboral con ingenieros disponibles; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — automatización continua de los experimentos; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — límites de las pruebas estadísticas; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Retrospectiva basada en evidencia](./retrospectiva-basada-en-evidencia.md) · [Retry y operaciones inciertas →](./retry-y-operaciones-inciertas.md)
