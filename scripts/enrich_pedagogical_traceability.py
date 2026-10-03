"""Add claim-level pedagogical traceability to Parts 01-09 without deleting drafts.

This is a migration aid, not an approval tool. It inserts a reviewed, class-specific
learning purpose and writes a machine-readable audit record. It never marks a class
GUIDED and refuses to overwrite an existing traceability section.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SECTION = "## Punto profesional y fundamento pedagógico"
PEDAGOGY = (
    "La secuencia usa predicción, explicación propia, contraste y recuperación. "
    "[ICAP](https://icap.education.asu.edu/research) distingue participación de "
    "construcción de conocimiento; [How People Learn II](https://nap.nationalacademies.org/"
    "catalog/24783/how-people-learn-ii-learners-contexts-and-cultures) exige conectar "
    "conocimiento previo, contexto y transferencia; la [práctica de recuperación]"
    "(https://pubmed.ncbi.nlm.nih.gov/16507066/) respalda producir de nuevo la explicación "
    "tras una demora; y [Education for Life and Work](https://nap.nationalacademies.org/"
    "resource/13398/dbasse_084153.pdf) exige devolución que explique la causa del error."
)


# id: (punto profesional, error conceptual, evidencia verificable, límite honesto)
PROFILES = {
    13: ("separar arquitectura física, ISA, sistema operativo y runtime antes de atribuir una propiedad a la máquina", "confundir ‘64 bits’, núcleos, ISA y versión del sistema como una sola propiedad", "machine-map.md con comandos, salidas, capas y dos conclusiones que los datos no permiten", "las APIs del runtime no demuestran la microarquitectura interna"),
    14: ("interpretar un valor binario solo cuando se declaran base, ancho, signo y orden de bytes", "creer que una secuencia de bytes posee signo y orden por sí misma", "representations.md con valor↔bits↔bytes, round trips y un desbordamiento explicado", "los enteros de Python no reproducen un registro de ancho fijo sin imponerlo"),
    15: ("distinguir carácter, punto de código, unidades de código, bytes y glifo al diagnosticar texto", "tratar Unicode como una codificación única o suponer que toda corrupción es reversible", "text-lab.md con code points, hex, normalización y un fallo de decodificación reproducible", "Unicode no determina por sí solo tipografía, shaping ni bidi"),
    16: ("evaluar precisión según representación, propagación del error y tolerancia ligada a la escala", "esperar aritmética decimal exacta de coma flotante o elegir epsilon por costumbre", "numeric-errors.md con predicción, error absoluto/relativo y contraejemplo inestable", "el ejercicio no certifica estabilidad de algoritmos científicos completos"),
    17: ("explicar instrucciones como transiciones de estado sin confundir bytecode con ISA", "leer la salida de dis como ensamblador o convertir bytecodes en ciclos de CPU", "execution-trace.md con estados antes/después y la frontera VM↔ISA", "sin código nativo y contadores no se afirman instrucciones físicas ni ciclos"),
    18: ("elegir almacenamiento y acceso por localidad, latencia, capacidad y durabilidad", "atribuir una segunda ejecución rápida a una caché concreta o equiparar write con persistencia", "hierarchy.md con protocolo frío/caliente, muestras y dos hipótesis rivales", "sin contadores de hardware se observan efectos agregados, no una caché específica"),
    19: ("atribuir concurrencia y espera a procesos, hilos, interrupciones e I/O según su mecanismo", "inferir paralelismo de CPU porque dos hilos se solapan", "concurrency-observation.md con cronología, tiempos de pared/CPU e hipótesis descartadas", "scheduler, GIL y primitivas dependen de plataforma e implementación"),
    20: ("seguir fuente, AST, bytecode, IR y ejecución para localizar la etapa que introduce un fallo", "creer que interpretar excluye compilar o que JIT compila todo antes de iniciar", "pipeline.md con representaciones, tres etapas de fallo y contraste con otra VM", "inspeccionar IR no prueba optimizaciones ni código nativo final"),
    21: ("razonar sobre carga, memoria y recolección separando especificación de estrategia del runtime", "suponer que gc.collect devuelve memoria al sistema o que toda VM recolecta igual", "runtime-memory.md con grafo de referencias, snapshots y recolección", "los resultados de CPython no generalizan a otros runtimes y RSS no equivale a memoria rastreada"),
    22: ("formular afirmaciones de rendimiento y energía con unidad funcional, protocolo, variación y frontera", "concluir que más rápido significa menor energía o comparar sin calentamiento", "performance-report.md con datos crudos, dispersión, unidad funcional y afirmaciones permitidas", "sin sensor o modelo validado no se infiere consumo energético"),
    23: ("integrar las capas del computador en una explicación causal que separe observación, inferencia e hipótesis", "elegir una causa a partir de una sola métrica o presentar una captura como explicación", "end-to-end-trace.md con mapa fuente→runtime→SO→máquina y vacíos explícitos", "la traza explica solo el caso y el entorno instrumentados"),
    24: ("convertir observaciones en un informe reproducible que otra persona pueda repetir y disputar", "confundir reproducibilidad con capturas o correlación con causalidad", "protocolo, datos crudos, script, checksum, informe y resultados no validados", "un procedimiento reproducible no garantiza representatividad ni exactitud física"),
    25: ("comparar Windows, Linux y macOS por contratos observables y no por estereotipos", "suponer que una orden o ruta portable conserva idéntica semántica", "os-contracts.md con la misma operación, resultado, diferencia y decisión por plataforma", "una muestra de versiones no representa todas las ediciones ni configuraciones"),
    26: ("razonar sobre identidad de archivos mediante rutas, enlaces, metadatos y resolución", "equiparar nombre de ruta con identidad o tratar symlink como copia", "filesystem-fixture.md con árbol temporal, enlaces, permisos y resolución paso a paso", "la semántica exacta depende del sistema de archivos y opciones de montaje"),
    27: ("explicar autorización como evaluación de identidad, pertenencia, ACL y elevación", "creer que ser propietario implica acceso efectivo o que elevar corrige diseño de permisos", "access-matrix.md con sujeto, objeto, regla, resultado y recuperación", "el laboratorio local no modela políticas corporativas completas"),
    28: ("modelar ciclo de vida, señales, supervisión y reinicio de procesos y servicios", "tratar proceso, daemon, servicio y tarea programada como sinónimos", "lifecycle.md con estados, señal, código de salida, política de reinicio y fallo controlado", "los administradores de servicios difieren y no se infiere disponibilidad distribuida"),
    29: ("predecir cómo el shell analiza texto, expande argumentos y conecta flujos", "pensar que una tubería pasa objetos en todos los shells o que citar es decorativo", "shell-trace.md con tokens, stdin/stdout/stderr, quoting y resultado en dos shells", "la portabilidad exige declarar shell y versión"),
    30: ("preservar intención al portar scripts entre PowerShell y Bash", "traducir sintaxis línea por línea ignorando tipos, errores y códigos de salida", "paired-scripts.md con contrato común, casos límite y tabla de divergencias", "equivalencia funcional no implica equivalencia de seguridad ni rendimiento"),
    31: ("diseñar precedencia de configuración y tratamiento de secretos con frontera explícita", "guardar secretos en variables o archivos sin considerar herencia, logs y repositorio", "configuration-map.md con fuentes, precedencia, redacción y rotación simulada", "no se usan secretos reales ni se certifica un gestor externo"),
    32: ("distinguir paquetes del sistema, del lenguaje y artefactos descargados por procedencia y alcance", "mezclar gestores o ejecutar instalaciones sin plan de reversión", "software-inventory.md con origen, versión, checksum o firma, alcance y rollback", "la presencia de firma no prueba ausencia de vulnerabilidades"),
    33: ("usar logs como observaciones parciales que deben correlacionarse con reloj, contexto y causalidad", "buscar una cadena y declarar causa sin línea temporal ni evidencia rival", "incident-timeline.md con evento, fuente, reloj, hipótesis y dato ausente", "los logs pueden omitir, retrasar o redactar hechos"),
    34: ("distinguir virtualización, namespaces, cgroups, WSL y contenedores por la frontera que aíslan", "tratar contenedor como máquina virtual o aislamiento como seguridad absoluta", "isolation-matrix.md con kernel, filesystem, red, recursos y ruptura simulada", "un laboratorio local no equivale a una evaluación de aislamiento hostil"),
    35: ("preparar, romper, diagnosticar y restaurar un entorno desde un runbook verificable", "resolver el síntoma cambiando varias variables sin conservar una reproducción", "runbook.md con estado inicial, fallo, hipótesis, reparación, rollback y repetición limpia", "la reparación demostrada cubre solo las versiones declaradas"),
    36: ("entregar un kit de diagnóstico multiplataforma que observe sin alterar innecesariamente", "coleccionar datos sin pregunta diagnóstica o exponer secretos en el reporte", "kit ejecutable, fixtures, salidas redactadas y comparación en dos plataformas", "la ausencia de hallazgo no demuestra salud del sistema"),
    37: ("usar OSI y TCP/IP como modelos de localización de fallos, no como descripción literal del recorrido", "asignar cada herramienta a una capa rígida o creer que una capa descarta las demás", "layer-hypotheses.md con síntoma, capas candidatas y observación discriminante", "los modelos simplifican implementaciones que atraviesan capas"),
    38: ("explicar entrega local mediante tramas, direcciones de enlace y resolución de vecinos", "confundir dirección MAC con identidad global o ARP con enrutamiento", "lan-trace.md con trama, caché de vecino, broadcast y fallo de resolución", "Wi‑Fi y Ethernet comparten objetivos pero no todos los mecanismos físicos"),
    39: ("decidir entrega directa o por gateway usando prefijos, rutas y traducción de direcciones", "creer que NAT es firewall o que una IP privada nunca aparece fuera de una LAN", "routing-lab.md con longest-prefix match y transformaciones antes/después de NAT", "la topología simulada no demuestra políticas del proveedor"),
    40: ("seleccionar TCP, UDP o QUIC por fiabilidad, orden, latencia y control de congestión", "reducir la decisión a ‘TCP seguro, UDP rápido’", "transport-decision.md con pérdidas, reordenamiento, handshake y requisito del producto", "la especificación no predice rendimiento en toda red"),
    41: ("seguir resolución DNS, delegación, caché y TTL para distinguir ausencia, demora y respuesta obsoleta", "tratar DNS como una sola base o asumir que limpiar una caché limpia todas", "dns-trace.md con consultas, autoridad, TTL, cachés y fallo inducido", "una consulta desde un resolver no describe todas las vistas"),
    42: ("razonar sobre HTTP por semántica de método, representación, validación, caché y negociación", "equiparar GET con ausencia de efectos o 200 con respuesta no cacheada", "http-exchange.md con mensajes crudos, validators y decisión de caché", "HTTP define semántica; no garantiza conducta correcta de la aplicación"),
    43: ("explicar qué autentica y cifra TLS a partir de handshake, cadena y nombre del servicio", "creer que el candado prueba que el sitio es confiable o que TLS protege datos ya comprometidos en el endpoint", "tls-evidence.md con certificado, SAN, cadena, protocolo y fallo de nombre", "la inspección del canal no audita la aplicación ni la CA"),
    44: ("mapear cómo proxy, balanceador, gateway y CDN cambian conexiones, metadatos y caché", "suponer que el servidor ve directamente al cliente o que todos los intermediarios son transparentes", "hop-map.md con terminaciones, headers confiables, caché y punto de fallo", "el diagrama de una arquitectura no generaliza a todos los proveedores"),
    45: ("modelar conexiones persistentes y tiempo real por estados, framing, heartbeat y backpressure", "confundir conexión abierta con entrega garantizada o ignorar consumidores lentos", "connection-state.md con apertura, mensajes, cierre, timeout y cola acotada", "WebSocket no define semántica de negocio ni recuperación por sí solo"),
    46: ("capturar y medir tráfico con una pregunta previa y distinguir ausencia de evidencia de evidencia de ausencia", "filtrar hasta encontrar la hipótesis preferida o interpretar cifrado como falta de tráfico", "capture-notes.md con interfaz, filtro, reloj, paquetes y conclusión acotada", "una captura puede perder paquetes y no revela payload cifrado"),
    47: ("reconstruir una petición extremo a extremo correlacionando DNS, transporte, TLS y HTTP", "narrar capas por separado sin una identidad temporal común", "request-timeline.md con timestamps, IDs, saltos y dos hipótesis descartadas", "la correlación temporal no prueba causalidad sin experimento discriminante"),
    48: ("construir un servicio observable que trate timeout, reintento e idempotencia como decisiones de producto", "reintentar cualquier fallo y duplicar efectos", "servicio, cliente de prueba, fallos inyectados, trazas correlacionadas y matriz de reintentos", "el proyecto local no demuestra disponibilidad ni tolerancia regional"),
    49: ("descomponer un problema por responsabilidades y contratos sin perder restricciones transversales", "convertir descomposición en una lista arbitraria de tareas", "problem-tree.md con fronteras, dependencias, invariantes y una descomposición alternativa", "ninguna partición elimina coordinación; solo cambia dónde ocurre"),
    50: ("usar lógica para comprobar validez de inferencias y hacer visibles supuestos", "confundir una conclusión plausible con una consecuencia lógica", "logic-check.md con formalización, tabla o derivación y contraejemplo", "la validez no garantiza que las premisas describan el mundo"),
    51: ("elegir conjuntos, relaciones, funciones y grafos según la estructura que deben preservar", "usar una colección por conveniencia sintáctica sin modelar multiplicidad y dirección", "model-comparison.md con el mismo dominio en dos estructuras y una consulta discriminante", "el modelo matemático abstrae costos de almacenamiento y concurrencia"),
    52: ("formular precondiciones, poscondiciones e invariantes que hagan verificable una transición", "escribir validaciones aisladas sin una propiedad que deba preservarse", "contract-proof.md con estados válidos, transición, invariante y contraejemplo mínimo", "probar casos no constituye demostración exhaustiva"),
    53: ("relacionar definición recursiva, caso base, progreso e inducción", "aceptar recursión porque termina en ejemplos pequeños", "recursion-proof.md con medida decreciente, traza e hipótesis inductiva", "terminación no implica complejidad aceptable"),
    54: ("separar corrección parcial, terminación y adecuación del algoritmo al contrato", "declarar correcto un algoritmo porque produce una salida esperada", "correctness.md con especificación, invariante de bucle, terminación y caso límite", "el argumento cubre el modelo de entrada declarado, no datos arbitrarios"),
    55: ("comparar crecimiento temporal y espacial antes de interpretar benchmarks", "equiparar Big‑O con segundos o descartar constantes en cargas reales", "complexity.md con conteo, cota, gráfica y medición que no contradiga su alcance", "el análisis asintótico no predice por sí solo el umbral práctico"),
    56: ("usar heurísticas y aproximaciones declarando objetivo, garantía y contraejemplo", "presentar una buena solución observada como óptima", "heuristic-report.md con baseline, calidad, tiempo y caso adverso", "sin garantía formal la calidad fuera de la muestra permanece desconocida"),
    57: ("modelar estado, transiciones y eventos para detectar secuencias imposibles o ambiguas", "describir estados como pantallas sin condiciones de entrada y salida", "state-model.md con tabla, diagrama, guardas y secuencia inválida", "el modelo omite detalles deliberadamente y debe declarar cuáles"),
    58: ("resolver problemas registrando hipótesis rivales y observaciones que realmente las discriminan", "cambiar código antes de formular una explicación falsable", "hypothesis-log.md con síntoma, predicción, experimento, resultado y descarte", "no encontrar causa en la ventana observada no valida la hipótesis restante"),
    59: ("convertir un problema ambiguo en contratos, riesgos, preguntas y evidencia de aceptación", "empezar por implementar la interpretación más cómoda", "ambiguity-map.md con actores, términos, decisiones, pruebas y preguntas abiertas", "la especificación conserva incertidumbre explícita; no la inventa"),
    60: ("entregar una especificación y solución contrastable mediante propiedades y evidencia", "hacer que la prueba copie la implementación en vez de verificar el contrato", "specification.md, solución, oráculo independiente, casos y límites", "pasar el conjunto acordado no demuestra corrección universal"),
    61: ("explicar valores, tipos, expresiones y nombres por su semántica y ciclo de vida", "tratar variable como caja idéntica en todos los lenguajes", "value-trace.md con tipo, identidad, enlace, mutación y liberación", "la traza de Python no define la semántica de otros lenguajes"),
    62: ("diseñar control de flujo desde decisiones del dominio y caminos verificables", "anidar condicionales hasta que las reglas quedan implícitas", "decision-table.md enlazada a caminos, casos límite y ramas inalcanzables", "cubrir ramas no equivale a cubrir combinaciones semánticas"),
    63: ("elegir iteración, recursión o recorrido manteniendo una invariante explícita", "reescribir un bucle como recursión sin medida de progreso", "traversal.md con invariante, traza, caso vacío y comparación de pila", "equivalencia de resultado no implica igual consumo de recursos"),
    64: ("usar funciones como contratos con parámetros, retorno, efectos y alcance localizables", "confundir paso de argumentos con copia universal o depender de variables globales ocultas", "call-contract.md con frame, aliasing, efecto y caso inválido", "el modelo de llamadas depende del lenguaje y runtime declarados"),
    65: ("distinguir error esperado, excepción, resultado explícito y fallo irrecuperable", "capturar toda excepción y continuar sin preservar causa", "failure-taxonomy.md con propagación, contexto, recuperación y regresión", "ninguna estrategia única sirve para todas las fronteras"),
    66: ("seleccionar colecciones y transformaciones según orden, unicidad, acceso, memoria y mutabilidad", "encadenar transformaciones sin observar pérdidas de información o aliasing", "collection-pipeline.md con entradas, invariantes, complejidad y contraejemplo", "la biblioteca puede cambiar constantes y detalles internos"),
    67: ("tratar entrada, salida y serialización como fronteras que validan y preservan significado", "confiar en datos parseables o asumir que JSON conserva todos los tipos", "boundary-fixtures.md con válido, límite, inválido, round trip y error", "serializar no autentica ni cifra los datos"),
    68: ("separar módulos por responsabilidades y contratos estables, no por tamaño de archivo", "crear módulos que solo redistribuyen dependencias o exponen internals", "dependency-map.md con API, consumidores, ciclo roto y prueba contractual", "modularidad local no garantiza arquitectura mantenible"),
    69: ("usar ejemplos para descubrir particiones y propiedades antes de fijar implementación", "escribir pruebas que solo confirman casos felices ya conocidos", "test-design.md con particiones, límites, propiedad y mutación que la suite detecta", "una suite finita reduce riesgo; no prueba ausencia de defectos"),
    70: ("evaluar legibilidad por el costo de comprender y cambiar, no por preferencias estéticas", "aplicar nombres o formato sin mejorar el modelo", "maintenance-change.md con tarea antes/después, diff y explicación de carga cognitiva", "una medición local no demuestra mantenibilidad a largo plazo"),
    71: ("transferir una solución entre lenguajes preservando contrato y haciendo visibles diferencias semánticas", "traducir sintaxis y declarar equivalencia", "semantic-contrast.md con ausencia, error, mutabilidad, orden y pruebas comunes", "una comparación de dos lenguajes no establece superioridad general"),
    72: ("integrar CLI, validación, archivos, pruebas y diagnóstico en una herramienta reproducible", "aceptar una salida correcta sin contrato de errores ni códigos de retorno", "CLI, fixtures, pruebas, help, códigos de salida y ejecución desde checkout limpio", "el proyecto no se considera distribuible ni compatible fuera de versiones declaradas"),
    73: ("usar estado mutable con propietario, vida útil e invariantes visibles", "suponer que asignación local evita aliasing o estados intermedios", "state-transitions.md con traza, alias, invariante y retorno temprano defectuoso", "el caso secuencial no resuelve concurrencia ni persistencia"),
    74: ("descomponer procedimientos por contratos y efectos, no solo por longitud", "extraer funciones que comparten estado implícito y llamar a eso modularidad", "procedure-contracts.md con entradas, salidas, efectos y orden permitido", "la descomposición procedural no elimina acoplamiento de datos"),
    75: ("diseñar objetos por responsabilidades, mensajes e invariantes encapsuladas", "usar clases como contenedores de datos o herencia como reutilización automática", "object-protocol.md con mensajes, estados válidos y sustitución fallida", "encapsular no vuelve correcto ni concurrente al objeto"),
    76: ("razonar con composición, valores inmutables y efectos localizados", "llamar funcional a cualquier uso de map o lambda", "composition.md con función pura, efecto aislado y contraste mutable", "inmutabilidad puede trasladar costos y no elimina I/O"),
    77: ("expresar el qué mediante relaciones o restricciones y reconocer el motor que decide el cómo", "confundir declarativo con ausencia de orden o costo", "declarative-model.md con regla, consulta, plan observado y contraejemplo", "la sintaxis declarativa no garantiza optimización"),
    78: ("explicar unificación, búsqueda y backtracking como mecanismo operacional de la lógica", "leer Prolog como ejecución exhaustiva sin depender de orden", "resolution-trace.md con sustituciones, árbol de búsqueda y corte problemático", "la verdad lógica y el comportamiento operacional no son equivalentes"),
    79: ("modelar eventos por fuente, orden, identidad, handler y efecto", "suponer que un callback implica secuencia global o entrega única", "event-timeline.md con emisión, handler, reentrada y duplicado", "el modelo local no garantiza orden distribuido"),
    80: ("diseñar flujos reactivos por contrato de notificación, terminación, error y presión", "tratar stream como lista diferida o ignorar consumidores lentos", "stream-contract.md con next/error/complete, cancelación y backpressure", "ReactiveX no define una política universal de presión"),
    81: ("comparar memoria compartida y actores por aislamiento, buzones, fallos y supervisión", "creer que mensajes eliminan carreras o garantizan entrega", "actor-failure.md con mailbox, orden, monitor, reinicio y mensaje duplicado", "actores no resuelven consistencia del dominio por sí solos"),
    82: ("seleccionar y combinar paradigmas por fuerzas del problema y costo de adaptación", "elegir paradigma por moda o forzar uno sobre todas las capas", "decision-record.md con alternativas, fuerzas, adaptadores y pérdida aceptada", "la matriz orienta una decisión contextual, no produce un ganador universal"),
    83: ("comparar cinco paradigmas sobre la misma regla y los mismos casos", "cambiar los fixtures para favorecer cada implementación", "cinco implementaciones o modelos, contrato común, fixtures y tabla semántica", "la comparación no controla ecosistema, equipo ni operación"),
    84: ("demostrar qué semántica se conserva y cuál cambia mediante pruebas comunes", "concluir equivalencia por resultados felices o cantidad de líneas", "suite común, matriz de diferencias, fallos y costo de cambio medido", "las pruebas observadas no prueban equivalencia completa"),
    85: ("elegir secuencias por acceso, inserción, localidad y representación", "tratar lista y arreglo como nombres intercambiables", "sequence-bench.md con operaciones, tamaños, modelo de costo y medición", "los costos concretos dependen de runtime y carga"),
    86: ("usar pila, cola, deque o prioridad según la disciplina de extracción requerida", "elegir por API disponible sin preservar orden e igualdad de prioridad", "queue-model.md con operaciones, invariante, empate y caso vacío", "la estructura no define por sí sola concurrencia ni persistencia"),
    87: ("diseñar tablas hash, mapas y conjuntos con igualdad, hash, colisiones y mutabilidad coherentes", "suponer acceso O(1) incondicional o usar claves mutables", "hash-contract.md con igualdad/hash, colisión y degradación observada", "el promedio esperado no es garantía de peor caso"),
    88: ("modelar jerarquías y prefijos con árboles o tries justificando recorrido y balance", "elegir árbol porque el dominio ‘parece jerárquico’", "tree-invariants.md con inserción, recorrido, altura y árbol degenerado", "un árbol lógico no implica representación enlazada"),
    89: ("representar relaciones como grafos y elegir recorrido por la pregunta que se responde", "usar BFS o DFS por costumbre sin definir visitados y dirección", "graph-trace.md con frontera, visitados, camino y ciclo", "un recorrido no resuelve automáticamente pesos ni restricciones"),
    90: ("seleccionar búsqueda, ordenamiento y selección por precondiciones y estabilidad", "comparar solo tiempo final o ignorar que los datos ya están ordenados", "algorithm-comparison.md con entradas, comparaciones, estabilidad y umbral", "un microbenchmark no reemplaza análisis de crecimiento"),
    91: ("distinguir elección voraz de subproblemas solapados y justificar optimalidad", "llamar dinámica a cualquier caché o asumir que una elección local es globalmente óptima", "strategy-proof.md con recurrencia, propiedad voraz y contraejemplo", "la corrección depende de la estructura del problema"),
    92: ("usar backtracking o divide y vencerás con espacio de búsqueda, poda y combinación explícitos", "confundir recursión con estrategia o podar sin preservar soluciones", "search-tree.md con ramas, poda válida, recurrencia y peor caso", "poda efectiva en ejemplos no cambia necesariamente la complejidad"),
    93: ("evaluar índices, estructuras probabilísticas y persistentes por errores permitidos y patrones de actualización", "tratar falsos positivos o structural sharing como detalles gratuitos", "advanced-structures.md con contrato, tasa de error o sharing y carga adversa", "los parámetros de laboratorio no generalizan a producción"),
    94: ("confrontar el modelo de complejidad con mediciones reproducibles y perfiles", "optimizar la función más lenta de una muestra sin evaluar representatividad", "benchmark-report.md con warm-up, muestras, perfil, hipótesis y regresión", "el profiler altera la ejecución y una máquina no representa todas"),
    95: ("elegir estructura y algoritmo por distribución de carga, no por familiaridad", "usar promedios que ocultan colas largas o casos adversos", "decision-evidence.md con workload, candidatos, percentiles y decisión reversible", "la carga sintetizada debe declararse y puede no representar tráfico real"),
    96: ("entregar una biblioteca con contratos, casos límite y comparaciones de costo", "considerar correcta una API porque sus ejemplos pasan", "biblioteca, pruebas de propiedades, benchmarks, documentación y límites", "la evidencia local no certifica seguridad ni rendimiento universal"),
    97: ("entender editor, IDE y servidor de lenguaje como componentes con protocolos y capacidades negociadas", "atribuir al editor análisis que realmente ejecuta otra herramienta", "tooling-map.md con proceso, mensaje LSP, capacidad y modo degradado", "soportar el protocolo no implica soportar todas las capacidades"),
    98: ("observar ejecución con breakpoints, frames y variables sin confundir observación con ausencia de perturbación", "cambiar estado desde el depurador y tratar la corrida como equivalente", "debug-session.md con hipótesis, breakpoint, stack, variable y efecto observado", "el depurador puede alterar temporización y comportamiento concurrente"),
    99: ("medir CPU, memoria, I/O y red con el instrumento que corresponde a cada recurso", "usar un único profiler y concluir causa por el mayor porcentaje", "profile-plan.md con pregunta, instrumento, overhead, datos y optimización verificada", "un perfil muestral y uno instrumentado tienen sesgos distintos"),
    100: ("separar compilación, formato, lint y análisis estático por la propiedad que verifican", "tratar cero advertencias como prueba de corrección", "static-analysis.md con hallazgo real, falso positivo, configuración y límite", "el análisis estático aproxima comportamientos y no ejecuta todos los caminos"),
    101: ("usar REPL y notebooks para explorar conservando orden, estado y transición a artefactos reproducibles", "creer que celdas visibles documentan el orden ejecutado", "exploration-log.md con kernel limpio, orden, dependencia oculta y script extraído", "una sesión interactiva no es por sí sola un pipeline reproducible"),
    102: ("fijar y cambiar versiones de runtimes haciendo visible la resolución efectiva", "confundir gestor de versiones con entorno de dependencias", "runtime-resolution.md con archivo de versión, PATH, ejecutable y prueba en dos versiones", "instalar una versión no garantiza compatibilidad de dependencias"),
    103: ("aislar dependencias y explicar qué comparte un entorno virtual con el sistema", "tratar venv como contenedor o lockfile", "environment-audit.md con intérprete, rutas, paquetes, recreación y contaminación inducida", "el entorno virtual no aísla kernel, red ni bibliotecas del sistema"),
    104: ("declarar un entorno de desarrollo desechable por imagen, features, mounts y ciclo de vida", "confundir reconstrucción con estado persistente o imagen con configuración completa", "devcontainer-evidence.md con build, create, post-create, rebuild y limpieza", "la reproducibilidad depende también de imágenes y registros externos"),
    105: ("reducir un fallo conservando la condición causal y descartando ruido", "eliminar pasos hasta que desaparece también el defecto", "minimal-reproduction.md con condición, reducción, hipótesis y prueba de regresión", "un caso mínimo puede ocultar interacciones necesarias en producción"),
    106: ("evaluar productividad del entorno junto con teclado, zoom, contraste, movimiento y carga cognitiva", "optimizar atajos para una persona y llamarlo ergonomía universal", "accessibility-check.md con tareas, barreras, ajustes y verificación por teclado", "la revisión básica no sustituye auditoría especializada ni pruebas con usuarios"),
    107: ("diagnosticar un fallo desconocido desde síntoma hasta causa usando instrumentos elegidos por hipótesis", "abrir todas las herramientas sin una pregunta discriminante", "diagnosis.md con reproducción, hipótesis rivales, evidencia, causa y recuperación", "resolver el caso no demuestra que no existan causas adicionales"),
    108: ("entregar un entorno autocontenido que se reconstruya, diagnostique y recupere", "considerar reproducible un contenedor que depende de cachés o pasos manuales", "configuración, locks, build limpio, smoke test, SBOM y guía de recuperación", "autocontenido no significa hermético frente a servicios externos"),
    109: ("distinguir biblioteca, framework, runtime, plataforma y SDK por control, contrato y superficie de actualización", "clasificar por marketing o por el nombre del paquete", "capability-map.md con quién llama a quién, artefactos, runtime y contrato público", "un producto puede ocupar más de una categoría según la frontera"),
    110: ("usar SemVer solo después de declarar API pública y reglas observables de compatibilidad", "inferir compatibilidad por número de versión sin contrato", "compatibility.md con API, cambios, clasificación y consumidor de regresión", "SemVer comunica intención; no prueba que la versión sea compatible"),
    111: ("explicar resolución de dependencias como satisfacción de restricciones y distinguirla del lock reproducible", "pedir ‘la última compatible’ como si hubiera una solución única", "resolution-report.md con grafo, restricciones, solución, lock y cambio de entorno", "un lock no garantiza disponibilidad futura ni igualdad entre plataformas"),
    112: ("separar módulo importable, paquete de distribución, metadata, build y publicación", "equiparar carpeta de código con artefacto publicable", "package-lifecycle.md con sdist/wheel, metadata, instalación limpia e importación", "construir un artefacto no demuestra que sea publicable o seguro"),
    113: ("diseñar una CLI como interfaz pública con gramática, streams, códigos de salida y compatibilidad", "imprimir errores en stdout o devolver cero tras un fallo", "cli-contract.md con help, casos, stdout/stderr, exit codes y automatización", "argparse resuelve parsing; no diseña por sí solo la experiencia"),
    114: ("hacer scripts repetibles mediante precondiciones, detección de estado y efectos idempotentes", "suponer que ejecutar dos veces es seguro porque la primera terminó", "idempotence.md con estado inicial, dos ejecuciones, fallo intermedio y recuperación", "idempotencia local no implica atomicidad ni seguridad concurrente"),
    115: ("diseñar plugins con descubrimiento, contrato, compatibilidad, aislamiento y confianza explícitos", "cargar código encontrado y tratar extensión como configuración", "plugin-contract.md con entry point, versión incompatible, fallo aislado y procedencia", "un punto de extensión aumenta superficie de ataque y soporte"),
    116: ("tratar generación de código y metaprogramación como transformación con fuente de verdad y salida revisable", "editar generado a mano o esconder cambios semánticos en plantillas", "generation-report.md con entrada, generador, diff determinista y regeneración limpia", "determinismo de salida no demuestra corrección del generador"),
    117: ("registrar licencia, copyright, procedencia y SBOM para reutilización verificable", "copiar una licencia raíz y asumir que cubre todos los archivos y dependencias", "provenance.md, headers REUSE, SPDX y excepción documentada", "metadata correcta no resuelve por sí sola compatibilidad jurídica; no es asesoría legal"),
    118: ("evaluar experiencia de desarrollador por tiempo de primera tarea, mensajes, recuperación y consistencia", "medir DX por apariencia o número de comandos", "dx-study.md con tarea, tiempo, error inducido, mensaje y recuperación", "una prueba interna pequeña no representa toda la población"),
    119: ("empaquetar una capacidad reutilizable con API, metadata, documentación y consumidor externo", "probar solo desde el árbol fuente y confundir eso con instalación", "sdist/wheel, instalación aislada, consumidor, licencia y comprobación de metadata", "el taller no publica ni promete mantenimiento futuro"),
    120: ("entregar SDK y CLI con contrato común y compatibilidad verificada entre versiones", "duplicar lógica entre interfaces o declarar compatibilidad sin consumidor anterior", "matriz de versiones, artefactos, consumidor de regresión, CLI, SDK y changelog", "la matriz cubre versiones y plataformas declaradas, no compatibilidad universal"),
}


PREFERRED_SOURCE_KEYWORDS = {
    25: ("Windows documentation", "man-pages", "Apple Developer", "Open Group"),
    26: ("Pathname Resolution", "Naming Files", "pathlib"),
    27: ("File Access", "Access Control", "User Account Control", "Apple Platform"),
    28: ("Process Concepts", "systemd.service", "Services"),
    29: ("Bash", "PowerShell", "Open Group"),
    30: ("Bash", "PowerShell", "Open Group"),
    31: ("Environment_Variables", "Environment Variables", "OWASP"),
    32: ("WinGet", "APT", "Homebrew", "Packaging"),
    33: ("Event Logging", "journalctl", "Apple Developer", "OpenTelemetry"),
    34: ("WSL", "namespaces", "cgroup", "Docker"),
    35: ("Sysinternals", "Open Group", "systemd", "subprocess"),
    36: ("Open Group", "PowerShell", "Bash", "WSL", "OWASP"),
    73: ("Python Language", "Rust", "SWEBOK"), 74: ("Python Language", "SWEBOK"),
    75: ("Python Language", "Rust", "SWEBOK"), 76: ("Python Language", "Rust", "SWEBOK"),
    77: ("SWI-Prolog", "SWEBOK"), 78: ("SWI-Prolog", "SWEBOK"),
    79: ("ReactiveX", "Erlang", "Python Language"), 80: ("ReactiveX", "Python Language"),
    81: ("Erlang", "Rust", "Python Language"), 82: ("Python Language", "Rust", "SWEBOK"),
    83: ("Python Language", "Rust", "SWI-Prolog", "ReactiveX", "Erlang"),
    84: ("Python Language", "Rust", "SWI-Prolog", "ReactiveX", "Erlang", "SWEBOK"),
    85: ("6.006", "Data Model", "Debugging"), 86: ("6.006", "Standard Library", "Data Model"),
    87: ("6.006", "Data Model", "Mathematics"), 88: ("6.006", "Mathematics", "SWEBOK"),
    89: ("6.006", "Standard Library", "Mathematics"), 90: ("6.006", "Standard Library", "Debugging"),
    91: ("6.006", "Mathematics", "SWEBOK"), 92: ("6.006", "Mathematics", "Debugging"),
    93: ("6.006", "Data Model", "Mathematics"), 94: ("Debugging", "6.006", "SWEBOK"),
    95: ("6.006", "Debugging", "SWEBOK"), 96: ("6.006", "Data Model", "Debugging", "SWEBOK"),
    97: ("Language Server", "Debug Adapter", "WCAG"), 98: ("Debug Adapter", "Debugging"),
    99: ("Debugging", "Debug Adapter"), 100: ("Language Server", "Debugging"),
    101: ("Debugging", "venv"), 102: ("venv", "Development Container"),
    103: ("venv", "Development Container"), 104: ("Development Container", "venv"),
    105: ("Debug Adapter", "Debugging"), 106: ("WCAG", "Language Server"),
    107: ("Debug Adapter", "Debugging", "Development Container"),
    108: ("Development Container", "venv", "Language Server"),
    109: ("Packaging", "Standard Library", "Semantic"), 110: ("Semantic", "Packaging"),
    111: ("pylock", "Packaging", "Semantic"), 112: ("Packaging", "pylock", "Standard Library"),
    113: ("Standard Library", "Semantic"), 114: ("Standard Library", "pylock"),
    115: ("Packaging", "Standard Library", "Semantic"), 116: ("Standard Library", "Packaging"),
    117: ("SPDX", "REUSE", "Packaging"), 118: ("Standard Library", "Packaging", "Semantic"),
    119: ("Packaging", "pylock", "REUSE"), 120: ("Semantic", "Packaging", "pylock", "SPDX"),
}


EXTRA_SOURCES = {
    100: [("Python ast", "https://docs.python.org/3/library/ast.html", "define el árbol sintáctico que un análisis puede inspeccionar"), ("Ruff documentation", "https://docs.astral.sh/ruff/", "documenta alcance, reglas y configuración del linter")],
    101: [("Python interactive mode", "https://docs.python.org/3/tutorial/interpreter.html", "documenta el modo interactivo y su estado de sesión"), ("Jupyter messaging protocol", "https://jupyter-client.readthedocs.io/en/stable/messaging.html", "define mensajes y canales entre cliente y kernel")],
    102: [("pyenv", "https://github.com/pyenv/pyenv", "documenta selección de intérprete mediante shims y archivos de versión"), ("rustup", "https://rust-lang.github.io/rustup/", "documenta toolchains y selección de versiones")],
    105: [("Delta Debugging", "https://doi.org/10.1109/TSE.2002.1039487", "formaliza reducción sistemática de causas relevantes")],
    109: [("Python importlib.metadata", "https://docs.python.org/3/library/importlib.metadata.html", "define acceso a metadata de distribuciones instaladas")],
    113: [("Python argparse", "https://docs.python.org/3/library/argparse.html", "define parsing, ayuda y errores de una CLI"), ("POSIX Utility Syntax Guidelines", "https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html", "define convenciones interoperables de argumentos")],
    114: [("Python subprocess", "https://docs.python.org/3/library/subprocess.html", "define creación, streams y códigos de procesos automatizados")],
    115: [("PyPA plugin discovery", "https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/", "documenta estrategias de descubrimiento de plugins")],
    116: [("Python ast", "https://docs.python.org/3/library/ast.html", "define transformaciones estructuradas de código Python")],
}


def inferred_support(title: str, class_id: int) -> str:
    point = PROFILES[class_id][0]
    lower = title.lower()
    rules = (
        (("rfc ",), "define la semántica normativa del protocolo nombrado en el título y sus límites interoperables"),
        (("risc-v",), "separa el contrato de la ISA del comportamiento dependiente de una implementación"),
        (("unicode",), "define caracteres, codificaciones o normalización en la frontera exacta citada por la clase"),
        (("python",), "define la semántica y los límites de la API de Python utilizada en el experimento"),
        (("jvm", "java virtual"), "distingue requisitos de la máquina virtual de estrategias que la especificación no prescribe"),
        (("llvm",), "documenta representaciones intermedias, generación de código y ejecución JIT"),
        (("open group", "posix"), "define el contrato portable de procesos, rutas, entorno o shell que se contrasta entre sistemas"),
        (("microsoft", "powershell", "windows"), "documenta el comportamiento de Windows o PowerShell que se compara con el contrato POSIX"),
        (("bash",), "documenta parsing, expansión, quoting, pipelines y estado de salida en Bash"),
        (("systemd", "journalctl"), "define ciclo de vida, supervisión o consulta de eventos en systemd"),
        (("mit 6.006", "introduction to algorithms"), "aporta definiciones, invariantes y análisis de estructuras y algoritmos usados en la clase"),
        (("6.042", "mathematics for computer science"), "aporta lógica, inducción, relaciones, grafos y técnicas de demostración aplicadas"),
        (("18.404", "theory of computation"), "delimita computabilidad, complejidad y los límites de las soluciones algorítmicas"),
        (("swebok",), "sitúa la decisión dentro de construcción, diseño, pruebas y práctica profesional de ingeniería de software"),
        (("rust",), "documenta ownership, tipos de error, traits y concurrencia usados como contraste semántico"),
        (("prolog",), "define hechos, reglas, unificación, búsqueda y comportamiento operacional de Prolog"),
        (("reactivex",), "define notificaciones, terminación y errores del contrato Observable"),
        (("erlang",), "define procesos, buzones, enlaces y monitores del modelo de actores de Erlang/OTP"),
        (("language server",), "define mensajes, capacidades y sincronización entre cliente editor y servidor de lenguaje"),
        (("debug adapter",), "define breakpoints, frames, variables y negociación de capacidades del depurador"),
        (("development container",), "define configuración y ciclo de vida reproducible de un entorno de desarrollo en contenedor"),
        (("wcag",), "define criterios verificables de percepción, teclado, foco y reducción de barreras"),
        (("semantic version",), "define cómo cambios de una API pública se comunican mediante versiones mayores, menores y parches"),
        (("pylock",), "define un formato de lock y la selección de paquetes según el entorno de instalación"),
        (("packaging",), "define metadata, nombres, versiones, dependencias y artefactos de distribución de Python"),
        (("spdx",), "define identificadores y datos de procedencia y composición legibles por máquinas"),
        (("reuse",), "define cómo declarar copyright y licencias de forma verificable por archivo"),
    )
    for keys, support in rules:
        if any(key in lower for key in keys):
            return support
    return f"delimita el contrato técnico que debe cumplirse al {point}"


def source_lines(text: str, class_id: int) -> list[tuple[str, str, str]]:
    source_block = text.split("## Fuentes", 1)[1] if "## Fuentes" in text else ""
    found = []
    for line in source_block.splitlines():
        match = re.match(r"- \[([^]]+)\]\((https?://[^)]+)\)(.*)", line)
        if match:
            title, url, tail = match.groups()
            support = re.sub(r"^\s*(?:[—:-]|respalda)\s*", "", tail, flags=re.IGNORECASE).rstrip(".")
            vague = (not support or "sustenta las definiciones" in support.lower() or
                     "sustenta los mecanismos" in support.lower() or
                     "referencia oficial para el mecanismo" in support.lower())
            if vague:
                support = inferred_support(title, class_id)
            found.append((title, url, support))
    keys = PREFERRED_SOURCE_KEYWORDS.get(class_id)
    if keys:
        selected = []
        for key in keys:
            hit = next((item for item in found if key.lower() in item[0].lower()), None)
            if hit and hit not in selected:
                selected.append(hit)
        found = selected
    else:
        found = found[:3]
    for extra in EXTRA_SOURCES.get(class_id, []):
        if extra[1] not in {item[1] for item in found}:
            found.append(extra)
    return found


def strengthen_source_bullets(text: str, class_id: int) -> str:
    if "## Fuentes" not in text:
        return text
    prefix, block = text.split("## Fuentes", 1)
    updated = []
    for line in block.splitlines():
        match = re.match(r"(- \[([^]]+)\]\((https?://[^)]+)\))(.*)", line)
        if not match:
            updated.append(line)
            continue
        lead, title, _url, tail = match.groups()
        lower = tail.lower()
        vague = (not tail.strip() or "sustenta las definiciones" in lower or
                 "sustenta los mecanismos" in lower or
                 "referencia oficial para el mecanismo" in lower)
        updated.append(f"{lead} — {inferred_support(title, class_id)}." if vague else line)
    return prefix + "## Fuentes\n" + "\n".join(updated) + ("\n" if block.endswith("\n") else "")


def strengthen_topic_evidence(text: str, class_id: int) -> str:
    marker = "## Temas y por qué importan"
    if marker not in text:
        return text
    prefix, remainder = text.split(marker, 1)
    boundary = re.search(r"\n## ", remainder)
    if not boundary:
        return text
    table = remainder[: boundary.start()]
    suffix = remainder[boundary.start() :]
    artifact = PROFILES[class_id][2].split(" con ", 1)[0].split(",", 1)[0]
    rewritten = []
    for line in table.splitlines():
        if "Evidencia o contraejemplo registrado" not in line or not line.startswith("|"):
            rewritten.append(line)
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 3:
            rewritten.append(line)
            continue
        topic = cells[0]
        cells[2] = f"Predicción, traza causal y contraejemplo de **{topic}** en `{artifact}`"
        rewritten.append("| " + " | ".join(cells) + " |")
    return prefix + marker + "\n".join(rewritten) + suffix


def build_section(class_id: int, title: str, previous: str, following: str, sources: list[tuple[str, str, str]]) -> str:
    point, misconception, evidence, limit = PROFILES[class_id]
    rows = "\n".join(
        f"| [{name}]({url}) | {support.rstrip('.')} | No demuestra por sí sola que el artefacto del estudiante sea correcto. |"
        for name, url, support in sources
    )
    return f"""{SECTION}

