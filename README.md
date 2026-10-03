# 🧭 Programa de Ingeniería de Software Moderna

## 480 clases · 40 partes · de fundamentos a IA, SPEC y sistemas multiagente

Currículo abierto en español para comprender, construir, probar, entregar, operar
y evolucionar software. Recorre computación, programación, producto, requisitos,
arquitectura, datos, calidad, seguridad, DevOps, SRE y desarrollo asistido por IA.

[📚 480 clases](classes/README.md) · [🧭 Rutas](#-rutas-sugeridas) · [🧪 Práctica](#-práctica-y-producto-transversal) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/) · [📐 Estándar](docs/PEDAGOGICAL-STANDARD.md) · [📊 Estado](STATUS.md) · [🗺️ Roadmap](ROADMAP.md) · [🤝 Contribuir](CONTRIBUTING.md)

---

[![Validate](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml)
[![Pages](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/pages.yml)
[![Estado](https://img.shields.io/badge/clases%20GUIDED-24%20de%20480-2ea043?style=flat-square)](STATUS.md)
[![Currículo](https://img.shields.io/badge/currículo-480%20clases-7c5cff?style=flat-square)](curriculum.yaml)
[![Sitio](https://img.shields.io/badge/sitio-521%20páginas-ff8c42?style=flat-square)](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=flat-square)](docs/PROGRAM-ARCHITECTURE.md)
[![Licencia](https://img.shields.io/badge/licencia-MIT-3fb950?style=flat-square)](LICENSE)

> [!CAUTION]
> **Estado real:** la arquitectura contiene 480 clases y hoy hay **24 clases
> `GUIDED`** aprobadas contra el estándar pedagógico (`SE-001`–`SE-024`).
> `SE-025`–`SE-360` son borradores estructurales; `SE-361`–`SE-480` son scaffolds.
> No deben confundirse con material docente terminado.

## 🎯 Qué es esto

Es la arquitectura verificable de un programa completo de ingeniería de software.
La secuencia va desde qué es un sistema y cómo funciona un computador hasta SPEC,
agentes con herramientas, MCP, delegación, evaluación y recuperación de sistemas
asistidos por IA.

El objetivo no es coleccionar títulos. Cada clase que llegue a estado `GUIDED`
deberá desarrollar realmente:

- 🎯 objetivo, límites y resultados de aprendizaje observables;
- 🗺️ temas con la razón por la que cada uno importa;
- 📖 primeros principios, mecanismos, causas y consecuencias;
- 🧠 definiciones, características, contraejemplos y glosario;
- 🧩 diagrama específico interpretado dentro de la narrativa;
- 🛠️ herramientas, versiones, entorno y archivos clave;
- 🧪 práctica reproducible, recuperación y evidencia observable;
- ✍️ ejercicios graduados y reto con criterio de aceptación;
- ⚠️ errores comunes expresados como síntoma → causa → solución;
- ❓ preguntas frecuentes auténticas;
- 🔗 fuentes primarias u oficiales vinculadas a afirmaciones concretas.

## 🔎 Cómo revisar las clases

1. Abre el [índice plano de las 480 clases](classes/README.md).
2. Haz clic en el título para leer su `README.md` en GitHub.
3. Usa el enlace **🌐 portal** para comprobar la publicación de la misma clase.
4. Verifica si declara **GUIDED**, **borrador no aprobado** o **scaffold planificado**.
5. En una clase `GUIDED`, comprueba la conexión anterior/siguiente, el mapa visual,
   la práctica y la evidencia acumulativa.
6. Contrasta el material con el [estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md).

Acceso inmediato: [Parte 00](classes/part-00-ingenieria-de-software-como-profesion/README.md) · [SE-001 en GitHub](classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) · [SE-001 en Pages](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/SE-001.html).

## 🔗 Familia de programas

Este repositorio integra el ciclo de vida completo y se coordina con programas
especializados para profundizar lenguajes, datos y frameworks.

| Repositorio | Responsabilidad | Unidad de transferencia |
| --- | --- | --- |
| `polyglot-programming-labs` | lenguajes, algoritmos y paradigmas | comportamiento y pruebas comunes |
| `database-systems-labs` | datos, motores y recuperación | dominio, carga y garantías |
| `framework-ecosystems-labs` | interfaces, frameworks y plataformas | contrato y atributos equivalentes |
| `software-engineering-learning-suite` | producto y ciclo de vida completo | resultado operable y defendible |

Las fronteras y reglas antiduplicación están en
[docs/REPOSITORY-BOUNDARIES.md](docs/REPOSITORY-BOUNDARIES.md).

## 📐 Estándar pedagógico

Cada clase aprobada debe enseñar el tema completo, no resumirlo. El contrato exige
objetivo, resultados verificables, tabla de temas, explicación desde primeros
principios, definiciones, glosario, diagrama interpretado, preparación, laboratorio,
ejercicios, reto con aceptación, errores síntoma→causa→solución, FAQ y fuentes
trazables. El gate completo está en
[docs/PEDAGOGICAL-STANDARD.md](docs/PEDAGOGICAL-STANDARD.md).

La referencia de profundidad es la
[Parte 6 de modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/tree/main/classes/parte-6-analisis-de-malware).
Se replica su calidad docente, no su contenido ni una cuota de palabras.

## 📚 Pauta derivada de la literatura de ingeniería de software

El programa no depende de una sola herramienta ni de la opinión de un autor. Su
cobertura se contrasta con cuerpos de conocimiento, normas y especificaciones
primarias. Estas referencias orientan el currículo; una clase solo puede citarlas
como evidencia cuando su contenido haya sido revisado de forma individual.

| Área | Referencia de orientación | Uso dentro del programa |
| --- | --- | --- |
| profesión y cuerpo de conocimiento | [SWEBOK v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | mapa de áreas, prácticas y límites profesionales |
| resultados de aprendizaje | [ACM/IEEE SE2014](https://www.acm.org/binaries/content/assets/education/se2014.pdf) | línea base curricular histórica y competencias |
| calidad del producto | [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | atributos de calidad y decisiones verificables |
| desarrollo seguro | [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) | seguridad integrada al ciclo de vida |
| accesibilidad | [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/) | experiencia inclusiva y criterios comprobables |
| contratos HTTP y API | [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) y [OpenAPI](https://spec.openapis.org/oas/latest.html) | semántica, interoperabilidad y especificaciones ejecutables |
| IA responsable | [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) | riesgo, evaluación y supervisión humana |
| desarrollo basado en SPEC | [Spec Kit](https://github.github.com/spec-kit/) | intención, especificación, plan, tareas e implementación |
| agentes y herramientas | [Model Context Protocol](https://modelcontextprotocol.io/) | contexto, capacidades, autorización y límites |

## 📖 De dónde sale el material

Las fuentes se mantienen como datos auditables, no como una bibliografía decorativa:

- [línea base](sources/baseline.json): normas y documentación que definen la cobertura general;
- [registro por clase](sources/class-sources.json): asignación inicial de fuentes a las 480 clases;
- [registro de fase 3](sources/phase3.json): fuentes usadas por 24 clases `GUIDED` y 156 borradores;
- [registro de fase 4](sources/phase4.json): fuentes usadas por `SE-181`–`SE-360`;
- [política de fuentes](docs/SOURCES.md): autoridad, vigencia, trazabilidad y tratamiento de material obsoleto.

Una asignación en el registro **no demuestra** que la clase esté terminada. Falta
ligar cada afirmación importante con su fuente concreta y revisar vigencia,
interpretación y alcance antes de promoverla a `GUIDED`.

## 🗂️ Las 40 partes

Cada parte tiene un README con sus doce clases enlazadas. La fase 3 comprende las
partes 00–14 y la fase 4 las partes 15–29. Las partes 00–01 están aprobadas; las
partes 02–29 siguen pendientes de revisión cualitativa clase por clase.

| # | Parte | Clases | Foco | Estado | README |
| ---: | --- | --- | --- | --- | --- |
| 00 | Ingeniería de software como profesión | SE-001–SE-012 | disciplina, ética, evidencia y calidad | `GUIDED` | [📘 leer](classes/part-00-ingenieria-de-software-como-profesion/README.md) |
| 01 | Computadores y representación de información | SE-013–SE-024 | máquina, datos, memoria y runtimes | `GUIDED` | [📘 leer](classes/part-01-computadores-y-representacion-de-informacion/README.md) |
| 02 | Sistemas operativos, terminal y automatización base | SE-025–SE-036 | Windows, Linux, macOS, shells y diagnóstico | borrador no aprobado | [📘 leer](classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md) |
| 03 | Redes, Internet y protocolos | SE-037–SE-048 | TCP/IP, DNS, HTTP, TLS y observación | borrador no aprobado | [📘 leer](classes/part-03-redes-internet-y-protocolos/README.md) |
| 04 | Pensamiento computacional y resolución de problemas | SE-049–SE-060 | lógica, modelos, complejidad y estrategias | borrador no aprobado | [📘 leer](classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/README.md) |
| 05 | Fundamentos de programación | SE-061–SE-072 | control, funciones, datos, errores y pruebas | borrador no aprobado | [📘 leer](classes/part-05-fundamentos-de-programacion/README.md) |
| 06 | Paradigmas de programación | SE-073–SE-084 | imperativo, objetos, funcional, lógico y reactivo | borrador no aprobado | [📘 leer](classes/part-06-paradigmas-de-programacion/README.md) |
| 07 | Estructuras de datos y algoritmos | SE-085–SE-096 | colecciones, grafos, diseño y medición | borrador no aprobado | [📘 leer](classes/part-07-estructuras-de-datos-y-algoritmos/README.md) |
| 08 | Entornos, herramientas y depuración | SE-097–SE-108 | IDE, depuración, profiling y entornos reproducibles | borrador no aprobado | [📘 leer](classes/part-08-entornos-herramientas-y-depuracion/README.md) |
| 09 | Bibliotecas, paquetes, SDK y automatización | SE-109–SE-120 | dependencias, SemVer, CLI, plugins y DX | borrador no aprobado | [📘 leer](classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md) |
| 10 | Descubrimiento y estrategia de producto | SE-121–SE-132 | problema, usuarios, mercado y experimentación | borrador no aprobado | [📘 leer](classes/part-10-descubrimiento-y-estrategia-de-producto/README.md) |
| 11 | Economía, métricas y decisiones de producto | SE-133–SE-144 | valor, costo, métricas y priorización | borrador no aprobado | [📘 leer](classes/part-11-economia-metricas-y-decisiones-de-producto/README.md) |
| 12 | Ingeniería de requisitos | SE-145–SE-156 | elicitación, calidad, trazabilidad y cambio | borrador no aprobado | [📘 leer](classes/part-12-ingenieria-de-requisitos/README.md) |
| 13 | Especificaciones, contratos y modelos | SE-157–SE-168 | SPEC, invariantes, APIs y aceptación | borrador no aprobado | [📘 leer](classes/part-13-especificaciones-contratos-y-modelos/README.md) |
| 14 | Experiencia, accesibilidad e internacionalización | SE-169–SE-180 | UX, inclusión, contenido e i18n | borrador no aprobado | [📘 leer](classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md) |
| 15 | Procesos, planificación y estimación | SE-181–SE-192 | flujo, incertidumbre y mejora | borrador no aprobado | [📘 leer](classes/part-15-procesos-planificacion-y-estimacion/README.md) |
| 16 | Git, colaboración y código abierto | SE-193–SE-204 | historial, integración y gobernanza | borrador no aprobado | [📘 leer](classes/part-16-git-colaboracion-y-codigo-abierto/README.md) |
| 17 | Documentación y conocimiento técnico | SE-205–SE-216 | docs-as-code, ADR, runbook y búsqueda | borrador no aprobado | [📘 leer](classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| 18 | CLI, TUI, servicios y automatización | SE-217–SE-228 | interfaces textuales y procesos | borrador no aprobado | [📘 leer](classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| 19 | Web, frontend y aplicaciones progresivas | SE-229–SE-240 | navegador, UI, estado y PWA | borrador no aprobado | [📘 leer](classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md) |
| 20 | Backend, APIs y procesamiento asíncrono | SE-241–SE-252 | servicios, contratos y tareas | borrador no aprobado | [📘 leer](classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| 21 | Software móvil, escritorio y multiplataforma | SE-253–SE-264 | plataformas, distribución y ciclo de vida | borrador no aprobado | [📘 leer](classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) |
| 22 | Embedded, IoT y tiempo real | SE-265–SE-276 | recursos, hardware y temporización | borrador no aprobado | [📘 leer](classes/part-22-embedded-iot-y-tiempo-real/README.md) |
| 23 | Software especializado y dominios | SE-277–SE-288 | datos, ciencia, juegos y regulación | borrador no aprobado | [📘 leer](classes/part-23-software-especializado-y-dominios/README.md) |
| 24 | Diseño, patrones y refactorización | SE-289–SE-300 | diseño evolutivo y deuda | borrador no aprobado | [📘 leer](classes/part-24-diseno-patrones-y-refactorizacion/README.md) |
| 25 | Arquitectura de software y dominio | SE-301–SE-312 | límites, estilos, DDD y decisiones | borrador no aprobado | [📘 leer](classes/part-25-arquitectura-de-software-y-dominio/README.md) |
| 26 | Datos, persistencia y recuperación | SE-313–SE-324 | modelos, transacciones, índices y backup | borrador no aprobado | [📘 leer](classes/part-26-datos-persistencia-y-recuperacion/README.md) |
| 27 | Integración, eventos y mensajería | SE-325–SE-336 | contratos, colas, eventos y consistencia | borrador no aprobado | [📘 leer](classes/part-27-integracion-eventos-y-mensajeria/README.md) |
| 28 | Concurrencia y sistemas distribuidos | SE-337–SE-348 | coordinación, fallos y consenso | borrador no aprobado | [📘 leer](classes/part-28-concurrencia-y-sistemas-distribuidos/README.md) |
| 29 | Cloud, plataforma e infraestructura | SE-349–SE-360 | nube, contenedores, IaC y plataforma | borrador no aprobado | [📘 leer](classes/part-29-cloud-plataforma-e-infraestructura/README.md) |
| 30 | Estrategia y técnicas de prueba | SE-361–SE-372 | niveles, propiedades, contratos y E2E | planificado | [📘 leer](classes/part-30-estrategia-y-tecnicas-de-prueba/README.md) |
| 31 | Calidad, rendimiento y resiliencia | SE-373–SE-384 | atributos, carga, degradación y recuperación | planificado | [📘 leer](classes/part-31-calidad-rendimiento-y-resiliencia/README.md) |
| 32 | Seguridad, privacidad y cumplimiento | SE-385–SE-396 | amenazas, controles, privacidad y regulación | planificado | [📘 leer](classes/part-32-seguridad-privacidad-y-cumplimiento/README.md) |
| 33 | Build, release y cadena de suministro | SE-397–SE-408 | builds, artefactos, SBOM y procedencia | planificado | [📘 leer](classes/part-33-build-release-y-cadena-de-suministro/README.md) |
| 34 | CI/CD, IaC y platform engineering | SE-409–SE-420 | pipelines, despliegue y autoservicio | planificado | [📘 leer](classes/part-34-ci-cd-iac-y-platform-engineering/README.md) |
| 35 | Observabilidad, SRE e incidentes | SE-421–SE-432 | señales, SLO, guardias e incidentes | planificado | [📘 leer](classes/part-35-observabilidad-sre-e-incidentes/README.md) |
| 36 | Mantenimiento y modernización legacy | SE-433–SE-444 | comprensión, migración y continuidad | planificado | [📘 leer](classes/part-36-mantenimiento-y-modernizacion-legacy/README.md) |
| 37 | Gestión, liderazgo y práctica profesional | SE-445–SE-456 | equipos, comunicación y decisiones | planificado | [📘 leer](classes/part-37-gestion-liderazgo-y-practica-profesional/README.md) |
| 38 | Desarrollo de software asistido por IA | SE-457–SE-468 | copilotos, contexto, evals y seguridad | planificado | [📘 leer](classes/part-38-desarrollo-de-software-asistido-por-ia/README.md) |
| 39 | SPEC, agentes y ciclo de vida agentic | SE-469–SE-480 | SPEC, MCP, agentes, delegación y control | planificado | [📘 leer](classes/part-39-spec-agentes-y-ciclo-de-vida-agentic/README.md) |

➡️ [Abrir el índice plano con enlaces directos a las 480 clases](classes/README.md).

La fuente canónica de títulos, estados y horas es [curriculum.yaml](curriculum.yaml).

## 🤖 IA, SPEC y agentes

La etapa final cubre autocompletado, chat, edición, generación, pruebas,
documentación, migraciones, context engineering, evaluaciones, desarrollo basado en
especificaciones, greenfield, brownfield, reparación, agentes con herramientas,
skills, plugins, MCP, delegación, multiagente, aprobación humana, seguridad agentic y
recuperación.

La matriz precisa se encuentra en [docs/COVERAGE-MATRIX.md](docs/COVERAGE-MATRIX.md).

## 🧪 Práctica y producto transversal

La práctica se organiza alrededor de un producto de referencia que atraviesa
descubrimiento, requisitos, arquitectura, APIs, pruebas, amenazas y operación. El
objetivo es que una decisión sobreviva al cambio de lenguaje o framework y deje
evidencia revisable.

| Recurso | Qué permite revisar hoy |
| --- | --- |
| [Producto de referencia](blueprints/reference-product/README.md) | mapa del caso transversal y sus artefactos |
| [Requisitos](blueprints/reference-product/REQUIREMENTS.md) | alcance, reglas y trazabilidad inicial |
| [Arquitectura](blueprints/reference-product/ARCHITECTURE.md) | límites y estructura del sistema |
| [Contrato OpenAPI](blueprints/reference-product/api/openapi.yaml) | interfaz formal y verificable |
| [Estrategia de pruebas](blueprints/reference-product/TEST_STRATEGY.md) | niveles, riesgos y evidencia esperada |
| [Modelo de amenazas](blueprints/reference-product/THREAT_MODEL.md) | activos, amenazas y controles |
| [Runbook de degradación](blueprints/reference-product/runbooks/API_DEGRADED.md) | diagnóstico y recuperación operacional |
| [Proyecto integrador](projects/capstone.md) | transferencia del aprendizaje a un producto completo |
| [Rúbrica transversal](assessments/rubric.md) | criterios comunes de evaluación |

Estos artefactos son una base documental versionada; todavía no constituyen una
colección de laboratorios ejecutados ni evidencia de que las 456 clases restantes
estén aprobadas.

## 🌐 Portal y navegación

El [portal público](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
permite buscar por texto, filtrar por parte y estado, abrir una parte y leer cada
clase. La Parte 00 añade un caso conductor, ruta de evidencias, progreso visible,
conexión **vienes de / construyes / conecta con**, índice lateral y diagramas
renderizados con su notación fuente accesible. Cada clase conserva navegación
**anterior / parte / índice / siguiente** al inicio y al final, además de su enlace equivalente en GitHub. El
[índice plano](classes/README.md) conserva acceso directo a las 480 clases y a sus
480 páginas publicadas.

La fuente de verdad sigue siendo el repositorio: Pages es una presentación generada
y la CI falla si difiere de los manifiestos o del contenido de las clases.

## 👩‍🏫 Para instructores y revisores

- [Arquitectura del programa](docs/PROGRAM-ARCHITECTURE.md): etapas, progresión y dependencias;
- [modelo de aprendizaje](docs/LEARNING-MODEL.md): cómo se transforma teoría en evidencia;
- [estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md): gate obligatorio por clase;
- [matriz de cobertura](docs/COVERAGE-MATRIX.md): conceptos y ubicación curricular;
- [auditoría de fase 3](docs/PHASE3-CONTENT-AUDIT.md): defectos conocidos y conteos comprobables;
- [gobernanza](docs/GOVERNANCE.md): decisiones, revisión y evolución;
- [guía de contribución](CONTRIBUTING.md): cambio reproducible y validación local.

## 🚀 Cómo usar el programa

1. Empieza en el [índice completo](classes/README.md) y abre la ruta que corresponda a tu base actual.
2. Lee el estado de la clase: un borrador sirve para revisión; un scaffold solo describe trabajo pendiente.
3. Produce el artefacto solicitado, registra decisiones y conserva evidencia del resultado y del fallo.
4. Compara tu entrega con la rúbrica y las fuentes; no promociones contenido por cantidad de texto.
5. Continúa con los enlaces anterior/siguiente o vuelve al README de la parte para revisar dependencias.

## 🧭 Rutas sugeridas

| Objetivo | Recorrido recomendado | Resultado esperado |
| --- | --- | --- |
| construir fundamentos sólidos | partes 00–09 | razonar sobre sistemas, código, datos, herramientas y depuración |
| pasar de problema a SPEC | partes 10–17 | descubrir valor, especificar, planificar, colaborar y documentar |
| desarrollar productos en distintas plataformas | partes 18–29 | construir interfaces, servicios, sistemas de datos, distribuidos y cloud |
| asegurar calidad y entrega | partes 30–34 | probar, proteger, empaquetar y desplegar con evidencia |
| operar y evolucionar software | partes 35–37 | observar, responder, modernizar y liderar cambios |
| crear software con IA y agentes | partes 38–39, después de 00–17 y 30–35 | usar SPEC, contexto, evals, herramientas, MCP, delegación y recuperación |

## 📦 Formatos y superficies disponibles

Actualmente existen dos superficies oficiales: documentación navegable en GitHub y
el portal estático en GitHub Pages. No se anuncian como disponibles un manual
descargable, una aplicación móvil/escritorio, seguimiento personal de progreso ni
releases empaquetadas; cualquiera de esas superficies deberá implementarse,
probarse y declararse de forma separada antes de aparecer como capacidad del programa.

## 📊 Estado verificable

Las fases 1 y 2 están resueltas. La fase 3 fue reabierta tras una auditoría y la
infraestructura pública de fase 4 ya está implementada:

- arquitectura de ocho etapas;
- 40 partes con doce clases cada una;
- 480 identificadores y títulos únicos;
- contrato pedagógico y estados de madurez;
- propietarios y fronteras entre repositorios;
- ADR de expansión;
- fuentes primarias iniciales;
- manifiesto, catálogo, validación y CI multiplataforma.
- 480 scaffolds con contrato pedagógico protegido;
- 480 metadatos y registros bibliográficos iniciales;
- índices globales y por parte generados;
- sitio estático con 521 páginas, búsqueda y filtros;
- validadores dedicados de contratos y UTF-8;
- workflow separado para GitHub Pages.
- alcance corregido: 180 clases consecutivas, `SE-001`–`SE-180`;
- 24 clases `GUIDED` y 156 borradores estructurales de fase 3;
- fase 4 añadida: 180 borradores, actividades y rúbricas de `SE-181`–`SE-360`;
- texto íntegro de cada borrador publicado en Pages, no una ficha-resumen;
- promoción limitada a las 24 clases revisadas de las partes 00–01;
- instrucción permanente en [AGENTS.md](AGENTS.md) para impedir la regresión.

`GUIDED` no significa `EXECUTABLE`, `TESTED` u `OPERABLE`; tampoco se concede por
generación automática. El estado actual vive en [STATUS.md](STATUS.md) y la
evidencia de por qué las 180 entradas no cuentan como clases construidas está en
[docs/PHASE3-CONTENT-AUDIT.md](docs/PHASE3-CONTENT-AUDIT.md).
La auditoría equivalente de fase 4 está en
[docs/PHASE4-CONTENT-AUDIT.md](docs/PHASE4-CONTENT-AUDIT.md).

## ✅ Calidad, CI y validación local

| Workflow | Qué comprueba | Plataformas / salida |
| --- | --- | --- |
| [Validate](.github/workflows/validate.yml) | generación reproducible, contratos, madurez, UTF-8, enlaces, políticas y tests | Python 3.11–3.14 en Linux; portabilidad en Windows y macOS |
| [Pages](.github/workflows/pages.yml) | las 521 páginas generadas, integridad del portal y despliegue | artefacto y publicación en GitHub Pages |

Las acciones externas están fijadas por SHA, los permisos son mínimos por job y los
workflows usan concurrencia con cancelación de ejecuciones obsoletas. La misma
validación crítica puede ejecutarse localmente sin instalar dependencias:

Requiere Python 3.11 o posterior y no instala dependencias:

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

## 🧱 Estructura

```text
curriculum.yaml    manifiesto generado de las 480 clases
catalog.json       métricas canónicas de estado
classes/           480 clases; 24 GUIDED, 336 borradores y 120 scaffolds
curriculum/        línea base anterior, pendiente de migración controlada
docs/              arquitectura, cobertura, gobierno y decisiones
manifest/          mapa de la familia de repositorios
sources/           registro de fuentes primarias y oficiales
schemas/           contratos legibles por máquinas
site/              521 páginas estáticas generadas para GitHub Pages
blueprints/        producto documental de referencia
projects/          dominios y proyectos transversales
assessments/       diagnóstico y rúbrica
templates/         artefactos profesionales reutilizables
portal/            portada local histórica de transición
scripts/           generación y validación sin dependencias externas
tests/             pruebas estructurales
```

## 🌐 Publicación

La identidad, About, topics, gates y URL de Pages están definidos en
[docs/PUBLICATION-PLAN.md](docs/PUBLICATION-PLAN.md). El sitio se genera íntegramente
desde el manifiesto. El workflow remoto y la respuesta HTTPS del
[portal público](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
fueron verificados el 30 de septiembre de 2026.

## 🎯 Qué es y qué no es este programa

| Es | No es todavía |
| --- | --- |
| una arquitectura pública de 480 clases con secuencia y fuentes | 480 clases terminadas |
| 24 clases `GUIDED` y 336 borradores ampliados | 480 clases aprobadas o listas para impartir |
| un estándar explícito para aceptar contenido | una certificación profesional |
| un producto transversal con artefactos de ingeniería | una garantía de empleo o dominio sin práctica |
| un portal generado y verificado por CI | una app con cuenta, progreso o modo offline |
| una cobertura deliberada de IA, SPEC y agentes | permiso para delegar decisiones críticas sin supervisión |

## 🧭 Principios editoriales

- conceptos transferibles antes que catálogos de herramientas;
- problemas, decisiones y evidencia antes que texto genérico;
- seguridad, privacidad, accesibilidad y recuperación desde el diseño;
- continuidad operativa antes que reescritura impulsiva;
- IA como capacidad supervisada, evaluada y reversible;
- afirmaciones públicas derivadas de fuentes verificables;
- portafolio reproducible en vez de certificación sin práctica.

## 💡 Idea fuerza

> Crear software no es producir archivos: es convertir una necesidad en un sistema
> comprensible, verificable, seguro, operable y capaz de evolucionar. La IA amplía
> esa capacidad solo cuando la intención, la evidencia y la responsabilidad siguen
> bajo control humano.

## 📄 Licencia

MIT para el código y contenido propio actualmente cubierto por [LICENSE](LICENSE).
Las fuentes, estándares, marcas y tecnologías externas conservan sus propios términos.

---

Hecho para aprender ingeniería de software de principio a fin, con práctica,
evidencia y límites explícitos.

[⬆️ Volver al inicio](#-programa-de-ingeniería-de-software-moderna) · [📚 Abrir las 480 clases](classes/README.md) · [🌐 Entrar al portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/) · [👤 Vladimir Acuña](https://github.com/vladimiracunadev-create)
