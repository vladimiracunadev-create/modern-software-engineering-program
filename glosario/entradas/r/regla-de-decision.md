# Regla de decisión

[↑ Glosario](../../README.md) · [← Regla de confianza](./regla-de-confianza.md) · [Regla de dependencia →](./regla-de-dependencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Procedimiento por el que un proyecto acepta o rechaza una propuesta.

Definición de trabajo de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md): Criterio escrito que asigna un candidato a una carga.

## Por qué importa

En [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), el tema «Reglas de decisión» importa porque cada regla tolera un tipo de error distinto y depende de quién está disponible.

En [SE-287 — Taller: elegir y aislar un runtime para una carga no confiable](../../../classes/part-23-runtimes-y-plataformas-modernas/se-287-taller-elegir-y-aislar-un-runtime-para-una-carga-no-confiable/README.md), el tema «Regla de decisión» importa porque hace la elección revisable.

## Cómo funciona

Según [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), en la sección «Reglas de decisión»:

Un proyecto decide cómo acepta cambios o propuestas: un líder con la última palabra, votación por mayoría, aprobación por consenso con veto, o consenso por falta de objeción en un plazo (consenso perezoso). Cada regla tolera errores distintos: la que acepta por silencio es rápida y deja pasar lo que nadie leyó; la que exige votos mínimos se bloquea si faltan votantes. La disponibilidad de las personas decide cuál es adecuada.

## Ejemplo

Ejemplo de [SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) (sección «Ejemplo profesional»):

La plataforma publica `CONTRIBUTING.md` con el entorno, el formato de ramas, la plantilla de PR, el tiempo objetivo de primera respuesta y lo que no se acepta. Una regla de decisión escrita: los cambios pequeños los aprueba una mantenedora; los que modifican una regla de negocio exigen dos aprobaciones y un plazo de 72 horas; los cambios de gobierno exigen consenso. Un indicador mensual muestra cuántas personas cubren la mitad de los commits y qué rutas solo conoce una, para planificar relevos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-200 — Contribución, gobernanza y comunidades abiertas](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md)) son:

- **Las contribuciones externas se quedan sin respuesta** — causa: no hay tiempo objetivo ni responsable. Corrección: fijar un tiempo de primera respuesta y rotar quien lo cumple.
- **Los PR externos chocan al revisarse** — causa: la copia se quedó atrás. Corrección: pedir sincronización y ofrecer una guía para hacerla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada grupo es una regla de decisión y sus tres barras son el porcentaje de propuestas dañinas aceptadas (coral), buenas rechazadas (dorado) y sin decisión (gris). ([SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md))

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
