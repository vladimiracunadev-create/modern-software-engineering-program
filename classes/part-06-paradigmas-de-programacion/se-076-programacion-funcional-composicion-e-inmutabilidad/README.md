# SE-076 — Programación funcional, composición e inmutabilidad

[← SE-075 — Orientación a objetos, mensajes y encapsulación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-076.html) · [SE-077 — Programación declarativa y basada en reglas →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para razonar con composición, valores inmutables y efectos localizados.

**Por qué aparece aquí.** Se sitúa después de **Orientación a objetos, mensajes y encapsulación** y antes de **Programación declarativa y basada en reglas**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Llamar funcional a cualquier uso de map o lambda.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Composition.md con función pura, efecto aislado y contraste mutable. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Inmutabilidad puede trasladar costos y no elimina I/O.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Python Language Reference](https://docs.python.org/3/reference/) | Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) | Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **motor de reglas comparado de la Parte 06**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Programación funcional, composición e inmutabilidad** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué se gana al expresar la decisión como transformación de valores sin efectos ocultos?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

El motor de reglas comparado necesita evaluar la misma evidencia en pruebas, CLI y simulaciones paralelas. El núcleo orientado a objetos conserva cachés internas y el orden de llamadas cambia el resultado.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Funciones puras / transparencia referencial] --> N2[Inmutabilidad / evolución de valores] --> N3[Funciones de orden superior] --> N4[Composición / tipos de resultado] --> N5[Recursión, evaluación / efectos]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Funciones puras y transparencia referencial | Una función pura devuelve el mismo valor para los mismos argumentos y no modifica estado observable. | Predicción, traza causal y contraejemplo de **Funciones puras y transparencia referencial** en `composition.md` |
| Inmutabilidad y evolución de valores | En vez de cambiar un registro se produce otro que comparte o copia lo necesario. | Predicción, traza causal y contraejemplo de **Inmutabilidad y evolución de valores** en `composition.md` |
| Funciones de orden superior | Pasar una regla como valor permite parametrizar evaluación sin condicionales globales. | Predicción, traza causal y contraejemplo de **Funciones de orden superior** en `composition.md` |
| Composición y tipos de resultado | Funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra. | Predicción, traza causal y contraejemplo de **Composición y tipos de resultado** en `composition.md` |
| Recursión, evaluación y efectos | La recursión describe estructuras inductivas, aunque Python no optimiza llamadas terminales y un bucle puede ser más seguro. | Predicción, traza causal y contraejemplo de **Recursión, evaluación y efectos** en `composition.md` |
## Conceptos y decisiones

### 1. Funciones puras y transparencia referencial

Una función pura devuelve el mismo valor para los mismos argumentos y no modifica estado observable. Esto permite sustituir una llamada por su resultado al razonar. Pureza no significa ausencia total de efectos en el programa: significa empujarlos a fronteras explícitas.

### 2. Inmutabilidad y evolución de valores

En vez de cambiar un registro se produce otro que comparte o copia lo necesario. Cada versión puede inspeccionarse y compararse. La inmutabilidad reduce aliasing, pero estructuras copiadas ingenuamente pueden costar memoria; las estructuras persistentes comparten internamente sin exponer mutación.

### 3. Funciones de orden superior

Pasar una regla como valor permite parametrizar evaluación sin condicionales globales. `map`, `filter` y `reduce` expresan transformaciones, pero una cadena excesiva puede ocultar orden, errores o complejidad. La forma debe servir al modelo y no demostrar virtuosismo sintáctico.

### 4. Composición y tipos de resultado

Funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra. Un resultado explícito distingue éxito y error sin lanzar a distancia. La composición falla si cada paso usa convenciones distintas para ausencia, error o contexto.

### 5. Recursión, evaluación y efectos

La recursión describe estructuras inductivas, aunque Python no optimiza llamadas terminales y un bucle puede ser más seguro. La evaluación perezosa evita trabajo hasta consumirlo, pero también desplaza errores y vida de recursos. El motor de reglas comparado mide antes de adoptar cualquiera de las dos.

## Definiciones de trabajo

- **funciones puras y transparencia referencial:** una función pura devuelve el mismo valor para los mismos argumentos y no modifica estado observable.
- **inmutabilidad y evolución de valores:** en vez de cambiar un registro se produce otro que comparte o copia lo necesario.
- **funciones de orden superior:** pasar una regla como valor permite parametrizar evaluación sin condicionales globales.
- **composición y tipos de resultado:** funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra.
- **recursión, evaluación y efectos:** la recursión describe estructuras inductivas, aunque python no optimiza llamadas terminales y un bucle puede ser más seguro.

Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
from dataclasses import replace

def add_evidence(state, item):
    return replace(state, evidence=state.evidence + (item,))

def eligible(rule, evidence):
    return rule.authorized and rule.predicate(evidence)
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

Inserta una consulta al reloj dentro de `eligible`; la misma entrada cambia entre ejecuciones. Pasa `now` como valor de contexto y congélalo en pruebas para restaurar determinismo.

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
work/SE-076/
├── README.md
├── rule_engine/
│   ├── domain.py
│   └── se_076.py
├── fixtures/cases.json
├── tests/test_se_076.py
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



- [Python Language Reference](https://docs.python.org/3/reference/) — Semántica de sentencias, funciones, clases, generadores y corrutinas; autoridad: Python Software Foundation.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) — Ownership, enums, traits, errores y concurrencia sin carreras de datos; autoridad: Rust project.
- [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) — Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project.
- [ReactiveX Observable Contract](https://reactivex.io/documentation/contract.html) — Notificaciones, terminación, errores y control de flujo observable; autoridad: ReactiveX project.
- [Erlang System Documentation: Processes](https://www.erlang.org/doc/system/ref_man_processes.html) — Procesos, buzones, envío de mensajes, enlaces y monitores; autoridad: Erlang/OTP project.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación del motor de reglas comparado sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

Pureza y composición no resuelven automáticamente interacción, latencia ni grandes flujos. La siguiente clase expresa el resultado deseado como reglas declarativas.

## Glosario

- **funciones puras y transparencia referencial:** una función pura devuelve el mismo valor para los mismos argumentos y no modifica estado observable.
- **inmutabilidad y evolución de valores:** en vez de cambiar un registro se produce otro que comparte o copia lo necesario.
- **funciones de orden superior:** pasar una regla como valor permite parametrizar evaluación sin condicionales globales.
- **composición y tipos de resultado:** funciones pequeñas se conectan cuando la salida de una satisface la entrada de otra.
- **recursión, evaluación y efectos:** la recursión describe estructuras inductivas, aunque python no optimiza llamadas terminales y un bucle puede ser más seguro.

---

[← SE-075 — Orientación a objetos, mensajes y encapsulación](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-076.html) · [SE-077 — Programación declarativa y basada en reglas →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md)
