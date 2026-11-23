# Decidibilidad

[↑ Glosario](../../README.md) · [← Debugger, adapter y runtime](./debugger-adapter-y-runtime.md) · [Decisión abierta →](./decision-abierta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Existencia de un algoritmo que termina y responde todos los casos.

Definición de trabajo de [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md).

## Por qué importa

La clase donde se define, [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md), existe con este propósito: la clase existe para usar heurísticas y aproximaciones declarando objetivo, garantía y contraejemplo.

## Cómo funciona

[SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md):

El modelo de decisión diagnóstica usa greedy como primera solución, luego búsqueda acotada por 200 ms. Reporta costo de la mejor secuencia, límite inferior disponible y si probó optimalidad. Bajo presión mantiene autorización y cobertura mínima como restricciones duras.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md)) son:

- **«Es óptimo» tras probar tres casos** — causa: muestra pequeña. Corrección: buscar contraejemplos en un dominio acotado.
- **Se reporta solo la media** — causa: se oculta el peor caso. Corrección: reportar media, peor y mejor observados.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md)) son: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada. La clase no prueba NP-completitud de un problema nuevo. Enseña a reconocer el tipo de afirmación requerida. La siguiente modela comportamiento dinámico mediante estados y eventos.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Algoritmo](../a/algoritmo.md), [Anytime](../a/anytime.md), [Aproximación](../a/aproximacion.md), [Dominio](./dominio.md), [Estrategia](../e/estrategia.md), [Heurística](../h/heuristica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-056 — Heurísticas, aproximación y límites computacionales](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-056-heuristicas-aproximacion-y-limites-computacionales/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 18.404J — Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) — delimita computabilidad, complejidad y los límites de las soluciones algorítmicas.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.

---

[↑ Glosario](../../README.md) · [← Debugger, adapter y runtime](./debugger-adapter-y-runtime.md) · [Decisión abierta →](./decision-abierta.md)
