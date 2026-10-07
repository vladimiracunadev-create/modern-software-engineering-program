from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    ".github/repository-metadata.json",
    "STATUS.md",
    "ROADMAP.md",
    "LICENSE",
    "LICENSE-CONTENT.md",
    "NOTICE",
    "THIRD_PARTY_NOTICES.md",
    "ASSET_LICENSES.md",
    "DATA_LICENSES.md",
    "LICENSING_AUDIT.md",
    "TRADEMARKS.md",
    "catalog.json",
    "curriculum.yaml",
    "FILE_INDEX.md",
    "classes/README.md",
    "roles/README.md",
    "manifest/repositories.json",
    "docs/PROGRAM-ARCHITECTURE.md",
    "docs/PEDAGOGICAL-STANDARD.md",
    "docs/MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md",
    "docs/PHASE3-CONTENT-AUDIT.md",
    "docs/PROGRAM-COVERAGE-AUDIT-2026-10-04.md",
    "docs/PROGRAM-COVERAGE-AUDIT-2026-10-06.md",
    "docs/COVERAGE-MATRIX.md",
    "docs/REPOSITORY-BOUNDARIES.md",
    "docs/PUBLICATION-PLAN.md",
    "docs/LICENSING_HISTORY.md",
    "docs/WORKFLOW-ARCHITECTURE.md",
    "docs/adr/ADR-002-expand-to-480-class-program.md",
    "docs/adr/ADR-003-reconcile-480-baseline-with-progressive-expansion.md",
    "docs/ARCHITECTURE.md",
    "docs/INTEGRATION-CONTRACT.md",
    "docs/SOURCES.md",
    "sources/baseline.json",
    "sources/class-sources.json",
    "sources/phase3.json",
    "schemas/curriculum.schema.json",
    "schemas/activity.schema.json",
    "schemas/rubric.schema.json",
    "matrices/COMPETENCY-MAP.md",
    "projects/capstone.md",
    "blueprints/reference-product/README.md",
    "blueprints/reference-product/api/openapi.yaml",
    "assessments/rubric.md",
    "portal/index.html",
    "portal/styles.css",
    "portal/app.js",
    "site/index.html",
    "site/assets/catalog.json",
    "scripts/build_phase2.py",
    "scripts/build_phase3.py",
    "scripts/validate_class_contracts.py",
    "scripts/validate_encoding.py",
    "scripts/validate_licensing.py",
    "scripts/validate_site.py",
    "scripts/validate_phase3.py",
]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FULL_SHA = re.compile(r"^[0-9a-f]{40}$")
ALLOWED_OWNERS = {
    "polyglot-programming-labs",
    "database-systems-labs",
    "framework-ecosystems-labs",
    "suite",
}


def read_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def validate_required() -> None:
    missing = [item for item in REQUIRED if not (ROOT / item).exists()]
    if missing:
        raise AssertionError(f"Missing required files: {missing}")


def validate_manifest() -> None:
    payload = read_json("manifest/repositories.json")
    repositories = payload["repositories"]
    names = [item["name"] for item in repositories]
    expected = {
        "polyglot-programming-labs",
        "database-systems-labs",
        "framework-ecosystems-labs",
        "modern-software-engineering-program",
    }
    if set(names) != expected or len(names) != len(set(names)):
        raise AssertionError("Repository manifest does not match the four-part suite")


