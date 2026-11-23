# Costo por solución aceptada

[↑ Glosario](../../README.md) · [← Costo por resultado](./costo-por-resultado.md) · [Costura →](./costura.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md)

## Definición

Costo total de intentos y revisión dividido por las soluciones que se aceptan.

Definición de trabajo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md).

## Por qué importa

En [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md), el tema «Costo por solución aceptada» importa porque incluye reintentos y revisión humana

## Cómo funciona

Según [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

Se definen seis configuraciones sintéticas con tasa de éxito, costo por intento y latencia. El costo por solución aceptada es (costo del intento + costo de revisión) dividido por la tasa de éxito, con un costo de revisión de 0,40 por intento, en una unidad arbitraria.

Según [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones arma una eval con 120 tareas reales de mantenimiento, cada una con una prueba ejecutable escrita desde la especificación (`SE-558`), y reserva 40 que nadie usa para ajustar. Calcula que para detectar una diferencia de 10 puntos con el 90 % de fiabilidad necesita unas 100 tareas pareadas; con 120 está en el límite y lo declara. Compara tres configuraciones: éxito, costo por intento, latencia y minutos de revisión humana medidos en veinte tareas.

## Ejemplo

Ejemplo de [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo del módulo de calificaciones arma una eval con 120 tareas reales de mantenimiento, cada una con una prueba ejecutable escrita desde la especificación (`SE-558`), y reserva 40 que nadie usa para ajustar. Calcula que para detectar una diferencia de 10 puntos con el 90 % de fiabilidad necesita unas 100 tareas pareadas; con 120 está en el límite y lo declara. Compara tres configuraciones: éxito, costo por intento, latencia y minutos de revisión humana medidos en veinte tareas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La configuración más barata sale cara** — causa: no se midió la revisión humana. Corrección: costo por solución aceptada con revisión medida. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El costo por intento varía por un factor de 55 entre la primera y la última configuración (de 0,002 a 0,110), pero el costo por solución aceptada solo entre 0,55 y 0,77: la revisión humana (0,40 por intento) domina el total. ([SE-561](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-560](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-560-context-engineering-y-reduccion-de-ambiguedad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](./costo.md), [Evidencia](../e/evidencia.md), [Revisión](../r/revision.md), [Evaluación](../e/evaluacion.md), [Frontera de Pareto](../f/frontera-de-pareto.md), [Intervalo de Wilson](../i/intervalo-de-wilson.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-561 — Evals de exactitud, utilidad, costo y latencia](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-561-evals-de-exactitud-utilidad-costo-y-latencia/README.md) — [Parte 46](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/README.md), Desarrollo de software asistido por IA.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md).

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

[↑ Glosario](../../README.md) · [← Costo por resultado](./costo-por-resultado.md) · [Costura →](./costura.md)
