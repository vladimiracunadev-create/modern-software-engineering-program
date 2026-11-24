# Escape

[↑ Glosario](../../README.md) · [← Escáner previo al envío](./escaner-previo-al-envio.md) · [Escape hatch y ownership →](./escape-hatch-y-ownership.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

Un **escape** es un defecto que supera las puertas del proceso y se descubre después de dar el trabajo por terminado. Es el sentido de [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) (defecto descubierto tras dar un incremento por terminado) y de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md). En [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) el matiz es el más grave: un defecto que llega a producción sin ser detectado. No es lo mismo que un defecto encontrado durante el desarrollo: lo que define al escape es que el proceso lo dejó pasar.

## Por qué importa

Cambia qué se mide para saber si el proceso de calidad funciona. Cuántos defectos se encuentran no dice nada sobre cuántos se escapan; los escapes sí miden lo que las comprobaciones no vieron. Por eso la definición de terminado se revisa con los escapes del periodo ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)), y las estrategias de prueba por riesgo se evalúan por la pérdida que causan, no solo por su número ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)).

## Cómo funciona

Si cada comprobación detectara defectos al azar y de forma independiente, añadir otra reduciría los escapes de forma multiplicativa. [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) muestra que no es así: las comprobaciones miran cosas parecidas, los defectos «fáciles» los ve cualquiera y los «difíciles» se escapan a todas. Esa **correlación** hace que la segunda y la tercera comprobación aporten mucho menos de lo esperado y, a partir de cierto punto, nada. En el ejemplo de la clase, cuando las comprobaciones ven exactamente lo mismo (correlación 1,0) los escapes se quedan en 4 500 aunque haya cuatro. Añadir comprobaciones que miran lo mismo no protege.

La consecuencia práctica es medir qué ve cada comprobación, retirar las redundantes y añadir las que ven algo distinto. [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md) añade una precisión sobre cómo evaluar: contar escapes ignora su impacto; hay que medir pérdida y percentil 95. Y [SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md) advierte contra premiar una métrica que se infla, como la velocidad, mientras el plazo no cambia: se sigue el rendimiento y los escapes.

## Ejemplo

El equipo de la plataforma de entregas reduce su definición de terminado de catorce casillas a tres niveles, cada casilla con la razón registrada, es decir, qué escape evitó. El fragmento de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) calcula los escapes esperados de dos comprobaciones independientes y de dos que ven lo mismo, y pide predecir cuál deja pasar menos defectos antes de ejecutarlo.

## Errores y confusiones comunes

- **Más casillas y los escapes no bajan.** Comprobaciones correlacionadas; medir qué ve cada una.
- **Evaluar la estrategia solo por número de escapes.** Ignora el impacto; medir pérdida y percentil 95 ([SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md)).
- **Premiar una métrica que se infla.** La velocidad sube y el plazo no cambia ([SE-189](../../../classes/part-15-procesos-planificacion-y-estimacion/se-189-metricas-de-flujo-calidad-y-resultados/README.md)).
- **Confundir escape con defecto encontrado tarde en desarrollo.** El escape cruza la puerta de «terminado».

## Límites y cuándo no aplica

El escape solo se cuenta cuando se descubre: los que aún no se han visto no aparecen, de modo que la cifra es un mínimo. Las cifras de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) son de un modelo con parámetros elegidos por la clase. Y reducir escapes tiene un costo; el nivel de comprobación debe ajustarse al riesgo del tipo de cambio.

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
