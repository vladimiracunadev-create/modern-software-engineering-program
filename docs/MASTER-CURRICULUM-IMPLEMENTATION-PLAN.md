# Plan maestro de auditoría y mejora curricular

Estado: **fuente canónica operativa**

Creado: 2026-10-06

Alcance base: `SE-001`–`SE-480`

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

La línea base actual es 480 clases. No se crea un ID nuevo hasta demostrar que una
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
`SE-001`–`SE-024` están desarrolladas; `SE-025`–`SE-360` son borradores publicados y
`SE-361`–`SE-480` son estructuras curriculares. Solo la Parte 01 tiene un laboratorio
ejecutable común, con seis pruebas. Hay tres workflows. Estos marcadores de estado se
sincronizan en la auditoría vigente; esta oración queda como línea base histórica.

Brechas detectadas que se atienden parte a parte:

- actividades y rúbricas genéricas fuera de las partes aprobadas;
- guías de parte insuficientes en Partes 10–39;
- párrafos repetidos en numerosos borradores, aunque la Parte 02 tiene menor deriva;
- validadores que detectan duplicados de documento completo pero no boilerplate interno;
- fuentes por clase demasiado gruesas y ausencia de registros estructurados para SLSA,
  OpenSSF, DORA, SPACE, OpenTelemetry, Google SRE, Backstage, Team Topologies, TLA+,
  Alloy, Function Points, COCOMO II y Monte Carlo;
- laboratorios, casos reales, proyectos y evidencia operativa insuficientes;
- Partes 30–39 no enseñables todavía y afirmaciones de madurez que deben seguir
  bloqueadas hasta su desarrollo real.

## Plan de mejora clase por clase

Cada línea nombra la mejora mínima específica que debe sobrevivir a la revisión de la
clase. No sustituye el temario vigente: lo enfoca y añade el artefacto o límite que
evita una explicación genérica.

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

- [ ] `SE-025` — construir una matriz de capacidades Windows, Linux y macOS.
- [ ] `SE-026` — probar rutas, case sensitivity, enlaces, metadatos y ACL sin mutación peligrosa.
- [ ] `SE-027` — aplicar mínimo privilegio, elevación controlada y rollback.
- [ ] `SE-028` — ensayar procesos, señales, cancelación, servicios y tareas programadas.
- [ ] `SE-029` — verificar quoting, pipes, streams, códigos de salida y encoding.
- [ ] `SE-030` — implementar rutas equivalentes PowerShell/Bash con pruebas de portabilidad.
- [ ] `SE-031` — definir precedencia de configuración y redacción de secretos.
- [ ] `SE-032` — documentar instalación, verificación, pinning y rollback de paquetes.
- [ ] `SE-033` — correlacionar logs, relojes, contexto y causa sin exponer datos.
- [ ] `SE-034` — comparar VM, WSL y contenedor con límites verificables.
- [ ] `SE-035` — romper, diagnosticar, reparar y volver a ejecutar un entorno seguro.
- [ ] `SE-036` — entregar un kit idempotente probado en los tres sistemas operativos.

### Parte 03 — Redes

- [ ] `SE-037` — diagnosticar una petición por capas con evidencia por salto.
- [ ] `SE-038` — explicar Ethernet y Wi-Fi sin confundir enlace con Internet.
- [ ] `SE-039` — experimentar IPv4, IPv6, routing y NAT con límites del entorno.
- [ ] `SE-040` — comparar TCP, UDP y QUIC bajo latencia, pérdida y orden.
- [ ] `SE-041` — probar DNS, caché negativa y límites de DNSSEC.
- [ ] `SE-042` — verificar HTTP, negociación, caché y semántica de métodos.
- [ ] `SE-043` — reconstruir cadena TLS, nombres, vencimiento y revocación.
- [ ] `SE-044` — razonar sobre proxies, balanceo y fronteras de confianza de headers.
- [ ] `SE-045` — comparar polling, SSE y WebSocket, incluida reconexión.
- [ ] `SE-046` — capturar tráfico sintético con minimización y privacidad.
- [ ] `SE-047` — producir una traza extremo a extremo con correlation ID.
- [ ] `SE-048` — inyectar DNS, TLS, latencia y pérdida y demostrar recuperación.

### Parte 04 — Pensamiento computacional

