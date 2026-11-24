# Definición de listo

[↑ Glosario](../../README.md) · [← Defensa por profundidad](./defensa-por-profundidad.md) · [Definición de paso →](./definicion-de-paso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 15](../../../classes/part-15-procesos-planificacion-y-estimacion/README.md)

## Definición

La **definición de listo** (*Definition of Ready*) es el acuerdo sobre la información que un elemento de trabajo debe tener antes de comenzar a construirse ([SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md)). Es la puerta de entrada del trabajo, como la definición de terminado es la de salida.

## Por qué importa

Reduce el riesgo de empezar sin entender, a cambio de retrasar el inicio. Un equipo que sufrió historias empezadas con información incompleta (y luego rehechas) acuerda qué debe saberse de antemano. [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) aclara que **no es un requisito de la guía de Scrum**: es una práctica de equipos que aprendieron por la vía difícil. Cambia el momento de aclarar dudas: antes de construir y no a mitad.

## Cómo funciona

El acuerdo lista qué debe saberse de un elemento: **qué problema resuelve, para quién, qué ejemplos lo describen y qué dependencias tiene**. En el equipo de la plataforma se reduce a tres preguntas: qué problema resuelve, qué ejemplo lo ilustra y qué dependencia tiene.

La definición tiene un costo y un beneficio que se oponen. El costo: el **tiempo de espera y de preparación** (las historias esperan hasta estar «listas»). El beneficio: **menos historias se rehacen**. Si la definición es demasiado exigente, las historias esperan semanas y el flujo se detiene; si es demasiado laxa, se empieza sin entender. El mínimo útil está en el punto donde cada pregunta evita más rehacer de lo que cuesta responderla, y se calibra midiendo el plazo de espera y la tasa de rehacer.

El síntoma que [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md) describe de una definición excesiva: las historias esperan dos semanas para estar «listas». La corrección es reducirla a las preguntas que evitan los rehacer y medir el plazo. Y se vincula con los criterios de aceptación: un elemento listo trae los ejemplos con los que se aceptará.

## Ejemplo

Una historia «mostrar el descuento por entrega tardía al estudiante» entra al trabajo cuando se responde: qué problema resuelve (las estudiantes no entienden su nota), qué ejemplo la ilustra (una entrega con 30 horas de retraso muestra un 10 % de descuento y el porqué) y qué dependencia tiene (la función de cálculo ya existe). Si la historia llega sin ejemplo, se pide antes de empezar. (Ilustración del enfoque de tres preguntas de [SE-188](../../../classes/part-15-procesos-planificacion-y-estimacion/se-188-definition-of-ready-done-y-aceptacion/README.md).)

## Errores y confusiones comunes

- **Historias que esperan dos semanas para estar «listas»**: definición demasiado exigente.
- **Tratarla como contrato** en lugar de acuerdo del equipo.
- **Confundirla con la definición de terminado**: una es de entrada; la otra, de salida.
- **No revisarla**: debe ajustarse con los rehacer reales.

## Límites y cuándo no aplica

En trabajo exploratorio, una definición de listo estricta frena el aprendizaje, que justamente ocurre al construir. En equipos con comunicación continua con quien pide el trabajo, el coste de aclarar sobre la marcha puede ser menor. No sustituye a los criterios de aceptación ni a la definición de terminado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Sobre](../s/sobre.md), [Correlación entre comprobaciones](../c/correlacion-entre-comprobaciones.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Definición de terminado](./definicion-de-terminado.md), [Escape](../e/escape.md).
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

[↑ Glosario](../../README.md) · [← Defensa por profundidad](./defensa-por-profundidad.md) · [Definición de paso →](./definicion-de-paso.md)
