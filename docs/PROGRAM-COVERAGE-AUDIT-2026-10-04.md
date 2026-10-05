# Auditoría de cobertura y madurez — 2026-10-04

## Alcance y método

Esta auditoría compara el mandato curricular vigente con `curriculum.yaml`, las 480
carpetas de clase, los registros de fuentes, los validadores, el portal y el estándar
pedagógico. El estado describe **contenido enseñable**, no la mera presencia de un
título. Por eso una competencia puede estar bien ubicada en el mapa y seguir
`SUPERFICIAL` o `AUSENTE` mientras solo exista un borrador o scaffold.

Línea base reproducible:

- 40 partes y 480 IDs consecutivos (`SE-001`–`SE-480`);
- 12 clases `GUIDED`, 468 `PLANNED`;
- `SE-013`–`SE-360`: borradores públicos no aprobados;
- `SE-361`–`SE-480`: scaffolds planificados;
- 521 páginas HTML generadas;
- cuatro archivos de pruebas estructurales y dos workflows.

## Matriz de diagnóstico

| Área | Estado | Archivos existentes | Profundidad | Brechas | Acción |
| --- | --- | --- | --- | --- | --- |
| Fundamentos, profesión y ética | PARCIAL | Partes 00–04; `content/part-00`; línea base 00–01 | Parte 00 profunda; resto no aprobado | completar abstracción, sistemas y práctica sobre infraestructura sin perder la mirada sociotécnica | construir partes 01–04 una por una y conservar el caso conductor |
| Construcción, paradigmas y depuración | SUPERFICIAL | Partes 05–09 y repositorio `polyglot-programming-labs` | borradores de fase 3 | faltan mecanismos desarrollados, fallos reproducibles y límites por paradigma | integrar aquí decisiones de ingeniería y delegar sintaxis/lenguajes al propietario especializado |
| Requisitos y discovery | SUPERFICIAL | Partes 10, 12 y 13; `sources/phase3.json` | títulos y borradores, sin aprobación | profundizar observación, workshops, prototipos, conflictos, ambigüedad, NFR y cambio | construir con trazabilidad necesidad → requisito → prueba → evidencia |
| Economía, estimación y experimentación | SUPERFICIAL | Partes 11 y 15; `SE-134`, `SE-138`, `SE-140`, `SE-185` | cobertura nominal | Monte Carlo, Function Points y COCOMO II no son explícitos; falta separar pronóstico de compromiso | profundizar primero `SE-185`, `SE-191` y el proyecto económico; dividir solo si el artefacto exige otra clase |
| Diseño, patrones y refactorización | SUPERFICIAL | Parte 24 | borrador no aprobado | GRASP, antipatterns y criterios de no refactorizar requieren desarrollo | convertir trade-offs y refactorización segura en evidencia ejecutable |
| Arquitectura y sistemas sociotécnicos | SUPERFICIAL | Partes 25, 29 y `SE-310` | borradores | explicitar SOA, cloud-native, Team Topologies, Conway e inverse Conway sin hacer catálogo | usar CONTEXTO → PROBLEMA → SOLUCIÓN → COSTE → FALLOS → OPERACIÓN → EVOLUCIÓN |
| API engineering | SUPERFICIAL | `SE-163`, Parte 20 y `SE-331` | contratos y protocolos anunciados | gRPC, WebSockets, SSE, gateways y deprecación no están explícitos como recorrido completo | reconciliar `SE-163`, `SE-243`, `SE-248` y `SE-331`; añadir solo la brecha que no quepa |
| Sistemas distribuidos | SUPERFICIAL | Partes 27–28 | buenos títulos, contenido no aprobado | PACELC y service discovery no son explícitos; faltan experimentos completos de fallos | construir laboratorios de reloj, partición, duplicación, consenso y degradación |
| Software intensivo en datos | SUPERFICIAL | Partes 26–27 y repositorio `database-systems-labs` | borradores | OLTP/OLAP, data contracts y calidad de datos necesitan trazabilidad transversal | enseñar decisiones y contratos aquí; motores y consultas profundas en el repositorio propietario |
| Testing y calidad | AUSENTE | Partes 30–31; `ISO-25010-2023` en fuentes | scaffolds | snapshot, accesibilidad, seguridad y qué no probar deben integrarse; no hay clases enseñables | desarrollar estrategia por riesgo antes de técnicas y exigir defectos detectados |
| Rendimiento y resiliencia | AUSENTE | Parte 31 y continuidad en 35 | scaffolds | capacity planning, percentiles, RTO/RPO y game days requieren ejercicios verificables | producir benchmarks, pruebas de presión y recuperación con límites medidos |
| DevOps, Platform Engineering y DevEx | AUSENTE | Partes 33–34; `SE-417`, `SE-418` | scaffolds | platform-as-product, Backstage como caso y SPACE no están explícitos | construir golden path, self-service y métricas con guardrails contra gaming |
| SRE, observabilidad e incidentes | AUSENTE | Parte 35 | scaffolds | falta practicar la variedad de fallos y el ciclo detectar → aprender | usar OpenTelemetry y Google SRE como fuentes; ejecutar incidentes controlados, no inventar resultados |
| Seguridad, privacidad y compliance | AUSENTE | Parte 32 y NIST/OWASP en fuentes | scaffolds | falta desarrollar la cadena regulación → requisito → control → prueba → evidencia → auditoría | construir threat model, pruebas negativas y paquete de evidencia; declarar jurisdicción y límites |
| Supply chain | AUSENTE | Parte 33; `SE-400`, `SE-406` | scaffolds | SLSA, OpenSSF, typosquatting y dependency confusion requieren fuentes y práctica explícitas | verificar procedencia, firma, SBOM y política de consumo con artefactos reales |
| Git y colaboración | SUPERFICIAL | Parte 16 y reglas transversales | borrador | GitHub Projects, Dependabot, Packages, releases y mantenimiento comunitario requieren integración | mantener Git transversal y evitar una clase por función de interfaz |
| Legacy, evolución y retiro | AUSENTE | Parte 36 | scaffolds | rehost/replatform/refactor/rearchitect/rewrite, EOL y borrado seguro necesitan decisión comparativa | construir un proyecto brownfield reversible con characterization tests y plan de retiro |
| Open Source, InnerSource y organizaciones | SUPERFICIAL | `SE-199`–`SE-202`, `SE-310`, Parte 37 | títulos parciales | OSPO, InnerSource, sostenibilidad, bus factor y topologías de equipo no están desarrollados | integrar gobernanza y ownership; separar solo competencias con artefacto propio |
| Carrera y liderazgo | AUSENTE | Parte 37; línea base 16 | scaffolds | rutas Staff/Principal/Architect/Manager/Platform/SRE/Security/QA no están demostradas | reutilizar clases por rutas y evaluar decisiones, mentoría, incidentes y defensa |
| Métodos formales y sistemas críticos | SUPERFICIAL | `SE-157`–`SE-161`, `SE-274`, `SE-283` | introducción planificada | TLA+, Alloy, hazard analysis y límites de assurance no son explícitos | profundizar invariantes y model checking; proponer expansión solo si el laboratorio no cabe |
| Embedded, IoT y edge | SUPERFICIAL | Parte 22 | borrador | faltan prácticas verificadas de RTOS, OTA y device security | usar simulación honesta y declarar ausencia de hardware cuando corresponda |
| Green software | PARCIAL | `SE-009`, `SE-134`, `SE-267`, `SE-356`; fuente GSF-SCI | sostenibilidad guiada en Parte 00, implementación pendiente | carbon awareness, SCI y GreenOps no forman aún un recorrido medible | integrar medición y efectos rebote; no afirmar reducción sin datos |
| Accesibilidad e internacionalización | SUPERFICIAL | Parte 14; WCAG 2.2 y Unicode en fuentes | borrador no aprobado | RTL, pluralización y pruebas con tecnologías de asistencia deben quedar explícitos | construir flujo accesible y localizado con verificación por teclado, zoom y lector cuando sea posible |
| IA aplicada y agentes | AUSENTE | Partes 38–39 | scaffolds | hallucinated APIs, loops, coste, provenance y regresiones están anunciados pero no enseñados | aplicar HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS VERIFICAN → HUMANO REVISA → SISTEMA VALIDA |
| Casos reales, laboratorios y evaluación | PARCIAL | `activity.yaml`, `rubric.json`, proyectos y Parte 00 | estructura amplia; evidencia real escasa fuera de Parte 00 | separar hechos/interpretación/lecciones y ejecutar laboratorios antes de declarar resultados | incorporar casos documentados y artefactos reales durante la construcción de cada parte |
| Fuentes, glosario, rutas y portal | PARCIAL | `sources/`, `classes/README.md`, `site/`, `docs/SOURCES.md` | navegación y registro existen | bibliografía temática, glosario relacional y rutas profesionales detalladas están incompletos | actualizar junto a cada parte y publicar el contenido íntegro, no una ficha |

