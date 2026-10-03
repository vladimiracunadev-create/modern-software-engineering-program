# SE-088 — Árboles, tries y estructuras jerárquicas

[← SE-087 — Tablas hash, mapas y conjuntos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-088.html) · [SE-089 — Grafos y recorridos →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md)

> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica.

## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para modelar jerarquías y prefijos con árboles o tries justificando recorrido y balance.

**Por qué aparece aquí.** Se sitúa después de **Tablas hash, mapas y conjuntos** y antes de **Grafos y recorridos**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Elegir árbol porque el dominio ‘parece jerárquico’.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Tree-invariants.md con inserción, recorrido, altura y árbol degenerado. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Un árbol lógico no implica representación enlazada.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | Estructuras, algoritmos, corrección y análisis de complejidad; autoridad: MIT OpenCourseWare | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | Inducción, grafos, conteo y razonamiento discreto; autoridad: MIT OpenCourseWare | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Construcción, medición y fundamentos de ingeniería; autoridad: IEEE Computer Society | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa la **biblioteca de estructuras y algoritmos de la Parte 07**. Recupera la evidencia de la clase anterior, añade una decisión propia de **Árboles, tries y estructuras jerárquicas** y deja un artefacto que la clase siguiente deberá consumir. La pregunta activa es: **¿Qué invariante convierte una jerarquía en una estructura buscable?**

## Prerrequisitos

- Haber completado la clase anterior o reconstruir su contrato y evidencia.
- Python 3.11 o posterior, terminal, editor y Git; un segundo runtime es opcional y debe declararse.
- Trabajar con fixtures sintéticos: ninguna observación necesita datos de una persona o sistema real.

## Problema auténtico

La biblioteca de estructuras y algoritmos organiza casos por equipo, servicio y componente, y además necesita completar prefijos de etiquetas. Un diccionario plano duplica rutas y no puede listar un subárbol sin escanear todo.

## Objetivos observables

Al terminar podrás explicar los cinco mecanismos de esta clase, predecir su comportamiento antes de ejecutar, construir un caso normal y uno límite, diagnosticar el fallo controlado, comparar una alternativa y entregar evidencia que otra persona pueda reproducir.

## Mapa conceptual

```mermaid
flowchart LR
    N1[Árbol, raíz / subárbol] --> N2[Árbol de búsqueda] --> N3[Balance / rotaciones] --> N4[Trie / prefijos] --> N5[Recorridos / serialización]
    N5 -->|fallo o cambio| N1
```

El mapa se lee como una cadena de razonamiento, no como fases obligatorias del runtime. La flecha de retorno indica que un fallo o cambio de requisito obliga a revisar el modelo inicial; no autoriza a parchear solo la última salida.

## Temas y por qué importan

| Tema | Por qué cambia una decisión profesional | Evidencia mínima |
|---|---|---|
| Árbol, raíz y subárbol | Un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz. | Predicción, traza causal y contraejemplo de **Árbol, raíz y subárbol** en `tree-invariants.md` |
| Árbol de búsqueda | En un BST, claves menores y mayores se separan por subárbol. | Predicción, traza causal y contraejemplo de **Árbol de búsqueda** en `tree-invariants.md` |
| Balance y rotaciones | Árboles AVL o rojo-negro acotan altura mediante metadatos y rotaciones que preservan orden. | Predicción, traza causal y contraejemplo de **Balance y rotaciones** en `tree-invariants.md` |
| Trie y prefijos | Un trie comparte prefijos a lo largo de aristas o nodos. | Predicción, traza causal y contraejemplo de **Trie y prefijos** en `tree-invariants.md` |
| Recorridos y serialización | Preorden sirve para copiar estructura, inorden produce claves ordenadas en un BST y postorden procesa hijos antes que padre. | Predicción, traza causal y contraejemplo de **Recorridos y serialización** en `tree-invariants.md` |
## Conceptos y decisiones

### 1. Árbol, raíz y subárbol

Un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz. Profundidad, altura y grado describen forma. Una jerarquía organizacional puede no ser árbol si un nodo tiene varios padres; forzarla pierde relaciones.

### 2. Árbol de búsqueda

En un BST, claves menores y mayores se separan por subárbol. La búsqueda sigue una rama, pero cuesta proporcional a altura. Sin balance, inserciones ordenadas degeneran a lista y convierten el caso esperado logarítmico en lineal.

### 3. Balance y rotaciones

Árboles AVL o rojo-negro acotan altura mediante metadatos y rotaciones que preservan orden. La garantía cuesta trabajo en escritura y complejidad de implementación. La clase razona el mecanismo; no reimplementa un árbol productivo sin necesidad.

### 4. Trie y prefijos