def validate_program_blueprint() -> None:
    payload = read_json("curriculum.yaml")
    catalog = read_json("catalog.json")
    if payload["part_count"] != 40 or len(payload["parts"]) != 40:
        raise AssertionError("Program blueprint must contain exactly 40 parts")
    if len(payload["stages"]) != 8:
        raise AssertionError("Program blueprint must contain exactly 8 stages")
    expected_part_ids = [f"{number:02d}" for number in range(40)]
    part_ids = [part["id"] for part in payload["parts"]]
    if part_ids != expected_part_ids:
        raise AssertionError(f"Expected part IDs 00 through 39, found {part_ids}")

    lessons = [lesson for part in payload["parts"] for lesson in part["lessons"]]
    if len(lessons) != 480 or payload["class_count"] != 480:
        raise AssertionError("Program blueprint must contain exactly 480 classes")
    expected_ids = [f"SE-{number:03d}" for number in range(1, 481)]
    ids = [lesson["id"] for lesson in lessons]
    if ids != expected_ids or len(ids) != len(set(ids)):
        raise AssertionError("Class IDs must be unique and sequential from SE-001 to SE-480")
    titles = [lesson["title"].strip().casefold() for lesson in lessons]
    if len(titles) != len(set(titles)):
        raise AssertionError("Class titles must be unique")
    if any(len(part["lessons"]) != 12 for part in payload["parts"]):
        raise AssertionError("Each part must contain exactly 12 classes")
    if any(part["owner"] not in ALLOWED_OWNERS for part in payload["parts"]):
        raise AssertionError("Every part must use a declared repository owner")
    for part in payload["parts"]:
        kinds = [lesson["kind"] for lesson in part["lessons"]]
        if kinds != ["class"] * 10 + ["studio", "project"]:
            raise AssertionError(f"Part {part['id']} must have ten classes, one studio and one project")
        if any("status" in lesson for lesson in part["lessons"]):
            raise AssertionError(f"Part {part['id']} leaks class workflow state into the curriculum")
    hours = sum(lesson["estimated_hours"] for lesson in lessons)
    if hours != payload["estimated_hours"]:
        raise AssertionError("Estimated hours do not match the class manifest")
    expected_catalog = {
        "stages": 8,
        "parts": 40,
        "classes": 480,
        "estimated_hours": hours,
        "phase_3_target": {
            "first_class": "SE-001",
            "last_class": "SE-180",
            "classes": 180,
        },
        "phase_4_target": {
            "first_class": "SE-181",
            "last_class": "SE-360",
            "classes": 180,
        },
    }
    for key, value in expected_catalog.items():
        if catalog.get(key) != value:
            raise AssertionError(f"catalog.json drift for {key}: {catalog.get(key)!r} != {value!r}")


def validate_legacy_curriculum() -> None:
    modules = sorted((ROOT / "curriculum").glob("[0-9][0-9]-*.md"))
    prefixes = [item.name[:2] for item in modules]
    expected = [f"{number:02d}" for number in range(17)]
    if prefixes != expected:
        raise AssertionError(f"Legacy baseline expected documents 00 through 16, found {prefixes}")


def validate_relative_links() -> None:
    failures: list[str] = []
    for markdown in ROOT.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            clean = unquote(target.split("#", 1)[0].strip("<>"))
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            if not (markdown.parent / clean).resolve().exists():
                failures.append(f"{markdown.relative_to(ROOT)} -> {target}")
    if failures:
        raise AssertionError("Broken relative links: " + "; ".join(failures))


