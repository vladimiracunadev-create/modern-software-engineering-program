"""Validate the "Casos de estudio" surface (see casos/GUIDE.md).

Always checked: the registered cases exist, group pages list every case, every case carries the exact
navigation, relative links resolve. Checked only for a finished case (no skeleton marker): section schema,
minimum length, figures, alt text without brackets, links to real classes and public sources.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_cases import case_nav, group_markdown  # noqa: E402
from cases_data import CASES, KINDS, SKELETON_MARKER, case_path, cases_of  # noqa: E402

COMMON_HEAD = [
    "Ficha histórica",
    "Contexto y problema",
    "Mercado, usuarios y casos de uso",
    "Funcionalidad de principio a fin",
    "Negocio y economía",
    "Arquitectura y esquemas",
    "Casos especiales y cómo",
    "Línea de tiempo",
]
FAILURE_ONLY = ["Qué falló en cada instancia", "Causa raíz y factores", "Mejoras que debieron hacerse"]
COMMON_TAIL = ["Vínculo con el curso", "Qué no generalizar", "Fuentes públicas verificadas"]
MIN_WORDS = 2000
MIN_CASES_PER_KIND = 8
MIN_FIGURES = 2
MIN_CLASS_LINKS = 5
MIN_SOURCES = 5

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE = re.compile(r"!\[([^\n]*?)\]\(([^)\s]+)(?:\s+\"([^\"]*)\")?\)")
CLASS_LINK = re.compile(r"\]\((?:\.\./)+classes/part-\d\d-[^/]+/se-(\d{3})-[^/]+/README\.md\)")


def required_headings(kind: str) -> list[str]:
    return COMMON_HEAD + (FAILURE_ONLY if kind == "fallo" else []) + COMMON_TAIL


def check_links(path: Path, text: str, failures: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    for target in LINK.findall(text) + [m[1] for m in IMAGE.findall(text)]:
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target):
            continue
        clean = unquote(target.split("#", 1)[0])
        if clean and not (path.parent / clean).resolve().exists():
            failures.append(f"{rel}: broken link -> {target}")


def check_finished(case: dict[str, str], text: str, failures: list[str]) -> None:
    rel = case_path(case)
    headings = re.findall(r"^## (.+)$", text, re.MULTILINE)
    wanted = required_headings(case["kind"])
    if len(headings) != len(wanted) or any(not h.startswith(w) for h, w in zip(headings, wanted)):
        failures.append(f"{rel}: section schema differs; expected {wanted}, found {headings}")
    if len(re.findall(r"\w+", text)) < MIN_WORDS:
        failures.append(f"{rel}: a finished case needs at least {MIN_WORDS} words")
    images = IMAGE.findall(text)
    if len(images) < MIN_FIGURES:
        failures.append(f"{rel}: a finished case needs at least {MIN_FIGURES} figures, found {len(images)}")
    for alt, src, _caption in images:
        if not alt.strip() or re.search(r"[\[\]]", alt):
            failures.append(f"{rel}: figure alt text empty or with brackets -> {alt[:50]!r}")
        if alt.strip().lower().startswith("tabla"):
            failures.append(f"{rel}: figure alt text must not start with 'Tabla' -> {alt[:50]!r}")
        name = src.rsplit("/", 1)[-1]
        if not src.startswith("../figures/") or not name.startswith(case["slug"] + "-"):
            failures.append(f"{rel}: figures must be ../figures/{case['slug']}-*.svg, found {src}")
    if "Vínculo con el curso" in text:
        tail = text.split("## Vínculo con el curso", 1)[1].split("\n## ", 1)[0]
        classes = set(CLASS_LINK.findall(tail))
        if len(classes) < MIN_CLASS_LINKS:
            failures.append(f"{rel}: 'Vínculo con el curso' needs {MIN_CLASS_LINKS} distinct real class links, found {len(classes)}")
    if "Fuentes públicas verificadas" in text:
        tail = text.split("## Fuentes públicas verificadas", 1)[1].split("\n## ", 1)[0]
        urls = set(re.findall(r"\]\((https://[^)\s]+)\)", tail))
        if len(urls) < MIN_SOURCES:
            failures.append(f"{rel}: 'Fuentes públicas verificadas' needs {MIN_SOURCES} distinct https links, found {len(urls)}")


def main() -> int:
    failures: list[str] = []
    if not (ROOT / "casos/GUIDE.md").is_file():
        failures.append("casos/GUIDE.md missing")
    for kind in KINDS:
        if len(cases_of(kind)) < MIN_CASES_PER_KIND:
            failures.append(f"the registry must keep at least {MIN_CASES_PER_KIND} {kind} cases")
        group = ROOT / "casos" / kind / "README.md"
        if not group.is_file():
            failures.append(f"missing group page casos/{kind}/README.md")
            continue
        text = group.read_text(encoding="utf-8")
        if text != group_markdown(kind):
            failures.append(f"casos/{kind}/README.md is stale; run python scripts/build_cases.py")
        for case in cases_of(kind):
            if f"]({case['slug']}.md)" not in text:
                failures.append(f"casos/{kind}/README.md lacks a link to {case['slug']}")
        check_links(group, text, failures)
    unexpected = {p.relative_to(ROOT).as_posix() for p in (ROOT / "casos").glob("*/*.md")} - {
        case_path(c) for c in CASES
    } - {f"casos/{k}/README.md" for k in KINDS}
    if unexpected:
        failures.append(f"case files outside the fixed list: {sorted(unexpected)}")
    finished = 0
    for case in CASES:
        path = ROOT / case_path(case)
        if not path.is_file():
            failures.append(f"missing case file {case_path(case)}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith(f"# {case['name']}\n"):
            failures.append(f"{case_path(case)}: first line must be '# {case['name']}'")
        if text.count(case_nav(case)) != 2:
            failures.append(f"{case_path(case)}: the navigation line must appear exactly twice: {case_nav(case)}")
        check_links(path, text, failures)
        if SKELETON_MARKER in text:
            continue
        finished += 1
        check_finished(case, text, failures)
    for figure in (ROOT / "casos/figures").glob("*.svg"):
        slug_prefixes = {c["slug"] for c in CASES} | set(KINDS)
        if not any(figure.name.startswith(s + "-") for s in slug_prefixes):
            failures.append(f"casos/figures/{figure.name} does not start with a case slug")
    if failures:
        print("\n".join(failures[:80]), file=sys.stderr)
        return 1
    print(f"CASES_OK: {len(CASES)} cases ({finished} finished, {len(CASES) - finished} skeletons)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
