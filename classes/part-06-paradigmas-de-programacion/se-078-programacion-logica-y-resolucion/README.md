# SE-078 — Programación lógica y resolución

[← SE-077 — Programación declarativa y basada en reglas](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-078.html) · [SE-079 — Programación orientada a eventos →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)

> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica.

## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para explicar unificación, búsqueda y backtracking como mecanismo operacional de la lógica.

**Por qué aparece aquí.** Se sitúa después de **Programación declarativa y basada en reglas** y antes de **Programación orientada a eventos**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Leer Prolog como ejecución exhaustiva sin depender de orden.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Resolution-trace.md con sustituciones, árbol de búsqueda y corte problemático. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** La verdad lógica y el comportamiento operacional no son equivalentes.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) | Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **motor de reglas comparado de la Parte 06**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Programación lógica y resolución** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo produce respuestas un motor lógico a partir de relaciones, variables y búsqueda?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

El motor de reglas comparado debe responder qué prueba es admisible y también por qué. Enumerar rutas a mano duplica combinaciones; una relación lógica puede derivarlas, pero una regla recursiva mal ordenada no termina.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Términos, hechos / consultas] --> N2[Unificación] --> N3[Resolución / backtracking] --> N4[Negación / mundo cerrado] --> N5[Restricciones / explicación]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Términos, hechos y consultas | Un programa lógico describe relaciones mediante términos. | Predicción, traza causal y contraejemplo de **Términos, hechos y consultas** en `resolution-trace.md` |
| Unificación | Unificar busca una sustitución compatible entre estructuras. | Predicción, traza causal y contraejemplo de **Unificación** en `resolution-trace.md` |
| Resolución y backtracking | El motor selecciona metas, prueba cláusulas y retrocede cuando una elección falla. | Predicción, traza causal y contraejemplo de **Resolución y backtracking** en `resolution-trace.md` |
| Negación y mundo cerrado | En muchos sistemas Prolog, no poder demostrar una meta permite tratarla como falsa bajo supuestos de mundo cerrado. | Predicción, traza causal y contraejemplo de **Negación y mundo cerrado** en `resolution-trace.md` |
| Restricciones y explicación | La programación lógica con restricciones mantiene dominios posibles y propaga reducciones antes de enumerar. | Predicción, traza causal y contraejemplo de **Restricciones y explicación** en `resolution-trace.md` |
## Conceptos y decisiones

### 1. Términos, hechos y consultas

Un programa lógico describe relaciones mediante términos. Una consulta pregunta qué sustituciones vuelven verdadera una relación. La dirección no siempre está fijada como en una función, aunque la implementación y los modos de uso sí afectan terminación y rendimiento.

### 2. Unificación

Unificar busca una sustitución compatible entre estructuras. No es asignación mutable: una variable lógica queda vinculada dentro de una rama de búsqueda. El chequeo de ocurrencia y las extensiones del sistema determinan qué términos son admitidos, por lo que no conviene extrapolar desde pseudocódigo.

### 3. Resolución y backtracking

El motor selecciona metas, prueba cláusulas y retrocede cuando una elección falla. Ese mecanismo enumera alternativas sin escribir bucles explícitos. Orden de metas y cláusulas puede cambiar drásticamente costo o terminación aunque el significado declarativo pretendido parezca igual.

### 4. Negación y mundo cerrado

En muchos sistemas Prolog, no poder demostrar una meta permite tratarla como falsa bajo supuestos de mundo cerrado. Eso no equivale a negar un hecho desconocido. El motor de reglas comparado distingue `denied`, `not_proven` y `not_applicable` para no convertir ausencia de evidencia en evidencia de ausencia.

### 5. Restricciones y explicación

La programación lógica con restricciones mantiene dominios posibles y propaga reducciones antes de enumerar. Puede expresar horarios o compatibilidad con claridad, pero requiere inspeccionar qué restricciones sustentan una respuesta. La traza bruta del motor no reemplaza una explicación de dominio.

## Definiciones de trabajo

- **términos, hechos y consultas:** un programa lógico describe relaciones mediante términos.
- **unificación:** unificar busca una sustitución compatible entre estructuras.
- **resolución y backtracking:** el motor selecciona metas, prueba cláusulas y retrocede cuando una elección falla.
- **negación y mundo cerrado:** en muchos sistemas prolog, no poder demostrar una meta permite tratarla como falsa bajo supuestos de mundo cerrado.
- **restricciones y explicación:** la programación lógica con restricciones mantiene dominios posibles y propaga reducciones antes de enumerar.

Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
authorized(case_17).
observed(case_17, high_latency).
next(Case, inspect_transport) :-
    authorized(Case),
    observed(Case, high_latency).
% Consulta: ?- next(case_17, Action).
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En el motor de reglas comparado, una recomendación contiene acción, evidencia usada, versión de política y explicación. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si devuelve una cadena: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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
2. **Construcción:** añade una regla del motor de reglas comparado sin alterar los fixtures anteriores.
3. **Frontera:** cubre vacío, empate, no autorizado e inválido con resultados distintos.
4. **Contraste:** reescribe una pieza con otro modelo y explica una mejora y una pérdida.

## Reto verificable

Entrega implementación, fixtures, pruebas y un informe corto. Se aprueba si otra persona ejecuta desde checkout limpio, obtiene los mismos resultados y puede relacionar cada rama o transformación con una regla del dominio. No se aprueba por cantidad de archivos ni por usar la sintaxis característica del paradigma.

## Caso conductor

El motor de reglas comparado recibe una observación autorizada, evalúa reglas y devuelve una recomendación explicable. En esta clase, ejecuta el caso `latency_ms=900`, el límite `latency_ms=800`, el contraejemplo `authorized=false` y una entrada incompleta. Cambia después una sola regla y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta la comparación final de la parte.

## Preguntas frecuentes

### ¿Un paradigma determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar modelos es válido si los adaptadores preservan identidad, orden, errores y evidencia.

### ¿Menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todos los lenguajes mencionados?

No. Python basta para la práctica base. Si usas Prolog, Rust o Erlang, registra versión y comandos; si solo analizas notación, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Define una regla recursiva que se invoca antes del caso base y observa no terminación. Reordena metas, acota el dominio y conserva una consulta que demuestre respuesta y finalización.

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
work/SE-078/
├── README.md
├── rule_engine/
│   ├── domain.py
│   └── se_078.py
├── fixtures/cases.json
├── tests/test_se_078.py
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



- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación del motor de reglas comparado sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

La resolución lógica depende de supuestos operacionales y no gestiona por sí sola una secuencia temporal de eventos. La siguiente clase convierte entradas externas en eventos con contrato y ciclo de vida.

## Glosario

- **términos, hechos y consultas:** un programa lógico describe relaciones mediante términos.
- **unificación:** unificar busca una sustitución compatible entre estructuras.
- **resolución y backtracking:** el motor selecciona metas, prueba cláusulas y retrocede cuando una elección falla.
- **negación y mundo cerrado:** en muchos sistemas prolog, no poder demostrar una meta permite tratarla como falsa bajo supuestos de mundo cerrado.
- **restricciones y explicación:** la programación lógica con restricciones mantiene dominios posibles y propaga reducciones antes de enumerar.

---

[← SE-077 — Programación declarativa y basada en reglas](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-078.html) · [SE-079 — Programación orientada a eventos →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md)
