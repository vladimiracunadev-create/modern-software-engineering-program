# Ejercicio de mesa

[↑ Glosario](../../README.md) · [← Ejemplos concretos](./ejemplos-concretos.md) · [Ejercicio de recuperación →](./ejercicio-de-recuperacion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Discusión de cómo se respondería a un escenario, sin inyectar nada.

Definición de trabajo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md).

## Por qué importa

La clase donde se define, [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), existe con este propósito: la clase existe para que diseñes y conduzcas un **día de práctica (game day)**: un ejercicio programado donde un equipo responde a una falla inyectada con sus propios procedimientos, herramientas y comunicación.

## Cómo funciona

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Un **día de práctica** es un ejercicio programado donde se provoca una falla (real o simulada) y un equipo responde con sus herramientas y procedimientos habituales, mientras alguien observa y registra. AWS lo describe como ejercitar con regularidad los procedimientos de respuesta a eventos que afectan a una carga de trabajo, con los mismos equipos que responderían en producción, simulando eventos en entornos similares a producción y realizando las mismas acciones que se harían en el evento real. Se distingue de tres cosas parecidas. De una **prueba automática**, porque incluye personas, decisiones y comunicación. De una **demostración**, porque no se sabe de antemano cómo termina. Y de un **ejercicio de mesa**, que discute en una sala qué se haría y, aunque útil, no encuentra el comando que ya no existe.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Supón, como caso hipotético y no como medición, que el equipo planifica su primer día de práctica de tres horas para el tercer martes del mes, fuera de cierres de plazo. Escenario:

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md)) son:

- **El ejercicio «sale perfecto» siempre** — causa: escenario conocido o demasiado fácil. Corrección: variar el escenario y ocultar detalles progresivamente.
- **Los hallazgos no se corrigen** — causa: retrospectiva sin acciones verificables. Corrección: responsable, fecha y verificación en el siguiente ejercicio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Y de un **ejercicio de mesa**, que discute en una sala qué se haría y, aunque útil, no encuentra el comando que ya no existe. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Escenario](./escenario.md), [Acción verificable](../a/accion-verificable.md), [Defecto latente](../d/defecto-latente.md), [Día de práctica](../d/dia-de-practica.md), [Guion de inyección](../g/guion-de-inyeccion.md), [Retrospectiva sin culpa](../r/retrospectiva-sin-culpa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-502](../../../classes/part-41-observabilidad-sre-e-incidentes/se-502-continuidad-disaster-recovery-y-ejercicios/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Well-Architected: REL12-BP05 Conduct game days regularly](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_game_days_resiliency.html) — definición, buenas prácticas y antipatrones; autoridad: documentación de Amazon Web Services.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — ejecución en horario laboral con ingenieros disponibles; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — automatización continua de los experimentos; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — límites de las pruebas estadísticas; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Ejemplos concretos](./ejemplos-concretos.md) · [Ejercicio de recuperación →](./ejercicio-de-recuperacion.md)
