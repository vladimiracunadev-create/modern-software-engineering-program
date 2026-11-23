# Tarea

[↑ Glosario](../../README.md) · [← Tapado](./tapado.md) · [Tarea de regresión →](./tarea-de-regresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Acción con verbo y resultado observable que una audiencia quiere completar usando la documentación.

Definición de trabajo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md): Objetivo de una persona con un resultado observable, independiente de la pantalla que se use para lograrlo.
- En [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md): Unidad de trabajo que el bucle de eventos toma de una cola y ejecuta hasta vaciar la pila.
- En [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md): Unidad de trabajo ordenada, con dependencias, archivos afectados y, si procede, marca de ejecución en paralelo.

## Por qué importa

En [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), el tema «Tarea» importa porque es la unidad por la que alguien busca; si la página no responde a un verbo, no se encuentra.

## Cómo funciona

Según [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), en la sección «Tarea»:

Una tarea tiene un verbo y un resultado observable: «cambiar el plazo de una tarea y avisar a la clase». Es la unidad por la que la gente busca, aunque no la formule como título. Una página que responde a una tarea puede reconocerse porque termina cuando el resultado existe; una página que describe «el módulo de calendario» no termina nunca. Las tareas también delimitan lo que no hay que escribir: si ninguna audiencia necesita saber cómo se implementa el redondeo para hacer su tarea, esa explicación pertenece a otra página, y quien la necesita la encontrará por su propia tarea (depurar, auditar). Un inventario de tareas por audiencia, aunque sea de quince filas, expone dos defectos que el índice de componentes oculta: tareas sin página y páginas sin tarea.

## Ejemplo

Ejemplo de [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) (sección «Ejemplo profesional»):

El portal documental de la plataforma de entregas tiene un inventario de tareas por audiencia en `audiencias.md`: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga, corregir una nota), secretaría (exportar el acta con la nota final), mantenimiento (depurar el cálculo, cambiar el tope). La regla vive en `politica/penalizacion.md`, versionada, con responsable y fecha de revisión. Las cuatro vistas enlazan esa fuente con una frase de contexto cada una. Cuando la política cambia el tope al 30 %, el cambio es un único commit en la fuente y una lista de verificación señala las cuatro vistas para revisar.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Nadie encuentra «cómo cambiar el plazo» aunque existe la página** — causa: el título usa el nombre del componente («Módulo de calendario») y no la tarea. Corrección: reescribir el título con verbo y resultado y añadirla al índice de tareas. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))
- **Una página explica todo y nadie la termina** — causa: mezcla audiencias y tareas en un solo texto. Corrección: separar por audiencia o por tarea y enlazar lo común. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))
- **La documentación «está completa» pero las preguntas siguen llegando por mensaje** — causa: se documentó lo que se sabía y no lo que se pregunta. Corrección: registrar las preguntas recibidas y convertir las repetidas en páginas por tarea. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una página que responde a una tarea puede reconocerse porque termina cuando el resultado existe; una página que describe «el módulo de calendario» no termina nunca. ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md))
- La distinción importa porque dos diseños muy distintos pueden resolver la misma tarea (un formulario, un arrastre de archivo, un envío por correo) y porque una función puede existir sin servir a ninguna tarea. ([SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Dependencia](../d/dependencia.md), [Evento](../e/evento.md), [Resultado](../r/resultado.md), [Embudo](../e/embudo.md), [Escenario de uso](../e/escenario-de-uso.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-169 — Diseño centrado en personas y tareas](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-205 — Documentación orientada a tareas y audiencias](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-230 — JavaScript, DOM y eventos del navegador](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) — [Parte 19](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md), Web, frontend y aplicaciones progresivas.
- [SE-566 — Constitución, specify, clarify, plan y tasks](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (281 clases más lo mencionan; las que más):

[SE-563](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-563-taller-comparar-flujos-manual-asistido-y-automatizado/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-532](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-532-mentoria-feedback-y-crecimiento/README.md).

**Aparece en los casos de estudio:** [Airbnb](../../../casos/exito/airbnb.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [Caída global de Meta](../../../casos/fallo/meta-2021.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gould y Lewis, «Designing for usability» (CACM, 1985)](https://doi.org/10.1145/3166.3170) — principios de diseño centrado en usuarios y tareas; autoridad: Communications of the ACM.
- [HTML Standard: bucles de eventos (WHATWG)](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops) — tareas, microtareas y renderizado; autoridad: WHATWG.
- [web.dev: Interaction to Next Paint](https://web.dev/articles/inp) — latencia de interacción y tareas largas; autoridad: Google web.dev.
- [web.dev: Optimizar tareas largas](https://web.dev/articles/optimize-long-tasks) — fragmentar el trabajo y ceder el control; autoridad: Google web.dev.
- [Spec Kit — referencia del proceso agentic](https://github.github.io/spec-kit/reference/agentic-sdd.html) — secuencia de comandos, clarificación, análisis y tareas; autoridad: GitHub y mantenedores de la comunidad.

---

[↑ Glosario](../../README.md) · [← Tapado](./tapado.md) · [Tarea de regresión →](./tarea-de-regresion.md)
