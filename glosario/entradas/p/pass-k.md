# Pass@k

[↑ Glosario](../../README.md) · [← Paso fijo](./paso-fijo.md) · [Pass@k y pass^k →](./pass-k-y-pass-k.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Probabilidad de que al menos una de k muestras pase las pruebas.

Definición de trabajo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

## Por qué importa

La clase donde se define, [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), existe con este propósito: la clase existe para que dejes de tratar a un modelo generativo como un oráculo o como un compañero con criterio, y lo trates como lo que es: un generador de texto que produce continuaciones plausibles a partir de una distribución de probabilidad, con habilidades útiles y con modos de fallo que no avisan.

## Cómo funciona

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

El criterio práctico más útil para decidir qué delegar es la verificabilidad. Una tarea cuyo resultado se comprueba de forma mecánica y barata (una función con pruebas, una transformación con un oráculo, un código que compila y pasa un analizador) tolera mucha variación en la generación porque el comprobador filtra: Chen y sus coautores evalúan el código generado precisamente ejecutando pruebas, y su métrica pass@k mide la probabilidad de que al menos una de k muestras pase. Una tarea comprobable solo con criterio humano (una decisión de diseño, un texto para estudiantes) exige que alguien lea con atención y asume el costo de esa lectura.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica diez tareas que quiere hacer con el asistente según la verificabilidad. «Generar una función que convierta notas con coma a número» es comprobable mecánicamente: se escriben cinco casos con la especificación y se acepta si pasan. «Explicar la regla de redondeo del módulo» es comprobable contra el código, pero solo si el código está en el contexto; se decide aportar la función y exigir que la explicación cite líneas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son:

- **Se acepta una respuesta porque «suena segura»** — causa: se confunde tono con calibración. Corrección: medir acierto por tramos con tareas del propio equipo.
- **Se vota entre varias respuestas y se confirma un error** — causa: los errores están correlacionados. Corrección: añadir un comprobador externo (prueba, fuente).

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con procesos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se llamó a ningún modelo real, no se evaluó ninguna herramienta comercial ni se observó ningún equipo; los logits, las distribuciones de confianza, la proporción de preguntas difíciles y los tamaños de archivo son construcciones del autor, y los «modelos» fueron escritos sabiendo qué fenómeno ilustran.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Calibración](../c/calibracion.md), [Confabulación](../c/confabulacion.md), [Modelo generativo](../m/modelo-generativo.md), [Modo de fallo](../m/modo-de-fallo.md), [Temperatura](../t/temperatura.md), [Ventana de contexto](../v/ventana-de-contexto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-549](../../../classes/part-45-metodologias-de-desarrollo-de-tdd-a-odd/se-549-edd-evaluaciones-como-especificacion-y-puerta-de-release/README.md), [SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación de código con pruebas; autoridad: preprint de OpenAI.
- [Holtzman et al., «The Curious Case of Neural Text Degeneration»](https://arxiv.org/abs/1904.09751) — generación como muestreo y degeneración al elegir lo más probable; autoridad: ICLR 2020.
- [Wang et al., «Self-Consistency Improves Chain of Thought Reasoning»](https://arxiv.org/abs/2203.11171) — votar entre muestras de razonamiento; autoridad: ICLR 2023.
- [Guo et al., «On Calibration of Modern Neural Networks»](https://arxiv.org/abs/1706.04599) — calibración y error de calibración esperado; autoridad: ICML 2017.
- [Liu et al., «Lost in the Middle»](https://arxiv.org/abs/2307.03172) — uso de la información según su posición en el contexto; autoridad: Transactions of the ACL.

---

[↑ Glosario](../../README.md) · [← Paso fijo](./paso-fijo.md) · [Pass@k y pass^k →](./pass-k-y-pass-k.md)
