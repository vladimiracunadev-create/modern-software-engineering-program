# Orden e iteración

[↑ Glosario](../../README.md) · [← Orden de resolución de métodos](./orden-de-resolucion-de-metodos.md) · [Orden global de adquisición →](./orden-global-de-adquisicion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

**Orden e iteración** designa, en [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), la pregunta de **en qué orden entrega sus elementos una colección al recorrerla** y qué garantías ofrece el lenguaje sobre eso. En Python: el `dict` **garantiza el orden de inserción**; el `set` **no promete un orden estable entre ejecuciones**. Es la razón por la que «iterar» no equivale a «iterar en un orden de fiar»: depende de la estructura y de lo que la documentación promete, no de lo que se ve en una ejecución.

## Por qué importa

Un programa que depende del orden observado de un conjunto funciona hoy y falla mañana, sin cambios de código: otra versión del intérprete, otra ejecución con otra semilla de hash, otros datos. [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) lo señala con un caso: usar el orden observado de un `set` como desempate **crea pruebas frágiles**. La decisión que cambia es dónde vive el orden: si importa, **debe representarse explícitamente** (una lista, una clave de ordenamiento), no heredarse como efecto secundario de la estructura.

## Cómo funciona

Una tabla hash coloca cada elemento según el valor de su *hash*, no según su llegada. Un `set` de cadenas, en Python, usa un *hash* **aleatorizado por ejecución** (una medida de seguridad contra colisiones deliberadas), de modo que el orden de iteración puede cambiar de una ejecución a otra. Un `dict`, desde las versiones modernas de Python, conserva el **orden de inserción** como parte de su contrato, porque guarda las entradas en un arreglo ordenado además de la tabla.

Eso produce reglas prácticas:

- Si se necesita recorrer en el orden en que se insertó, el `dict` lo garantiza; un `set` no.
- Si se necesita un orden por valor, se **ordena explícitamente** antes de producir resultados (`sorted`).
- Si el resultado de un programa depende de un orden que no se ordenó, es un defecto latente aunque las pruebas hoy pasen.

[SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) documenta dos síntomas: el orden de salida cambia entre ejecuciones porque se itera un `set` de cadenas con *hash* aleatorizado (se ordena antes de producir resultados), y una búsqueda en un `dict` falla para una clave que «seguro» se insertó porque la clave se mutó después de insertarla (se usan claves inmutables o un identificador estable).

## Ejemplo

```python
etiquetas = {"rojo", "verde", "azul"}
print(list(etiquetas))          # puede variar entre ejecuciones del programa

print(sorted(etiquetas))        # ['azul', 'rojo', 'verde']: orden definido por el programa

d = {}
d["b"] = 1; d["a"] = 2
print(list(d))                  # ['b', 'a']: orden de inserción, garantizado
```

Una prueba que compara `list(etiquetas)` con una lista fija es frágil: pasa o falla según la ejecución. La corrección es comparar con `sorted(etiquetas)` o con otro conjunto, que no depende del orden.

## Errores y confusiones comunes

- **Tomar el orden observado por garantía.** Que un `set` salga ordenado un día no lo promete.
- **Pruebas que dependen del orden de un `set`.** Son intermitentes.
- **Confundir orden de inserción con orden por clave.** El `dict` conserva el primero, no ordena.
- **Mutar una clave después de insertarla.** La búsqueda falla porque el *hash* cambió.

## Límites y cuándo no aplica

Las tablas hash no mantienen rangos ni prefijos ordenados ([SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md)): para consultas por rango se necesita una estructura ordenada, como un árbol de búsqueda, que la clase siguiente estudia. La garantía de orden del `dict` es de Python moderno; en otros lenguajes los mapas hash pueden no ofrecerla, y hay que consultar la documentación de cada uno antes de apoyarse en ella.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Factor de carga y crecimiento](../f/factor-de-carga-y-crecimiento.md), [Función hash y buckets](../f/funcion-hash-y-buckets.md), [Igualdad y estabilidad](../i/igualdad-y-estabilidad.md), [Mapa y conjunto](../m/mapa-y-conjunto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-087 — Tablas hash, mapas y conjuntos](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Orden de resolución de métodos](./orden-de-resolucion-de-metodos.md) · [Orden global de adquisición →](./orden-global-de-adquisicion.md)
