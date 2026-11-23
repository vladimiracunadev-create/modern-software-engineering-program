# Tiempo de ciclo o plazo

[↑ Glosario](../../README.md) · [← Tiempo agotado ambiguo](./tiempo-agotado-ambiguo.md) · [Tiempo de llegada →](./tiempo-de-llegada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Tiempo desde que un elemento entra al sistema hasta que sale terminado.

Definición de trabajo de [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md): Tiempo desde que un elemento empieza a trabajarse hasta que se termina.

## Por qué importa

La clase donde se define, [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), existe con este propósito: la clase existe para que expliques con un modelo cuantitativo por qué el trabajo espera, qué palanca reduce esa espera (menos trabajo en curso, menos variabilidad, lotes más pequeños, más capacidad) y por qué una persona o un equipo al 95 % de utilización no es eficiente sino frágil.

## Cómo funciona

[SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md):

El equipo de la plataforma de entregas mide el tablero durante cuatro semanas: 18 elementos en curso de media y un rendimiento de 3 por semana, que por Little implica un plazo medio de 6 semanas, y es lo que ven. Proponen un límite de 9 (tres por persona) y una regla: si alguien queda sin trabajo disponible, ayuda a terminar el elemento más antiguo antes de empezar otro. Además, la revisión de código deja de hacerse los viernes en bloque y pasa a ser inmediata, para eliminar lotes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)) son:

- **El plazo crece sin que el rendimiento baje** — causa: el trabajo en curso crece. Corrección: aplicar la ley de Little y fijar un límite.
- **Se pide llegar al 100 % de ocupación** — causa: se confunde ocupación con eficiencia. Corrección: mostrar la curva de espera y fijar una utilización objetivo.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se observó ningún tablero real: las colas de un servidor, las tareas exponenciales y los lotes de cinco son construcciones del autor, y la simulación cerca del 95 % queda por debajo de la fórmula por convergencia lenta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Antigüedad del trabajo en curso](../a/antiguedad-del-trabajo-en-curso.md), [Escape](../e/escape.md), [Ley de Goodhart](../l/ley-de-goodhart.md), [Ley de Little](../l/ley-de-little.md), [Lote](../l/lote.md), [Rendimiento](../r/rendimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-184 — Lean, teoría de colas y límites de trabajo](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

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

[↑ Glosario](../../README.md) · [← Tiempo agotado ambiguo](./tiempo-agotado-ambiguo.md) · [Tiempo de llegada →](./tiempo-de-llegada.md)