- [ ] `SE-049` — descomponer un problema y hacer visibles sus supuestos.
- [ ] `SE-050` — usar tablas de verdad y contraejemplos para refutar soluciones.
- [ ] `SE-051` — modelar relaciones y grafos como artefactos ejecutables.
- [ ] `SE-052` — formular invariantes comprobables.
- [ ] `SE-053` — conectar inducción, recursión y caso base.
- [ ] `SE-054` — distinguir corrección parcial, total y terminación.
- [ ] `SE-055` — separar complejidad teórica de benchmark empírico.
- [ ] `SE-056` — justificar heurísticas, límites y condiciones de fallo.
- [ ] `SE-057` — construir una máquina de estados ejecutable.
- [ ] `SE-058` — mantener un registro de hipótesis y evidencia contraria.
- [ ] `SE-059` — reconciliar un problema ambiguo y contradictorio.
- [ ] `SE-060` — entregar especificación, solución, oráculo y contraejemplos.

### Parte 05 — Fundamentos de programación

- [ ] `SE-061` — hacer explícitos tipos, coerciones y contratos.
- [ ] `SE-062` — relacionar decisiones de control con cobertura alcanzable.
- [ ] `SE-063` — usar invariantes de bucle y condiciones de término.
- [ ] `SE-064` — separar alcance, efectos y contratos de funciones.
- [ ] `SE-065` — comparar excepciones, Result y recuperación.
- [ ] `SE-066` — diseñar transformaciones de colecciones sin mutación accidental.
- [ ] `SE-067` — validar esquema, streaming y errores de E/S.
- [ ] `SE-068` — controlar dependencias y límites de módulos.
- [ ] `SE-069` — derivar código desde ejemplos, bordes y propiedades.
- [ ] `SE-070` — revisar legibilidad con evidencia de mantenimiento.
- [ ] `SE-071` — transferir la misma solución entre dos lenguajes.
- [ ] `SE-072` — entregar una CLI empaquetada, probada y documentada.

### Parte 06 — Paradigmas

- [ ] `SE-073` — observar estado y mutación en el paradigma imperativo.
- [ ] `SE-074` — evaluar descomposición procedural y sus límites.
- [ ] `SE-075` — probar encapsulación y mensajería entre objetos.
- [ ] `SE-076` — razonar sobre inmutabilidad, efectos y composición funcional.
- [ ] `SE-077` — construir una regla declarativa y explicar su motor.
- [ ] `SE-078` — seguir resolución y fallos en programación lógica.
- [ ] `SE-079` — controlar orden, reentrada y errores en eventos.
- [ ] `SE-080` — probar backpressure y cancelación en flujos reactivos.
- [ ] `SE-081` — ensayar supervisión y aislamiento con actores.
- [ ] `SE-082` — usar una matriz contextual para combinar paradigmas.
- [ ] `SE-083` — implementar una regla de negocio en cinco paradigmas.
- [ ] `SE-084` — comparar implementaciones con fixtures y propiedades comunes.

### Parte 07 — Estructuras y algoritmos

- [ ] `SE-085` — elegir secuencia según operaciones y carga.
- [ ] `SE-086` — comparar colas, deques y prioridades.
- [ ] `SE-087` — medir hashing, colisiones y adversarios.
- [ ] `SE-088` — mantener invariantes de árboles y balance.
- [ ] `SE-089` — tratar ciclos, pesos y alcanzabilidad en grafos.
- [ ] `SE-090` — comparar búsqueda y ordenamiento por workload.
- [ ] `SE-091` — contrastar greedy y programación dinámica.
- [ ] `SE-092` — hacer visible poda y explosión combinatoria.
- [ ] `SE-093` — evaluar estructuras probabilísticas y persistentes.
- [ ] `SE-094` — diseñar benchmarks sin sesgo obvio.
- [ ] `SE-095` — justificar selección con una carga representativa.
- [ ] `SE-096` — entregar biblioteca de bordes con pruebas y límites.

### Parte 08 — Entornos y depuración

- [ ] `SE-097` — reproducir configuración de editor y tareas.
- [ ] `SE-098` — conservar una sesión de depuración explicada.
- [ ] `SE-099` — perfilar una hipótesis y no una intuición vaga.
- [ ] `SE-100` — explicar capacidad y límites de lint y análisis estático.
- [ ] `SE-101` — hacer reproducibles notebooks y resultados.
- [ ] `SE-102` — verificar una matriz de runtimes.
- [ ] `SE-103` — demostrar aislamiento de entornos.
- [ ] `SE-104` — reconstruir un Dev Container desde cero.
- [ ] `SE-105` — minimizar un fallo conservando su causa.
- [ ] `SE-106` — medir accesibilidad y carga cognitiva de herramientas.
- [ ] `SE-107` — diagnosticar un sistema desconocido con hipótesis.
- [ ] `SE-108` — reproducir el entorno desde un checkout limpio.

### Parte 09 — Paquetes y automatización

