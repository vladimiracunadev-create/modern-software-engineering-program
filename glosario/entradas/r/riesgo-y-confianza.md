# Riesgo y confianza

[↑ Glosario](../../README.md) · [← Riesgo residual](./riesgo-residual.md) · [Risk appetite →](./risk-appetite.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Grado de respaldo empírico de las estimaciones de un ítem, expresado como factor que reduce su puntuación cuando la evidencia es débil.

Definición de trabajo de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Por qué importa

En [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), el tema «Riesgo y confianza» importa porque la confianza descuenta el entusiasmo por ideas con poca evidencia, pero es otra estimación subjetiva.

## Cómo funciona

Según [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), en la sección «Riesgo y confianza»:

En RICE la confianza (100 %, 80 %, 50 %) penaliza lo que se estima sin datos. Hace dos cosas: reduce el puesto de ideas apasionantes pero indocumentadas y señala qué ítems conviene investigar antes. Pero es una opinión sobre la evidencia, no la evidencia, y puede inflarse o desinflarse según quién la proponga. La salida honesta es tratar los ítems de baja confianza como candidatos a un experimento (`SE-127`) en lugar de a construcción, y registrar de dónde sale cada porcentaje.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md):

En la plataforma de entregas, el registro de priorización conserva por cada ítem: identificador, regla aplicada, valores de entrada con su fuente y fecha, quién los estimó, puntuación base, probabilidad de top 3 bajo perturbación y estado (construir, probar, esperar, descartar). El contrato es que ningún ítem sube de puesto sin que cambie una entrada o su fuente, y que el orden se recalcula cuando se resuelve un experimento.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son:

- **El primer puesto cambia en cada reunión** — causa: el ranking no resiste la incertidumbre de sus entradas. Corrección: calcular la probabilidad de primer puesto y tratar como empatados los ítems que comparten más del 25 %.
- **El equipo hace primero lo más valioso y todo lo demás se retrasa** — causa: no se consideró la duración ni el coste del retraso. Corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se priorizó un backlog real, la perturbación es independiente y el modelo de aprender antes usa parámetros ilustrativos. La siguiente clase revisa qué aprendizaje es éticamente aceptable y cómo proteger a quienes participan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Respaldo](./respaldo.md), [Coste del retraso](../c/coste-del-retraso.md), [Decisión revisable](../d/decision-revisable.md), [Valor del aprendizaje](../v/valor-del-aprendizaje.md), [Valor y esfuerzo](../v/valor-y-esfuerzo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Intercom: RICE, simple prioritization for product managers](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/) — definición de los cuatro factores de RICE; autoridad: Intercom (fuente del autor del método).
- [Scaled Agile Framework: Weighted Shortest Job First](https://scaledagileframework.com/wsjf/) — definición de WSJF y su relación con el coste del retraso; autoridad: Scaled Agile, Inc.
- [Douglas Hubbard: How to Measure Anything](https://www.howtomeasureanything.com/) — valor de la información y cuantificación de la incertidumbre; autoridad: Hubbard Decision Research.
- [Product Talk: Opportunity Solution Tree](https://www.producttalk.org/opportunity-solution-tree/) — estructura para conectar oportunidades, soluciones y experimentos; autoridad: Teresa Torres (fuente del autor).
- [The Lean Startup: principios](https://theleanstartup.com/principles) — aprendizaje validado como unidad de progreso; autoridad: Eric Ries (fuente del autor).

---

[↑ Glosario](../../README.md) · [← Riesgo residual](./riesgo-residual.md) · [Risk appetite →](./risk-appetite.md)
