# Intervalo de confianza de Wilson

[↑ Glosario](../../README.md) · [← Intervalo de confianza](./intervalo-de-confianza.md) · [Intervalo de retroalimentación →](./intervalo-de-retroalimentacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Rango plausible de una proporción verdadera dada una proporción observada y un tamaño de muestra.

Definición de trabajo de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md).

## Por qué importa

La clase donde se define, [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), existe con este propósito: el taller existe para que reúnas en una sola práctica tres capacidades que se enseñaron por separado y que se necesitan juntas en cuanto un agente trabaja sin que nadie lo mire: detenerlo cuando se descontrola, recuperarlo cuando se cae sin duplicar lo que ya hizo y evaluarlo con una vara que no se deje engañar por el ruido.

## Cómo funciona

[SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. El presupuesto se fija por tarea según su clase, no global. Al detenerse, el agente guarda su estado y notifica a una persona con la última acción, el número de pasos y el motivo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)) son:

- **Un agente trabaja toda la noche sin avanzar** — causa: sin condiciones de parada o solo con un máximo enorme. Corrección: añadir estado repetido y falta de avance con presupuesto por tarea.
- **La regla de parada detiene tareas buenas** — causa: parámetros globales. Corrección: calibrar por clase de tarea y basar la regla en progreso.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: las reglas de parada y la reanudación son código real sobre máquinas de estados y SQLite en memoria, y la evaluación es una simulación con semilla fija. No se invocó ningún modelo, no se evaluó ningún agente real y los efectos no salen de la base.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Rango](../r/rango.md), [Acierto en tres de tres](../a/acierto-en-tres-de-tres.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Condición de parada](../c/condicion-de-parada.md), [Punto de control](../p/punto-de-control.md), [Transacción única](../t/transaccion-unica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno, puntos de control humanos y condiciones de parada; autoridad: Anthropic.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.
- [Patrón de bandeja de salida transaccional](https://microservices.io/patterns/data/transactional-outbox.html) — efecto y registro en una transacción; autoridad: catálogo de patrones de microservicios.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de una proporción; autoridad: Journal of the American Statistical Association.

---

[↑ Glosario](../../README.md) · [← Intervalo de confianza](./intervalo-de-confianza.md) · [Intervalo de retroalimentación →](./intervalo-de-retroalimentacion.md)