- [ ] `SE-109` — separar contratos de biblioteca, framework y runtime.
- [ ] `SE-110` — comprobar compatibilidad SemVer, no solo declararla.
- [ ] `SE-111` — explicar resolución, lockfile y conflictos transitivos.
- [ ] `SE-112` — publicar un artefacto reproducible.
- [ ] `SE-113` — estabilizar contrato y códigos de salida de CLI.
- [ ] `SE-114` — probar idempotencia y recuperación de scripts.
- [ ] `SE-115` — aislar plugins y manejar incompatibilidad.
- [ ] `SE-116` — evaluar riesgo y deriva de code generation.
- [ ] `SE-117` — registrar licencia y provenance de dependencias.
- [ ] `SE-118` — medir tiempo hasta el primer éxito del consumidor.
- [ ] `SE-119` — validar el paquete desde un consumidor externo.
- [ ] `SE-120` — mantener compatibilidad de SDK/CLI con clientes anteriores.

### Parte 10 — Discovery

- [ ] `SE-121` — separar síntoma, problema y oportunidad.
- [ ] `SE-122` — mapear actores, poder y exclusiones.
- [ ] `SE-123` — diseñar entrevistas que reduzcan sesgo.
- [ ] `SE-124` — mantener un mapa de supuestos.
- [ ] `SE-125` — formular outcomes medibles.
- [ ] `SE-126` — comparar alternativas, incluido no construir.
- [ ] `SE-127` — diseñar un experimento falsable.
- [ ] `SE-128` — priorizar por riesgo y evidencia.
- [ ] `SE-129` — aplicar consentimiento y minimización.
- [ ] `SE-130` — fijar criterios de abandono.
- [ ] `SE-131` — convertir una petición en investigación.
- [ ] `SE-132` — entregar un brief de producto respaldado por evidencia.

### Parte 11 — Economía y métricas

- [ ] `SE-133` — modelar sostenibilidad del negocio.
- [ ] `SE-134` — calcular TCO y coste de oportunidad.
- [ ] `SE-135` — detectar vanity metrics.
- [ ] `SE-136` — analizar cohortes y retención.
- [ ] `SE-137` — diseñar telemetría con consentimiento.
- [ ] `SE-138` — reconocer causalidad débil y errores estadísticos.
- [ ] `SE-139` — definir guardrails y contramétricas.
- [ ] `SE-140` — relacionar coste con outcome.
- [ ] `SE-141` — tratar cartera como opciones reversibles.
- [ ] `SE-142` — valorar reversibilidad de una decisión.
- [ ] `SE-143` — construir un árbol de métricas.
- [ ] `SE-144` — defender un caso económico por escenarios.

### Parte 12 — Requisitos

- [ ] `SE-145` — elaborar un plan de elicitación.
- [ ] `SE-146` — extraer reglas, excepciones y vocabulario de dominio.
- [ ] `SE-147` — volver medibles los requisitos no funcionales.
- [ ] `SE-148` — elegir entre historia, caso de uso y job story.
- [ ] `SE-149` — escribir aceptación mediante ejemplos y bordes.
- [ ] `SE-150` — negociar conflictos sin ocultarlos.
- [ ] `SE-151` — mantener trazabilidad bidireccional.
- [ ] `SE-152` — traducir regulación a controles comprobables.
- [ ] `SE-153` — analizar impacto del cambio.
- [ ] `SE-154` — detectar contradicciones e incompletitud.
- [ ] `SE-155` — reparar un requisito defectuoso.
- [ ] `SE-156` — entregar una especificación revisable.

### Parte 13 — Especificaciones y contratos

- [ ] `SE-157` — elegir el grado de formalidad adecuado.
- [ ] `SE-158` — usar BDD como conversación y evidencia, no ritual.
- [ ] `SE-159` — verificar precondiciones, postcondiciones e invariantes.
- [ ] `SE-160` — comprobar consistencia entre modelos.
- [ ] `SE-161` — obtener un contraejemplo con TLA+ o Alloy y declarar límites.
- [ ] `SE-162` — evolucionar esquemas de forma compatible.
- [ ] `SE-163` — separar contratos OpenAPI, AsyncAPI y GraphQL.
- [ ] `SE-164` — probar compatibilidad, versionado y deprecación.
- [ ] `SE-165` — gobernar una fuente de verdad contractual.
- [ ] `SE-166` — ejecutar contract tests contra productor y consumidor.
- [ ] `SE-167` — trazar intención hasta contrato y prueba.
- [ ] `SE-168` — entregar un paquete de especificación trazable.

### Parte 14 — UX, accesibilidad e i18n

