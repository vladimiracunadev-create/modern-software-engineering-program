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

Se revisó cualitativamente la Parte 01 clase por clase, se ejecutó su laboratorio común
y se reconsultaron fuentes oficiales vigentes. Unicode 18.0, Java SE 27, la biblioteca
ratificada de RISC-V, Python 3 y SCI sustituyen marcadores de versión ya superados sin
alterar referencias históricas.

## Línea base verificable

- 8 etapas, 40 partes y 480 IDs consecutivos (`SE-001`–`SE-480`);
- 24 clases desarrolladas (`SE-001`–`SE-024`), 336 borradores y 120 estructuras;
- Partes 00–01 desarrolladas; Partes 02–29 publicadas para revisión; Partes 30–39
  pendientes de desarrollo íntegro;
- 521 páginas HTML generadas;
- un laboratorio ejecutable transversal a la Parte 01, con fixture sintético y seis
  pruebas automáticas;
- tres workflows; la evidencia remota del incremento se acepta solo cuando sus jobs y
  Pages terminen en verde.

## Matriz de diagnóstico

| Área | Estado | Archivos existentes | Profundidad | Brechas | Acción |
| --- | --- | --- | --- | --- | --- |
| Fundamentos, profesión y ética | PARCIAL | Partes 00–04; `content/part-00..04`; laboratorio de Parte 01 | Partes 00–01 desarrolladas; 02–04 no aprobadas | sistemas operativos, redes y razonamiento computacional aún carecen de ejecución y revisión integral | desarrollar Partes 02–04, una por commit, reutilizando la evidencia del analizador |
| Construcción, paradigmas y depuración | SUPERFICIAL | Partes 05–09 y `polyglot-programming-labs` | borradores editoriales | mecanismos, fallos y transferencia entre paradigmas no han sido validados de extremo a extremo | profundizar decisiones de ingeniería aquí y conservar sintaxis especializada fuera |
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
| Casos reales, laboratorios y evaluación | PARCIAL | actividades, rúbricas, Parte 00 y laboratorio Parte 01 | primera práctica ejecutable conservada; evidencia escasa en el resto | casos documentados y artefactos ejecutados deben crecer parte a parte | separar HECHOS / INTERPRETACIÓN / LECCIONES y no inventar resultados |
| Fuentes, glosario, rutas y portal | PARCIAL | `sources/`, `roles/`, `site/`, `docs/SOURCES.md` | portal íntegro y rutas publicadas; glosario temático incompleto | fuentes por afirmación y relaciones terminológicas faltan fuera de partes aprobadas | actualizar junto a cada parte y evitar archivos huérfanos |

## Decisión sobre nuevas clases

No se crean IDs posteriores a `SE-480` en este incremento. La Parte 01 demuestra que
una brecha de práctica puede resolverse con un laboratorio transversal sin fragmentar
la secuencia. Los candidatos a expansión permanecen en investigación en `ROADMAP.md`.
Una clase nueva necesitará competencia propia, artefacto distinto, prerrequisitos y
evidencia de que integrar el tema en una clase existente degradaría su profundidad.

## Próximo incremento

La Parte 02 (`SE-025`–`SE-036`) es la siguiente unidad indivisible. Debe convertir el
analizador local en un kit de diagnóstico multiplataforma, ejecutar rutas compatibles,
conservar fallos y recuperación, actualizar fuentes y publicar la parte completa en un
solo commit después de los gates.

## Métricas antes y después del incremento

| Métrica | 2026-10-04 | 2026-10-06 |
| --- | ---: | ---: |
| clases desarrolladas | 12 | 24 |
| borradores publicados | 348 | 336 |
| estructuras curriculares | 120 | 120 |
| laboratorios ejecutables versionados | 0 | 1 |
| pruebas del laboratorio de Parte 01 | 0 | 6 |
| clases totales | 480 | 480 |
| páginas HTML | 521 | 521 |

Los conteos no sustituyen la revisión cualitativa. El cambio conserva las 480 clases,
la navegación y el historial; profundiza una parte completa y deja explícito lo que no
se midió.

## Fuentes primarias reconsultadas

- [RISC-V Ratified Specifications Library](https://docs.riscv.org/), consultada el 2026-10-06.
- [The Unicode Standard 18.0](https://www.unicode.org/versions/Unicode18.0.0/), consultada el 2026-10-06.
- [Python 3 documentation](https://docs.python.org/3/), consultada el 2026-10-06.
- [Java Virtual Machine Specification SE 27](https://docs.oracle.com/javase/specs/jvms/se27/html/), consultada el 2026-10-06.
- [Software Carbon Intensity](https://greensoftware.foundation/standards/sci/), consultada el 2026-10-06.

No se afirma acceso al texto completo de normas de pago ni ejecución en hardware no
disponible. Los resultados de CI y Pages se documentan después de la publicación.
