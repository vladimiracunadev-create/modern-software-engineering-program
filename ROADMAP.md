# Roadmap del programa de Ingeniería de Software

Este documento define qué programa se está construyendo, cómo progresa y qué debe
incorporarse. No es un prompt ni un conjunto de instrucciones para agentes. Las reglas
de contribución viven en `AGENTS.md`, `CONTRIBUTING.md` y
`docs/PEDAGOGICAL-STANDARD.md`; aquí se describe el producto educativo.

La meta es un programa profesional integral de aproximadamente 500 clases. El número
no es una cuota: cualquier ampliación debe resolver una brecha real y respetar la
prioridad **calidad > profundidad > coherencia > cantidad**.

El mandato completo, las brechas transversales y la acción específica pendiente para
cada uno de los 480 IDs se conservan en el
[`plan maestro de auditoría y mejora curricular`](docs/MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md).
Ese plan es el backlog operativo recuperable; este roadmap continúa siendo la fuente
de verdad sobre el producto educativo y su secuencia.

## Estado verificable de partida

- La arquitectura curricular contiene 8 etapas, 40 partes y 480 posiciones de clase,
  de `SE-001` a `SE-480`, sin renumerar el material existente.
- Las Partes 00–01 contienen 24 clases desarrolladas con explicación, práctica,
  fuentes, navegación y un laboratorio ejecutable para `SE-013`–`SE-024`. Las partes
  02–29 conservan 336 borradores que deben revisarse y
  profundizarse. Las partes 30–39 disponen de estructura curricular y requieren aún el
  desarrollo íntegro de sus 120 clases.
- El portal publica el recorrido completo, pero la presencia de una página no demuestra
  por sí sola que la enseñanza, los laboratorios o sus resultados hayan sido validados.
- Los conteos describen archivos y alcance; la calidad se demuestra revisando contenido,
  ejecutando prácticas y comprobando evidencias.

## Resultado profesional buscado

La persona egresada podrá comprender sistemas ajenos, convertir necesidades ambiguas
en requisitos verificables, diseñar y construir software mantenible, probarlo,
asegurarlo, entregarlo, observarlo, operarlo, evolucionarlo y retirarlo. También podrá
justificar decisiones con evidencia técnica, económica, ética y organizacional.

La progresión común es:

**FUNDAMENTOS → COMPRENSIÓN → PRÁCTICA → CONSTRUCCIÓN → INTEGRACIÓN → PRODUCCIÓN →
OPERACIÓN → SISTEMAS COMPLEJOS → ARQUITECTURA → LIDERAZGO → EVOLUCIÓN → RETIRO**.

Git, seguridad, accesibilidad, observabilidad, economía, sostenibilidad, documentación
e IA controlada atraviesan el programa; no se enseñan como preocupaciones aisladas al
final del recorrido.

## Desarrollo previsto por parte

Cada fila fija el alcance que debe desarrollarse sin sustituirlo por una lista de
títulos. El artefacto expresa qué produce el estudiante y la comprobación indica cómo
se demuestra aprendizaje.