- [ ] `SE-169` — investigar personas, tareas y contexto sin estereotipos.
- [ ] `SE-170` — probar arquitectura de información y navegación.
- [ ] `SE-171` — diseñar feedback y affordances perceptibles.
- [ ] `SE-172` — construir errores recuperables.
- [ ] `SE-173` — aplicar criterios WCAG a un flujo concreto.
- [ ] `SE-174` — verificar teclado, foco y lector de pantalla.
- [ ] `SE-175` — comprobar contraste, zoom y tipografía.
- [ ] `SE-176` — respetar responsive y preferencias del usuario.
- [ ] `SE-177` — probar locale, plural, tiempo, moneda y RTL.
- [ ] `SE-178` — realizar un estudio de usabilidad con protocolo.
- [ ] `SE-179` — reparar una barrera y explicar la exclusión evitada.
- [ ] `SE-180` — entregar un flujo accesible en varios locales.

### Parte 15 — Procesos y estimación

- [ ] `SE-181` — seleccionar proceso según riesgo y contexto.
- [ ] `SE-182` — separar principios ágiles de rituales.
- [ ] `SE-183` — comparar métodos sobre el mismo caso.
- [ ] `SE-184` — gestionar colas y WIP con datos.
- [ ] `SE-185` — comparar Function Points, COCOMO II y rangos.
- [ ] `SE-186` — modelar dependencias y camino crítico.
- [ ] `SE-187` — mantener un registro de riesgos.
- [ ] `SE-188` — definir DoR y DoD observables.
- [ ] `SE-189` — usar métricas sin incentivar gaming.
- [ ] `SE-190` — ejecutar un experimento de mejora.
- [ ] `SE-191` — producir un forecast Monte Carlo reproducible.
- [ ] `SE-192` — entregar un plan adaptable con intervalos.

### Parte 16 — Git y colaboración

- [ ] `SE-193` — explicar objetos Git y recuperar con reflog.
- [ ] `SE-194` — crear commits revisables y recuperables.
- [ ] `SE-195` — resolver rebase y conflictos de forma segura.
- [ ] `SE-196` — hacer review basada en riesgo.
- [ ] `SE-197` — comparar branching strategies con métricas.
- [ ] `SE-198` — trazar issue, cambio, revisión y release.
- [ ] `SE-199` — usar CODEOWNERS sin ocultar bus factor.
- [ ] `SE-200` — practicar InnerSource y función de OSPO.
- [ ] `SE-201` — aplicar obligaciones de licencia.
- [ ] `SE-202` — verificar firmas y provenance.
- [ ] `SE-203` — rescatar una integración fallida.
- [ ] `SE-204` — operar una contribución y release reales.

### Parte 17 — Documentación

- [ ] `SE-205` — definir audiencia, tarea y éxito documental.
- [ ] `SE-206` — separar tutorial, how-to, referencia y explicación.
- [ ] `SE-207` — medir time-to-first-success.
- [ ] `SE-208` — conservar alternativas rechazadas en ADR/RFC.
- [ ] `SE-209` — crear diagramas con propósito y límites.
- [ ] `SE-210` — probar ejemplos contra contratos.
- [ ] `SE-211` — ensayar un runbook.
- [ ] `SE-212` — validar publicación y enlaces.
- [ ] `SE-213` — mantener un glosario relacional.
- [ ] `SE-214` — distinguir documentación humana y legible por máquina.
- [ ] `SE-215` — reconstruir conocimiento desde evidencia legacy.
- [ ] `SE-216` — entregar un portal accesible y versionado.

### Parte 18 — CLI, TUI y servicios

- [ ] `SE-217` — diseñar un contrato CLI estable.
- [ ] `SE-218` — componer stdout, stderr, pipes y códigos de salida.
- [ ] `SE-219` — implementar precedencia de configuración.
- [ ] `SE-220` — devolver errores accionables.
- [ ] `SE-221` — probar accesibilidad de una TUI.
- [ ] `SE-222` — gestionar lifecycle de un daemon.
- [ ] `SE-223` — diseñar jobs con leasing y concurrencia.
- [ ] `SE-224` — usar checkpoints e idempotencia.
- [ ] `SE-225` — verificar instalación, actualización y desinstalación.
- [ ] `SE-226` — diseñar telemetría opt-in.
- [ ] `SE-227` — endurecer una automatización peligrosa.
- [ ] `SE-228` — entregar una herramienta operable multiplataforma.

### Parte 19 — Web y frontend

- [ ] `SE-229` — construir sobre HTML semántico.
- [ ] `SE-230` — explicar lifecycle de DOM y eventos.
- [ ] `SE-231` — medir SSR, CSR y SSG en un caso.
- [ ] `SE-232` — mantener consistencia de estado.
- [ ] `SE-233` — implementar validación accesible.
- [ ] `SE-234` — diseñar URLs durables.
- [ ] `SE-235` — fijar Core Web Vitals y presupuestos.
- [ ] `SE-236` — aplicar CSP y fronteras del navegador.
- [ ] `SE-237` — resolver offline y conflictos.
- [ ] `SE-238` — medir SEO sin promesas vagas.
- [ ] `SE-239` — diagnosticar un flujo web degradado.
- [ ] `SE-240` — entregar una aplicación offline y accesible.

