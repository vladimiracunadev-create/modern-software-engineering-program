# Guion de inyección

[↑ Glosario](../../README.md) · [← Guía práctica](./guia-practica.md) · [Habilidad →](../h/habilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Plan privado de qué se inyecta, cuándo y qué hacer si el equipo no responde.

Definición de trabajo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md).

## Por qué importa

La clase donde se define, [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), existe con este propósito: la clase existe para que diseñes y conduzcas un **día de práctica (game day)**: un ejercicio programado donde un equipo responde a una falla inyectada con sus propios procedimientos, herramientas y comunicación.

## Cómo funciona

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Un escenario se toma del catálogo de `SE-508`, se concreta con una falla, una intensidad y un contexto («el almacenamiento deja de responder a las 23:40 de un cierre de plazo con 300 entregas por minuto») y se escribe un **guion de inyección** privado: qué se inyecta, cuándo, y qué se hará si el equipo no responde. El nivel de sorpresa es una decisión explícita. La primera práctica se anuncia con fecha, hora y escenarios, como recomienda AWS para el primero; las siguientes pueden ocultar el escenario o la hora; las que se hacen sin aviso a quien responde solo son defendibles con un control del daño muy sólido y un acuerdo previo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Supón, como caso hipotético y no como medición, que el equipo planifica su primer día de práctica de tres horas para el tercer martes del mes, fuera de cierres de plazo. Escenario:

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md)) son:

- **El ejercicio «sale perfecto» siempre** — causa: escenario conocido o demasiado fácil. Corrección: variar el escenario y ocultar detalles progresivamente.
- **Los hallazgos no se corrigen** — causa: retrospectiva sin acciones verificables. Corrección: responsable, fecha y verificación en el siguiente ejercicio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un escenario se toma del catálogo de `SE-508`, se concreta con una falla, una intensidad y un contexto («el almacenamiento deja de responder a las 23:40 de un cierre de plazo con 300 entregas por minuto») y se escribe un **guion de inyección** privado: qué se inyecta, cuándo, y qué se hará si el equipo no responde. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Plan](../p/plan.md), [Acción verificable](../a/accion-verificable.md), [Defecto latente](../d/defecto-latente.md), [Día de práctica](../d/dia-de-practica.md), [Ejercicio de mesa](../e/ejercicio-de-mesa.md), [Retrospectiva sin culpa](../r/retrospectiva-sin-culpa.md).
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

[↑ Glosario](../../README.md) · [← Guía práctica](./guia-practica.md) · [Habilidad →](../h/habilidad.md)
