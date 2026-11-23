# Escape

[↑ Glosario](../../README.md) · [← Escáner previo al envío](./escaner-previo-al-envio.md) · [Escape hatch y ownership →](./escape-hatch-y-ownership.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Defecto que supera las puertas del proceso y se descubre después de dar el trabajo por terminado.

Definición de trabajo de [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md): Defecto que llega a producción sin ser detectado.
- En [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md): Defecto descubierto después de dar un incremento por terminado.

## Por qué importa

En [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), el tema «Correlación entre comprobaciones» importa porque añadir una comprobación que ve lo mismo que otra casi no reduce los escapes.

## Cómo funciona

Según [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md):

Si cada comprobación detectara defectos al azar con su propia probabilidad, añadir otra siempre reduciría los escapes de forma multiplicativa. Pero las comprobaciones miran cosas parecidas: los defectos «fáciles» los ve cualquiera y los «difíciles» se escapan a todas. Esa correlación hace que la segunda y la tercera comprobación aporten mucho menos de lo esperado, y que a partir de cierto punto no aporten nada. Jones observó que ninguna técnica los elimina todos y que las combinaciones de técnicas distintas rinden más que repetir la misma. La consecuencia de diseño es elegir comprobaciones que vean defectos distintos, no más comprobaciones.

Según [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md):

El equipo de la plataforma de entregas reduce su definición de terminado de catorce casillas a tres niveles. Para cambios de texto: revisión y prueba de aceptación automática. Para cambios de interfaz: además, comprobación de accesibilidad con una herramienta y una lectora de pantalla. Para cambios en la regla de penalización o en notas: además, comparación contra la función de referencia de `SE-157` y una segunda persona que lee el sentido. Cada casilla tiene una razón registrada (qué escape evitó la última vez) y una fecha de revisión. La definición de listo se reduce a tres preguntas (qué problema resuelve, qué ejemplo lo ilustra, qué dependencia tiene) y se aplica en menos de un día.

## Ejemplo

Ejemplo de [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula los escapes esperados de dos comprobaciones independientes y de dos que ven lo mismo. Antes de ejecutarlo, predice cuál deja pasar menos defectos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La definición de terminado tiene catorce casillas y los escapes no bajan** — causa: comprobaciones correlacionadas. Corrección: medir qué ve cada una y retirar las que ven lo mismo. ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md))
- **Se evalúa la estrategia por escapes** — causa: se ignora el impacto de cada escape. Corrección: medir pérdida y percentil 95. ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md))
- **La velocidad sube y el plazo no cambia** — causa: métrica premiada que se infla. Corrección: retirarla de la vista externa y seguir rendimiento y escapes. ([SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si ven lo mismo (coral, correlación 1,0), el escape se queda en 4 500 aunque haya cuatro: añadir comprobaciones que miran lo mismo no protege. ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Producción](../p/produccion.md), [Puerta](../p/puerta.md), [Trabajo](../t/trabajo.md), [Antigüedad del trabajo en curso](../a/antiguedad-del-trabajo-en-curso.md), [Correlación entre comprobaciones](../c/correlacion-entre-comprobaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-189 — Métricas de flujo, calidad y resultados](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.
- [SE-432 — Proyecto: estrategia ejecutable por riesgo](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (19 clases más lo mencionan; las que más):

[SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md), [SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-282](../../../classes/part-23-runtimes-y-plataformas-modernas/se-282-contenedores-microvm-y-sandboxes/README.md), [SE-570](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-570-skills-plugins-hooks-y-entornos-aislados/README.md), [SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), [SE-116](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-116-generacion-de-codigo-y-metaprogramacion/README.md), [SE-174](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-174-semantica-teclado-foco-y-tecnologias-de-asistencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The Scrum Guide](https://scrumguides.org/scrum-guide.html) — definición de terminado e incremento; autoridad: Scrum.org y Scrum Inc. (autores de la guía).
- [Jones, «Software defect-removal efficiency» (IEEE Computer, 1996)](https://doi.org/10.1109/2.488361) — eficiencia de eliminación de defectos por técnica; autoridad: IEEE Computer.
- [Fagan, «Design and code inspections to reduce errors in program development» (IBM Systems Journal, 1976)](https://doi.org/10.1147/sj.153.0182) — inspecciones formales de diseño y código; autoridad: IBM Systems Journal.
- [North, «Introducing BDD»](https://dannorth.net/introducing-bdd/) — criterios de aceptación como escenarios; autoridad: autor de la práctica.
- [Agile Alliance: definition of done](https://www.agilealliance.org/glossary/definition-of-done/) — glosario de la práctica; autoridad: Agile Alliance.

---

[↑ Glosario](../../README.md) · [← Escáner previo al envío](./escaner-previo-al-envio.md) · [Escape hatch y ownership →](./escape-hatch-y-ownership.md)
