# SE-119 — Taller: empaquetar una capacidad reusable

[← SE-118 — Diseño de experiencia para desarrolladores](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) · [↑ Parte 09](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-119.html) · [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md)

> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica.

## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para empaquetar una capacidad reutilizable con API, metadata, documentación y consumidor externo.

**Por qué aparece aquí.** Se sitúa después de **Diseño de experiencia para desarrolladores** y antes de **Proyecto: SDK y CLI con compatibilidad verificada**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Probar solo desde el árbol fuente y confundir eso con instalación.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Sdist/wheel, instalación aislada, consumidor, licencia y comprobación de metadata. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** El taller no publica ni promete mantenimiento futuro.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) | Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) | Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [REUSE Specification](https://reuse.software/spec-3.3/) | Declaración inequívoca y verificable de copyright y licencias por archivo; autoridad: Free Software Foundation Europe | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **producto reutilizable con SDK y CLI de la Parte 09**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Taller: empaquetar una capacidad reusable** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Cómo demostrar que una capacidad reusable sobrevive a build, instalación y uso externo?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

El taller debe extraer `choose_next` de la biblioteca de estructuras y algoritmos sin exponer internals, construir wheel/sdist, instalar en un proyecto consumidor y comprobar API y CLI.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Slice reusable] --> N2[Diseño desde consumidor] --> N3[Artefacto e instalación] --> N4[API / CLI coherentes] --> N5[Cambio compatible]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Slice reusable | Se elige una capacidad pequeña con entrada, salida, errores y dependencia claros. | Predicción, traza causal y contraejemplo de **Slice reusable** en `sdist/wheel` |
| Diseño desde consumidor | La prueba se escribe desde un directorio externo usando solo imports públicos. | Predicción, traza causal y contraejemplo de **Diseño desde consumidor** en `sdist/wheel` |
| Artefacto e instalación | Se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio. | Predicción, traza causal y contraejemplo de **Artefacto e instalación** en `sdist/wheel` |
| API y CLI coherentes | Ambas superficies llaman el mismo núcleo pero adaptan errores a su medio. | Predicción, traza causal y contraejemplo de **API y CLI coherentes** en `sdist/wheel` |
| Cambio compatible | Se agrega una opción sin romper consumidor anterior y se ejecutan ambas pruebas. | Predicción, traza causal y contraejemplo de **Cambio compatible** en `sdist/wheel` |
## Conceptos y decisiones

### 1. Slice reusable

Se elige una capacidad pequeña con entrada, salida, errores y dependencia claros. Extraer todo el sistema crea una API extensa antes de entender consumidores. El slice conserva semántica y deja adaptadores en el producto original.

### 2. Diseño desde consumidor

La prueba se escribe desde un directorio externo usando solo imports públicos. Mocks de internals no participan. Esto revela nombres, defaults, errores y documentación que el autor daba por supuestos.

### 3. Artefacto e instalación

Se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio. Ejecutar desde checkout no cuenta. Los hashes del artefacto se conservan para comparar lo probado con lo entregado.

### 4. API y CLI coherentes

Ambas superficies llaman el mismo núcleo pero adaptan errores a su medio. La CLI no captura una excepción de dominio para devolver éxito; el SDK no imprime. Fixtures compartidos comprueban equivalencia observable.

### 5. Cambio compatible

Se agrega una opción sin romper consumidor anterior y se ejecutan ambas pruebas. El taller propone versión según API declarada y revisa changelog/migración. El número se decide después de clasificar el cambio.

## Definiciones de trabajo

- **slice reusable:** se elige una capacidad pequeña con entrada, salida, errores y dependencia claros.
- **diseño desde consumidor:** la prueba se escribe desde un directorio externo usando solo imports públicos.
- **artefacto e instalación:** se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio.
- **api y cli coherentes:** ambas superficies llaman el mismo núcleo pero adaptan errores a su medio.
- **cambio compatible:** se agrega una opción sin romper consumidor anterior y se ejecutan ambas pruebas.

Las definiciones son operativas para el producto reutilizable con SDK y CLI. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```shell
python -m build
python -m venv consumer/.venv
consumer/.venv/Scripts/python -m pip install dist/engineering_sdk-*.whl
consumer/.venv/Scripts/python consumer/check_api.py
consumer/.venv/Scripts/engineering_sdk choose --input consumer/cases.json
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En el producto reutilizable con SDK y CLI, un release contiene contrato público, artefactos inmutables, dependencias, procedencia, ejemplos, errores y ruta de migración. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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
2. **Construcción:** añade una capacidad pública y prueba el comportamiento desde un proyecto consumidor.
3. **Frontera:** cubre vacío, empate, no autorizado e inválido con resultados distintos.
4. **Contraste:** reescribe una pieza con otro modelo y explica una mejora y una pérdida.

## Reto verificable

Entrega implementación, fixtures, pruebas y un informe corto. Se aprueba si otra persona ejecuta desde checkout limpio, obtiene los mismos resultados y puede relacionar cada rama o transformación con una regla del dominio. No se aprueba por cantidad de archivos ni por usar la sintaxis característica del paradigma.

## Caso conductor

El producto reutilizable con SDK y CLI empaqueta el motor de la biblioteca de estructuras y algoritmos como `engineering_sdk`, expone `choose_next`, una CLI y un punto de extensión. Ejecuta instalación limpia, entrada válida, configuración ausente, plugin incompatible y actualización entre dos versiones. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Una técnica o herramienta determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar técnicas es válido si las fronteras preservan identidad, orden, errores y evidencia.

### ¿Más automatización o menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todas las herramientas mencionadas?

No. Instala solo lo necesario para la práctica elegida. Registra versión y comandos; si solo analizas una notación o salida, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

El consumidor importa `engineering_sdk._internal`. Renombra internals y la prueba rompe: corrige al contrato público o reconoce que esa superficie ya se volvió pública.

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
work/SE-119/
├── README.md
├── engineering_sdk/
│   ├── domain.py
│   └── se_119.py
├── fixtures/cases.json
├── tests/test_se_119.py
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


- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.
- [SPDX Specification 3.0](https://spdx.dev/use/specifications/) — Identificadores, sbom y procedencia legible por máquinas; autoridad: Linux Foundation.
- [REUSE Specification](https://reuse.software/spec-3.3/) — Declaración inequívoca y verificable de copyright y licencias por archivo; autoridad: Free Software Foundation Europe.

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación del producto reutilizable con SDK y CLI sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

El taller verifica una versión y un entorno principal. El proyecto siguiente construye una matriz de compatibilidad, plugin, automatización y procedencia para SDK+CLI.

## Glosario

- **slice reusable:** se elige una capacidad pequeña con entrada, salida, errores y dependencia claros.
- **diseño desde consumidor:** la prueba se escribe desde un directorio externo usando solo imports públicos.
- **artefacto e instalación:** se construyen sdist y wheel, inspeccionan contenidos y se instalan en venv limpio.
- **api y cli coherentes:** ambas superficies llaman el mismo núcleo pero adaptan errores a su medio.
- **cambio compatible:** se agrega una opción sin romper consumidor anterior y se ejecutan ambas pruebas.

---

[← SE-118 — Diseño de experiencia para desarrolladores](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-118-diseno-de-experiencia-para-desarrolladores/README.md) · [↑ Parte 09](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-119.html) · [SE-120 — Proyecto: SDK y CLI con compatibilidad verificada →](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-120-proyecto-sdk-y-cli-con-compatibilidad-verificada/README.md)
