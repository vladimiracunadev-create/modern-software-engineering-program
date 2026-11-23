# Compromiso

[↑ Glosario](../../README.md) · [← Comprobación previa de CORS](./comprobacion-previa-de-cors.md) · [Compromiso de capacidad →](./compromiso-de-capacidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Previsión de qué se terminará en un ciclo, con la regla usada para calcularla.

Definición de trabajo de [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md): Decisión que mejora un atributo a costa de otro.

## Por qué importa

La clase donde se define, [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md), existe con este propósito: la clase existe para que elijas o combines marcos por la política que cada uno impone (cuándo entra trabajo, cuánto se compromete, qué se recorta) y por el problema que resuelve, en lugar de adoptar uno entero por reputación.

## Cómo funciona

Según [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md):

Scrum organiza el trabajo en sprints de longitud fija con un objetivo, una lista de elementos seleccionada y tres roles (responsable del producto, equipo de desarrollo, facilitación). Su política de entrada es en lotes: lo nuevo espera a la planificación del siguiente sprint, salvo renegociación con quien lleva el producto. Su política de compromiso es una previsión del equipo, no una promesa. La guía permite cambiar alcance durante el sprint si el objetivo se mantiene; muchos equipos lo convierten en una regla rígida que la guía no escribe. Lo que aporta es ritmo, un lugar para inspeccionar y adaptar, y un horizonte corto para la previsión.

Según [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md):

Los tiene, pero se expresan como previsión de flujo (percentiles del plazo de los elementos) y no como compromiso de ciclo. `SE-189` desarrolla esas métricas.

## Ejemplo

Ejemplo de [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas continúa como caso conductor de la [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md). Esta clase deja el tercer artefacto: las tres políticas del equipo (entrada, compromiso, recorte) con su regla y su efecto medido. `SE-184` explicará con teoría de colas por qué la extracción y el límite de trabajo acortan la espera. Cambia después una sola política, por ejemplo el porcentaje de capacidad reservado para urgencias, y revisa qué otras mediciones cambian.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Casi la mitad de los sprints no se cumple y se culpa al equipo** — causa: compromiso con la media del rendimiento. Corrección: comprometer con un valor prudente y llenar el resto con trabajo opcional. ([SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Su política de compromiso es una previsión del equipo, no una promesa. ([SE-183](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md))
- **riesgos** (decisiones que pueden causar problemas), **puntos de sensibilidad** (parámetros de los que depende mucho un atributo) y **compromisos** (decisiones que mejoran un atributo a costa de otro). ([SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Ciclo](./ciclo.md), [Regla](../r/regla.md), [Apetito](../a/apetito.md), [Árbol de utilidad](../a/arbol-de-utilidad.md), [Carril exprés](./carril-expres.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-183 — Scrum, Kanban, XP y Shape Up](../../../classes/part-15-procesos-planificacion-y-estimacion/se-183-scrum-kanban-xp-y-shape-up/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-335 — Taller: revisar una arquitectura contra escenarios](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) — [Parte 27](../../../classes/part-27-arquitectura-de-software-y-dominio/README.md), Arquitectura de software y dominio.

**También se usa en** (110 clases más lo mencionan; las que más):

[SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md), [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md), [SE-404](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-404-escalado-capacidad-y-costos/README.md), [SE-138](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-138-experimentos-sesgos-y-causalidad-basica/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md), [SE-478](../../../classes/part-39-build-release-y-cadena-de-suministro/se-478-riesgos-de-ci-y-dependencias-comprometidas/README.md), [SE-095](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Slack](../../../casos/exito/slack.md), [Knight Capital](../../../casos/fallo/knight-capital.md), [TSB Bank](../../../casos/fallo/tsb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «trade-off».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — definición oficial de Scrum; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [The Kanban Guide](https://kanbanguides.org/english/) — definición de Kanban y sus prácticas; autoridad: Scrum.org (Kanban Guide).
- [Extreme Programming: valores](http://www.extremeprogramming.org/values.html) — valores de XP; autoridad: sitio de la práctica.
- [Singer, «Shape Up»](https://basecamp.com/shapeup) — ciclos de apetito fijo y alcance variable; autoridad: Basecamp.
- [Fowler, «Continuous Integration»](https://martinfowler.com/articles/continuousIntegration.html) — integración frecuente como práctica técnica; autoridad: martinfowler.com.

---

[↑ Glosario](../../README.md) · [← Comprobación previa de CORS](./comprobacion-previa-de-cors.md) · [Compromiso de capacidad →](./compromiso-de-capacidad.md)
