# Auditoría de cobertura — 2026-10-06

## Alcance y método

Esta auditoría actualiza, sin reescribir, la fotografía histórica del
[4 de octubre de 2026](PROGRAM-COVERAGE-AUDIT-2026-10-04.md). Contrasta el mandato
curricular con `ROADMAP.md`, `curriculum.yaml`, las 480 carpetas de clase, fuentes,
validadores, portal y prácticas ejecutables. Un título o una página generada demuestra
ubicación curricular; no demuestra enseñanza completa.

El mandato completo y la acción específica acordada para cada clase se conservan en el
[`plan maestro de implementación`](MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md). Esta
auditoría sigue siendo la fotografía de estado; el plan es el backlog recuperable.

Se revisaron cualitativamente las Partes 01–05 clase por clase, se ejecutaron sus
laboratorios comunes y se reconsultaron fuentes oficiales vigentes. Unicode 18.0,
Java SE 27, la biblioteca ratificada de RISC-V, Python 3, SCI, POSIX.1-2024 y GNU
Bash 5.3 sustituyen marcadores de versión ya superados sin alterar referencias
históricas.

## Línea base verificable

- 8 etapas, 40 partes y 480 IDs consecutivos (`SE-001`–`SE-480`);
- 72 clases desarrolladas (`SE-001`–`SE-072`), 288 borradores y 120 estructuras;
- Partes 00–05 desarrolladas; Partes 06–29 publicadas para revisión; Partes 30–39
  pendientes de desarrollo íntegro;
- 521 páginas HTML generadas;
- cinco laboratorios ejecutables transversales: el de la Parte 01 con fixture sintético
  y seis pruebas, el de la Parte 02 con diez pruebas y adaptadores PowerShell/Bash, y
  el de la Parte 03 con siete escenarios de red locales y once pruebas, y el de la
  Parte 04 con especificación contrastable y trece pruebas, y el de la Parte 05 con
  CLI empaquetada, quince contratos y un puerto Rust contrastado en CI;
- tres workflows; la evidencia remota del incremento se acepta solo cuando sus jobs y
  Pages terminen en verde.

## Matriz de diagnóstico