### Parte 20 — Backend y APIs

- [ ] `SE-241` — definir límites y ownership de servicio.
- [ ] `SE-242` — aplicar semántica REST/HTTP con precisión.
- [ ] `SE-243` — comparar RPC, GraphQL y gRPC.
- [ ] `SE-244` — normalizar validación y errores.
- [ ] `SE-245` — probar autorización por recurso.
- [ ] `SE-246` — implementar idempotencia y replay seguro.
- [ ] `SE-247` — tratar poison messages.
- [ ] `SE-248` — controlar backpressure y uploads.
- [ ] `SE-249` — diseñar caché y rate limiting.
- [ ] `SE-250` — probar readiness y shutdown.
- [ ] `SE-251` — reparar una API incompatible.
- [ ] `SE-252` — entregar servicio con contratos y telemetría.

### Parte 21 — Móvil y escritorio

- [ ] `SE-253` — modelar lifecycle del cliente.
- [ ] `SE-254` — conservar estado ante suspensión.
- [ ] `SE-255` — justificar nativo, híbrido o multiplataforma.
- [ ] `SE-256` — resolver sync y conflictos.
- [ ] `SE-257` — pedir el mínimo de permisos.
- [ ] `SE-258` — probar accesibilidad por modalidad.
- [ ] `SE-259` — verificar firma y distribución.
- [ ] `SE-260` — diseñar offline-first.
- [ ] `SE-261` — medir batería y recursos honestamente.
- [ ] `SE-262` — asumir cliente hostil y sandbox.
- [ ] `SE-263` — comparar dos plataformas con la misma prueba.
- [ ] `SE-264` — entregar cliente sincronizable y recuperable.

### Parte 22 — Embedded, IoT y edge

- [ ] `SE-265` — trazar frontera hardware/firmware.
- [ ] `SE-266` — comparar buses y contratos eléctricos/lógicos.
- [ ] `SE-267` — medir memoria, CPU y energía con límites.
- [ ] `SE-268` — verificar deadlines y jitter de RTOS.
- [ ] `SE-269` — controlar ISR y estado compartido.
- [ ] `SE-270` — operar con conectividad intermitente.
- [ ] `SE-271` — probar OTA y rollback.
- [ ] `SE-272` — diseñar provisioning y rotación de claves.
- [ ] `SE-273` — repartir decisiones entre edge y nube.
- [ ] `SE-274` — analizar hazards y vida útil.
- [ ] `SE-275` — simular fallos físicos y digitales con honestidad.
- [ ] `SE-276` — entregar dispositivo simulado actualizable y recuperable.

### Parte 23 — Dominios especializados

- [ ] `SE-277` — exigir reproducibilidad científica.
- [ ] `SE-278` — asegurar calidad en pipelines de datos.
- [ ] `SE-279` — evaluar drift y modelos ML.
- [ ] `SE-280` — controlar determinismo en game loops.
- [ ] `SE-281` — tratar latencia y accesibilidad en AV.
- [ ] `SE-282` — formalizar invariantes contables.
- [ ] `SE-283` — separar privacidad, safety y cumplimiento médico.
- [ ] `SE-284` — explicar cuándo no usar blockchain.
- [ ] `SE-285` — manejar CRS, tiempo y precisión geoespacial.
- [ ] `SE-286` — delimitar low-code y escape hatches.
- [ ] `SE-287` — comparar riesgos entre dominios.
- [ ] `SE-288` — entregar un diseño profundo de dominio.

### Parte 24 — Diseño y refactorización

- [ ] `SE-289` — interpretar cohesión y acoplamiento en contexto.
- [ ] `SE-290` — aplicar SOLID con sus límites.
- [ ] `SE-291` — preferir composición cuando las fuerzas lo justifiquen.
- [ ] `SE-292` — elegir patrones por fuerzas, no por catálogo.
- [ ] `SE-293` — tratar efectos y concurrencia en patrones.
- [ ] `SE-294` — usar contraejemplos para code smells.
- [ ] `SE-295` — construir pruebas de caracterización.
- [ ] `SE-296` — diseñar para observabilidad.
- [ ] `SE-297` — distinguir complejidad accidental y esencial.
- [ ] `SE-298` — modelar economía de deuda técnica.
- [ ] `SE-299` — refactorizar con regresión protegida.
- [ ] `SE-300` — evolucionar diseño conservando compatibilidad.

