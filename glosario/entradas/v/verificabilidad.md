# Verificabilidad

[↑ Glosario](../../README.md) · [← Veredicto de corrección](./veredicto-de-correccion.md) · [Verificación →](./verificacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md)

## Definición

Existencia de un procedimiento finito, ejecutable por otra persona, que produce un veredicto aceptado de cumple o no cumple.

Definición de trabajo de [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md).

## Por qué importa

En [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), el tema «Verificabilidad» importa porque determina cuánto puede delegarse: lo comprobable mecánicamente se delega mejor

## Cómo funciona

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

El criterio práctico más útil para decidir qué delegar es la verificabilidad. Una tarea cuyo resultado se comprueba de forma mecánica y barata (una función con pruebas, una transformación con un oráculo, un código que compila y pasa un analizador) tolera mucha variación en la generación porque el comprobador filtra: Chen y sus coautores evalúan el código generado precisamente ejecutando pruebas, y su métrica pass@k mide la probabilidad de que al menos una de k muestras pase. Una tarea comprobable solo con criterio humano (una decisión de diseño, un texto para estudiantes) exige que alguien lea con atención y asume el costo de esa lectura.

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica diez tareas que quiere hacer con el asistente según la verificabilidad. «Generar una función que convierta notas con coma a número» es comprobable mecánicamente: se escriben cinco casos con la especificación y se acepta si pasan. «Explicar la regla de redondeo del módulo» es comprobable contra el código, pero solo si el código está en el contexto; se decide aportar la función y exigir que la explicación cite líneas. «Decidir si la nota 3,95 aprueba» no es una pregunta para el asistente: la fuente es el reglamento, y se resuelve consultándolo.

## Ejemplo

Ejemplo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica diez tareas que quiere hacer con el asistente según la verificabilidad. «Generar una función que convierta notas con coma a número» es comprobable mecánicamente: se escriben cinco casos con la especificación y se acepta si pasan. «Explicar la regla de redondeo del módulo» es comprobable contra el código, pero solo si el código está en el contexto; se decide aportar la función y exigir que la explicación cite líneas. «Decidir si la nota 3,95 aprueba» no es una pregunta para el asistente: la fuente es el reglamento, y se resuelve consultándolo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se usa el mismo nivel de confianza para toda tarea** — causa: no se clasificó por verificabilidad. Corrección: clasificar las tareas y fijar la comprobación de cada clase. ([SE-553](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con procesos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se llamó a ningún modelo real, no se evaluó ninguna herramienta comercial ni se observó ningún equipo; los logits, las distribuciones de confianza, la proporción de preguntas difíciles y los tamaños de archivo son construcciones del autor, y los «modelos» fueron escritos sabiendo qué fenómeno ilustran.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-154](../../../classes/part-12-ingenieria-de-requisitos/se-154-ambiguedad-contradiccion-e-incompletitud/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calibración](../c/calibracion.md), [Confabulación](../c/confabulacion.md), [Modelo generativo](../m/modelo-generativo.md), [Modo de fallo](../m/modo-de-fallo.md), [Pass@k](../p/pass-k.md), [Patrones de reparación](../p/patrones-de-reparacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-155 — Taller: reparar requisitos no verificables](../../../classes/part-12-ingenieria-de-requisitos/se-155-taller-reparar-requisitos-no-verificables/README.md) — [Parte 12](../../../classes/part-12-ingenieria-de-requisitos/README.md), Ingeniería de requisitos.
- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-554](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-554-prompting-instrucciones-y-criterios-de-salida/README.md), [SE-574](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-574-seguridad-agentic-prompt-injection-y-auditoria/README.md), [SE-594](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-594-embeddings-recuperacion-y-agentic-rag/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Holtzman et al., «The Curious Case of Neural Text Degeneration»](https://arxiv.org/abs/1904.09751) — generación como muestreo y degeneración al elegir lo más probable; autoridad: ICLR 2020.
- [Wang et al., «Self-Consistency Improves Chain of Thought Reasoning»](https://arxiv.org/abs/2203.11171) — votar entre muestras de razonamiento; autoridad: ICLR 2023.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación de código con pruebas; autoridad: preprint de OpenAI.
- [Guo et al., «On Calibration of Modern Neural Networks»](https://arxiv.org/abs/1706.04599) — calibración y error de calibración esperado; autoridad: ICML 2017.
- [Liu et al., «Lost in the Middle»](https://arxiv.org/abs/2307.03172) — uso de la información según su posición en el contexto; autoridad: Transactions of the ACL.

---

[↑ Glosario](../../README.md) · [← Veredicto de corrección](./veredicto-de-correccion.md) · [Verificación →](./verificacion.md)
