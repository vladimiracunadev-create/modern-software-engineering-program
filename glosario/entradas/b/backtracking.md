# Backtracking

[↑ Glosario](../../README.md) · [← Backpressure y pérdida](./backpressure-y-perdida.md) · [Baja →](./baja.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

El **backtracking** (vuelta atrás) es una estrategia de búsqueda exhaustiva en la que se **elige** una opción, se **avanza** con ella, se **detecta** si el estado parcial ya no puede completarse y, en ese caso, se **revierte** la última elección para probar otra. En [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) se enseña junto con divide y vencerás como dos formas de organizar un problema grande: una explora un espacio de decisiones en profundidad; la otra lo parte en subproblemas independientes. No es un algoritmo concreto sino un esquema que se instancia para cada problema.

## Por qué importa

Muchos problemas (asignar tareas respetando dependencias, colocar piezas, elegir subconjuntos) no tienen una fórmula directa y obligan a explorar combinaciones. La decisión profesional es **cómo explorar sin enumerar todo**: el backtracking descarta ramas completas en cuanto una decisión parcial es imposible, y eso separa un programa que termina en segundos de uno que no termina. También importa por su riesgo: una poda equivocada elimina soluciones válidas sin dar error, así que el algoritmo puede ser rápido y estar mal.

## Cómo funciona

Se recorre un **árbol de decisiones** implícito: cada nivel es una variable por decidir y cada rama, uno de sus valores. En cada nodo:

1. Si el estado parcial viola una restricción, se abandona la rama (poda).
2. Si está completo y es válido, se registra la solución.
3. Si no, para cada candidato se aplica, se llama recursivamente y se **deshace**.

El corazón del mecanismo es la **restauración simétrica**: lo que la elección cambió debe quedar exactamente como estaba al volver, incluso si la llamada recursiva falla con una excepción ([SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md)). Hay dos maneras de lograrlo. Copiar el estado en cada paso simplifica el razonamiento (cada rama trabaja sobre su copia) pero cuesta tiempo y memoria. Mutar y deshacer es más barato pero exige un invariante claro y pruebas de que no queda contaminación entre ramas. La eficiencia depende de dos palancas: qué tan temprano se detecta la imposibilidad y el **orden** en que se eligen las variables; probar primero la más restringida suele reducir mucho los nodos visitados.

## Ejemplo

En la biblioteca de estructuras y algoritmos de [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md), un caso lleva identidad, prioridad, dependencias, instante de llegada y estado. Elegir un orden de resolución que respete las dependencias es un problema de este tipo. Un esqueleto (ilustración) muestra la simetría exigida:

```python
def resolver(estado, pendientes, solucion, salida):
    if not pendientes:
        salida.append(list(solucion)); return
    for c in list(pendientes):
        if estado.puede(c):
            estado.aplicar(c); pendientes.remove(c); solucion.append(c)
            try:
                resolver(estado, pendientes, solucion, salida)
            finally:
                solucion.pop(); pendientes.add(c); estado.deshacer(c)
```

El `finally` garantiza la restauración aunque haya error. Para validar la poda, [SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) pide contrastar el conteo de soluciones con enumeración completa en un `n` pequeño.

## Errores y confusiones comunes

- **Podar una rama válida.** El algoritmo encuentra menos soluciones que la fuerza bruta; se detecta comparando conteos en `n` pequeño.
- **Restaurar solo en el camino feliz.** Una excepción deja el estado sucio y las ramas siguientes parten de datos contaminados.
- **Culpar al algoritmo cuando la búsqueda es lenta.** A menudo el orden de las decisiones es desfavorable; probar primero las variables más restringidas y medir nodos.
- **Confundirlo con recursión.** La recursión es el mecanismo; el backtracking es la política de elegir, deshacer y podar.

## Límites y cuándo no aplica

La exploración exacta puede seguir siendo intratable: en el peor caso el árbol es exponencial y ninguna poda lo evita ([SE-092](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md)). Si el problema tiene subproblemas superpuestos, la programación dinámica evita recomputar lo que el backtracking repite. Si basta una solución aproximada, una estrategia voraz o una heurística puede ser mejor. El backtracking conviene cuando se necesita una solución exacta o todas las soluciones y el espacio, tras la poda, es abarcable.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Divide y vencerás](../d/divide-y-venceras.md), [Espacio de estados](../e/espacio-de-estados.md), [Poda segura](../p/poda-segura.md), [Recurrencias y umbral práctico](../r/recurrencias-y-umbral-practico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-092 — Backtracking, divide y vencerás](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-091](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md).

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

[↑ Glosario](../../README.md) · [← Backpressure y pérdida](./backpressure-y-perdida.md) · [Baja →](./baja.md)