| Área | Estado | Archivos existentes | Profundidad | Brechas | Acción |
| --- | --- | --- | --- | --- | --- |
| Fundamentos, profesión y ética | PARCIAL | Partes 00–05; `content/part-00..05`; laboratorios de Partes 01–05 | Partes 00–05 desarrolladas | paradigmas y estructuras aún no permiten comparar estilos y costes sobre un contrato común | desarrollar la Parte 06 sobre la CLI y conservar los mecanismos ya validados |
| Construcción, paradigmas y depuración | PARCIAL | Parte 05 desarrollada; Partes 06–09 y `polyglot-programming-labs` | CLI, fronteras y transferencia Python/Rust verificadas; resto en borrador | paradigmas, estructuras, depuración y empaquetado ampliado no han sido validados de extremo a extremo | profundizar decisiones de ingeniería aquí y conservar sintaxis especializada fuera |
| Requisitos y discovery | SUPERFICIAL | Partes 10, 12 y 13 | títulos y borradores | observación, workshops, conflictos, NFR y cambio no están aprobados | construir trazabilidad necesidad → requisito → prueba → evidencia |
| Economía, estimación y experimentación | SUPERFICIAL | Partes 11, 15 y 37 | cobertura nominal | Monte Carlo, Function Points, COCOMO II y compromiso probabilístico requieren práctica | profundizar `SE-185`, `SE-191` y el proyecto económico antes de dividir |
| Diseño, patrones y refactorización | SUPERFICIAL | Parte 24 | borrador | GRASP, antipatterns y criterios de no refactorizar no tienen evidencia ejecutada | proteger refactor con caracterización y ADR contextual |
| Arquitectura y sistemas sociotécnicos | SUPERFICIAL | Partes 25, 29 y `SE-310` | borradores | SOA, cloud-native, Conway, inverse Conway y Team Topologies no están desarrollados | usar CONTEXTO → PROBLEMA → SOLUCIÓN → COSTE → FALLOS → OPERACIÓN → EVOLUCIÓN |
| API engineering | SUPERFICIAL | `SE-163`, Parte 20 y `SE-331` | contratos y protocolos anunciados | gRPC, WebSockets, SSE, gateways y deprecación no forman aún un recorrido aprobado | reconciliar las clases existentes; expandir solo si el artefacto contractual no cabe |
| Sistemas distribuidos | SUPERFICIAL | Partes 27–28 | buenos títulos, contenido no aprobado | PACELC, discovery y experimentos de fallos completos | construir relojes, partición, duplicación, consenso y degradación controlada |
| Software intensivo en datos | SUPERFICIAL | Partes 26–27 y `database-systems-labs` | borradores | contratos, calidad, CDC y evolución no tienen trazabilidad completa | enseñar decisiones aquí y motores/consultas en el repositorio especializado |
| Testing y calidad | AUSENTE | Partes 30–31 | scaffolds | no existe contenido enseñable ni selección explícita de qué no probar | desarrollar estrategia por riesgo antes de técnicas |
| Rendimiento y resiliencia | PARCIAL | Parte 01 desarrollada; Partes 31 y 35 planificadas | medición fundamental validada; producción y recuperación ausentes | carga, colas, capacity planning, RTO/RPO, DR y game days | reutilizar el protocolo de `SE-022` y añadir fallos productivos en 31/35 |
| DevOps, Platform Engineering y DevEx | AUSENTE | Partes 33–34 | scaffolds | platform-as-product, Backstage, SPACE y self-service no están desarrollados | construir golden path y evaluar métricas sin gaming |
| SRE, observabilidad e incidentes | AUSENTE | Parte 35 | scaffolds | falta practicar detectar → contener → diagnosticar → recuperar → aprender | usar OpenTelemetry y Google SRE; conservar timelines reales de simulación |
| Seguridad, privacidad y compliance | AUSENTE | Parte 32 y fuentes NIST/OWASP | scaffolds | no se ha desarrollado regulación → requisito → control → prueba → evidencia → auditoría | construir threat model, pruebas negativas y límites jurisdiccionales |
| Supply chain | AUSENTE | Parte 33 | scaffolds | SBOM, SLSA, OpenSSF, signing y ataques de dependencias no son enseñables aún | verificar procedencia y reconstrucción con artefactos reales |
| Git y colaboración | SUPERFICIAL | Parte 16 y reglas transversales | borrador | Projects, Dependabot, Packages, releases y mantenimiento comunitario | mantener Git transversal; no fragmentar por cada control de UI |
| Legacy, evolución y retiro | AUSENTE | Parte 36 | scaffolds | estrategia comparativa, EOL, retención y borrado seguro | proyecto brownfield reversible con caracterización y plan de retiro |
| Open Source, InnerSource y organizaciones | SUPERFICIAL | Parte 16, `SE-310` y Parte 37 | títulos parciales | OSPO, sostenibilidad, bus factor y topologías de equipo | integrar gobernanza y ownership; dividir solo con artefacto independiente |
| Carrera y liderazgo | PARCIAL | Parte 37 y 40 guías en `roles/` | rutas navegables; clases aún no desarrolladas | Staff/Principal/Architect/Manager/Platform/SRE/Security/QA requieren evidencia | reutilizar clases y evaluar mentoría, crisis y defensa de decisiones |
| Métodos formales y sistemas críticos | SUPERFICIAL | `SE-157`–`SE-161`, `SE-274`, `SE-283` | introducción planificada | TLA+, Alloy, hazards y límites de assurance | profundizar primero; expandir solo si un laboratorio indivisible no cabe |
| Embedded, IoT y edge | SUPERFICIAL | Parte 22 | borrador | RTOS, OTA y device security no están verificados | usar simulación honesta y declarar ausencia de hardware |
| Green software | PARCIAL | `SE-009`, `SE-022`, `SE-134`, `SE-267`, `SE-356` | `SE-022` delimita energía/SCI; GreenOps pendiente | falta medición física, carbon awareness operativo y efectos rebote | integrar medición en 29/31 sin inventar reducción desde tiempo |
| Accesibilidad e internacionalización | SUPERFICIAL | Parte 14; Unicode 18.0 en Parte 01 | representación de texto desarrollada; experiencia inclusiva pendiente | RTL, pluralización, teclado, zoom y lector de pantalla | construir y verificar un flujo localizado accesible |
| IA aplicada y agentes | AUSENTE | Partes 38–39 | scaffolds | evals, APIs inventadas, loops, coste, provenance y regresiones | aplicar HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS VERIFICAN → HUMANO REVISA → SISTEMA VALIDA |
| Casos reales, laboratorios y evaluación | PARCIAL | actividades, rúbricas, Parte 00 y laboratorios de Partes 01–05 | cinco prácticas ejecutables conservadas; evidencia escasa en el resto | casos documentados y artefactos ejecutados deben crecer parte a parte | separar HECHOS / INTERPRETACIÓN / LECCIONES y no inventar resultados |
| Fuentes, glosario, rutas y portal | PARCIAL | `sources/`, `roles/`, `site/`, `docs/SOURCES.md` | portal íntegro y rutas publicadas; glosario temático incompleto | fuentes por afirmación y relaciones terminológicas faltan fuera de partes aprobadas | actualizar junto a cada parte y evitar archivos huérfanos |

