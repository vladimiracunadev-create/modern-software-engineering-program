# Retroalimentación

[↑ Glosario](../../README.md) · [← Retraso de replicación](./retraso-de-replicacion.md) · [Retroalimentación con uso real →](./retroalimentacion-con-uso-real.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

La **retroalimentación** (*feedback*) es información que vuelve a quien actuó, a tiempo para modificar su siguiente decisión ([SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md)). El programa la usa con tres matices:

- **De una interfaz** ([SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md)): la respuesta perceptible de un sistema a una acción de la persona.
- **De un agente** ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)): la información que el agente recibe tras una acción.
- **De una persona** ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md)): la que recibe en mentoría o revisión, que mejora el desempeño solo si es oportuna y específica.

## Por qué importa

Sin retroalimentación, no hay corrección. Un ciclo corto (probar, ver, ajustar) es lo que distingue el aprendizaje del repetir errores, tanto en personas como en sistemas. Cambia el diseño del trabajo: qué se mide, cuándo se avisa, y a quién.

## Cómo funciona

**En desarrollo** ([SE-002](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md)): la ingeniería continua acorta el ciclo entre una decisión y su efecto observable (pruebas, integración continua, revisión); la información debe llegar a tiempo para cambiar la decisión.

**En personas** ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md)): la práctica deliberada (Ericsson y colegas) describe la mejora como resultado de tareas precisas, de dificultad ligeramente superior al nivel actual, con retroalimentación inmediata y oportunidad de repetir. Los comentarios útiles tienen forma: «esta línea convierte fechas sin zona horaria; en la exportación de marzo causó dos filas erróneas; prueba `datetime.fromisoformat` con zona explícita» (línea, efecto, siguiente paso). El metaanálisis de Kluger y DeNisi mostró que la retroalimentación mejora el desempeño de media, pero que en más de un tercio de los casos lo empeora, sobre todo cuando atrae la atención hacia la persona (cómo se ve a sí misma) y no hacia la tarea (qué se hizo y cómo mejorarlo).

**En agentes** ([SE-583](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md)): lo que el agente recibe tras cada acción determina qué hace después: un resultado claro de una compuerta permite corregir; uno ambiguo, no.

## Ejemplo

Revisión de código el mismo día, con línea, efecto y camino de mejora, frente a un comentario genérico («esto está mal») una semana después. Ilustración de retroalimentación de un agente:

```text
pytest: 1 failed — test_exporta_fecha: esperado 2026-03-01T00:00+00:00, obtenido 2026-03-01T00:00
```

## Errores y confusiones comunes

- **La persona repite el mismo error.** Causa: retroalimentación tardía o vaga; corrección: dar el aviso en el mismo cambio, con línea y efecto ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md)).
- **Se percibe como ataque.** Causa: se dirige a la persona; corrección: describir el comportamiento y su efecto ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md)).
- **Confundir cantidad con calidad.** Más comentarios no mejoran si no son específicos y accionables.

## Límites y cuándo no aplica

La retroalimentación no corrige un problema de diseño del trabajo: si la tarea es demasiado difícil, solo informa del fracaso. Un ciclo muy corto sin criterio de qué importa genera ruido. Y la evidencia citada (Kluger y DeNisi) indica que puede empeorar el desempeño: hay que diseñarla, no solo darla.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agente](../a/agente.md), [Affordance percibida](../a/affordance-percibida.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Crisis del software](../c/crisis-del-software.md), [Ingeniería continua](../i/ingenieria-continua.md), [Integración continua](../i/integracion-continua.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.
- [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-532 — Mentoría, feedback y crecimiento](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.
- [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (121 clases más lo mencionan; las que más):

[SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), [SE-182](../../../classes/part-15-procesos-planificacion-y-estimacion/se-182-agile-como-principios-y-no-como-ceremonia/README.md), [SE-170](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-170-arquitectura-de-informacion-y-navegacion/README.md), [SE-172](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-172-estados-vacios-carga-error-y-recuperacion/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md), [SE-533](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-533-estimacion-organizacional-y-compromisos/README.md), [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Kluger y DeNisi, «The effects of feedback interventions on performance»](https://doi.org/10.1037/0033-2909.119.2.254) — efectos de la retroalimentación; autoridad: Psychological Bulletin.
- [Ericsson, Krampe y Tesch-Römer, «The role of deliberate practice in the acquisition of expert performance»](https://doi.org/10.1037/0033-295X.100.3.363) — práctica deliberada; autoridad: Psychological Review.
- [Software Engineering at Google, cap. 3 «Knowledge Sharing»](https://abseil.io/resources/swe-book/html/ch03.html) — transferencia de conocimiento; autoridad: equipo de ingeniería de Google.
- [Software Engineering at Google, cap. 9 «Code Review»](https://abseil.io/resources/swe-book/html/ch09.html) — revisión de código como aprendizaje; autoridad: equipo de ingeniería de Google.
- [Kahneman, Sibony y Sunstein, *Noise*](https://openlibrary.org/isbn/9780316451406) — ruido en los juicios; autoridad: libro con ISBN 978-0-316-45140-6.

---

[↑ Glosario](../../README.md) · [← Retraso de replicación](./retraso-de-replicacion.md) · [Retroalimentación con uso real →](./retroalimentacion-con-uso-real.md)
