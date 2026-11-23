# Plan maestro de auditoría y mejora curricular

Estado: **fuente canónica operativa**

Creado: 2026-10-06

Alcance base: 480 clases; ampliado a 540 por ADR-004, a 588 por ADR-006 y puesto en secuencia pedagógica con 612 posiciones (`SE-001`–`SE-612`, Partes 34 y 42 reservadas y luego desarrolladas) por ADR-007

## Cómo recuperar el contexto

Este documento conserva la misión, los criterios y el análisis clase por clase para
que una compactación de contexto o una sesión nueva no dependa del chat. Antes de una
intervención curricular amplia se lee junto con `AGENTS.md`, `ROADMAP.md`,
`docs/PEDAGOGICAL-STANDARD.md`, `docs/PROGRAM-ARCHITECTURE.md` y la auditoría de
cobertura vigente. Si hay contradicción, el estándar pedagógico gobierna la calidad,
el roadmap gobierna el programa y la auditoría vigente gobierna el estado comprobado.

Las casillas de este documento son backlog, no evidencia de madurez. Se cierran solo
cuando la parte completa supera revisión cualitativa, práctica reproducible, fuentes,
portal y gates. El commit y la auditoría vigente conservan la evidencia de cierre.

## Misión preservada

Mejorar progresivamente el repositorio existente hasta convertirlo en un programa
integral, profundo, práctico y profesional de Ingeniería de Software, cercano a 500
clases solo si la cobertura lo justifica. Se preserva el conocimiento acumulado: no se
reconstruye desde cero, no se elimina contenido válido, no se renumera para aparentar
orden y no se rompen navegación, enlaces, scripts, automatizaciones ni contratos.

El proceso obligatorio es:

**REVISAR → COMPRENDER → INVENTARIAR → CONTRASTAR → DETECTAR BRECHAS → DISEÑAR →
IMPLEMENTAR → VALIDAR → DOCUMENTAR**.

Toda mejora debe ser aditiva, compatible, coherente y trazable. Si un tema existe se
profundiza; si es parcial se completa; si está obsoleto se actualiza conservando lo
útil; si falta se integra donde corresponde; si se duplica se consolida sin pérdida.
No se replica masivamente lo que pertenece a repositorios especializados en lenguajes,
bases de datos, frameworks, ciberseguridad, IA, cloud, redes o matemática: aquí se
enseñan las decisiones propias de Ingeniería de Software y se enlaza la especialización.

## Contratos de profundidad y evidencia

La progresión general es **FUNDAMENTOS → COMPRENSIÓN → PRÁCTICA → CONSTRUCCIÓN →
INTEGRACIÓN → PRODUCCIÓN → OPERACIÓN → SISTEMAS COMPLEJOS → ARQUITECTURA → LIDERAZGO
→ EVOLUCIÓN → RETIRO**.

Cuando corresponda, cada clase recorre qué es, por qué existe, qué problema resuelve,
su mecanismo, cuándo usarla o evitarla, alternativas, ventajas, límites, trade-offs,
implementación, pruebas, fallos, observabilidad, mantenimiento, evolución, un caso
documentado, una práctica y fuentes. La secuencia pedagógica preferida es **CONCEPTO →
FUNDAMENTO → MECANISMO → EJEMPLO → IMPLEMENTACIÓN → ERROR → DEBUGGING → PRODUCCIÓN →
TRADE-OFF → EJERCICIO**. No se aceptan fichas de pocas líneas, relleno, frases
intercambiables, datos inventados ni una cuota uniforme de palabras.

Cada práctica declara entorno, versiones, preparación, archivos, criterio de éxito,
limpieza, recuperación y límites de lo realmente ejecutado. Debe producir evidencia
útil: código, pruebas, diagramas, ADR/RFC, contratos, pipelines, métricas, dashboards,
informes de incidente, postmortems, threat models, SBOM, benchmarks, planes de
migración o runbooks. La evaluación comprueba si la persona puede explicar,
implementar, probar, detectar el fallo, operar y justificar su decisión.

Los casos reales separan **HECHOS / INTERPRETACIÓN / LECCIONES**, citan fuentes
primarias y nunca completan vacíos con detalles plausibles. Las afirmaciones de
ejecución, compatibilidad, rendimiento, seguridad o cumplimiento requieren evidencia;
un agente que termina una tarea no demuestra que el software funcione.

## Cobertura obligatoria

El programa debe desarrollar, sin convertirlos en silos, fundamentos; requisitos;
diseño, patrones y arquitectura; API engineering; sistemas distribuidos; software
intensivo en datos; construcción; testing y calidad; rendimiento y resiliencia;
DevOps, Platform Engineering y DevEx; SRE, observabilidad e incidentes; seguridad,
privacidad, compliance y supply chain; Git y colaboración; legacy, evolución y retiro;
economía, estimación y experimentación; open source, InnerSource y organizaciones;
carrera y liderazgo; métodos formales y sistemas críticos; embedded, IoT y edge;
green software; accesibilidad e internacionalización; e IA aplicada.

Las fuentes se contrastan con ediciones vigentes y documentación primaria de SWEBOK,
ISO/IEC/IEEE 12207, 15288 y 29148, ISO/IEC 25010/SQuaRE, IEEE, ACM/IEEE CS2023,
OWASP, NIST, CNCF, OpenSSF, SLSA, DORA, Google SRE, WCAG/W3C y proyectos oficiales.
Las normas protegidas se explican y referencian; no se copian.

IA es transversal a requisitos, análisis, arquitectura, código, refactoring, review,
testing, documentación, debugging, DevOps, seguridad, observabilidad, incidentes y
modernización. Incluye copilots, coding y terminal agents, autonomía, multiagente,
MCP, tools, skills, memoria, context engineering, instrucciones de repositorio y
guardrails. El modelo de control es **HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS
VERIFICAN → HUMANO REVISA → SISTEMA VALIDA**. Se evalúan APIs alucinadas, dependencias
falsas, inseguridad, duplicación, drift arquitectónico, tests incorrectos, supuestos,
licencias, provenance, pérdida de contexto, loops, tokens, coste, latencia y regresión.

## Experiencias y proyectos que no pueden faltar

El estudiante debe recibir un sistema sin documentación, comprender código ajeno,
encontrar bugs difíciles, reconstruir arquitectura, investigar incidentes, estimar,
resolver requisitos contradictorios, defender y rechazar decisiones, revisar código,
modernizar legacy, diseñar APIs, añadir observabilidad, reducir deuda, decidir
build-vs-buy, calcular TCO, preparar ADR/RFC, planificar migraciones, gestionar
vulnerabilidades y EOL, y retirar sistemas.

Se preservan y mejoran los proyectos existentes. Deben existir recorridos distinguibles
de producto completo, sistema distribuido con fallos, modernización legacy, análisis
económico y cambio con IA controlada y evaluable. Cada proyecto cubre **REQUISITOS →
DISEÑO → IMPLEMENTACIÓN → TESTING → SEGURIDAD → CI/CD → DEPLOYMENT → OBSERVABILIDAD →
OPERACIÓN → INCIDENTES → MANTENIMIENTO → EVOLUCIÓN**.

Las rutas reutilizan clases para fundamentos, backend, frontend, full-stack, QA,
DevOps, SRE, platform, arquitectura, seguridad, modernización legacy, liderazgo e
ingeniería de software aumentada por IA. Glosario, bibliografía, índices y navegación
se actualizan en cada incremento; no se dejan archivos huérfanos.