### Parte 25 — Arquitectura

- [ ] `SE-301` — derivar arquitectura desde drivers medibles.
- [ ] `SE-302` — mantener vistas consistentes.
- [ ] `SE-303` — evaluar primero un monolito modular.
- [ ] `SE-304` — comparar layered, hexagonal, clean y onion.
- [ ] `SE-305` — delimitar bounded contexts.
- [ ] `SE-306` — explicar fallos de CQRS y event sourcing.
- [ ] `SE-307` — comparar serverless, edge y P2P.
- [ ] `SE-308` — automatizar fitness functions.
- [ ] `SE-309` — cuantificar coste y reversibilidad en ADR.
- [ ] `SE-310` — relacionar Conway y Team Topologies.
- [ ] `SE-311` — probar escenarios de atributos de calidad.
- [ ] `SE-312` — defender una arquitectura y su evolución.

### Parte 26 — Datos

- [ ] `SE-313` — explicar modelos y pérdida de información.
- [ ] `SE-314` — diseñar desde patrones de acceso.
- [ ] `SE-315` — reproducir anomalías de aislamiento.
- [ ] `SE-316` — proteger invariantes transaccionales.
- [ ] `SE-317` — interpretar planes e índices.
- [ ] `SE-318` — aplicar expand-contract a esquemas.
- [ ] `SE-319` — comparar replicación y partición.
- [ ] `SE-320` — tratar invalidación de caché.
- [ ] `SE-321` — probar restore, no solo backup.
- [ ] `SE-322` — ejecutar retención y borrado.
- [ ] `SE-323` — migrar con rollback.
- [ ] `SE-324` — entregar un sistema de datos recuperable.

### Parte 27 — Integración y eventos

- [ ] `SE-325` — elegir sincronía o asincronía por fuerzas.
- [ ] `SE-326` — formalizar semántica de mensajes.
- [ ] `SE-327` — comparar modelos de broker.
- [ ] `SE-328` — probar entrega, orden y duplicación.
- [ ] `SE-329` — combinar outbox, inbox y saga.
- [ ] `SE-330` — evolucionar CDC y esquemas.
- [ ] `SE-331` — comparar webhook, polling y suscripción.
- [ ] `SE-332` — gobernar schemas.
- [ ] `SE-333` — traducir ACL entre dominios.
- [ ] `SE-334` — conservar trazas y autorización.
- [ ] `SE-335` — inyectar duplicados y reconciliar.
- [ ] `SE-336` — entregar retries y compensaciones verificadas.

### Parte 28 — Sistemas distribuidos

- [ ] `SE-337` — distinguir concurrencia, paralelismo y distribución.
- [ ] `SE-338` — reproducir y diagnosticar una race.
- [ ] `SE-339` — aplicar cancelación estructurada.
- [ ] `SE-340` — razonar con relojes y orden parcial.
- [ ] `SE-341` — definir el modelo de fallos.
- [ ] `SE-342` — aplicar CAP y PACELC sin eslóganes.
- [ ] `SE-343` — explicar consenso y elección de líder.
- [ ] `SE-344` — implementar idempotencia distribuida.
- [ ] `SE-345` — comparar replicación y sharding.
- [ ] `SE-346` — diseñar hipótesis de chaos.
- [ ] `SE-347` — combinar race y partición controlada.
- [ ] `SE-348` — demostrar degradación y recuperación.

### Parte 29 — Cloud y plataforma

- [ ] `SE-349` — aplicar responsabilidad compartida.
- [ ] `SE-350` — comparar aislamiento de cómputo.
- [ ] `SE-351` — diseñar scheduling y capacidad.
- [ ] `SE-352` — medir cold start y lock-in serverless.
- [ ] `SE-353` — aplicar IAM y secretos con mínimo privilegio.
- [ ] `SE-354` — gestionar estado y drift de IaC.
- [ ] `SE-355` — separar cuentas y entornos.
- [ ] `SE-356` — integrar FinOps y carbono.
- [ ] `SE-357` — probar portabilidad sin prometer neutralidad total.
- [ ] `SE-358` — construir platform-as-product y golden path.
- [ ] `SE-359` — desplegar y destruir de forma segura.
- [ ] `SE-360` — reconstruir una plataforma desde evidencia.

### Parte 30 — Testing

