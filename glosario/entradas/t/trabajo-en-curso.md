# Trabajo en curso

[↑ Glosario](../../README.md) · [← Trabajo diferido](./trabajo-diferido.md) · [Trabajo venenoso →](./trabajo-venenoso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** desarrollada · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

El **trabajo en curso** (*work in progress*, WIP) es la cantidad de elementos iniciados y no terminados ([SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md)).

## Por qué importa

Explica por qué un equipo con muchas cosas abiertas termina todo más tarde. Reducir el tiempo de permanencia sin reducir el ritmo de entrega exige reducir el trabajo en curso.

## Cómo funciona

[SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) aplica la ley de Little: en un sistema estable, el trabajo promedio en curso es el ritmo de entrada por el tiempo promedio de permanencia. Si el ritmo es fijo, bajar el tiempo exige bajar el WIP. Además, según Kingman, la espera de una cola de un servidor crece de forma brusca al aproximarse la utilización a uno: un equipo al 95 % no tiene elementos lentos por pereza sino por saturación. El compromiso incluye entonces un **límite de trabajo en curso** y una **reserva de capacidad**.

## Ejemplo

Un equipo con 20 elementos abiertos y que termina 4 por semana tarda en promedio 5 semanas por elemento (20 / 4). Al limitar el WIP a 8, el tiempo medio baja a 2 semanas sin cambiar el ritmo. (Ilustración de la ley de Little.)

## Errores y confusiones comunes

**Los elementos tardan cada vez más.** Equipo saturado; limitar el trabajo en curso y reservar capacidad.

## Límites y cuándo no aplica

La ley de Little supone un sistema estable. Limitar el WIP no sirve si se reabre trabajo que ya estaba cerrado; y una reserva de capacidad tiene costo aparente de «ociosidad» que debe explicarse.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Compromiso probabilístico](../c/compromiso-probabilistico.md), [Percentil 85](../p/percentil-85.md), [Pronóstico por simulación](../p/pronostico-por-simulacion.md), [Utilización](../u/utilizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-533 — Estimación organizacional y compromisos](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), [SE-345](../../../classes/part-28-estilos-arquitectonicos/se-345-12-factor-y-aplicaciones-nativas-de-la-nube/README.md), [SE-190](../../../classes/part-15-procesos-planificacion-y-estimacion/se-190-retrospectivas-y-mejora-del-sistema-de-trabajo/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Little, «A Proof for the Queuing Formula: L = λW»](https://doi.org/10.1287/opre.9.3.383) — relación entre trabajo en curso, ritmo y permanencia; autoridad: Operations Research.
- [Kanban Guide](https://kanbanguides.org/english/) — límites de trabajo en curso, métricas de flujo y expectativa de servicio; autoridad: Kanban Guides.
- [Buehler, Griffin y Ross, «Exploring the "planning fallacy"»](https://doi.org/10.1037/0022-3514.67.3.366) — subestimación sistemática de plazos; autoridad: Journal of Personality and Social Psychology.
- [Kingman, «The single server queue in heavy traffic»](https://doi.org/10.1017/S0305004100036094) — espera con alta utilización; autoridad: Mathematical Proceedings of the Cambridge Philosophical Society.
- [Python, módulo `statistics`](https://docs.python.org/3/library/statistics.html) — mediana y cuantiles; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Trabajo diferido](./trabajo-diferido.md) · [Trabajo venenoso →](./trabajo-venenoso.md)
