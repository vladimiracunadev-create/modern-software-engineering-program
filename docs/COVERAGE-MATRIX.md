# Matriz de cobertura del programa

Esta matriz demuestra qué parte del programa es propietaria de cada área. El detalle
clase por clase vive en `curriculum.yaml`; esta vista evita confundir cobertura con
una lista de herramientas.

## Cuerpo profesional estable

| Área | Partes principales | Evidencia esperada |
| --- | --- | --- |
| Fundamentos profesionales | 00–04 | análisis, modelos y entorno reproducible |
| Construcción de software | 05–09 | programas, pruebas, paquetes y automatización |
| Producto y requisitos | 10–13 | brief, métricas, SRS, SPEC y contratos |
| UX y accesibilidad | 14 | prototipo y evaluación |
| Proceso y colaboración | 15–17 | plan, cambio revisable y documentación |
| Superficies de ejecución | 18–23 | fragmentos verticales por plataforma |
| Diseño y arquitectura | 24–25 | refactorización, ADR y vistas |
| Datos e integración | 26–29 | modelo, migración, eventos y despliegue |
| Pruebas y calidad | 30–31 | estrategia que detecta defectos y mediciones |
| Seguridad y privacidad | 32 | amenazas, controles y pruebas negativas |
| Entrega y supply chain | 33–34 | artefacto, procedencia, pipeline y rollback |
| Operación y SRE | 35 | SLO, telemetría, incidente y recuperación |
| Mantenimiento y legacy | 36 | migración incremental reversible |
| Gestión y liderazgo | 37 | decisión, riesgo, economía y defensa |
| IA, SPEC y agentes | 38–39 | evals, autoridad, trazabilidad y producto final |

## Formas de producir software

La cobertura incluye desarrollo manual, asistido y automatizado; greenfield y
brownfield; producto, plataforma, librería, SDK, CLI, web, backend, móvil,
escritorio, embedded, IoT, datos, ML, juegos, sistemas regulados, blockchain,
low-code y automatización visual.

No todas las tecnologías reciben la misma profundidad. El programa enseña el modelo
de decisión y utiliza implementaciones representativas. Los catálogos especializados
mantienen la profundidad de lenguajes, motores y frameworks.

## IA y desarrollo basado en especificaciones

| Capacidad | Clases |
| --- | --- |
| Autocompletado, chat, edición y generación | SE-457–SE-460 |
| Pruebas, documentación, migración y refactorización | SE-461–SE-463 |
| Context engineering | SE-464 |
| Evals, seguridad y propiedad intelectual | SE-465–SE-466 |
| Comparación manual/asistido/automatizado | SE-467 |
| Cambio trazable con revisión humana | SE-468 |
| SPEC durable y flujo specification-to-code | SE-469–SE-471 |
| Greenfield, brownfield, bugs e ideas | SE-472 |
| Agentes, herramientas, permisos y skills | SE-473–SE-474 |
| MCP y confianza | SE-475 |
| Delegación y multiagente | SE-476 |
| Human-in-the-loop y reversibilidad | SE-477 |
| Seguridad agentic y prompt injection | SE-478 |
| Detención, recuperación y evaluación | SE-479 |
| Producto final construido desde SPEC | SE-480 |

## Regla de actualización

El cuerpo estable se revisa contra estándares y literatura. La capa de frontera se
revisa con fuentes oficiales fechadas. Una herramienta nueva entra primero como caso
comparativo; solo se promueve al núcleo cuando agrega una competencia transferible.
