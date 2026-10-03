# SE-099 — Profilers de CPU, memoria, I/O y red

[← SE-098 — Depuradores, breakpoints y observación de estado](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-099.html) · [SE-100 — Compiladores, linters, formatters y análisis estático →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md)

> Estado: **GUIDED** · Clase desarrollada y revisada cualitativamente.

## Antes de empezar

Esta clase continúa **Lupa**, el caso conductor de la Parte 08. Recupera la evidencia de la clase anterior, añade una decisión propia de **Profilers de CPU, memoria, I/O y red** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué recurso está realmente saturado y qué herramienta puede atribuirlo?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Orbe se siente lento. El equipo optimiza CPU, pero el perfil revela espera de disco al registrar cada evento y memoria retenida por snapshots antiguos.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Tiempo de pared / CPU] --> N2[Perfil determinista / muestreo] --> N3[Asignaciones, retención / pico] --> N4[I/O / red] --> N5[Perfil como hipótesis]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Tiempo de pared y CPU | Wall time incluye espera; CPU time cuenta ejecución en procesador. | Evidencia o contraejemplo registrado |
| Perfil determinista y muestreo | El perfil determinista registra llamadas y tiempos con detalle, añadiendo overhead. | Evidencia o contraejemplo registrado |
| Asignaciones, retención y pico | Memoria asignada no equivale a memoria retenida ni RSS. | Evidencia o contraejemplo registrado |
| I/O y red | Trazar duración, bytes y concurrencia por operación separa espera de cómputo. | Evidencia o contraejemplo registrado |
| Perfil como hipótesis | El perfil señala dónde se observa costo, no por qué. | Evidencia o contraejemplo registrado |

## Conceptos y decisiones

### 1. Tiempo de pared y CPU

Wall time incluye espera; CPU time cuenta ejecución en procesador. Una tarea I/O-bound puede tener pared alta y CPU baja. Perfilar solo funciones de CPU no atribuye latencia externa ni cola.

### 2. Perfil determinista y muestreo

El perfil determinista registra llamadas y tiempos con detalle, añadiendo overhead. El muestreo interrumpe periódicamente y aproxima distribución con menor intrusión. Eventos cortos o raros pueden perderse; se elige según pregunta.

### 3. Asignaciones, retención y pico

Memoria asignada no equivale a memoria retenida ni RSS. `tracemalloc` compara snapshots de asignaciones Python; no observa necesariamente memoria nativa completa. Una referencia viva explica retención mejor que el tamaño de una línea aislada.

### 4. I/O y red

Trazar duración, bytes y concurrencia por operación separa espera de cómputo. Un profiler general puede agrupar todo como llamada del sistema. Correlación y timestamps monotónicos permiten relacionar solicitud, bloqueo y respuesta.

### 5. Perfil como hipótesis

El perfil señala dónde se observa costo, no por qué. Se formula una causa, cambia una variable y repite con salida correcta. Optimizar una función caliente irrelevante para el SLO es trabajo sin impacto.

## Definiciones de trabajo

- **tiempo de pared y cpu:** wall time incluye espera; cpu time cuenta ejecución en procesador.
- **perfil determinista y muestreo:** el perfil determinista registra llamadas y tiempos con detalle, añadiendo overhead.
- **asignaciones, retención y pico:** memoria asignada no equivale a memoria retenida ni rss.
- **i/o y red:** trazar duración, bytes y concurrencia por operación separa espera de cómputo.
- **perfil como hipótesis:** el perfil señala dónde se observa costo, no por qué.

Las definiciones son operativas para Lupa. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```shell
python -m cProfile -o evidence/cpu.prof -m orbe.benchmark
python -X tracemalloc=10 -m unittest tests.test_snapshot
python -m timeit -r 9 -n 1000 "target()"
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En Lupa, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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
2. **Construcción:** añade una observación que refute una hipótesis sin cambiar simultáneamente el sistema.
3. **Frontera:** cubre vacío, empate, no autorizado e inválido con resultados distintos.
4. **Contraste:** reescribe una pieza con otro modelo y explica una mejora y una pérdida.

## Reto verificable

Entrega implementación, fixtures, pruebas y un informe corto. Se aprueba si otra persona ejecuta desde checkout limpio, obtiene los mismos resultados y puede relacionar cada rama o transformación con una regla del dominio. No se aprueba por cantidad de archivos ni por usar la sintaxis característica del paradigma.

## Caso conductor

Lupa parte de una inversión de empates en Orbe, captura versión y entrada mínima, compara un entorno sano con uno afectado y conserva la primera divergencia observable. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Una técnica o herramienta determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar técnicas es válido si las fronteras preservan identidad, orden, errores y evidencia.

### ¿Más automatización o menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todas las herramientas mencionadas?

No. Instala solo lo necesario para la práctica elegida. Registra versión y comandos; si solo analizas una notación o salida, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Perfila generación de fixtures y concluye que el algoritmo es lento. Mueve preparación fuera de la región, valida resultado y repite manteniendo la misma carga.

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
work/SE-099/
├── README.md
├── lupa/
│   ├── domain.py
│   └── se_099.py
├── fixtures/cases.json
├── tests/test_se_099.py
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

Traslada un fixture al segundo modelo, herramienta, plataforma o lenguaje. Compara representación de ausencia, error, mutabilidad, orden y cancelación. La transferencia está lograda cuando el contrato se conserva y las diferencias están explicadas, no cuando la interfaz se parece.

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

- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.
- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — Percepción, operación por teclado y reducción de barreras en interfaces; autoridad: W3C.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación de Lupa sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

Un perfil dinámico observa entradas ejecutadas. La siguiente clase combina compilador, linter, formatter y análisis estático para detectar clases distintas de defectos.

## Glosario

- **tiempo de pared y cpu:** wall time incluye espera; cpu time cuenta ejecución en procesador.
- **perfil determinista y muestreo:** el perfil determinista registra llamadas y tiempos con detalle, añadiendo overhead.
- **asignaciones, retención y pico:** memoria asignada no equivale a memoria retenida ni rss.
- **i/o y red:** trazar duración, bytes y concurrencia por operación separa espera de cómputo.
- **perfil como hipótesis:** el perfil señala dónde se observa costo, no por qué.

---

[← SE-098 — Depuradores, breakpoints y observación de estado](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-099.html) · [SE-100 — Compiladores, linters, formatters y análisis estático →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-100-compiladores-linters-formatters-y-analisis-estatico/README.md)
