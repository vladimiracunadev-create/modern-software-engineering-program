# SE-086 — Pilas, colas, deques y prioridades

[← SE-085 — Arreglos, listas y secuencias](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-086.html) · [SE-087 — Tablas hash, mapas y conjuntos →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md)

> Estado: **GUIDED** · Clase desarrollada y revisada cualitativamente.

## Antes de empezar

Esta clase continúa **Orbe**, el caso conductor de la Parte 07. Recupera la evidencia de la clase anterior, añade una decisión propia de **Pilas, colas, deques y prioridades** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo cambia el comportamiento cuando la estructura impone LIFO, FIFO o prioridad?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Orbe mezcla trabajo urgente, reintentos y navegación de historial en una lista. El mismo método inserta en posiciones distintas y nadie puede afirmar qué caso saldrá después.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Pila / disciplina LIFO] --> N2[Cola / disciplina FIFO] --> N3[Deque / ventanas] --> N4[Heap / prioridad parcial] --> N5[Starvation / envejecimiento]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Pila y disciplina LIFO | Una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir. | Evidencia o contraejemplo registrado |
| Cola y disciplina FIFO | Una cola conserva llegada entre elementos de la misma clase. | Evidencia o contraejemplo registrado |
| Deque y ventanas | La cola doble inserta y retira en ambos extremos; sirve para ventanas deslizantes y work stealing bajo contratos específicos. | Evidencia o contraejemplo registrado |
| Heap y prioridad parcial | Un heap mantiene el mínimo o máximo en la raíz y una propiedad local entre padre e hijos; no mantiene toda la colección ordenada. | Evidencia o contraejemplo registrado |
| Starvation y envejecimiento | Prioridad estricta puede posponer indefinidamente trabajo bajo. | Evidencia o contraejemplo registrado |

## Conceptos y decisiones

### 1. Pila y disciplina LIFO

Una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir. Modela deshacer, marcos y exploración en profundidad. Buscar arbitrariamente dentro rompe la abstracción y suele indicar que la carga necesita otra estructura.

### 2. Cola y disciplina FIFO

Una cola conserva llegada entre elementos de la misma clase. FIFO no garantiza equidad si un trabajo nunca termina ni si existen varias colas. `deque` permite extremos eficientes, pero operaciones interiores siguen otro costo.

### 3. Deque y ventanas

La cola doble inserta y retira en ambos extremos; sirve para ventanas deslizantes y work stealing bajo contratos específicos. No equivale a un arreglo con acceso aleatorio constante en toda posición. El límite máximo puede descartar elementos y debe hacerse visible.

### 4. Heap y prioridad parcial

Un heap mantiene el mínimo o máximo en la raíz y una propiedad local entre padre e hijos; no mantiene toda la colección ordenada. Insertar y extraer cuestan logarítmico, consultar la raíz constante. Empates requieren una clave estable para evitar comparar cargas incompatibles.

### 5. Starvation y envejecimiento

Prioridad estricta puede posponer indefinidamente trabajo bajo. Aging aumenta prioridad con espera o reserva capacidad por clase. Esa política pertenece al dominio y modifica qué significa correcto, no es un detalle de optimización.

## Definiciones de trabajo

- **pila y disciplina lifo:** una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir.
- **cola y disciplina fifo:** una cola conserva llegada entre elementos de la misma clase.
- **deque y ventanas:** la cola doble inserta y retira en ambos extremos; sirve para ventanas deslizantes y work stealing bajo contratos específicos.
- **heap y prioridad parcial:** un heap mantiene el mínimo o máximo en la raíz y una propiedad local entre padre e hijos; no mantiene toda la colección ordenada.
- **starvation y envejecimiento:** prioridad estricta puede posponer indefinidamente trabajo bajo.

Las definiciones son operativas para Orbe. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
import heapq
queue = []
heapq.heappush(queue, (10, 0, "case-old"))
heapq.heappush(queue, (5, 1, "case-urgent"))
assert heapq.heappop(queue)[2] == "case-urgent"
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En Orbe, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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

Orbe recibe casos de Prisma, mantiene una frontera de trabajo priorizada y explica por qué el siguiente caso es elegible. Ejecuta una carga pequeña trazable, duplicados, prioridades iguales y una dependencia ausente. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Un paradigma determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar modelos es válido si los adaptadores preservan identidad, orden, errores y evidencia.

### ¿Menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todos los lenguajes mencionados?

No. Python basta para la práctica base. Si usas Prolog, Rust o Erlang, registra versión y comandos; si solo analizas notación, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Usa `(priority, payload)` y crea dos prioridades iguales cuyos payloads no son comparables. Añade contador estable y prueba que el desempate respeta llegada.

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
work/SE-086/
├── README.md
├── orbe/
│   ├── domain.py
│   └── se_086.py
├── fixtures/cases.json
├── tests/test_se_086.py
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

Los snippets no elevan la clase a `EXECUTABLE` o `TESTED`: esos estados requieren artefactos versionados y ejecuciones verificadas fuera de la guía.

## Fuentes

- [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare.
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html) — Semántica de secuencias, conjuntos, mappings, igualdad y hash; autoridad: Python Software Foundation.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Deque, heapq, bisect, graphlib y contenedores disponibles; autoridad: Python Software Foundation.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Timeit, cprofile y tracemalloc con sus límites; autoridad: Python Software Foundation.
- [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — Construcción, medición y fundamentos de ingeniería; autoridad: IEEE Computer Society.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación de Orbe sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

Una cola responde cuál sale después, no cómo encontrar identidad ni evitar duplicados. La siguiente clase añade mapas y conjuntos con contratos de igualdad y hash.

## Glosario

- **pila y disciplina lifo:** una pila expone `push`, `pop` y `peek`; el último elemento entra primero en salir.
- **cola y disciplina fifo:** una cola conserva llegada entre elementos de la misma clase.
- **deque y ventanas:** la cola doble inserta y retira en ambos extremos; sirve para ventanas deslizantes y work stealing bajo contratos específicos.
- **heap y prioridad parcial:** un heap mantiene el mínimo o máximo en la raíz y una propiedad local entre padre e hijos; no mantiene toda la colección ordenada.
- **starvation y envejecimiento:** prioridad estricta puede posponer indefinidamente trabajo bajo.

---

[← SE-085 — Arreglos, listas y secuencias](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-085-arreglos-listas-y-secuencias/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-086.html) · [SE-087 — Tablas hash, mapas y conjuntos →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md)
