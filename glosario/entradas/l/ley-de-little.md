# Ley de Little

[↑ Glosario](../../README.md) · [← Ley de Goodhart](./ley-de-goodhart.md) · [Licencia de software →](./licencia-de-software.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **ley de Little** afirma que, en un sistema estable, el número medio de elementos dentro del sistema es igual a la tasa media de llegadas por el tiempo medio que cada elemento pasa dentro: **L = λ · W**. Es la formulación de [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-396](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) y [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md), que la aplican a tableros de trabajo, colas de peticiones y concurrencia de servicios. Es una identidad, no un modelo: no necesita suponer distribuciones de llegada, de servicio ni orden de atención.

## Por qué importa

Convierte tres números que suelen medirse por separado en una comprobación de coherencia y en una herramienta de dimensionamiento. Para un equipo, [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) lo traduce en una frase práctica: plazo medio = trabajo en curso ÷ rendimiento; si el rendimiento no cambia, duplicar el trabajo en curso duplica el plazo. Para un servicio, [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) muestra que se usa para saber cuántas solicitudes concurrentes hay que soportar.

## Cómo funciona

Con **L** el número medio de elementos en el sistema, **λ** la tasa media de llegadas (en régimen estable, igual a la de terminaciones) y **W** el tiempo medio de estancia, cualquiera de los tres se despeja de los otros dos. Dos usos que las clases desarrollan:

1. **Comprobar una medición.** Si un panel dice 50 solicitudes en vuelo, 100 por segundo y 300 ms de latencia media, la ley exige 100 × 0,3 = 30; como 50 ≠ 30, alguno de los tres números mide otra cosa ([SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)).
2. **Dimensionar.** Un servicio de 200 solicitudes por segundo con 500 ms de estancia media necesita soportar 200 × 0,5 = 100 solicitudes concurrentes ([SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)).

Vale sin más supuestos porque no depende de la distribución de llegadas, de la del servicio ni de la disciplina de la cola ([SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md)). Su condición es que el sistema esté en **régimen estable** y que las definiciones de «dentro» sean coherentes ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)).

## Ejemplo

En el tablero de trabajo de [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), con un límite de trabajo en curso igual al número de personas, el rendimiento llega a unos 3 elementos por día y no crece más, mientras que el plazo crece linealmente y coincide con n ÷ rendimiento, como predice la ley. La clase usa esa relación para proponer un límite de trabajo en curso para el tablero del equipo, con la observación que lo cambiaría. Los números son de una simulación con datos sintéticos.

## Errores y confusiones comunes

- **No cuadra con el tablero.** Elementos abandonados o fechas de inicio inconsistentes rompen la igualdad. Corrección ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)): definir qué entra, qué sale y qué fecha cuenta, y recalcular.
- **El plazo crece sin que baje el rendimiento.** Es el trabajo en curso el que crece; aplicar la ley y fijar un límite.
- **Creer que la ley predice la espera por sí sola.** Relaciona promedios; no dice cómo se distribuye la espera ni cómo crece cerca de la saturación, cosa que [SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) trata aparte con utilización y variabilidad.

## Límites y cuándo no aplica

Little advirtió que la ley exige un sistema en régimen estable y definiciones coherentes de qué es «dentro» ([SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)). No describe lo que ocurre durante picos transitorios, ni da percentiles: dos sistemas con el mismo L, λ y W pueden tener colas de latencia muy distintas. Tampoco dice qué hacer cuando el sistema no es estable (la cola crece sin límite): ahí no hay promedio que relacionar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Concurrencia](../c/concurrencia.md), [Relación](../r/relacion.md), [Backpressure](../b/backpressure.md), [Cola de muertos](../c/cola-de-muertos.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Handler idempotente](../h/handler-idempotente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-321 — Resiliencia: bulkhead, sidecar, ambassador y degradación](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-396 — Proyecto: servicio distribuido con degradación](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-396-proyecto-servicio-distribuido-con-degradacion/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-404 — Escalado, capacidad y costos](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-436 — Latencia, throughput, saturación y capacidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Little, «A proof for the queuing formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) — ley de Little; autoridad: artículo original, Operations Research 1961.
- [Little, «Little's law as viewed on its 50th anniversary» (Operations Research, 2011)](https://doi.org/10.1287/opre.1110.0940) — condiciones y usos de la ley; autoridad: Operations Research.
- [Kingman, «The single server queue in heavy traffic» (Math. Proc. Cambridge Philos. Soc., 1961)](https://doi.org/10.1017/S0305004100036094) — aproximación de la espera con carga alta; autoridad: Cambridge Philosophical Society.
- [The Kanban Guide](https://kanbanguides.org/english/) — límites de trabajo y gestión del flujo; autoridad: Scrum.org (Kanban Guide).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — gestión de ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Ley de Goodhart](./ley-de-goodhart.md) · [Licencia de software →](./licencia-de-software.md)
