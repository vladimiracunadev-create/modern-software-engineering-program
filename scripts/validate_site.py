from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import program_state as ps  # noqa: E402
from cases_data import CASES  # noqa: E402

SITE = ROOT / "site"
PROGRAM_NAME = "Programa de Ingeniería de Software Moderna"
RETIRED_PROGRAM_NAME = "Software Engineering Learning Suite"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.has_main = False
        self.has_title = False
        self.language = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "html":
            self.language = attributes.get("lang") or ""
        elif tag == "main":
            self.has_main = True
        elif tag == "title":
            self.has_title = True
        for name in ("href", "src"):
            value = attributes.get(name)
            if value:
                self.links.append(value)


def main() -> int:
    failures: list[str] = []
    pages = sorted(SITE.rglob("*.html"))
    case_pages = [page for page in pages if page.relative_to(SITE).parts[0] == "casos"]
    legacy_pages = [page for page in pages if page.relative_to(SITE).parts[0] == "legacy"]
    not_found = [page for page in pages if page.relative_to(SITE).as_posix() == "404.html"]
    pages = [page for page in pages if page not in case_pages and page not in legacy_pages and page not in not_found]
    expected_pages = 1 + len(ps.developed_parts()) + ps.developed_class_count()
    if len(pages) != expected_pages:
        failures.append(f"expected {expected_pages} HTML pages, found {len(pages)}")
    migration = json.loads((ROOT / "docs" / "ID-MIGRATION.json").read_text(encoding="utf-8"))
    expected_legacy = 1 + len(migration["classes"]) + sum(1 for part in migration["parts"] if part["old"] is not None)
    if len(legacy_pages) != expected_legacy:
        failures.append(f"expected {expected_legacy} pages under site/legacy, found {len(legacy_pages)}")
    if len(not_found) != 1:
        failures.append("site/404.html is required to explain old identifiers and reserved URLs")
    for number in ps.planned_parts():
        reserved = [SITE / "parts" / f"{number:02d}.html"] + [SITE / "classes" / f"{class_id}.html" for class_id in ps.class_ids(number)]
        failures.extend(f"planned part must not have a published page: {path.relative_to(SITE)}" for path in reserved if path.exists())
    if len(case_pages) != 2 + len(CASES):
        failures.append(f"expected {2 + len(CASES)} case pages under site/casos, found {len(case_pages)}")
    pages = sorted(pages + case_pages + legacy_pages + not_found)
    for page in pages:
        page_text = page.read_text(encoding="utf-8")
        parser = LinkParser()
        parser.feed(page_text)
        name = page.relative_to(SITE).as_posix()
        if PROGRAM_NAME not in page_text:
            failures.append(f"current program name missing: {name}")
        if RETIRED_PROGRAM_NAME in page_text:
            failures.append(f"retired program name present: {name}")
        if parser.language != "es":
            failures.append(f"missing lang=es: {name}")
        if not parser.has_main or not parser.has_title:
            failures.append(f"missing main/title: {name}")
        for link in parser.links:
            parsed = urlparse(link)
            if parsed.scheme or parsed.netloc or link.startswith(("mailto:", "#")):
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            resolved = (page.parent / target).resolve()
            try:
                resolved.relative_to(SITE.resolve())
            except ValueError:
                failures.append(f"link escapes site: {name} -> {link}")
                continue
            if not resolved.exists():
                failures.append(f"broken site link: {name} -> {link}")
    catalog = json.loads((SITE / "assets/catalog.json").read_text(encoding="utf-8"))
    expected_classes = ps.developed_class_count()
    if len(catalog.get("classes", [])) != expected_classes:
        failures.append(f"site catalog does not contain {expected_classes} developed classes")
    for number in range(1, 181):
        draft = (SITE / "classes" / f"SE-{number:03d}.html").read_text(encoding="utf-8")
        for marker in ("Problema auténtico", "Ejercicios", "Fuentes"):
            if marker not in draft:
                failures.append(f"phase 3 page lacks published draft section: SE-{number:03d} -> {marker}")
        if number <= 72:
            for marker in ("Antes de empezar", "lesson-progress", "lesson-context", "concept-map"):
                if marker not in draft:
                    failures.append(f"developed page lacks pedagogical presentation: SE-{number:03d} -> {marker}")
    if failures:
        print("\n".join(failures[:100]), file=sys.stderr)
        return 1
    print(
        f"SITE_OK: {len(pages) - len(case_pages) - len(legacy_pages) - len(not_found)} pages + {len(case_pages)} case pages"
        f" + {len(legacy_pages)} legacy pages + 404, {len(catalog['classes'])} classes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
