# SE-107 — Taller: diagnosticar un fallo desconocido

[← SE-106 — Ergonomía, accesibilidad y productividad del entorno](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-107.html) · [SE-108 — Proyecto: entorno de desarrollo autocontenido →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md)

> Estado: **GUIDED** · Clase desarrollada y revisada cualitativamente.

## Antes de empezar

Esta clase continúa **Lupa**, el caso conductor de la Parte 08. Recupera la evidencia de la clase anterior, añade una decisión propia de **Taller: diagnosticar un fallo desconocido** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo investigar un fallo desconocido sin saltar de herramienta en herramienta?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Se entrega una versión de Orbe que a veces invierte empates y consume memoria. No se revela si la causa está en algoritmo, runtime, fixture, extensión o entorno.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Triage / contención] --> N2[Cronología / hechos] --> N3[Hipótesis rivales] --> N4[Escalera de herramientas] --> N5[Causa, corrección / seguimiento]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Triage y contención | Primero se describe impacto, alcance, seguridad y acción reversible para evitar daño. | Evidencia o contraejemplo registrado |
| Cronología y hechos | El equipo registra qué cambió, cuándo apareció y en qué entornos, separando observación de interpretación. | Evidencia o contraejemplo registrado |
| Hipótesis rivales | Se formulan al menos dos explicaciones con predicciones distintas. | Evidencia o contraejemplo registrado |
| Escalera de herramientas | Se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta. | Evidencia o contraejemplo registrado |
| Causa, corrección y seguimiento | La causa explica mecanismo y condiciones; la corrección cambia ese mecanismo; la regresión falla antes y pasa después. | Evidencia o contraejemplo registrado |

## Conceptos y decisiones

### 1. Triage y contención

Primero se describe impacto, alcance, seguridad y acción reversible para evitar daño. Contener no es corregir: puede fijar versión o desactivar ruta mientras se investiga. La evidencia original se conserva antes de limpiar.

### 2. Cronología y hechos

El equipo registra qué cambió, cuándo apareció y en qué entornos, separando observación de interpretación. Una cronología evita reconstrucciones de memoria. Correlación con un deploy orienta, pero no demuestra causalidad.

### 3. Hipótesis rivales

Se formulan al menos dos explicaciones con predicciones distintas. Cada experimento elige la observación que más separa. Confirmar solo la favorita genera sesgo; una hipótesis que no puede refutarse todavía no guía diagnóstico.

### 4. Escalera de herramientas

Se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta. Herramienta más sofisticada no implica mejor evidencia. Cada paso registra qué descartó y qué incertidumbre queda.

### 5. Causa, corrección y seguimiento

La causa explica mecanismo y condiciones; la corrección cambia ese mecanismo; la regresión falla antes y pasa después. El informe añade factores contribuyentes y acciones con owner, sin culpar a la persona que activó una debilidad sistémica.

## Definiciones de trabajo

- **triage y contención:** primero se describe impacto, alcance, seguridad y acción reversible para evitar daño.
- **cronología y hechos:** el equipo registra qué cambió, cuándo apareció y en qué entornos, separando observación de interpretación.
- **hipótesis rivales:** se formulan al menos dos explicaciones con predicciones distintas.
- **escalera de herramientas:** se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta.
- **causa, corrección y seguimiento:** la causa explica mecanismo y condiciones; la corrección cambia ese mecanismo; la regresión falla antes y pasa después.

Las definiciones son operativas para Lupa. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```text
| Hipótesis | Predicción | Observación | Estado |
|---|---|---|---|
| comparador inestable | diverge antes del heap | traza de claves | abierta |
| runtime distinto | solo falla en 3.13 | matriz limpia | abierta |
| fixture mutado | hash cambia antes de ordenar | snapshot | abierta |
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

Actualiza dependencia, runtime y comparador a la vez; el fallo desaparece sin causa. Revierte en rama aislada y construye una matriz que cambie una dimensión por ejecución.

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
work/SE-107/
├── README.md
├── lupa/
│   ├── domain.py
│   └── se_107.py
├── fixtures/cases.json
├── tests/test_se_107.py
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

El taller produce diagnóstico del caso dado; no demuestra que todo el equipo pueda recrearlo. El proyecto siguiente convierte el proceso en entorno autocontenido con ruta de recuperación.

## Glosario

- **triage y contención:** primero se describe impacto, alcance, seguridad y acción reversible para evitar daño.
- **cronología y hechos:** el equipo registra qué cambió, cuándo apareció y en qué entornos, separando observación de interpretación.
- **hipótesis rivales:** se formulan al menos dos explicaciones con predicciones distintas.
- **escalera de herramientas:** se empieza por versión, logs y reproducción; luego debugger, profiler o análisis según la pregunta.
- **causa, corrección y seguimiento:** la causa explica mecanismo y condiciones; la corrección cambia ese mecanismo; la regresión falla antes y pasa después.

---

[← SE-106 — Ergonomía, accesibilidad y productividad del entorno](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-106-ergonomia-accesibilidad-y-productividad-del-entorno/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-107.html) · [SE-108 — Proyecto: entorno de desarrollo autocontenido →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md)