## Revisión clase a clase de la Parte 02

La marca `COMPLETA` de esta tabla significa que la clase superó la revisión de
contenido, actividad, rúbrica, fuentes, navegación y publicación dentro de su alcance.
No significa que se hayan probado todas las versiones, políticas o plataformas que la
clase analiza.

| Clase | Estado | Hallazgo de la revisión | Mejora y evidencia incorporada |
| --- | --- | --- | --- |
| `SE-025` | COMPLETA | la comparación por nombre de sistema podía ocultar arquitectura, runtime y política | matriz de capacidades minimizada, separación API/ABI/ISA y práctica `prepare`/`inspect` sin identificadores personales |
| `SE-026` | COMPLETA | rutas, enlaces y sensibilidad necesitaban distinguir sintaxis de capacidad efectiva | probes sintéticos confinados al workspace, negativa de escape y limpieza explícita |
| `SE-027` | COMPLETA | el tratamiento de permisos debía evitar que elevación fuera la primera respuesta | modelo sujeto–acción–objeto–política, marker de ownership y rechazo con código 3 |
| `SE-028` | COMPLETA | proceso, servicio y ejecutable podían confundirse en una sola entidad | línea temporal, cancelación, códigos de salida y comprobación de ausencia de procesos residuales |
| `SE-029` | COMPLETA | quoting, streams y pipelines requerían un contrato observable, no recetas de shell | ruta con espacios, separación datos/diagnóstico y preservación del fallo intermedio |
| `SE-030` | COMPLETA | una traducción literal entre Bash y PowerShell no demostraba portabilidad | dos adaptadores mínimos sobre el mismo núcleo y pruebas del esquema y códigos compartidos |
| `SE-031` | COMPLETA | configuración y secreto podían mezclarse o revelar el entorno completo | precedencia argumento > entorno > archivo > default y prueba con centinela redactado |
| `SE-032` | COMPLETA | la instalación se presentaba sin suficiente procedencia, alcance y retiro | manifiesto de herramientas y decisión explícita de no instalar durante el laboratorio |
| `SE-033` | COMPLETA | los logs podían confundirse con causas concluyentes | eventos estructurados, primera divergencia, hipótesis rival, minimización y revisión de privacidad |
| `SE-034` | COMPLETA | VM, WSL y contenedor necesitaban compararse por fronteras, no por etiquetas | mapa de kernel, montajes, red y recursos; evidencia clasificada como ejecutada, diseñada o no disponible |
| `SE-035` | COMPLETA | la reparación podía borrar el síntoma o cambiar varias variables a la vez | ciclo reproducir–diagnosticar–reparar–regresar con corrupción controlada y regresión |
| `SE-036` | COMPLETA | el proyecto necesitaba ser un producto operable y no una colección de comandos | núcleo Python, adaptadores, diez pruebas, códigos 0/2/3, limpieza conservadora y registro de validación |

## Revisión clase a clase de la Parte 03

`COMPLETA` significa que la clase superó revisión de mecanismo, práctica, límites,
fuentes, actividad, rúbrica, navegación y publicación. El laboratorio usa sockets
reales solo en loopback; DNS, confianza TLS y pérdida se identifican como modelos.

| Clase | Estado | Hallazgo de la revisión | Mejora y evidencia incorporada |
| --- | --- | --- | --- |
| `SE-037` | COMPLETA | los modelos podían leerse como implementación literal | hipótesis rivales y mapa de observaciones por frontera |
| `SE-038` | COMPLETA | loopback podía confundirse con evidencia Ethernet/Wi-Fi | límites explícitos y diseño de una práctica LAN autorizada |
| `SE-039` | COMPLETA | faltaba separar ruta observada de NAT diseñada | longest-prefix match verificable sin modificar rutas del host |
| `SE-040` | COMPLETA | los reintentos no distinguían resultado desconocido | conexión, deadline, pérdida sintética e idempotencia en una matriz |
| `SE-041` | COMPLETA | DNSSEC y caché negativa requerían mecanismo y límites | NXDOMAIN/SOA/TTL y estados secure/insecure/bogus con RFC 2308/4033 |
| `SE-042` | COMPLETA | el éxito final podía borrar el 503 previo | historial de intentos, semántica de método y caso ETag/304 diseñado |
| `SE-043` | COMPLETA | una simulación podía parecer handshake real | rechazo de nombre tipado y práctica separada de cadena, vigencia y revocación |
| `SE-044` | COMPLETA | faltaba una política comprobable de cabeceras confiables | mapa de saltos y tratamiento de Forwarded, Via, request ID y traceparent |
| `SE-045` | COMPLETA | conexión abierta podía confundirse con entrega | estados de polling/SSE/WebSocket, backpressure y cierre verificado |
| `SE-046` | COMPLETA | una muestra pequeña podía producir métricas falsas | telemetría mínima, privacidad y prohibición de inferir p95 o pérdida real |
| `SE-047` | COMPLETA | correlación temporal podía presentarse como causalidad | primera divergencia, hipótesis rivales y Trace Context con límites de confianza |
| `SE-048` | COMPLETA | faltaba un producto local ejecutable y recuperable | siete escenarios, once pruebas, resultados tipados, redacción y limpieza |