| Parte y clases | Contenido que se incorpora | Artefacto y comprobación principal |
|---|---|---|
| 00 · Ingeniería de software como profesión (`SE-001`–`SE-012`) | Fronteras de software, historia de la disciplina, ciclo de vida, ética, roles, evidencia, calidad, riesgo, sostenibilidad y lectura crítica de estándares. | Anatomía documentada de un producto y contrato de aprendizaje; defensa oral de límites, impactos y fuentes. |
| 01 · Computadores y representación de información (`SE-013`–`SE-024`) | Arquitectura de computador, datos binarios, Unicode, precisión numérica, CPU, memoria, procesos, compilación, runtimes, energía y límites físicos. | Experimento reproducible que conecta código, instrucciones, memoria, tiempo y consumo; resultados repetibles en dos entornos. |
| 02 · Sistemas operativos, terminal y automatización base (`SE-025`–`SE-036`) | Sistemas de archivos, identidad y permisos, procesos, shells, configuración, paquetes, logs, virtualización y diagnóstico multiplataforma. | Kit idempotente de preparación y reparación con pruebas de error, limpieza y recuperación. |
| 03 · Redes, Internet y protocolos (`SE-037`–`SE-048`) | TCP/IP, direccionamiento, transporte, DNS, HTTP, TLS, proxies, balanceo, CDN, sockets y captura de tráfico. | Servicio observable cuya petición se rastrea de extremo a extremo y se somete a latencia, pérdida, DNS y certificado inválido. |
| 04 · Pensamiento computacional y resolución de problemas (`SE-049`–`SE-060`) | Abstracción, lógica, relaciones, invariantes, inducción, corrección, complejidad, heurísticas, estado e investigación de hipótesis. | Especificación contrastable de un problema ambiguo, solución razonada y contraejemplos que delimitan su validez. |
| 05 · Fundamentos de programación (`SE-061`–`SE-072`) | Tipos, control, iteración, funciones, errores, colecciones, E/S, módulos, diseño por ejemplos, legibilidad y transferencia entre lenguajes. | Herramienta CLI modular con pruebas, manejo de errores, formatos estables y comparación de dos implementaciones. |
| 06 · Paradigmas de programación (`SE-073`–`SE-084`) | Imperativo, procedural, objetos, funcional, declarativo, lógico, eventos, reactivo, concurrencia y criterios para combinarlos. | Una misma regla de negocio implementada y probada bajo varios paradigmas; informe sobre semántica y trade-offs. |
| 07 · Estructuras de datos y algoritmos (`SE-085`–`SE-096`) | Secuencias, colas, mapas, árboles, grafos, búsqueda, ordenamiento, programación dinámica, backtracking, índices y medición empírica. | Biblioteca probada con benchmarks reproducibles y selección de estructura justificada por carga y restricciones. |
| 08 · Entornos, herramientas y depuración (`SE-097`–`SE-108`) | Editores, depuradores, profiling, logs, trazas, inspección de memoria, reproducibilidad, diagnóstico remoto y método de investigación. | Expediente de un bug difícil con hipótesis descartadas, causa raíz, prueba de regresión y mediciones antes/después. |
| 09 · Bibliotecas, paquetes, SDK y automatización (`SE-109`–`SE-120`) | Diseño de API interna, dependencias, SemVer, empaquetado, lockfiles, publicación, SDK, generación de código, licencias y automatización. | Paquete consumible y firmado, con contrato público, compatibilidad comprobada, SBOM y plan de deprecación. |
| 10 · Descubrimiento y estrategia de producto (`SE-121`–`SE-132`) | Stakeholders, dominio, entrevistas, observación, workshops, oportunidades, prototipos, outcomes, priorización y discovery continuo. | Dossier de descubrimiento con evidencia, mapa de supuestos, prototipo probado y decisión explícita de qué no construir. |
| 11 · Economía, métricas y decisiones de producto (`SE-133`–`SE-144`) | TCO, ROI, CAPEX/OPEX, coste de oportunidad, build-vs-buy, SaaS, licencias, FinOps, métricas y experimentación causal. | Caso económico con escenarios, sensibilidad, guardrails y recomendación reversible bajo incertidumbre. |
| 12 · Ingeniería de requisitos (`SE-145`–`SE-156`) | Elicitación, funcionales y no funcionales, restricciones, reglas, aceptación, priorización, trazabilidad, cambios y conflictos. | Baseline trazable que detecta requisitos ambiguos, contradictorios e incompletos y documenta su resolución. |
| 13 · Especificaciones, contratos y modelos (`SE-157`–`SE-168`) | Casos de uso, máquinas de estado, contratos, invariantes, UML útil, modelos de dominio, TLA+/Alloy introductorios y revisión. | Especificación ejecutable o verificable de un flujo crítico, con propiedades, contraejemplo y decisión documentada. |
| 14 · Experiencia, accesibilidad e internacionalización (`SE-169`–`SE-180`) | Investigación UX, arquitectura de información, semántica, WCAG, teclado, lectores de pantalla, Unicode, locale, tiempo, RTL e inclusión. | Flujo usable y accesible evaluado con pruebas automáticas y manuales, varios locales y reporte de barreras. |
| 15 · Procesos, planificación y estimación (`SE-181`–`SE-192`) | Ciclos de vida, flujo, Kanban/Scrum con criterio, throughput, cycle time, puntos, Function Points, COCOMO II y Monte Carlo. | Plan probabilístico con intervalos, dependencias, riesgos y actualización a partir de datos reales, no una fecha determinista. |
| 16 · Git, colaboración y código abierto (`SE-193`–`SE-204`) | Commits, branches, merge/rebase, PR, review, Issues, Projects, CODEOWNERS, releases, licencias, governance, OSPO e InnerSource. | Repositorio colaborativo operado mediante contribuciones reales, revisión razonada, release y gestión de vulnerabilidad. |
| 17 · Documentación y conocimiento técnico (`SE-205`–`SE-216`) | Documentación orientada a tareas, referencia, ADR, RFC, diagramas, glosarios, runbooks, knowledge bases, vigencia y docs-as-code. | Paquete documental probado por otra persona para operar y cambiar un sistema sin conocimiento tácito. |
| 18 · CLI, TUI, servicios y automatización (`SE-217`–`SE-228`) | Contratos de línea de comandos, streams, códigos de salida, TUI, daemons, jobs, scheduling, idempotencia y automatización segura. | Herramienta automatizable con interfaz estable, cancelación, reintentos, telemetría, instalación y desinstalación verificadas. |
| 19 · Web, frontend y aplicaciones progresivas (`SE-229`–`SE-240`) | Plataforma web, HTML/CSS/JS, estado, componentes, rendimiento, seguridad de navegador, PWA, accesibilidad y observabilidad cliente. | Aplicación web accesible con presupuestos de rendimiento, pruebas por capas y diagnóstico de un fallo de red o renderizado. |
| 20 · Backend, APIs y procesamiento asíncrono (`SE-241`–`SE-252`) | REST, RPC, GraphQL, gRPC, SSE, WebSockets, webhooks, OpenAPI, AsyncAPI, versionado, idempotencia, cuotas y workers. | API y consumidor contractualmente probados, con paginación, autorización, compatibilidad, deprecación y recuperación de duplicados. |
| 21 · Software móvil, escritorio y multiplataforma (`SE-253`–`SE-264`) | Ciclos de vida, almacenamiento local, sincronización, permisos, offline-first, distribución, actualizaciones, telemetría y trade-offs nativo/híbrido. | Cliente que trabaja sin conexión, reconcilia conflictos y demuestra actualización y rollback seguros. |
| 22 · Embedded, IoT y tiempo real (`SE-265`–`SE-276`) | Firmware, restricciones, hardware/software, interrupciones, RTOS, deadlines, protocolos, OTA, telemetría, edge y seguridad de dispositivo. | Prototipo o simulación con presupuesto temporal y energético, actualización recuperable y análisis de amenazas físicas y remotas. |
| 23 · Software especializado y dominios (`SE-277`–`SE-288`) | Modelado de restricciones médicas, financieras, industriales, científicas y públicas; safety, hazard analysis, auditoría y datos sensibles. | Análisis de un dominio regulado que traduce riesgo en requisitos, controles, pruebas y evidencia sin inventar cumplimiento. |
| 24 · Diseño, patrones y refactorización (`SE-289`–`SE-300`) | Modularidad, cohesión, acoplamiento, encapsulación, SOLID/GRASP críticos, composición, patrones, antipatterns, smells y refactoring. | Refactor incremental protegido por caracterización y métricas pertinentes; ADR que explica costes y alternativas descartadas. |
| 25 · Arquitectura de software y dominio (`SE-301`–`SE-312`) | Layered, hexagonal, clean/onion, monolito modular, DDD, SOA, microservicios, event-driven, serverless, edge y evolución. | Arquitectura derivada de atributos de calidad, con escenarios de fallo, límites, ADR y estrategia de evolución. |
| 26 · Datos, persistencia y recuperación (`SE-313`–`SE-324`) | OLTP/OLAP, modelado, transacciones, índices, caché, partición, réplica, CDC, contratos, migración, backup y restore. | Sistema de datos con migración compatible, medición de consultas, calidad de datos y restauración ensayada contra RPO/RTO. |
| 27 · Integración, eventos y mensajería (`SE-325`–`SE-336`) | Colas, streams, logs, entrega, orden, esquemas, outbox/inbox, sagas, CQRS, event sourcing y compatibilidad entre productores. | Flujo asíncrono sometido a duplicación, retraso, reordenamiento y poison messages, con reconciliación demostrada. |
| 28 · Concurrencia y sistemas distribuidos (`SE-337`–`SE-348`) | Memoria y coordinación, relojes, fallos parciales, consistencia, CAP/PACELC, consenso, elección, replicación, retries y discovery. | Laboratorio de fallos que mide comportamiento ante partición, latencia y reinicio y explica qué garantías conserva o pierde. |
| 29 · Cloud, plataforma e infraestructura (`SE-349`–`SE-360`) | Modelos cloud, IAM, redes, cómputo, storage, containers, Kubernetes, IaC, GitOps, multi-entorno, costes y arquitectura cloud-native. | Entorno reproducible con mínimo privilegio, políticas, costes estimados, destrucción segura y recuperación documentada. |
| 30 · Estrategia y técnicas de prueba (`SE-361`–`SE-372`) | Unitarias, integración, sistema, aceptación, E2E, contrato, property-based, mutation, fuzzing, snapshots y selección de qué no probar. | Estrategia de riesgo con suites ejecutables, oráculos claros, datos controlados y análisis explícito de falsos positivos y huecos. |
| 31 · Calidad, rendimiento y resiliencia (`SE-373`–`SE-384`) | ISO 25010/SQuaRE, deuda, análisis estático, métricas y límites, profiling, carga, percentiles, capacidad, degradación, DR y chaos. | Informe de calidad y game day con baseline, cuello de botella, mejora medida, recuperación y deuda residual priorizada. |
| 32 · Seguridad, privacidad y cumplimiento (`SE-385`–`SE-396`) | Threat modeling, secure design/coding, secretos, IAM, OWASP, SAST/DAST/SCA, privacidad, respuesta y trazabilidad regulatoria. | Cadena LEY/REGULACIÓN → REQUISITO → CONTROL → IMPLEMENTACIÓN → PRUEBA → EVIDENCIA → AUDITORÍA aplicada a un caso. |
| 33 · Build, release y cadena de suministro (`SE-397`–`SE-408`) | Builds reproducibles, artefactos, repositorios, SBOM, provenance, signing, SLSA, OpenSSF, pinning, typosquatting y releases. | Release reconstruible y verificable con inventario, firma, procedencia y simulación de dependencia comprometida. |
| 34 · CI/CD, IaC y platform engineering (`SE-409`–`SE-420`) | Pipelines, quality gates, ambientes, progressive delivery, canary, blue/green, rollback, IDP, portales, golden paths, DevEx y DORA/SPACE. | Camino autoservicio medido como producto, con despliegue progresivo, rollback probado y evaluación del riesgo de métricas. |
| 35 · Observabilidad, SRE e incidentes (`SE-421`–`SE-432`) | SLI/SLO/SLA, error budgets, toil, logs, métricas, traces, OpenTelemetry, alertas, runbooks, incident command y postmortems. | Incidente simulado: DETECTAR → CONTENER → DIAGNOSTICAR → RECUPERAR → ANALIZAR → APRENDER, con timeline y acciones verificables. |
| 36 · Mantenimiento y modernización legacy (`SE-433`–`SE-444`) | Arqueología, ingeniería inversa, caracterización, dependencias, deuda, strangler, branch by abstraction, ACL, migraciones, EOL y retiro. | Modernización incremental de un sistema ajeno con mapa de dependencias, compatibilidad, rollout, archivo y borrado seguro. |
| 37 · Gestión, liderazgo y práctica profesional (`SE-445`–`SE-456`) | Rutas técnicas y de gestión, mentoring, reviews, negociación, priorización, Conway, Team Topologies, carga cognitiva, ownership y crisis. | Propuesta técnica defendida ante intereses en conflicto, plan organizacional y retrospectiva de una decisión bajo incertidumbre. |
| 38 · Desarrollo de software asistido por IA (`SE-457`–`SE-468`) | IA en requisitos, diseño, código, review, pruebas, documentación, debugging, DevOps, seguridad, incidentes, legacy, evals y costes. | Cambio asistido con trazabilidad de prompts y herramientas, pruebas deterministas, revisión humana, seguridad y comparación de coste/latencia. |
| 39 · SPEC, agentes y ciclo de vida agentic (`SE-469`–`SE-480`) | Coding/terminal agents, MCP, tools, skills, memoria, contexto, instrucciones de repositorio, multiagente, guardrails, loops y regresiones. | Flujo agentic evaluable donde HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS VERIFICAN → HUMANO REVISA → SISTEMA VALIDA. |

