from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


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
    if len(pages) != 521:
        failures.append(f"expected 521 HTML pages, found {len(pages)}")
    for page in pages:
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        name = page.relative_to(SITE).as_posix()
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
    if len(catalog.get("classes", [])) != 480:
        failures.append("site catalog does not contain 480 classes")
    for number in range(1, 181):
        draft = (SITE / "classes" / f"SE-{number:03d}.html").read_text(encoding="utf-8")
        for marker in ("PLANNED · EN REVISIÓN", "Problema auténtico", "Ejercicios", "Fuentes"):
            if marker not in draft:
                failures.append(f"phase 3 page lacks published draft section: SE-{number:03d} -> {marker}")
    if failures:
        print("\n".join(failures[:100]), file=sys.stderr)
        return 1
    print(f"SITE_OK: {len(pages)} pages, {len(catalog['classes'])} classes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
