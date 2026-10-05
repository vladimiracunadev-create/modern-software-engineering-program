# 🧭 Programa de Ingeniería de Software Moderna

## 480 clases · 40 partes (00–39) · del fundamento al diseño, la operación, el liderazgo y la IA

Currículo abierto en español para aprender a comprender, especificar, construir,
probar, entregar, operar, modernizar y retirar software profesional. Conecta
computación, producto, arquitectura, datos, calidad, seguridad, DevOps, SRE,
liderazgo y desarrollo asistido por agentes.

[📚 Índice completo de clases](classes/README.md) · [🧭 Rutas por rol](roles/README.md) · [🧪 Producto transversal](blueprints/reference-product/README.md) · [🌐 Aplicación web](https://vladimiracunadev-create.github.io/modern-software-engineering-program/) · [📐 Estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md) · [🗺️ Roadmap](ROADMAP.md) · [🤝 Contribuir](CONTRIBUTING.md)

---

[![Validate](https://github.com/vladimiracunadev-create/modern-software-engineering-program/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/modern-software-engineering-program/actions/workflows/validate.yml)
[![Pages](https://github.com/vladimiracunadev-create/modern-software-engineering-program/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/modern-software-engineering-program/actions/workflows/pages.yml)
[![Currículo](https://img.shields.io/badge/currículo-480%20clases-7c5cff?style=flat-square)](curriculum.yaml)
[![Partes](https://img.shields.io/badge/partes-40-2ea043?style=flat-square)](#-las-40-partes-numeradas-de-00-a-39)
[![Sitio](https://img.shields.io/badge/sitio-521%20páginas-ff8c42?style=flat-square)](https://vladimiracunadev-create.github.io/modern-software-engineering-program/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=flat-square)](docs/PROGRAM-ARCHITECTURE.md)
[![Licencia](https://img.shields.io/badge/licencia-MIT-3fb950?style=flat-square)](LICENSE)

> [!IMPORTANT]
> **Cobertura real, sin inflar cifras:** la arquitectura contiene 480 clases. La
> Parte 00 (`SE-001`–`SE-012`) tiene contenido desarrollado; las partes 01–29
> (`SE-013`–`SE-360`) conservan material de trabajo que requiere revisión cualitativa,
> y las partes 30–39 (`SE-361`–`SE-480`) todavía deben desarrollar su enseñanza
> completa. Una carpeta o página generada no cuenta como aprendizaje terminado.

## 🎯 Qué es esto

Un programa modular y secuencial que recorre el ciclo de vida completo de un sistema:

**FUNDAMENTOS → COMPRENSIÓN → PRÁCTICA → CONSTRUCCIÓN → INTEGRACIÓN → PRODUCCIÓN →
OPERACIÓN → SISTEMAS COMPLEJOS → ARQUITECTURA → LIDERAZGO → EVOLUCIÓN → RETIRO**.

Cada clase se diseña para integrar, cuando corresponde:

- 🎯 objetivo, límites y resultados de aprendizaje observables;
- 🗺️ temas con la razón profesional por la que importan;
- 📖 principios, mecanismos, causas, consecuencias y trade-offs;
- 🧠 definiciones en contexto, ejemplos y contraejemplos;
- 🧩 diagramas interpretados, no imágenes ornamentales;
- 🛠️ herramientas, versiones, entorno, preparación y limpieza;
- 🧪 práctica reproducible con evidencia observable;
- ✍️ ejercicios graduados y reto con criterio de aceptación;
- ⚠️ fallos expresados como síntoma → hipótesis → causa → solución;
- 🔭 observabilidad, mantenimiento, evolución y límites;
- 🔗 fuentes primarias u oficiales vinculadas a lo que sustentan.

El contrato completo está en el
[estándar pedagógico permanente](docs/PEDAGOGICAL-STANDARD.md). Una plantilla completa
no compensa contenido superficial y un agente que termina no demuestra que el software
funcione.

## 📚 Pauta profesional y cuerpos de conocimiento

El programa no depende de una herramienta, proveedor o autor. La cobertura se
contrasta con fuentes que representan distintas dimensiones de la disciplina:

| Área | Referencia de orientación | Uso en el programa |
| --- | --- | --- |
| profesión | [SWEBOK v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | áreas de conocimiento, prácticas y límites |
| educación | [ACM/IEEE SE2014](https://www.acm.org/binaries/content/assets/education/se2014.pdf) | competencias y progresión curricular |
| ciclo de vida | [ISO/IEC/IEEE 12207](https://www.iso.org/standard/63712.html) | procesos de software y relaciones durante su vida útil |
| requisitos | [ISO/IEC/IEEE 29148](https://www.iso.org/standard/72089.html) | calidad, trazabilidad y validación de requisitos |
| calidad | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | atributos y escenarios de calidad |
| seguridad | [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | desarrollo seguro integrado al ciclo |
| accesibilidad | [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) | experiencia inclusiva y verificable |
| APIs | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) y [OpenAPI](https://spec.openapis.org/oas/latest.html) | semántica y contratos interoperables |
| confiabilidad | [Google SRE](https://sre.google/books/) | SLO, error budgets, toil e incidentes |
| supply chain | [SLSA](https://slsa.dev/) y [OpenSSF](https://openssf.org/) | procedencia, artefactos y consumo seguro |
| IA responsable | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | riesgo, evaluación y supervisión humana |
| agentes | [Model Context Protocol](https://modelcontextprotocol.io/) | herramientas, contexto, autorización y límites |

> Las referencias orientan y respaldan; no se reproduce el texto protegido de los
> estándares. El material del programa tiene redacción propia.

## 📖 De dónde sale el material

Las fuentes se conservan como datos auditables, no como bibliografía decorativa:

- [línea base de fuentes](sources/baseline.json): estándares, especificaciones y documentación oficial;
- [registro por clase](sources/class-sources.json): fuentes asignadas a `SE-001`–`SE-480`;
- [fuentes de fase 3](sources/phase3.json) y [fase 4](sources/phase4.json): cobertura por parte;
- [trazabilidad pedagógica](sources/pedagogical/): afirmación, evidencia, error conceptual y límite;
- [política de fuentes](docs/SOURCES.md): autoridad, vigencia y tratamiento de material obsoleto.

Una fuente asignada no demuestra que cada afirmación esté sustentada ni que una
práctica se haya ejecutado. Esa revisión ocurre clase por clase y se documenta en las
[auditorías de contenido](docs/PHASE3-CONTENT-AUDIT.md).

## 🔗 Ecosistema y fronteras entre programas

Este repositorio integra producto y ciclo de vida completo. Reutiliza repositorios
especializados cuando el aprendizaje exige profundidad propia de lenguajes, motores de
datos o frameworks, sin copiar masivamente su contenido:

| Repositorio | Responsabilidad | Unidad de transferencia |
| --- | --- | --- |
| `polyglot-programming-labs` | lenguajes, algoritmos y paradigmas | comportamiento y pruebas comunes |
| `database-systems-labs` | datos, motores y recuperación | dominio, carga y garantías |
| `framework-ecosystems-labs` | interfaces, frameworks y plataformas | contrato y atributos equivalentes |
| `modern-software-engineering-program` | producto y ciclo de vida completo | resultado operable y defendible |

Las reglas de propiedad, integración y antiduplicación están en
[fronteras entre repositorios](docs/REPOSITORY-BOUNDARIES.md) y en el
[contrato de integración](docs/INTEGRATION-CONTRACT.md).

## 🗂️ Las 40 partes, numeradas de 00 a 39

Cada parte contiene doce clases: diez clases nucleares, un taller y un proyecto. Su
README enlaza el recorrido y el [roadmap](ROADMAP.md) explica qué contenido, artefacto
y comprobación debe incorporar.

> La Parte 00 es la primera unidad; por eso la cuadragésima y última se identifica como
> Parte 39. «40 partes» expresa la cantidad, no una carpeta `part-40`.

| # | Parte | Clases | Foco | README |
| ---: | --- | --- | --- | --- |
| 00 | Ingeniería de software como profesión | SE-001–SE-012 | disciplina, ética, evidencia y calidad | [📘 leer](classes/part-00-ingenieria-de-software-como-profesion/README.md) |
| 01 | Computadores y representación de información | SE-013–SE-024 | máquina, datos, memoria y runtimes | [📘 leer](classes/part-01-computadores-y-representacion-de-informacion/README.md) |
| 02 | Sistemas operativos, terminal y automatización base | SE-025–SE-036 | Windows, Linux, macOS, shells y diagnóstico | [📘 leer](classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| 03 | Redes, Internet y protocolos | SE-037–SE-048 | TCP/IP, DNS, HTTP, TLS y observación | [📘 leer](classes/part-03-redes-internet-y-protocolos/README.md) |
| 04 | Pensamiento computacional y resolución de problemas | SE-049–SE-060 | lógica, modelos, complejidad y estrategias | [📘 leer](classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) |
| 05 | Fundamentos de programación | SE-061–SE-072 | control, funciones, datos, errores y pruebas | [📘 leer](classes/part-05-fundamentos-de-programacion/README.md) |
| 06 | Paradigmas de programación | SE-073–SE-084 | imperativo, objetos, funcional, lógico y reactivo | [📘 leer](classes/part-06-paradigmas-de-programacion/README.md) |
| 07 | Estructuras de datos y algoritmos | SE-085–SE-096 | colecciones, grafos, diseño y medición | [📘 leer](classes/part-07-estructuras-de-datos-y-algoritmos/README.md) |
| 08 | Entornos, herramientas y depuración | SE-097–SE-108 | IDE, depuración, profiling y reproducibilidad | [📘 leer](classes/part-08-entornos-herramientas-y-depuracion/README.md) |
| 09 | Bibliotecas, paquetes, SDK y automatización | SE-109–SE-120 | dependencias, SemVer, CLI, plugins y DevEx | [📘 leer](classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) |
| 10 | Descubrimiento y estrategia de producto | SE-121–SE-132 | problema, usuarios, outcomes y experimentación | [📘 leer](classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) |
| 11 | Economía, métricas y decisiones de producto | SE-133–SE-144 | valor, TCO, costes y priorización | [📘 leer](classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) |
| 12 | Ingeniería de requisitos | SE-145–SE-156 | elicitación, calidad, trazabilidad y cambio | [📘 leer](classes/part-12-ingenieria-de-requisitos/README.md) |
| 13 | Especificaciones, contratos y modelos | SE-157–SE-168 | SPEC, invariantes, estados, APIs y aceptación | [📘 leer](classes/part-13-especificaciones-contratos-y-modelos/README.md) |
| 14 | Experiencia, accesibilidad e internacionalización | SE-169–SE-180 | UX, inclusión, contenido e i18n | [📘 leer](classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md) |
| 15 | Procesos, planificación y estimación | SE-181–SE-192 | flujo, incertidumbre y forecasting | [📘 leer](classes/part-15-procesos-planificacion-y-estimacion/README.md) |
| 16 | Git, colaboración y código abierto | SE-193–SE-204 | historial, revisión, releases y gobernanza | [📘 leer](classes/part-16-git-colaboracion-y-codigo-abierto/README.md) |
| 17 | Documentación y conocimiento técnico | SE-205–SE-216 | docs-as-code, ADR, RFC y runbooks | [📘 leer](classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| 18 | CLI, TUI, servicios y automatización | SE-217–SE-228 | interfaces textuales, jobs y procesos | [📘 leer](classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| 19 | Web, frontend y aplicaciones progresivas | SE-229–SE-240 | navegador, UI, estado y PWA | [📘 leer](classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md) |
| 20 | Backend, APIs y procesamiento asíncrono | SE-241–SE-252 | servicios, contratos, workers y tiempo real | [📘 leer](classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| 21 | Software móvil, escritorio y multiplataforma | SE-253–SE-264 | plataformas, distribución y ciclo de vida | [📘 leer](classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) |
| 22 | Embedded, IoT y tiempo real | SE-265–SE-276 | firmware, hardware, OTA y temporización | [📘 leer](classes/part-22-embedded-iot-y-tiempo-real/README.md) |
| 23 | Software especializado y dominios | SE-277–SE-288 | ciencia, industria, regulación y safety | [📘 leer](classes/part-23-software-especializado-y-dominios/README.md) |
| 24 | Diseño, patrones y refactorización | SE-289–SE-300 | modularidad, patrones y deuda | [📘 leer](classes/part-24-diseno-patrones-y-refactorizacion/README.md) |
| 25 | Arquitectura de software y dominio | SE-301–SE-312 | límites, estilos, DDD y evolución | [📘 leer](classes/part-25-arquitectura-de-software-y-dominio/README.md) |
| 26 | Datos, persistencia y recuperación | SE-313–SE-324 | modelos, transacciones, índices y backup | [📘 leer](classes/part-26-datos-persistencia-y-recuperacion/README.md) |
| 27 | Integración, eventos y mensajería | SE-325–SE-336 | colas, streams, sagas y compatibilidad | [📘 leer](classes/part-27-integracion-eventos-y-mensajeria/README.md) |
| 28 | Concurrencia y sistemas distribuidos | SE-337–SE-348 | coordinación, fallos, consistencia y consenso | [📘 leer](classes/part-28-concurrencia-y-sistemas-distribuidos/README.md) |
| 29 | Cloud, plataforma e infraestructura | SE-349–SE-360 | nube, contenedores, IaC y costes | [📘 leer](classes/part-29-cloud-plataforma-e-infraestructura/README.md) |
| 30 | Estrategia y técnicas de prueba | SE-361–SE-372 | niveles, propiedades, contratos y E2E | [📘 leer](classes/part-30-estrategia-y-tecnicas-de-prueba/README.md) |
| 31 | Calidad, rendimiento y resiliencia | SE-373–SE-384 | atributos, carga, degradación y recuperación | [📘 leer](classes/part-31-calidad-rendimiento-y-resiliencia/README.md) |
| 32 | Seguridad, privacidad y cumplimiento | SE-385–SE-396 | amenazas, controles, privacidad y evidencia | [📘 leer](classes/part-32-seguridad-privacidad-y-cumplimiento/README.md) |
| 33 | Build, release y cadena de suministro | SE-397–SE-408 | artefactos, SBOM, firma y procedencia | [📘 leer](classes/part-33-build-release-y-cadena-de-suministro/README.md) |
| 34 | CI/CD, IaC y platform engineering | SE-409–SE-420 | pipelines, despliegue y autoservicio | [📘 leer](classes/part-34-ci-cd-iac-y-platform-engineering/README.md) |
| 35 | Observabilidad, SRE e incidentes | SE-421–SE-432 | señales, SLO, guardias y aprendizaje | [📘 leer](classes/part-35-observabilidad-sre-e-incidentes/README.md) |
| 36 | Mantenimiento y modernización legacy | SE-433–SE-444 | arqueología, migración, EOL y retiro | [📘 leer](classes/part-36-mantenimiento-y-modernizacion-legacy/README.md) |
| 37 | Gestión, liderazgo y práctica profesional | SE-445–SE-456 | equipos, comunicación y decisiones | [📘 leer](classes/part-37-gestion-liderazgo-y-practica-profesional/README.md) |
| 38 | Desarrollo de software asistido por IA | SE-457–SE-468 | copilots, contexto, evals y seguridad | [📘 leer](classes/part-38-desarrollo-de-software-asistido-por-ia/README.md) |
| 39 | SPEC, agentes y ciclo de vida agentic | SE-469–SE-480 | MCP, agentes, delegación y control | [📘 leer](classes/part-39-spec-agentes-y-ciclo-de-vida-agentic/README.md) |

➡️ [Abrir el índice plano con enlaces directos a las 480 clases](classes/README.md).

## 🧪 Práctica y producto transversal

El programa mantiene un producto documental de referencia para conectar decisiones que
normalmente se enseñan por separado:

| Artefacto | Qué permite revisar |
| --- | --- |
| [Brief de producto](blueprints/reference-product/PRODUCT_BRIEF.md) | problema, usuarios, alcance y valor |
| [Requisitos](blueprints/reference-product/REQUIREMENTS.md) | reglas, restricciones y trazabilidad |
| [Arquitectura](blueprints/reference-product/ARCHITECTURE.md) | límites, componentes y decisiones |
| [ADR](blueprints/reference-product/adr/ADR-001-modular-monolith.md) | contexto, alternativas y trade-offs |
| [Contrato OpenAPI](blueprints/reference-product/api/openapi.yaml) | interfaz formal, errores e idempotencia |
| [Estrategia de pruebas](blueprints/reference-product/TEST_STRATEGY.md) | riesgos, niveles y evidencia esperada |
| [Modelo de amenazas](blueprints/reference-product/THREAT_MODEL.md) | activos, amenazas y controles |
| [Runbook](blueprints/reference-product/runbooks/API_DEGRADED.md) | diagnóstico y recuperación operacional |
| [Proyecto integrador](projects/capstone.md) | transferencia a un producto completo |
| [Rúbrica](assessments/rubric.md) | explicación, implementación, prueba y operación |

Estos artefactos son una base versionada; no se presentan como laboratorios ejecutados.
El [roadmap](ROADMAP.md#proyectos-integradores) incorpora además proyectos de sistema
distribuido, modernización legacy, análisis económico e IA controlada.

## 🌐 Portal y navegación

El [sitio del programa](https://vladimiracunadev-create.github.io/modern-software-engineering-program/)
publica 521 páginas: portada, 40 partes y 480 clases. Permite buscar por ID o título,
filtrar por etapa y recorrer anterior / parte / índice / siguiente.

- 📚 [Abrir el portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/).
- 🗂️ [Usar el índice completo en GitHub](classes/README.md).
- 🧭 [Elegir una ruta profesional](roles/README.md).
- 📊 [Consultar la cobertura verificable](STATUS.md).

La fuente de verdad sigue siendo el repositorio. El portal se genera desde los
manifiestos y la CI falla cuando el sitio queda desincronizado. La identidad pública,
el About, los topics, los gates y la URL canónica están documentados en el
[plan de publicación](docs/PUBLICATION-PLAN.md).

## 👩‍🏫 Para instructores y revisores

- 📐 [Estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md) — profundidad mínima y revisión cualitativa.
- 🧠 [Modelo de aprendizaje](docs/LEARNING-MODEL.md) — contexto, práctica, fallo, transferencia e integración.
- 🧭 [Arquitectura del programa](docs/PROGRAM-ARCHITECTURE.md) — etapas, partes y dependencias.
- 🗺️ [Matriz de cobertura](docs/COVERAGE-MATRIX.md) — propiedad curricular por área.
- 🔎 [Auditoría de cobertura](docs/PROGRAM-COVERAGE-AUDIT-2026-10-04.md) — brechas y acciones.
- 📊 [Rúbrica transversal](assessments/rubric.md) — evaluación de decisiones y evidencia.
- 🤝 [Guía de contribución](CONTRIBUTING.md) — cambio reproducible y validación local.

## 🚀 Cómo usar el programa

1. Empieza por [la Parte 00](classes/part-00-ingenieria-de-software-como-profesion/README.md) y realiza el diagnóstico inicial.
2. Sigue la numeración para construir fundamentos; una ruta profesional no elimina prerrequisitos.
3. Produce el artefacto solicitado y conserva tanto el resultado como el fallo controlado.
4. Contrasta tu entrega con la rúbrica y las fuentes; leer no sustituye practicar.
5. Cuando una parte aún no tenga enseñanza completa, usa el [roadmap](ROADMAP.md) para comprender el alcance, no la presentes como terminada.
6. Elige una [ruta por rol](roles/README.md) cuando tengas la base para evaluar sus decisiones.

## 🧭 Rutas sugeridas por rol

El programa ofrece **40 guías profesionales**. Cada una incluye misión, jornada,
responsabilidades y límites, conocimientos, recorrido curricular, evidencia de
portafolio, progresión, mitos y próximos pasos. No son cuarenta cursos separados:
reutilizan las partes comunes y cambian el foco de decisión.

### 💻 Construcción de productos y sistemas

- [🧑‍💻 Software Engineer](roles/software-engineer.md) — ciclo de vida de extremo a extremo.
- [⚙️ Systems Programmer](roles/systems-programmer.md) — memoria, procesos, concurrencia y recursos.
- [⚙️ Backend Engineer](roles/backend-engineer.md) — servicios, dominio, datos y operación.
- [🎨 Frontend Engineer](roles/frontend-engineer.md) — interfaces accesibles, rápidas y mantenibles.
- [🧩 Full-stack Engineer](roles/full-stack-engineer.md) — fragmentos verticales con contratos y despliegue.
- [📱 Mobile Engineer](roles/mobile-engineer.md) — ciclo de vida, offline, sincronización y distribución.
- [🖥️ Desktop Engineer](roles/desktop-engineer.md) — integración nativa, instalación y actualización.
- [🔌 Embedded & IoT Engineer](roles/embedded-iot-engineer.md) — firmware, RTOS, energía, telemetría y OTA.
- [🛡️ Safety-Critical Software Engineer](roles/safety-critical-software-engineer.md) — hazards, controles y assurance.

### 🔗 APIs, datos y sistemas distribuidos

- [🔗 API Engineer](roles/api-engineer.md) — contratos, compatibilidad, experiencia y gobernanza.
- [🧱 Data Engineer](roles/data-engineer.md) — pipelines, contratos, calidad y lineage.
- [🗄️ Database Reliability Engineer](roles/database-reliability-engineer.md) — capacidad, migraciones y recuperación.
- [🌐 Distributed Systems Engineer](roles/distributed-systems-engineer.md) — consistencia, coordinación y fallos parciales.

### 🧪 Calidad, inclusión y análisis

- [🧪 QA / Test Automation Engineer](roles/qa-test-engineer.md) — riesgo, exploración y automatización.
- [⏱️ Performance Engineer](roles/performance-engineer.md) — profiling, carga, percentiles y capacidad.
- [♿ Accessibility Engineer](roles/accessibility-engineer.md) — WCAG, tecnología asistiva y prevención de barreras.
- [🌍 Internationalization Engineer](roles/internationalization-engineer.md) — Unicode, locales, tiempo, RTL y localización.
- [🧾 Requirements Engineer / Business Systems Analyst](roles/requirements-engineer.md) — elicitación, reglas y trazabilidad.

### 🚀 Cloud, entrega, confiabilidad y plataforma

- [🚚 DevOps Engineer](roles/devops-engineer.md) — entrega repetible, supply chain y rollback.
- [📦 Build & Release Engineer](roles/build-release-engineer.md) — artefactos, procedencia, firma y promoción.
- [☁️ Cloud Engineer](roles/cloud-engineer.md) — IAM, infraestructura, automatización y recuperación.
- [📈 Site Reliability Engineer](roles/site-reliability-engineer.md) — SLO, capacidad, incidentes y aprendizaje.
- [🔭 Observability Engineer](roles/observability-engineer.md) — logs, métricas, trazas y diagnóstico.
- [🛤️ Platform Engineer](roles/platform-engineer.md) — IDP, golden paths y autoservicio.
- [🧰 Developer Experience Engineer](roles/developer-experience-engineer.md) — tooling, onboarding y feedback loops.

### 🔐 Gobierno, economía y sostenibilidad

- [🔐 Security Engineer](roles/security-engineer.md) — secure design, AppSec y respuesta.
- [⚖️ Compliance Engineer](roles/compliance-engineer.md) — obligación, control, prueba y evidencia.
- [💸 FinOps Engineer](roles/finops-engineer.md) — costes unitarios, forecast y decisiones de valor.
- [🌱 Green Software Engineer](roles/green-software-engineer.md) — eficiencia, carbono y GreenOps medidos.
- [✍️ Technical Writer / Documentation Engineer](roles/technical-writer.md) — información técnica usable y mantenible.
- [🤝 Open Source & InnerSource Engineer](roles/open-source-innersource-engineer.md) — contribución, governance y ownership.

### 🏛️ Arquitectura, evolución y liderazgo

- [🏚️ Legacy Modernization Engineer](roles/legacy-modernization-engineer.md) — arqueología, compatibilidad y retiro.
- [🏛️ Software Architect](roles/software-architect.md) — atributos, límites, trade-offs y evolución.
- [🧩 Solutions Architect](roles/solutions-architect.md) — contexto, integración, adopción y transición.
- [🧭 Technical Product Engineer](roles/technical-product-engineer.md) — discovery, economía y factibilidad.
- [🧭 Staff / Principal / Technical Lead](roles/technical-leadership.md) — influencia, RFC, arquitectura y mentoring.
- [👥 Engineering Manager](roles/engineering-manager.md) — personas, flujo, riesgo y sostenibilidad.
- [🧭 CTO / Dirección de Tecnología](roles/cto.md) — estrategia, organización, portafolio y riesgo.

### 🤖 Ingeniería con inteligencia artificial

- [🤖 AI-Augmented Software Engineer](roles/ai-augmented-software-engineer.md) — desarrollo con agentes, evals y guardrails.
- [🧠 AI Systems Engineer](roles/ai-systems-engineer.md) — productos con modelos, datasets, fallback y operación.

### 🪜 El ecosistema de carrera técnica

Junior → Semi Senior → Senior → Staff → Principal no es una escala de velocidad ni
un camino obligatorio hacia management. Aumentan autonomía, ambigüedad, alcance e
impacto multiplicador. Engineering Manager, Architect, Technical Product y CTO son
variantes con mandatos distintos; el [índice de roles](roles/README.md) explica sus
fronteras y transiciones.

## 📦 Formatos disponibles

Actualmente existen dos superficies oficiales:

- documentación navegable directamente en GitHub;
- portal estático completo en GitHub Pages.

No se anuncian como disponibles un manual PDF consolidado, aplicación Android,
seguimiento personal, certificación ni paquetes de release. Cuando existan, deberán
tener generación reproducible, validación y evidencia propias antes de aparecer aquí.

## ✅ Calidad y CI

El repositorio no se publica a ciegas. Cada push y cada pull request validan
generación, contratos, enlaces, encoding, portal y pruebas en varias versiones y
plataformas.

| ⚙️ Workflow | Qué cubre |
| --- | --- |
| [🧪 `validate.yml`](.github/workflows/validate.yml) | manifiestos reproducibles, 480 contratos de clase, fases 3–4, UTF-8, enlaces, políticas, tests y portabilidad en Linux, Windows y macOS |
| [🚀 `pages.yml`](.github/workflows/pages.yml) | integridad de las 521 páginas, artefacto y despliegue en GitHub Pages |

Las acciones externas están fijadas por SHA, los permisos son mínimos por job y las
ejecuciones obsoletas se cancelan. Los mismos controles se ejecutan localmente:

```bash
python scripts/build_program_blueprint.py --check
python scripts/build_phase2.py --check
python scripts/build_phase3.py --check
python scripts/build_phase4.py --check
python scripts/validate_class_contracts.py
python scripts/validate_phase3.py
python scripts/validate_phase4.py
python scripts/validate_encoding.py
python scripts/validate_site.py
python scripts/validate_repository.py --strict
python -m unittest discover -s tests -v
```

Requiere Python 3.11 o posterior y no instala dependencias para estas validaciones.

## 🔎 Cobertura disponible hoy

| Superficie | Evidencia verificable |
| --- | --- |
| arquitectura | 8 etapas, 40 partes, 480 IDs únicos y 2.160 horas estimadas |
| clases | 12 con contenido desarrollado, 348 con material de trabajo y 120 con estructura curricular |
| contratos | 480 metadatos; 360 actividades y 360 rúbricas en las fases 3–4 |
| fuentes | línea base y registros por clase y por parte |
| navegación | índice global, 40 índices de parte y enlaces anterior/siguiente |
| portal | 521 páginas generadas y desplegadas por CI |
| carrera | 40 guías profesionales enlazadas a partes reales |

La evidencia detallada y las brechas están en [STATUS.md](STATUS.md), la
[auditoría de fase 3](docs/PHASE3-CONTENT-AUDIT.md), la
[auditoría de fase 4](docs/PHASE4-CONTENT-AUDIT.md) y la
[auditoría general de cobertura](docs/PROGRAM-COVERAGE-AUDIT-2026-10-04.md).

## 🧱 Estructura del repositorio

```text
curriculum.yaml    manifiesto generado de las 480 clases
catalog.json       conteos canónicos del programa
classes/           clases, índices de parte, actividades y rúbricas
roles/             índice y 40 guías profesionales
curriculum/        línea base anterior preservada para migración controlada
docs/              arquitectura, cobertura, gobierno y decisiones
manifest/          mapa de la familia de repositorios
sources/           fuentes primarias, oficiales y trazabilidad pedagógica
schemas/           contratos legibles por máquinas
site/              521 páginas estáticas generadas para GitHub Pages
blueprints/        producto documental de referencia
projects/          dominios y proyectos transversales
assessments/       diagnóstico y rúbrica
templates/         artefactos profesionales reutilizables
scripts/           generación y validación sin dependencias externas
tests/             pruebas estructurales y de navegación
```

## 🎯 Qué es y qué no es este programa

### ✅ Lo que sí es

- 📚 una arquitectura curricular secuencial de 480 clases y 40 partes;
- 🧭 un recorrido que conecta profesión, producto, construcción, operación y retiro;
- 🧪 una base de artefactos profesionales, actividades, rúbricas y producto transversal;
- 👥 cuarenta rutas profesionales con responsabilidades, límites, evidencia y progresión;
- 🌐 documentación abierta y un portal generado por CI;
- 🤖 una cobertura explícita de IA y agentes bajo verificación humana.

### ❌ Lo que no es

- 🚫 una afirmación de que las 480 clases están terminadas;
- 🚫 una colección de resúmenes o títulos para inflar conteos;
- 🚫 una certificación profesional o una promesa de empleo;
- 🚫 un curso profundo de cada lenguaje, base de datos o framework;
- 🚫 una garantía de producción basada solo en archivos o tests generados;
- 🚫 permiso para delegar decisiones críticas a un agente sin supervisión.

## 🧭 Principios editoriales

- conceptos transferibles antes que catálogos de herramientas;
- problemas, mecanismos, decisiones y evidencia antes que texto genérico;
- seguridad, privacidad, accesibilidad y recuperación desde el diseño;
- continuidad operativa antes que reescritura impulsiva;
- IA como capacidad supervisada, evaluada y reversible;
- afirmaciones públicas derivadas de fuentes verificables;
- portafolio reproducible antes que credenciales sin práctica.

## 💡 Idea fuerza

> Crear software no es producir archivos: es convertir una necesidad en un sistema
> comprensible, verificable, seguro, operable y capaz de evolucionar. La IA amplía
> esa capacidad solo cuando la intención, la evidencia y la responsabilidad siguen
> bajo control humano.

## 📄 Licencia y propiedad intelectual

El código y el contenido propio del repositorio están cubiertos por la
[Licencia MIT](LICENSE). Estándares, libros, herramientas, marcas y documentación de
terceros conservan sus licencias y términos originales. Las referencias se enlazan y
explican; no se reproducen obras protegidas.

---

Hecho para quien quiere aprender Ingeniería de Software en serio, de principio a fin.

[⬆️ Empezar por el índice de clases](classes/README.md) · [🧭 Elegir una ruta profesional](roles/README.md) · [🌐 Abrir el portal](https://vladimiracunadev-create.github.io/modern-software-engineering-program/)

¿Te resulta útil? ⭐ Dale una estrella al repositorio.

Hecho con 🧠 y ☕ por [Vladimir Acuña](https://github.com/vladimiracunadev-create).
