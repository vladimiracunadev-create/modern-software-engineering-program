# Punto de control

[↑ Glosario](../../README.md) · [← Punto de compromiso](./punto-de-compromiso.md) · [Punto de corte →](./punto-de-corte.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md)

## Definición

Un **punto de control** (*checkpoint*) es el estado mínimo guardado en almacenamiento duradero que permite reanudar una tarea sin repetirla entera. [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) (automatización idempotente y reanudable) lo define como el registro del progreso que permite reanudar sin empezar de cero; [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) (detener, recuperar y evaluar un agente) lo aplica a agentes. No es una copia completa del sistema: es lo mínimo para continuar.

## Por qué importa

Reiniciar desde el principio es caro y, además, repite los efectos ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)). Con un punto de control se recalcula como mucho el paso en curso. Pero [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) avisa que no es gratis: evita rehacer, y crea ventanas de duplicado o de pérdida entre el efecto y el registro del progreso.

## Cómo funciona

[SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) describe el contenido: en qué paso va el agente, qué ha hecho y qué le falta. Se guarda en un almacenamiento que sobrevive a la caída (una base de datos, un archivo) y se escribe en **puntos conocidos**. Anthropic informa, según la clase, de que en su sistema de investigación no pueden reiniciar desde el principio por el costo, y han construido uno que reanuda desde donde estaba el agente, combinando el modelo con reintentos y puntos de control deterministas.

La tensión que [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) hace explícita está entre dos escrituras: el efecto (enviar, cobrar) y el registro del progreso.

- **Si se registra antes del efecto,** una caída entre ambos pierde el efecto.
- **Si se registra después,** una caída entre ambos lo repite.

Por eso el punto de control se combina con **idempotencia**: el paso que se repite no debe causar daño al hacerlo dos veces.

## Ejemplo

El equipo de *Avisos* en [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. Al detenerse por una regla, deja un punto de control para que la reanudación continúe sin repetir los avisos ya enviados.

## Errores y confusiones comunes

- **Reiniciar desde cero tras una caída** y repetir efectos ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)).
- **Guardarlo en memoria o en un archivo temporal** que no sobrevive.
- **Ignorar la ventana entre efecto y registro.**
- **Confundirlo con una copia de seguridad:** es progreso de una tarea, no un respaldo del sistema.

## Límites y cuándo no aplica

Para tareas muy cortas, el costo de guardar supera al de repetir. Para tareas cuyo estado no se puede resumir de forma segura (conversaciones con contexto largo), el punto de control es incompleto. La escenografía de [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) es hipotética: sin datos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-223](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-223-schedulers-workers-y-trabajos-por-lotes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Estado](../e/estado.md), [Progreso](./progreso.md), [Registro](../r/registro.md), [Tarea](../t/tarea.md), [Acierto en tres de tres](../a/acierto-en-tres-de-tres.md), [Clave de idempotencia](../c/clave-de-idempotencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md), [SE-414](../../../classes/part-34-saas-y-plataformas-de-producto/se-414-planes-derechos-de-uso-y-banderas-de-funcionalidad/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-573](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-573-human-in-the-loop-aprobacion-y-acciones-reversibles/README.md), [SE-576](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-576-proyecto-final-producto-operable-construido-desde-spec/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Puntos de control».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno, puntos de control humanos y condiciones de parada; autoridad: Anthropic.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.
- [Patrón de bandeja de salida transaccional](https://microservices.io/patterns/data/transactional-outbox.html) — efecto y registro en una transacción; autoridad: catálogo de patrones de microservicios.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de una proporción; autoridad: Journal of the American Statistical Association.
- [POSIX: `rename`](https://pubs.opengroup.org/onlinepubs/9699919799/functions/rename.html) — sustitución atómica del destino; autoridad: The Open Group.

---

[↑ Glosario](../../README.md) · [← Punto de compromiso](./punto-de-compromiso.md) · [Punto de corte →](./punto-de-corte.md)