## Ejes transversales obligatorios

- **Git y colaboración:** cada parte produce cambios revisables, historial comprensible y
  decisiones trazables.
- **Calidad y pruebas:** la estrategia nace del riesgo; incluye qué no merece una prueba
  y evita confundir cobertura con confianza.
- **Seguridad, privacidad y supply chain:** amenazas, privilegios, dependencias,
  procedencia y respuesta aparecen desde diseño hasta retiro.
- **Accesibilidad e internacionalización:** semántica, teclado, lectores de pantalla,
  Unicode, locales y zonas horarias se comprueban en los productos que corresponda.
- **Observabilidad y operación:** los sistemas relevantes deben permitir detectar,
  diagnosticar, recuperar y aprender de fallos.
- **Economía y sostenibilidad:** las decisiones consideran TCO, coste de oportunidad,
  energía, carbono, capacidad y vida útil.
- **IA en ingeniería:** se estudian beneficios y fallos —APIs inventadas, dependencias
  falsas, código inseguro, drift, pérdida de contexto, licencias, coste y loops— con
  evals, guardrails y revisión humana.

## Modelo de clases, laboratorios y evaluación

Una clase profunda conecta **CONCEPTO → FUNDAMENTO → MECANISMO → EJEMPLO →
IMPLEMENTACIÓN → ERROR → DEBUGGING → PRODUCCIÓN → TRADE-OFF → EJERCICIO** cuando el
tema lo permite. Debe explicar qué es, por qué existe, cuándo usarlo o evitarlo, cómo
falla, cómo se mantiene y qué evidencia permitiría aceptar la solución.

