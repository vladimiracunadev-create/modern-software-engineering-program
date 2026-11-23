# Corrección total

[↑ Glosario](../../README.md) · [← Corrección por comparaciones múltiples](./correccion-por-comparaciones-multiples.md) · [Correlación →](./correlacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Corrección parcial más terminación.

Definición de trabajo de [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md).

## Por qué importa

La clase donde se define, [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), existe con este propósito: la clase existe para separar corrección parcial, terminación y adecuación del algoritmo al contrato.

## Cómo funciona

Según [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md), en la sección «Corrección total»:

Combina corrección parcial y terminación. También requiere que operaciones primitivas cumplan sus contratos. Un argumento informal debe declarar dominio y supuestos; si el grafo es finito y acíclico, eso forma parte de la precondición.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md):

El planificador del modelo de decisión diagnóstica selecciona el nodo autorizado de menor costo entre candidatos. El argumento prueba que nunca retorna fuera del conjunto elegible y que elimina un candidato por paso. Las pruebas cubren empate, vacío, costo límite y datos inválidos.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)) son:

- **El algoritmo «funciona» pero a veces no termina** — causa: falta una medida decreciente. Corrección: identificar la medida o imponer un tope.
- **Se afirma «correcto» tras pocos ejemplos** — causa: evidencia confundida con demostración. Corrección: argumentar con invariante para toda la clase de entradas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)) son: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada. Una demostración depende de un modelo preciso y no garantiza rendimiento adecuado. La siguiente clase analiza recursos conforme crece la entrada.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Corrección parcial](./correccion-parcial.md), [Terminación](../t/terminacion.md), [Algoritmo](../a/algoritmo.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Variante](../v/variante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-054 — Algoritmos, corrección y terminación](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software.

---

[↑ Glosario](../../README.md) · [← Corrección por comparaciones múltiples](./correccion-por-comparaciones-multiples.md) · [Correlación →](./correlacion.md)
