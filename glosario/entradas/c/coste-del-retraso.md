# Coste del retraso

[↑ Glosario](../../README.md) · [← Coste de una consulta](./coste-de-una-consulta.md) · [Coste hundido y compromiso →](./coste-hundido-y-compromiso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

El **coste del retraso** (*cost of delay*) es la pérdida económica o de beneficio por unidad de tiempo en que un trabajo no está disponible; sirve para ordenar trabajos de distinta duración ([SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)). Se expresa en valor por semana, por ejemplo, no como un total.

## Por qué importa

Cambia cómo se ordena una cola de trabajo. Ordenar solo por «lo más valioso primero» parece razonable y no minimiza la pérdida total. [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) lo muestra: un trabajo muy valioso pero largo retrasa a todos los demás. Cuando el trabajo se secuencia, importan dos cosas a la vez: cuánto cuesta cada semana de espera y cuánto dura cada trabajo.

## Cómo funciona

Si cuatro trabajos se hacen uno tras otro, cada semana que espera uno acumula su coste de retraso. El coste total depende del orden: un trabajo corto con coste de retraso alto conviene antes que uno largo con valor algo mayor, porque libera su valor pronto y retrasa poco a los demás. La regla que lo formaliza es **«trabajo más corto ponderado primero»** (WSJF, *weighted shortest job first*): ordenar por coste de retraso dividido entre duración. En el caso simple de trabajos independientes y sin dependencias, esta regla **minimiza el coste total**, resultado clásico de la teoría de planificación.

[SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) insiste en dos cautelas. Primera, los costes de retraso reales son **difíciles de estimar** (hay que estimar el valor perdido por semana, que cambia con el tiempo y con la competencia), por lo que se trabajan como rangos y se evalúa si el orden resiste a perturbaciones. El registro de priorización de la plataforma guarda por ítem la regla aplicada, los valores de entrada con su fuente y fecha, quién los estimó, la puntuación base, la probabilidad de quedar entre los tres primeros bajo perturbación y el estado (construir, probar, esperar, descartar). Segunda, el orden se recalcula cuando se resuelve un experimento y ningún ítem sube sin que cambie una entrada o su fuente.

## Ejemplo

Tres trabajos con (coste de retraso por semana, duración): A (10, 4 semanas), B (6, 1 semana), C (3, 1 semana). WSJF: A=2,5; B=6; C=3 → orden B, C, A. Coste total de espera: B espera 0, C espera 1 semana (3), A espera 2 semanas (20): 23. El orden «mayor valor primero» (A, B, C) da: B espera 4 (24) y C espera 5 (15): 39. (Aritmética ilustrativa del principio de [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).)

## Errores y confusiones comunes

- **Hacer primero lo más valioso y retrasar todo lo demás**: no se consideró la duración ni el coste del retraso; corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total.
- **Tratar una estimación como un hecho.**
- **Ignorar las dependencias**: la regla supone trabajos independientes.
- **Confundir coste del retraso con costo de oportunidad**: el primero es por unidad de tiempo de espera; el segundo, el valor de lo que se descarta.

## Límites y cuándo no aplica

WSJF solo es óptimo con trabajos independientes y costes de retraso constantes en el tiempo. Con fechas límite duras (un cumplimiento regulatorio), el coste cambia bruscamente y hay que modelarlo. Cuando las estimaciones son muy inciertas, una regla simple con rangos y pruebas de sensibilidad es más honesta que una puntuación precisa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Trabajo](../t/trabajo.md), [Decisión revisable](../d/decision-revisable.md), [Riesgo y confianza](../r/riesgo-y-confianza.md), [Valor del aprendizaje](../v/valor-del-aprendizaje.md), [Valor y esfuerzo](../v/valor-y-esfuerzo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Scaled Agile Framework: Weighted Shortest Job First](https://scaledagileframework.com/wsjf/) — definición de WSJF y su relación con el coste del retraso; autoridad: Scaled Agile, Inc.
- [Intercom: RICE, simple prioritization for product managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) — definición de los cuatro factores de RICE; autoridad: Intercom (fuente del autor del método).
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — valor de la información y cuantificación de la incertidumbre; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar oportunidades, soluciones y experimentos; autoridad: Teresa Torres (fuente del autor).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado como unidad de progreso; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Coste de una consulta](./coste-de-una-consulta.md) · [Coste hundido y compromiso →](./coste-hundido-y-compromiso.md)