def validate_role_guides() -> None:
    role_root = ROOT / "roles"
    guides = sorted(path for path in role_root.glob("*.md") if path.name != "README.md")
    if len(guides) != 40:
        raise AssertionError(f"Expected 40 professional role guides, found {len(guides)}")

    required_sections = (
        "## 🧭 Qué es y por qué importa",
        "## 🗓️ Un día en el puesto",
        "## ✅ Responsabilidades y límites",
        "## 🧠 Qué necesitas saber",
        "## 📚 Tu ruta en el programa",
        "## 🧪 Evidencia de portafolio",
        "## 📈 Progresión",
        "## ⚠️ Mitos frecuentes",
        "## 🚀 Siguientes pasos",
        "## 🗺️ Sistema profesional del rol",
        "## 🧱 Partes y clases asociadas",
        "## ⚖️ Decisiones y trade-offs que debes defender",
        "## 🚨 Escenario profesional:",
        "## 📊 Señales útiles y límites de las métricas",
        "## 🧩 Proyecto integrador del rol:",
        "## 📈 Dominio esperado por alcance",
        "## 🗓️ Plan de práctica 30 · 60 · 90 días",
        "## 🎤 Preguntas para revisión o entrevista",
        "## 🔗 Fuentes primarias y oficiales",
    )
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    role_index = (role_root / "README.md").read_text(encoding="utf-8")
    for guide in guides:
        text = guide.read_text(encoding="utf-8")
        missing = [section for section in required_sections if section not in text]
        if missing:
            raise AssertionError(f"Role guide {guide.name} is missing sections: {missing}")
        if len(text.split()) < 2200:
            raise AssertionError(f"Role guide is too shallow for publication: {guide.name}")
        if text.count("../classes/") < 1:
            raise AssertionError(f"Role guide has no concrete curriculum link: {guide.name}")
        if text.count("```mermaid") != 2:
            raise AssertionError(f"Role guide must contain two visual models: {guide.name}")
        if text.count("/se-") < 15:
            raise AssertionError(f"Role guide has too few associated class links: {guide.name}")
        if "style=for-the-badge" not in text:
            raise AssertionError(f"Role guide has no visual identity badges: {guide.name}")
        link = f"roles/{guide.name}"
        if link not in root_readme:
            raise AssertionError(f"Role guide is not linked from README.md: {guide.name}")
        if f"]({guide.name})" not in role_index:
            raise AssertionError(f"Role guide is not linked from roles/README.md: {guide.name}")

    readme_contract = (
        "## 🎯 Qué es esto",
        "## 📚 Pauta profesional y cuerpos de conocimiento",
        "## 🔗 Ecosistema y fronteras entre programas",
        "## 🗂️ Las 40 partes, numeradas de 00 a 39",
        "## 🧭 Rutas sugeridas por rol",
        "## ✅ Calidad y CI",
        "## 🧱 Estructura del repositorio",
        "## 🎯 Qué es y qué no es este programa",
        "## 🧭 Principios editoriales",
        "¿Te resulta útil? ⭐ Dale una estrella al repositorio.",
        '<div align="center">',
        "style=for-the-badge",
        "github/stars/vladimiracunadev-create/modern-software-engineering-program",
        "github/forks/vladimiracunadev-create/modern-software-engineering-program",
        "github/followers/vladimiracunadev-create",
        '<td valign="top" width="50%">',
        "40 guías profesionales",
        "Partes núcleo y clases asociadas por rol",
        "<!-- role-map:start -->",
    )
    missing_readme = [token for token in readme_contract if token not in root_readme]
    if missing_readme:
        raise AssertionError(f"Main README presentation contract missing: {missing_readme}")
    if "<!-- role-index-depth:start -->" not in role_index:
        raise AssertionError("Professional role index is missing its detailed visual map")


def validate_sources() -> None:
    payload = read_json("sources/baseline.json")
    sources = payload["sources"]
    ids = [source["id"] for source in sources]
    if len(sources) < 12 or len(ids) != len(set(ids)):
        raise AssertionError("Source baseline must have at least 12 unique primary sources")
    for source in sources:
        if not source["url"].startswith("https://"):
            raise AssertionError(f"Source must use HTTPS: {source['id']}")
        if not source.get("used_for"):
            raise AssertionError(f"Source must declare its purpose: {source['id']}")

    class_sources = read_json("sources/class-sources.json")
    expected_ids = {f"SE-{number:03d}" for number in range(1, 481)}
    if class_sources.get("class_count") != 480 or set(class_sources.get("classes", {})) != expected_ids:
        raise AssertionError("Class source registry must cover SE-001 through SE-480")
    for class_id, entry in class_sources["classes"].items():
        if not entry.get("source_ids") or not set(entry["source_ids"]).issubset(set(ids)):
            raise AssertionError(f"Class source registry has unresolved sources: {class_id}")

    phase3 = read_json("sources/phase3.json")
    phase3_ids = {source["id"] for source in phase3.get("sources", [])}
    if len(phase3_ids) < 20 or len(phase3.get("parts", {})) != 15:
        raise AssertionError("Phase 3 source registry must cover 15 parts with at least 20 sources")
    if any(not set(items).issubset(phase3_ids) for items in phase3["parts"].values()):
        raise AssertionError("Phase 3 source registry contains unresolved IDs")
    phase4 = read_json("sources/phase4.json")
    phase4_ids = {source["id"] for source in phase4.get("sources", [])}
    if len(phase4_ids) < 20 or len(phase4.get("parts", {})) != 15:
        raise AssertionError("Phase 4 source registry must cover 15 parts with at least 20 sources")
    if any(not set(items).issubset(phase4_ids) for items in phase4["parts"].values()):
        raise AssertionError("Phase 4 source registry contains unresolved IDs")