Un trie comparte prefijos a lo largo de aristas o nodos. Buscar depende de longitud de la clave más que del número total, pero el alfabeto y nodos dispersos pueden consumir memoria. Comprimir caminos cambia representación, no el conjunto de claves.

### 5. Recorridos y serialización

Preorden sirve para copiar estructura, inorden produce claves ordenadas en un BST y postorden procesa hijos antes que padre. Recursión puede exceder pila en árboles profundos; una pila explícita hace visible el recurso.

## Definiciones de trabajo

- **árbol, raíz y subárbol:** un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz.
- **árbol de búsqueda:** en un bst, claves menores y mayores se separan por subárbol.
- **balance y rotaciones:** árboles avl o rojo-negro acotan altura mediante metadatos y rotaciones que preservan orden.
- **trie y prefijos:** un trie comparte prefijos a lo largo de aristas o nodos.
- **recorridos y serialización:** preorden sirve para copiar estructura, inorden produce claves ordenadas en un bst y postorden procesa hijos antes que padre.

Las definiciones son operativas para la biblioteca de estructuras y algoritmos. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo mínimo

```python
tree = {"platform": {"api": {"auth": {}, "billing": {}}}}
node = tree
for segment in "platform/api/auth".split("/"):
    node = node[segment]
assert node == {}
```

Antes de ejecutar, predice estado, resultado y error. Después registra versión, comando y salida. Si el fragmento es pseudocódigo o pertenece a otro lenguaje, etiquétalo como tal y no afirmes que fue ejecutado.

## Ejemplo profesional

En la biblioteca de estructuras y algoritmos, un caso conserva identidad, prioridad, dependencias, instante de llegada y estado de resolución. La implementación de esta clase debe conservar ese contrato aunque cambie la forma interna. El caso profesional no pregunta únicamente si produce una salida: pregunta quién puede producirla, qué estado observa, cómo falla y qué rastro permite disputar una decisión incorrecta.

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

La biblioteca de estructuras y algoritmos recibe casos del motor de reglas comparado, mantiene una frontera de trabajo priorizada y explica por qué el siguiente caso es elegible. Ejecuta una carga pequeña trazable, duplicados, prioridades iguales y una dependencia ausente. Cambia después una sola regla o condición y revisa qué archivos, pruebas y trazas debieron modificarse. Esa superficie de cambio alimenta el proyecto final de la parte.

## Preguntas frecuentes

### ¿Un paradigma determina toda la arquitectura?

No. Puede organizar un núcleo o una frontera sin dominar el sistema completo. Combinar modelos es válido si los adaptadores preservan identidad, orden, errores y evidencia.

### ¿Menos líneas significan una solución mejor?

No. La brevedad puede quitar duplicación o esconder decisiones. Se evalúan semántica, diagnóstico, costo de cambio y adecuación a la carga.

### ¿Debo instalar todos los lenguajes mencionados?

No. Python basta para la práctica base. Si usas Prolog, Rust o Erlang, registra versión y comandos; si solo analizas notación, decláralo como análisis no ejecutado.

## Fallo controlado y diagnóstico

Inserta claves ordenadas en un BST sin balance y mide altura igual a `n`. Contrasta con entrada permutada y explica por qué el promedio no es garantía.

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
work/SE-088/
├── README.md
├── algorithm_library/
│   ├── domain.py
│   └── se_088.py
├── fixtures/cases.json
├── tests/test_se_088.py
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

Cada fuente respalda el mecanismo indicado; ninguna demuestra que la implementación de la biblioteca de estructuras y algoritmos sea correcta. Esa afirmación depende de fixtures, pruebas, trazas y revisión reproducible.

## Límites y siguiente paso

Un árbol representa jerarquía, no dependencias arbitrarias o múltiples rutas. La siguiente clase generaliza a grafos y recorridos.

## Glosario

- **árbol, raíz y subárbol:** un árbol conecta nodos sin ciclos mediante relación padre-hijo y ofrece un camino único desde la raíz.
- **árbol de búsqueda:** en un bst, claves menores y mayores se separan por subárbol.
- **balance y rotaciones:** árboles avl o rojo-negro acotan altura mediante metadatos y rotaciones que preservan orden.
- **trie y prefijos:** un trie comparte prefijos a lo largo de aristas o nodos.
- **recorridos y serialización:** preorden sirve para copiar estructura, inorden produce claves ordenadas en un bst y postorden procesa hijos antes que padre.

---

[← SE-087 — Tablas hash, mapas y conjuntos](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-087-tablas-hash-mapas-y-conjuntos/README.md) · [↑ Parte 07](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-088.html) · [SE-089 — Grafos y recorridos →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-07-estructuras-de-datos-y-algoritmos/se-089-grafos-y-recorridos/README.md)