## Reglas de expansión y control de cambios

La línea base original fue de 480 clases; el alcance vigente es de 612 posiciones en 51 partes (ADR-004, ADR-006 y ADR-007). No se crea un ID nuevo hasta demostrar que una
brecha posee competencia, artefacto, prerrequisitos y secuencia propios y que integrarla
en una clase existente degradaría su profundidad. Se puede superar ligeramente 500 si
la cobertura lo exige o permanecer por debajo mientras añadir contenido sería relleno.
La prioridad es **calidad > profundidad > coherencia > cantidad**.

El trabajo se publica por partes pequeñas: diagnóstico, brechas, mapa, archivos a
conservar/modificar/crear, implementación, validación, enlaces, navegación y registro
de cambios. Una parte por commit. Antes de marcarla desarrollada se revisa cada clase
completa, su guía, práctica, fuentes y salida; después se sincronizan README, STATUS,
arquitectura, auditoría, portal y About cuando corresponda.

## Línea base verificada y brechas transversales

Al crear este plan existen 8 etapas, 40 partes, 480 IDs consecutivos y 521 páginas.
`SE-001`–`SE-024` están desarrolladas; `SE-025`–`SE-408` son borradores publicados y
`SE-421`–`SE-576` son estructuras curriculares. Solo la Parte 01 tiene un laboratorio
ejecutable común, con seis pruebas. Hay tres workflows. Estos marcadores de estado se
sincronizan en la auditoría vigente; esta oración queda como línea base histórica.

Estado actual (2026-11-23): las 51 partes están desarrolladas y publicadas con CI verde
(`SE-001`–`SE-612`); sus hitos figuran como hechos en
las listas de abajo. Las Partes 34 y 42 se reservaron por
[ADR-007](adr/ADR-007-pedagogical-renumbering-and-new-parts.md), que también reordenó las partes en
secuencia pedagógica; los IDs de esta lista son los vigentes y el mapa con los anteriores está en
[`ID-MIGRATION.md`](ID-MIGRATION.md). Falta la revisión editorial humana independiente.

Brechas detectadas que se atienden parte a parte:

- actividades y rúbricas genéricas fuera de las partes aprobadas;
- guías de parte insuficientes en Partes 10–22, 24–25, 27, 29, 31–33, 35–36, 38–41, 43–44 y 46–47;
- párrafos repetidos en numerosos borradores, aunque la Parte 02 tiene menor deriva;
- validadores que detectan duplicados de documento completo pero no boilerplate interno;
- fuentes por clase demasiado gruesas y ausencia de registros estructurados para SLSA,
  OpenSSF, DORA, SPACE, OpenTelemetry, Google SRE, Backstage, Team Topologies, TLA+,
  Alloy, Function Points, COCOMO II y Monte Carlo;
- laboratorios, casos reales, proyectos y evidencia operativa insuficientes;
- Partes 35–36, 38–41, 43–44 y 46–47 no enseñables todavía y afirmaciones de madurez que deben seguir
  bloqueadas hasta su desarrollo real.

## Plan de mejora clase por clase

Cada línea nombra la mejora mínima específica que debe sobrevivir a la revisión de la
clase. No sustituye el temario vigente: lo enfoca y añade el artefacto o límite que
evita una explicación genérica.

Las Partes 23, 26, 28, 30, 37, 45 y 46–50 se añadieron por ADR-004 y ADR-006; las Partes 34 y 42 se reservaron por
ADR-007 y ya están desarrolladas. Cada casilla se marca `[x]` solo cuando existe `content/part-NN/SE-NNN.md`
y la parte completa está validada. Los IDs siguen la secuencia pedagógica vigente; el mapa con la numeración
anterior está en [`ID-MIGRATION.md`](ID-MIGRATION.md).

### Parte 00 — Profesión

- [x] `SE-001` — delimitar un producto real, sus fronteras y dependencias.
- [x] `SE-002` — analizar un caso histórico separando hechos, interpretación y lecciones.
- [x] `SE-003` — trazar ciclo de vida, decisiones, responsables y evidencia.
- [x] `SE-004` — resolver un dilema ético con afectados, deberes y límites.
- [x] `SE-005` — relacionar roles, ownership, bus factor y carga cognitiva.
- [x] `SE-006` — mantener hipótesis, incertidumbre y criterios de actualización.
- [x] `SE-007` — convertir calidad en escenarios observables, no adjetivos.
- [x] `SE-008` — comparar trade-offs y riesgo bajo contexto explícito.
- [x] `SE-009` — medir sostenibilidad e inclusión sin inferencias falsas.
- [x] `SE-010` — evaluar autoridad, vigencia y aplicabilidad de una fuente.
- [x] `SE-011` — reconstruir anatomía, licencia y gobernanza de un proyecto abierto.
- [x] `SE-012` — formular un plan profesional con hitos y evidencias verificables.

### Parte 01 — Computadores

- [x] `SE-013` — separar host, máquina virtual, runtime, sistema operativo y hardware.
- [x] `SE-014` — experimentar rango, signo, endianess y serialización.
- [x] `SE-015` — probar grafemas, normalización, bidi y mojibake.
- [x] `SE-016` — comparar coma flotante, decimal y entero escalado.
- [x] `SE-017` — seguir fuente, bytecode e instrucciones sin confundir ISA y microarquitectura.
- [x] `SE-018` — medir localidad sin inventar conclusiones sobre caché física.
- [x] `SE-019` — distinguir proceso, hilo, async, interrupción e I/O.
- [x] `SE-020` — comparar CPython, JVM y LLVM por contratos de traducción.
- [x] `SE-021` — observar GC y liberar recursos externos explícitamente.
- [x] `SE-022` — medir tiempo y recursos; tratar energía como instrumentación opcional.
- [x] `SE-023` — integrar señales desde código hasta proceso conservando evidencia cruda.
- [x] `SE-024` — entregar un informe que otra persona pueda reproducir y refutar.

### Parte 02 — Sistemas operativos y terminal

- [x] `SE-025` — construir una matriz de capacidades Windows, Linux y macOS.
- [x] `SE-026` — probar rutas, case sensitivity, enlaces, metadatos y ACL sin mutación peligrosa.
- [x] `SE-027` — aplicar mínimo privilegio, elevación controlada y rollback.
- [x] `SE-028` — ensayar procesos, señales, cancelación, servicios y tareas programadas.
- [x] `SE-029` — verificar quoting, pipes, streams, códigos de salida y encoding.
- [x] `SE-030` — implementar rutas equivalentes PowerShell/Bash con pruebas de portabilidad.
- [x] `SE-031` — definir precedencia de configuración y redacción de secretos.
- [x] `SE-032` — documentar instalación, verificación, pinning y rollback de paquetes.
- [x] `SE-033` — correlacionar logs, relojes, contexto y causa sin exponer datos.
- [x] `SE-034` — comparar VM, WSL y contenedor con límites verificables.
- [x] `SE-035` — romper, diagnosticar, reparar y volver a ejecutar un entorno seguro.
- [x] `SE-036` — entregar un kit idempotente probado por la matriz de tres sistemas operativos.

### Parte 03 — Redes

