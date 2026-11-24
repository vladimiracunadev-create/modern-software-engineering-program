# Contrato de comparación

[↑ Glosario](../../README.md) · [← Contrato de bootstrap](./contrato-de-bootstrap.md) · [Contrato de consumidor →](./contrato-de-consumidor.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

El **contrato de comparación** es el conjunto de propiedades que una relación de orden debe cumplir para que ordenar tenga sentido. [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) lo enuncia así: ordenar requiere una relación **consistente**, normalmente **total**, o una **clave total derivada** a partir de los datos. Importan la antisimetría, la transitividad y el tratamiento de los iguales. Quien pasa un comparador o una clave a un algoritmo de ordenamiento está firmando este contrato, aunque el lenguaje no lo compruebe.

## Por qué importa

Los algoritmos de ordenamiento se demuestran correctos **bajo el supuesto** de que la comparación es un orden bien definido. Si el supuesto falla, el resultado deja de estar garantizado: puede quedar «ordenado» sin estarlo, o variar según el algoritmo o la versión del lenguaje, sin ningún error visible. La decisión que cambia es dónde se invierte la atención al ordenar: no solo en elegir el algoritmo, sino en definir y probar la relación. La mayoría de los defectos de ordenamiento viven en el comparador, no en el algoritmo.

## Cómo funciona

Las propiedades exigidas, para elementos `a`, `b`, `c`:

- **Total:** para todo par, `a ≤ b` o `b ≤ a`. Si hay pares incomparables, no hay orden total.
- **Antisimétrica:** si `a ≤ b` y `b ≤ a`, entonces son iguales según el criterio.
- **Transitiva:** si `a ≤ b` y `b ≤ c`, entonces `a ≤ c`.
- **Iguales definidos:** qué pasa con elementos equivalentes (¿se conserva su orden original? Un ordenamiento **estable** lo garantiza).

Los problemas reales vienen de datos que violan estas propiedades. Los valores no numéricos de punto flotante (`NaN`) no son menores, mayores ni iguales a nada, así que rompen la totalidad. Fechas sin zona horaria pueden representar instantes distintos con la misma etiqueta; valores ausentes (`None`) no se comparan con números. Por eso [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) indica que deben **normalizarse antes del comparador**: se construye una **clave total derivada** (por ejemplo, la fecha en UTC y la ausencia convertida a un valor definido) y se ordena por ella.

## Ejemplo

En [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), un resultado «ordenado» que no lo está tiene como causa la presencia de `NaN` o un comparador no transitivo, y la corrección es normalizar el criterio y verificar con una prueba de orden total. Ilustración:

```python
datos = [3.0, float("nan"), 1.0, 2.0]
sorted(datos)          # el resultado depende de dónde cae el NaN

def clave(x):          # clave total derivada: NaN al final, de forma explícita
    return (x != x, x if x == x else 0.0)
sorted(datos, key=clave)   # [1.0, 2.0, 3.0, nan]
```

Una prueba de orden total comprueba, sobre un conjunto de muestras, que para todo par se cumpla la totalidad y para toda terna la transitividad; falla si el comparador las rompe.

## Errores y confusiones comunes

- **Comparador que devuelve «menor» en un sentido y en el otro.** Viola la antisimetría y puede hacer entrar en bucle a algunos algoritmos.
- **Restar para comparar.** `a - b` puede desbordar o redondear en flotantes y producir inconsistencias.
- **Ignorar los ausentes y los `NaN`.** Rompen la totalidad sin error evidente.
- **Esperar estabilidad sin pedirla.** Si se necesita conservar el orden de iguales, hay que usar un algoritmo estable o añadir un desempate explícito.

## Límites y cuándo no aplica

Elegir los *k* mejores no resuelve decisiones secuenciales con subproblemas o restricciones; ahí la relación de orden no basta y se pasa a estrategias voraces o programación dinámica ([SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)). Para órdenes parciales (dependencias entre tareas) se usa ordenamiento topológico, no un comparador. Y si el orden depende de contexto cambiante (preferencias del usuario), no existe un contrato único estable.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Relación](../r/relacion.md), [Búsqueda lineal y binaria](../b/busqueda-lineal-y-binaria.md), [Estabilidad](../e/estabilidad.md), [Familias de ordenamiento](../f/familias-de-ordenamiento.md), [Selección parcial](../s/seleccion-parcial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-090 — Búsqueda, ordenamiento y selección](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Contrato de bootstrap](./contrato-de-bootstrap.md) · [Contrato de consumidor →](./contrato-de-consumidor.md)
