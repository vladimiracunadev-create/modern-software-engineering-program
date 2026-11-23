# Contraejemplo mínimo

[↑ Glosario](../../README.md) · [← Contraejemplo](./contraejemplo.md) · [Contrafactual →](./contrafactual.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** B — Programación y construcción · **Primera aparición:** [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md)

## Definición

Cuando se propone una regla local, se busca la entrada más pequeña que la rompe.

Definición de trabajo de [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md).

## Por qué importa

En [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), el tema «Contraejemplo mínimo» importa porque cuando se propone una regla local, se busca la entrada más pequeña que la rompe.

## Cómo funciona

Según [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md), en la sección «Contraejemplo mínimo»:

Cuando se propone una regla local, se busca la entrada más pequeña que la rompe. Un contraejemplo no solo refuta: muestra qué interacción faltaba en el modelo. La biblioteca de estructuras y algoritmos conserva esos casos como pruebas y no los llama edge cases irrelevantes.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md):

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md)) son:

- **El cambio devuelto usa más monedas de las necesarias** — causa: voraz con un sistema de monedas no canónico. Corrección: usar DP o demostrar que el sistema es canónico.
- **El conteo de actividades es menor al esperado** — causa: criterio de orden equivocado (por inicio). Corrección: ordenar por fin y contrastar con fuerza bruta en casos pequeños.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md)) son: Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. La programación dinámica exige un estado finito y manejable. La siguiente clase estudia exploración, poda y descomposición cuando no basta llenar una tabla.

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Regla](../r/regla.md), [Estrategia voraz](../e/estrategia-voraz.md), [Memoización y tabulación](../m/memoizacion-y-tabulacion.md), [Reconstrucción de la solución](../r/reconstruccion-de-la-solucion.md), [Subproblemas superpuestos](../s/subproblemas-superpuestos.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-091 — Algoritmos voraces y programación dinámica](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-091-algoritmos-voraces-y-programacion-dinamica/README.md) — [Parte 07](../../../classes/part-07-estructuras-de-datos-y-algoritmos/README.md), Estructuras de datos y algoritmos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md).

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

[↑ Glosario](../../README.md) · [← Contraejemplo](./contraejemplo.md) · [Contrafactual →](./contrafactual.md)
