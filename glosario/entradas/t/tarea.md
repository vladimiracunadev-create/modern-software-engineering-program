# Tarea

[↑ Glosario](../../README.md) · [← Tapado](./tapado.md) · [Tarea de regresión →](./tarea-de-regresion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

**Tarea** es una palabra con varios sentidos en el programa. El principal ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), documentación) es una acción con verbo y resultado observable que una audiencia quiere completar usando la documentación. [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md) (usabilidad) la define como el objetivo de una persona con un resultado observable, independiente de la pantalla que se use. [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md) (concurrencia) la usa para la unidad de trabajo que el bucle de eventos toma de una cola y ejecuta hasta vaciar la pila. [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md) (desarrollo asistido por IA) la usa para una unidad de trabajo ordenada, con dependencias, archivos afectados y, si procede, marca de ejecución en paralelo. Esta entrada desarrolla sobre todo el sentido de personas ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md)) y señala los técnicos.

## Por qué importa

Una tarea es la unidad por la que la gente busca, aunque no la formule como título. Si una página no responde a un verbo, no se encuentra; si una interfaz se diseña por pantallas y no por tareas, se pierde el objetivo de la persona. Cambia cómo se organiza la documentación y cómo se evalúa la usabilidad: por tareas completadas, no por páginas escritas.

## Cómo funciona

Una tarea tiene **un verbo y un resultado observable**: «cambiar el plazo de una tarea y avisar a la clase». Se reconoce la página que responde a una tarea porque **termina cuando el resultado existe**; una página que describe «el módulo de calendario» no termina nunca. Las tareas además delimitan lo que no hay que escribir: si ninguna audiencia necesita saber cómo se implementa el redondeo para hacer su tarea, esa explicación pertenece a otra página.

En usabilidad ([SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md)), la tarea es independiente de la pantalla: «entregar el trabajo» puede hacerse desde el móvil o la web, y evaluar por tarea permite comparar diseños distintos con el mismo criterio de éxito.

En los sentidos técnicos, la lógica es parecida: una tarea del bucle de eventos ([SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md)) es una unidad que se ejecuta hasta vaciar la pila; una tarea de un plan de IA ([SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md)) es una unidad ordenada con dependencias y archivos afectados, de modo que las independientes pueden ejecutarse en paralelo y las dependientes, en orden.

## Ejemplo

El portal documental de la plataforma de entregas ([SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md)) tiene un inventario de tareas por audiencia: estudiante (entender el descuento, pedir prórroga), docente (cambiar plazo, conceder prórroga, corregir una nota), secretaría (exportar el acta con la nota final) y mantenimiento (depurar el cálculo, cambiar el tope). «Conceder prórroga» es una tarea con verbo y resultado: tras la guía, la prórroga existe y la estudiante ve el nuevo plazo.

## Errores y confusiones comunes

- **Páginas por módulo, no por tarea**: nadie encuentra lo que busca.
- **Confundir tarea con función del producto**: la función es del producto; la tarea, de la persona.
- **Definir la tarea por la pantalla**: se pierde el objetivo.
- **Mezclar los sentidos**: tarea de documentación, de usabilidad, del bucle de eventos y de un plan de IA son conceptos distintos.

## Límites y cuándo no aplica

Para documentación de referencia (parámetros, firmas), la tarea no es el eje: se organiza como el producto. Una tarea mal acotada (demasiado grande) no «termina» y no se puede comprobar. En el sentido técnico de concurrencia, no hay relación con las tareas de los equipos ni de los tableros.

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