- [x] `SE-037` — diagnosticar una petición por capas con evidencia por salto.
- [x] `SE-038` — explicar Ethernet y Wi-Fi sin confundir enlace con Internet.
- [x] `SE-039` — experimentar IPv4, IPv6, routing y NAT con límites del entorno.
- [x] `SE-040` — comparar TCP, UDP y QUIC bajo latencia, pérdida y orden.
- [x] `SE-041` — probar DNS, caché negativa y límites de DNSSEC.
- [x] `SE-042` — verificar HTTP, negociación, caché y semántica de métodos.
- [x] `SE-043` — reconstruir cadena TLS, nombres, vencimiento y revocación.
- [x] `SE-044` — razonar sobre proxies, balanceo y fronteras de confianza de headers.
- [x] `SE-045` — comparar polling, SSE y WebSocket, incluida reconexión.
- [x] `SE-046` — capturar tráfico sintético con minimización y privacidad.
- [x] `SE-047` — producir una traza extremo a extremo con correlation ID.
- [x] `SE-048` — inyectar DNS, TLS, latencia y pérdida y demostrar recuperación.

### Parte 04 — Pensamiento computacional

- [x] `SE-049` — descomponer un problema y hacer visibles sus supuestos.
- [x] `SE-050` — usar tablas de verdad y contraejemplos para refutar soluciones.
- [x] `SE-051` — modelar relaciones y grafos como artefactos ejecutables.
- [x] `SE-052` — formular invariantes comprobables.
- [x] `SE-053` — conectar inducción, recursión y caso base.
- [x] `SE-054` — distinguir corrección parcial, total y terminación.
- [x] `SE-055` — separar complejidad teórica de benchmark empírico.
- [x] `SE-056` — justificar heurísticas, límites y condiciones de fallo.
- [x] `SE-057` — construir una máquina de estados ejecutable.
- [x] `SE-058` — mantener un registro de hipótesis y evidencia contraria.
- [x] `SE-059` — reconciliar un problema ambiguo y contradictorio.
- [x] `SE-060` — entregar especificación, solución, oráculo y contraejemplos.

### Parte 05 — Fundamentos de programación

- [x] `SE-061` — hacer explícitos tipos, coerciones y contratos.
- [x] `SE-062` — relacionar decisiones de control con cobertura alcanzable.
- [x] `SE-063` — usar invariantes de bucle y condiciones de término.
- [x] `SE-064` — separar alcance, efectos y contratos de funciones.
- [x] `SE-065` — comparar excepciones, Result y recuperación.
- [x] `SE-066` — diseñar transformaciones de colecciones sin mutación accidental.
- [x] `SE-067` — validar esquema, streaming y errores de E/S.
- [x] `SE-068` — controlar dependencias y límites de módulos.
- [x] `SE-069` — derivar código desde ejemplos, bordes y propiedades.
- [x] `SE-070` — revisar legibilidad con evidencia de mantenimiento.
- [x] `SE-071` — transferir la misma solución entre dos lenguajes.
- [x] `SE-072` — entregar una CLI empaquetada, probada y documentada.

### Parte 06 — Paradigmas

- [x] `SE-073` — observar estado y mutación en el paradigma imperativo.
- [x] `SE-074` — evaluar descomposición procedural y sus límites.
- [x] `SE-075` — probar encapsulación y mensajería entre objetos.
- [x] `SE-076` — razonar sobre inmutabilidad, efectos y composición funcional.
- [x] `SE-077` — construir una regla declarativa y explicar su motor.
- [x] `SE-078` — seguir resolución y fallos en programación lógica.
- [x] `SE-079` — controlar orden, reentrada y errores en eventos.
- [x] `SE-080` — probar backpressure y cancelación en flujos reactivos.
- [x] `SE-081` — ensayar supervisión y aislamiento con actores.
- [x] `SE-082` — usar una matriz contextual para combinar paradigmas.
- [x] `SE-083` — implementar una regla de negocio en cinco paradigmas.
- [x] `SE-084` — comparar implementaciones con fixtures y propiedades comunes.

### Parte 07 — Estructuras y algoritmos

- [x] `SE-085` — elegir secuencia según operaciones y carga.
- [x] `SE-086` — comparar colas, deques y prioridades.
- [x] `SE-087` — medir hashing, colisiones y adversarios.
- [x] `SE-088` — mantener invariantes de árboles y balance.
- [x] `SE-089` — tratar ciclos, pesos y alcanzabilidad en grafos.
- [x] `SE-090` — comparar búsqueda y ordenamiento por workload.
- [x] `SE-091` — contrastar greedy y programación dinámica.
- [x] `SE-092` — hacer visible poda y explosión combinatoria.
- [x] `SE-093` — evaluar estructuras probabilísticas y persistentes.
- [x] `SE-094` — diseñar benchmarks sin sesgo obvio.
- [x] `SE-095` — justificar selección con una carga representativa.
- [x] `SE-096` — entregar biblioteca de bordes con pruebas y límites.

### Parte 08 — Entornos y depuración

- [x] `SE-097` — reproducir configuración de editor y tareas.
- [x] `SE-098` — conservar una sesión de depuración explicada.
- [x] `SE-099` — perfilar una hipótesis y no una intuición vaga.
- [x] `SE-100` — explicar capacidad y límites de lint y análisis estático.
- [x] `SE-101` — hacer reproducibles notebooks y resultados.
- [x] `SE-102` — verificar una matriz de runtimes.
- [x] `SE-103` — demostrar aislamiento de entornos.
- [x] `SE-104` — reconstruir un Dev Container desde cero.
- [x] `SE-105` — minimizar un fallo conservando su causa.
- [x] `SE-106` — medir accesibilidad y carga cognitiva de herramientas.
- [x] `SE-107` — diagnosticar un sistema desconocido con hipótesis.
- [x] `SE-108` — reproducir el entorno desde un checkout limpio.

### Parte 09 — Paquetes y automatización

- [x] `SE-109` — separar contratos de biblioteca, framework y runtime.
- [x] `SE-110` — comprobar compatibilidad SemVer, no solo declararla.
- [x] `SE-111` — explicar resolución, lockfile y conflictos transitivos.
- [x] `SE-112` — publicar un artefacto reproducible.
- [x] `SE-113` — estabilizar contrato y códigos de salida de CLI.
- [x] `SE-114` — probar idempotencia y recuperación de scripts.
- [x] `SE-115` — aislar plugins y manejar incompatibilidad.
- [x] `SE-116` — evaluar riesgo y deriva de code generation.
- [x] `SE-117` — registrar licencia y provenance de dependencias.
- [x] `SE-118` — medir tiempo hasta el primer éxito del consumidor.
- [x] `SE-119` — validar el paquete desde un consumidor externo.
- [x] `SE-120` — mantener compatibilidad de SDK/CLI con clientes anteriores.

### Parte 10 — Discovery

- [x] `SE-121` — separar síntoma, problema y oportunidad.
- [x] `SE-122` — mapear actores, poder y exclusiones.
- [x] `SE-123` — diseñar entrevistas que reduzcan sesgo.
- [x] `SE-124` — mantener un mapa de supuestos.
- [x] `SE-125` — formular outcomes medibles.
- [x] `SE-126` — comparar alternativas, incluido no construir.
- [x] `SE-127` — diseñar un experimento falsable.
- [x] `SE-128` — priorizar por riesgo y evidencia.
- [x] `SE-129` — aplicar consentimiento y minimización.
- [x] `SE-130` — fijar criterios de abandono.
- [x] `SE-131` — convertir una petición en investigación.
- [x] `SE-132` — entregar un brief de producto respaldado por evidencia.

### Parte 11 — Economía y métricas