## Revisión clase a clase de la Parte 04

| Clase | Estado | Hallazgo de la revisión | Mejora y evidencia incorporada |
| --- | --- | --- | --- |
| `SE-049` | COMPLETA | descomponer podía reducirse a listar tareas | dos descomposiciones y restricciones transversales preservadas |
| `SE-050` | COMPLETA | plausibilidad y consecuencia lógica podían confundirse | tabla exhaustiva y contraejemplo ejecutable |
| `SE-051` | COMPLETA | relación, función, árbol y grafo requerían multiplicidad explícita | recorrido cíclico con visitados y consulta discriminante |
| `SE-052` | COMPLETA | contratos positivos no mostraban cómo fallar | outcomes incompletos, autorización y presupuesto como casos negativos |
| `SE-053` | COMPLETA | recursión sintáctica no demostraba progreso | caso base, reducción, medida y comparación iterativa |
| `SE-054` | COMPLETA | terminar podía confundirse con resolver | corrección parcial, variante e inconclusión separadas |
| `SE-055` | COMPLETA | un benchmark podía reemplazar el análisis | conteos de operaciones separados de tiempo de pared |
| `SE-056` | COMPLETA | la heurística podía presentarse como aproximación garantizada | búsqueda adversarial y oráculo exacto para casos pequeños |
| `SE-057` | COMPLETA | el diagrama no hacía ejecutables las transiciones | tabla de estados y rechazo de secuencias imposibles |
| `SE-058` | COMPLETA | evidencia contraria podía desaparecer del relato | timeline preservado y detención ante contradicción |
| `SE-059` | COMPLETA | requisitos contradictorios podían resolverse en silencio | conflicto, actores, experimento seguro y criterio de salida |
| `SE-060` | COMPLETA | la especificación necesitaba implementación y oráculo independientes | fixtures, solución, trece pruebas, contraejemplos y límites |

## Revisión clase a clase de la Parte 05

| Clase | Estado | Hallazgo de la revisión | Mejora y evidencia incorporada |
| --- | --- | --- | --- |
| `SE-061` | COMPLETA | tipo Python, representación JSON y valor del dominio podían confundirse | parser estricto y rechazo explícito de `true` como presupuesto entero |
| `SE-062` | COMPLETA | el control podía reducirse a ramas sin semántica | tabla de decisiones, guard clauses ordenadas y casos de rechazo observables |
| `SE-063` | COMPLETA | streaming podía presentarse sin progreso ni terminación | límites de bytes, pruebas no repetidas y máximo de pasos por especificación |
| `SE-064` | COMPLETA | una función nombrada todavía podía ocultar I/O | núcleo puro, dependencias visibles y pruebas con streams sustituibles |
| `SE-065` | COMPLETA | capturar excepciones podía borrar defectos internos | `Result` para fallos esperados y taxonomía estable de códigos de proceso |
| `SE-066` | COMPLETA | elegir colecciones por costumbre ocultaba aliasing | tuplas, `frozenset`, mapas por operación e inmutabilidad comprobada |
| `SE-067` | COMPLETA | JSON válido podía confundirse con dominio válido | UTF-8, JSON/JSONL, esquema, `NaN`, tamaño y separación stdout/stderr |
| `SE-068` | COMPLETA | separar archivos no garantizaba dirección de dependencia | grafo CLI → adapters/engine → domain y superficie pública verificada |
| `SE-069` | COMPLETA | cobertura de líneas podía sustituir selección por riesgo | quince pruebas de ejemplos, límites, propiedades, integración y consumidor |
| `SE-070` | COMPLETA | legibilidad podía evaluarse solo por estilo | tarea de mantenimiento, refactor protegido y cambio semántico rechazado |
| `SE-071` | COMPLETA | traducción literal entre lenguajes ocultaba ownership y alcance | puerto Rust, cuatro fixtures comunes y límites de equivalencia declarados |
| `SE-072` | COMPLETA | ejecutar un script no demostraba entrega | paquete local, CLI, ayuda, streams, códigos, tests y aceptación reproducible |

