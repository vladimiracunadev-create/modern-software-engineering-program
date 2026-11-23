# Ventana de contexto

[↑ Glosario](../../README.md) · [← Ventana](./ventana.md) · [Ventana de deduplicación →](./ventana-de-deduplicacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Cantidad máxima de tokens que el modelo considera en una misma interacción.

Definición de trabajo de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md): Conjunto de fichas que el modelo ve en una decisión.

## Por qué importa

La clase donde se define, [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md), existe con este propósito: la clase existe para que dejes de tratar a un modelo generativo como un oráculo o como un compañero con criterio, y lo trates como lo que es: un generador de texto que produce continuaciones plausibles a partir de una distribución de probabilidad, con habilidades útiles y con modos de fallo que no avisan.

## Cómo funciona

Según [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

La **ventana de contexto** es el máximo de símbolos (tokens) que el modelo puede considerar a la vez, entre instrucciones, archivos, historial y respuesta. Una ventana grande no elimina el problema: un repositorio real suele superarla por órdenes de magnitud, el costo y la latencia crecen con el contexto, y la evidencia de Liu y sus coautores indica que la información relevante situada en medio de un contexto largo se usa peor que la del principio o el final. Hay dos decisiones de ingeniería escondidas. Qué archivos entran (por una herramienta de recuperación, por una selección manual, por una convención del asistente), y en qué orden y con qué marcas.

Según [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md):

La ventana de contexto contiene, en cada paso, las instrucciones, las definiciones de las herramientas, el historial de mensajes y las observaciones acumuladas. Todo ocupa fichas y compite por atención. Anthropic define la ingeniería de contexto como la curaduría de ese conjunto de fichas en cada decisión de qué incluir. Una salida de herramienta de cien líneas de registro ocupa lo mismo que cien líneas de decisiones, y es mucho menos valiosa. El primer control es el más sencillo: que las herramientas devuelvan lo necesario y no más, y que el harness recorte salidas largas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones clasifica diez tareas que quiere hacer con el asistente según la verificabilidad. «Generar una función que convierta notas con coma a número» es comprobable mecánicamente: se escriben cinco casos con la especificación y se acepta si pasan. «Explicar la regla de redondeo del módulo» es comprobable contra el código, pero solo si el código está en el contexto; se decide aportar la función y exigir que la explicación cite líneas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son:

- **Se acepta una respuesta porque «suena segura»** — causa: se confunde tono con calibración. Corrección: medir acierto por tramos con tareas del propio equipo.
- **Se vota entre varias respuestas y se confirma un error** — causa: los errores están correlacionados. Corrección: añadir un comprobador externo (prueba, fuente).

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con procesos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se llamó a ningún modelo real, no se evaluó ninguna herramienta comercial ni se observó ningún equipo; los logits, las distribuciones de confianza, la proporción de preguntas difíciles y los tamaños de archivo son construcciones del autor, y los «modelos» fueron escritos sabiendo qué fenómeno ilustran.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-540](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-540-proyecto-dossier-profesional-defendible/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Modelo](../m/modelo.md), [Token](../t/token.md), [Archivo de relevo](../a/archivo-de-relevo.md), [Calibración](../c/calibracion.md), [Compactación](../c/compactacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-553 — Capacidades y límites de los modelos generativos](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-553-capacidades-y-limites-de-los-modelos-generativos/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.
- [SE-580 — Gestión de contexto, resets y handoffs](../../../classes/part-48-harness-y-agentic-engineering/se-580-gestion-de-contexto-resets-y-handoffs/README.md) — [Parte 48](../../../classes/part-48-harness-y-agentic-engineering/README.md), Harness y agentic engineering.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-018](../../../classes/part-01-computadores-y-representacion-de-informacion/se-018-memoria-caches-almacenamiento-y-jerarquias/README.md), [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), [SE-593](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-593-memoria-y-gestion-de-estado-de-agentes/README.md).

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

[↑ Glosario](../../README.md) · [← Ventana](./ventana.md) · [Ventana de deduplicación →](./ventana-de-deduplicacion.md)
