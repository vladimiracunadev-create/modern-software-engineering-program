# Instrucciones en conflicto

[↑ Glosario](../../README.md) · [← Instrucción](./instruccion.md) · [Instrumento →](./instrumento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Pares de reglas del encargo cuyo cumplimiento simultáneo es imposible.

Definición de trabajo de [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md).

## Por qué importa

En [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md), el tema «Instrucciones en conflicto» importa porque evita que el modelo elija arbitrariamente entre reglas contradictorias

## Cómo funciona

[SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo reescribe el encargo para «calcular la nota final» con los seis componentes. Objetivo: función `nota_final(trabajos, examen)` que devuelve nota y estado. Contexto: módulo de calificaciones, Python 3.12, sin dependencias. Restricciones: no modificar otras funciones; lanzar `ValueError` ante lista vacía de trabajos. Formato: un parche unificado más un archivo de pruebas. Ejemplos: cinco casos, entre ellos la frontera 4,0 y un promedio con medio punto de redondeo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El asistente alterna entre dos estilos** — causa: instrucciones en conflicto. Corrección: detectar pares y reescribir con una precedencia. ([SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de requisitos con semilla fija, un validador real aplicado a salidas sintéticas y un cálculo exacto de conflictos. No se llamó a ningún modelo real; las probabilidades de cumplimiento, los seis tipos de defecto, su reparto uniforme y la tasa de conflicto son construcciones del autor, y el validador se escribió sabiendo qué defectos se inyectaban.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Encargo](../e/encargo.md), [Regla](../r/regla.md), [Contrato de salida](../c/contrato-de-salida.md), [Criterio de aceptación](../c/criterio-de-aceptacion.md), [Validación por capas](../v/validacion-por-capas.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-554 — Prompting, instrucciones y criterios de salida](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Anthropic: prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — claridad, ejemplos y criterios de éxito antes de iterar; autoridad: documentación de Anthropic.
- [JSON Schema](https://json-schema.org/specification) — validación de la estructura de documentos JSON; autoridad: especificación del proyecto JSON Schema.
- [Wallace et al., «The Instruction Hierarchy»](https://arxiv.org/abs/2404.13208) — jerarquía de instrucciones por nivel de privilegio; autoridad: preprint de OpenAI.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — evaluación de código por pruebas; autoridad: preprint de OpenAI.
- [Python: json](https://docs.python.org/3/library/json.html) — análisis de JSON; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Instrucción](./instruccion.md) · [Instrumento →](./instrumento.md)
