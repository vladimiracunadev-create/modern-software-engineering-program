# Frontera de Pareto

[↑ Glosario](../../README.md) · [← Frontera de módulo](./frontera-de-modulo.md) · [Frontera de validación →](./frontera-de-validacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Conjunto de configuraciones que ninguna otra supera en todas las dimensiones a la vez.

Definición de trabajo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Por qué importa

La clase donde se define, [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), existe con este propósito: la clase existe para que dejes de decidir con la impresión de «parece que ahora responde mejor» y midas.

## Cómo funciona

Según [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

El costo por llamada es el número más visible y rara vez el que importa. Lo relevante es cuánto cuesta obtener una solución que pasa: el costo de cada intento dividido por la probabilidad de éxito, más lo que cuesta revisar cada intento. Si revisar un intento cuesta mucho más que generarlo, la configuración más barata por llamada sale cara por solución, porque falla más y cada fallo pasa por una revisión. La **frontera de Pareto** reúne las configuraciones que ninguna otra supera en todas las dimensiones a la vez (éxito, costo, latencia); una configuración dominada no se elige nunca, y entre las no dominadas la elección depende del contexto de uso: un editor interactivo valora la latencia, un trabajo por lotes valora el costo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones arma una eval con 120 tareas reales de mantenimiento, cada una con una prueba ejecutable escrita desde la especificación (`SE-558`), y reserva 40 que nadie usa para ajustar. Calcula que para detectar una diferencia de 10 puntos con el 90 % de fiabilidad necesita unas 100 tareas pareadas; con 120 está en el límite y lo declara. Compara tres configuraciones: éxito, costo por intento, latencia y minutos de revisión humana medidos en veinte tareas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md)) son:

- **Se adopta una configuración por 3 puntos de diferencia** — causa: conjunto pequeño sin intervalos. Corrección: calcular tamaño y mostrar intervalos.
- **Se ajusta el prompt hasta que pasan los ejemplos** — causa: sin conjunto reservado. Corrección: reservar tareas que no se usan para ajustar.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **frontera de Pareto** reúne las configuraciones que ninguna otra supera en todas las dimensiones a la vez (éxito, costo, latencia); una configuración dominada no se elige nunca, y entre las no dominadas la elección depende del contexto de uso: un editor interactivo valora la latencia, un trabajo por lotes valora el costo. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Dimensión](../d/dimension.md), [Costo por solución aceptada](../c/costo-por-solucion-aceptada.md), [Evaluación](../e/evaluacion.md), [Intervalo de Wilson](../i/intervalo-de-wilson.md), [Juez automático](../j/juez-automatico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-325](../../../classes/part-27-arquitectura-de-software-y-dominio/se-325-drivers-restricciones-y-atributos-de-arquitectura/README.md).

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

[↑ Glosario](../../README.md) · [← Frontera de módulo](./frontera-de-modulo.md) · [Frontera de validación →](./frontera-de-validacion.md)