def validate_phase2_outputs() -> None:
    part_directories = sorted((ROOT / "classes").glob("part-*"))
    metadata = sorted((ROOT / "classes").glob("part-*/se-*/lesson.json"))
    scaffolds = sorted((ROOT / "classes").glob("part-*/se-*/README.md"))
    pages = sorted((ROOT / "site").rglob("*.html"))
    activities = sorted((ROOT / "classes").glob("part-*/se-*/activity.yaml"))
    rubrics = sorted((ROOT / "classes").glob("part-*/se-*/rubric.json"))
    if len(part_directories) != 40:
        raise AssertionError(f"Expected 40 generated part directories, found {len(part_directories)}")
    if len(metadata) != 480 or len(scaffolds) != 480:
        raise AssertionError(f"Expected 480 class metadata/scaffolds, found {len(metadata)}/{len(scaffolds)}")
    if len(pages) != 521:
        raise AssertionError(f"Expected 521 generated HTML pages, found {len(pages)}")
    if len(activities) != 360 or len(rubrics) != 360:
        raise AssertionError(f"Expected 360 phase 3-4 activities/rubrics, found {len(activities)}/{len(rubrics)}")


def validate_developed_part_guide() -> None:
    """Keep developed part overviews from collapsing into class tables."""
    program = read_json("curriculum.yaml")
    for part in program["parts"][:3]:
        source = ROOT / "content" / f"part-{part['id']}" / "README.md"
        if not source.is_file():
            raise AssertionError(f"Part {part['id']} has no editorial source")
        text = source.read_text(encoding="utf-8")
        guide_heading = "## Guía razonada clase por clase"
        summary_heading = "## Resumen operativo del recorrido"
        if guide_heading not in text or summary_heading not in text:
            raise AssertionError(f"Part {part['id']} must contain a reasoned guide followed by an operational summary")
        guide_start = text.index(guide_heading) + len(guide_heading)
        summary_start = text.index(summary_heading)
        if summary_start <= guide_start:
            raise AssertionError(f"Part {part['id']} places its operational summary before the reasoned guide")
        guide = text[guide_start:summary_start]
        matches = list(re.finditer(r"^#### (SE-\d{3}) — .+$", guide, re.MULTILINE))
        expected_ids = [lesson["id"] for lesson in part["lessons"]]
        found_ids = [match.group(1) for match in matches]
        if found_ids != expected_ids:
            raise AssertionError(f"Part {part['id']} reasoned guide covers {found_ids}, expected {expected_ids}")
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(guide)
            body = guide[match.end():end]
            paragraphs = [
                paragraph for paragraph in re.split(r"\n\s*\n", body)
                if paragraph.strip() and not paragraph.lstrip().startswith("#")
            ]
            if len(paragraphs) < 2:
                raise AssertionError(f"{match.group(1)} needs at least two explanatory paragraphs in its part guide")
            if index + 1 < len(matches) and f"`{expected_ids[index + 1]}`" not in body:
                raise AssertionError(f"{match.group(1)} must explain its connection to {expected_ids[index + 1]}")