- [ ] `SE-361` — seleccionar por riesgo y declarar qué no probar.
- [ ] `SE-362` — conectar unit tests y testabilidad.
- [ ] `SE-363` — probar integración y contratos.
- [ ] `SE-364` — delimitar E2E, aceptación y snapshots.
- [ ] `SE-365` — aplicar property-based y model-based testing.
- [ ] `SE-366` — medir mutation y fuzzing.
- [ ] `SE-367` — usar dobles y virtualización con límites.
- [ ] `SE-368` — controlar fixtures y determinismo.
- [ ] `SE-369` — integrar exploración, accesibilidad y seguridad.
- [ ] `SE-370` — diagnosticar flakiness.
- [ ] `SE-371` — demostrar que una prueba detecta el defecto.
- [ ] `SE-372` — entregar una estrategia ejecutable.

### Parte 31 — Calidad, rendimiento y resiliencia

- [ ] `SE-373` — aplicar las nueve características ISO 25010:2023.
- [ ] `SE-374` — usar métricas y gates con límites explícitos.
- [ ] `SE-375` — ejecutar load, stress, spike y soak.
- [ ] `SE-376` — trabajar percentiles y capacidad.
- [ ] `SE-377` — validar metodología de benchmark.
- [ ] `SE-378` — diseñar retries con presupuesto.
- [ ] `SE-379` — probar aislamiento y degradación.
- [ ] `SE-380` — contrastar RTO/RPO mediante restore.
- [ ] `SE-381` — verificar compatibilidad.
- [ ] `SE-382` — fijar performance budgets.
- [ ] `SE-383` — ejecutar un game day.
- [ ] `SE-384` — entregar informe con evidencia cruda.

### Parte 32 — Seguridad, privacidad y compliance

- [ ] `SE-385` — crear un threat model mantenible.
- [ ] `SE-386` — endurecer autenticación y sesiones.
- [ ] `SE-387` — ejecutar pruebas negativas de autorización.
- [ ] `SE-388` — prevenir y probar inyección.
- [ ] `SE-389` — gestionar claves y criptografía por contrato.
- [ ] `SE-390` — rotar secretos sin caída.
- [ ] `SE-391` — aplicar minimización y privacidad.
- [ ] `SE-392` — usar SSDF y abuse cases.
- [ ] `SE-393` — operar divulgación de vulnerabilidades.
- [ ] `SE-394` — trazar regulación, control, prueba y evidencia.
- [ ] `SE-395` — explotar un control ficticio y repararlo.
- [ ] `SE-396` — entregar un producto evaluado con ASVS.

### Parte 33 — Supply chain y release

- [ ] `SE-397` — producir un build hermético.
- [ ] `SE-398` — promover artefactos inmutables.
- [ ] `SE-399` — simular typosquatting y dependency confusion.
- [ ] `SE-400` — generar SBOM y provenance conforme a SLSA vigente.
- [ ] `SE-401` — verificar antes de consumir.
- [ ] `SE-402` — operar release y SemVer.
- [ ] `SE-403` — retirar feature flags.
- [ ] `SE-404` — comparar canary y blue/green.
- [ ] `SE-405` — diseñar actualizaciones seguras.
- [ ] `SE-406` — responder a un paquete comprometido.
- [ ] `SE-407` — verificar un release externo.
- [ ] `SE-408` — entregar release firmado y reconstruible.

### Parte 34 — CI/CD y Platform Engineering

- [ ] `SE-409` — acortar feedback sin ocultar riesgo.
- [ ] `SE-410` — asegurar matrices y cachés de CI.
- [ ] `SE-411` — diseñar gates según riesgo.
- [ ] `SE-412` — usar OIDC y credenciales efímeras.
- [ ] `SE-413` — desplegar progresivamente.
- [ ] `SE-414` — validar una pipeline de IaC.
- [ ] `SE-415` — explicar GitOps y reconciliación.
- [ ] `SE-416` — crear previews con datos seguros.
- [ ] `SE-417` — estudiar Backstage como caso, no receta.
- [ ] `SE-418` — usar DORA y SPACE sin gaming.
- [ ] `SE-419` — reparar una pipeline vulnerable.
- [ ] `SE-420` — entregar rollback probado.

### Parte 35 — Observabilidad, SRE e incidentes

- [ ] `SE-421` — elegir señales que respondan preguntas operativas.
- [ ] `SE-422` — producir logs estructurados y seguros.
- [ ] `SE-423` — controlar cardinalidad de métricas.
- [ ] `SE-424` — propagar contexto de traza.
- [ ] `SE-425` — derivar SLI, SLO y error budget.
- [ ] `SE-426` — diseñar alertas accionables.
- [ ] `SE-427` — ensayar runbook y on-call.
- [ ] `SE-428` — practicar incident command.
- [ ] `SE-429` — escribir postmortem sin culpa.
- [ ] `SE-430` — probar recuperación ante desastre.
- [ ] `SE-431` — diagnosticar con telemetría incompleta.
- [ ] `SE-432` — completar detectar, contener, diagnosticar, recuperar y aprender.

