# Poda segura

[↑ Glosario](../../README.md) · [← Poda](./poda.md) · [Polisemia →](./polisemia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Una **poda** es el descarte de una rama completa del espacio de búsqueda sin explorarla; es **segura** cuando se puede demostrar que esa rama **no contiene ninguna solución válida ni mejor que la ya encontrada**. En [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md): una poda descarta ramas que no pueden mejorar o satisfacer, y debe derivarse de una **cota o restricción necesaria**. La seguridad es la condición que separa una poda de una apuesta: la primera no cambia el resultado del algoritmo, solo su costo.

## Por qué importa

La búsqueda exhaustiva crece de forma exponencial; sin poda, muchos problemas son inviables, y con una poda mal hecha, el algoritmo termina rápido y devuelve una respuesta incorrecta sin avisar. La decisión que cambia es qué se permite eliminar: solo lo que se puede **justificar**. [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) marca la frontera: una **heurística que parece improbable no es una poda correcta**. Puede usarse para **ordenar** la exploración (probar primero lo prometedor) pero no para **eliminar** sin prueba.

## Cómo funciona

Hay dos clases de razonamiento que dan podas seguras:

- **Por restricción (viabilidad):** si el estado parcial ya viola una condición que ninguna extensión puede reparar, no hay solución en esa rama. Ejemplo: al repartir tareas con dependencias, si se elige una cuyas dependencias no están resueltas, esa rama es imposible.
- **Por cota (optimalidad):** se calcula una **cota** del mejor resultado alcanzable desde un estado; si ni siquiera esa cota mejora la mejor solución conocida, la rama no puede superarla y se descarta. La cota debe ser **optimista y válida**: nunca menor (en maximización) que lo realmente alcanzable, o se podarían ramas buenas.

La heurística, en cambio, es una apuesta («esta rama parece mala»): puede acelerar, pero no ofrece garantía. Usada para ordenar (explorar primero lo mejor) mejora el rendimiento sin riesgo, porque todas las ramas se acaban explorando si hace falta. Usada para eliminar, cambia el resultado.

Para validar, [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) pide **contrastar el conteo de soluciones con la enumeración completa** en un `n` pequeño: si la versión con poda encuentra menos soluciones que la fuerza bruta, la poda eliminó una rama válida.

## Ejemplo

Se buscan combinaciones de casos cuyo costo total no supere un presupuesto. Poda segura: si la suma parcial ya excede el presupuesto y los costos son no negativos, ninguna extensión podrá bajarla.

```python
def combinaciones(costos, presupuesto, i=0, suma=0, actual=None, salida=None):
    actual = [] if actual is None else actual
    salida = [] if salida is None else salida
    if suma > presupuesto:          # poda segura: costos >= 0
        return salida
    if i == len(costos):
        salida.append(list(actual)); return salida
    actual.append(costos[i]); combinaciones(costos, presupuesto, i+1, suma+costos[i], actual, salida)
    actual.pop();             combinaciones(costos, presupuesto, i+1, suma, actual, salida)
    return salida
```

La poda es segura solo por la hipótesis «costos ≥ 0»: con un costo negativo, una rama que ya excede podría recuperarse y la poda sería incorrecta.

## Errores y confusiones comunes

- **Podar por intuición.** «Esto parece improbable» no es una prueba.
- **Cota inválida.** Si subestima lo alcanzable, elimina ramas buenas.
- **No contrastar con fuerza bruta.** Sin esa comprobación el error pasa inadvertido.
- **Culpar a la poda de la lentitud.** A veces el problema es el orden de decisiones: se prueban primero las variables más restringidas y se mide el número de nodos.

## Límites y cuándo no aplica

La exploración exacta puede seguir siendo intratable aunque se pode ([SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md)): una buena poda reduce el árbol, no cambia su naturaleza exponencial en el peor caso. Si solo se necesita una buena solución y no la óptima, una heurística declarada como tal es honesta y suficiente. Y la poda exige conocer propiedades del problema (monotonía, cotas), que no siempre existen.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Poda](./poda.md), [Backtracking](../b/backtracking.md), [Divide y vencerás](../d/divide-y-venceras.md), [Espacio de estados](../e/espacio-de-estados.md), [Recurrencias y umbral práctico](../r/recurrencias-y-umbral-practico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Poda](./poda.md) · [Polisemia →](./polisemia.md)
