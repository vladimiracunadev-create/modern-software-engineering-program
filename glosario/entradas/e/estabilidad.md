# Estabilidad

[↑ Glosario](../../README.md) · [← Esquema de datos](./esquema-de-datos.md) · [Estabilidad de segmentos →](./estabilidad-de-segmentos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

En el contexto de ordenamiento ([SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)), un algoritmo de ordenamiento es **estable** si **conserva el orden relativo entre claves iguales**: si dos elementos tienen la misma clave de comparación, el que estaba antes en la entrada queda antes en la salida. En este programa, «estabilidad» designa esa propiedad y no otros sentidos de la palabra (estabilidad numérica, estabilidad de una API o de un sistema), que aparecen en otras entradas.

## Por qué importa

Muchas veces los datos se ordenan por más de un criterio: primero por prioridad y, entre iguales, por orden de llegada. Si el ordenamiento es estable, el orden de llegada sobrevive como desempate sin escribirlo. Si no se sabe si lo es, o se asume sin garantía, el orden de los empates cambia entre versiones o entre implementaciones, y lo que parecía presentación se convierte en **comportamiento accidental** de lo que dependen otros ([SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)). La decisión que cambia es qué se promete sobre los empates: se garantiza o se desempata de forma explícita.

## Cómo funciona

Un algoritmo es estable cuando, ante claves iguales, nunca intercambia elementos de modo que invierta su orden original. El ordenamiento por mezcla (*merge sort*) y la implementación `sorted` de Python (Timsort) lo son; otros, como el *quicksort* clásico o el de selección, no lo garantizan. La propiedad permite una técnica útil: **ordenar por varias claves con pasadas sucesivas**, de la menos significativa a la más significativa. Cada pasada estable preserva el orden que dejó la anterior entre empates.

[SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) lo mide: con registros `[('b',1),('a',1),('c',0),('d',1),('e',0)]`, `sorted(registros, key=prioridad)` devolvió `['c','e','b','a','d']`: los empates conservaron el orden de llegada (b antes de a). La misma clase mide tres trampas del orden: `sorted([3.0, nan, 1.0, 2.0])` devolvió `[3.0, nan, 1.0, 2.0]` (no ordenó nada, porque `NaN` rompe el orden total), `sorted([1, 'a'])` lanza `TypeError`, y `sorted(['Zebra','apple','Árbol','zeta'])` dio `['Zebra','apple','zeta','Árbol']`: orden por punto de código, no alfabético del español.

## Ejemplo

Una lista de tareas con prioridad que debe ordenarse por prioridad ascendente y, entre iguales, por fecha de creación. Con un ordenamiento estable basta con dos pasadas:

```python
tareas.sort(key=lambda t: t.creada)        # criterio menos significativo
tareas.sort(key=lambda t: t.prioridad)     # más significativo; estable
```

Tras la segunda pasada, entre tareas de igual prioridad se conserva el orden por fecha. Si se cambiara a una implementación sin garantía de estabilidad, el orden de los empates podría variar sin que ninguna prueba lo advirtiera, salvo que haya una que lo compruebe.

## Errores y confusiones comunes

- **Suponer estabilidad donde no se garantiza.** Los empates cambian de orden entre versiones; la corrección es usar `sorted` (estable) o añadir un desempate explícito.
- **Confundir estabilidad con determinismo.** Un algoritmo puede ser determinista y no estable.
- **Ordenar en el orden de significancia equivocado.** Con pasadas sucesivas se ordena primero por el criterio menos importante.
- **Dar por buena la comparación de texto.** El orden por punto de código no es el alfabético del español.

## Límites y cuándo no aplica

La estabilidad solo importa cuando hay claves iguales y el orden de los empates tiene significado. Si la clave es única, es irrelevante. Garantizarla puede costar memoria adicional o tiempo en algunos algoritmos. Y es un contrato de la implementación concreta: Python lo documenta para `sorted` y `list.sort`, pero otros lenguajes o bibliotecas de ordenamiento pueden no hacerlo, y depender de ello sin leer la documentación es el error que describe [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md).

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Búsqueda lineal y binaria](../b/busqueda-lineal-y-binaria.md), [Contrato de comparación](../c/contrato-de-comparacion.md), [Familias de ordenamiento](../f/familias-de-ordenamiento.md), [Selección parcial](../s/seleccion-parcial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (37 clases más lo mencionan; las que más):

[SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md), [SE-125](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-125-propuesta-de-valor-y-resultados-deseados/README.md), [SE-608](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-608-monitoreo-deriva-y-reentrenamiento/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), [SE-087](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md), [SE-095](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-095-taller-elegir-por-carga-y-no-por-costumbre/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: Sorting HOW TO](https://docs.python.org/3/howto/sorting.html) — estabilidad, claves y el orden total que se espera de `sorted`.
- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare.
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) — Semántica de secuencias, conjuntos, mappings, igualdad y hash; autoridad: Python Software Foundation.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Timeit, cprofile y tracemalloc con sus límites; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Esquema de datos](./esquema-de-datos.md) · [Estabilidad de segmentos →](./estabilidad-de-segmentos.md)
