# SE-082 — Selección y combinación responsable de paradigmas

[← SE-081 — Programación concurrente y actores](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-082.html) · [SE-083 — Taller: una regla de negocio en cinco paradigmas →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)

> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica.

## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para seleccionar y combinar paradigmas por fuerzas del problema y costo de adaptación.

**Por qué aparece aquí.** Se sitúa después de **Programación concurrente y actores** y antes de **Taller: una regla de negocio en cinco paradigmas**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Elegir paradigma por moda o forzar uno sobre todas las capas.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Decision-record.md con alternativas, fuerzas, adaptadores y pérdida aceptada. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** La matriz orienta una decisión contextual, no produce un ganador universal.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Python Language Reference](https://docs.python.org/3/reference/) | Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) | Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **motor de reglas comparado de la Parte 06**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Selección y combinación responsable de paradigmas** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo elegir y combinar paradigmas a partir de fuerzas del problema y evidencia?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

El equipo quiere objetos para el dominio, flujos reactivos para entradas y reglas declarativas para política. Cada elección aislada parece razonable, pero las conversiones multiplican tipos, errores y puntos de depuración.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Fuerzas del problema] --> N2[Semántica antes que sintaxis] --> N3[Fronteras entre modelos] --> N4[Costo cognitivo / operativo] --> N5[Decisión reversible / experimento]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Fuerzas del problema | La elección parte de estado, temporalidad, concurrencia, tasa de cambio, auditabilidad y habilidades del equipo. | Predicción, traza causal y contraejemplo de **Fuerzas del problema** en `decision-record.md` |
| Semántica antes que sintaxis | Dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error. | Predicción, traza causal y contraejemplo de **Semántica antes que sintaxis** en `decision-record.md` |
| Fronteras entre modelos | Combinar modelos exige adaptadores: evento a valor, objeto a registro, resultado a excepción o mensaje. | Predicción, traza causal y contraejemplo de **Fronteras entre modelos** en `decision-record.md` |
| Costo cognitivo y operativo | Una solución elegante para especialistas puede ser inoperable para el equipo que la mantiene. | Predicción, traza causal y contraejemplo de **Costo cognitivo y operativo** en `decision-record.md` |
| Decisión reversible y experimento | Cuando la evidencia no basta, se limita la apuesta: un slice, criterios y fecha de revisión. | Predicción, traza causal y contraejemplo de **Decisión reversible y experimento** en `decision-record.md` |
## Conceptos y decisiones

### 1. Fuerzas del problema

La elección parte de estado, temporalidad, concurrencia, tasa de cambio, auditabilidad y habilidades del equipo. Un paradigma es adecuado cuando vuelve directas las propiedades dominantes. Popularidad o brevedad no son fuerzas técnicas suficientes.

### 2. Semántica antes que sintaxis

Dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error. Contar líneas o tokens sin verificar semántica premia omisiones. El motor de reglas comparado usa fixtures comunes y normaliza solo diferencias de presentación.

### 3. Fronteras entre modelos

Combinar modelos exige adaptadores: evento a valor, objeto a registro, resultado a excepción o mensaje. Cada traducción puede perder orden, identidad o información de error. El contrato de la frontera debe declarar qué se preserva y qué se descarta.

### 4. Costo cognitivo y operativo

Una solución elegante para especialistas puede ser inoperable para el equipo que la mantiene. Se consideran trazabilidad, tooling, profiling, contratación, ecosistema y respuesta a incidentes. El costo no invalida innovación, pero impide presentarla como gratuita.

### 5. Decisión reversible y experimento

Cuando la evidencia no basta, se limita la apuesta: un slice, criterios y fecha de revisión. Una matriz ponderada ayuda a hacer supuestos visibles, no produce una verdad automática. El resultado debe registrar contraejemplos que cambiarían la decisión.

## Definiciones de trabajo

- **fuerzas del problema:** la elección parte de estado, temporalidad, concurrencia, tasa de cambio, auditabilidad y habilidades del equipo.
- **semántica antes que sintaxis:** dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error.
- **fronteras entre modelos:** combinar modelos exige adaptadores: evento a valor, objeto a registro, resultado a excepción o mensaje.
- **costo cognitivo y operativo:** una solución elegante para especialistas puede ser inoperable para el equipo que la mantiene.
- **decisión reversible y experimento:** cuando la evidencia no basta, se limita la apuesta: un slice, criterios y fecha de revisión.

Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
| Fuerza | Imperativo | Funcional | Reglas | Reactivo | Actores |
|---|---:|---:|---:|---:|---:|
| auditar decisión | 2 | 3 | 5 | 2 | 3 |
| presión de flujo | 2 | 3 | 2 | 5 | 4 |
| fallo aislado | 1 | 3 | 2 | 3 | 5 |
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

Elige el mayor total de una matriz sin revisar pesos. Cambia la prioridad de auditabilidad y observa que vence otra alternativa. Documenta sensibilidad y condiciones de reversión.

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
work/SE-082/
├── README.md
├── rule_engine/
│   ├── domain.py
│   └── se_082.py
├── fixtures/cases.json
├── tests/test_se_082.py
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

Una matriz organiza juicio, no sustituye un prototipo ni datos de mantenimiento. El taller siguiente implementa una regla en cinco modelos y obliga a contrastar sus trazas.

## Glosario

- **fuerzas del problema:** la elección parte de estado, temporalidad, concurrencia, tasa de cambio, auditabilidad y habilidades del equipo.
- **semántica antes que sintaxis:** dos implementaciones son comparables si aceptan el mismo dominio y producen resultados equivalentes para normal, límite y error.
- **fronteras entre modelos:** combinar modelos exige adaptadores: evento a valor, objeto a registro, resultado a excepción o mensaje.
- **costo cognitivo y operativo:** una solución elegante para especialistas puede ser inoperable para el equipo que la mantiene.
- **decisión reversible y experimento:** cuando la evidencia no basta, se limita la apuesta: un slice, criterios y fecha de revisión.

---

[← SE-081 — Programación concurrente y actores](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-082.html) · [SE-083 — Taller: una regla de negocio en cinco paradigmas →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-083-taller-una-regla-de-negocio-en-cinco-paradigmas/README.md)