- [x] `SE-133` — modelar sostenibilidad del negocio.
- [x] `SE-134` — calcular TCO y coste de oportunidad.
- [x] `SE-135` — detectar vanity metrics.
- [x] `SE-136` — analizar cohortes y retención.
- [x] `SE-137` — diseñar telemetría con consentimiento.
- [x] `SE-138` — reconocer causalidad débil y errores estadísticos.
- [x] `SE-139` — definir guardrails y contramétricas.
- [x] `SE-140` — relacionar coste con outcome.
- [x] `SE-141` — tratar cartera como opciones reversibles.
- [x] `SE-142` — valorar reversibilidad de una decisión.
- [x] `SE-143` — construir un árbol de métricas.
- [x] `SE-144` — defender un caso económico por escenarios.

### Parte 12 — Requisitos

- [x] `SE-145` — elaborar un plan de elicitación.
- [x] `SE-146` — extraer reglas, excepciones y vocabulario de dominio.
- [x] `SE-147` — volver medibles los requisitos no funcionales.
- [x] `SE-148` — elegir entre historia, caso de uso y job story.
- [x] `SE-149` — escribir aceptación mediante ejemplos y bordes.
- [x] `SE-150` — negociar conflictos sin ocultarlos.
- [x] `SE-151` — mantener trazabilidad bidireccional.
- [x] `SE-152` — traducir regulación a controles comprobables.
- [x] `SE-153` — analizar impacto del cambio.
- [x] `SE-154` — detectar contradicciones e incompletitud.
- [x] `SE-155` — reparar un requisito defectuoso.
- [x] `SE-156` — entregar una especificación revisable.

### Parte 13 — Especificaciones y contratos

- [x] `SE-157` — elegir el grado de formalidad adecuado.
- [x] `SE-158` — usar BDD como conversación y evidencia, no ritual.
- [x] `SE-159` — verificar precondiciones, postcondiciones e invariantes.
- [x] `SE-160` — comprobar consistencia entre modelos.
- [x] `SE-161` — obtener un contraejemplo con TLA+ o Alloy y declarar límites.
- [x] `SE-162` — evolucionar esquemas de forma compatible.
- [x] `SE-163` — separar contratos OpenAPI, AsyncAPI y GraphQL.
- [x] `SE-164` — probar compatibilidad, versionado y deprecación.
- [x] `SE-165` — gobernar una fuente de verdad contractual.
- [x] `SE-166` — ejecutar contract tests contra productor y consumidor.
- [x] `SE-167` — trazar intención hasta contrato y prueba.
- [x] `SE-168` — entregar un paquete de especificación trazable.

### Parte 14 — UX, accesibilidad e i18n

- [x] `SE-169` — investigar personas, tareas y contexto sin estereotipos.
- [x] `SE-170` — probar arquitectura de información y navegación.
- [x] `SE-171` — diseñar feedback y affordances perceptibles.
- [x] `SE-172` — construir errores recuperables.
- [x] `SE-173` — aplicar criterios WCAG a un flujo concreto.
- [x] `SE-174` — verificar teclado, foco y lector de pantalla.
- [x] `SE-175` — comprobar contraste, zoom y tipografía.
- [x] `SE-176` — respetar responsive y preferencias del usuario.
- [x] `SE-177` — probar locale, plural, tiempo, moneda y RTL.
- [x] `SE-178` — realizar un estudio de usabilidad con protocolo.
- [x] `SE-179` — reparar una barrera y explicar la exclusión evitada.
- [x] `SE-180` — entregar un flujo accesible en varios locales.

### Parte 15 — Procesos y estimación

- [x] `SE-181` — seleccionar proceso según riesgo y contexto.
- [x] `SE-182` — separar principios ágiles de rituales.
- [x] `SE-183` — comparar métodos sobre el mismo caso.
- [x] `SE-184` — gestionar colas y WIP con datos.
- [x] `SE-185` — comparar Function Points, COCOMO II y rangos.
- [x] `SE-186` — modelar dependencias y camino crítico.
- [x] `SE-187` — mantener un registro de riesgos.
- [x] `SE-188` — definir DoR y DoD observables.
- [x] `SE-189` — usar métricas sin incentivar gaming.
- [x] `SE-190` — ejecutar un experimento de mejora.
- [x] `SE-191` — producir un forecast Monte Carlo reproducible.
- [x] `SE-192` — entregar un plan adaptable con intervalos.

### Parte 16 — Git y colaboración

- [x] `SE-193` — explicar objetos Git y recuperar con reflog.
- [x] `SE-194` — crear commits revisables y recuperables.
- [x] `SE-195` — resolver rebase y conflictos de forma segura.
- [x] `SE-196` — hacer review basada en riesgo.
- [x] `SE-197` — comparar branching strategies con métricas.
- [x] `SE-198` — trazar issue, cambio, revisión y release.
- [x] `SE-199` — usar CODEOWNERS sin ocultar bus factor.
- [x] `SE-200` — practicar InnerSource y función de OSPO.
- [x] `SE-201` — aplicar obligaciones de licencia.
- [x] `SE-202` — verificar firmas y provenance.
- [x] `SE-203` — rescatar una integración fallida.
- [x] `SE-204` — operar una contribución y release reales.

### Parte 17 — Documentación

- [x] `SE-205` — definir audiencia, tarea y éxito documental.
- [x] `SE-206` — separar tutorial, how-to, referencia y explicación.
- [x] `SE-207` — medir time-to-first-success.
- [x] `SE-208` — conservar alternativas rechazadas en ADR/RFC.
- [x] `SE-209` — crear diagramas con propósito y límites.
- [x] `SE-210` — probar ejemplos contra contratos.
- [x] `SE-211` — ensayar un runbook.
- [x] `SE-212` — validar publicación y enlaces.
- [x] `SE-213` — mantener un glosario relacional.
- [x] `SE-214` — distinguir documentación humana y legible por máquina.
- [x] `SE-215` — reconstruir conocimiento desde evidencia legacy.
- [x] `SE-216` — entregar un portal accesible y versionado.

### Parte 18 — CLI, TUI y servicios

- [x] `SE-217` — diseñar un contrato CLI estable.
- [x] `SE-218` — componer stdout, stderr, pipes y códigos de salida.
- [x] `SE-219` — implementar precedencia de configuración.
- [x] `SE-220` — devolver errores accionables.
- [x] `SE-221` — probar accesibilidad de una TUI.
- [x] `SE-222` — gestionar lifecycle de un daemon.
- [x] `SE-223` — diseñar jobs con leasing y concurrencia.
- [x] `SE-224` — usar checkpoints e idempotencia.
- [x] `SE-225` — verificar instalación, actualización y desinstalación.
- [x] `SE-226` — diseñar telemetría opt-in.
- [x] `SE-227` — endurecer una automatización peligrosa.
- [x] `SE-228` — entregar una herramienta operable multiplataforma.

### Parte 19 — Web y frontend

- [x] `SE-229` — construir sobre HTML semántico.
- [x] `SE-230` — explicar lifecycle de DOM y eventos.
- [x] `SE-231` — medir SSR, CSR y SSG en un caso.
- [x] `SE-232` — mantener consistencia de estado.
- [x] `SE-233` — implementar validación accesible.
- [x] `SE-234` — diseñar URLs durables.
- [x] `SE-235` — fijar Core Web Vitals y presupuestos.
- [x] `SE-236` — aplicar CSP y fronteras del navegador.
- [x] `SE-237` — resolver offline y conflictos.
- [x] `SE-238` — medir SEO sin promesas vagas.
- [x] `SE-239` — diagnosticar un flujo web degradado.
- [x] `SE-240` — entregar una aplicación offline y accesible.

