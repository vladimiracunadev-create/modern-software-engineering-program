# Intervalo de Wilson

[↑ Glosario](../../README.md) · [← Intervalo de retroalimentación](./intervalo-de-retroalimentacion.md) · [Intervención sobre el sistema →](./intervencion-sobre-el-sistema.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Intervalo de confianza para una proporción, adecuado para tamaños pequeños.

Definición de trabajo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Por qué importa

La clase donde se define, [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), existe con este propósito: la clase existe para que dejes de decidir con la impresión de «parece que ahora responde mejor» y midas.

## Cómo funciona

Según [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

La tasa de éxito observada en *n* tareas es una estimación con incertidumbre. El intervalo de Wilson da un rango plausible para la tasa verdadera y se comporta bien con tamaños pequeños y tasas extremas. Su ancho decrece con la raíz de *n*: para reducirlo a la mitad hay que cuadruplicar las tareas. Comparar dos sistemas añade otra capa: aun si uno es mejor, un conjunto pequeño puede ordenarlos mal. La probabilidad de que el sistema mejor puntúe más que el peor depende de la diferencia verdadera y de *n*, y para diferencias de pocos puntos exige cientos de tareas. Cuando las tareas son pareadas (las mismas para ambos), la comparación es más sensible porque cancela la dificultad compartida.

Según [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

Reproduce el fallo clásico de la clase: **una diferencia de diez puntos en treinta tareas que desaparece con más datos**. Compara 21 y 24 aciertos de 30 con sus intervalos de Wilson.

## Ejemplo

Ejemplo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el intervalo de Wilson para 21 y 24 aciertos de 30. Antes de ejecutarlo, predice si los intervalos se solapan.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md)) son:

- **Se adopta una configuración por 3 puntos de diferencia** — causa: conjunto pequeño sin intervalos. Corrección: calcular tamaño y mostrar intervalos.
- **Se ajusta el prompt hasta que pasan los ejemplos** — causa: sin conjunto reservado. Corrección: reservar tareas que no se usan para ajustar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Cómo leer la figura.** Cada fila es un tamaño de conjunto de tareas; el marcador dorado es el 70 % observado y los marcadores turquesa y coral los límites del intervalo de Wilson al 95 %. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Intervalo de confianza](./intervalo-de-confianza.md), [Confianza](../c/confianza.md), [Intervalo](./intervalo.md), [Costo por solución aceptada](../c/costo-por-solucion-aceptada.md), [Evaluación](../e/evaluacion.md), [Frontera de Pareto](../f/frontera-de-pareto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-136](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-136-metricas-de-adopcion-retencion-y-tarea-util/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), [SE-130](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-130-criterios-de-no-exito-y-decisiones-de-abandono/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo de confianza para una proporción; autoridad: Journal of the American Statistical Association.
- [Efron (1979)](https://doi.org/10.1214/aos/1176344552) — el bootstrap; autoridad: The Annals of Statistics.
- [Chen et al., «Evaluating Large Language Models Trained on Code»](https://arxiv.org/abs/2107.03374) — pass@k y evaluación por pruebas; autoridad: preprint de OpenAI.
- [Jimenez et al., «SWE-bench»](https://arxiv.org/abs/2310.06770) — evaluación con problemas reales de repositorios; autoridad: ICLR 2024.
- [Zheng et al., «Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena»](https://arxiv.org/abs/2306.05685) — jueces automáticos y sus sesgos; autoridad: NeurIPS 2023.

---

[↑ Glosario](../../README.md) · [← Intervalo de retroalimentación](./intervalo-de-retroalimentacion.md) · [Intervención sobre el sistema →](./intervencion-sobre-el-sistema.md)
