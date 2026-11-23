# Variabilidad

[↑ Glosario](../../README.md) · [← Valor, costo y riesgo](./valor-costo-y-riesgo.md) · [Variable independiente →](./variable-independiente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Dispersión de los tiempos entre llegadas o de servicio; se resume con el coeficiente de variación al cuadrado.

Definición de trabajo de [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md).

## Por qué importa

En [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), el tema «Variabilidad y lotes» importa porque con la misma carga media, más variabilidad y lotes más grandes multiplican la espera.

## Cómo funciona

Según [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md):

La aproximación de Kingman descompone la espera en tres factores: la utilización, la variabilidad de las llegadas y de los servicios, y el tiempo medio de servicio. Con la misma utilización, duplicar la variabilidad duplica casi la espera. Los lotes cuentan como variabilidad de llegadas: cinco elementos que llegan juntos esperan más que cinco que llegan de uno en uno. En software la variabilidad aparece como tareas de tamaños muy distintos y como la costumbre de entregar a revisión en bloques; reducirla (cortar en piezas de tamaño parecido, revisar de inmediato) cuesta menos que añadir personas.

Según [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md):

Compara la propuesta con «contratar a dos personas más»: añadir capacidad reduce la utilización, pero deja intactos los lotes y la variabilidad. Una decisión de flujo es adecuada cuando se apoya en la medición del trabajo en curso y del rendimiento; es débil cuando se apoya en la ocupación de las personas.

## Ejemplo

Ejemplo de [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) (sección «Ejemplo profesional»):

Compara la propuesta con «contratar a dos personas más»: añadir capacidad reduce la utilización, pero deja intactos los lotes y la variabilidad. Una decisión de flujo es adecuada cuando se apoya en la medición del trabajo en curso y del rendimiento; es débil cuando se apoya en la ocupación de las personas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se contratan personas y el plazo no mejora** — causa: la espera venía de lotes y variabilidad. Corrección: medir tamaños y lotes antes de añadir capacidad. ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los lotes cuentan como variabilidad de llegadas: cinco elementos que llegan juntos esperan más que cinco que llegan de uno en uno. ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Coeficiente de variación](../c/coeficiente-de-variacion.md), [Dispersión](../d/dispersion.md), [Servicio](../s/servicio.md), [Ley de Little](../l/ley-de-little.md), [Lote](../l/lote.md), [Tiempo de ciclo o plazo](../t/tiempo-de-ciclo-o-plazo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (22 clases más lo mencionan; las que más):

[SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md), [SE-591](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-591-orquestador-trabajadores-y-evaluador-optimizador/README.md), [SE-147](../../../classes/part-12-ingenieria-de-requisitos/se-147-atributos-de-calidad-y-restricciones/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Little, «A proof for the queuing formula: L = λW» (Operations Research, 1961)](https://doi.org/10.1287/opre.9.3.383) — demostración de la ley; autoridad: Operations Research.
- [Little, «Little's law as viewed on its 50th anniversary» (Operations Research, 2011)](https://doi.org/10.1287/opre.1110.0940) — condiciones y usos de la ley; autoridad: Operations Research.
- [Kingman, «The single server queue in heavy traffic» (Math. Proc. Cambridge Philos. Soc., 1961)](https://doi.org/10.1017/S0305004100036094) — aproximación de la espera con carga alta; autoridad: Cambridge Philosophical Society.
- [The Kanban Guide](https://kanbanguides.org/english/) — límites de trabajo y gestión del flujo; autoridad: Scrum.org (Kanban Guide).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Valor, costo y riesgo](./valor-costo-y-riesgo.md) · [Variable independiente →](./variable-independiente.md)
