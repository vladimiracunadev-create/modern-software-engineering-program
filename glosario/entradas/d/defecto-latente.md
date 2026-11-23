# Defecto latente

[↑ Glosario](../../README.md) · [← Defecto enmascarado](./defecto-enmascarado.md) · [Defecto sembrado →](./defecto-sembrado.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md)

## Definición

Debilidad de un sistema o de un procedimiento que aún no ha causado daño.

Definición de trabajo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md).

## Por qué importa

La clase donde se define, [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), existe con este propósito: la clase existe para que diseñes y conduzcas un **día de práctica (game day)**: un ejercicio programado donde un equipo responde a una falla inyectada con sus propios procedimientos, herramientas y comunicación.

## Cómo funciona

Según [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md):

Los defectos latentes entran con cada cambio y esperan hasta que algo los encuentre: un incidente real, un ejercicio o un experimento automático. Se modelan 24 meses del equipo de la API de entregas: cada mes entran 0, 1 o 2 defectos (media de 1) de las seis clases; cada defecto latente tiene 6 % de probabilidad al mes de salir a la luz en un incidente real; un día de práctica descubre 70 % de los latentes; un experimento automático descubre 80 % de los técnicos y ninguno de los humanos. Se comparan cuatro programas con 300 simulaciones cada uno.

## Ejemplo

Ejemplo de [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula la probabilidad de que un defecto latente siga escondido tras n meses si cada mes tiene una probabilidad p de salir a la luz. Antes de ejecutarlo, predice cuántos meses espera, en promedio, un defecto con p = 6 %.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md)) son:

- **El ejercicio «sale perfecto» siempre** — causa: escenario conocido o demasiado fácil. Corrección: variar el escenario y ocultar detalles progresivamente.
- **Los hallazgos no se corrigen** — causa: retrospectiva sin acciones verificables. Corrección: responsable, fecha y verificación en el siguiente ejercicio.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Sin práctica quedan 12,6 defectos y ocurren 11,5 incidentes con un defecto latente como causa. ([SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-499](../../../classes/part-41-observabilidad-sre-e-incidentes/se-499-runbooks-on-call-y-escalamiento/README.md), [SE-500](../../../classes/part-41-observabilidad-sre-e-incidentes/se-500-gestion-de-incidentes-y-comunicacion/README.md), [SE-508](../../../classes/part-42-ingenieria-del-caos/se-508-fallos-de-recursos-e-infraestructura-cpu-memoria-disco-y-nodos/README.md), [SE-509](../../../classes/part-42-ingenieria-del-caos/se-509-caos-en-kubernetes-y-en-plataformas-cloud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Daño](./dano.md), [Acción verificable](../a/accion-verificable.md), [Día de práctica](./dia-de-practica.md), [Ejercicio de mesa](../e/ejercicio-de-mesa.md), [Guion de inyección](../g/guion-de-inyeccion.md), [Retrospectiva sin culpa](../r/retrospectiva-sin-culpa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-511 — Game days y ejercicios de respuesta a incidentes](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md) — [Parte 42](../../../classes/part-42-ingenieria-del-caos/README.md), Ingeniería del caos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-528](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-528-proyecto-migracion-incremental-reversible/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-470](../../../classes/part-39-build-release-y-cadena-de-suministro/se-470-artefactos-repositorios-y-promocion/README.md).

**Aparece en los casos de estudio:** [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Well-Architected: REL12-BP05 Conduct game days regularly](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_game_days_resiliency.html) — definición, buenas prácticas y antipatrones; autoridad: documentación de Amazon Web Services.
- [Netflix: The Netflix Simian Army](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116) — ejecución en horario laboral con ingenieros disponibles; autoridad: blog de ingeniería de Netflix.
- [Principles of Chaos Engineering](https://principlesofchaos.org/) — automatización continua de los experimentos; autoridad: documento vivo de la comunidad de ingeniería del caos.
- [Google SRE: Testing for Reliability](https://sre.google/sre-book/testing-reliability/) — límites de las pruebas estadísticas; autoridad: libro de ingeniería de confiabilidad de Google.

---

[↑ Glosario](../../README.md) · [← Defecto enmascarado](./defecto-enmascarado.md) · [Defecto sembrado →](./defecto-sembrado.md)
