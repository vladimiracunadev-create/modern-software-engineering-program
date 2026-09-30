<div align="center">

# 🧭 Software Engineering Learning Suite

## **480 clases · 40 partes · de fundamentos a IA y sistemas multiagente**

**Programa profesional de ingeniería de software en español: fundamentos,
programación, producto, SPEC, arquitectura, calidad, seguridad, DevOps, SRE,
desarrollo asistido por IA y sistemas multiagente.**

[📚 Índice de clases](classes/README.md) · [🌐 Portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/) · [📐 Estándar pedagógico](docs/PEDAGOGICAL-STANDARD.md) · [📊 Estado verificable](STATUS.md) · [🗺️ Roadmap](ROADMAP.md) · [🤝 Contribuir](CONTRIBUTING.md)

---

[![Validate](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/software-engineering-learning-suite/actions/workflows/validate.yml)
[![Estado](https://img.shields.io/badge/fase%203-en%20reconstrucción-c47f17?style=flat-square)](STATUS.md)
[![Clases](https://img.shields.io/badge/objetivo%20fase%203-180%20clases-7c5cff?style=flat-square)](curriculum.yaml)
[![Sitio](https://img.shields.io/badge/sitio-521%20páginas-ff8c42?style=flat-square)](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
[![Idioma](https://img.shields.io/badge/idioma-español-1f6feb?style=flat-square)](docs/PROGRAM-ARCHITECTURE.md)
[![License](https://img.shields.io/badge/license-MIT-3fb950?style=flat-square)](LICENSE)

</div>

> [!WARNING]
> La fase 3 está **en reconstrucción cualitativa**. Su alcance correcto es
> `SE-001`–`SE-180`. Los 180 borradores son públicos para auditoría, pero hay
> **0 clases aprobadas** contra el estándar pedagógico profundo. Ninguna se presenta
> como terminada por tener muchas secciones, palabras o archivos generados.

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

## Estándar pedagógico

Cada clase aprobada debe enseñar el tema completo, no resumirlo. El contrato exige
objetivo, resultados verificables, tabla de temas, explicación desde primeros
principios, definiciones, glosario, diagrama interpretado, preparación, laboratorio,
ejercicios, reto con aceptación, errores síntoma→causa→solución, FAQ y fuentes
trazables. El gate completo está en
[docs/PEDAGOGICAL-STANDARD.md](docs/PEDAGOGICAL-STANDARD.md).

La referencia de profundidad es la
[Parte 6 de modern-cybersecurity-program](https://github.com/vladimiracunadev-create/modern-cybersecurity-program/tree/main/classes/parte-6-analisis-de-malware).
Se replica su calidad docente, no su contenido ni una cuota de palabras.

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
- 180 borradores, actividades y rúbricas visibles para revisión;
- contenido completo del borrador publicado en Pages, no una ficha-resumen;
- 0 clases `GUIDED` hasta completar revisión cualitativa clase por clase;
- instrucción permanente en [AGENTS.md](AGENTS.md) para impedir la regresión.

`GUIDED` no significa `EXECUTABLE`, `TESTED` u `OPERABLE`; tampoco se concede por
generación automática. El estado actual y los conteos viven en [STATUS.md](STATUS.md).

## Validación local

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

## Estructura

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

## Fuentes

La línea base y la fase 3 usan fuentes oficiales o primarias y registran fecha,
autoridad, estado y propósito en [sources/baseline.json](sources/baseline.json) y
[sources/phase3.json](sources/phase3.json). Las afirmaciones temporales se revisan
antes de publicarse.

## Publicación

La identidad, About, topics, gates y URL de Pages están definidos en
[docs/PUBLICATION-PLAN.md](docs/PUBLICATION-PLAN.md). El sitio se genera íntegramente
desde el manifiesto. El workflow remoto y la respuesta HTTPS del
[portal público](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/)
fueron verificados el 30 de septiembre de 2026.

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