### Parte 20 — Backend y APIs

- [x] `SE-241` — definir límites y ownership de servicio.
- [x] `SE-242` — aplicar semántica REST/HTTP con precisión.
- [x] `SE-243` — comparar RPC, GraphQL y gRPC.
- [x] `SE-244` — normalizar validación y errores.
- [x] `SE-245` — probar autorización por recurso.
- [x] `SE-246` — implementar idempotencia y replay seguro.
- [x] `SE-247` — tratar poison messages.
- [x] `SE-248` — controlar backpressure y uploads.
- [x] `SE-249` — diseñar caché y rate limiting.
- [x] `SE-250` — probar readiness y shutdown.
- [x] `SE-251` — reparar una API incompatible.
- [x] `SE-252` — entregar servicio con contratos y telemetría.

### Parte 21 — Móvil y escritorio

- [x] `SE-253` — modelar lifecycle del cliente.
- [x] `SE-254` — conservar estado ante suspensión.
- [x] `SE-255` — justificar nativo, híbrido o multiplataforma.
- [x] `SE-256` — resolver sync y conflictos.
- [x] `SE-257` — pedir el mínimo de permisos.
- [x] `SE-258` — probar accesibilidad por modalidad.
- [x] `SE-259` — verificar firma y distribución.
- [x] `SE-260` — diseñar offline-first.
- [x] `SE-261` — medir batería y recursos honestamente.
- [x] `SE-262` — asumir cliente hostil y sandbox.
- [x] `SE-263` — comparar dos plataformas con la misma prueba.
- [x] `SE-264` — entregar cliente sincronizable y recuperable.

### Parte 22 — Embedded, IoT y edge

- [x] `SE-265` — trazar frontera hardware/firmware.
- [x] `SE-266` — comparar buses y contratos eléctricos/lógicos.
- [x] `SE-267` — medir memoria, CPU y energía con límites.
- [x] `SE-268` — verificar deadlines y jitter de RTOS.
- [x] `SE-269` — controlar ISR y estado compartido.
- [x] `SE-270` — operar con conectividad intermitente.
- [x] `SE-271` — probar OTA y rollback.
- [x] `SE-272` — diseñar provisioning y rotación de claves.
- [x] `SE-273` — repartir decisiones entre edge y nube.
- [x] `SE-274` — analizar hazards y vida útil.
- [x] `SE-275` — simular fallos físicos y digitales con honestidad.
- [x] `SE-276` — entregar dispositivo simulado actualizable y recuperable.

### Parte 23 — Runtimes y plataformas modernas

- [x] `SE-277` — WebAssembly y WASI.
- [x] `SE-278` — WebAssembly en servidor y borde: component model.
- [x] `SE-279` — eBPF: observabilidad, red y seguridad en el kernel.
- [x] `SE-280` — GPU y aceleradores: modelo de ejecución.
- [x] `SE-281` — Rendimiento y costo en aceleradores.
- [x] `SE-282` — Contenedores, microVM y sandboxes.
- [x] `SE-283` — Hardware seguro: TEE y atestación.
- [x] `SE-284` — Computación cuántica para ingenieros de software.
- [x] `SE-285` — Criptografía poscuántica y migración.
- [x] `SE-286` — Confianza cero en la práctica.
- [x] `SE-287` — Taller: elegir y aislar un runtime para una carga no confiable.
- [x] `SE-288` — Proyecto: plataforma de ejecución aislada con evidencia.

### Parte 24 — Dominios especializados

- [x] `SE-289` — exigir reproducibilidad científica.
- [x] `SE-290` — asegurar calidad en pipelines de datos.
- [x] `SE-291` — evaluar drift y modelos ML.
- [x] `SE-292` — controlar determinismo en game loops.
- [x] `SE-293` — tratar latencia y accesibilidad en AV.
- [x] `SE-294` — formalizar invariantes contables.
- [x] `SE-295` — separar privacidad, safety y cumplimiento médico.
- [x] `SE-296` — explicar cuándo no usar blockchain.
- [x] `SE-297` — manejar CRS, tiempo y precisión geoespacial.
- [x] `SE-298` — delimitar low-code y escape hatches.
- [x] `SE-299` — comparar riesgos entre dominios.
- [x] `SE-300` — entregar un diseño profundo de dominio.

### Parte 25 — Diseño y refactorización

- [x] `SE-301` — interpretar cohesión y acoplamiento en contexto.
- [x] `SE-302` — aplicar SOLID con sus límites.
- [x] `SE-303` — preferir composición cuando las fuerzas lo justifiquen.
- [x] `SE-304` — elegir patrones por fuerzas, no por catálogo.
- [x] `SE-305` — tratar efectos y concurrencia en patrones.
- [x] `SE-306` — usar contraejemplos para code smells.
- [x] `SE-307` — construir pruebas de caracterización.
- [x] `SE-308` — diseñar para observabilidad.
- [x] `SE-309` — distinguir complejidad accidental y esencial.
- [x] `SE-310` — modelar economía de deuda técnica.
- [x] `SE-311` — refactorizar con regresión protegida.
- [x] `SE-312` — evolucionar diseño conservando compatibilidad.

### Parte 26 — Patrones de diseño, empresariales y de resiliencia

- [x] `SE-313` — criterios para usar un catálogo de patrones.
- [x] `SE-314` — goF creacionales: Factory, Builder, Singleton y Prototype.
- [x] `SE-315` — goF estructurales: Adapter, Decorator, Facade, Proxy y Composite.
- [x] `SE-316` — goF conductuales: Strategy, Observer, Command, State y Template Method.
- [x] `SE-317` — gRASP y asignación de responsabilidades.
- [x] `SE-318` — repository, Unit of Work y Active Record.
- [x] `SE-319` — enterprise Integration Patterns como lenguaje común.
- [x] `SE-320` — resiliencia: timeout, retry con jitter y circuit breaker.
- [x] `SE-321` — resiliencia: bulkhead, sidecar, ambassador y degradación.
- [x] `SE-322` — antipatrones y deuda de diseño.
- [x] `SE-323` — taller: refactorizar con patrones y medir su costo.
- [x] `SE-324` — proyecto: catálogo de patrones de un sistema real.

### Parte 27 — Arquitectura

- [x] `SE-325` — derivar arquitectura desde drivers medibles.
- [x] `SE-326` — mantener vistas consistentes.
- [x] `SE-327` — evaluar primero un monolito modular.
- [x] `SE-328` — comparar layered, hexagonal, clean y onion.
- [x] `SE-329` — delimitar bounded contexts.
- [x] `SE-330` — explicar fallos de CQRS y event sourcing.
- [x] `SE-331` — comparar serverless, edge y P2P.
- [x] `SE-332` — automatizar fitness functions.
- [x] `SE-333` — cuantificar coste y reversibilidad en ADR.
- [x] `SE-334` — relacionar Conway y Team Topologies.
- [x] `SE-335` — probar escenarios de atributos de calidad.
- [x] `SE-336` — defender una arquitectura y su evolución.

### Parte 28 — Estilos arquitectónicos

