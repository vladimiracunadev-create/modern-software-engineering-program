# SE-053 — Recursión, inducción y razonamiento estructural

[← SE-052 — Invariantes, precondiciones y poscondiciones](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) · [↑ Parte 04](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-053.html) · [SE-054 — Algoritmos, corrección y terminación →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)


## Punto profesional y fundamento pedagógico

**Punto profesional.** La clase existe para relacionar definición recursiva, caso base, progreso e inducción.

**Por qué aparece aquí.** Se sitúa después de **Invariantes, precondiciones y poscondiciones** y antes de **Algoritmos, corrección y terminación**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** Aceptar recursión porque termina en ejemplos pequeños.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. La secuencia usa predicción, explicación propia, contraste y recuperación. [ICAP](https://icap.education.asu.edu/research) distingue participación de construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar conocimiento previo, contexto y transferencia; la [práctica de recuperación](https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error.

**Evidencia de aprendizaje.** Recursion-proof.md con medida decreciente, traza e hipótesis inductiva. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** Terminación no implica complejidad aceptable.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
| [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) | aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas | No demuestra por sí sola que el artefacto del estudiante sea correcto. |
| [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) | aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase | No demuestra por sí sola que el artefacto del estudiante sea correcto. |

## Antes de empezar

Esta clase continúa el **modelo de decisión diagnóstica**, que convierte la evidencia de la petición observable de extremo a extremo en una siguiente decisión explicable. Recupera `SE-052`: escribe qué artefacto dejó, qué supuesto permanece abierto y qué propiedad debe sobrevivir al nuevo modelo. La matemática se usa para restringir interpretaciones y encontrar errores; no como ornamentación.

## Prerrequisitos

- Poder separar hecho, interpretación, hipótesis y decisión.
- Manejar tablas, diagramas y pseudocódigo legible; Python es opcional.
- Trabajar con datos sintéticos del caso del modelo de decisión diagnóstica y conservar cada versión en Git.

## Problema auténtico

El árbol de diagnóstico del modelo de decisión diagnóstica contiene subárboles anidados. Una función recursiva los recorre bien en ejemplos pequeños, pero puede omitir nodos o no terminar ante ciclos. Hace falta relacionar definición recursiva, caso base, medida decreciente e inducción.

## Objetivos observables

Al finalizar podrás explicar el mecanismo con ejemplo y contraejemplo; construir un modelo con dominio y límites; derivar una prueba que pueda refutarlo; comparar al menos dos representaciones; y entregar una decisión cuya evidencia pueda revisar otra persona.

## Mapa conceptual

```mermaid
flowchart LR
    P[Problema situado] --> A[Abstracción explícita]
    A --> R[Reglas e invariantes]
    R --> S[Solución o estrategia]
    S --> C[Casos y contraejemplos]
    C --> E[Evidencia de aceptación]
    E -->|modelo insuficiente| A
```

El mapa separa el problema de su representación. Los casos no reemplazan reglas; las reglas no prueban que el problema esté bien encuadrado. La pregunta de esta clase es: **¿Qué estructura disminuye en cada llamada y por qué el argumento cubre todos los casos?**

## Temas y por qué importan

| Lente | Pregunta | Evidencia |
|---|---|---|
| dominio | ¿qué entradas y estados existen? | vocabulario y particiones |
| estructura | ¿qué relaciones se conservan? | modelo interpretado |
| regla | ¿qué debe ser cierto? | contrato o invariante |
| estrategia | ¿qué pasos producen el resultado? | pseudocódigo y traza |
| límite | ¿dónde falla el argumento? | contraejemplo y caso límite |
## Conceptos y decisiones

### 1. Definición recursiva

Una estructura recursiva se define mediante casos base y constructores que contienen estructuras menores. Un árbol vacío o hoja es base; un nodo con hijos combina subárboles. La definición excluye ciclos; si el dominio admite grafos, se requiere memoria de visitados.

### 2. Llamada y marco

Cada llamada recibe un subproblema y conserva un marco con argumentos y punto de retorno. La profundidad consume espacio. La elegancia sintáctica no evita desbordamiento; un recorrido iterativo con pila explícita puede conservar la misma lógica y controlar recursos.

### 3. Inducción matemática

Para demostrar una propiedad P(n), se prueba base y paso desde la hipótesis para un tamaño menor. La inducción fuerte permite asumir todos los tamaños anteriores. Elegir n exige una medida que refleje la estructura: cantidad de nodos restantes, no valor de un ID.

### 4. Inducción estructural

Se prueba la propiedad para cada constructor: hoja y nodo compuesto. Si el resultado es correcto para cada hijo y la combinación preserva la propiedad, lo es para todo árbol finito generado por la definición. Este argumento se alinea mejor que una inducción numérica artificial.

### 5. Recursión, ciclos y memoización

Recursión sobre un grafo sin visitados puede repetir trabajo o divergir. Un conjunto de visitados garantiza que cada vértice se expanda una vez bajo identidad estable. Memoizar reutiliza resultados de subproblemas idénticos, pero exige que dependan solo de la clave y contexto incluido.

### La recursión tiene profundidad finita

Una definición recursiva describe un problema en términos de una versión más pequeña de sí mismo, y es correcta si tiene un caso base y cada llamada se acerca a él. Pero toda implementación consume pila. En CPython 3.12.9 el límite por defecto de `sys.getrecursionlimit()` es 1000 y una función recursiva simple alcanzó una profundidad de 999 antes de lanzar `RecursionError`. Eso importa en la práctica: `json.loads` sobre una estructura anidada 100 000 veces también lanzó `RecursionError`. Una entrada hostil puede agotar la pila, de modo que los datos de tamaño no acotado (JSON, árboles, expresiones) exigen un límite de profundidad explícito o una versión iterativa con una pila propia.

![Figura 1. Límite de recursión de 1000, profundidad alcanzada de 999 y RecursionError al decodificar JSON con 100 000 niveles](../../../content/part-04/figures/se-053-limite-de-recursion.svg)

**Cómo leer la figura.** Las tres filas son tres pruebas: el límite, la profundidad real y una entrada hostil. **Dónde deja de valer:** el límite es de CPython y puede cambiarse con `sys.setrecursionlimit`, pero aumentarlo no elimina el problema (puede cerrar el proceso por desbordamiento de la pila nativa). Otros lenguajes optimizan la recursión de cola; CPython no.

### Llamadas solapadas: ingenuo frente a memoizado

La definición de Fibonacci `fib(n) = fib(n−1) + fib(n−2)` es correcta y muy costosa: calcular `fib(27) = 196 418` con la recursión directa hizo 635 621 llamadas y tardó 0,097 s; con memoización (`functools.lru_cache`) hizo 28 cálculos únicos y tardó 0,000021 s. Los subproblemas se *solapan*: `fib(25)` se recalcula varias veces. La memoización resuelve cada subproblema una vez y convierte el crecimiento exponencial en lineal sin cambiar la definición. Conviene recordar el costo: la caché usa memoria y supone que la función es pura (misma entrada, misma salida, sin efectos).

![Figura 2. Comparación de fib(27): 635621 llamadas y 0,097 s frente a 28 cálculos y 0,000021 s con memoización](../../../content/part-04/figures/se-053-fibonacci-llamadas.svg)

**Cómo leer la figura.** La tabla compara llamadas y tiempo; el cuadro explica por qué cambia la complejidad. **Dónde deja de valer:** los tiempos son de un equipo y de CPython; la proporción es lo que importa. La memoización no sirve si los subproblemas no se repiten o si las entradas son demasiado variadas para la caché.

### Inducción: demostrar y comprobar

Para demostrar que la suma de 0 a n es n(n+1)/2: el **caso base** n = 0 da 0; en el **paso inductivo**, si vale para n, la suma hasta n+1 es n(n+1)/2 + (n+1) = (n+1)(n+2)/2. Con eso queda demostrado para todo n, algo que ninguna cantidad de pruebas logra. La comprobación computacional para n de 0 a 1999 no encontró contraejemplos, y es útil por otra razón: detecta errores *en la demostración* (un paso mal escrito se delata con un caso concreto). Demostración y comprobación se contrastan; ninguna sustituye a la otra.

![Figura 3. Pasos de una demostración por inducción de la suma hasta n y la comprobación para n de 0 a 1999](../../../content/part-04/figures/se-053-induccion-comprobada.svg)

**Cómo leer la figura.** La tabla separa el caso base, la hipótesis, el paso y la comprobación. **Dónde deja de valer:** la inducción exige que la propiedad se enuncie con precisión; en programas con efectos o concurrencia, «el paso» involucra estados y se necesita un invariante más fuerte.

## Definiciones de trabajo

- **recursión:** definición o cálculo expresado mediante instancias menores.
- **caso base:** instancia resuelta sin llamada recursiva.
- **hipótesis inductiva:** propiedad asumida para estructuras menores.
- **medida:** cantidad bien fundada que disminuye.
- **memoización:** reutilización de resultados de subproblemas identificados.

Las definiciones fijan el uso en el modelo de decisión diagnóstica. Si una fuente usa otra convención, documenta la traducción. Una palabra definida no equivale a una propiedad demostrada.

## Ejemplo mínimo

Define `contar_pruebas(nodo)` para hoja y nodo con hijos. Traza llamadas para un árbol de tres niveles y demuestra por inducción estructural que cuenta cada hoja una vez.

Antes de resolver, predice el resultado y la propiedad que debería conservarse. Después marca qué parte del resultado procede de la regla y cuál depende del ejemplo.

## Ejemplo profesional

El modelo de decisión diagnóstica recorre el grafo de hipótesis con una pila explícita, límite de profundidad y conjunto de visitados. La especificación explica que un ciclo es error del modelo; no se oculta devolviendo silenciosamente una lista parcial.

La entrega profesional hace visible el costo de simplificar. Incluye al menos una alternativa descartada y la condición que obligaría a revisar la decisión.

## Práctica guiada

1. define la estructura y casos base.
2. traza pila de llamadas.
3. elige medida estrictamente decreciente.
4. escribe base e hipótesis inductiva.
5. introduce un ciclo y añade detección explícita.
6. solicita una revisión adversarial y corrige el modelo sin borrar la versión que falló.

## Ejercicios

1. **Profundidad:** mide el máximo de niveles que soporta tu recursión simple y compáralo con el límite configurado.
2. **Memoización:** cuenta las llamadas de `fib(30)` con y sin caché y explica la diferencia.
3. **Inducción:** demuestra que la suma de los primeros n impares es n² y comprueba para n de 0 a 1000.
4. **Entrada hostil:** diseña un límite de profundidad para un analizador de expresiones y justifica el valor.

## Reto verificable

Entrega `problem.md`, `model.md` y `checks.md`. Una persona revisora debe poder reconstruir dominio, supuestos, regla, resultado y límite; además debe encontrar qué caso refutaría la solución sin preguntarte oralmente.

## Demostración guiada

1. Declara el dominio y selecciona un caso pequeño calculable a mano.
2. Ejecuta la estrategia paso a paso y conserva estados intermedios.
3. Comprueba el resultado contra la definición, no contra intuición.
4. Introduce el fallo controlado y localiza la primera regla violada.
5. Repara el modelo y repite el caso original y el contraejemplo.

## Preguntas frecuentes

### ¿Cuándo prefiero una versión iterativa?

Cuando la profundidad no está acotada por el problema o cuando la entrada puede ser hostil. Una pila explícita permite fijar un límite y devolver un error controlado en lugar de agotar la pila.

### ¿La memoización siempre mejora el rendimiento?

No. Ayuda si los subproblemas se repiten y la función es pura; si no se repiten, solo gasta memoria. Medir con entradas representativas decide.

### ¿Una prueba para muchos n equivale a inducción?

No. La inducción demuestra la propiedad para todos los n; la comprobación solo para los probados. Una cubre el infinito, la otra detecta errores concretos.

### ¿Aumentar `setrecursionlimit` es una solución?

Es un parche con riesgo: una recursión muy profunda puede terminar el proceso. Se usa con límites medidos y, si la profundidad depende de la entrada, se cambia el diseño.
## Fallo controlado y diagnóstico

Elimina el caso base o llama recursivamente con el mismo nodo. Observa no terminación controlada por límite; identifica qué medida dejó de disminuir y repara el contrato.

Conserva el modelo fallido, la entrada que lo expone, la regla violada y la corrección. No ajustes solo el resultado esperado para hacer pasar el caso.


Provoca el agotamiento de la pila con un dato propio, no con una función de laboratorio: genera un JSON con 100 000 corchetes anidados y llámalo con `json.loads`. **Síntoma:** `RecursionError`. **Hipótesis:** el decodificador es recursivo y la entrada no tiene límite de profundidad. **Prueba:** mide cuántos niveles soporta (por ejemplo con 500, 900 y 1200). **Conclusión:** hay que validar la profundidad *antes* de decodificar, o rechazar entradas por encima de un máximo. Registra el límite elegido y por qué en `model.md`. No resuelvas el problema subiendo el límite sin medir.

## Errores comunes y cómo corregirlos

| Síntoma | Causa | Corrección |
|---|---|---|
| `RecursionError` con entradas grandes | Profundidad dependiente de la entrada | Limitar la profundidad o iterar con pila propia |
| La recursión tarda una cantidad exponencial | Subproblemas solapados | Memoizar o usar programación dinámica |
| La caché devuelve resultados viejos | La función no es pura | Incluir en la clave todo lo que influye |
| La demostración «funciona» con ejemplos pero no es válida | Se probó en lugar de demostrar | Escribir caso base, hipótesis y paso |
| El caso base no se alcanza nunca | El argumento no se acerca al base | Definir la medida que decrece |

## Entorno y archivos clave

```text
work/SE-053/
├── problem.md     # contexto, dominio, supuestos y exclusiones
├── model.md       # definiciones, reglas, diagrama y estrategia
├── checks.md      # ejemplos, contraejemplos y aceptación
└── review.md      # objeciones y revisión del modelo
```

El pseudocódigo debe ser independiente de lenguaje y cada diagrama necesita explicación textual. Si usas código para explorar, registra versión, entrada y salida; no lo presentes automáticamente como producto de la clase.

### Laboratorio integrado de la Parte 04

Usa el grafo cíclico de la [especificación contrastable](https://github.com/vladimiracunadev-create/modern-software-engineering-program/tree/main/labs/part-04-contrastable-spec) para escribir caso base, paso estructural y medida de nodos no visitados. Compara una formulación recursiva con `reachable()` iterativo y explica qué sucede si se elimina `visited`; semejanza con un árbol no prueba ausencia de ciclos.

## Seguridad, ética y accesibilidad

- usa incidentes sintéticos y evita convertir direcciones o usuarios en datos de práctica;
- trata autorización y privacidad como invariantes, no como pasos opcionales;
- registra a quién perjudica un falso positivo, falso negativo o prioridad automática;
- ofrece tablas y texto alternativo para diagramas y símbolos;
- define mecanismo de revisión humana y apelación para recomendaciones;
- no uses un modelo parcial para justificar una decisión irreversible.

## Puente hacia el trabajo con agentes

Los agentes recursivos —que delegan en subagentes o se reinvocan— tienen el mismo problema de profundidad que una función. Un harness debe fijar una profundidad máxima, un presupuesto de llamadas y una condición de parada explícita, porque un agente que se llama a sí mismo sin medida decreciente consume presupuesto sin límite. También conviene memoizar resultados puros (una consulta idempotente) para evitar pagar dos veces la misma llamada, y no memoizar lo que cambia entre ejecuciones.

## Transferencia

Aplica el mecanismo a otro dominio y conserva la estructura del argumento, no los nombres del modelo de decisión diagnóstica. Explica qué dominio, invariante o medida cambia. Si el razonamiento deja de funcionar, identifica el supuesto que pertenecía al caso original.

## Evaluación y evidencia

| Criterio | Para aprobar |
|---|---|
| precisión | dominio, términos y cuantificadores explícitos |
| mecanismo | pasos y relaciones explican el resultado |
| corrección | invariantes, casos o argumento adecuados a la afirmación |
| límites | contraejemplo, costo y supuestos visibles |
| revisión | trazabilidad y objeciones preservadas |

Completar archivos no concede aprobación. La evidencia debe sostener la afirmación exacta, y la revisión de otra persona debe poder contradecirla.

## Fuentes



- [MIT 6.042J — Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) — aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas.
- [MIT 6.006 — Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase.

Los cursos y SWEBOK aportan definiciones y métodos; no validan automáticamente el modelo del modelo de decisión diagnóstica. Cada aplicación se sostiene con el artefacto y sus casos.

- [Python: `sys.setrecursionlimit` y `getrecursionlimit`](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit): definición y advertencias sobre el límite de recursión, medidas en la Figura 1.
- [Python: `functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache): funcionamiento de la memoización usada en la Figura 2.
- Thomas Cormen, Charles Leiserson, Ronald Rivest y Clifford Stein, *Introduction to Algorithms* (MIT Press): recursión, programación dinámica e inducción.

## Límites y siguiente paso

Inducción demuestra una propiedad del modelo, no corrige una especificación equivocada. La próxima clase combina contrato, invariante y variante para demostrar corrección y terminación.

## Glosario

- **recursión:** definición o cálculo expresado mediante instancias menores.
- **caso base:** instancia resuelta sin llamada recursiva.
- **hipótesis inductiva:** propiedad asumida para estructuras menores.
- **medida:** cantidad bien fundada que disminuye.
- **memoización:** reutilización de resultados de subproblemas identificados.

---

[← SE-052 — Invariantes, precondiciones y poscondiciones](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md) · [↑ Parte 04](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) · [📚 Índice completo](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/classes/SE-053.html) · [SE-054 — Algoritmos, corrección y terminación →](https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-054-algoritmos-correccion-y-terminacion/README.md)