def validate_program_roadmap() -> None:
    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    required_roadmap_tokens = (
        "## Estado verificable de partida",
        "## Resultado profesional buscado",
        "## Desarrollo previsto por parte",
        "## Ejes transversales obligatorios",
        "## Modelo de clases, laboratorios y evaluación",
        "## Proyectos integradores",
        "## Fases de implementación",
        "## Criterio de término del programa",
        "aproximadamente 500 clases",
        "HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS VERIFICAN",
        "calidad > profundidad > coherencia > cantidad",
    )
    for token in required_roadmap_tokens:
        if token not in roadmap:
            raise AssertionError(f"Program roadmap contract missing: {token}")

    part_rows = re.findall(r"^\| \d{2} · .+\(`SE-\d{3}`–`SE-\d{3}`\)", roadmap, re.MULTILINE)
    if len(part_rows) != 40:
        raise AssertionError(f"Program roadmap must define all 40 parts, found {len(part_rows)}")

    audit = (ROOT / "docs" / "PROGRAM-COVERAGE-AUDIT-2026-10-06.md").read_text(encoding="utf-8")
    if "| Área | Estado | Archivos existentes | Profundidad | Brechas | Acción |" not in audit:
        raise AssertionError("Coverage audit must contain the required diagnostic matrix")

    adr = (ROOT / "docs" / "adr" / "ADR-003-reconcile-480-baseline-with-progressive-expansion.md").read_text(encoding="utf-8")
    for token in ("SE-001`–`SE-480", "no una cuota", "no se elimina ni renumera"):
        if token not in adr:
            raise AssertionError(f"Expansion ADR guardrail missing: {token}")


def validate_master_curriculum_plan() -> None:
    """Keep the recoverable mandate complete and class-specific."""
    path = ROOT / "docs" / "MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md"
    text = path.read_text(encoding="utf-8")
    required_tokens = (
        "## Cómo recuperar el contexto",
        "## Misión preservada",
        "## Contratos de profundidad y evidencia",
        "## Cobertura obligatoria",
        "## Experiencias y proyectos que no pueden faltar",
        "## Reglas de expansión y control de cambios",
        "## Línea base verificada y brechas transversales",
        "## Plan de mejora clase por clase",
        "## Orden de ejecución y registro",
        "## Validación final obligatoria",
        "REVISAR → COMPRENDER → INVENTARIAR → CONTRASTAR → DETECTAR BRECHAS",
        "HUMANO ESPECIFICA → IA PROPONE → HERRAMIENTAS",
        "calidad > profundidad > coherencia > cantidad",
        "HECHOS / INTERPRETACIÓN / LECCIONES",
    )
    for token in required_tokens:
        if token not in text:
            raise AssertionError(f"Master curriculum plan contract missing: {token}")

    start = text.index("## Plan de mejora clase por clase")
    end = text.index("## Orden de ejecución y registro")
    class_plan = text[start:end]
    rows = re.findall(r"^- \[([ x])\] `(SE-\d{3})` — .+$", class_plan, re.MULTILINE)
    expected_ids = [f"SE-{number:03d}" for number in range(1, 481)]
    found_ids = [class_id for _, class_id in rows]
    if found_ids != expected_ids:
        raise AssertionError(
            "Master curriculum plan must cover SE-001 through SE-480 exactly once and in order"
        )
    if any(marker != "x" for marker, _ in rows[:72]):
        raise AssertionError("The first 72 developed classes must stay recorded as reviewed")
    if any(marker != " " for marker, _ in rows[72:]):
        raise AssertionError("A pending class cannot be checked without updating the plan validator")


def validate_blueprint() -> None:
    contract = (ROOT / "blueprints/reference-product/api/openapi.yaml").read_text(encoding="utf-8")
    for token in ("openapi: 3.1.0", "/students/{studentId}/progress:", "Idempotency-Key"):
        if token not in contract:
            raise AssertionError(f"Blueprint contract token missing: {token}")