Los laboratorios producen código, pruebas, diagramas, ADR, RFC, contratos de API,
pipelines, dashboards, postmortems, threat models, SBOM, benchmarks, planes de
migración y runbooks. Una ejecución debe declarar entorno, versiones, preparación,
criterios de éxito, limpieza y recuperación.

La evaluación combina explicación, implementación, debugging, code review, diseño,
incidentes y defensa de decisiones. Para cada competencia pregunta: ¿puede explicarla,
implementarla, probarla, detectar que falló, operarla y justificar su decisión?

## Proyectos integradores

El caso conductor evoluciona durante el programa y conserva evidencia de requisitos,
diseño, implementación, pruebas, seguridad, entrega, observabilidad, operación,
incidentes, mantenimiento y retiro. Además, deben existir cuatro recorridos distinguibles:

1. **Producto profesional completo:** desde discovery hasta operación con usuarios y
   cambios de requisitos.
2. **Sistema distribuido:** contratos, mensajería, consistencia y experimentos de fallos.
3. **Modernización legacy:** sistema sin documentación, caracterización, migración
   progresiva y retiro sin reescritura automática.
4. **Decisión económica e IA controlada:** build-vs-buy y TCO, seguida de una mejora
   asistida por agentes con evals, provenance, revisión humana y regresión automatizada.