### Parte 36 — Legacy y retiro

- [ ] `SE-433` — clasificar mantenimiento y riesgo.
- [ ] `SE-434` — practicar arqueología de software.
- [ ] `SE-435` — crear caracterización y seams.
- [ ] `SE-436` — gestionar runtime obsoleto y EOL.
- [ ] `SE-437` — comparar strangler, branch by abstraction y ACL.
- [ ] `SE-438` — migrar runtime con compatibilidad.
- [ ] `SE-439` — migrar datos progresivamente.
- [ ] `SE-440` — controlar coexistencia y double write.
- [ ] `SE-441` — ejecutar EOL, retención y borrado seguro.
- [ ] `SE-442` — comparar TCO de reescritura y evolución.
- [ ] `SE-443` — estabilizar un sistema ajeno.
- [ ] `SE-444` — entregar una migración reversible.

### Parte 37 — Liderazgo

- [ ] `SE-445` — liderar mediante contexto y decisiones.
- [ ] `SE-446` — diseñar ownership y reducir bus factor.
- [ ] `SE-447` — resolver conflicto técnico-organizacional.
- [ ] `SE-448` — practicar mentoring observable.
- [ ] `SE-449` — comunicar compromisos probabilísticos.
- [ ] `SE-450` — presentar una decisión ejecutiva.
- [ ] `SE-451` — defender build-vs-buy.
- [ ] `SE-452` — considerar IP y contratos.
- [ ] `SE-453` — calcular TCO, ROI, CAPEX y OPEX.
- [ ] `SE-454` — diferenciar niveles y rutas profesionales.
- [ ] `SE-455` — superar una revisión técnica adversarial.
- [ ] `SE-456` — entregar dossier de portafolio defendible.

### Parte 38 — Ingeniería asistida por IA

- [ ] `SE-457` — medir límites y APIs alucinadas.
- [ ] `SE-458` — especificar criterios antes de generar.
- [ ] `SE-459` — probar pérdida de contexto y memoria.
- [ ] `SE-460` — comparar trabajo manual y asistido.
- [ ] `SE-461` — detectar deuda de scaffolding.
- [ ] `SE-462` — encontrar tests y docs convincentes pero incorrectos.
- [ ] `SE-463` — detectar drift arquitectónico.
- [ ] `SE-464` — practicar context engineering.
- [ ] `SE-465` — ejecutar evals de coste, latencia y regresión.
- [ ] `SE-466` — revisar privacidad, licencias y provenance.
- [ ] `SE-467` — comparar flujo manual, asistido y agentic.
- [ ] `SE-468` — entregar un cambio real con revisión humana.

### Parte 39 — SPEC y agentes

- [ ] `SE-469` — escribir una SPEC durable.
- [ ] `SE-470` — convertir ambigüedad en plan y tareas verificables.
- [ ] `SE-471` — definir convergencia y stop conditions.
- [ ] `SE-472` — comparar agentes en greenfield, brownfield y bugs.
- [ ] `SE-473` — operar con mínima autoridad.
- [ ] `SE-474` — aislar skills, hooks y herramientas.
- [ ] `SE-475` — aplicar el modelo de confianza de MCP vigente.
- [ ] `SE-476` — resolver conflictos multiagente.
- [ ] `SE-477` — diseñar aprobaciones y reversibilidad.
- [ ] `SE-478` — resistir prompt injection y conservar auditoría.
- [ ] `SE-479` — detener, recuperar y evaluar loops.
- [ ] `SE-480` — entregar un producto validado por el sistema, no por autodeclaración.

## Orden de ejecución y registro

| Orden | Unidad | Estado inicial | Condición de cierre |
| ---: | --- | --- | --- |
| 1 | Partes 00–01 | desarrolladas | conservar calidad y regresiones verdes |
| 2 | Parte 02 | siguiente | kit multiplataforma, actividades específicas y matriz CI verde |
| 3 | Partes 03–04 | pendientes | laboratorios de red y razonamiento, un commit por parte |
| 4 | Partes 05–09 | borradores | construcción y transferencia ejecutables |
| 5 | Partes 10–14 | borradores | evidencia de producto, requisitos, contratos y accesibilidad |
| 6 | Partes 15–29 | borradores | prácticas profesionales e integración por dominio |
| 7 | Partes 30–37 | estructuras | enseñanza completa, casos y laboratorios operativos |
| 8 | Partes 38–39 | estructuras | evals, guardrails, coste, seguridad y regresión |
| 9 | Integración | parcial | glosario, bibliografía, rutas y proyectos reconciliados |
| 10 | Expansión | no habilitada | auditoría demuestra brechas indivisibles y aprueba nuevos IDs |

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
