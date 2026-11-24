# Definición de terminado

[↑ Glosario](../../README.md) · [← Definición de paso](./definicion-de-paso.md) · [Degradación →](./degradacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **definición de terminado** (*Definition of Done*) es el conjunto de comprobaciones que un incremento debe pasar para considerarse utilizable y liberable: pruebas, revisión, análisis, documentación mínima y criterios de aceptación. Es el sentido de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md). Es una promesa compartida de calidad y, según la clase, la guía de Scrum la hace obligatoria.

## Por qué importa

Cambia qué quiere decir «hecho» en una conversación. Sin una definición compartida, cada persona termina en un punto distinto y la deuda aparece al final. [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) fija el corolario: un incremento que no la cumple no está parcialmente terminado, no lo está. Sirve también para no confundir terminado con aceptado: lo primero es calidad técnica; lo segundo, el reconocimiento de que resuelve el problema.

## Cómo funciona

La definición es una lista de comprobaciones aplicable a todo incremento. Para que funcione tiene que mantenerse viva: se revisa con los defectos que se escaparon y se calibra por tipo de trabajo, porque un cambio de texto y un cambio de la regla de penalización no necesitan las mismas barreras.

El defecto típico es la lista que crece: catorce casillas con comprobaciones correlacionadas, que ven lo mismo y no reducen los escapes. La corrección de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) es medir qué ve cada casilla y retirar las que ven lo mismo; cada casilla debe tener una razón registrada, el escape concreto que evitó. Si tras añadir dos casillas los escapes del trimestre no bajan, el síntoma es que las nuevas son redundantes.

## Ejemplo

El equipo de la plataforma de entregas reduce su definición de catorce casillas a tres niveles. Cambios de texto: revisión y prueba de aceptación automática. Cambios de interfaz: además, comprobación de accesibilidad con una herramienta y una lectora de pantalla. Cambios en la regla de penalización o en notas: además, comparación contra la función de referencia de [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) y una segunda persona que lee el sentido. Cada casilla lleva la razón que la justifica.

## Errores y confusiones comunes

- **Catorce casillas y los escapes no bajan.** Comprobaciones correlacionadas; medir qué ve cada una y retirar las redundantes.
- **Una lista única para todo.** Frena lo trivial y no basta para lo crítico.
- **Confundirla con los criterios de aceptación.** Esos son por historia; la definición es común a todas.
- **Terminado a medias.** No existe: o cumple la definición o no.

## Límites y cuándo no aplica

La definición garantiza que se hicieron ciertas comprobaciones, no que el incremento sea el correcto: puede estar terminado y no ser aceptado. No sustituye a la definición de «listo» (*Ready*), que regula la entrada del trabajo, ni a la aceptación por quien lo pidió. Una definición demasiado ambiciosa para el contexto se incumple por sistema y deja de ser promesa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Correlación entre comprobaciones](../c/correlacion-entre-comprobaciones.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Definición de listo](./definicion-de-listo.md), [Escape](../e/escape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-188 — Definition of Ready, Done y aceptación](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) — [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md), Procesos, planificación y estimación.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-003](../../../classes/part-00-ingenieria-de-software-como-profesion/se-003-ciclo-de-vida-completo-y-responsabilidades-profesionales/README.md).

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

[↑ Glosario](../../README.md) · [← Definición de paso](./definicion-de-paso.md) · [Degradación →](./degradacion.md)
