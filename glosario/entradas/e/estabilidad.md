# Estabilidad

[↑ Glosario](../../README.md) · [← Esquema de datos](./esquema-de-datos.md) · [Estabilidad de segmentos →](./estabilidad-de-segmentos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un sort estable conserva orden relativo entre claves iguales.

Definición de trabajo de [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md).

## Por qué importa

En [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), el tema «Estabilidad» importa porque un sort estable conserva orden relativo entre claves iguales.

## Cómo funciona

Según [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), en la sección «Estabilidad»:

Un sort estable conserva orden relativo entre claves iguales. Permite ordenar por varias claves en pasadas o preservar llegada como desempate. Si la estabilidad no está garantizada, depender de ella convierte presentación en comportamiento accidental.

## Ejemplo

Caso medido en la sección «Trampas del orden: estabilidad, NaN y tipos» de [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md):

`sorted(registros, key=prioridad)` con registros `[('b',1),('a',1),('c',0),('d',1),('e',0)]` devolvió `['c','e','b','a','d']`: los empates conservaron el orden de llegada (b antes de a), porque el ordenamiento es estable. Esa propiedad permite ordenar por varios criterios aplicando sorts sucesivos, del menos al más significativo. Tres trampas se midieron: `sorted([3.0, nan, 1.0, 2.0])` devolvió `[3.0, nan, 1.0, 2.0]`, es decir, no ordenó nada, porque NaN rompe el orden total (toda comparación con NaN es falsa); `sorted([1, 'a'])` lanza `TypeError`; y `sorted(['Zebra','apple','Árbol','zeta'])` dio `['Zebra','apple','zeta','Árbol']`, orden por punto de código, no alfabético del español.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los empates cambian de orden entre versiones** — causa: se supuso estabilidad en una estructura que no la garantiza. Corrección: ordenar con `sorted` (estable) o añadir un desempate explícito. ([SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Si la estabilidad no está garantizada, depender de ella convierte presentación en comportamiento accidental. ([SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md))

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
