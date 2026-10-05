# SE-077 — Programación declarativa y basada en reglas

[← SE-076 — Programación funcional, composición e inmutabilidad](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-077.html) · [SE-078 — Programación lógica y resolución →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para expresar el qué mediante relaciones o restricciones y reconocer el motor que decide el cómo.

**Por qué aparece aquí.** Se sitúa después de **Programación funcional, composición e inmutabilidad** y antes de **Programación lógica y resolución**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Confundir declarativo con ausencia de orden o costo.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Declarative-model.md con regla, consulta, plan observado y contraejemplo. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** La sintaxis declarativa no garantiza optimización.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [SWI-Prolog Reference Manual](https://www.swi-prolog.org/pldoc/man?section=intro) | Hechos, reglas, unificación, búsqueda y límites operacionales; autoridad: SWI-Prolog project | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Construcción, diseño y fundamentos profesionales; autoridad: IEEE Computer Society | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **motor de reglas comparado de la Parte 06**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Programación declarativa y basada en reglas** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué significa declarar una relación sin fijar todos los pasos para obtenerla?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

Las reglas del motor de reglas comparado cambian con frecuencia y están enterradas entre bucles y asignaciones. Producto puede describir condiciones, pero no auditar la precedencia ni detectar conflictos sin leer control imperativo.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Intención declarada / estrategia de ejecución] --> N2[Hechos, reglas / condiciones] --> N3[Prioridad / conflictos] --> N4[Evaluación incremental / explicación] --> N5[Límites de lenguajes declarativos]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Intención declarada y estrategia de ejecución | Una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor. | Predicción, traza causal y contraejemplo de **Intención declarada y estrategia de ejecución** en `declarative-model.md` |
| Hechos, reglas y condiciones | Un hecho representa una observación; una regla deriva una consecuencia cuando su antecedente se satisface. | Predicción, traza causal y contraejemplo de **Hechos, reglas y condiciones** en `declarative-model.md` |
| Prioridad y conflictos | Dos reglas pueden habilitar acciones incompatibles. | Predicción, traza causal y contraejemplo de **Prioridad y conflictos** en `declarative-model.md` |
| Evaluación incremental y explicación | Un motor puede reevaluar todo o actualizar solo consecuencias afectadas por hechos nuevos. | Predicción, traza causal y contraejemplo de **Evaluación incremental y explicación** en `declarative-model.md` |
| Límites de lenguajes declarativos | Expresar estado temporal, efectos externos o algoritmos irregulares puede volverse difícil. | Predicción, traza causal y contraejemplo de **Límites de lenguajes declarativos** en `declarative-model.md` |
## Conceptos y decisiones

### 1. Intención declarada y estrategia de ejecución

Una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor. SQL, CSS y sistemas de reglas no son equivalentes, pero comparten esa separación. El costo y el orden no desaparecen: quedan en el planificador, la especificidad o la estrategia de resolución.

### 2. Hechos, reglas y condiciones

Un hecho representa una observación; una regla deriva una consecuencia cuando su antecedente se satisface. Las reglas necesitan vocabulario, tipos y alcance temporal. Una condición ambigua como `high_latency` debe vincularse a unidad, umbral y fuente de medición.

### 3. Prioridad y conflictos

Dos reglas pueden habilitar acciones incompatibles. Salience, orden textual o una política explícita deciden cuál vence. Confiar en un orden accidental hace que añadir una regla cambie otra sin señal; el motor de reglas comparado conserva una matriz de conflictos y exige desempate documentado.

### 4. Evaluación incremental y explicación

Un motor puede reevaluar todo o actualizar solo consecuencias afectadas por hechos nuevos. La segunda opción mejora escala pero mantiene dependencias internas. Cada recomendación debe incluir reglas activadas y hechos usados para que una persona pueda revisar la decisión.

### 5. Límites de lenguajes declarativos

Expresar estado temporal, efectos externos o algoritmos irregulares puede volverse difícil. Insertar funciones opacas dentro de reglas recupera poder pero pierde análisis y portabilidad. Una capa declarativa sirve cuando el dominio comparte un vocabulario estable y auditable.

## Definiciones de trabajo

- **intención declarada y estrategia de ejecución:** una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor.
- **hechos, reglas y condiciones:** un hecho representa una observación; una regla deriva una consecuencia cuando su antecedente se satisface.
- **prioridad y conflictos:** dos reglas pueden habilitar acciones incompatibles.
- **evaluación incremental y explicación:** un motor puede reevaluar todo o actualizar solo consecuencias afectadas por hechos nuevos.
- **límites de lenguajes declarativos:** expresar estado temporal, efectos externos o algoritmos irregulares puede volverse difícil.

Las definiciones son operativas para el motor de reglas comparado. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
rules = [
    {"when": {"authorized": True, "latency_ms_gte": 800},
     "then": "inspect-transport", "priority": 20},
    {"when": {"dns_failed": True},
     "then": "inspect-dns", "priority": 30},
]
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

Crea dos reglas de igual prioridad que recomiendan acciones incompatibles. Verifica que el motor no dependa del orden del archivo: debe devolver conflicto explícito o aplicar un desempate publicado.

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
work/SE-077/
├── README.md
├── rule_engine/
│   ├── domain.py
│   └── se_077.py
├── fixtures/cases.json
├── tests/test_se_077.py
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

Una tabla de reglas no prueba consistencia ni completitud. La siguiente clase usa unificación y búsqueda para estudiar resolución lógica y sus costos.

## Glosario

- **intención declarada y estrategia de ejecución:** una descripción declarativa especifica qué relación debe cumplirse y delega parte del cómo a un motor.
- **hechos, reglas y condiciones:** un hecho representa una observación; una regla deriva una consecuencia cuando su antecedente se satisface.
- **prioridad y conflictos:** dos reglas pueden habilitar acciones incompatibles.
- **evaluación incremental y explicación:** un motor puede reevaluar todo o actualizar solo consecuencias afectadas por hechos nuevos.
- **límites de lenguajes declarativos:** expresar estado temporal, efectos externos o algoritmos irregulares puede volverse difícil.

---

[← SE-076 — Programación funcional, composición e inmutabilidad](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md) · [↑ Parte 06](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-077.html) · [SE-078 — Programación lógica y resolución →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md)