- [x] `SE-337` — estilos como respuestas a fuerzas de calidad.
- [x] `SE-338` — microkernel y arquitecturas de plugins.
- [x] `SE-339` — pipes and filters y arquitecturas de flujo.
- [x] `SE-340` — microservicios y sus costes reales.
- [x] `SE-341` — bFF, API gateway y service mesh.
- [x] `SE-342` — multi-tenancy y aislamiento.
- [x] `SE-343` — data mesh y propiedad de los datos.
- [x] `SE-344` — arquitectura celular y radio de impacto.
- [x] `SE-345` — 12-factor y aplicaciones nativas de la nube.
- [x] `SE-346` — evolución y migración entre estilos.
- [x] `SE-347` — taller: seleccionar un estilo con escenarios de calidad.
- [x] `SE-348` — proyecto: decisión arquitectónica defendida con ADR.

### Parte 29 — Datos

- [x] `SE-349` — explicar modelos y pérdida de información.
- [x] `SE-350` — diseñar desde patrones de acceso.
- [x] `SE-351` — reproducir anomalías de aislamiento.
- [x] `SE-352` — proteger invariantes transaccionales.
- [x] `SE-353` — interpretar planes e índices.
- [x] `SE-354` — aplicar expand-contract a esquemas.
- [x] `SE-355` — comparar replicación y partición.
- [x] `SE-356` — tratar invalidación de caché.
- [x] `SE-357` — probar restore, no solo backup.
- [x] `SE-358` — ejecutar retención y borrado.
- [x] `SE-359` — migrar con rollback.
- [x] `SE-360` — entregar un sistema de datos recuperable.

### Parte 30 — Ingeniería de datos y plataformas de datos

- [x] `SE-361` — Del dato operacional al analítico.
- [x] `SE-362` — Ingesta batch y streaming.
- [x] `SE-363` — Modelado analítico: hechos, dimensiones y granularidad.
- [x] `SE-364` — Transformación y orquestación idempotente con backfills.
- [x] `SE-365` — Calidad y observabilidad de datos.
- [x] `SE-366` — Contratos de datos y evolución de esquemas.
- [x] `SE-367` — Linaje, catálogo y metadatos.
- [x] `SE-368` — Warehouse, lake, lakehouse y formatos columnares.
- [x] `SE-369` — Gobierno, privacidad y retención de datos.
- [x] `SE-370` — Costos y operación de plataformas de datos.
- [x] `SE-371` — Taller: reparar un pipeline defectuoso.
- [x] `SE-372` — Proyecto: plataforma de datos mínima gobernada.

### Parte 31 — Integración y eventos

- [x] `SE-373` — elegir sincronía o asincronía por fuerzas.
- [x] `SE-374` — formalizar semántica de mensajes.
- [x] `SE-375` — comparar modelos de broker.
- [x] `SE-376` — probar entrega, orden y duplicación.
- [x] `SE-377` — combinar outbox, inbox y saga.
- [x] `SE-378` — evolucionar CDC y esquemas.
- [x] `SE-379` — comparar webhook, polling y suscripción.
- [x] `SE-380` — gobernar schemas.
- [x] `SE-381` — traducir ACL entre dominios.
- [x] `SE-382` — conservar trazas y autorización.
- [x] `SE-383` — inyectar duplicados y reconciliar.
- [x] `SE-384` — entregar retries y compensaciones verificadas.

### Parte 32 — Sistemas distribuidos

- [x] `SE-385` — distinguir concurrencia, paralelismo y distribución.
- [x] `SE-386` — reproducir y diagnosticar una race.
- [x] `SE-387` — aplicar cancelación estructurada.
- [x] `SE-388` — razonar con relojes y orden parcial.
- [x] `SE-389` — definir el modelo de fallos.
- [x] `SE-390` — aplicar CAP y PACELC sin eslóganes.
- [x] `SE-391` — explicar consenso y elección de líder.
- [x] `SE-392` — implementar idempotencia distribuida.
- [x] `SE-393` — comparar replicación y sharding.
- [x] `SE-394` — diseñar hipótesis de chaos.
- [x] `SE-395` — combinar race y partición controlada.
- [x] `SE-396` — demostrar degradación y recuperación.

### Parte 33 — Cloud y plataforma

- [x] `SE-397` — aplicar responsabilidad compartida.
- [x] `SE-398` — comparar aislamiento de cómputo.
- [x] `SE-399` — diseñar scheduling y capacidad.
- [x] `SE-400` — medir cold start y lock-in serverless.
- [x] `SE-401` — aplicar IAM y secretos con mínimo privilegio.
- [x] `SE-402` — gestionar estado y drift de IaC.
- [x] `SE-403` — separar cuentas y entornos.
- [x] `SE-404` — integrar FinOps y carbono.
- [x] `SE-405` — probar portabilidad sin prometer neutralidad total.
- [x] `SE-406` — construir platform-as-product y golden path.
- [x] `SE-407` — desplegar y destruir de forma segura.
- [x] `SE-408` — reconstruir una plataforma desde evidencia.

### Parte 34 — SaaS y plataformas de producto

- [x] `SE-409` — qué hace distinto a un producto SaaS.
- [x] `SE-410` — aislamiento multi-inquilino y vecino ruidoso.
- [x] `SE-411` — alta, aprovisionamiento y configuración por cliente.
- [x] `SE-412` — suscripciones, ciclos de facturación y dunning.
- [x] `SE-413` — medición de uso y facturación por consumo.
- [x] `SE-414` — planes, derechos de uso y banderas de funcionalidad.
- [x] `SE-415` — precios, empaquetado y límites por plan.
- [x] `SE-416` — marketplaces y plataformas de dos lados.
- [x] `SE-417` — pagos, idempotencia y conciliación.
- [x] `SE-418` — comercio electrónico: carrito, inventario, pagos y devoluciones.
- [x] `SE-419` — sLA por nivel, soporte y operación del producto.
- [x] `SE-420` — Taller y proyecto integrador: producto SaaS mínimo con evidencia.

### Parte 35 — Testing

- [x] `SE-421` — seleccionar por riesgo y declarar qué no probar.
- [x] `SE-422` — conectar unit tests y testabilidad.
- [x] `SE-423` — probar integración y contratos.
- [x] `SE-424` — delimitar E2E, aceptación y snapshots.
- [x] `SE-425` — aplicar property-based y model-based testing.
- [x] `SE-426` — medir mutation y fuzzing.
- [x] `SE-427` — usar dobles y virtualización con límites.
- [x] `SE-428` — controlar fixtures y determinismo.
- [x] `SE-429` — integrar exploración, accesibilidad y seguridad.
- [x] `SE-430` — diagnosticar flakiness.
- [x] `SE-431` — demostrar que una prueba detecta el defecto.
- [x] `SE-432` — entregar una estrategia ejecutable.

### Parte 36 — Calidad, rendimiento y resiliencia

- [x] `SE-433` — aplicar las nueve características ISO 25010:2023.
- [x] `SE-434` — usar métricas y gates con límites explícitos.
- [x] `SE-435` — ejecutar load, stress, spike y soak.
- [x] `SE-436` — trabajar percentiles y capacidad.
- [x] `SE-437` — validar metodología de benchmark.
- [x] `SE-438` — diseñar retries con presupuesto.
- [x] `SE-439` — probar aislamiento y degradación.
- [x] `SE-440` — contrastar RTO/RPO mediante restore.
- [x] `SE-441` — verificar compatibilidad.
- [x] `SE-442` — fijar performance budgets.
- [x] `SE-443` — ejecutar un game day.
- [x] `SE-444` — entregar informe con evidencia cruda.

