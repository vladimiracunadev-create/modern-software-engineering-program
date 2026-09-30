<div align="center">

# 🧭 Software Engineering Learning Suite

## **8 etapas · 40 partes · 480 clases especificadas · 2.160 horas estimadas**

**Programa integral y verificable para aprender a descubrir, especificar, construir,
probar, entregar, operar, recuperar y evolucionar software — desde los fundamentos
de computación hasta SPEC, desarrollo asistido por IA y sistemas multiagente.**

[![Validate](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml)
[![Estado](https://img.shields.io/badge/fase%202-infraestructura%20lista-2e8b57?style=flat-square)](STATUS.md)
[![Clases](https://img.shields.io/badge/clases-480%20planificadas-7c5cff?style=flat-square)](curriculum.yaml)
[![Sitio](https://img.shields.io/badge/sitio-521%20páginas-ff8c42?style=flat-square)](site/index.html)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=flat-square)](docs/PROGRAM-ARCHITECTURE.md)
[![License](https://img.shields.io/badge/license-MIT-3fb950?style=flat-square)](LICENSE)

</div>

> [!IMPORTANT]
> Las 480 clases están **especificadas y planificadas**, no terminadas. El estado
> `PLANNED` evita presentar estructura generada como contenido pedagógico construido.
> Consulta [STATUS.md](STATUS.md) para conocer la evidencia disponible.

## Qué es

Este repositorio es el integrador de una familia de programas prácticos. Define el
ciclo de vida completo, la arquitectura curricular, los productos persistentes, la
evaluación y la evidencia profesional. La profundidad de lenguajes, datos y
frameworks pertenece a repositorios especializados.

| Repositorio | Responsabilidad | Unidad de transferencia |
| --- | --- | --- |
| `polyglot-programming-labs` | lenguajes, algoritmos y paradigmas | comportamiento y pruebas comunes |
| `database-systems-labs` | datos, motores y recuperación | dominio, carga y garantías |
| `framework-ecosystems-labs` | interfaces, frameworks y plataformas | contrato y atributos equivalentes |
| `software-engineering-learning-suite` | producto y ciclo de vida completo | resultado operable y defendible |

Las fronteras y reglas antiduplicación están en
[docs/REPOSITORY-BOUNDARIES.md](docs/REPOSITORY-BOUNDARIES.md).

## Recorrido

| Etapa | Partes | Resultado |
| --- | ---: | --- |
| A · Fundamentos de la profesión | 00–04 | comprender la máquina, la red y el problema |
| B · Programación y construcción | 05–09 | construir y transferir soluciones |
| C · Producto, requisitos y especificación | 10–17 | convertir intención en evidencia verificable |
| D · Superficies y formas de software | 18–23 | producir software para plataformas y dominios distintos |
| E · Diseño, arquitectura, datos e integración | 24–29 | diseñar sistemas evolutivos y distribuidos |
| F · Calidad, seguridad y entrega | 30–34 | verificar y entregar artefactos confiables |
| G · Operación, evolución y liderazgo | 35–37 | operar, recuperar, modernizar y liderar |
| H · Ingeniería de software nativa con IA | 38–39 | trabajar con IA, SPEC y agentes bajo control |

El detalle completo —incluidos los 480 títulos, propietarios, horas y estados— vive
en [curriculum.yaml](curriculum.yaml). La arquitectura y el contrato de una clase
están en [docs/PROGRAM-ARCHITECTURE.md](docs/PROGRAM-ARCHITECTURE.md).

## IA, SPEC y agentes

La etapa final cubre autocompletado, chat, edición, generación, pruebas,
documentación, migraciones, context engineering, evaluaciones, desarrollo basado en
especificaciones, greenfield, brownfield, reparación, agentes con herramientas,
skills, plugins, MCP, delegación, multiagente, aprobación humana, seguridad agentic y
recuperación.

La matriz precisa se encuentra en [docs/COVERAGE-MATRIX.md](docs/COVERAGE-MATRIX.md).

## Estado verificable

Las fases 1 y 2 están resueltas:

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

El programa todavía no afirma que las clases estén construidas. Esa producción
corresponde a las fases siguientes descritas en [ROADMAP.md](ROADMAP.md).

## Validación local

Requiere Python 3.11 o posterior y no instala dependencias:

```bash
python scripts/build_program_blueprint.py --check
python scripts/build_phase2.py --check
python scripts/validate_class_contracts.py
python scripts/validate_encoding.py
python scripts/validate_site.py
python scripts/validate_repository.py --strict
python -m unittest discover -s tests -v
```

## Estructura

```text
curriculum.yaml    manifiesto generado de las 480 clases
catalog.json       métricas canónicas de estado
classes/           40 índices, 480 scaffolds y metadatos
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

## Fuentes

La línea base usa fuentes oficiales o primarias y registra fecha, autoridad, estado y
propósito en [sources/baseline.json](sources/baseline.json). Las afirmaciones
temporales se revisan antes de publicarse.

## Publicación

La identidad, About, topics, gates y URL de Pages están definidos en
[docs/PUBLICATION-PLAN.md](docs/PUBLICATION-PLAN.md). El sitio se genera íntegramente
desde el manifiesto y su publicación solo se considera válida después de comprobar el
workflow remoto y la respuesta de la URL pública.

## Filosofía

- conceptos transferibles antes que catálogos de herramientas;
- problemas, decisiones y evidencia antes que texto genérico;
- seguridad, privacidad, accesibilidad y recuperación desde el diseño;
- continuidad operativa antes que reescritura impulsiva;
- IA como capacidad supervisada, evaluada y reversible;
- afirmaciones públicas derivadas de fuentes verificables;
- portafolio reproducible en vez de certificación sin práctica.

## Licencia

MIT para el código y contenido propio actualmente cubierto por [LICENSE](LICENSE).
Las fuentes, estándares, marcas y tecnologías externas conservan sus propios términos.
