# Contrato de la biblioteca

[↑ Glosario](../../README.md) · [← Contrato de interfaz](./contrato-de-interfaz.md) · [Contrato de línea de comandos →](./contrato-de-linea-de-comandos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

El **contrato de la biblioteca** es, en el proyecto de [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), la API que fija **tipos, operaciones, errores, orden y complejidad esperada** de la biblioteca de estructuras y algoritmos. Es la frontera que separa lo que la biblioteca promete de la manera en que lo cumple por dentro. Todo candidato (lista, árbol, tabla hash) debe satisfacerlo, y quien consume la biblioteca solo puede apoyarse en él. En este programa «contrato» tiene el sentido de promesa verificable, la misma noción que desarrolla la entrada general sobre contratos.

## Por qué importa

Si el contrato no define un caso, cada implementación lo resuelve a su manera y nadie se entera hasta que dos de ellas difieren en producción. [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) da el ejemplo: dos implementaciones difieren cuando `lo > hi` porque el contrato no decía qué hacer con un rango invertido. La decisión que cambia es dónde se escribe el comportamiento en los bordes: en el contrato y en una prueba con nombre, no en la cabeza de quien implementó. Además, un contrato que expone la estructura interna impide **sustituirla** después.

## Cómo funciona

Un contrato útil cubre cinco dimensiones:

- **Tipos:** qué entra y qué sale, incluidos los valores especiales.
- **Operaciones:** qué se puede hacer y con qué efecto sobre el estado.
- **Errores:** qué falla, con qué excepción o valor, ante qué entrada.
- **Orden:** si el resultado tiene un orden garantizado, y cuál (por ejemplo, estable).
- **Complejidad esperada:** el costo que se promete.

Las garantías de costo se expresan **con supuestos**, no como promesa absoluta de latencia: «`O(log n)` si el árbol está equilibrado» o «`O(1)` esperado con una función hash razonable». Esto evita prometer lo que depende de la máquina o de los datos. Como todos los candidatos cumplen el mismo contrato, se pueden comparar y reemplazar; esa sustituibilidad es lo que el contrato compra.

## Ejemplo

El proyecto de [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) compara implementaciones sobre un corpus con casos límite y verifica cada una con un oráculo diferencial y con mutantes. Cuando dos implementaciones difieren con `lo > hi`, la corrección es decidir la regla y escribirla:

```python
def buscar_en_rango(estructura, lo, hi):
    """Devuelve las claves k con lo <= k <= hi, en orden ascendente.
    Si lo > hi devuelve una lista vacía (no lanza excepción).
    Complejidad esperada: O(log n + m), m = tamaño del resultado,
    si la estructura está equilibrada."""
```

Con esa regla, una prueba nombrada (`test_rango_invertido_vacio`) convierte el caso en parte del contrato. Sin el oráculo diferencial, el hecho de que todas las pruebas con ejemplos pasaran no habría revelado el defecto.

## Errores y confusiones comunes

- **Pruebas solo con ejemplos.** Pasan todas y un defecto llega a producción; se añade un oráculo diferencial con semillas y mutantes.
- **Dejar casos sin definir.** El comportamiento queda «por accidente» y cada implementación lo decide distinto.
- **Exponer la estructura interna.** Quien la usa queda atado a ella.
- **Prometer latencias.** Una complejidad con supuestos es honesta; un tiempo absoluto, no.

## Límites y cuándo no aplica

La biblioteca demuestra comportamiento en el corpus y protocolo declarados, no superioridad universal ([SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md)). Un contrato escrito no garantiza que se cumpla: necesita pruebas, y las pruebas solo cubren lo que se probó. Para código interno de un solo uso, un contrato formal puede ser exceso; se justifica cuando varias implementaciones o varios consumidores dependen de él. La [Parte 08](../../../classes/part-08-entornos-herramientas-y-depuracion/README.md) usará un fallo de esta biblioteca como material de diagnóstico.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Complejidad](./complejidad.md), [Operación](../o/operacion.md), [Tipo](../t/tipo.md), [Benchmark versionado](../b/benchmark-versionado.md), [Casos límite y oráculo](./casos-limite-y-oraculo.md), [Informe y decisión](../i/informe-y-decision.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-096 — Proyecto: biblioteca comparada con casos límite](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Contrato de interfaz](./contrato-de-interfaz.md) · [Contrato de línea de comandos →](./contrato-de-linea-de-comandos.md)
