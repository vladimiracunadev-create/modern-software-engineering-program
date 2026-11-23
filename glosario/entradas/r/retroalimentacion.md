# Retroalimentación

[↑ Glosario](../../README.md) · [← Retraso de replicación](./retraso-de-replicacion.md) · [Retroalimentación con uso real →](./retroalimentacion-con-uso-real.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Respuesta perceptible de un sistema a una acción de la persona.

Definición de trabajo de [SE-171 — Interacción, affordances y retroalimentación](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-002 — Historia de la crisis del software a la ingeniería continua](../../../classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md): Información que llega a tiempo para modificar una decisión.
- En [SE-583 — Verificación, gates y menú único de validación](../../../classes/part-48-harness-y-agentic-engineering/se-583-verificacion-gates-y-menu-unico-de-validacion/README.md): Información que el agente recibe tras una acción.

## Por qué importa

En [SE-532 — Mentoría, feedback y crecimiento](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md), el tema «Retroalimentación» importa porque su efecto depende del objeto, el momento y el formato.

## Cómo funciona

Según [SE-532 — Mentoría, feedback y crecimiento](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md):

La **práctica deliberada** (Ericsson et al.) describe la mejora como resultado de tareas definidas con precisión, de dificultad ligeramente superior al nivel actual, con retroalimentación inmediata y oportunidad de repetir. Las tareas muy fáciles no producen aprendizaje y las muy difíciles producen fracaso sin información útil sobre qué corregir. La mentora decide la brecha: qué tan por encima del nivel actual está la tarea. En ingeniería de software una tarea que estira tiene límites claros (qué se entrega y cómo se sabe que está bien), es verificable por pruebas o por revisión, y deja un artefacto que la persona puede explicar. Asignar siempre tareas fáciles por protección es una forma de abandono; asignar siempre tareas difíciles por confianza es una forma de descuido.

Según [SE-532 — Mentoría, feedback y crecimiento](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md):

Escenario hipotético, construido para la clase y sin datos reales. La mentora y la ingeniera nueva firman un acuerdo de seis meses con una meta («asumir la responsabilidad del módulo de exportación con revisión de otra persona»), una reunión cada dos semanas y tres tareas escalonadas: ajustar una regla de formato con pruebas existentes, escribir la prueba de caracterización de la exportación y diseñar el contrato de versiones con el equipo de calificaciones. La mentora revisa cada cambio el mismo día y escribe comentarios sobre el código con la forma «esta línea convierte fechas sin zona horaria; en la exportación de marzo causó dos filas erróneas; prueba `datetime.fromisoformat` con zona explícita».

## Ejemplo

Ejemplo de [SE-532 — Mentoría, feedback y crecimiento](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md) (sección «Ejemplo mínimo»):

El fragmento mide qué fracción de errores se evita según cuándo llega la retroalimentación en un modelo sencillo de 60 días. Antes de ejecutarlo, predice cuál es mayor.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La persona repite el mismo error** — causa: retroalimentación tardía o vaga. Corrección: dar el aviso en el mismo cambio, con línea y efecto. ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md))
- **La retroalimentación se percibe como ataque** — causa: se dirige a la persona. Corrección: describir el comportamiento y su efecto. ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El metaanálisis de Kluger y DeNisi mostró que la retroalimentación mejora el desempeño de media, pero que en más de un tercio de los casos lo empeora, sobre todo cuando atrae la atención hacia la persona (cómo se ve a sí misma) y no hacia la tarea (qué se hizo y cómo mejorarlo). ([SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md))

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
