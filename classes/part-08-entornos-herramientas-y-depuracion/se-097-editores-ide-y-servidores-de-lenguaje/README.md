# SE-097 — Editores, IDE y servidores de lenguaje

[← SE-096 — Proyecto: biblioteca comparada con casos límite](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-097.html) · [SE-098 — Depuradores, breakpoints y observación de estado →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para entender editor, IDE y servidor de lenguaje como componentes con protocolos y capacidades negociadas.

**Por qué aparece aquí.** Se sitúa después de **Proyecto: biblioteca comparada con casos límite** y antes de **Depuradores, breakpoints y observación de estado**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Atribuir al editor análisis que realmente ejecuta otra herramienta.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Tooling-map.md con proceso, mensaje LSP, capacidad y modo degradado. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Soportar el protocolo no implica soportar todas las capacidades.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) | Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) | Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **entorno reproducible de diagnóstico de la Parte 08**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Editores, IDE y servidores de lenguaje** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué trabajo pertenece al editor, al IDE y al servidor que entiende el lenguaje?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

En el entorno reproducible de diagnóstico, una importación aparece válida en un editor y rota en CI. Se atribuye al IDE, pero el diagnóstico proviene de otro intérprete configurado por el servidor de lenguaje.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Editor e IDE] --> N2[Modelo sintáctico / semántico] --> N3[Language Server Protocol] --> N4[Workspace / configuración] --> N5[Confianza / extensiones]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Editor e IDE | Un editor manipula texto y puede integrar capacidades; un IDE reúne proyecto, build, ejecución, depuración y navegación. | Predicción, traza causal y contraejemplo de **Editor e IDE** en `tooling-map.md` |
| Modelo sintáctico y semántico | Resaltado por tokens no equivale a resolver nombres o tipos. | Predicción, traza causal y contraejemplo de **Modelo sintáctico y semántico** en `tooling-map.md` |
| Language Server Protocol | LSP estandariza mensajes JSON-RPC entre cliente y servidor para completado, definición, referencias y diagnósticos. | Predicción, traza causal y contraejemplo de **Language Server Protocol** en `tooling-map.md` |
| Workspace y configuración | La raíz del workspace condiciona búsqueda de configuración, módulos y herramientas. | Predicción, traza causal y contraejemplo de **Workspace y configuración** en `tooling-map.md` |
| Confianza y extensiones | Una extensión ejecuta código con acceso relevante al workspace. | Predicción, traza causal y contraejemplo de **Confianza y extensiones** en `tooling-map.md` |
## Conceptos y decisiones

### 1. Editor e IDE

Un editor manipula texto y puede integrar capacidades; un IDE reúne proyecto, build, ejecución, depuración y navegación. La frontera no es absoluta. Elegir uno exige describir tareas y costos, no usar `IDE` como sinónimo de herramienta profesional.

### 2. Modelo sintáctico y semántico

Resaltado por tokens no equivale a resolver nombres o tipos. Parsing construye estructura; análisis semántico necesita símbolos, imports, configuración y a veces build. Un archivo puede verse correcto mientras el proyecto que interpreta el servidor es otro.

### 3. Language Server Protocol

LSP estandariza mensajes JSON-RPC entre cliente y servidor para completado, definición, referencias y diagnósticos. El protocolo no garantiza calidad del análisis; cliente y servidor negocian capacidades y sincronizan documentos con versiones.

### 4. Workspace y configuración

La raíz del workspace condiciona búsqueda de configuración, módulos y herramientas. Abrir una subcarpeta puede producir otro grafo de proyecto. Configuración de usuario, workspace y repositorio necesita precedencia explícita para que dos personas observen lo mismo.

### 5. Confianza y extensiones

Una extensión ejecuta código con acceso relevante al workspace. Procedencia, permisos, actualización y política de red forman parte del riesgo. Un perfil mínimo reduce variabilidad y facilita recuperar el entorno sin exportar secretos personales.

## Definiciones de trabajo

