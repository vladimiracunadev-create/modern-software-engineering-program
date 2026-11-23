# Juez automático

[↑ Glosario](../../README.md) · [← JSON-RPC 2.0](./json-rpc-2-0.md) · [Just transition →](./just-transition.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Modelo usado para puntuar o comparar respuestas, cuyo acuerdo con personas debe calibrarse.

Definición de trabajo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Por qué importa

En [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), el tema «Jueces automáticos» importa porque escalan la evaluación a costa de sesgos

## Cómo funciona

[SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Caso medido en la sección «Un juez automático sintético: acuerdo, posición y longitud» de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

Se simulan 1 000 comparaciones entre dos respuestas con calidades normales independientes y longitudes uniformes. El juez puntúa cada respuesta con su calidad más 0,8 por su longitud más ruido, y suma 0,4 a la primera respuesta (sesgo de posición). La etiqueta humana es la respuesta de mayor calidad. Se compara el veredicto con la etiqueta humana, el veredicto al intercambiar el orden y la frecuencia con que gana la más larga.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md)) son:

- **Se adopta una configuración por 3 puntos de diferencia** — causa: conjunto pequeño sin intervalos. Corrección: calcular tamaño y mostrar intervalos.
- **Se ajusta el prompt hasta que pasan los ejemplos** — causa: sin conjunto reservado. Corrección: reservar tareas que no se usan para ajustar.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md)) son: Las definiciones son operativas para el módulo de calificaciones. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos: una simulación de ordenación con cálculo exacto del intervalo de Wilson, un cálculo de costo por solución aceptada y dominancia, y una simulación de un juez sesgado.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Modelo](../m/modelo.md), [Costo por solución aceptada](../c/costo-por-solucion-aceptada.md), [Evaluación](../e/evaluacion.md), [Frontera de Pareto](../f/frontera-de-pareto.md), [Intervalo de Wilson](../i/intervalo-de-wilson.md), [Latencia](../l/latencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Jueces automáticos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Zheng et al., «Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena»](https://arxiv.org/abs/2306.05685) — jueces automáticos y sus sesgos; autoridad: NeurIPS 2023.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de confianza para una proporción; autoridad: Journal of the American Statistical Association.
- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación por pruebas; autoridad: preprint de OpenAI.
- [Jimenez et al., «SWE-bench»](https://arxiv.org/abs/2310.06770) — evaluación con problemas reales de repositorios; autoridad: ICLR 2024.

---

[↑ Glosario](../../README.md) · [← JSON-RPC 2.0](./json-rpc-2-0.md) · [Just transition →](./just-transition.md)