## Brechas que podrían justificar expansión

No se crean clases en esta auditoría. El siguiente backlog solo habilita investigación:

1. métodos formales aplicados y assurance de sistemas críticos;
2. green software medible y GreenOps;
3. InnerSource, OSPO y sostenibilidad de comunidades;
4. DevEx y SPACE junto a platform-as-product;
5. API en tiempo real, gateways y deprecación;
6. estimación probabilística y economía de decisiones;
7. compliance engineering basado en evidencia;
8. rutas Staff/Principal/Architect/Engineering Manager;
9. seguridad de cadena de suministro alineada con SLSA y OpenSSF;
10. retirada, retención y borrado seguro de sistemas y datos.

Cada candidato debe demostrar primero que no puede profundizarse coherentemente en
una clase existente. El gate completo está en
[`ADR-003`](adr/ADR-003-reconcile-480-baseline-with-progressive-expansion.md).

## Orden de implementación

1. **Gobernanza:** prompt, auditoría, ADR, validadores y roadmap (este incremento).
2. **Fase 3:** construir `SE-013`–`SE-180` parte por parte; una parte por commit.
3. **Fase 4:** reconstruir cualitativamente `SE-181`–`SE-360` con el mismo gate.
4. **Fases 5–6:** desarrollar `SE-361`–`SE-480`, hoy scaffolds.
5. **Decisión de expansión:** repetir la matriz, medir brechas residuales y recién
   entonces diseñar IDs posteriores a `SE-480`.

## Fuentes primarias contrastadas para esta auditoría

- [SWEBOK Guide V4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering/v4), consultada el 2026-10-04.
- [ISO/IEC/IEEE 12207:2026](https://www.iso.org/standard/90219.html), consultada el 2026-10-04.
- [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html), consultada el 2026-10-04.
- [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html), consultada el 2026-10-04.
- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html), consultada el 2026-10-04.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/), consultada el 2026-10-04.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), consultada el 2026-10-04.
- [SLSA v1.2](https://slsa.dev/spec/v1.2/), consultada el 2026-10-04.
- [DORA software delivery performance metrics](https://dora.dev/guides/dora-metrics/), consultada el 2026-10-04.
- [OpenTelemetry](https://opentelemetry.io/docs/), consultada el 2026-10-04.
- [Software Carbon Intensity](https://sci.greensoftware.foundation/), consultada el 2026-10-04.

No se afirma acceso al texto completo de normas de pago; se usaron sus fichas públicas
y alcance oficial. La auditoría no demuestra que los laboratorios pendientes funcionen.
