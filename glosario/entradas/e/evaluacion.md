# Evaluación

[↑ Glosario](../../README.md) · [← Evacuación de una región](./evacuacion-de-una-region.md) · [Evaluación de idea →](./evaluacion-de-idea.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md)

## Definición

Conjunto de casos con un criterio que mide la calidad de un componente.

Definición de trabajo de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md): Conjunto de tareas con criterio de éxito ejecutable y procedimiento reproducible para medir un sistema.
- En [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md): Conjunto de casos con un criterio de calificación que mide un sistema.

## Por qué importa

En [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), el tema «Evaluación frente a prueba determinista» importa porque la primera mide una proporción con ruido; la segunda, un hecho.

## Cómo funciona

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

Una evaluación bien hecha tiene tres partes: un conjunto de **casos** (entradas representativas, incluidas las difíciles), un **criterio** que decide si una salida es aceptable (una aserción de código, una rúbrica aplicada por una persona o por un modelo evaluador) y una **regla de decisión** (umbral y margen). Juntas funcionan como especificación: dicen qué se espera, con ejemplos, sin exigir una salida única. Husain las ordena por costo: primero pruebas de comportamiento que se pueden comprobar con código, luego revisión humana y de modelos sobre trazas registradas, por último experimentos A/B en producción. La base barata es la más frecuente, y cada nivel se justifica por lo que el anterior no ve.

Según [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md):

El equipo diseña la puerta del asistente de redacción. Parte de treinta casos curados: veinte que han fallado antes o que el negocio considera críticos (avisos para una entrega con una hora de adelanto, textos en un tono que no alarma) y diez de un registro de producción. Mide la línea base ocho veces y obtiene una media de 0,86 y una desviación de 0,03. Fija el umbral en 0,80 (dos desviaciones por debajo) y una zona de duda entre 0,80 y 0,83 en la que se repite la evaluación con cinco corridas por caso. Añade una regla: cada fallo real en producción se convierte en un caso nuevo en menos de una semana.

## Ejemplo

Ejemplo de [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) (sección «Ejemplo profesional»):

El equipo diseña la puerta del asistente de redacción. Parte de treinta casos curados: veinte que han fallado antes o que el negocio considera críticos (avisos para una entrega con una hora de adelanto, textos en un tono que no alarma) y diez de un registro de producción. Mide la línea base ocho veces y obtiene una media de 0,86 y una desviación de 0,03. Fija el umbral en 0,80 (dos desviaciones por debajo) y una zona de duda entre 0,80 y 0,83 en la que se repite la evaluación con cinco corridas por caso.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El resultado público no se reproduce en tu equipo** — causa: distribución de tareas distinta o contaminación. Corrección: eval propia con tareas reales y reservadas. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una eval tiene cuatro piezas: un conjunto de tareas, un criterio de éxito aplicable sin intervención humana (o con una intervención medida), un procedimiento reproducible para correrla y una forma de resumir el resultado con su incertidumbre. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))
- La documentación de Anthropic sobre evaluaciones de agentes distingue justo esos tres tipos de calificador y subraya que el comportamiento no determinista exige repetir. ([SE-597](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-548](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-548-sdd-spec-first-spec-anchored-y-spec-as-source/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Criterio de éxito](../c/criterio-de-exito.md), [Componente](../c/componente.md), [Conjunto](../c/conjunto.md), [Tarea](../t/tarea.md), [Conjunto curado](../c/conjunto-curado.md), [Costo por solución aceptada](../c/costo-por-solucion-aceptada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-549 — EDD: evaluaciones como especificación y puerta de release](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md) — [Parte 45](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/README.md), Metodologías de desarrollo: de TDD a ODD.
- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-597 — Evals y LLMOps de sistemas con LLM](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-597-evals-y-llmops-de-sistemas-con-llm/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (609 clases más lo mencionan; las que más):

[SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-604](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-604-evaluacion-sesgos-y-validacion-de-modelos/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-610](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-610-gobierno-de-ia-y-regulacion-eu-ai-act-iso-42001-y-nist-ai-rmf/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [TSB Bank](../../../casos/fallo/tsb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «eval».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación por pruebas; autoridad: preprint de OpenAI.
- [Jimenez et al., «SWE-bench»](https://arxiv.org/abs/2310.06770) — evaluación con problemas reales de repositorios; autoridad: ICLR 2024.
- [Jacovi et al., «Stop Uploading Test Data in Plain Text»](https://arxiv.org/abs/2305.10160) — contaminación de conjuntos de evaluación; autoridad: EMNLP 2023.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de confianza para una proporción; autoridad: Journal of the American Statistical Association.
- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.

---

[↑ Glosario](../../README.md) · [← Evacuación de una región](./evacuacion-de-una-region.md) · [Evaluación de idea →](./evaluacion-de-idea.md)
