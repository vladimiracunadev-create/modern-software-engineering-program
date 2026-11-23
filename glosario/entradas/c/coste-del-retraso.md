# Coste del retraso

[↑ Glosario](../../README.md) · [← Coste de una consulta](./coste-de-una-consulta.md) · [Coste hundido y compromiso →](./coste-hundido-y-compromiso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Pérdida económica o de beneficio por unidad de tiempo en que un trabajo no está disponible; sirve para ordenar trabajos de distinta duración.

Definición de trabajo de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Por qué importa

En [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), el tema «Coste del retraso» importa porque cuando el trabajo se secuencia, importa cuánto cuesta cada semana de espera y cuánto dura cada trabajo.

## Cómo funciona

Según [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), en la sección «Coste del retraso»:

Si cuatro trabajos se hacen uno tras otro, cada semana que espera uno acumula su coste de retraso. Ordenar por mayor valor no minimiza el total: un trabajo muy valioso pero largo retrasa a todos los demás. La regla de «trabajo más corto ponderado primero» (WSJF) ordena por coste de retraso dividido entre duración y, en el caso simple de trabajos independientes y sin dependencias, minimiza el coste total. Los costes de retraso reales son difíciles de estimar y las dependencias entre trabajos rompen la regla, de modo que sirve como criterio, no como algoritmo infalible.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md):

En la plataforma de entregas, el registro de priorización conserva por cada ítem: identificador, regla aplicada, valores de entrada con su fuente y fecha, quién los estimó, puntuación base, probabilidad de top 3 bajo perturbación y estado (construir, probar, esperar, descartar). El contrato es que ningún ítem sube de puesto sin que cambie una entrada o su fuente, y que el orden se recalcula cuando se resuelve un experimento.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El equipo hace primero lo más valioso y todo lo demás se retrasa** — causa: no se consideró la duración ni el coste del retraso. Corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total. ([SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se priorizó un backlog real, la perturbación es independiente y el modelo de aprender antes usa parámetros ilustrativos. La siguiente clase revisa qué aprendizaje es éticamente aceptable y cómo proteger a quienes participan.

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
