# Caso base

[↑ Glosario](../../README.md) · [← Cascada de reinicios](./cascada-de-reinicios.md) · [Caso coherente →](./caso-coherente.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Instancia resuelta sin llamada recursiva.

Definición de trabajo de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md): Entrada resuelta sin nueva recursión.

## Por qué importa

La clase donde se define, [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), existe con este propósito: la clase existe para relacionar definición recursiva, caso base, progreso e inducción.

## Cómo funciona

Según [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

Una estructura recursiva se define mediante casos base y constructores que contienen estructuras menores. Un árbol vacío o hoja es base; un nodo con hijos combina subárboles. La definición excluye ciclos; si el dominio admite grafos, se requiere memoria de visitados.

Según [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

Elimina el caso base o llama recursivamente con el mismo nodo. Observa no terminación controlada por límite; identifica qué medida dejó de disminuir y repara el contrato.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

El modelo de decisión diagnóstica recorre el grafo de hipótesis con una pila explícita, límite de profundidad y conjunto de visitados. La especificación explica que un ciclo es error del modelo; no se oculta devolviendo silenciosamente una lista parcial.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La demostración «funciona» con ejemplos pero no es válida** — causa: se probó en lugar de demostrar. Corrección: escribir caso base, hipótesis y paso. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))
- **El caso base no se alcanza nunca** — causa: el argumento no se acerca al base. Corrección: definir la medida que decrece. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md)) son: Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada. Inducción demuestra una propiedad del modelo, no corrige una especificación equivocada. La próxima clase combina contrato, invariante y variante para demostrar corrección y terminación.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Instancia](../i/instancia.md), [Recursión](../r/recursion.md), [Contrato](./contrato.md), [Control](./control.md), [Dominio](../d/dominio.md), [Efecto](../e/efecto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.
- [SE-063 — Iteración, recursión y recorridos](../../../classes/part-05-fundamentos-de-programacion/se-063-iteracion-recursion-y-recorridos/README.md) — [Parte 05](../../../classes/part-05-fundamentos-de-programacion/README.md), Fundamentos de programación.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-300](../../../classes/part-24-software-especializado-y-dominios/se-300-proyecto-diseno-profundo-de-un-dominio-elegido/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.
- [Python Tutorial](https://docs.python.org/3/tutorial/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Language Reference](https://docs.python.org/3/reference/) — define la semántica y los límites de la API de Python utilizada en el experimento.
- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — define la semántica y los límites de la API de Python utilizada en el experimento.

---

[↑ Glosario](../../README.md) · [← Cascada de reinicios](./cascada-de-reinicios.md) · [Caso coherente →](./caso-coherente.md)
