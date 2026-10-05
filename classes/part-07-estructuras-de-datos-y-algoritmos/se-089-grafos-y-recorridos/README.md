# SE-089 — Grafos y recorridos

[← SE-088 — Árboles, tries y estructuras jerárquicas](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-089.html) · [SE-090 — Búsqueda, ordenamiento y selección →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para representar relaciones como grafos y elegir recorrido por la pregunta que se responde.

**Por qué aparece aquí.** Se sitúa después de **Árboles, tries y estructuras jerárquicas** y antes de **Búsqueda, ordenamiento y selección**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Usar BFS o DFS por costumbre sin definir visitados y dirección.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Graph-trace.md con frontera, visitados, camino y ciclo. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Un recorrido no resuelve automáticamente pesos ni restricciones.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Python Standard Library](https://docs.python.org/3/library/index.html) | Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa la **biblioteca de estructuras y algoritmos de la Parte 07**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Grafos y recorridos** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo explorar relaciones arbitrarias sin perder visitados, distancia ni causa del camino?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Un caso de la biblioteca de estructuras y algoritmos depende de varios servicios y una falla puede propagarse por rutas distintas. La jerarquía única ya no representa el dominio y un recorrido sin conjunto de visitados entra en ciclo.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Vértices, aristas / dirección] --> N2[Lista / matriz de adyacencia] --> N3[BFS / distancia no ponderada] --> N4[DFS, ciclos / orden] --> N5[Componentes / alcanzabilidad]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Vértices, aristas y dirección | Un grafo modela entidades y relaciones. | Predicción, traza causal y contraejemplo de **Vértices, aristas y dirección** en `graph-trace.md` |
| Lista y matriz de adyacencia | Una lista almacena vecinos y favorece grafos dispersos; una matriz permite consultar arista directa de forma constante a costo cuadrático de espacio. | Predicción, traza causal y contraejemplo de **Lista y matriz de adyacencia** en `graph-trace.md` |
| BFS y distancia no ponderada | BFS usa cola y descubre por capas; el primer camino hallado tiene menos aristas en un grafo no ponderado. | Predicción, traza causal y contraejemplo de **BFS y distancia no ponderada** en `graph-trace.md` |
| DFS, ciclos y orden | DFS usa pila implícita o explícita y profundiza antes de retroceder. | Predicción, traza causal y contraejemplo de **DFS, ciclos y orden** en `graph-trace.md` |
| Componentes y alcanzabilidad | Alcanzabilidad responde si existe camino; componentes agrupan conectividad bajo definición dirigida o no dirigida. | Predicción, traza causal y contraejemplo de **Componentes y alcanzabilidad** en `graph-trace.md` |
## Conceptos y decisiones

### 1. Vértices, aristas y dirección

Un grafo modela entidades y relaciones. Dirección, peso, multiplicidad y autoaristas cambian las preguntas admisibles. Dibujar flechas sin definir su significado impide distinguir `depende de` de `impacta a`.

### 2. Lista y matriz de adyacencia

Una lista almacena vecinos y favorece grafos dispersos; una matriz permite consultar arista directa de forma constante a costo cuadrático de espacio. La densidad y operaciones, no el tamaño aislado, guían la representación.

### 3. BFS y distancia no ponderada

BFS usa cola y descubre por capas; el primer camino hallado tiene menos aristas en un grafo no ponderado. Si pesos importan, esa garantía deja de valer. Registrar predecesor permite reconstruir explicación, no solo distancia.

### 4. DFS, ciclos y orden

DFS usa pila implícita o explícita y profundiza antes de retroceder. Colores o estados distinguen no visto, activo y terminado para detectar ciclos dirigidos. Un conjunto visitado simple puede perder la diferencia necesaria para explicar un back edge.

### 5. Componentes y alcanzabilidad

Alcanzabilidad responde si existe camino; componentes agrupan conectividad bajo definición dirigida o no dirigida. En dependencias, estar en la misma componente no implica impacto simétrico. La biblioteca de estructuras y algoritmos etiqueta la relación y conserva el camino que sostiene la conclusión.

## Definiciones de trabajo

- **vértices, aristas y dirección:** un grafo modela entidades y relaciones.
- **lista y matriz de adyacencia:** una lista almacena vecinos y favorece grafos dispersos; una matriz permite consultar arista directa de forma constante a costo cuadrático de espacio.
- **bfs y distancia no ponderada:** bfs usa cola y descubre por capas; el primer camino hallado tiene menos aristas en un grafo no ponderado.
- **dfs, ciclos y orden:** dfs usa pila implícita o explícita y profundiza antes de retroceder.
- **componentes y alcanzabilidad:** alcanzabilidad responde si existe camino; componentes agrupan conectividad bajo definición dirigida o no dirigida.

Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
from collections import deque
graph = {"api": ["auth", "db"], "auth": ["db"], "db": []}
queue, seen = deque(["api"]), {"api"}
while queue:
    node = queue.popleft()
    for nxt in graph[node]:
        if nxt not in seen:
            seen.add(nxt); queue.append(nxt)
assert seen == {"api", "auth", "db"}
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

Compara el caso normal con autorización falsa, evidencia incompleta, empate y repetición. Un mecanismo es apropiado cuando esas diferencias quedan visibles y localizadas; es peligroso cuando dependen de orden accidental, estado oculto o una convención que el consumidor no puede conocer.

## Práctica guiada

1. Copia el contrato de entrada y salida antes de escribir implementación.
2. Predice el caso normal y un límite; identifica la invariante que no puede romperse.
3. Implementa la versión mínima sin I/O dentro del núcleo.
4. Ejecuta el caso y conserva comando, versión y salida bajo `evidence/`.
5. Introduce el fallo controlado, reduce la reproducción y formula dos hipótesis rivales.
6. Corrige la causa, añade regresión y ejecuta el conjunto completo.
7. Compara con otro paradigma o lenguaje indicando qué semántica se preserva.

## Ejercicios

1. **Lectura:** dibuja una traza de cinco pasos y marca dónde cambia estado o control.
2. **Construcción:** añade una operación dominante y demuestra la invariante que conserva.
3. **Frontera:** cubre vacío, empate, no autorizado e inválido con resultados distintos.
4. **Contraste:** reescribe una pieza con otro modelo y explica una mejora y una pérdida.

## Reto verificable

Entrega implementación, fixtures, pruebas y un informe corto. Se aprueba si otra persona ejecuta desde checkout limpio, obtiene los mismos resultados y puede relacionar cada rama o transformación con una regla del dominio. No se aprueba por cantidad de archivos ni por usar la sintaxis característica del paradigma.

## Caso conductor

La biblioteca de estructuras y algoritmos recibe casos del motor de reglas comparado, mantiene una frontera de trabajo priorizada y explica por qué el siguiente caso es elegible. Ejecuta una carga pequeña trazable, duplicados, prioridades iguales y una dependencia ausente. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Un paradigma determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar modelos es válido si los adaptadores preservan identidad, orden, errores y evidencia.

### ¿Menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todos los lenguajes mencionados?

No. Python basta para la práctica base. Si usas Prolog, Rust o Erlang, registra versión y comandos; si solo analizas notación, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Añade `db -> api` y elimina `seen`. Reduce el caso hasta tres nodos, restaura el conjunto y prueba que cada vértice se procesa una vez.

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. No cambies simultáneamente implementación, fixture y expectativa.

## Errores comunes y cómo corregirlos

| Síntoma | Causa probable | Corrección |
|---|---|---|
| dos pruebas aisladas pasan y juntas fallan | estado o dependencia compartida | aislar propietario y reiniciar fixture |
| implementación corta pero opaca | semántica delegada sin contrato | documentar transición, error y orden |
| modelos “equivalentes” divergen | fixtures normalizan diferencias reales | comparar contrato antes de presentación |
| reintento duplica resultado | efecto sin identidad ni idempotencia | correlacionar y probar repetición |
| diagrama y código cuentan historias distintas | visual ornamental o desactualizado | trazar el mismo caso en ambos |

## Entorno y archivos clave

```text
work/SE-089/
├── README.md
├── algorithm_library/
│   ├── domain.py
│   └── se_089.py
├── fixtures/cases.json
├── tests/test_se_089.py
└── evidence/diagnosis.md
```

El `README` declara plataforma, runtimes, comandos, limpieza y límites. Evita dependencias externas cuando la biblioteca estándar permita observar el mecanismo; si agregas una, fija procedencia y versión.

## Seguridad, ética y accesibilidad

- la autorización forma parte del dominio y no se infiere por ausencia de rechazo;
- no uses `eval`, reglas descargadas ni serialización insegura;
- limita colas, recursión, tamaño de entrada y tiempo de evaluación;
- redacta trazas y conserva una explicación textual además de color o animación;
- una recomendación automatizada debe poder revisarse, impugnarse y corregirse;
- respeta licencias de ejemplos y atribuye adaptaciones.

## Transferencia

Traslada un fixture al segundo modelo o lenguaje. Compara representación de ausencia, error, mutabilidad, orden y cancelación. La transferencia está lograda cuando el contrato se conserva y las diferencias están explicadas, no cuando la sintaxis se parece.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
|---|---|
| comprensión | explicación causal de los cinco mecanismos |
| corrección | normal, límite, inválido y contraejemplo |
| diseño | estado, efectos y contrato localizables |
| diagnóstico | reproducción mínima y regresión |
| transferencia | comparación semántica, no estética |
| reproducibilidad | versiones, comandos, salida y límites |


## Fuentes


- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare.
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) — Semántica de secuencias, conjuntos, mappings, igualdad y hash; autoridad: Python Software Foundation.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Timeit, cprofile y tracemalloc con sus límites; autoridad: Python Software Foundation.
- [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — Construcción, medición y fundamentos de ingeniería; autoridad: IEEE Computer Society.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación de la biblioteca de estructuras y algoritmos sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

BFS no resuelve pesos negativos ni toda forma de optimización de caminos. La siguiente clase contrasta búsqueda, ordenamiento y selección bajo contratos precisos.

## Glosario

- **vértices, aristas y dirección:** un grafo modela entidades y relaciones.
- **lista y matriz de adyacencia:** una lista almacena vecinos y favorece grafos dispersos; una matriz permite consultar arista directa de forma constante a costo cuadrático de espacio.
- **bfs y distancia no ponderada:** bfs usa cola y descubre por capas; el primer camino hallado tiene menos aristas en un grafo no ponderado.
- **dfs, ciclos y orden:** dfs usa pila implícita o explícita y profundiza antes de retroceder.
- **componentes y alcanzabilidad:** alcanzabilidad responde si existe camino; componentes agrupan conectividad bajo definición dirigida o no dirigida.

---

[← SE-088 — Árboles, tries y estructuras jerárquicas](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-089.html) · [SE-090 — Búsqueda, ordenamiento y selección →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md)
