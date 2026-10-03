# SE-093 — Índices, probabilísticas y estructuras persistentes

[← SE-092 — Backtracking, divide y vencerás](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-093.html) · [SE-094 — Complejidad empírica, benchmarks y perfiles →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md)

> Estado: **GUIDED** · Clase desarrollada y revisada cualitativamente.

## Antes de empezar

Esta clase continúa **Orbe**, el caso conductor de la Parte 07. Recupera la evidencia de la clase anterior, añade una decisión propia de **Índices, probabilísticas y estructuras persistentes** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué garantía se intercambia al usar un índice especializado, probabilidad o versiones persistentes?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Orbe consulta rangos temporales, filtra millones de IDs vistos y necesita conservar snapshots auditables. Una sola tabla hash no satisface rango, memoria y versión al mismo tiempo.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Índices ordenados / consultas de rango] --> N2[Bloom filter] --> N3[Sketches / aproximación] --> N4[Estructuras persistentes] --> N5[Índice como proyección]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Índices ordenados y consultas de rango | Un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo. | Evidencia o contraejemplo registrado |
| Bloom filter | Un Bloom filter marca varios bits por elemento. | Evidencia o contraejemplo registrado |
| Sketches y aproximación | Estructuras de resumen estiman frecuencia o cardinalidad con memoria acotada. | Evidencia o contraejemplo registrado |
| Estructuras persistentes | Una actualización produce nueva versión compartiendo partes inmutables con la anterior. | Evidencia o contraejemplo registrado |
| Índice como proyección | Todo índice duplica una vista derivada y puede quedar desincronizado. | Evidencia o contraejemplo registrado |

## Conceptos y decisiones

### 1. Índices ordenados y consultas de rango

Un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo. Mantenerlo encarece escritura y requiere coherencia con la fuente. `bisect` encuentra posición logarítmica en una lista, pero insertar sigue siendo lineal por desplazamiento.

### 2. Bloom filter

Un Bloom filter marca varios bits por elemento. Puede afirmar `posiblemente presente` o `definitivamente ausente`: admite falsos positivos, no falsos negativos bajo operación correcta sin borrado. Tamaño, hashes y tasa esperada deben calcularse para la carga.

### 3. Sketches y aproximación

Estructuras de resumen estiman frecuencia o cardinalidad con memoria acotada. El error es parte del contrato e incluye probabilidad y cota. No sirven cuando una decisión individual exige exactitud o derecho de corrección.

### 4. Estructuras persistentes

Una actualización produce nueva versión compartiendo partes inmutables con la anterior. Persistente aquí significa conservar versiones, no necesariamente guardar en disco. Compartir reduce copia pero retiene memoria mientras haya referencias a raíces antiguas.

### 5. Índice como proyección

Todo índice duplica una vista derivada y puede quedar desincronizado. Se define quién lo actualiza, cómo se reconstruye y qué ocurre ante fallo parcial. Orbe prueba equivalencia entre consulta indexada y escaneo para fixtures pequeños.

## Definiciones de trabajo

- **índices ordenados y consultas de rango:** un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo.
- **bloom filter:** un bloom filter marca varios bits por elemento.
- **sketches y aproximación:** estructuras de resumen estiman frecuencia o cardinalidad con memoria acotada.
- **estructuras persistentes:** una actualización produce nueva versión compartiendo partes inmutables con la anterior.
- **índice como proyección:** todo índice duplica una vista derivada y puede quedar desincronizado.

Las definiciones son operativas para Orbe. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
from bisect import bisect_left
timestamps = [10, 20, 35, 50]
start = bisect_left(timestamps, 20)
end = bisect_left(timestamps, 50)
assert timestamps[start:end] == [20, 35]
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

Interpreta `possibly present` de Bloom como confirmación y omite una escritura necesaria. Usa el filtro solo para descartar ausentes y confirma positivos contra la fuente exacta.

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
work/SE-093/
├── README.md
├── orbe/
│   ├── domain.py
│   └── se_093.py
├── fixtures/cases.json
├── tests/test_se_093.py
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

Una garantía teórica no predice constantes, asignaciones ni distribución real. La siguiente clase diseña medición empírica y perfilado sin sesgos obvios.

## Glosario

- **índices ordenados y consultas de rango:** un índice ordenado localiza fronteras y recorre un intervalo sin escanear todo.
- **bloom filter:** un bloom filter marca varios bits por elemento.
- **sketches y aproximación:** estructuras de resumen estiman frecuencia o cardinalidad con memoria acotada.
- **estructuras persistentes:** una actualización produce nueva versión compartiendo partes inmutables con la anterior.
- **índice como proyección:** todo índice duplica una vista derivada y puede quedar desincronizado.

---

[← SE-092 — Backtracking, divide y vencerás](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-092-backtracking-divide-y-venceras/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-093.html) · [SE-094 — Complejidad empírica, benchmarks y perfiles →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md)
