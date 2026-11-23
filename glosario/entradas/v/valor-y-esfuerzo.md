# Valor y esfuerzo

[↑ Glosario](../../README.md) · [← Valor presente neto](./valor-presente-neto.md) · [Valor, costo y riesgo →](./valor-costo-y-riesgo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Razón entre el beneficio esperado de un ítem y su costo estimado; ordena ítems comparables, no mide su valor real.

Definición de trabajo de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Por qué importa

En [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), el tema «Valor y esfuerzo» importa porque un cociente de beneficio y costo ordena rápido, pero oculta cuánto se sabe de cada término.

## Cómo funciona

Según [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), en la sección «Valor y esfuerzo»:

RICE multiplica alcance (cuántas personas en un periodo), impacto (cuánto mejora a cada una) y confianza (cuánta evidencia respalda las dos estimaciones) y divide entre esfuerzo (persona-meses). La virtud de una fórmula así es obligar a poner números donde antes había opiniones y permitir compararlos. Su límite es que cada número es estimado, y una multiplicación de cuatro estimaciones inciertas produce otra estimación más incierta, pero con apariencia de precisión de entero. Una puntuación sirve para discutir; la discusión es lo que decide.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md):

En la plataforma de entregas, el registro de priorización conserva por cada ítem: identificador, regla aplicada, valores de entrada con su fuente y fecha, quién los estimó, puntuación base, probabilidad de top 3 bajo perturbación y estado (construir, probar, esperar, descartar). El contrato es que ningún ítem sube de puesto sin que cambie una entrada o su fuente, y que el orden se recalcula cuando se resuelve un experimento.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son:

- **El primer puesto cambia en cada reunión** — causa: el ranking no resiste la incertidumbre de sus entradas. Corrección: calcular la probabilidad de primer puesto y tratar como empatados los ítems que comparten más del 25 %.
- **El equipo hace primero lo más valioso y todo lo demás se retrasa** — causa: no se consideró la duración ni el coste del retraso. Corrección: comparar con WSJF sobre las permutaciones relevantes y elegir el orden de menor coste total.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se priorizó un backlog real, la perturbación es independiente y el modelo de aprender antes usa parámetros ilustrativos. La siguiente clase revisa qué aprendizaje es éticamente aceptable y cómo proteger a quienes participan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Costo](../c/costo.md), [Valor](./valor.md), [Coste del retraso](../c/coste-del-retraso.md), [Decisión revisable](../d/decision-revisable.md), [Riesgo y confianza](../r/riesgo-y-confianza.md), [Valor del aprendizaje](./valor-del-aprendizaje.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md).

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

[↑ Glosario](../../README.md) · [← Valor presente neto](./valor-presente-neto.md) · [Valor, costo y riesgo →](./valor-costo-y-riesgo.md)
