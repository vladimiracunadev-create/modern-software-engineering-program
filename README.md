# 🧭 Programa de Ingeniería de Software Moderna

## 480 clases · 40 partes · de fundamentos a IA, SPEC y sistemas multiagente

Currículo abierto en español para comprender, construir, probar, entregar, operar
y evolucionar software. Recorre computación, programación, producto, requisitos,
arquitectura, datos, calidad, seguridad, DevOps, SRE y desarrollo asistido por IA.

[📚 Índice completo de las 480 clases](classes/README.md) · [🔎 Revisar fase 3 desde SE-001](classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md) · [🌐 Portal web](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/) · [📐 Estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md) · [📊 Estado verificable](STATUS.md) · [🗺️ Roadmap](ROADMAP.md) · [🤝 Contribuir](CONTRIBUTING.md)

---

[![Validate](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml)
[![Pages](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/pages.yml)
[![Estado](https://img.shields.io/badge/clases%20aprobadas-0%20de%20180-c47f17?style=flat-square)](STATUS.md)
[![Currículo](https://img.shields.io/badge/currículo-480%20clases-7c5cff?style=flat-square)](curriculum.yaml)
[![Sitio](https://img.shields.io/badge/sitio-521%20páginas-ff8c42?style=flat-square)](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=flat-square)](docs/PROGRAM-ARCHITECTURE.md)
[![Licencia](https://img.shields.io/badge/licencia-MIT-3fb950?style=flat-square)](LICENSE)

> [!CAUTION]
> **Estado real:** la arquitectura contiene 480 clases, pero hoy hay **0 clases
> aprobadas** contra el estándar pedagógico. `SE-001`–`SE-180` son borradores
> estructurales públicos y repetitivos; `SE-181`–`SE-480` son scaffolds. No deben
> confundirse con material docente terminado.

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
4. Verifica si declara **borrador no aprobado** o **scaffold planificado**.
5. Contrasta el material con el [estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md).

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

## 🗂️ Las 40 partes

Cada parte tiene un README con sus doce clases enlazadas. La fase 3 comprende las
partes 00–14; todas siguen pendientes de desarrollo y aprobación cualitativa.

| # | Parte | Clases | Foco | Estado | README |
| ---: | --- | --- | --- | --- | --- |
| 00 | Ingeniería de software como profesión | SE-001–SE-012 | disciplina, ética, evidencia y calidad | borrador no aprobado | [📘 leer](classes/part-00-ingenieria-de-software-como-profesion/README.md) |
| 01 | Computadores y representación de información | SE-013–SE-024 | máquina, datos, memoria y runtimes | borrador no aprobado | [📘 leer](classes/part-01-computadores-y-representacion-de-informacion/README.md) |
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
| 15 | Procesos, planificación y estimación | SE-181–SE-192 | flujo, incertidumbre y mejora | planificado | [📘 leer](classes/part-15-procesos-planificacion-y-estimacion/README.md) |
| 16 | Git, colaboración y código abierto | SE-193–SE-204 | historial, integración y gobernanza | planificado | [📘 leer](classes/part-16-git-colaboracion-y-codigo-abierto/README.md) |
| 17 | Documentación y conocimiento técnico | SE-205–SE-216 | docs-as-code, ADR, runbook y búsqueda | planificado | [📘 leer](classes/part-17-documentacion-y-conocimiento-tecnico/README.md) |
| 18 | CLI, TUI, servicios y automatización | SE-217–SE-228 | interfaces textuales y procesos | planificado | [📘 leer](classes/part-18-cli-tui-servicios-y-automatizacion/README.md) |
| 19 | Web, frontend y aplicaciones progresivas | SE-229–SE-240 | navegador, UI, estado y PWA | planificado | [📘 leer](classes/part-19-web-frontend-y-aplicaciones-progresivas/README.md) |
| 20 | Backend, APIs y procesamiento asíncrono | SE-241–SE-252 | servicios, contratos y tareas | planificado | [📘 leer](classes/part-20-backend-apis-y-procesamiento-asincrono/README.md) |
| 21 | Software móvil, escritorio y multiplataforma | SE-253–SE-264 | plataformas, distribución y ciclo de vida | planificado | [📘 leer](classes/part-21-software-movil-escritorio-y-multiplataforma/README.md) |
| 22 | Embedded, IoT y tiempo real | SE-265–SE-276 | recursos, hardware y temporización | planificado | [📘 leer](classes/part-22-embedded-iot-y-tiempo-real/README.md) |
| 23 | Software especializado y dominios | SE-277–SE-288 | datos, ciencia, juegos y regulación | planificado | [📘 leer](classes/part-23-software-especializado-y-dominios/README.md) |
| 24 | Diseño, patrones y refactorización | SE-289–SE-300 | diseño evolutivo y deuda | planificado | [📘 leer](classes/part-24-diseno-patrones-y-refactorizacion/README.md) |
| 25 | Arquitectura de software y dominio | SE-301–SE-312 | límites, estilos, DDD y decisiones | planificado | [📘 leer](classes/part-25-arquitectura-de-software-y-dominio/README.md) |
| 26 | Datos, persistencia y recuperación | SE-313–SE-324 | modelos, transacciones, índices y backup | planificado | [📘 leer](classes/part-26-datos-persistencia-y-recuperacion/README.md) |
| 27 | Integración, eventos y mensajería | SE-325–SE-336 | contratos, colas, eventos y consistencia | planificado | [📘 leer](classes/part-27-integracion-eventos-y-mensajeria/README.md) |
| 28 | Concurrencia y sistemas distribuidos | SE-337–SE-348 | coordinación, fallos y consenso | planificado | [📘 leer](classes/part-28-concurrencia-y-sistemas-distribuidos/README.md) |
| 29 | Cloud, plataforma e infraestructura | SE-349–SE-360 | nube, contenedores, IaC y plataforma | planificado | [📘 leer](classes/part-29-cloud-plataforma-e-infraestructura/README.md) |
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

## 📊 Estado verificable

Las fases 1 y 2 están resueltas. La fase 3 fue reabierta tras una auditoría:

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
- 180 borradores estructurales, actividades y rúbricas visibles para revisión;
- texto íntegro de cada borrador publicado en Pages, no una ficha-resumen;
- 0 clases `GUIDED` hasta completar revisión cualitativa clase por clase;
- instrucción permanente en [AGENTS.md](AGENTS.md) para impedir la regresión.

`GUIDED` no significa `EXECUTABLE`, `TESTED` u `OPERABLE`; tampoco se concede por
generación automática. El estado actual vive en [STATUS.md](STATUS.md) y la
evidencia de por qué las 180 entradas no cuentan como clases construidas está en
[docs/PHASE3-CONTENT-AUDIT.md](docs/PHASE3-CONTENT-AUDIT.md).

## ✅ Validación local

Requiere Python 3.11 o posterior y no instala dependencias:

```bash
python scripts/build_program_blueprint.py --check
python scripts/build_phase2.py --check
python scripts/build_phase3.py --check
python scripts/validate_class_contracts.py
python scripts/validate_phase3.py
python scripts/validate_encoding.py
python scripts/validate_site.py
python scripts/validate_repository.py --strict
python -m unittest discover -s tests -v
```

## 🧱 Estructura

```text
curriculum.yaml    manifiesto generado de las 480 clases
catalog.json       métricas canónicas de estado
classes/           480 clases; 180 borradores en revisión de fase 3
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

## 📖 Fuentes

La línea base y la fase 3 usan fuentes oficiales o primarias y registran fecha,
autoridad, estado y propósito en [sources/baseline.json](sources/baseline.json) y
[sources/phase3.json](sources/phase3.json). Las afirmaciones temporales se revisan
antes de publicarse.

## 🌐 Publicación

La identidad, About, topics, gates y URL de Pages están definidos en
[docs/PUBLICATION-PLAN.md](docs/PUBLICATION-PLAN.md). El sitio se genera íntegramente
desde el manifiesto. El workflow remoto y la respuesta HTTPS del
[portal público](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
fueron verificados el 30 de septiembre de 2026.

## 🧭 Filosofía

- conceptos transferibles antes que catálogos de herramientas;
- problemas, decisiones y evidencia antes que texto genérico;
- seguridad, privacidad, accesibilidad y recuperación desde el diseño;
- continuidad operativa antes que reescritura impulsiva;
- IA como capacidad supervisada, evaluada y reversible;
- afirmaciones públicas derivadas de fuentes verificables;
- portafolio reproducible en vez de certificación sin práctica.

## 📄 Licencia

MIT para el código y contenido propio actualmente cubierto por [LICENSE](LICENSE).
Las fuentes, estándares, marcas y tecnologías externas conservan sus propios términos.
