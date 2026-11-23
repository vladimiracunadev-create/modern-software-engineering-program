# Percentil 85

[↑ Glosario](../../README.md) · [← Percentil 75](./percentil-75.md) · [Percentil 95 →](./percentil-95.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Valor que se supera el 15 % de las veces en un conjunto de resultados.

Definición de trabajo de [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md).

## Por qué importa

La clase donde se define, [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md), existe con este propósito: la clase existe para que conviertas una estimación en un compromiso que se pueda cumplir y defender.

## Cómo funciona

Según [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md):

La suma de las medianas de doce tareas es el valor mediano de un proyecto **solo si las duraciones son simétricas**. Con una cola larga hacia arriba, el total tiende a quedar por encima de la suma de medianas, porque los excesos de unas tareas no se compensan con los defectos de otras (el defecto está acotado por cero). Además, las tareas de un mismo proyecto no son independientes: comparten ambigüedad, herramientas y personas, de modo que cuando una tarda más, varias lo hacen. Un factor común hace que el total tenga una dispersión mayor (colas más pesadas) aunque su mediana se acerque a la suma.

Según [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo toma las últimas 24 semanas de entrega, que incluyen tres semanas con cero elementos terminados por guardia, y pronostica los sesenta elementos pendientes: percentil 50 en 13 semanas y percentil 85 en 14 a 15. Antes de comunicar, repite el cálculo con las últimas 12 semanas y ve que el percentil 85 se mueve entre 13 y 16: lo comunica como rango. Redacta el compromiso: «con 85 % de probabilidad, la exportación adaptada estará entregada antes de 15 semanas; con 50 %, antes de 13. Supuestos: alcance de los 60 elementos, equipo de ocho sin cambios, guardia como en el historial.

## Ejemplo

Ejemplo de [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) (sección «Ejemplo mínimo»):

El fragmento simula doce tareas con mediana de cinco días y dispersión logarítmica de 0,59 (1,8 elevado a una variable normal) y mira la mediana y el percentil 85 del total. Antes de ejecutarlo, predice si la mediana es mayor, igual o menor que 60.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md)) son:

- **Se incumple la fecha pese a estimaciones razonables** — causa: se sumaron medianas. Corrección: simular el total y comunicar percentiles.
- **El pronóstico cambia mucho de una semana a otra** — causa: historial muy corto. Corrección: repetir con subconjuntos y comunicar rango.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md)) son: Las definiciones son operativas para el equipo de plataforma educativa. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con las fuentes primarias enlazadas al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se estimó ni se pronosticó ningún proyecto real; las duraciones lognormales, el factor común, el historial de Poisson y la cola de un servidor son construcciones del autor, y el modelo supone semanas independientes y elementos de tamaño parecido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Resultado](../r/resultado.md), [Valor](../v/valor.md), [Compromiso probabilístico](../c/compromiso-probabilistico.md), [Pronóstico por simulación](./pronostico-por-simulacion.md), [Trabajo en curso](../t/trabajo-en-curso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-191](../../../classes/part-15-procesos-planificacion-y-estimacion/se-191-taller-planificar-bajo-incertidumbre-explicita/README.md), [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-192](../../../classes/part-15-procesos-planificacion-y-estimacion/se-192-proyecto-plan-adaptativo-con-evidencia-y-guardrails/README.md), [SE-185](../../../classes/part-15-procesos-planificacion-y-estimacion/se-185-estimacion-por-tamano-rango-y-evidencia-historica/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Buehler, Griffin y Ross, «Exploring the "planning fallacy"»](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación sistemática de plazos; autoridad: Journal of Personality and Social Psychology.
- [Little, «A Proof for the Queuing Formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) — relación entre trabajo en curso, ritmo y permanencia; autoridad: Operations Research.
- [Kingman, «The single server queue in heavy traffic»](https://doi.org/10.1017/S0305004100036094) — espera con alta utilización; autoridad: Mathematical Proceedings of the Cambridge Philosophical Society.
- [Kanban Guide](https://kanbanguides.org/english/) — límites de trabajo en curso, métricas de flujo y expectativa de servicio; autoridad: Kanban Guides.
- [Python, módulo `statistics`](https://docs.python.org/3/library/statistics.html) — mediana y cuantiles; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Percentil 75](./percentil-75.md) · [Percentil 95 →](./percentil-95.md)
