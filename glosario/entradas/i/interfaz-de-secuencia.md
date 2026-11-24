# Interfaz de secuencia

[↑ Glosario](../../README.md) · [← Interfaz](./interfaz.md) · [Interferencia →](./interferencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Una **interfaz de secuencia** es el conjunto de operaciones que ofrece una colección ordenada: **orden, longitud, acceso por posición e iteración**. [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) subraya que esta interfaz **no fija la representación**: tanto un arreglo contiguo como una lista de nodos enlazados pueden ofrecerla, con costos muy distintos en cada operación. Así se separa qué se puede hacer con una secuencia (el contrato) de cómo está organizada en memoria (la implementación).

## Por qué importa

El mismo código que usa una secuencia puede ser rápido o lento según su representación. Elegir sin pensar la operación dominante lleva a errores caros: usar `lista.pop(0)` como cola en Python es lineal en cada llamada y vaciar 80 000 elementos tarda casi un segundo. La decisión que cambia es el orden del razonamiento: **primero se enumeran las operaciones que el programa necesita y su frecuencia**, y después se elige la representación que favorece las dominantes. Elegir al revés, por costumbre, es lo que [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) desaconseja.

## Cómo funciona

Cada representación optimiza unas operaciones a costa de otras:

- **Arreglo dinámico** (la `list` de Python): acceso por posición en `O(1)`, añadir al final amortizado `O(1)`, insertar o borrar al inicio o en medio `O(n)` porque desplaza elementos. Buena localidad de memoria.
- **Lista enlazada:** insertar o borrar en una posición ya localizada en `O(1)`, pero acceso por posición `O(n)` y peor localidad.
- **Cola de dos extremos** (`deque`): añadir y quitar en ambos extremos en `O(1)`, acceso por posición en el medio más lento.

La clave de [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) es que **acceso aleatorio, inserción interior y recorrido no pueden optimizarse todos con la misma organización**. Cada decisión de representación es un compromiso. Antes de elegir se enumeran las operaciones y su frecuencia relativa; la estructura que favorece la operación dominante gana, y se confirma con una medición sobre una carga representativa.

## Ejemplo

Una cola de trabajos donde se añade al final y se extrae del inicio. Con una lista:

```python
cola = list(range(80_000))
while cola:
    cola.pop(0)           # O(n) cada vez: desplaza todo
```

Con una estructura cuya interfaz favorece esa operación:

```python
from collections import deque
cola = deque(range(80_000))
while cola:
    cola.popleft()        # O(1)
```

Ambas implementan «una secuencia con orden y longitud», pero solo una hace barata la operación dominante. [SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) documenta además otra trampa de secuencias anidadas: tres filas de una cuadrícula cambian a la vez porque `[[0]] * 3` repite la misma lista interna; se construye con `[[0] for _ in range(3)]` y se prueba una escritura aislada.

## Errores y confusiones comunes

- **Elegir por costumbre.** Se usa `list` para todo y se paga el costo en la operación dominante.
- **Confundir interfaz con representación.** Que dos colecciones ofrezcan iteración no implica costos parecidos.
- **Citar costos sin medir.** La localidad y las constantes pueden invertir el orden esperado.
- **Repetir referencias al multiplicar listas anidadas.** Las filas comparten el mismo objeto.

## Límites y cuándo no aplica

La secuencia preserva el orden, pero **no expresa por sí sola la disciplina LIFO, FIFO o de prioridad** ([SE-085](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md)): una pila, una cola y una cola de prioridad son interfaces propias, que la clase siguiente diseña explícitamente. Para colecciones pequeñas, la elección casi no importa y conviene la más clara. Y cuando se necesita buscar por clave más que por posición, ya no se trata de una secuencia sino de un mapa o un conjunto.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Interfaz](./interfaz.md), [Representación](../r/representacion.md), [Secuencia](../s/secuencia.md), [Arreglo contiguo y localidad](../a/arreglo-contiguo-y-localidad.md), [Estructuras enlazadas](../e/estructuras-enlazadas.md), [Lista dinámica y capacidad](../l/lista-dinamica-y-capacidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-085 — Arreglos, listas y secuencias](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Interfaz](./interfaz.md) · [Interferencia →](./interferencia.md)
