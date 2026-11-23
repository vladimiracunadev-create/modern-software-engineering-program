# Día de práctica

[↑ Glosario](../../README.md) · [← Dfs, ciclos y orden](./dfs-ciclos-y-orden.md) · [Diagnóstico →](./diagnostico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Ejercicio programado donde un equipo responde con sus procedimientos a una falla inyectada, con observación y registro.

Definición de trabajo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md): Ejercicio planificado en que un equipo responde a un fallo inyectado.

## Por qué importa

La clase donde se define, [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), existe con este propósito: la clase existe para que diseñes y conduzcas un **día de práctica (game day)**: un ejercicio programado donde un equipo responde a una falla inyectada con sus propios procedimientos, herramientas y comunicación.

## Cómo funciona

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Un **día de práctica** es un ejercicio programado donde se provoca una falla (real o simulada) y un equipo responde con sus herramientas y procedimientos habituales, mientras alguien observa y registra. AWS lo describe como ejercitar con regularidad los procedimientos de respuesta a eventos que afectan a una carga de trabajo, con los mismos equipos que responderían en producción, simulando eventos en entornos similares a producción y realizando las mismas acciones que se harían en el evento real. Se distingue de tres cosas parecidas. De una **prueba automática**, porque incluye personas, decisiones y comunicación. De una **demostración**, porque no se sabe de antemano cómo termina. Y de un **ejercicio de mesa**, que discute en una sala qué se haría y, aunque útil, no encuentra el comando que ya no existe.

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Supón, como caso hipotético y no como medición, que el equipo planifica su primer día de práctica de tres horas para el tercer martes del mes, fuera de cierres de plazo. Escenario: «el almacenamiento deja de responder durante 20 minutos»; radio: preproducción con tráfico sintético de 300 entregas por minuto; roles: una persona facilita, tres responden, una observa y otra controla la plataforma; reglas: se usan los runbooks y los accesos de guardia, no se cambia la falla; aborto: a los 75 minutos si el servicio no está en estado estable. Mide el tiempo hasta detectar, hasta decidir y hasta mitigar, y registra los hallazgos con clase de defecto.

## Ejemplo

Ejemplo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético y no como medición, que el equipo planifica su primer día de práctica de tres horas para el tercer martes del mes, fuera de cierres de plazo. Escenario: «el almacenamiento deja de responder durante 20 minutos»; radio: preproducción con tráfico sintético de 300 entregas por minuto; roles: una persona facilita, tres responden, una observa y otra controla la plataforma; reglas: se usan los runbooks y los accesos de guardia, no se cambia la falla; aborto: a los 75 minutos si el servicio no está en estado estable. Mide el tiempo hasta detectar, hasta decidir y hasta mitigar, y registra los hallazgos con clase de defecto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md)) son:

- **El ejercicio «sale perfecto» siempre** — causa: escenario conocido o demasiado fácil. Corrección: variar el escenario y ocultar detalles progresivamente.
- **Los hallazgos no se corrigen** — causa: retrospectiva sin acciones verificables. Corrección: responsable, fecha y verificación en el siguiente ejercicio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por eso un día de práctica y un experimento automático no compiten: encuentran defectos de naturaleza distinta. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))
- **un día de práctica sin controlador de plataforma ni aborto**. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), [SE-438](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Falla inyectada](../f/falla-inyectada.md), [Fallo inyectado](../f/fallo-inyectado.md), [Observación](../o/observacion.md), [Registro](../r/registro.md), [Acción verificable](../a/accion-verificable.md), [Criterio de aborto](../c/criterio-de-aborto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-443 — Taller: someter un sistema a presión controlada](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-443-taller-someter-un-sistema-a-presion-controlada/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-512](../../../classes/part-42-ingenieria-del-caos/se-512-caos-continuo-automatizacion-en-ci-cd-y-en-produccion/README.md), [SE-510](../../../classes/part-42-ingenieria-del-caos/se-510-fallos-de-datos-y-de-estado-replicas-particiones-y-corrupcion/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md), [SE-515](../../../classes/part-42-ingenieria-del-caos/se-515-taller-ejecutar-un-experimento-de-caos-acotado-con-criterio-de-aborto/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «día de simulacro».

**Forma en inglés o término técnico original:** «game day».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Well-Architected: REL12-BP05 Conduct game days regularly](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_game_days_resiliency.html) — definición, buenas prácticas y antipatrones; autoridad: documentación de Amazon Web Services.
- [AWS Well-Architected: probar la fiabilidad](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html) — pruebas de fallo y días de simulacro; autoridad: Amazon Web Services.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — ejecución en horario laboral con ingenieros disponibles; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — automatización continua de los experimentos; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — límites de las pruebas estadísticas; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Dfs, ciclos y orden](./dfs-ciclos-y-orden.md) · [Diagnóstico →](./diagnostico.md)