### Parte 37 — Sistemas críticos, tiempo real y normas de seguridad

- [x] `SE-445` — Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA.
- [x] `SE-446` — IEC 61508 y niveles de integridad de seguridad.
- [x] `SE-447` — Automoción: ISO 26262 y niveles ASIL.
- [x] `SE-448` — Aviación: DO-178C, DO-254 y ARP4754.
- [x] `SE-449` — Dispositivos médicos: IEC 62304.
- [x] `SE-450` — Casos de seguridad y trazabilidad.
- [x] `SE-451` — RTOS y planificación de tiempo real.
- [x] `SE-452` — Codificación segura: MISRA y CERT.
- [x] `SE-453` — Verificación formal y model checking: TLA+, SPARK y Alloy.
- [x] `SE-454` — Verificación y cobertura: MC/DC, HIL y SIL.
- [x] `SE-455` — Taller: analizar un fallo real frente a las normas.
- [x] `SE-456` — Proyecto: paquete de aseguramiento de un controlador.

### Parte 38 — Seguridad, privacidad y compliance

- [x] `SE-457` — crear un threat model mantenible.
- [x] `SE-458` — endurecer autenticación y sesiones.
- [x] `SE-459` — ejecutar pruebas negativas de autorización.
- [x] `SE-460` — prevenir y probar inyección.
- [x] `SE-461` — gestionar claves y criptografía por contrato.
- [x] `SE-462` — rotar secretos sin caída.
- [x] `SE-463` — aplicar minimización y privacidad.
- [x] `SE-464` — usar SSDF y abuse cases.
- [x] `SE-465` — operar divulgación de vulnerabilidades.
- [x] `SE-466` — trazar regulación, control, prueba y evidencia.
- [x] `SE-467` — explotar un control ficticio y repararlo.
- [x] `SE-468` — entregar un producto evaluado con ASVS.

### Parte 39 — Supply chain y release

- [x] `SE-469` — producir un build hermético.
- [x] `SE-470` — promover artefactos inmutables.
- [x] `SE-471` — simular typosquatting y dependency confusion.
- [x] `SE-472` — generar SBOM y provenance conforme a SLSA vigente.
- [x] `SE-473` — verificar antes de consumir.
- [x] `SE-474` — operar release y SemVer.
- [x] `SE-475` — retirar feature flags.
- [x] `SE-476` — comparar canary y blue/green.
- [x] `SE-477` — diseñar actualizaciones seguras.
- [x] `SE-478` — responder a un paquete comprometido.
- [x] `SE-479` — verificar un release externo.
- [x] `SE-480` — entregar release firmado y reconstruible.

### Parte 40 — CI/CD y Platform Engineering

- [x] `SE-481` — acortar feedback sin ocultar riesgo.
- [x] `SE-482` — asegurar matrices y cachés de CI.
- [x] `SE-483` — diseñar gates según riesgo.
- [x] `SE-484` — usar OIDC y credenciales efímeras.
- [x] `SE-485` — desplegar progresivamente.
- [x] `SE-486` — validar una pipeline de IaC.
- [x] `SE-487` — explicar GitOps y reconciliación.
- [x] `SE-488` — crear previews con datos seguros.
- [x] `SE-489` — estudiar Backstage como caso, no receta.
- [x] `SE-490` — usar DORA y SPACE sin gaming.
- [x] `SE-491` — reparar una pipeline vulnerable.
- [x] `SE-492` — entregar rollback probado.

### Parte 41 — Observabilidad, SRE e incidentes

- [x] `SE-493` — elegir señales que respondan preguntas operativas.
- [x] `SE-494` — producir logs estructurados y seguros.
- [x] `SE-495` — controlar cardinalidad de métricas.
- [x] `SE-496` — propagar contexto de traza.
- [x] `SE-497` — derivar SLI, SLO y error budget.
- [x] `SE-498` — diseñar alertas accionables.
- [x] `SE-499` — ensayar runbook y on-call.
- [x] `SE-500` — practicar incident command.
- [x] `SE-501` — escribir postmortem sin culpa.
- [x] `SE-502` — probar recuperación ante desastre.
- [x] `SE-503` — diagnosticar con telemetría incompleta.
- [x] `SE-504` — completar detectar, contener, diagnosticar, recuperar y aprender.

### Parte 42 — Ingeniería del caos

- [x] `SE-505` — principios de la ingeniería del caos: estado estable e hipótesis.
- [x] `SE-506` — diseñar experimentos de fallo: alcance y radio de impacto.
- [x] `SE-507` — inyección de fallos de red, latencia y dependencias.
- [x] `SE-508` — fallos de recursos e infraestructura: CPU, memoria, disco y nodos.
- [x] `SE-509` — caos en Kubernetes y en plataformas cloud.
- [x] `SE-510` — fallos de datos y de estado: réplicas, particiones y corrupción.
- [x] `SE-511` — game days y ejercicios de respuesta a incidentes.
- [x] `SE-512` — caos continuo: automatización en CI/CD y en producción.
- [x] `SE-513` — seguridad y gobernanza de los experimentos: abortar, autorizar y registrar.
- [x] `SE-514` — aprender de los experimentos: hallazgos, métricas y mejora.
- [x] `SE-515` — Taller: ejecutar un experimento de caos acotado con criterio de aborto.
- [x] `SE-516` — Proyecto: programa de caos de un servicio con evidencia y remediación.

### Parte 43 — Legacy y retiro

- [x] `SE-517` — clasificar mantenimiento y riesgo.
- [x] `SE-518` — practicar arqueología de software.
- [x] `SE-519` — crear caracterización y seams.
- [x] `SE-520` — gestionar runtime obsoleto y EOL.
- [x] `SE-521` — comparar strangler, branch by abstraction y ACL.
- [x] `SE-522` — migrar runtime con compatibilidad.
- [x] `SE-523` — migrar datos progresivamente.
- [x] `SE-524` — controlar coexistencia y double write.
- [x] `SE-525` — ejecutar EOL, retención y borrado seguro.
- [x] `SE-526` — comparar TCO de reescritura y evolución.
- [x] `SE-527` — estabilizar un sistema ajeno.
- [x] `SE-528` — entregar una migración reversible.

### Parte 44 — Liderazgo

- [x] `SE-529` — liderar mediante contexto y decisiones.
- [x] `SE-530` — diseñar ownership y reducir bus factor.
- [x] `SE-531` — resolver conflicto técnico-organizacional.
- [x] `SE-532` — practicar mentoring observable.
- [x] `SE-533` — comunicar compromisos probabilísticos.
- [x] `SE-534` — presentar una decisión ejecutiva.
- [x] `SE-535` — defender build-vs-buy.
- [x] `SE-536` — considerar IP y contratos.
- [x] `SE-537` — calcular TCO, ROI, CAPEX y OPEX.
- [x] `SE-538` — diferenciar niveles y rutas profesionales.
- [x] `SE-539` — superar una revisión técnica adversarial.
- [x] `SE-540` — entregar dossier de portafolio defendible.

### Parte 45 — Metodologías de TDD a ODD

