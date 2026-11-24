# Regla de decisión

[↑ Glosario](../../README.md) · [← Regla de confianza](./regla-de-confianza.md) · [Regla de dependencia →](./regla-de-dependencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Una **regla de decisión** es el procedimiento por el cual un proyecto acepta o rechaza una propuesta ([SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md)). [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) usa el término en un sentido emparentado: un criterio escrito que asigna un candidato a una carga (qué elementos van a qué lugar), que hace la elección revisable. En ambos, lo esencial es que la regla esté escrita antes de decidir.

## Por qué importa

Cada regla tolera un tipo de error distinto, y la disponibilidad de las personas decide cuál es adecuada. Si no hay regla, las decisiones dependen de quién tiene más peso o de quién insiste más. Con una regla escrita, quien contribuye sabe qué esperar y la decisión puede revisarse. Cambia cómo se gobierna un proyecto: no solo qué se decide, sino cómo.

## Cómo funciona

[SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) enumera cuatro familias de reglas: un **líder con la última palabra**, **votación por mayoría**, **consenso con veto** y **consenso por falta de objeción en un plazo** (consenso perezoso). Cada una paga con un error diferente. La que acepta por silencio es rápida y deja pasar lo que nadie leyó (acepta propuestas dañinas). La que exige votos mínimos se bloquea si faltan votantes (rechaza propuestas buenas por falta de quórum). El líder único decide rápido y concentra el riesgo en una persona.

La clase representa esto en una figura: cada grupo es una regla de decisión y sus barras muestran el porcentaje de propuestas dañinas aceptadas, de buenas rechazadas y el tiempo de decisión, en una simulación. Lo que enseña es el compromiso entre velocidad y protección, no una regla óptima.

En la plataforma de entregas, la regla escrita en `CONTRIBUTING.md` es graduada: los cambios pequeños los aprueba una mantenedora; los que modifican una regla de negocio exigen dos aprobaciones y un plazo de 72 horas; los cambios de gobierno exigen consenso. La graduación asigna más exigencia donde el error cuesta más. Se acompaña con un indicador mensual de cuántas personas cubren la mitad de los commits, para planificar relevos (factor de camión), y con un tiempo objetivo de primera respuesta a contribuciones externas.

En [SE-287](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), la misma idea se aplica a asignar un candidato a una carga: un criterio escrito (por ejemplo, un umbral o un orden de preferencia) que otra persona puede reaplicar y discutir.

## Ejemplo

Un cambio de texto en la documentación se aprueba con una sola revisora; una modificación de la fórmula de penalización necesita dos aprobaciones y esperar 72 horas, para que quien esté de vacaciones tenga ocasión de objetar. Si nadie objeta en el plazo, procede (consenso perezoso, solo en cambios de bajo riesgo). (Estructura tomada de [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md).)

## Errores y confusiones comunes

- **Contribuciones externas sin respuesta**: no hay tiempo objetivo ni responsable; corrección: fijar un tiempo de primera respuesta y rotar quien lo cumple.
- **Una sola regla para todo**: la misma exigencia para un cambio de texto y para el gobierno.
- **No escribirla**: se improvisa y se percibe arbitraria.
- **Confundir regla de decisión con regla de negocio**: la primera gobierna el proyecto; la segunda, el producto.

## Límites y cuándo no aplica

Una regla escrita no sustituye la confianza ni el liderazgo. En proyectos muy pequeños, con una o dos personas, el formalismo sobra. Las cifras de la simulación son ilustrativas de un modelo, no mediciones de proyectos reales.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Candidato](../c/candidato.md), [Alcance](../a/alcance.md), [Batería hostil](../b/bateria-hostil.md), [Capacidad](../c/capacidad.md), [Código de conducta](../c/codigo-de-conducta.md), [Concentración de conocimiento](../c/concentracion-de-conocimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.
- [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md) — [Parte 23](../../../classes/part-23-runtimes-y-plataformas-modernas/README.md), Runtimes y plataformas modernas.

**También se usa en** (12 clases más lo mencionan; las que más):

[SE-124](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-124-hipotesis-supuestos-y-preguntas-criticas/README.md), [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md), [SE-024](../../../classes/part-01-computadores-y-representacion-de-informacion/se-024-proyecto-informe-reproducible-de-comportamiento-y-recursos/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-603](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-603-experimentos-y-entrenamiento-reproducible/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Reglas de decisión».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Source Guides: liderazgo y gobernanza](https://opensource.guide/leadership-and-governance/) — estructuras de gobierno habituales; autoridad: Open Source Guides.
- [Apache: proceso de votación](https://www.apache.org/foundation/voting.html) — tipos de voto, consenso y periodos mínimos; autoridad: Apache Software Foundation.
- [PEP 13: modelo de gobierno de Python](https://peps.python.org/pep-0013/) — transición de un líder benevolente a un consejo; autoridad: Python Software Foundation.
- [Contributor Covenant](https://www.contributor-covenant.org/) — código de conducta para comunidades digitales; autoridad: Contributor Covenant.
- [GitHub: sincronizar un fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) — actualizar una copia con el original; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Regla de confianza](./regla-de-confianza.md) · [Regla de dependencia →](./regla-de-dependencia.md)
