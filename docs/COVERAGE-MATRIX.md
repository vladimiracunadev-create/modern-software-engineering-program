# Matriz de cobertura del programa

Esta matriz demuestra qué parte del programa es propietaria de cada área. El detalle
clase por clase vive en `curriculum.yaml`; esta vista evita confundir cobertura con
una lista de herramientas.

La presencia en esta matriz expresa **propiedad curricular**, no contenido terminado.
Consulta la [auditoría de cobertura y profundidad](PROGRAM-COVERAGE-AUDIT-2026-10-06.md)
para distinguir contenido desarrollado, borradores y estructura pendiente. Estado actual: las 51 partes están desarrolladas (`SE-001`–`SE-612`), a falta de revisión
editorial humana independiente; las Partes 34 y 42 se reservaron por ADR-007 y ya tienen contenido. Los números de parte de las tablas siguientes usan la
secuencia pedagógica vigente; el mapa con la numeración anterior está en
[`ID-MIGRATION.md`](ID-MIGRATION.md).

## Cuerpo profesional estable

| Área | Partes principales | Evidencia esperada |
| --- | --- | --- |
| Fundamentos profesionales | 00–04 | análisis, modelos y entorno reproducible |
| Construcción de software | 05–09 | programas, pruebas, paquetes y automatización |
| Producto y requisitos | 10–13 | brief, métricas, SRS, SPEC y contratos |
| UX y accesibilidad | 14 | prototipo y evaluación |
| Proceso y colaboración | 15–17 | plan, cambio revisable y documentación |
| Superficies de ejecución | 18–22, 24 | fragmentos verticales por plataforma |
| Diseño y arquitectura | 25, 27 | refactorización, ADR y vistas |
| Datos e integración | 29, 31–33 | modelo, migración, eventos y despliegue |
| Pruebas y calidad | 35–36 | estrategia que detecta defectos y mediciones |
| Seguridad y privacidad | 38 | amenazas, controles y pruebas negativas |
| Entrega y supply chain | 39–40 | artefacto, procedencia, pipeline y rollback |
| Operación y SRE | 41 | SLO, telemetría, incidente y recuperación |
| Mantenimiento y legacy | 43 | migración incremental reversible |
| Gestión y liderazgo | 44 | decisión, riesgo, economía y defensa |
| IA, SPEC y agentes | 46–47 | evals, autoridad, trazabilidad y producto final |
| Runtimes y plataformas modernas | 23 | aislamiento, medición y modelo de amenaza |
| Patrones de diseño y estilos arquitectónicos | 26, 28 | catálogo con su costo y decisión defendida con ADR |
| Ingeniería de datos y ML en producción | 30, 50 | plataforma de datos gobernada y sistema de ML operable |
| Sistemas críticos y normas de seguridad | 37 | paquete de aseguramiento de un controlador |
| Producto SaaS | 34 | núcleo SaaS multi-tenant con facturación por uso |
| Ingeniería del caos | 42 | programa de caos de un servicio con evidencia |
| Metodologías, harness y patrones agénticos | 45, 48–49 | política metodológica, harness gobernado y sistema con LLM evaluado |

## Brechas explícitas bajo investigación

| Brecha | Ubicación que debe intentarse primero | Condición para crear otra clase |
| --- | --- | --- |
| métodos formales y assurance | 13, 22, 24 | laboratorio y competencia no caben en `SE-159`–`SE-161` o `SE-274` |
| API en tiempo real y deprecación | 13, 20, 31 | el ciclo contractual queda fragmentado o sobrecarga esas clases |
| estimación probabilística | 11, 15, 44 | necesita evidencia distinta de planificación y economía existentes |
| InnerSource, OSPO y sociotécnica | 16, 27, 44 | gobernanza y diseño organizacional requieren artefactos independientes |
| DevEx y SPACE | 40, 44 | no pueden evaluarse responsablemente dentro de plataforma y liderazgo |
| green software medible | 00, 11, 22, 33, 36 | SCI y GreenOps requieren una secuencia práctica propia |
| compliance engineering | 12, 38 | la cadena requisito → control → evidencia no cabe en el proyecto vigente |
| carrera Staff/Principal/Manager | 44 | las rutas no se pueden construir reutilizando clases actuales |

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
| Autocompletado, chat, edición y generación | SE-553–SE-556 |
| Pruebas, documentación, migración y refactorización | SE-557–SE-559 |
| Context engineering | SE-560 |
| Evals, seguridad y propiedad intelectual | SE-561–SE-562 |
| Comparación manual/asistido/automatizado | SE-563 |
| Cambio trazable con revisión humana | SE-564 |
| SPEC durable y flujo specification-to-code | SE-565–SE-567 |
| Greenfield, brownfield, bugs e ideas | SE-568 |
| Agentes, herramientas, permisos y skills | SE-569–SE-570 |
| MCP y confianza | SE-571 |
| Delegación y multiagente | SE-572 |
| Human-in-the-loop y reversibilidad | SE-573 |
| Seguridad agentic y prompt injection | SE-574 |
| Detención, recuperación y evaluación | SE-575 |
| Producto final construido desde SPEC | SE-576 |

## Regla de actualización

El cuerpo estable se revisa contra estándares y literatura. La capa de frontera se
revisa con fuentes oficiales fechadas. Una herramienta nueva entra primero como caso
comparativo; solo se promueve al núcleo cuando agrega una competencia transferible.
