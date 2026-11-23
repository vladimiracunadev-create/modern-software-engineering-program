# Confabulación

[↑ Glosario](../../README.md) · [← Condición de salida](./condicion-de-salida.md) · [Confianza →](./confianza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Producción de contenido falso expresado con seguridad, sin señal de que lo sea.

Definición de trabajo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Por qué importa

En [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), el tema «Modos de fallo» importa porque permite anticipar la confabulación, la omisión silenciosa y la inconsistencia

## Cómo funciona

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

El conocimiento de un modelo tiene tres fuentes distintas que conviene no confundir. Lo que aprendió durante el entrenamiento está comprimido, es general y tiene una fecha de corte: sabe cómo se escribe una consulta SQL, no sabe cómo redondea *tu* módulo. Lo que le aportas en el contexto (archivos, documentos, resultados de herramientas) lo puede usar de forma casi literal, pero solo mientras esté dentro de la ventana. Y hay lo que no está en ninguna de las dos: las reglas no escritas del módulo, las decisiones del equipo, el estado actual de la base de datos. Ante esto último el modelo no se detiene: produce una respuesta plausible porque su mecanismo es producir texto, no abstenerse.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica diez tareas que quiere hacer con el asistente según la verificabilidad. «Generar una función que convierta notas con coma a número» es comprobable mecánicamente: se escriben cinco casos con la especificación y se acepta si pasan. «Explicar la regla de redondeo del módulo» es comprobable contra el código, pero solo si el código está en el contexto; se decide aportar la función y exigir que la explicación cite líneas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son:

- **Se acepta una respuesta porque «suena segura»** — causa: se confunde tono con calibración. Corrección: medir acierto por tramos con tareas del propio equipo.
- **Se vota entre varias respuestas y se confirma un error** — causa: los errores están correlacionados. Corrección: añadir un comprobador externo (prueba, fuente).

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El NIST llama a este fenómeno confabulación y lo cuenta entre los riesgos propios de la IA generativa. ([SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producción](../p/produccion.md), [Seguridad](../s/seguridad.md), [Señal](../s/senal.md), [Calibración](./calibracion.md), [Modelo generativo](../m/modelo-generativo.md), [Modo de fallo](../m/modo-de-fallo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST AI 600-1: Generative AI Profile](https://doi.org/10.6028/NIST.AI.600-1) — riesgos de la IA generativa, entre ellos la confabulación; autoridad: NIST.
- [Holtzman et al., «The Curious Case of Neural Text Degeneration»](https://arxiv.org/abs/1904.09751) — generación como muestreo y degeneración al elegir lo más probable; autoridad: ICLR 2020.
- [Wang et al., «Self-Consistency Improves Chain of Thought Reasoning»](https://arxiv.org/abs/2203.11171) — votar entre muestras de razonamiento; autoridad: ICLR 2023.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación de código con pruebas; autoridad: preprint de OpenAI.
- [Guo et al., «On Calibration of Modern Neural Networks»](https://arxiv.org/abs/1706.04599) — calibración y error de calibración esperado; autoridad: ICML 2017.

---

[↑ Glosario](../../README.md) · [← Condición de salida](./condicion-de-salida.md) · [Confianza →](./confianza.md)
