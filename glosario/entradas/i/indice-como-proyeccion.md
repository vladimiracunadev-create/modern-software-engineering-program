# Índice como proyección

[↑ Glosario](../../README.md) · [← Índice](./indice.md) · [Índice compuesto →](./indice-compuesto.md)

> **Tipo:** métrica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Decir que un **índice es una proyección** es afirmar, con [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), que **todo índice duplica una vista derivada de los datos** y por eso **puede quedar desincronizado**. El índice no es la fuente de verdad: es una copia organizada para responder rápido a cierta consulta (por ejemplo, ordenada por una columna). La palabra «proyección» expresa que contiene una parte o una reorganización de la información original, calculada a partir de ella. Es un enfoque del programa para hablar de índices, no un término normalizado.

## Por qué importa

Los índices aceleran las consultas, y es fácil olvidar que tienen un costo y un riesgo. El costo: ocupan espacio y hay que actualizarlos en cada escritura. El riesgo: si el índice y los datos discrepan, las consultas indexadas devuelven resultados distintos que un recorrido completo, sin ningún error visible. La decisión que cambia es cómo se trata un índice: como una derivación cuya consistencia hay que **diseñar y comprobar**, no como una propiedad que se obtiene gratis al crearla.

## Cómo funciona

Para que un índice sea de fiar, tres cosas deben estar definidas ([SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)):

- **Quién lo actualiza:** el propio motor de la base de datos (en un índice de base de datos, de forma transaccional), o el código de la aplicación (en un índice en memoria que mantiene el programa). Si lo mantiene el código, cada ruta de escritura debe pasar por el mismo punto.
- **Cómo se reconstruye:** como es derivado, siempre debe poder recrearse desde los datos. Si no, un error no tiene remedio.
- **Qué ocurre ante un fallo parcial:** si la escritura de datos tuvo éxito y la del índice falló (o al revés), ¿qué estado queda y cómo se detecta?

La biblioteca de estructuras y algoritmos del programa **prueba equivalencia** entre la consulta indexada y el escaneo completo en conjuntos de prueba pequeños: ambos caminos deben devolver lo mismo. Esa prueba es la forma práctica de verificar que la proyección representa a los datos.

## Ejemplo

Un índice en memoria que asocia identificador de caso con posición. Si se borra un caso de la lista pero no del índice, la consulta indexada devuelve una posición obsoleta. La prueba de equivalencia lo detecta:

```python
def test_indice_equivale_a_escaneo(casos, indice):
    for clave in claves_de_prueba:
        por_indice = indice.get(clave)
        por_escaneo = next((c for c in casos if c.id == clave), None)
        assert por_indice == por_escaneo
```

[SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) documenta además un síntoma asociado: la consulta sigue lenta tras crear el índice porque la selectividad es baja o el planificador no lo usa; se lee `EXPLAIN QUERY PLAN` y se mide con y sin índice. El índice puede existir y no usarse: crearlo no basta.

## Errores y confusiones comunes

- **Tratar el índice como fuente de verdad.** Es derivado; ante discrepancia, mandan los datos.
- **Actualizarlo desde varios lugares.** Aumenta la probabilidad de olvidar uno.
- **Suponer que se usará.** El planificador puede ignorarlo si no es selectivo.
- **No medir.** Sin comparar con y sin índice, no se sabe si ayuda.

## Límites y cuándo no aplica

Una garantía teórica no predice constantes, asignaciones ni la distribución real de los datos ([SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md)). Para tablas pequeñas, un escaneo completo es más rápido que consultar un índice. Si la carga es de muchas escrituras y pocas lecturas, el costo de mantener el índice puede superar su beneficio. En bases de datos que mantienen los índices transaccionalmente, el riesgo de desincronización es menor, pero el costo de espacio y de escritura sigue ahí.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Índice](./indice.md), [Vista](../v/vista.md), [Bloom filter](../b/bloom-filter.md), [Estructuras persistentes](../e/estructuras-persistentes.md), [Índices ordenados y consultas de rango](./indices-ordenados-y-consultas-de-rango.md), [Sketches y aproximación](../s/sketches-y-aproximacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-093 — Índices, probabilísticas y estructuras persistentes](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Índice](./indice.md) · [Índice compuesto →](./indice-compuesto.md)
