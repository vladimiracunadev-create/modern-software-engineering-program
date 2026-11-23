# Carril exprés

[↑ Glosario](../../README.md) · [← Carrera entre peticiones](./carrera-entre-peticiones.md) · [Cascada de reinicios →](./cascada-de-reinicios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Capacidad reservada para trabajo urgente, con sus propias reglas de admisión.

Definición de trabajo de [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

## Por qué importa

La clase donde se define, [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), existe con este propósito: la clase existe para que elijas o combines marcos por la política que cada uno impone (cuándo entra trabajo, cuánto se compromete, qué se recorta) y por el problema que resuelve, en lugar de adoptar uno entero por reputación.

## Cómo funciona

Según [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md):

Un trabajo urgente que requiere 2 días llega en un momento uniforme dentro de un sprint de 10 días. Hay tres personas; los elementos en curso tienen una mediana de 2,6 días (lognormal, σ = 0,6) y cada uno lleva una fracción aleatoria consumida. En Scrum con alcance cerrado, el urgente espera al siguiente sprint. En Kanban con extracción, lo toma quien se libere primero. Con carril exprés, una ranura reservada lo atiende de inmediato. Se simulan 5000 llegadas.

Según [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md):

Compara el caso de un reporte urgente con el de una mejora grande de la exportación: el primero se atiende en menos de tres días por el carril exprés; la segunda se recorta en la cuarta semana porque una pieza resultó más grande de lo previsto. Una combinación es adecuada cuando cada política responde a una pregunta escrita; es débil cuando se defiende con «así lo hace el marco».

## Ejemplo

Ejemplo de [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sección «Ejemplo profesional»):

Compara el caso de un reporte urgente con el de una mejora grande de la exportación: el primero se atiende en menos de tres días por el carril exprés; la segunda se recorta en la cuarta semana porque una pieza resultó más grande de lo previsto. Una combinación es adecuada cuando cada política responde a una pregunta escrita; es débil cuando se defiende con «así lo hace el marco».

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los urgentes esperan hasta el siguiente sprint** — causa: alcance cerrado sin carril exprés. Corrección: reservar capacidad con una definición escrita de urgencia. ([SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** la espera de Scrum aparece porque el alcance del sprint está comprometido, no porque el marco lo exija; un equipo puede reservar capacidad para urgencias o renegociar con quien lleva el producto, y entonces se parece al carril exprés. ([SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](./capacidad.md), [Regla](../r/regla.md), [Trabajo](../t/trabajo.md), [Apetito](../a/apetito.md), [Compromiso](./compromiso.md), [Límite de trabajo en curso](../l/limite-de-trabajo-en-curso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — definición oficial de Scrum; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [The Kanban Guide](https://kanbanguides.org/english/) — definición de Kanban y sus prácticas; autoridad: Scrum.org (Kanban Guide).
- [Extreme Programming: valores](http://www.extremeprogramming.org/values.html) — valores de XP; autoridad: sitio de la práctica.
- [Singer, «Shape Up»](https://basecamp.com/shapeup) — ciclos de apetito fijo y alcance variable; autoridad: Basecamp.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — integración frecuente como práctica técnica; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Carrera entre peticiones](./carrera-entre-peticiones.md) · [Cascada de reinicios →](./cascada-de-reinicios.md)
