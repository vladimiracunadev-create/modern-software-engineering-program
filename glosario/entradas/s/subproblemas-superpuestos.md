# Subproblemas superpuestos

[↑ Glosario](../../README.md) · [← Subida reanudable](./subida-reanudable.md) · [Subtipado conductual →](./subtipado-conductual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un problema tiene **subproblemas superpuestos** cuando, al resolverlo recursivamente, **los mismos subproblemas se vuelven a calcular muchas veces**. En [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), la **programación dinámica** identifica esos estados que reaparecen y **guarda sus soluciones** para no recomputarlas. Es una de las dos propiedades que habilitan la técnica (la otra es la **subestructura óptima**: la solución del problema se construye con soluciones óptimas de subproblemas). Sin superposición, guardar resultados no ahorra nada.

## Por qué importa

Una recursión directa sobre un problema con superposición es exponencial por pura repetición: el caso conocido es el cálculo recursivo de los números de Fibonacci, que recalcula los mismos valores una y otra vez. Reconocer la superposición convierte un algoritmo inviable en uno polinomial. La decisión que cambia es cómo se aborda un problema de optimización: en lugar de explorar sin memoria (retroceso) o de confiar en una regla local (voraz), se pregunta si los subproblemas se repiten y se diseña el **estado** que los identifica.

## Cómo funciona

Hay dos formas de aprovecharla:

- **Descendente con memoización:** se escribe la recursión natural y se guarda el resultado de cada llamada en un diccionario, indexado por el estado. Si el estado ya se calculó, se devuelve el guardado.
- **Ascendente con tabla:** se calculan los subproblemas de menor a mayor tamaño llenando una tabla.

La clave es el **estado**: debe contener **toda la información necesaria para el futuro** del cálculo. [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md) marca los dos riesgos opuestos. Si se **omite una dimensión** que importaba, la memoria es rápida pero **incorrecta**: dos subproblemas distintos se consideran el mismo y se reutiliza un resultado que no corresponde. Si se **añaden dimensiones sin criterio**, el número de estados explota y la memoria se agota. El diseño del estado es, por tanto, el trabajo intelectual central, y lo verifica la comparación con la fuerza bruta en tamaños pequeños.

## Ejemplo

El número de formas de dar cambio para un total, con memoización:

```python
from functools import lru_cache

def formas(monedas, total):
    @lru_cache(maxsize=None)
    def f(restante, i):                    # estado: (restante, índice de moneda)
        if restante == 0: return 1
        if restante < 0 or i == len(monedas): return 0
        return f(restante - monedas[i], i) + f(restante, i + 1)
    return f(total, 0)
```

Sin `lru_cache`, `f(restante, i)` se evalúa muchas veces con los mismos argumentos; con ella, cada estado se calcula una vez, y el costo pasa a ser proporcional al número de estados (`total × len(monedas)`). Si se omitiera `i` del estado, se cometería el error de la dimensión omitida y se contarían formas repetidas. Contrastar con una enumeración completa para `total` pequeño lo revelaría.

## Errores y confusiones comunes

- **Memoizar sin estado completo.** Respuestas rápidas e incorrectas.
- **Estado con demasiadas dimensiones.** Memoria inviable.
- **Aplicar a problemas sin superposición.** La caché solo gasta memoria.
- **Confundir con la voracidad.** La voraz no guarda subproblemas ni reconsidera.

## Límites y cuándo no aplica

La programación dinámica exige un **estado finito y manejable** ([SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md)): si el número de estados es astronómico, la tabla no cabe y hay que usar poda, aproximación o heurística. Cuando el camino recorrido importa para el resultado (no solo el estado), no se pueden fusionar los caminos, y la exploración con retroceso es el enfoque adecuado. Y memoizar en funciones con efectos hace que los efectos «desaparezcan» tras la primera llamada.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Estado](../e/estado.md), [Evidencia](../e/evidencia.md), [Guarda](../g/guarda.md), [Contraejemplo mínimo](../c/contraejemplo-minimo.md), [Estrategia voraz](../e/estrategia-voraz.md), [Memoización y tabulación](../m/memoizacion-y-tabulacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare.
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) — Semántica de secuencias, conjuntos, mappings, igualdad y hash; autoridad: Python Software Foundation.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Timeit, cprofile y tracemalloc con sus límites; autoridad: Python Software Foundation.
- [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare.

---

[↑ Glosario](../../README.md) · [← Subida reanudable](./subida-reanudable.md) · [Subtipado conductual →](./subtipado-conductual.md)