- [x] `SE-541` — mapa de metodologías: qué decide cada una y cómo elegir.
- [x] `SE-542` — tDD: ciclo rojo-verde-refactor y diseño emergente.
- [x] `SE-543` — tDD en la práctica: escuelas de Londres y clásica, y sus límites.
- [x] `SE-544` — bDD: ejemplos, conversación y lenguaje compartido.
- [x] `SE-545` — aTDD y Specification by Example: aceptación ejecutable.
- [x] `SE-546` — dDD como lenguaje ubicuo y contexto para agentes.
- [x] `SE-547` — diseño por contrato y pruebas de contrato como oráculo.
- [x] `SE-548` — sDD: spec-first, spec-anchored y spec-as-source.
- [x] `SE-549` — eDD: evaluaciones como especificación y puerta de release.
- [x] `SE-550` — oDD: desarrollo orgánico y su contraste con SDD.
- [x] `SE-551` — taller: un mismo cambio con cinco metodologías.
- [x] `SE-552` — proyecto: política metodológica de equipo con evidencia.

### Parte 46 — Ingeniería asistida por IA

- [x] `SE-553` — medir límites y APIs alucinadas.
- [x] `SE-554` — especificar criterios antes de generar.
- [x] `SE-555` — probar pérdida de contexto y memoria.
- [x] `SE-556` — comparar trabajo manual y asistido.
- [x] `SE-557` — detectar deuda de scaffolding.
- [x] `SE-558` — encontrar tests y docs convincentes pero incorrectos.
- [x] `SE-559` — detectar drift arquitectónico.
- [x] `SE-560` — practicar context engineering.
- [x] `SE-561` — ejecutar evals de coste, latencia y regresión.
- [x] `SE-562` — revisar privacidad, licencias y provenance.
- [x] `SE-563` — comparar flujo manual, asistido y agentic.
- [x] `SE-564` — entregar un cambio real con revisión humana.

### Parte 47 — SPEC y agentes

- [x] `SE-565` — escribir una SPEC durable.
- [x] `SE-566` — convertir ambigüedad en plan y tareas verificables.
- [x] `SE-567` — definir convergencia y stop conditions.
- [x] `SE-568` — comparar agentes en greenfield, brownfield y bugs.
- [x] `SE-569` — operar con mínima autoridad.
- [x] `SE-570` — aislar skills, hooks y herramientas.
- [x] `SE-571` — aplicar el modelo de confianza de MCP vigente.
- [x] `SE-572` — resolver conflictos multiagente.
- [x] `SE-573` — diseñar aprobaciones y reversibilidad.
- [x] `SE-574` — resistir prompt injection y conservar auditoría.
- [x] `SE-575` — detener, recuperar y evaluar loops.
- [x] `SE-576` — entregar un producto validado por el sistema, no por autodeclaración.

### Parte 48 — Harness y agentic engineering

- [x] `SE-577` — anatomía de un harness: modelo, contexto, herramientas y bucles.
- [x] `SE-578` — instrucciones de repositorio y cumplimiento determinista.
- [x] `SE-579` — herramientas, permisos y superficies de acción.
- [x] `SE-580` — gestión de contexto, resets y handoffs.
- [x] `SE-581` — loops de agentes y criterios de parada.
- [x] `SE-582` — sandboxes, reversibilidad y control de daño.
- [x] `SE-583` — verificación, gates y menú único de validación.
- [x] `SE-584` — multiagente y coordinación dentro del harness.
- [x] `SE-585` — observabilidad y evals del propio harness.
- [x] `SE-586` — aI-DLC, gobierno y vibe coding frente a agentic engineering.
- [x] `SE-587` — taller: diagnosticar el fallo de un harness.
- [x] `SE-588` — proyecto: harness mínimo gobernado y evaluado.

### Parte 49 — Patrones agénticos y sistemas con LLM

- [x] `SE-589` — workflows frente a agentes: cuándo no usar un agente.
- [x] `SE-590` — encadenado, enrutamiento y paralelización.
- [x] `SE-591` — orquestador-trabajadores y evaluador-optimizador.
- [x] `SE-592` — reAct, plan-and-execute y reflexión.
- [x] `SE-593` — memoria y gestión de estado de agentes.
- [x] `SE-594` — embeddings, recuperación y agentic RAG.
- [x] `SE-595` — interoperabilidad entre agentes: MCP y A2A.
- [x] `SE-596` — ejecución durable, reintentos e idempotencia.
- [x] `SE-597` — evals y LLMOps de sistemas con LLM.
- [x] `SE-598` — costo, latencia y seguridad en sistemas con LLM.
- [x] `SE-599` — taller: elegir y degradar un patrón agéntico.
- [x] `SE-600` — proyecto: sistema con LLM evaluado y operable.

### Parte 50 — Machine learning en producción y MLOps

- [x] `SE-601` — Ciclo de vida de ML y por qué falla en producción.
- [x] `SE-602` — Datos de entrenamiento, etiquetas y feature stores.
- [x] `SE-603` — Experimentos y entrenamiento reproducible.
- [x] `SE-604` — Evaluación, sesgos y validación de modelos.
- [x] `SE-605` — Ajuste fino, adaptación y costo.
- [x] `SE-606` — Servir modelos: latencia, lotes y GPU.
- [x] `SE-607` — Despliegue seguro de modelos: shadow, canary y rollback.
- [x] `SE-608` — Monitoreo, deriva y reentrenamiento.
- [x] `SE-609` — Seguridad y robustez de sistemas de ML.
- [x] `SE-610` — Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF.
- [x] `SE-611` — Taller: degradar y recuperar un modelo.
- [x] `SE-612` — Proyecto: sistema de ML operable con evidencia.

## Orden de ejecución y registro

| Orden | Unidad | Estado inicial | Condición de cierre |
| ---: | --- | --- | --- |
| 1 | Partes 00–01 | desarrolladas | conservar calidad y regresiones verdes |
| 2 | Parte 02 | desarrollada | kit multiplataforma, actividades específicas y matriz CI verde |
| 3 | Partes 03–04 | siguientes | laboratorios de red y razonamiento, un commit por parte |
| 4 | Partes 05–09 | borradores | construcción y transferencia ejecutables |
| 5 | Partes 10–14 | borradores | evidencia de producto, requisitos, contratos y accesibilidad |
| 6 | Partes 15–22, 24–25, 27, 29 y 31–33 | borradores | prácticas profesionales e integración por dominio |
| 7 | Partes 35–36, 38–41 y 43–44 | estructuras | enseñanza completa, casos y laboratorios operativos |
| 8 | Partes 46–47 | estructuras | evals, guardrails, coste, seguridad y regresión |
| 9 | Integración | parcial | glosario, bibliografía, rutas y proyectos reconciliados |
| 10 | Expansión desarrollada (Partes 26, 28, 45 y 48–49 por ADR-004; 23, 30, 37 y 50 por ADR-006) | completada | una parte por commit, con su contenido completo, figuras y CI verde |
| 11 | Expansión reservada (Partes 34 y 42, ADR-007) | habilitada | una parte por commit; solo se marca como desarrollada con su contenido completo, figuras y CI verde |

## Validación final obligatoria

Antes de declarar terminado el programa se comprueban estructura y preservación;
navegación y enlaces; duplicación y numeración; consistencia terminológica; fuentes y
vigencia; laboratorios y proyectos; evaluaciones y progresión; rutas y documentación;
ausencia de archivos vacíos, placeholders y referencias inventadas; y coherencia entre
repositorio, portal, workflows y About.

El informe final responde: qué existía, qué faltaba, qué se amplió, qué se creó, qué
se actualizó, qué se preservó, qué queda pendiente y qué métricas verificables cambiaron.
No se declara terminado lo que no se validó. El objetivo no es “crear 500 clases”, sino
formar criterio profesional profundo y demostrar que la mejora funciona.