Los casos reales separan siempre **HECHOS / INTERPRETACIÓN / LECCIONES** y enlazan
fuentes primarias; no se completan vacíos con detalles inventados.

## Fases de implementación

1. **Consolidar la base:** preservar `SE-001`–`SE-480`, eliminar metadatos editoriales
   que no enseñan, sincronizar índices y mantener validadores estructurales.
2. **Profundizar por partes:** trabajar una parte completa, revisar cada tema anunciado,
   ejecutar sus prácticas y publicar contenido íntegro; un commit por parte.
3. **Integrar proyectos y rutas:** reutilizar clases para fundamentos, backend,
   frontend, full-stack, QA, DevOps, SRE, platform, arquitectura, seguridad, legacy,
   liderazgo e ingeniería aumentada por IA.
4. **Cerrar brechas verificadas:** contrastar con SWEBOK, ISO/IEC/IEEE 12207, 15288,
   29148, ISO/IEC 25010/SQuaRE, ACM/IEEE CS2023, OWASP, NIST, CNCF, OpenSSF, SLSA,
   DORA, Google SRE, WCAG/W3C y documentación oficial vigente.
5. **Expandir solo con justificación:** añadir clases después de `SE-480` únicamente si
   una auditoría demuestra que una competencia no cabe con profundidad y sin duplicar
   repositorios especializados. Toda adición actualiza navegación, rutas, evaluación,
   bibliografía y métricas en el mismo cambio.

