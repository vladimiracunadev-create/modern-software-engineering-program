# Memoización

[↑ Glosario](../../README.md) · [← Medidas y ventanas](./medidas-y-ventanas.md) · [Memoización y tabulación →](./memoizacion-y-tabulacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md)

## Definición

Reutilización de resultados de subproblemas identificados.

Definición de trabajo de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md).

## Por qué importa

La clase donde se define, [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), existe con este propósito: la clase existe para relacionar definición recursiva, caso base, progreso e inducción.

## Cómo funciona

Según [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

La definición de Fibonacci `fib(n) = fib(n−1) + fib(n−2)` es correcta y muy costosa: calcular `fib(27) = 196 418` con la recursión directa hizo 635 621 llamadas y tardó 0,097 s; con memoización (`functools.lru_cache`) hizo 28 cálculos únicos y tardó 0,000021 s. Los subproblemas se *solapan*: `fib(25)` se recalcula varias veces. La memoización resuelve cada subproblema una vez y convierte el crecimiento exponencial en lineal sin cambiar la definición. Conviene recordar el costo: la caché usa memoria y supone que la función es pura (misma entrada, misma salida, sin efectos).

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md):

El modelo de decisión diagnóstica recorre el grafo de hipótesis con una pila explícita, límite de profundidad y conjunto de visitados. La especificación explica que un ciclo es error del modelo; no se oculta devolviendo silenciosamente una lista parcial.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md)) son:

- **`RecursionError` con entradas grandes** — causa: profundidad dependiente de la entrada. Corrección: limitar la profundidad o iterar con pila propia.
- **La recursión tarda una cantidad exponencial** — causa: subproblemas solapados. Corrección: memoizar o usar programación dinámica.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La memoización resuelve cada subproblema una vez y convierte el crecimiento exponencial en lineal sin cambiar la definición. ([SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Resultado](../r/resultado.md), [Caso base](../c/caso-base.md), [Dominio](../d/dominio.md), [Estrategia](../e/estrategia.md), [Hipótesis inductiva](../h/hipotesis-inductiva.md), [Medida](./medida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-053 — Recursión, inducción y razonamiento estructural](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md) — [Parte 04](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md), Pensamiento computacional y resolución de problemas.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-064](../../../classes/part-05-fundamentos-de-programacion/se-064-funciones-parametros-retorno-y-alcance/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-150](../../../classes/part-12-ingenieria-de-requisitos/se-150-priorizacion-dependencias-y-negociacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.

---

[↑ Glosario](../../README.md) · [← Medidas y ventanas](./medidas-y-ventanas.md) · [Memoización y tabulación →](./memoizacion-y-tabulacion.md)
