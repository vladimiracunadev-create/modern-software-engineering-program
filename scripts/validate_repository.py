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
    ".github/repository-metadata.json",
    "STATUS.md",
    "ROADMAP.md",
    "PROMPT_MAESTRO.md",
    "LICENSE",
    "catalog.json",
    "curriculum.yaml",
    "FILE_INDEX.md",
    "classes/README.md",
    "manifest/repositories.json",
    "docs/PROGRAM-ARCHITECTURE.md",
    "docs/PEDAGOGICAL-STANDARD.md",
    "docs/PHASE3-CONTENT-AUDIT.md",
    "docs/COVERAGE-MATRIX.md",
    "docs/REPOSITORY-BOUNDARIES.md",
    "docs/PUBLICATION-PLAN.md",
    "docs/adr/ADR-002-expand-to-480-class-program.md",
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
        "software-engineering-learning-suite",
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
    expected_guided = {f"SE-{number:03d}" for number in range(1, 37)}
    for part in payload["parts"]:
        kinds = [lesson["kind"] for lesson in part["lessons"]]
        if kinds != ["class"] * 10 + ["studio", "project"]:
            raise AssertionError(f"Part {part['id']} must have ten classes, one studio and one project")
        for lesson in part["lessons"]:
            expected_status = "GUIDED" if lesson["id"] in expected_guided else "PLANNED"
            if lesson["status"] != expected_status:
                raise AssertionError(f"Unexpected maturity for {lesson['id']}")
    hours = sum(lesson["estimated_hours"] for lesson in lessons)
    if hours != payload["estimated_hours"]:
        raise AssertionError("Estimated hours do not match the class manifest")
    expected_catalog = {
        "stages": 8,
        "parts": 40,
        "classes": 480,
        "estimated_hours": hours,
        "class_status": {"GUIDED": 36, "PLANNED": 444},
        "phase_3_target": {
            "first_class": "SE-001",
            "last_class": "SE-180",
            "classes": 180,
            "approved": 36,
        },
        "phase_4_target": {
            "first_class": "SE-181",
            "last_class": "SE-360",
            "classes": 180,
            "approved": 0,
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
    if not workflows:
        raise AssertionError("At least one GitHub Actions workflow is required")
    for workflow in workflows:
        text = workflow.read_text(encoding="utf-8")
        if "permissions:" not in text or "timeout-minutes:" not in text:
            raise AssertionError(f"Workflow lacks permissions or timeout: {workflow.name}")
        for match in re.finditer(r"uses:\s*[^@\s]+@([^\s#]+)", text):
            ref = match.group(1)
            if strict and not FULL_SHA.fullmatch(ref):
                raise AssertionError(f"Action is not pinned to a full SHA in {workflow.name}: {ref}")


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
        validate_sources()
        validate_phase2_outputs()
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
