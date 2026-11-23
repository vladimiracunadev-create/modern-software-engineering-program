# Warm-up, caché y aislamiento

[↑ Glosario](../../README.md) · [← Warm-up](./warm-up.md) · [Warp →](./warp.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Importación, jit, page cache y asignadores cambian primeras corridas.

Definición de trabajo de [SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md).

## Por qué importa

En [SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), el tema «Warm-up, caché y aislamiento» importa porque importación, JIT, page cache y asignadores cambian primeras corridas.

## Cómo funciona

Según [SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), en la sección «Warm-up, caché y aislamiento»:

Importación, JIT, page cache y asignadores cambian primeras corridas. Aleatorizar orden reduce sesgo, pero caches también son parte de algunas cargas reales. El protocolo declara qué se calienta y qué se reinicia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md)) son:

- **Dos ejecuciones dan conclusiones opuestas** — causa: una sola pasada sin estimar el ruido. Corrección: repetir, usar mínimo o mediana y reportar la dispersión.
- **La operación «constante» resulta gratis** — causa: plegado de constantes o código muerto. Corrección: usar variables o datos opacos y verificar con una operación conocida.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La medición local no demuestra latencia productiva ni causalidad por sí sola. El taller siguiente usa una matriz de cargas y fuerza decisiones distintas.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Corrida](../c/corrida.md), [Importación](../i/importacion.md), [Comparabilidad y reporte](../c/comparabilidad-y-reporte.md), [Modelo de costo y pregunta](../m/modelo-de-costo-y-pregunta.md), [Perfil y atribución](../p/perfil-y-atribucion.md), [Reloj, repetición y distribución](../r/reloj-repeticion-y-distribucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-094 — Complejidad empírica, benchmarks y perfiles](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

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

[↑ Glosario](../../README.md) · [← Warm-up](./warm-up.md) · [Warp →](./warp.md)