def validate_portal() -> None:
    html = (ROOT / "portal/index.html").read_text(encoding="utf-8")
    for local_asset in ("styles.css", "app.js"):
        if local_asset not in html or not (ROOT / "portal" / local_asset).exists():
            raise AssertionError(f"Portal asset missing: {local_asset}")


def validate_workflows(strict: bool) -> None:
    workflows = sorted((ROOT / ".github/workflows").glob("*.yml"))
    names = {workflow.name for workflow in workflows}
    expected = {"validate.yml", "pages.yml", "security.yml"}
    if names != expected:
        raise AssertionError(f"Expected workflow set {sorted(expected)}, found {sorted(names)}")
    for workflow in workflows:
        text = workflow.read_text(encoding="utf-8")
        if "permissions:" not in text or "timeout-minutes:" not in text:
            raise AssertionError(f"Workflow lacks permissions or timeout: {workflow.name}")
        if "actions/checkout@" in text and "persist-credentials: false" not in text:
            raise AssertionError(f"Workflow persists checkout credentials: {workflow.name}")
        for match in re.finditer(r"uses:\s*[^@\s]+@([^\s#]+)", text):
            ref = match.group(1)
            if strict and not FULL_SHA.fullmatch(ref):
                raise AssertionError(f"Action is not pinned to a full SHA in {workflow.name}: {ref}")

    validate = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
    for token in ("documentation:", "markdownlint-cli2@0.23.0", "validate_licensing.py", "evidence:"):
        if token not in validate:
            raise AssertionError(f"Validation workflow is missing: {token}")

    pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
    for token in ('- "content/**"', '- "schemas/**"', "actions/configure-pages@"):
        if token not in pages:
            raise AssertionError(f"Pages workflow misses a publication dependency: {token}")

    security = (ROOT / ".github/workflows/security.yml").read_text(encoding="utf-8")
    for token in ('cron: "0 11 * * 1"', "GITLEAKS_VERSION", "bandit==1.9.4", "governance:"):
        if token not in security:
            raise AssertionError(f"Security workflow is missing: {token}")


def validate_package_policy() -> None:
    forbidden = ("package-lock.json", "yarn.lock", "bun.lock", "bun.lockb")
    found = [path.name for path in ROOT.rglob("*") if path.is_file() and path.name in forbidden]
    if found:
        raise AssertionError(f"Unsupported package-manager files: {found}")


def validate_encoding() -> None:
    # Escape sequences keep the detector from flagging its own source text.
    suspicious = (
        "\u006d\u00c3",
        "\u0069\u006e\u0066\u006f\u0072\u006d\u0061\u0063\u0069\u00c3",
        "\u00e2\u20ac\u201d",
        "\u00e2\u20ac\u201c",
        "\u00f0\u0178",
        "\u00c2\u00b7",
    )
    failures = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part.startswith(".git") for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".py", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8")
        if any(token in text for token in suspicious):
            failures.append(str(path.relative_to(ROOT)))
    if failures:
        raise AssertionError(f"Possible mojibake in: {failures}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Enable CI-grade policy checks")
    args = parser.parse_args()
    try:
        validate_required()
        validate_manifest()
        validate_program_blueprint()
        validate_legacy_curriculum()
        validate_relative_links()
        validate_role_guides()
        validate_sources()
        validate_phase2_outputs()
        validate_developed_part_guide()
        validate_program_roadmap()
        validate_master_curriculum_plan()
        validate_blueprint()
        validate_portal()
        validate_workflows(args.strict)
        validate_package_policy()
        validate_encoding()
    except (AssertionError, KeyError, json.JSONDecodeError, UnicodeDecodeError) as error:
        print(f"VALIDATION_FAILED: {error}", file=sys.stderr)
        return 1
    print("REPOSITORY_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
