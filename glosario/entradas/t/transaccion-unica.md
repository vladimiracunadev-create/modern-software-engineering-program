# Transacción única

[↑ Glosario](../../README.md) · [← Transacción](./transaccion.md) · [Transacción única de clave y efecto →](./transaccion-unica-de-clave-y-efecto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md)

## Definición

Operación atómica que incluye el efecto y el registro de que ocurrió.

Definición de trabajo de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md).

## Por qué importa

La clase donde se define, [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), existe con este propósito: el taller existe para que reúnas en una sola práctica tres capacidades que se enseñaron por separado y que se necesitan juntas en cuanto un agente trabaja sin que nadie lo mire: detenerlo cuando se descontrola, recuperarlo cuando se cae sin duplicar lo que ya hizo y evaluarlo con una vara que no se deje engañar por el ruido.

## Cómo funciona

Según [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

El punto delicado es el instante entre ejecutar un efecto y registrar que se ejecutó. Si el agente envía un aviso y se cae antes de anotar que lo hizo, al reanudar volverá a enviarlo. Hay tres soluciones, por orden creciente de fiabilidad. Una **clave de idempotencia** por paso: el efecto lleva un identificador (tarea, paso) y el receptor ignora los repetidos, de modo que repetir es seguro. Una **transacción única** que incluye el efecto y el punto de control: ocurren los dos o ninguno, lo que solo es posible cuando el efecto es una escritura en la misma base de datos, como en el patrón de la bandeja de salida (se escribe el mensaje en una tabla dentro de la transacción y otro proceso lo entrega con deduplicación).

Según [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** tras reiniciar el agente, un estudiante recibió dos veces el mismo aviso. **Hipótesis rivales:** (a) el agente decidió enviar dos veces; (b) el servicio de correo duplicó el mensaje; (c) el agente se cayó tras enviar y antes de anotar, y al reanudar volvió a enviar. **Prueba:** compara el registro de envíos con el punto de control; si el último paso enviado es posterior al último paso anotado, la causa es (c). **Conclusión:** el efecto y su registro no son atómicos. **Regresión:** añade una prueba que mate el proceso en cada fase y exija cero duplicados con la clave de idempotencia o la transacción única.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo de *Avisos* instala tres reglas para su agente de envíos: máximo de 80 pasos por tarea (calibrado con la cola de la distribución de las tareas buenas), cinco repeticiones del mismo estado y diez pasos sin avance del número de avisos preparados. El presupuesto se fija por tarea según su clase, no global. Al detenerse, el agente guarda su estado y notifica a una persona con la última acción, el número de pasos y el motivo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Tras reiniciar hay avisos duplicados** — causa: efecto y punto de control no atómicos. Corrección: clave de idempotencia o transacción única. ([SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md)) son: Las definiciones son operativas para el servicio *Avisos*. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: las reglas de parada y la reanudación son código real sobre máquinas de estados y SQLite en memoria, y la evaluación es una simulación con semilla fija. No se invocó ningún modelo, no se evaluó ningún agente real y los efectos no salen de la base.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Operación](../o/operacion.md), [Registro](../r/registro.md), [Acierto en tres de tres](../a/acierto-en-tres-de-tres.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Condición de parada](../c/condicion-de-parada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-575 — Taller: detener, recuperar y evaluar un agente](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-383](../../../classes/part-31-integracion-eventos-y-mensajeria/se-383-taller-provocar-y-contener-mensajes-duplicados/README.md), [SE-354](../../../classes/part-29-datos-persistencia-y-recuperacion/se-354-migraciones-compatibles-y-evolucion-de-esquema/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-411](../../../classes/part-34-saas-y-plataformas-de-producto/se-411-alta-aprovisionamiento-y-configuracion-por-cliente/README.md), [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: «Building effective agents»](https://www.anthropic.com/engineering/building-effective-agents) — verdad del entorno, puntos de control humanos y condiciones de parada; autoridad: Anthropic.
- [Anthropic: «How we built our multi-agent research system»](https://www.anthropic.com/engineering/multi-agent-research-system) — reanudar desde el punto del error, muestras pequeñas con efectos grandes y evaluación del estado final; autoridad: Anthropic.
- [Patrón de bandeja de salida transaccional](https://microservices.io/patterns/data/transactional-outbox.html) — efecto y registro en una transacción; autoridad: catálogo de patrones de microservicios.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de una proporción; autoridad: Journal of the American Statistical Association.

---

[↑ Glosario](../../README.md) · [← Transacción](./transaccion.md) · [Transacción única de clave y efecto →](./transaccion-unica-de-clave-y-efecto.md)
