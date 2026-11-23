# Correlación entre comprobaciones

[↑ Glosario](../../README.md) · [← Correlación](./correlacion.md) · [Corrida →](./corrida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Grado en que dos comprobaciones fallan o aciertan sobre los mismos defectos.

Definición de trabajo de [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md).

## Por qué importa

En [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), el tema «Correlación entre comprobaciones» importa porque añadir una comprobación que ve lo mismo que otra casi no reduce los escapes.

## Cómo funciona

Según [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md), en la sección «Correlación entre comprobaciones»:

Si cada comprobación detectara defectos al azar con su propia probabilidad, añadir otra siempre reduciría los escapes de forma multiplicativa. Pero las comprobaciones miran cosas parecidas: los defectos «fáciles» los ve cualquiera y los «difíciles» se escapan a todas. Esa correlación hace que la segunda y la tercera comprobación aporten mucho menos de lo esperado, y que a partir de cierto punto no aporten nada. Jones observó que ninguna técnica los elimina todos y que las combinaciones de técnicas distintas rinden más que repetir la misma. La consecuencia de diseño es elegir comprobaciones que vean defectos distintos, no más comprobaciones.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md):

El equipo de la plataforma de entregas reduce su definición de terminado de catorce casillas a tres niveles. Para cambios de texto: revisión y prueba de aceptación automática. Para cambios de interfaz: además, comprobación de accesibilidad con una herramienta y una lectora de pantalla. Para cambios en la regla de penalización o en notas: además, comparación contra la función de referencia de `SE-157` y una segunda persona que lee el sentido. Cada casilla tiene una razón registrada (qué escape evitó la última vez) y una fecha de revisión.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)) son:

- **La definición de terminado tiene catorce casillas y los escapes no bajan** — causa: comprobaciones correlacionadas. Corrección: medir qué ve cada una y retirar las que ven lo mismo.
- **Las historias esperan dos semanas para estar «listas»** — causa: definición de listo demasiado exigente. Corrección: reducir a las preguntas que evitan los rehacer y medir el plazo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna definición de terminado de un equipo ni se revisaron criterios reales: la dificultad de los defectos, la ambigüedad que decae con el refinamiento y los dieciséis criterios del verificador son construcciones del autor. La siguiente clase mide el flujo, la calidad y los resultados que producen esas puertas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Criterio de aceptación](./criterio-de-aceptacion.md), [Definición de listo](../d/definicion-de-listo.md), [Definición de terminado](../d/definicion-de-terminado.md), [Escape](../e/escape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

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

[↑ Glosario](../../README.md) · [← Correlación](./correlacion.md) · [Corrida →](./corrida.md)
