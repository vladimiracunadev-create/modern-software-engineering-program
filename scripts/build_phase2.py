from __future__ import annotations

import argparse
import html
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "curriculum.yaml"
SOURCE_PATH = ROOT / "sources/baseline.json"

REQUIRED_CLASS_SECTIONS = [
    "## Prerrequisitos",
    "## Problema auténtico",
    "## Objetivos observables",
    "## Mapa conceptual",
    "## Conceptos y decisiones",
    "## Ejemplo mínimo",
    "## Ejemplo profesional",
    "## Práctica guiada",
    "## Ejercicios",
    "## Fallo controlado y diagnóstico",
    "## Entorno y archivos clave",
    "## Seguridad, ética y accesibilidad",
    "## Transferencia",
    "## Evaluación y evidencia",
    "## Fuentes",
    "## Límites y siguiente paso",
]

PART_SOURCE_MAP = {
    "00": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "01": ["RISCV-ISA", "UNICODE-17", "PYTHON-3", "JVM-SE25", "LLVM-DOCS", "GSF-SCI"],
    "02": ["POSIX-2024", "WINDOWS-DOCS", "POWERSHELL-DOCS", "BASH-MANUAL", "SYSTEMD-MAN", "WSL-DOCS"],
    "03": [
        "IETF-RFC-1122", "IETF-RFC-826", "IETF-RFC-894", "IETF-RFC-1918",
        "IETF-RFC-3022", "IETF-RFC-8200", "IETF-RFC-9293", "IETF-RFC-768",
        "IETF-RFC-9000", "IETF-RFC-1034", "IETF-RFC-1035", "IETF-RFC-8499",
        "IETF-RFC-9110", "IETF-RFC-9111", "IETF-RFC-8446", "IETF-RFC-5280",
        "IETF-RFC-6455", "IETF-RFC-8305",
    ],
    "04": ["IEEE-SWEBOK-4A", "MIT-MATH-CS", "MIT-ALG-6006", "MIT-TOC-18404"],
    "05": ["IEEE-SWEBOK-4A", "PYTHON-3", "RUST-BOOK"],
    "06": ["IEEE-SWEBOK-4A", "PYTHON-3", "RUST-BOOK", "SWI-PROLOG", "REACTIVEX", "ERLANG-PROCESSES"],
    "07": ["IEEE-SWEBOK-4A", "MIT-MATH-CS", "MIT-ALG-6006", "PYTHON-3"],
    "08": ["IEEE-SWEBOK-4A", "PYTHON-3", "LSP-318", "DAP", "DEVCONTAINERS", "W3C-WCAG"],
    "09": ["IEEE-SWEBOK-4A"],
    "10": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "11": ["IEEE-SWEBOK-4A"],
    "12": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "13": ["IEEE-SWEBOK-4A", "OPENAPI-LATEST"],
    "14": ["W3C-WCAG", "ISO-25010-2023"],
    "15": ["IEEE-SWEBOK-4A"],
    "16": ["IEEE-SWEBOK-4A", "GITHUB-ACTIONS-SHA"],
    "17": ["IEEE-SWEBOK-4A"],
    "18": ["IEEE-SWEBOK-4A"],
    "19": ["W3C-WCAG", "IETF-RFC-9110"],
    "20": ["IETF-RFC-9110", "OPENAPI-LATEST"],
    "21": ["ISO-25010-2023"],
    "22": ["ISO-25010-2023", "NIST-SSDF-800-218"],
    "23": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "24": ["IEEE-SWEBOK-4A"],
    "25": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "26": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "27": ["IEEE-SWEBOK-4A", "OPENAPI-LATEST"],
    "28": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "29": ["IEEE-SWEBOK-4A", "NIST-SSDF-800-218"],
    "30": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "31": ["ISO-25010-2023"],
    "32": ["NIST-SSDF-800-218", "OWASP-ASVS"],
    "33": ["NIST-SSDF-800-218", "GITHUB-ACTIONS-SHA"],
    "34": ["NIST-SSDF-800-218", "GITHUB-ACTIONS-SHA"],
    "35": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "36": ["IEEE-SWEBOK-4A"],
    "37": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "38": ["NIST-AI-RMF", "NIST-AI-600-1", "NIST-SSDF-800-218"],
    "39": ["GITHUB-SPEC-KIT", "MCP-2026-07-28", "NIST-AI-RMF", "NIST-AI-600-1"],
}

