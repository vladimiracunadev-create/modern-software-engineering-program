# Benchmark versionado

[↑ Glosario](../../README.md) · [← Benchmark](./benchmark.md) · [BFF →](./bff.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Un **benchmark versionado** es, en [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), una medición de rendimiento que se trata como un artefacto del proyecto: un *runner* que separa la preparación de la operación medida, verifica que las salidas sean correctas, registra el entorno y emite datos estructurados, todo bajo control de versiones. «Versionado» se refiere a dos cosas: el código del benchmark y los datos que produce, de modo que un número pueda atribuirse a una versión concreta del programa, del corpus y de la máquina. El término lo usa el programa en su proyecto de biblioteca comparada; no es un nombre estándar de la industria.

## Por qué importa

Un número de tiempo suelto no es evidencia: no se sabe en qué máquina, con qué datos, ni si el código medido era correcto. Un benchmark que cambia sin dejar rastro hace imposible saber si una mejora es real o producto de otro corpus. La decisión que cambia es qué se cita al justificar una estructura o un algoritmo: ya no «es más rápido», sino «en este corpus, con este protocolo y este entorno, la mediana fue X». Esto sostiene el informe y la recomendación que cierran el proyecto.

## Cómo funciona

El runner se organiza por responsabilidad:

- **Preparación fuera del tiempo medido.** Construir los datos, calentar y crear estructuras no se cuenta como operación; solo se cronometra la operación bajo estudio.
- **Verificación de resultados.** Cada ejecución comprueba que la salida coincide con un oráculo o con otra implementación. Un algoritmo rápido que devuelve respuestas erróneas no es una mejora.
- **Registro del entorno.** Versión del lenguaje, sistema operativo, procesador y semillas, para poder comparar con criterio.
- **Salida estructurada.** Un formato legible por máquina (JSON, CSV) con repeticiones y estadística, no solo un texto impreso.
- **Umbrales prudentes.** Entre máquinas distintas los tiempos absolutos no se comparan; [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) recomienda fijar tendencias o presupuestos cuando sean defendibles, en lugar de prometer tiempos exactos que una máquina más lenta rompería sin que el código cambie.

Como los datos están versionados junto con el código, una regresión se detecta comparando la medición nueva con la anterior bajo el mismo protocolo.

## Ejemplo

En la biblioteca de estructuras y algoritmos de [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md), el benchmark compara implementaciones sobre un corpus con casos límite (vacío, un elemento, duplicados, orden inverso). El runner guarda en cada ejecución la versión del código, el corpus y el entorno, y emite una fila por caso. Una verificación diferencial con semillas detecta que dos implementaciones difieren cuando `lo > hi`; la causa es un contrato que no define ese caso, y la corrección es escribir la regla en el contrato y una prueba con nombre. Ilustración de un registro (formato inventado para el ejemplo):

```json
{"version": "1.4.0", "corpus": "v3", "caso": "orden-inverso",
 "n": 10000, "mediana_ms": 12.4, "python": "3.12", "ok": true}
```

## Errores y confusiones comunes

- **Medir la preparación con la operación.** Infla el tiempo y mezcla causas.
- **No verificar la salida.** Se premia código incorrecto.
- **Comparar tiempos absolutos entre máquinas.** Solo son comparables dentro del mismo entorno registrado.
- **Pruebas solo con ejemplos felices.** [SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) añade un oráculo diferencial con semillas y mutantes para que un defecto no llegue a producción con todas las pruebas en verde.

## Límites y cuándo no aplica

La biblioteca demuestra comportamiento en el corpus y el protocolo declarados, no superioridad universal ([SE-096](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md)). Un benchmark de laboratorio no sustituye medir en producción con carga real, y datos sintéticos pueden no reflejar la distribución del uso. Para código que se ejecuta pocas veces, medir y versionar puede costar más que el ahorro posible; el rigor se justifica cuando una decisión depende del resultado.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Entorno](../e/entorno.md), [Operación](../o/operacion.md), [Producción](../p/produccion.md), [Casos límite y oráculo](../c/casos-limite-y-oraculo.md), [Contrato de la biblioteca](../c/contrato-de-la-biblioteca.md), [Informe y decisión](../i/informe-y-decision.md).
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

[↑ Glosario](../../README.md) · [← Benchmark](./benchmark.md) · [BFF →](./bff.md)