## Backlog trazable por entregas

Este backlog conserva el trabajo pendiente sin convertir el número de clases en una
cuota. Cada fila se cierra únicamente con revisión de la parte completa, laboratorio o
actividad reproducible, fuentes próximas, portal regenerado y gates verdes.

| Orden | Entrega | Resultado verificable | Estado al 2026-10-06 |
| ---: | --- | --- | --- |
| 1 | Partes 00–01 | fundamentos profesionales y observación de un programa por capas | completadas; Parte 01 incluye laboratorio con seis pruebas |
| 2 | Partes 02–04 | entorno reproducible, petición de red observable y modelo de decisión | siguiente bloque; revisar y ejecutar una parte por commit |
| 3 | Partes 05–09 | construcción, paradigmas, algoritmos, depuración y empaquetado | contenido editorial existente; falta aprobación cualitativa y ejecución |
| 4 | Partes 10–14 | discovery, economía, requisitos, contratos, UX, accesibilidad e i18n | contenido editorial existente; falta aprobación cualitativa y evidencia |
| 5 | Partes 15–29 | planificación, colaboración, superficies, arquitectura, datos y cloud | borradores publicados; reconstruir en orden y preservar proyectos |
| 6 | Partes 30–37 | testing, calidad, seguridad, supply chain, plataforma, SRE, legacy y liderazgo | estructura curricular; desarrollar prácticas y casos reales |
| 7 | Partes 38–39 | IA asistida, SPEC y agentes controlados | estructura curricular; exigir evals, guardrails, coste y regresión |
| 8 | Integración transversal | glosario relacional, bibliografía temática, rutas, cuatro proyectos integradores y casos HECHOS/INTERPRETACIÓN/LECCIONES | actualizar junto con cada parte; no dejar una reconciliación final masiva |
| 9 | Auditoría de expansión | brechas residuales con competencia, artefacto y secuencia propias | no habilitada todavía: primero intentar integración en `SE-001`–`SE-480` |

Las brechas candidatas siguen siendo métodos formales aplicados, GreenOps medible,
InnerSource/OSPO, DevEx/SPACE, API en tiempo real, estimación probabilística,
compliance engineering, rutas Staff/Principal/Manager y retiro seguro. Cada candidata
debe documentar por qué no cabe con profundidad en una clase existente antes de recibir
un ID posterior a `SE-480`.

## Criterio de término del programa

El programa no está terminado porque existan 480 o aproximadamente 500 clases. Está
terminado cuando cada tema prometido se desarrolla, cada práctica relevante se puede
reproducir, las fuentes respaldan afirmaciones, los proyectos integran el ciclo de vida,
las rutas son transitables, el portal publica el contenido completo y las validaciones
estructurales, pedagógicas y técnicas concuerdan con la evidencia.

Una revisión final debe comprobar estructura, navegación, enlaces, numeración,
terminología, duplicaciones, fuentes, laboratorios, evaluaciones, proyectos, progresión,
rutas, archivos vacíos, placeholders y referencias inventadas. El informe resultante
explica qué existía, qué faltaba, qué se amplió, qué se creó, qué se preservó y qué queda
pendiente, con métricas antes/después que no sustituyen el juicio cualitativo.