PART_00_PATH = [
    ("Encuadrar", "Delimita sistema, producto y responsabilidad", "Mapa de fronteras"),
    ("Explicar", "Relaciona escala, coordinación y prácticas", "Cadena causal"),
    ("Sostener", "Extiende decisiones por todo el ciclo de vida", "Mapa de ciclo y handoffs"),
    ("Responder", "Examina daño, poder, apelación y reparación", "Análisis ético"),
    ("Coordinar", "Diseña autoridad e interfaces entre especialidades", "Mapa de colaboración"),
    ("Contrastar", "Separa observación, hipótesis e inferencia", "Registro de evidencia"),
    ("Especificar", "Convierte calidad en escenarios observables", "Escenarios de calidad"),
    ("Decidir", "Hace visibles restricciones, riesgos y pérdidas", "Registro de decisión"),
    ("Ampliar", "Incluye impactos humanos, sociales y ambientales", "Mapa de impactos"),
    ("Fundamentar", "Rastrea afirmaciones hasta fuentes vigentes", "Cadena de trazabilidad"),
    ("Integrar", "Reconstruye un producto real desde evidencia", "Anatomía verificable"),
    ("Proyectar", "Convierte evidencia en una ruta de aprendizaje", "Contrato profesional"),
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_generated(path: Path, content: str, check: bool, stale: list[str]) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(relative(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def repository_class_url(lesson: dict) -> str:
    return (
        "https://github.com/vladimiracunadev-create/software-engineering-learning-suite/"
        f"blob/main/{lesson['path']}/README.md"
    )


def class_navigation(part: dict, lesson: dict, previous: dict | None, following: dict | None) -> str:
    previous_link = (
        f"[← {previous['id']} — {previous['title']}]({repository_class_url(previous)})"
        if previous else "← Inicio del programa"
    )
    following_link = (
        f"[{following['id']} — {following['title']} →]({repository_class_url(following)})"
        if following else "Fin del programa →"
    )
    portal = (
        "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/"
        f"classes/{lesson['id']}.html"
    )
    return (
        f"{previous_link} · [↑ Parte {part['id']}](../README.md) · "
        "[📚 Índice completo](../../README.md) · "
        f"[🌐 Portal]({portal}) · {following_link}"
    )


def class_scaffold(
    part: dict,
    lesson: dict,
    source_ids: list[str],
    previous: dict | None,
    following: dict | None,
) -> str:
    sources = "\n".join(f"- `{source_id}` — fuente inicial; precisar uso al construir la clase." for source_id in source_ids)
    navigation = class_navigation(part, lesson, previous, following)
    return f"""# {lesson['id']} — {lesson['title']}

{navigation}

> [!WARNING]
> Estado: **PLANNED**. Este archivo es un scaffold de fase 2, no una clase terminada.

## Prerrequisitos

Pendiente de desarrollar en la fase de contenido.

## Problema auténtico

Pendiente de desarrollar en la fase de contenido.

## Objetivos observables

- Pendiente de desarrollar.

## Mapa conceptual

Pendiente de desarrollar.

## Conceptos y decisiones

Pendiente de desarrollar.

## Ejemplo mínimo

Pendiente de desarrollar. No se añadirá código ornamental cuando el objetivo sea conceptual.

## Ejemplo profesional

Pendiente de desarrollar con contexto, restricciones y evidencia.

## Práctica guiada

Pendiente de desarrollar.

## Ejercicios

1. Básico — pendiente.
2. Intermedio — pendiente.
3. Avanzado — pendiente.

## Fallo controlado y diagnóstico

Pendiente de desarrollar.

## Entorno y archivos clave

Pendiente de declarar por sistema operativo, runtime, comandos, datos y recuperación.

## Seguridad, ética y accesibilidad

Pendiente de desarrollar según los riesgos reales de la clase.

## Transferencia

Pendiente de desarrollar hacia otra tecnología, plataforma o dominio.

## Evaluación y evidencia

Pendiente de desarrollar con criterios observables y conexión al portafolio.

## Fuentes

{sources}

## Límites y siguiente paso

Este scaffold solo demuestra que la clase tiene identidad, lugar y contrato. No demuestra aprendizaje ni ejecución.

---

{navigation}
"""


def class_metadata(part: dict, lesson: dict, source_ids: list[str]) -> dict:
    return {
        "schema_version": 1,
        "id": lesson["id"],
        "title": lesson["title"],
        "stage": part["stage"],
        "part": part["id"],
        "kind": lesson["kind"],
        "owner": part["owner"],
        "estimated_hours": lesson["estimated_hours"],
        "status": lesson["status"],
        "source_ids": source_ids,
        "path": lesson["path"],
    }


def part_index(part: dict) -> str:
    rows = []
    for lesson in part["lessons"]:
        folder = Path(lesson["path"]).name
        rows.append(
            f"| {lesson['id']} | [{lesson['title']}]({folder}/README.md) · "
            f"[🌐 portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/{lesson['id']}.html) | "
            f"{lesson['kind']} | {lesson['estimated_hours']} | {lesson['status']} |"
        )
    statuses = Counter(lesson["status"] for lesson in part["lessons"])
    status_text = ", ".join(f"{count} `{status}`" for status, count in sorted(statuses.items()))
    return f"""# Parte {part['id']} — {part['title']}

- **Etapa:** {part['stage']} · {part['stage_title']}
- **Dominio técnico principal:** `{part['owner']}`
- **Estado:** {status_text}.

| ID | Clase | Tipo | Horas | Estado |
| --- | --- | --- | ---: | --- |
{chr(10).join(rows)}

[Volver al índice de clases](../README.md)
"""


def classes_index(program: dict) -> str:
    rows = []
    flat_sections = []
    for part in program["parts"]:
        start = part["lessons"][0]["id"]
        end = part["lessons"][-1]["id"]
        part_folder = Path(part["path"]).name
        rows.append(
            f"| {part['id']} | [{part['title']}]({part_folder}/README.md) | "
            f"{part['stage']} | {start}–{end} | `{part['owner']}` |"
        )
        lesson_links = []
        for lesson in part["lessons"]:
            lesson_folder = Path(lesson["path"]).name
            if lesson["status"] == "GUIDED":
                scope = "clase guiada y revisada"
            elif lesson["number"] <= 360:
                scope = "borrador no aprobado"
            else:
                scope = "scaffold planificado"
            lesson_links.append(
                f"- [{lesson['id']} — {lesson['title']}]({part_folder}/{lesson_folder}/README.md) "
                f"· [🌐 portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/classes/{lesson['id']}.html) "
                f"· `{scope}`"
            )
        flat_sections.append(
            f"## [Parte {part['id']} — {part['title']}]({part_folder}/README.md)\n\n"
            + "\n".join(lesson_links)
        )
    statuses = Counter(
        lesson["status"] for part in program["parts"] for lesson in part["lessons"]
    )
    status_text = " · ".join(f"{count} `{status}`" for status, count in sorted(statuses.items()))
    return f"""# Índice completo del currículo

480 clases · 40 partes · numeración secuencial `SE-001`–`SE-480`.

> [!WARNING]
> Estado verificable: {status_text}. Fases 3 y 4 comprenden `SE-001`–`SE-360`.
> Solo las entradas marcadas `GUIDED` han superado el gate; las demás siguen como
> **borradores no aprobados**.
> `SE-361`–`SE-480` permanecen como scaffolds. Cada enlace declara su estado.

[← Volver al README principal](../README.md) · [🌐 Abrir el portal](https://vladimiracunadev-create.github.io/software-engineering-learning-suite/) · [📐 Criterio de aprobación](../docs/PEDAGOGICAL-STANDARD.md)

## Las 40 partes

| Parte | Título | Etapa | Clases | Propietario |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

---

## Índice plano de las 480 clases

Cada título abre el `README.md` de la clase en GitHub. El enlace **portal** abre
la misma entrada en GitHub Pages. Esto permite auditar contenido y publicación
sin recorrer carpetas manualmente.

{chr(10).join(flat_sections)}

Generado desde [`../curriculum.yaml`](../curriculum.yaml); no editar a mano.
"""


def source_registry(program: dict, baseline: dict) -> dict:
    baseline_ids = {item["id"] for item in baseline["sources"]}
    entries = {}
    for part in program["parts"]:
        source_ids = PART_SOURCE_MAP[part["id"]]
        unresolved = set(source_ids) - baseline_ids
        if unresolved:
            raise ValueError(f"Unknown sources for part {part['id']}: {sorted(unresolved)}")
        for lesson in part["lessons"]:
            entries[lesson["id"]] = {
                "status": "GUIDED_BASELINE" if lesson["status"] == "GUIDED" else "SEEDED_BASELINE",
                "source_ids": source_ids,
                "note": (
                    "Fuentes base complementadas por sources/phase3.json y vinculadas en la guía."
                    if lesson["status"] == "GUIDED"
                    else "Fuentes iniciales de la parte; deben ampliarse y vincularse a afirmaciones al construir la clase."
                ),
            }
    return {
        "schema_version": 1,
        "verified_on": baseline["verified_on"],
        "class_count": len(entries),
        "classes": entries,
    }


def status_document(program: dict) -> str:
    statuses = Counter(
        lesson["status"] for part in program["parts"] for lesson in part["lessons"]
    )
    guided = statuses.get("GUIDED", 0)
    planned = statuses.get("PLANNED", 0)
    phase3 = program.get("phase_3_target", {"classes": 0, "approved": 0})
    phase4 = program.get("phase_4_target", {"classes": 0, "approved": 0})
    return f"""# Estado verificable

Este archivo es generado por `scripts/build_phase2.py`. No editar manualmente.

| Superficie | Estado actual |
| --- | --- |
| Arquitectura | fases 1 y 2 completadas; fases 3 y 4 en reconstrucción cualitativa |
| Etapas | {len(program['stages'])} especificadas |
| Partes | {program['part_count']} indexadas |
| Clases | {guided} `GUIDED`; {planned} `PLANNED` |
| Objetivo de fase 3 | {phase3['classes']} clases (`SE-001`–`SE-180`); {phase3['approved']} aprobadas contra el estándar profundo |
| Objetivo de fase 4 | {phase4['classes']} clases (`SE-181`–`SE-360`); {phase4['approved']} aprobadas contra el estándar profundo |
| Horas | {program['estimated_hours']:,} estimadas; pendientes de validación por contenido |
| Metadatos de clase | {program['class_count']} archivos generados |
| Registro bibliográfico | {program['class_count']} entradas sembradas desde fuentes base |
| Sitio | 521 páginas HTML generadas desde el manifiesto |
| Portal definitivo | catálogo navegable; borradores visibles sin presentarlos como clases aprobadas |
| Publicación | GitHub Pages activo; workflow y respuesta HTTPS verificados el 30 de septiembre de 2026 |

## Significado

Las fases 3 y 4 están abiertas contra el estándar permanente de los programas
educativos. Los borradores generados no equivalen a clases construidas.
Una clase solo avanzará a `GUIDED` tras revisión cualitativa completa, clase por clase.

La auditoría reproducible de las carencias actuales está documentada en
[`docs/PHASE3-CONTENT-AUDIT.md`](docs/PHASE3-CONTENT-AUDIT.md).
La fase 4 se audita en
[`docs/PHASE4-CONTENT-AUDIT.md`](docs/PHASE4-CONTENT-AUDIT.md).
""".replace("2,160", "2.160")


def file_index(program: dict) -> str:
    return f"""# Índice de archivos del programa

| Superficie | Ruta | Cantidad esperada |
| --- | --- | ---: |
| Manifiesto canónico | `curriculum.yaml` | 1 |
| Catálogo resumido | `catalog.json` | 1 |
| Índice general | `classes/README.md` | 1 |
| Índices de parte | `classes/part-*/README.md` | {program['part_count']} |
| Materiales de clase | `classes/part-*/se-*/README.md` | {program['class_count']} |
| Metadatos de clase | `classes/part-*/se-*/lesson.json` | {program['class_count']} |
| Fuentes por clase | `sources/class-sources.json` | {program['class_count']} entradas |
| Fuentes verificadas de fase 3 | `sources/phase3.json` | 15 partes |
| Contratos de actividad de fase 3 | `classes/part-*/se-*/activity.yaml` | 180 borradores |
| Rúbricas de fase 3 | `classes/part-*/se-*/rubric.json` | 180 borradores |
| Contratos de actividad de fase 4 | `classes/part-15..29/se-*/activity.yaml` | 180 borradores |
| Rúbricas de fase 4 | `classes/part-15..29/se-*/rubric.json` | 180 borradores |
| Páginas del sitio | `site/**/*.html` | 521 |

Todos los conteos se validan contra `curriculum.yaml`.
"""


def site_css() -> str:
    return """:root{color-scheme:light;--paper:#f6f3ec;--paper-2:#fffdf8;--ink:#142231;--muted:#596774;--navy:#102a43;--navy-2:#183f5d;--teal:#087f8c;--teal-soft:#dff1ee;--coral:#d85845;--gold:#d9a441;--line:#d8d7d0;--shadow:0 18px 50px rgba(17,42,67,.09);--max:1240px;--reading:760px;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);line-height:1.72}a{color:#086b78;text-decoration-thickness:.08em;text-underline-offset:.18em}.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:#fff;color:#111;padding:.7rem;z-index:20}.eyebrow{color:var(--coral);text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;font-weight:850}.hero{position:relative;overflow:hidden;padding:clamp(3.5rem,8vw,7.5rem) max(1rem,calc((100% - var(--max))/2));color:#fff;background:linear-gradient(122deg,var(--navy) 0%,#133852 55%,#0b5960 100%)}.hero:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:34px 34px;mask-image:linear-gradient(to left,#000,transparent 75%)}.hero>*{position:relative}.hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(3rem,7.4vw,6.7rem);font-weight:650;line-height:.94;letter-spacing:-.045em;margin:.65rem 0 1.25rem;max-width:12ch}.hero .hero-copy{max-width:710px;color:#d8e6ec;font-size:clamp(1.05rem,2vw,1.28rem)}.hero .eyebrow{color:#ffad8f}.hero-grid{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(280px,.75fr);gap:3rem;align-items:end}.hero-map{margin:0;padding:1.2rem;border:1px solid rgba(255,255,255,.18);border-radius:1.2rem;background:rgba(5,28,43,.38);backdrop-filter:blur(8px)}.hero-map figcaption{color:#b9dce0;font-size:.78rem;text-transform:uppercase;letter-spacing:.12em;margin-bottom:1rem}.hero-loop{display:grid;gap:.55rem}.hero-loop span{display:flex;align-items:center;gap:.7rem;padding:.68rem .78rem;border-radius:.65rem;background:rgba(255,255,255,.08);font-weight:750}.hero-loop span:before{content:attr(data-step);display:grid;place-items:center;width:1.65rem;height:1.65rem;border-radius:50%;background:#ffad8f;color:var(--navy);font-size:.73rem}.metrics,.stage-grid,.class-grid,.learning-principles{display:grid;gap:1rem}.metrics{grid-template-columns:repeat(4,1fr);margin-top:2.2rem}.metric{padding:1rem 0;border-top:1px solid rgba(255,255,255,.25)}.metric strong{display:block;color:#8de0d5;font-size:1.9rem}.metric span{color:#c9dbe2}main{width:min(var(--max),calc(100% - 2rem));margin:auto;padding:3.5rem 0 6rem}h1,h2,h3{text-wrap:balance}h2{font-family:Georgia,"Times New Roman",serif;font-size:clamp(2rem,4vw,3.35rem);font-weight:650;line-height:1.08;margin:4.2rem 0 1.2rem}h3{line-height:1.25}.section-intro{max-width:760px;color:var(--muted);font-size:1.08rem}.stage-grid{grid-template-columns:repeat(2,1fr)}.stage,.class-card,.notice,.lesson-toc,.callout,.learning-principle,.part-intro{background:var(--paper-2);border:1px solid var(--line);border-radius:1rem;box-shadow:var(--shadow)}.stage,.class-card,.learning-principle{padding:1.3rem}.stage h3,.class-card h3{margin:.25rem 0}.stage{border-top:4px solid var(--teal)}.learning-principles{grid-template-columns:repeat(4,1fr);counter-reset:principle}.learning-principle{counter-increment:principle}.learning-principle:before{content:"0" counter(principle);display:block;color:var(--coral);font-weight:850;letter-spacing:.1em}.learning-principle strong{display:block;margin:.35rem 0}.learning-principle p{margin:0;color:var(--muted)}.featured-path{display:grid;grid-template-columns:1.2fr .8fr;gap:1.2rem;padding:clamp(1.3rem,3vw,2.3rem);border-radius:1.2rem;color:#fff;background:linear-gradient(135deg,var(--navy),var(--navy-2));box-shadow:var(--shadow)}.featured-path h3{font-family:Georgia,"Times New Roman",serif;font-size:2rem;margin:.3rem 0}.featured-path p{color:#d9e5eb}.featured-path a{align-self:center;justify-self:end;display:inline-block;padding:.85rem 1.1rem;border-radius:.65rem;background:#fff;color:var(--navy);font-weight:800;text-decoration:none}.toolbar{display:grid;grid-template-columns:2fr 1fr;gap:1rem;position:sticky;top:0;background:rgba(246,243,236,.95);backdrop-filter:blur(10px);padding:1rem 0;z-index:5}.toolbar label{font-size:.82rem;font-weight:800;color:var(--muted)}.toolbar input,.toolbar select{display:block;width:100%;margin-top:.3rem;background:#fff;border:1px solid #b9c2c7;color:var(--ink);padding:.82rem;border-radius:.55rem;font:inherit}.class-grid{grid-template-columns:repeat(3,1fr)}.class-card{border-top:3px solid transparent}.class-card:has(.badge-guided){border-top-color:var(--teal)}.class-card h3{font-size:1.04rem}.meta{color:var(--muted);font-size:.86rem}.badge{display:inline-block;border:1px solid #b5c1c6;border-radius:999px;padding:.18rem .58rem;font-size:.72rem;font-weight:800;letter-spacing:.04em;color:var(--muted);background:#fff}.badge-guided{border-color:#67aaa4;color:#075d65;background:var(--teal-soft)}.notice{padding:1.1rem 1.25rem;border-left:5px solid var(--gold)}.notice strong{color:#8f371f}.back{display:inline-block;margin:1rem 0}.class-nav{display:grid;grid-template-columns:1fr auto auto 1fr;align-items:center;gap:.6rem;margin:1rem 0 1.5rem;padding:.7rem;border:1px solid var(--line);border-radius:.8rem;background:rgba(255,253,248,.96);box-shadow:var(--shadow)}.class-nav a,.class-nav span{padding:.45rem .55rem;text-decoration:none}.class-nav a:last-child,.class-nav span:last-child{text-align:right}.class-nav span{color:var(--muted)}.lesson-list{padding:0;list-style:none}.lesson-list li{border-bottom:1px solid var(--line);padding:.8rem 0}.lesson{max-width:var(--max)}.lesson-hero{position:relative;margin:1rem 0 1.4rem;padding:clamp(1.4rem,4vw,3rem);overflow:hidden;color:#fff;border-radius:1.25rem;background:linear-gradient(130deg,var(--navy),#12535a);box-shadow:var(--shadow)}.lesson-hero:after{content:attr(data-number);position:absolute;right:-.02em;bottom:-.35em;font-family:Georgia,serif;font-size:clamp(8rem,24vw,18rem);font-weight:700;color:rgba(255,255,255,.055);line-height:1}.lesson-hero>*{position:relative;z-index:1}.lesson-hero .eyebrow{color:#ffb195}.lesson-hero h1{font-family:Georgia,"Times New Roman",serif;font-size:clamp(2.45rem,5.4vw,4.8rem);line-height:1.02;letter-spacing:-.035em;max-width:19ch;margin:.5rem 0 1rem}.lesson-hero p{max-width:720px;color:#d9e6eb}.lesson-progress{margin:1.3rem 0 2rem}.lesson-progress__label{display:flex;justify-content:space-between;gap:1rem;color:var(--muted);font-size:.82rem;font-weight:800}.lesson-progress ol{display:grid;grid-template-columns:repeat(12,1fr);gap:.3rem;list-style:none;padding:0;margin:.55rem 0 0}.lesson-progress a,.lesson-progress span{display:block;height:.5rem;border-radius:99px;background:#d7dedf;text-indent:-9999px}.lesson-progress .is-complete{background:#82beb7}.lesson-progress .is-current{background:var(--coral);box-shadow:0 0 0 3px rgba(216,88,69,.16)}.lesson-context{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin:1.4rem 0 2rem}.context-card{padding:1rem 1.1rem;border:1px solid var(--line);border-radius:.8rem;background:var(--paper-2)}.context-card span{display:block;color:var(--coral);font-size:.72rem;font-weight:850;letter-spacing:.09em;text-transform:uppercase}.context-card strong{display:block;margin-top:.3rem}.lesson-shell{display:grid;grid-template-columns:250px minmax(0,var(--reading));gap:clamp(2rem,5vw,4.5rem);align-items:start;justify-content:center}.lesson-toc{position:sticky;top:1rem;margin:0;padding:1.1rem;border-top:5px solid var(--teal);box-shadow:none}.lesson-toc strong{display:block;margin-bottom:.7rem}.lesson-toc ol{margin:0;padding-left:1.25rem;font-size:.82rem}.lesson-toc li{margin:.25rem 0}.lesson-toc a{color:var(--muted);text-decoration:none}.lesson-toc a:hover{color:var(--teal)}.lesson-content{min-width:0}.lesson-content>p:first-child,.lesson-content>hr:first-child{display:none}.lesson-content h2{scroll-margin-top:1rem;border-top:1px solid var(--line);padding-top:2.5rem;margin-top:3.5rem}.lesson-content h2:first-of-type{border-top:0;margin-top:0}.lesson-content h3{color:var(--teal);margin-top:2rem}.lesson-content p{max-width:72ch}.lesson-content li{margin:.38rem 0}.lesson-content ul,.lesson-content ol{padding-left:1.35rem}.table-wrap{overflow-x:auto;margin:1.5rem 0;border:1px solid var(--line);border-radius:.8rem;background:#fff}.lesson-content table{border-collapse:collapse;width:100%}.lesson-content th,.lesson-content td{border-bottom:1px solid var(--line);padding:.82rem;text-align:left;vertical-align:top}.lesson-content th{background:#eaf1f1;color:var(--navy)}.lesson-content tr:last-child td{border-bottom:0}.lesson-content tbody tr:nth-child(even){background:#fbfaf6}.lesson-content pre{overflow:auto;background:#102a43;color:#e9f4f2;border:1px solid #294c65;padding:1rem;border-radius:.6rem}.lesson-content code{background:#e7eceb;padding:.12rem .3rem;border-radius:.25rem}.lesson-content pre code{background:transparent;padding:0}.callout{padding:1rem 1.2rem;border-left:5px solid var(--coral);margin:1rem 0;box-shadow:none}.callout.note,.callout.tip{border-left-color:var(--teal)}.source-link{width:min(var(--reading),100%);margin:3rem auto 1rem;padding-top:1rem;border-top:1px solid var(--line)}.source-link a{display:inline-block;padding:.75rem 1rem;border:1px solid #8da7ae;border-radius:.55rem;text-decoration:none;background:#fff}.concept-map{margin:1.7rem 0;padding:1.2rem;border:1px solid #b9d8d4;border-radius:1rem;background:linear-gradient(145deg,#eff8f5,#fffdf8);box-shadow:var(--shadow)}.concept-map figcaption{display:flex;justify-content:space-between;gap:1rem;align-items:baseline;margin-bottom:1rem}.concept-map figcaption span{color:var(--coral);font-size:.72rem;font-weight:850;letter-spacing:.1em;text-transform:uppercase}.concept-relations{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.65rem}.concept-relation{display:grid;grid-template-columns:minmax(0,1fr) auto minmax(0,1fr);align-items:center;gap:.5rem;padding:.65rem;border-radius:.65rem;background:#fff;border:1px solid #d1e4e0}.concept-node{font-weight:750;text-align:center}.concept-arrow{color:var(--coral);font-size:1.25rem;font-weight:900}.concept-map details{margin-top:1rem;color:var(--muted);font-size:.82rem}.part-intro{padding:clamp(1.2rem,3vw,2rem);border-top:5px solid var(--coral)}.part-intro p{max-width:78ch}.route{position:relative;list-style:none;padding:0;margin:2rem 0}.route:before{content:"";position:absolute;left:1.35rem;top:1rem;bottom:1rem;width:2px;background:#b6d4d1}.route li{position:relative;display:grid;grid-template-columns:2.7rem minmax(0,1fr) minmax(180px,.42fr);gap:1rem;align-items:start;padding:0 0 1.25rem}.route-number{display:grid;place-items:center;width:2.7rem;height:2.7rem;border-radius:50%;background:var(--navy);color:#fff;font-weight:850;z-index:1}.route-copy{padding:.2rem 0}.route-copy strong{display:block}.route-copy p{margin:.2rem 0;color:var(--muted)}.route-evidence{padding:.55rem .7rem;border-radius:.55rem;background:var(--teal-soft);color:#075d65;font-size:.85rem;font-weight:750}.route-block{margin:2.5rem 0 1rem;color:var(--coral);font-size:.78rem;font-weight:900;letter-spacing:.12em;text-transform:uppercase}footer{border-top:1px solid var(--line);padding:2rem;text-align:center;color:var(--muted)}@media(max-width:950px){.hero-grid,.featured-path,.lesson-shell{grid-template-columns:1fr}.hero-map{max-width:520px}.learning-principles{grid-template-columns:repeat(2,1fr)}.lesson-toc{position:static}.lesson-toc ol{columns:2}.lesson-context{grid-template-columns:1fr}.concept-relations{grid-template-columns:1fr}.route li{grid-template-columns:2.7rem minmax(0,1fr)}.route-evidence{grid-column:2}}@media(max-width:760px){.metrics,.class-grid{grid-template-columns:repeat(2,1fr)}.stage-grid{grid-template-columns:1fr}.class-nav{grid-template-columns:1fr 1fr}.lesson-progress ol{gap:.18rem}.featured-path a{justify-self:start}}@media(max-width:520px){.metrics,.class-grid,.toolbar,.learning-principles{grid-template-columns:1fr}.hero-map{display:none}.class-nav{display:grid;grid-template-columns:1fr}.class-nav a:last-child,.class-nav span:last-child{text-align:left}.lesson-toc ol{columns:1}.lesson-hero h1{font-size:2.35rem}.route li{gap:.7rem}.route-evidence{grid-column:1/-1;margin-left:3.4rem}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*:before,*:after{transition:none!important}}\n"""


def site_visual_enhancements() -> str:
    return """
::selection{background:#b9e2dc;color:#102a43}
a{transition:color .16s ease,background .16s ease,border-color .16s ease,transform .16s ease}
a:hover{color:#b44231}a:focus-visible,input:focus-visible,select:focus-visible,summary:focus-visible{outline:3px solid var(--coral);outline-offset:3px}
.stage,.class-card{transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}.stage:hover,.class-card:hover{transform:translateY(-3px);border-color:#8bb8b3;box-shadow:0 22px 55px rgba(17,42,67,.13)}
.class-nav a{border-radius:.45rem}.class-nav a:hover{background:var(--teal-soft)}
.lesson-progress ol{grid-template-columns:repeat(12,minmax(0,1fr));min-width:0}.lesson-progress li{min-width:0;overflow:hidden}.lesson-progress a,.lesson-progress span{overflow:hidden}
.context-card{min-width:0}.lesson-content>p:first-child+.callout{display:none}
.route li.route-block{display:block;margin:2.5rem 0 1rem;padding:0 0 0 4rem;color:var(--coral)}
html,body{max-width:100%;overflow-x:hidden}.lesson,.lesson-hero,.lesson-context,.lesson-shell,.lesson-content,.context-card{min-width:0;max-width:100%}
.lesson-hero h1,.lesson-hero p,.context-card strong,.notice,.class-nav a{overflow-wrap:anywhere;word-break:break-word}
@media(max-width:520px){main{width:calc(100% - 1rem);padding-top:1rem}.class-nav{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.lesson-hero{padding:1.35rem}.lesson-hero h1{font-size:clamp(2rem,10.5vw,2.35rem);line-height:1.05;text-wrap:wrap}.lesson-hero p{font-size:.98rem}.lesson-progress{max-width:100%;overflow:hidden}}
"""


def site_js() -> str:
    return """const grid=document.querySelector('#class-grid');const result=document.querySelector('#result');const search=document.querySelector('#search');const stage=document.querySelector('#stage');let classes=[];function render(){if(!grid)return;const q=(search.value||'').toLocaleLowerCase('es');const s=stage.value;const visible=classes.filter(item=>(!s||item.stage===s)&&(!q||`${item.id} ${item.title} ${item.part_title}`.toLocaleLowerCase('es').includes(q)));grid.replaceChildren(...visible.map(item=>{const article=document.createElement('article');article.className='class-card';const meta=document.createElement('div');meta.className='meta';meta.textContent=`${item.id} · Parte ${item.part} · ${item.hours} h`;const title=document.createElement('h3');const link=document.createElement('a');link.href=item.url;link.textContent=item.title;title.append(link);const badge=document.createElement('span');badge.className=`badge badge-${item.status.toLocaleLowerCase('es')}`;badge.textContent=item.status;article.append(meta,title,badge);return article;}));result.textContent=`${visible.length} clases visibles de ${classes.length}.`;}if(grid){fetch('assets/catalog.json').then(r=>{if(!r.ok)throw new Error('No se pudo cargar el catálogo');return r.json();}).then(data=>{classes=data.classes;render();}).catch(error=>{result.textContent=error.message;});search.addEventListener('input',render);stage.addEventListener('change',render);}\n"""


def site_index(program: dict) -> str:
    statuses = Counter(
        lesson["status"] for part in program["parts"] for lesson in part["lessons"]
    )
    guided = statuses.get("GUIDED", 0)
    planned = statuses.get("PLANNED", 0)
    public_drafts = sum(
        lesson["status"] == "PLANNED" and lesson["number"] <= 360
        for part in program["parts"] for lesson in part["lessons"]
    )
    stage_options = "".join(
        f'<option value="{stage["id"]}">{stage["id"]} · {html.escape(stage["title"])}</option>'
        for stage in program["stages"]
    )
    stage_cards = []
    for stage in program["stages"]:
        parts = [part for part in program["parts"] if part["stage"] == stage["id"]]
        links = " · ".join(
            f'<a href="parts/{part["id"]}.html">{part["id"]}</a>' for part in parts
        )
        stage_cards.append(
            f'<article class="stage"><span class="eyebrow">Etapa {stage["id"]}</span>'
            f'<h3>{html.escape(stage["title"])}</h3><p>{len(parts)} partes · {len(parts)*12} clases</p>'
            f'<p>{links}</p></article>'
        )
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Programa profesional de ingeniería de software: 480 clases planificadas; fases 3 y 4 publican SE-001 a SE-360 para revisión pedagógica.">
<title>Software Engineering Learning Suite</title><link rel="stylesheet" href="assets/styles.css"></head>
    <body><a class="skip" href="#content">Saltar al contenido</a><header class="hero"><div class="hero-grid"><div><p class="eyebrow">Programa profesional · aprender haciendo visible el criterio</p>
<h1>Software Engineering Learning Suite</h1><p class="hero-copy">Un recorrido conectado desde el problema hasta un producto que puede explicarse, verificarse, operarse y evolucionar responsablemente.</p></div>
<figure class="hero-map" aria-labelledby="hero-map-title"><figcaption id="hero-map-title">El ciclo de aprendizaje del programa</figcaption><div class="hero-loop"><span data-step="1">Comprender el contexto</span><span data-step="2">Modelar una decisión</span><span data-step="3">Practicar con evidencia</span><span data-step="4">Revisar, transferir y mejorar</span></div></figure></div>
<div class="metrics"><div class="metric"><strong>8</strong><span>etapas conectadas</span></div><div class="metric"><strong>40</strong><span>partes progresivas</span></div><div class="metric"><strong>{guided}</strong><span>clases revisadas</span></div><div class="metric"><strong>{planned}</strong><span>clases por desarrollar</span></div></div></header>
<main id="content"><div class="notice"><strong>Estado verificable:</strong> {guided} clases han superado el gate pedagógico; {public_drafts} borradores públicos siguen en revisión y no se presentan como terminados.</div>
<h2>Cómo se aprende aquí</h2><p class="section-intro">Cada clase comienza recuperando una decisión previa, introduce un problema profesional, explica el mecanismo, lo representa visualmente y termina con evidencia que alimenta la clase siguiente.</p><div class="learning-principles"><article class="learning-principle"><strong>Contexto antes que herramienta</strong><p>Primero se entiende el sistema, las personas y el límite de la decisión.</p></article><article class="learning-principle"><strong>Mecanismo antes que receta</strong><p>Cada práctica explica qué señal recibe, qué cambia y qué no garantiza.</p></article><article class="learning-principle"><strong>Evidencia antes que sensación</strong><p>Leer no basta: se producen artefactos que otra persona puede revisar.</p></article><article class="learning-principle"><strong>Conexión antes que acumulación</strong><p>La salida de una clase se convierte en entrada de la siguiente.</p></article></div>
<h2>Rutas desarrolladas</h2><div class="featured-path"><div><p class="eyebrow">Parte 00 · 12 clases guiadas</p><h3>Ingeniería de software como profesión</h3><p>Campus Abierto enlaza fronteras, ciclo de vida, ética, evidencia, calidad, riesgo, impacto y desarrollo profesional.</p></div><a href="parts/00.html">Comenzar la Parte 00 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 01 · 12 clases guiadas</p><h3>Computadores y representación de información</h3><p>Pulso sigue el mismo dato por bytes, Unicode, aritmética, CPU, memoria, runtime y medición reproducible.</p></div><a href="parts/01.html">Continuar con la Parte 01 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 02 · 12 clases guiadas</p><h3>Sistemas operativos, terminal y automatización base</h3><p>Faro convierte plataforma, rutas, permisos, procesos, configuración y evidencia en un diagnóstico seguro y reproducible.</p></div><a href="parts/02.html">Continuar con la Parte 02 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 03 · 12 clases guiadas</p><h3>Redes, Internet y protocolos</h3><p>Nexo sigue una petición desde el enlace local hasta DNS, transporte, TLS, HTTP, intermediarios y recuperación.</p></div><a href="parts/03.html">Continuar con la Parte 03 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 04 · 12 clases guiadas</p><h3>Pensamiento computacional y resolución de problemas</h3><p>Atlas convierte incidentes ambiguos en modelos, invariantes, algoritmos, límites y especificaciones contrastables.</p></div><a href="parts/04.html">Continuar con la Parte 04 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 05 · 12 clases guiadas</p><h3>Fundamentos de programación</h3><p>Brújula implementa Atlas como una CLI modular, probada, legible y transferible entre lenguajes.</p></div><a href="parts/05.html">Continuar con la Parte 05 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 06 · 12 clases guiadas</p><h3>Paradigmas de programación</h3><p>Prisma contrasta estado, objetos, funciones, reglas, eventos, flujos y actores mediante un contrato y pruebas comunes.</p></div><a href="parts/06.html">Continuar con la Parte 06 →</a></div>
<div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 07 · 12 clases guiadas</p><h3>Estructuras de datos y algoritmos</h3><p>Orbe relaciona operaciones e invariantes con estructuras, algoritmos, complejidad, benchmarks y perfiles reproducibles.</p></div><a href="parts/07.html">Continuar con la Parte 07 →</a></div><div class="featured-path" style="margin-top:1rem"><div><p class="eyebrow">Parte 08 · 12 clases guiadas</p><h3>Entornos, herramientas y depuración</h3><p>Lupa convierte un síntoma de Orbe en reproducción mínima, hipótesis, primera divergencia y entorno autocontenido.</p></div><a href="parts/08.html">Continuar con la Parte 08 →</a></div><h2>Ocho etapas</h2><p class="section-intro">El currículo completo conserva su arquitectura, pero solo una clase cambia de estado cuando su explicación, práctica, fuentes y publicación han sido revisadas.</p><div class="stage-grid">{''.join(stage_cards)}</div>
<h2>Explorar las 480 clases</h2><div class="toolbar"><label>Buscar por ID o título<input id="search" type="search" placeholder="Ej.: contratos, SRE, agentes"></label><label>Filtrar por etapa<select id="stage"><option value="">Todas</option>{stage_options}</select></label></div>
<p id="result" aria-live="polite">Cargando catálogo…</p><div class="class-grid" id="class-grid"></div></main>
<footer>Generado desde curriculum.yaml · Línea base {program['baseline_date']}</footer><script src="assets/app.js"></script></body></html>\n"""


def part_page(part: dict) -> str:
    items = "".join(
        f'<li><a href="../classes/{lesson["id"]}.html">{lesson["id"]} — {html.escape(lesson["title"])}</a> '
        f'<span class="badge">{lesson["status"]}</span></li>' for lesson in part["lessons"]
    )
    guided = sum(lesson["status"] == "GUIDED" for lesson in part["lessons"])
    if guided == 12:
        state = "Doce guías pedagógicas construidas."
    elif part["lessons"][-1]["number"] <= 360:
        phase = 3 if part["lessons"][-1]["number"] <= 180 else 4
        state = f"Fase {phase} en reconstrucción: doce borradores visibles, todavía sin aprobación pedagógica."
    else:
        state = "Contenido planificado para una fase posterior."
    editorial_source = ROOT / "content" / f"part-{part['id']}" / "README.md"
    editorial_content = ""
    editorial_toc = ""
    if editorial_source.is_file():
        # Publica toda parte editorial desde la misma fuente revisada que GitHub.
        try:
            from build_phase3 import markdown_to_html
        except ModuleNotFoundError:
            from scripts.build_phase3 import markdown_to_html
        editorial_markdown = editorial_source.read_text(encoding="utf-8")
        for lesson in part["lessons"]:
            editorial_markdown = editorial_markdown.replace(
                f"(../../{lesson['path']}/README.md)",
                f"(../classes/{lesson['id']}.html)",
            ).replace(
                f"(../../{lesson['path']}/)",
                f"(../classes/{lesson['id']}.html)",
            )
        editorial_markdown = re.sub(
            r"\(\.\./\.\./classes/part-(\d{2})-[^/]+/README\.md\)",
            r"(\1.html)",
            editorial_markdown,
        )
        editorial_markdown = re.sub(
            r"\(\.\./\.\./classes/part-(\d{2})-[^/]+/\)",
            r"(\1.html)",
            editorial_markdown,
        )
        editorial_markdown = editorial_markdown.replace(
            "(../../classes/README.md)", "(../index.html)"
        ).replace(
            "(../../docs/PEDAGOGICAL-STANDARD.md)",
            "(https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/docs/PEDAGOGICAL-STANDARD.md)",
        )
        editorial_content, editorial_headings = markdown_to_html(editorial_markdown)
        editorial_toc = "".join(
            f'<li><a href="#{anchor}">{html.escape(label)}</a></li>'
            for anchor, label in editorial_headings
        )
    if part["id"] == "00":
        route_items = []
        block_labels = {
            0: "Bloque 1 · comprender el objeto y su evolución",
            3: "Bloque 2 · asumir responsabilidad y colaborar",
            6: "Bloque 3 · decidir calidad, riesgo e impacto",
            9: "Bloque 4 · fundamentar, integrar y proyectar",
        }
        for index, lesson in enumerate(part["lessons"]):
            verb, connection, evidence = PART_00_PATH[index]
            if index in block_labels:
                route_items.append(f'<li class="route-block">{block_labels[index]}</li>')
            route_items.append(
                f'<li><span class="route-number">{index + 1:02}</span><div class="route-copy">'
                f'<strong><a href="../classes/{lesson["id"]}.html">{verb} · {html.escape(lesson["title"])}</a></strong>'
                f'<p>{connection}</p></div><span class="route-evidence">Evidencia: {evidence}</span></li>'
            )
        body = f"""<section class="part-intro"><p class="eyebrow">Caso conductor · Campus Abierto</p><h2>De “hacer software” a ejercer criterio profesional</h2><p>Seguirás un servicio ficticio de matrícula que combina personas, reglas, pagos, identidad y sistemas heredados. Cada clase vuelve sobre el mismo producto con una lente nueva y transforma la evidencia anterior; el recorrido no funciona como doce capítulos aislados.</p></section><div class="lesson-shell part-shell"><nav class="lesson-toc" aria-label="Contenido de la parte"><strong>En esta parte</strong><ol>{editorial_toc}</ol></nav><article class="lesson-content part-content">{editorial_content}</article></div><h2>Resumen visual del recorrido</h2><p class="section-intro">Después de la explicación completa, esta ruta permite recuperar de un vistazo la acción y la evidencia que encadena cada clase.</p><ol class="route">{''.join(route_items)}</ol>"""
    elif editorial_content:
        body = f"""<section class="part-intro"><p class="eyebrow">Parte desarrollada · contenido íntegro</p><h2>Un recorrido conectado, no una lista de clases</h2><p>La explicación, el caso conductor, la progresión y los criterios de salida publicados aquí proceden de la fuente editorial revisada de esta parte.</p></section><div class="lesson-shell part-shell"><nav class="lesson-toc" aria-label="Contenido de la parte"><strong>En esta parte</strong><ol>{editorial_toc}</ol></nav><article class="lesson-content part-content">{editorial_content}</article></div>"""
    else:
        body = f'<h2>Clases de la parte</h2><ol class="lesson-list">{items}</ol>'
    editorial_domains = {
        "00": "criterio profesional y sistemas sociotécnicos",
        "01": "computación, representación y evidencia experimental",
        "02": "sistemas operativos y automatización reproducible",
        "03": "redes, protocolos y diagnóstico extremo a extremo",
        "04": "modelado, algoritmos y resolución contrastable",
        "05": "programación, pruebas y herramientas de línea de comandos",
        "06": "paradigmas, semántica y comparación reproducible",
        "07": "estructuras, algoritmos, complejidad y medición empírica",
        "08": "entornos reproducibles, observación y diagnóstico causal",
    }
    domain = editorial_domains.get(part["id"], part["owner"])
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Parte {part['id']}: {html.escape(part['title'])}"><title>Parte {part['id']} · {html.escape(part['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><a class="skip" href="#content">Saltar al contenido</a><main id="content"><a class="back" href="../index.html">← Volver al programa</a><p class="eyebrow">Etapa {part['stage']} · Parte {part['id']}</p><h1>{html.escape(part['title'])}</h1><p class="meta">Dominio principal: {html.escape(domain)}</p><div class="notice">{state}</div>{body}</main><footer>Software Engineering Learning Suite</footer></body></html>\n"""


def class_page(
    part: dict,
    lesson: dict,
    source_ids: list[str],
    previous: dict | None,
    following: dict | None,
) -> str:
    source_list = "".join(f"<li><code>{html.escape(source_id)}</code></li>" for source_id in source_ids)
    previous_link = f'<a href="{previous["id"]}.html">← {previous["id"]}</a>' if previous else '<span>Inicio</span>'
    following_link = f'<a href="{following["id"]}.html">{following["id"]} →</a>' if following else '<span>Fin</span>'
    navigation = f'<nav class="class-nav" aria-label="Navegación entre clases">{previous_link}<a href="../parts/{part["id"]}.html">Parte {part["id"]}</a><a href="../index.html">Índice</a>{following_link}</nav>'
    lesson_index = next(
        index for index, item in enumerate(part["lessons"]) if item["id"] == lesson["id"]
    )
    progress_items = []
    for index, item in enumerate(part["lessons"]):
        state_class = "is-current" if index == lesson_index else ""
        label = f'{item["id"]}: {item["title"]}'
        if index == lesson_index:
            progress_items.append(f'<li><span class="{state_class}" aria-current="step">{html.escape(label)}</span></li>')
        else:
            progress_items.append(f'<li><a href="{item["id"]}.html" aria-label="{html.escape(label)}">{html.escape(label)}</a></li>')
    previous_title = previous["title"] if previous else "Inicio del programa"
    following_title = following["title"] if following else "Cierre del programa"
    context = f"""<div class="lesson-context" aria-label="Conexión curricular"><div class="context-card"><span>Vienes de</span><strong>{html.escape(previous_title)}</strong></div><div class="context-card"><span>Contenido previsto</span><strong>{html.escape(lesson['title'])}</strong></div><div class="context-card"><span>Conecta con</span><strong>{html.escape(following_title)}</strong></div></div>"""
    progress = f"""<nav class="lesson-progress" aria-label="Posición dentro de la parte"><div class="lesson-progress__label"><span>Parte {part['id']}</span><span>Clase {lesson_index + 1} de {len(part['lessons'])}</span></div><ol>{''.join(progress_items)}</ol></nav>"""
    kind_label = {"class": "Clase", "studio": "Taller", "project": "Proyecto"}.get(
        lesson["kind"], lesson["kind"].capitalize()
    )
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Contenido planificado {lesson['id']}: {html.escape(lesson['title'])}"><title>{lesson['id']} · {html.escape(lesson['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><a class="skip" href="#content">Saltar al contenido</a><main class="lesson" id="content">{navigation}<header class="lesson-hero" data-number="{lesson_index + 1:02}"><p class="eyebrow">Planificada · {lesson['id']} · {html.escape(kind_label)}</p><h1>{html.escape(lesson['title'])}</h1><p>Esta posición curricular está definida, pero su desarrollo pedagógico todavía no ha superado el gate de aprobación.</p></header>{progress}<div class="notice"><strong>PLANNED:</strong> scaffold navegable; esta clase aún no contiene desarrollo pedagógico.</div>{context}<div class="lesson-shell"><nav class="lesson-toc" aria-label="Contenido previsto"><strong>En esta ficha</strong><ol><li><a href="#contrato-previsto">Contrato previsto</a></li><li><a href="#fuentes-iniciales">Fuentes iniciales</a></li></ol></nav><article class="lesson-content"><h2 id="contrato-previsto">Contrato previsto</h2><p>Problema, objetivos, conceptos, ejemplos, práctica, tres ejercicios, fallo controlado, entorno, transferencia, evaluación, evidencia y límites.</p><h2 id="fuentes-iniciales">Fuentes iniciales</h2><ul>{source_list}</ul><p>Se ampliarán y vincularán a afirmaciones cuando la clase sea construida.</p></article></div>{navigation}</main><footer>Software Engineering Learning Suite</footer></body></html>\n"""


def validate_scaffold(path: Path, lesson: dict, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing scaffold: {relative(path)}")
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"# {lesson['id']} — {lesson['title']}"):
        failures.append(f"identity drift: {relative(path)}")
    if "## Ficha" in text or "| Campo | Valor |" in text:
        failures.append(f"forbidden ficha metadata in {relative(path)}")
    missing = [section for section in REQUIRED_CLASS_SECTIONS if section not in text]
    if missing:
        failures.append(f"contract sections missing in {relative(path)}: {missing}")


def build(check: bool) -> tuple[list[str], list[str]]:
    program = load_json(PROGRAM_PATH)
    baseline = load_json(SOURCE_PATH)
    sources = source_registry(program, baseline)
    stale: list[str] = []
    failures: list[str] = []

    write_generated(ROOT / "sources/class-sources.json", dump_json(sources), check, stale)
    write_generated(ROOT / "classes/README.md", classes_index(program), check, stale)

    web_catalog = {"generated_on": program["baseline_date"], "classes": []}
    flat_lessons = [lesson for part in program["parts"] for lesson in part["lessons"]]
    neighbors = {
        lesson["id"]: (
            flat_lessons[index - 1] if index else None,
            flat_lessons[index + 1] if index + 1 < len(flat_lessons) else None,
        )
        for index, lesson in enumerate(flat_lessons)
    }
    for part in program["parts"]:
        part_dir = ROOT / part["path"]
        editorial_part = ROOT / "content" / f"part-{part['id']}" / "README.md"
        if editorial_part.is_file():
            part_markdown = editorial_part.read_text(encoding="utf-8").replace(
                "(../../classes/",
                "(https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/",
            ).replace(
                "(../../docs/",
                "(https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/docs/",
            )
        else:
            part_markdown = part_index(part)
        write_generated(part_dir / "README.md", part_markdown, check, stale)
        source_ids = PART_SOURCE_MAP[part["id"]]
        write_generated(ROOT / "site/parts" / f"{part['id']}.html", part_page(part), check, stale)
        for lesson in part["lessons"]:
            previous, following = neighbors[lesson["id"]]
            lesson_dir = ROOT / lesson["path"]
            scaffold_path = lesson_dir / "README.md"
            if check:
                validate_scaffold(scaffold_path, lesson, failures)
            elif lesson["number"] > 360:
                write_generated(
                    scaffold_path,
                    class_scaffold(part, lesson, source_ids, previous, following),
                    check,
                    stale,
                )
            write_generated(
                lesson_dir / "lesson.json",
                dump_json(class_metadata(part, lesson, source_ids)),
                check,
                stale,
            )
            generated_target = program.get("phase_4_target", {}).get("last_class", "SE-180")
            generated_number = int(generated_target.split("-")[1])
            if lesson["status"] == "PLANNED" and lesson["number"] > generated_number:
                write_generated(
                    ROOT / "site/classes" / f"{lesson['id']}.html",
                    class_page(part, lesson, source_ids, previous, following),
                    check,
                    stale,
                )
            web_catalog["classes"].append({
                "id": lesson["id"],
                "title": lesson["title"],
                "part": part["id"],
                "part_title": part["title"],
                "stage": part["stage"],
                "kind": lesson["kind"],
                "hours": lesson["estimated_hours"],
                "status": lesson["status"],
                "phase": 3 if lesson["number"] <= 180 else 4 if lesson["number"] <= 360 else "futura",
                "url": f"classes/{lesson['id']}.html",
            })

    write_generated(ROOT / "site/index.html", site_index(program), check, stale)
    write_generated(ROOT / "site/assets/styles.css", site_css() + site_visual_enhancements(), check, stale)
    write_generated(ROOT / "site/assets/app.js", site_js(), check, stale)
    write_generated(ROOT / "site/assets/catalog.json", dump_json(web_catalog), check, stale)
    for schema_name in ("curriculum.schema.json", "activity.schema.json", "rubric.schema.json"):
        schema_content = (ROOT / "schemas" / schema_name).read_text(encoding="utf-8")
        write_generated(ROOT / "site/schemas" / schema_name, schema_content, check, stale)
    write_generated(ROOT / "site/.nojekyll", "", check, stale)
    write_generated(ROOT / "STATUS.md", status_document(program), check, stale)
    write_generated(ROOT / "FILE_INDEX.md", file_index(program), check, stale)
    return stale, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale, failures = build(args.check)
    if stale or failures:
        for message in (stale[:20] + failures[:20]):
            print(message, file=sys.stderr)
        if len(stale) + len(failures) > 40:
            print(f"... {len(stale) + len(failures) - 40} additional failures", file=sys.stderr)
        return 1
    action = "PHASE2_CHECK_OK" if args.check else "PHASE2_BUILD_OK"
    print(f"{action}: 40 parts, 480 class records, phase-aware site")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