- **editor e ide:** un editor manipula texto y puede integrar capacidades; un ide reúne proyecto, build, ejecución, depuración y navegación.
- **modelo sintáctico y semántico:** resaltado por tokens no equivale a resolver nombres o tipos.
- **language server protocol:** lsp estandariza mensajes json-rpc entre cliente y servidor para completado, definición, referencias y diagnósticos.
- **workspace y configuración:** la raíz del workspace condiciona búsqueda de configuración, módulos y herramientas.
- **confianza y extensiones:** una extensión ejecuta código con acceso relevante al workspace.

Las definiciones son operativas para el entorno reproducible de diagnóstico. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```shell
# Evidencia mínima, independiente del editor
python --version
python -c "import sys; print(sys.executable); print(*sys.path, sep='\n')"
python -m unittest -v
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En el entorno reproducible de diagnóstico, una investigación conserva síntoma, entorno, reproducción, hipótesis, observaciones, causa, corrección y regresión. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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

El entorno reproducible de diagnóstico parte de una inversión de empates en la biblioteca de estructuras y algoritmos, captura versión y entrada mínima, compara un entorno sano con uno afectado y conserva la primera divergencia observable. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Una técnica o herramienta determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar técnicas es válido si las fronteras preservan identidad, orden, errores y evidencia.

### ¿Más automatización o menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todas las herramientas mencionadas?

No. Instala solo lo necesario para la práctica elegida. Registra versión y comandos; si solo analizas una notación o salida, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Configura el LSP con un intérprete diferente al terminal integrado. Compara `sys.executable`, ruta del servidor y diagnóstico; fija la selección en configuración versionable cuando sea portable.

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
work/SE-097/
├── README.md
├── diagnostic_environment/
│   ├── domain.py
│   └── se_097.py
├── fixtures/cases.json
├── tests/test_se_097.py
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


## Fuentes



- [Language Server Protocol 3.18](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/) — Mensajes, capacidades y sincronización entre editor y servidor; autoridad: Microsoft.
- [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) — Breakpoints, frames, variables y negociación de capacidades; autoridad: Microsoft.
- [Python Debugging and Profiling](https://docs.python.org/3/library/debug.html) — Pdb, cprofile, timeit, tracemalloc y límites instrumentales; autoridad: Python Software Foundation.
- [Python venv](https://docs.python.org/3/library/venv.html) — Aislamiento de intérprete, scripts y entorno virtual; autoridad: Python Software Foundation.
- [Development Container Specification](https://containers.dev/implementors/spec/) — Configuración reproducible de herramientas y ciclo de vida del contenedor; autoridad: Dev Container Specification maintainers.
- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/) — Percepción, operación por teclado y reducción de barreras en interfaces; autoridad: W3C.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación del entorno reproducible de diagnóstico sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

Un diagnóstico estático no muestra necesariamente el estado que llevó al fallo. La siguiente clase detiene la ejecución y observa frames sin asumir que observar es neutral.

## Glosario

- **editor e ide:** un editor manipula texto y puede integrar capacidades; un ide reúne proyecto, build, ejecución, depuración y navegación.
- **modelo sintáctico y semántico:** resaltado por tokens no equivale a resolver nombres o tipos.
- **language server protocol:** lsp estandariza mensajes json-rpc entre cliente y servidor para completado, definición, referencias y diagnósticos.
- **workspace y configuración:** la raíz del workspace condiciona búsqueda de configuración, módulos y herramientas.
- **confianza y extensiones:** una extensión ejecuta código con acceso relevante al workspace.

---

[← SE-096 — Proyecto: biblioteca comparada con casos límite](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-096-proyecto-biblioteca-comparada-con-casos-limite/README.md) · [↑ Parte 08](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-08-entornos-herramientas-y-depuracion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-097.html) · [SE-098 — Depuradores, breakpoints y observación de estado →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-08-entornos-herramientas-y-depuracion/se-098-depuradores-breakpoints-y-observacion-de-estado/README.md)