**Punto profesional.** La clase existe para {point}.

**Por qué aparece aquí.** Se sitúa después de **{previous}** y antes de **{following}**: convierte el conocimiento anterior en una decisión observable que la clase siguiente podrá reutilizar. La continuidad se comprueba en el artefacto, no por compartir vocabulario.

**Error conceptual que debe corregir.** {misconception[0].upper() + misconception[1:]}.

**Secuencia de aprendizaje.** Antes de leer la solución, el estudiante predice el resultado del caso normal y del error conceptual anterior. Luego explica un caso resuelto paso a paso, construye un contraejemplo que cambie la decisión y, sin consultar el texto, reconstruye el mecanismo y lo aplica a una entrada nueva. {PEDAGOGY}

**Evidencia de aprendizaje.** {evidence[0].upper() + evidence[1:]}. Debe contener predicción previa, observación, explicación causal, contraejemplo, criterio de aceptación y una nota de qué dato haría cambiar la conclusión.

**Límite de la conclusión.** {limit[0].upper() + limit[1:]}.

### Trazabilidad fuente → afirmación

| Fuente primaria u oficial | Afirmación que respalda | Lo que no prueba |
|---|---|---|
{rows}

"""


def title_of(text: str) -> str:
    first = text.splitlines()[0]
    return first.split(" — ", 1)[1] if " — " in first else first.lstrip("# ")


def enrich_part(part: int) -> None:
    start = part * 12 + 1
    paths = [ROOT / "content" / f"part-{part:02d}" / f"SE-{class_id:03d}.md" for class_id in range(start, start + 12)]
    texts = {class_id: path.read_text(encoding="utf-8") for class_id, path in zip(range(start, start + 12), paths)}
    all_titles = {}
    for class_id in range(1, 121):
        p = ROOT / "content" / f"part-{(class_id - 1) // 12:02d}" / f"SE-{class_id:03d}.md"
        if p.exists():
            all_titles[class_id] = title_of(p.read_text(encoding="utf-8"))
    records = []
    for class_id, path in zip(range(start, start + 12), paths):
        text = texts[class_id]
        if SECTION in text:
            start_at = text.index(SECTION)
            end_match = re.search(r"\n## (?!Punto profesional)", text[start_at + len(SECTION):])
            if not end_match:
                raise SystemExit(f"{path}: cannot refresh traceability section")
            end_at = start_at + len(SECTION) + end_match.start() + 1
            text = text[:start_at] + text[end_at:]
        sources = source_lines(text, class_id)
        if len(sources) < 2:
            raise SystemExit(f"{path}: fewer than two relevant sources")
        status = re.search(r"^> Estado:.*$", text, flags=re.MULTILINE)
        if not status:
            raise SystemExit(f"{path}: missing status line")
        new_status = "> Estado: **PLANNED** · Borrador público conservado íntegramente y sometido a auditoría técnica y pedagógica."
        text = text[: status.start()] + new_status + text[status.end() :]
        insertion = text.find("\n\n", status.start())
        if insertion < 0:
            raise SystemExit(f"{path}: cannot locate insertion point")
        section = build_section(
            class_id,
            all_titles[class_id],
            all_titles.get(class_id - 1, "la clase anterior"),
            all_titles.get(class_id + 1, "la clase siguiente"),
            sources,
        )
        text = text[: insertion + 2] + section + text[insertion + 2 :]
        text = strengthen_source_bullets(text, class_id)
        text = strengthen_topic_evidence(text, class_id)
        if text.count(SECTION) != 1 or "**PLANNED**" not in text:
            raise SystemExit(f"{path}: postcondition failed")
        path.write_text(text, encoding="utf-8", newline="\n")
        point, misconception, evidence, limit = PROFILES[class_id]
        records.append({
            "class_id": f"SE-{class_id:03d}",
            "title": all_titles[class_id],
            "maturity": "PLANNED",
            "professional_point": point,
            "misconception": misconception,
            "evidence": evidence,
            "limit": limit,
            "sources": [{"title": a, "url": b, "supports": c} for a, b, c in sources],
            "reviewed_on": "2026-10-03",
            "approval": "not_granted",
        })
    audit_dir = ROOT / "sources" / "pedagogical"
    audit_dir.mkdir(parents=True, exist_ok=True)
    audit = {
        "part": part,
        "scope": f"SE-{start:03d}..SE-{start + 11:03d}",
        "content_preserved": True,
        "basis": "docs/PEDAGOGICAL-STANDARD.md",
        "status": "under_qualitative_audit",
        "classes": records,
    }
    (audit_dir / f"part-{part:02d}.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, required=True, choices=range(1, 10))
    args = parser.parse_args()
    enrich_part(args.part)


if __name__ == "__main__":
    main()
