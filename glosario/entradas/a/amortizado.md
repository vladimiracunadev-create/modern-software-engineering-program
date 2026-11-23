# Amortizado

[↑ Glosario](../../README.md) · [← AMFE](./amfe.md) · [Ampliar, migrar y contraer →](./ampliar-migrar-y-contraer.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Costo promedio garantizado sobre una secuencia.

Definición de trabajo de [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md).

## Por qué importa

La clase donde se define, [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md), existe con este propósito: la clase existe para comparar crecimiento temporal y espacial antes de interpretar benchmarks.

## Cómo funciona

Según [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md):

El peor caso fija garantía; promedio exige distribución justificada; amortizado reparte secuencias de operaciones sin asumir azar. Presentar el caso favorable como promedio es un error. El modelo de decisión diagnóstica usa peor caso para deadline y medición para distribución observada.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md):

El modelo de decisión diagnóstica modela recorrido O(V+E) y memoria O(V). El benchmark genera grafos dispersos y densos, separa construcción de consulta y registra versión. Un presupuesto cancela antes de agotar memoria y reporta salida parcial como incompleta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **«Es O(1)» y un caso tarda mucho** — causa: se confundió amortizado con peor caso. Corrección: declarar si el dato es promedio o peor caso. ([SE-055](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El peor caso fija garantía; promedio exige distribución justificada; amortizado reparte secuencias de operaciones sin asumir azar. ([SE-055](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Costo](../c/costo.md), [Secuencia](../s/secuencia.md), [Sobre](../s/sobre.md), [Benchmark](../b/benchmark.md), [Complejidad](../c/complejidad.md), [Cota](../c/cota.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-055 — Complejidad temporal y espacial](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-055-complejidad-temporal-y-espacial/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 18.404J — Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) — delimita computabilidad, complejidad y los límites de las soluciones algorítmicas.

---

[↑ Glosario](../../README.md) · [← AMFE](./amfe.md) · [Ampliar, migrar y contraer →](./ampliar-migrar-y-contraer.md)
