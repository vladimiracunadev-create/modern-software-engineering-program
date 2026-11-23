# Decisión revisable

[↑ Glosario](../../README.md) · [← Decisión reversible y experimento](./decision-reversible-y-experimento.md) · [Declaración de alcance →](./declaracion-de-alcance.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md)

## Definición

Regla de priorización escrita con sus entradas, fecha, responsable y condiciones de revisión, de modo que otra persona pueda reproducir y cuestionar el orden.

Definición de trabajo de [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

## Por qué importa

En [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), el tema «Decisión revisable» importa porque una regla que no se puede revisar ni disputar convierte el orden en autoridad.

## Cómo funciona

Según [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md), en la sección «Decisión revisable»:

Un registro de priorización conserva la regla, los valores de entrada, quién los estimó, cuándo, de dónde salen y qué los haría cambiar. Incluye una medida de robustez (qué ítems resisten la perturbación) y una lista de ítems «en duda» que se resolverán con un experimento. Evita dos fallos: gaming (inflar alcance o impacto para subir de puesto) y parálisis (esperar números perfectos). La revisión es periódica y se dispara por eventos: una prueba terminada, un cambio de alcance, un incidente.

Según [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), en la sección «Decisión revisable»:

La decisión incluye la opción elegida (financiar por etapas, no financiar, financiar por completo), el responsable, la fecha de decisión, la fecha de revisión, el criterio de abandono y los límites del caso. Un validador comprueba lo que se puede comprobar sin entender el negocio (campos, rangos, sumas, trazabilidad); lo demás exige a otra persona que recalcule el modelo y revise cada afirmación contra su evidencia.

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
- **Ver también:** [Condición de revisión](../c/condicion-de-revision.md), [Condición](../c/condicion.md), [Regla](../r/regla.md), [Revisión](../r/revision.md), [Caso de viabilidad](../c/caso-de-viabilidad.md), [Compuerta de abandono](../c/compuerta-de-abandono.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-128 — Priorización por valor, riesgo y aprendizaje](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md) — [Parte 10](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/README.md), Descubrimiento y estrategia de producto.
- [SE-144 — Proyecto: caso de viabilidad técnico-económica](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-059](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-059-taller-descomponer-un-problema-ambiguo/README.md), [SE-137](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-137-telemetria-de-producto-y-consentimiento/README.md).

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

[↑ Glosario](../../README.md) · [← Decisión reversible y experimento](./decision-reversible-y-experimento.md) · [Declaración de alcance →](./declaracion-de-alcance.md)