## Decisión sobre nuevas clases

No se crean IDs posteriores a `SE-480` en este incremento. La Parte 01 demuestra que
una brecha de práctica puede resolverse con un laboratorio transversal sin fragmentar
la secuencia. Los candidatos a expansión permanecen en investigación en `ROADMAP.md`.
Una clase nueva necesitará competencia propia, artefacto distinto, prerrequisitos y
evidencia de que integrar el tema en una clase existente degradaría su profundidad.

## Próximo incremento

La Parte 06 (`SE-073`–`SE-084`) es la siguiente unidad indivisible. Debe comparar
paradigmas sobre el mismo motor de reglas, conservar fixtures comunes y demostrar
estado, efectos, backpressure, aislamiento y límites sin declarar un ganador universal.

## Métricas antes y después del incremento

| Métrica | 2026-10-04 | Parte 01 | Parte 02 | Parte 03 | Parte 04 | Parte 05 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| clases desarrolladas | 12 | 24 | 36 | 48 | 60 | 72 |
| borradores publicados | 348 | 336 | 324 | 312 | 300 | 288 |
| estructuras curriculares | 120 | 120 | 120 | 120 | 120 | 120 |
| laboratorios ejecutables versionados | 0 | 1 | 2 | 3 | 4 | 5 |
| pruebas del laboratorio de Parte 01 | 0 | 6 | 6 | 6 | 6 | 6 |
| pruebas del laboratorio de Parte 02 | 0 | 0 | 10 | 10 | 10 | 10 |
| pruebas del laboratorio de Parte 03 | 0 | 0 | 0 | 11 | 11 | 11 |
| pruebas del laboratorio de Parte 04 | 0 | 0 | 0 | 0 | 13 | 13 |
| pruebas del laboratorio de Parte 05 | 0 | 0 | 0 | 0 | 0 | 15 |
| clases totales | 480 | 480 | 480 | 480 | 480 | 480 |
| páginas HTML | 521 | 521 | 521 | 521 | 521 | 521 |

Los conteos no sustituyen la revisión cualitativa. El cambio conserva las 480 clases,
la navegación y el historial; profundiza una parte completa y deja explícito lo que no
se midió.

## Fuentes primarias reconsultadas

- [RISC-V Ratified Specifications Library](https://docs.riscv.org/), consultada el 2026-10-06.
- [The Unicode Standard 18.0](https://www.unicode.org/versions/Unicode18.0.0/), consultada el 2026-10-06.
- [Python 3 documentation](https://docs.python.org/3/), consultada el 2026-10-06.
- [Java Virtual Machine Specification SE 27](https://docs.oracle.com/javase/specs/jvms/se27/html/), consultada el 2026-10-06.
- [Software Carbon Intensity](https://greensoftware.foundation/standards/sci/), consultada el 2026-10-06.
- [POSIX.1-2024, Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/), consultada el 2026-10-06.
- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/), consultada el 2026-10-06.
- [PowerShell documentation](https://learn.microsoft.com/powershell/), consultada el 2026-10-06.
- [Windows Subsystem for Linux documentation](https://learn.microsoft.com/windows/wsl/), consultada el 2026-10-06.
- [RFC 2308 — Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308), reconsultada el 2026-10-06.
- [RFC 4033 — DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033), reconsultada el 2026-10-06.
- [RFC 7239 — Forwarded HTTP Extension](https://www.rfc-editor.org/rfc/rfc7239), reconsultada el 2026-10-06.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/), reconsultada el 2026-10-06.
- [MIT Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/), reconsultada el 2026-10-06.
- [MIT Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/), reconsultada el 2026-10-06.
- [MIT Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/), reconsultada el 2026-10-06.
- [Python Language Reference](https://docs.python.org/3/reference/), reconsultada el 2026-10-06.
- [Python `json` documentation](https://docs.python.org/3/library/json.html), reconsultada el 2026-10-06.
- [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259), reconsultada el 2026-10-06.
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/), reconsultada el 2026-10-06.

No se afirma acceso al texto completo de normas de pago ni ejecución en hardware no
disponible. Los resultados de CI y Pages se documentan después de la publicación.
