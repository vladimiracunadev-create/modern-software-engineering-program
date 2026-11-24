#!/usr/bin/env python3
"""Genera los volúmenes PDF del programa a partir del portal ya publicado.

Cadena (sin servicios externos):

1. lee las páginas publicadas (``site/classes``, ``site/parts``, ``site/casos``,
   ``site/glosario``) y las guías Markdown de ``roles/``;
2. arma un HTML de impresión por volumen (portada, índice, partes, clases, casos,
   glosario) con enlaces internos, figuras SVG vectoriales y reglas ``@page`` con
   encabezado por parte y número de página;
3. lo imprime con Microsoft Edge / Chrome sin interfaz (``--print-to-pdf``);
4. con PyMuPDF añade marcadores (volumen > etapa > parte > clase), metadatos,
   idioma, y completa los números de página del índice (segunda pasada).

Uso::

    python scripts/build_pdf.py --out build/pdf                # todos los volúmenes
    python scripts/build_pdf.py --volumes etapa-a,glosario     # solo algunos
    python scripts/build_pdf.py --volumes libro --parts 00,01  # prueba rápida

Los PDF no se versionan en git: se publican como activos de un GitHub Release
(ver ``docs/PDF.md``). Aquí solo viven el script, la configuración y las sumas.
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PDF_DIR = ROOT / "pdf"
PROGRAM = "Programa de Ingeniería de Software Moderna"
REPO = "vladimiracunadev-create/modern-software-engineering-program"
PAGES = f"https://{REPO.split('/')[0]}.github.io/{REPO.split('/')[1]}/"
GH_BLOB = f"https://github.com/{REPO}/blob/main/"
GH_TREE = f"https://github.com/{REPO}/tree/main/"
LICENSE_LINE = "Contenido bajo CC BY-NC-SA 4.0 · código bajo la licencia del repositorio"

STAGE_SLUG = {
    "A": "fundamentos", "B": "programacion", "C": "producto", "D": "superficies",
    "E": "arquitectura", "F": "calidad-entrega", "G": "operacion-liderazgo", "H": "ia",
}
FILE_PREFIX = "ingenieria-software-moderna"


# ---------------------------------------------------------------- modelo --------
@dataclass
class Unit:
    kind: str            # part | class | case | cases-index | role | glossary | divider
    key: str             # id de ancla
    title: str
    html: str = ""
    eyebrow: str = ""
    sid: str = ""        # SE-nnn, etiqueta corta de encabezado
    part: str = ""       # número de parte
    stage: str = ""
    meta: str = ""
    base: str = ""       # ruta de origen relativa al sitio o al repositorio
    ids: set[str] = field(default_factory=set)


@dataclass
class Volume:
    slug: str
    title: str
    subtitle: str
    description: str
    units: list[Unit] = field(default_factory=list)
    stages: list[str] = field(default_factory=list)
    toc: list[tuple[str, str, str, str]] = field(default_factory=list)  # (nivel, id, etiqueta, texto)


def load_curriculum() -> dict:
    return json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))


def git(*args: str) -> str:
    try:
        return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001 - fuera de un repo git no hay procedencia
        return ""


def provenance() -> dict:
    commit = git("rev-parse", "HEAD")
    date = git("log", "-1", "--format=%cI") or dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    dirty = bool(git("status", "--porcelain", "--untracked-files=no"))
    return {"commit": commit, "short": commit[:8] if commit else "sin-git", "date": date, "dirty": dirty}


# --------------------------------------------------------------- utilidades -----
def esc(text: str) -> str:
    return html.escape(text, quote=True)


def css_str(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def strip_tags(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u26FF\u2700-\u27BF\u2B50\u2B55\uFE0F\u200D]")


def no_emoji(text: str) -> str:
    return re.sub(r"\s{2,}", " ", EMOJI.sub("", text)).strip()


def extract(page: str, tag_pattern: str) -> str:
    match = re.search(tag_pattern, page, re.S)
    return match.group(1) if match else ""


def article_of(page: str) -> str:
    match = re.search(r"<article class=\"lesson-content[^\"]*\">(.*?)</article>", page, re.S)
    if not match:
        raise ValueError("la página no contiene <article class=\"lesson-content\">")
    return match.group(1)


def strip_nav_paragraphs(body: str) -> str:
    """Quita la navegación de cabecera y pie que solo sirve en el portal."""
    body = re.sub(r"^\s*<p>←[^<]*Inicio del programa.*?</p>", "", body, count=1, flags=re.S)
    body = re.sub(r"<hr>\s*<p>←[^<]*Inicio del programa.*?</p>\s*$", "", body, flags=re.S)
    body = re.sub(r"\s*<hr>\s*$", "", body)
    return body


def demote_headings(body: str, steps: int) -> str:
    def bump(match: re.Match[str]) -> str:
        close, level = match.group(1), min(6, int(match.group(2)) + steps)
        return f"<{close}h{level}"
    return re.sub(r"<(/?)h([1-6])(?=[\s>])", bump, body)


def mark_short_blocks(body: str) -> str:
    """Los bloques de código cortos no se parten entre páginas; los largos sí."""
    def mark(match: re.Match[str]) -> str:
        block = match.group(0)
        if block.count(chr(10)) > 28:
            return block
        tag = re.match(r"<pre\b[^>]*>", block).group(0)
        new_tag = tag.replace('class="', 'class="keep ', 1) if 'class="' in tag else tag.replace("<pre", '<pre class="keep"', 1)
        return new_tag + block[len(tag):]
    return re.sub(r"<pre\b[^>]*>.*?</pre>", mark, body, flags=re.S)


def prefix_ids(body: str, key: str) -> tuple[str, set[str]]:
    ids: set[str] = set()

    def rename(match: re.Match[str]) -> str:
        new = f"{key}--{match.group(2)}"
        ids.add(new)
        return f'{match.group(1)}id="{new}"'

    body = re.sub(r'(<[a-zA-Z][^>]*?\s)id="([^"]+)"', rename, body)
    body = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{key}--{m.group(1)}"', body)
    return body, ids


# ------------------------------------------------------- resolución de enlaces ----
CLASS_REPO = re.compile(r"^classes/part-(\d\d)-[^/]+/se-(\d{3})-[^/]+(?:/.*)?$")
PART_REPO = re.compile(r"^classes/part-(\d\d)-[^/]+(?:/README\.md)?/?$")


def canonical_key(path: str) -> str | None:
    """Convierte una ruta del sitio o del repositorio en la clave de ancla del PDF."""
    path = path.lstrip("/")
    for pattern, fmt in (
        (r"^classes/(SE-\d{3})\.html$", "c-{0}"),
        (r"^parts/(\d\d)\.html$", "p-{0}"),
        (r"^casos/(exito|fallo)/index\.html$", "cases-{0}"),
        (r"^casos/(exito|fallo)/README\.md$", "cases-{0}"),
        (r"^casos/(exito|fallo)/([a-z0-9-]+)\.(?:html|md)$", "case-{0}-{1}"),
        (r"^roles/README\.md$", "roles-index"),
        (r"^roles/([a-z0-9-]+)\.md$", "role-{0}"),
        (r"^glosario/(?:README\.md|index\.html)$", "glossary"),
        (r"^glosario/(?:[0-9a-z-]+/)?([A-Za-z0-9._-]+)\.(?:html|md)$", "gl-{0}"),
    ):
        match = re.match(pattern, path)
        if match:
            return fmt.format(*match.groups())
    match = CLASS_REPO.match(path)
    if match:
        return f"c-SE-{match.group(2)}"
    match = PART_REPO.match(path)
    if match:
        return f"p-{match.group(1)}"
    return None


_GLOSSARY_PATHS: dict[str, str] = {}


def glossary_paths() -> dict[str, str]:
    """slug de entrada -> ruta publicada («a/a2a.html»)."""
    if not _GLOSSARY_PATHS:
        gdir = SITE / "glosario"
        if gdir.is_dir():
            for page in gdir.rglob("*.html"):
                if page.name != "index.html":
                    _GLOSSARY_PATHS[page.stem] = page.relative_to(gdir).as_posix()
    return _GLOSSARY_PATHS


def portal_url(key: str) -> str | None:
    if key.startswith("c-"):
        return f"{PAGES}classes/{key[2:]}.html"
    if key.startswith("p-"):
        return f"{PAGES}parts/{key[2:]}.html"
    if key.startswith("gl-"):
        path = glossary_paths().get(key[3:])
        return f"{PAGES}glosario/{path}" if path else None
    if key.startswith("cases-"):
        return f"{PAGES}casos/{key[6:]}/index.html"
    if key.startswith("case-"):
        kind, _, slug = key[5:].partition("-")
        return f"{PAGES}casos/{kind}/{slug}.html"
    return None


def rewrite_links(body: str, unit: Unit, present: set[str], all_ids: set[str], stats: dict) -> str:
    base_dir = posixpath.dirname(unit.base)

    def fix(match: re.Match[str]) -> str:
        attrs, inner = match.group(1), match.group(2)
        href_match = re.search(r'href="([^"]*)"', attrs)
        if not href_match or href_match.group(1).startswith("#"):
            return match.group(0)
        raw = html.unescape(href_match.group(1))
        target, _, fragment = raw.partition("#")
        path: str | None = None
        if target.startswith(PAGES):
            path = target[len(PAGES):]
        elif target.startswith(GH_BLOB):
            path = target[len(GH_BLOB):]
        elif target.startswith(GH_TREE):
            path = target[len(GH_TREE):]
        elif re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
            stats["external"] += 1
            return match.group(0)
        elif target:
            joined = posixpath.normpath(posixpath.join(base_dir, target))
            path = joined
        else:
            return match.group(0)
        key = canonical_key(path) if path else None
        if key and key in present:
            frag_id = f"{key}--{fragment}" if fragment else ""
            dest = frag_id if frag_id in all_ids else key
            stats["internal"] += 1
            return f'<a{attrs.replace(href_match.group(0), "href=" + chr(34) + "#" + dest + chr(34))}>{inner}</a>'
        if key and portal_url(key):
            stats["portal"] += 1
            url = portal_url(key) + (f"#{fragment}" if fragment else "")
            return f'<a{attrs.replace(href_match.group(0), "href=" + chr(34) + esc(url) + chr(34))}>{inner}</a>'
        if target.startswith(("http://", "https://")):
            stats["external"] += 1
            return match.group(0)
        repo_path = (path or "").split("?")[0]
        if not unit.base.startswith(("classes/", "parts/", "casos/")) and repo_path and (ROOT / repo_path).exists():
            # guía de rol o glosario (Markdown): el destino vive en el repositorio, no en este volumen
            stats["repo"] += 1
            kind = "tree" if (ROOT / repo_path).is_dir() else "blob"
            url = f"https://github.com/{REPO}/{kind}/main/{repo_path}" + (f"#{fragment}" if fragment else "")
            return f'<a{attrs.replace(href_match.group(0), "href=" + chr(34) + esc(url) + chr(34))}>{inner}</a>'
        stats["unwrapped"] += 1
        return inner

    return re.sub(r"<a\b([^>]*)>(.*?)</a>", fix, body, flags=re.S)


def absolutize_images(body: str, unit: Unit, stats: dict) -> str:
    base_dir = posixpath.dirname(unit.base)

    def fix(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_match = re.search(r'src="([^"]+)"', tag)
        if not src_match:
            return tag
        src = html.unescape(src_match.group(1))
        if re.match(r"^[a-z][a-z0-9+.-]*:", src, re.I):
            stats["remote_images"] += 1
            return ""  # sin red: una imagen remota no es reproducible
        rel = posixpath.normpath(posixpath.join(base_dir, src))
        target = SITE / rel if unit.base.startswith(("classes", "parts", "casos", "glosario")) else ROOT / rel
        if not target.exists():
            stats["missing_images"].append(f"{unit.key}: {src}")
            return ""
        stats["images"] += 1
        stats["image_files"].add(target.name)
        marker = f'<span class="fig-id" aria-hidden="true">fig:{target.name}</span>'
        return tag.replace(src_match.group(0), f'src="{target.resolve().as_uri()}"') + marker

    return re.sub(r"<img[^>]*>", fix, body)


BARE_SE = re.compile(r"(?<![\w/.-])SE-(\d{3})(?![\w-])")


def link_bare_references(body: str, present: set[str], stats: dict) -> str:
    """Enlaza las menciones ``SE-nnn`` que la publicación dejó como texto plano (fuera de código y enlaces)."""
    depth = {"a": 0, "code": 0, "pre": 0, "kbd": 0, "samp": 0}
    pieces: list[str] = []
    for token in re.split(r"(<[^>]+>)", body):
        if token.startswith("<"):
            tag = re.match(r"</?([a-zA-Z0-9]+)", token)
            if tag and tag.group(1).lower() in depth:
                depth[tag.group(1).lower()] += -1 if token.startswith("</") else 1
                depth[tag.group(1).lower()] = max(0, depth[tag.group(1).lower()])
            pieces.append(token)
        elif not any(depth.values()):
            def make(match: re.Match[str]) -> str:
                key = f"c-SE-{match.group(1)}"
                if key in present:
                    stats["bare_linked"] += 1
                    return f'<a href="#{key}">{match.group(0)}</a>'
                stats["bare_portal"] += 1
                return f'<a href="{PAGES}classes/SE-{match.group(1)}.html">{match.group(0)}</a>'
            pieces.append(BARE_SE.sub(make, token))
        else:
            pieces.append(token)
    return "".join(pieces)


# ---------------------------------------------------------- fuentes de contenido --
def page_title(page: str) -> str:
    return strip_tags(extract(page, r"<h1[^>]*>(.*?)</h1>"))


def load_part(part: dict) -> Unit:
    number = part["id"]
    page = (SITE / "parts" / f"{number}.html").read_text(encoding="utf-8")
    body = demote_headings(article_of(page), 2)  # h2 de la parte -> h4 bajo la apertura
    body = re.sub(r"<section class=\"part-intro\">", '<section class="part-intro">', body)
    eyebrow = strip_tags(extract(page, r'<p class="eyebrow">(.*?)</p>'))
    meta = strip_tags(extract(page, r'<p class="meta">(.*?)</p>'))
    intro = extract(page, r"(<section class=\"part-intro\">.*?</section>)")
    unit = Unit("part", f"p-{number}", part["title"], eyebrow=eyebrow or f"Etapa {part['stage']} · Parte {number}",
                part=number, stage=part["stage"], meta=meta, base=f"parts/{number}.html")
    unit.html = (demote_headings(intro, 2) if intro else "") + body
    # los títulos «SE-nnn — …» de la guía por clases enlazan a la clase (en el portal son texto)
    unit.html = re.sub(r"(<h[1-6][^>]*>)(SE-(\d{3}) — [^<]*)(</h[1-6]>)",
                       lambda m: f'{m.group(1)}<a href="../classes/SE-{m.group(3)}.html">{m.group(2)}</a>{m.group(4)}', unit.html)
    return unit


def load_class(part: dict, lesson: dict, index: int) -> Unit:
    sid = lesson["id"]
    page = (SITE / "classes" / f"{sid}.html").read_text(encoding="utf-8")
    body = mark_short_blocks(demote_headings(strip_nav_paragraphs(article_of(page)), 1))
    unit = Unit("class", f"c-{sid}", lesson["title"], sid=sid, part=part["id"], stage=part["stage"],
                eyebrow=f"Parte {part['id']} · Clase {index} de {len(part['lessons'])} · {sid}", base=f"classes/{sid}.html")
    unit.html = body
    return unit


def case_listing(kind: str) -> list[str]:
    """Slugs de los casos, en el orden del índice publicado."""
    index = SITE / "casos" / kind / "index.html"
    order = re.findall(r'href="([a-z0-9-]+)\.html"', index.read_text(encoding="utf-8")) if index.exists() else []
    seen: list[str] = []
    for slug in order:
        if slug != "index" and slug not in seen and (SITE / "casos" / kind / f"{slug}.html").exists():
            seen.append(slug)
    for page in sorted((SITE / "casos" / kind).glob("*.html")):
        if page.stem != "index" and page.stem not in seen:
            seen.append(page.stem)
    return seen


def load_case_units() -> list[Unit]:
    units: list[Unit] = []
    labels = {"exito": "Casos de éxito", "fallo": "Casos de fallo"}
    for kind in ("exito", "fallo"):
        idx = SITE / "casos" / kind / "index.html"
        if idx.exists():
            page = idx.read_text(encoding="utf-8")
            unit = Unit("cases-index", f"cases-{kind}", f"Casos de estudio · {labels[kind]}", eyebrow="Casos de estudio",
                        base=f"casos/{kind}/index.html")
            unit.html = demote_headings(strip_nav_paragraphs(article_of(page)), 1)
            units.append(unit)
        for slug in case_listing(kind):
            page = (SITE / "casos" / kind / f"{slug}.html").read_text(encoding="utf-8")
            title = page_title(page)
            lead = strip_tags(extract(page, r'<header class="lesson-hero">.*?</h1>\s*<p>(.*?)</p>'))
            eyebrow = strip_tags(extract(page, r'<p class="eyebrow">(.*?)</p>'))
            unit = Unit("case", f"case-{kind}-{slug}", re.sub(r"\s*·\s*caso de estudio$", "", title), eyebrow=eyebrow,
                        meta=lead, base=f"casos/{kind}/{slug}.html")
            unit.html = mark_short_blocks(demote_headings(strip_nav_paragraphs(article_of(page)), 1))
            units.append(unit)
    return units


def separate_blocks(text: str) -> str:
    """CommonMark deja que un título o una lista interrumpan un párrafo; python-markdown no.

    Inserta la línea en blanco que falta, sin tocar el interior de los bloques de código.
    """
    out: list[str] = []
    fenced = False
    previous = ""
    for line in text.split(chr(10)):
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
        starts_block = bool(re.match(r"^(#{1,6} |[-*+] |\d+[.)] )", line))
        previous_is_item = bool(re.match(r"^\s*([-*+]|\d+[.)]) ", previous)) or previous.startswith("  ")
        if not fenced and starts_block and previous.strip() and not previous_is_item and not previous.lstrip().startswith(("#", ">")):
            out.append("")
        elif not fenced and line.startswith("#") and re.match(r"^#{1,6} ", line) and previous.strip() and not previous.startswith("#"):
            out.append("")
        out.append(line)
        previous = line
    return chr(10).join(out)


def markdown_to_html(text: str) -> tuple[str, str]:
    import markdown  # dependencia opcional fijada en pdf/requirements.txt

    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<div align=\"center\">.*?</div>", "", text, flags=re.S)
    text = EMOJI.sub("", text)
    # tablas HTML usadas solo como maqueta en GitHub: se conserva el Markdown de cada celda, en secuencia
    text = re.sub(r"(?im)^[ \t]*</?(?:table|tbody|tr|td|div)\b[^>]*>[ \t]*$", "", text)
    text = separate_blocks(text)
    text = re.sub(r"!\[[^\]]*\]\(https?://[^)]*\)", "", text)  # insignias remotas
    text = re.sub(r"\[\s*\]\([^)]*\)", "", text)
    title_match = re.search(r"^#\s+(.+)$", text, re.M)
    title = no_emoji(title_match.group(1)) if title_match else ""
    if title_match:
        text = text[: title_match.start()] + text[title_match.end():]
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list", "def_list"])
    out = md.convert(text)
    out = re.sub(r"(<h[1-6][^>]*>)(.*?)(</h[1-6]>)", lambda m: m.group(1) + no_emoji(m.group(2)) + m.group(3), out, flags=re.S)
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return title, out


def load_role_units() -> list[Unit]:
    units: list[Unit] = []
    readme = ROOT / "roles" / "README.md"
    title, body = markdown_to_html(readme.read_text(encoding="utf-8"))
    units.append(Unit("role", "roles-index", title or "Rutas profesionales", eyebrow="Guías de rol",
                      html=mark_short_blocks(demote_headings(body, 1)), base="roles/README.md"))
    for path in sorted((ROOT / "roles").glob("*.md")):
        if path.name == "README.md":
            continue
        title, body = markdown_to_html(path.read_text(encoding="utf-8"))
        units.append(Unit("role", f"role-{path.stem}", title or path.stem, eyebrow="Guía de rol",
                          html=mark_short_blocks(demote_headings(body, 1)), base=f"roles/{path.name}"))
    return units


def load_glossary_units() -> list[Unit]:
    """Glosario: una unidad de introducción, una por letra y una por entrada (las entradas fluyen, sin página propia)."""
    gdir = SITE / "glosario"
    index = gdir / "index.html"
    if not index.exists():
        return []
    article = article_of(index.read_text(encoding="utf-8"))
    intro_paragraph = extract(article, r"^(<p>.*?</p>)")
    intro = Unit("glossary", "glossary", "Glosario del programa", eyebrow="Glosario · superficie propia, no son clases ni roles",
                 base="glosario/index.html",
                 html=intro_paragraph + "<p>Las entradas siguen el orden alfabético. Dentro del PDF, cada enlace a una clase, caso o "
                 "término salta al destino; los enlaces a material que no está en este volumen abren el portal.</p>")
    units: list[Unit] = [intro]
    for block in re.finditer(r'<section data-letter-block id="letra-([^"]+)"><h2>([^<]+)</h2><ul>(.*?)</ul></section>', article, re.S):
        letter_id, letter, items = block.group(1), block.group(2), block.group(3)
        units.append(Unit("gl-letter", f"gl-letra-{letter_id}", letter, eyebrow="Glosario", base="glosario/index.html"))
        for href, term in re.findall(r'<li[^>]*><a href="([^"]+)">(.*?)</a>', items):
            page = (gdir / href).read_text(encoding="utf-8")
            unit = Unit("gl-entry", f"gl-{Path(href).stem}", strip_tags(term), eyebrow="Glosario", base=f"glosario/{href}")
            unit.html = demote_headings(strip_nav_paragraphs(article_of(page)), 2)
            units.append(unit)
    return units


# ------------------------------------------------------------------- volúmenes ---
def build_volumes(curriculum: dict, only_parts: set[str] | None) -> dict[str, Volume]:
    parts = [p for p in curriculum["parts"] if only_parts is None or p["id"] in only_parts]
    stage_title = {s["id"]: s["title"] for s in curriculum["stages"]}
    part_units: dict[str, list[Unit]] = {}
    for part in parts:
        units = [load_part(part)]
        for i, lesson in enumerate(part["lessons"], 1):
            units.append(load_class(part, lesson, i))
        part_units[part["id"]] = units
    volumes: dict[str, Volume] = {}
    case_units = load_case_units()
    role_units = load_role_units()
    gloss_units = load_glossary_units()
    for stage in curriculum["stages"]:
        sid = stage["id"]
        members = [p for p in parts if p["stage"] == sid]
        if not members:
            continue
        vol = Volume(f"etapa-{sid.lower()}-{STAGE_SLUG[sid]}", f"Etapa {sid} · {stage['title']}",
                     f"Volumen de etapa {sid}",
                     f"Partes {members[0]['id']}–{members[-1]['id']} del programa, clase por clase, con sus figuras y laboratorios.",
                     stages=[sid])
        for part in members:
            vol.units += part_units[part["id"]]
        volumes[vol.slug] = vol
    book = Volume("libro-completo", "Libro completo",
                  "Clases, guías de rol, casos de estudio y glosario",
                  "Las ocho etapas del programa con todas sus partes y clases, las guías de rol, los casos de estudio de éxito y de fallo y el glosario.",
                  stages=[s["id"] for s in curriculum["stages"]])
    for part in parts:
        book.units += part_units[part["id"]]
    book.units += role_units + case_units + gloss_units
    volumes[book.slug] = book
    if case_units:
        volumes["casos-de-estudio"] = Volume("casos-de-estudio", "Casos de estudio", "Éxito y fallo frente a la teoría",
                                             "Los casos de plataformas que escalaron y de sistemas que fallaron, con ficha histórica, arquitectura, línea de tiempo y vínculo con las clases.",
                                             units=list(case_units))
    if gloss_units:
        volumes["glosario"] = Volume("glosario", "Glosario", "Vocabulario técnico del programa",
                                     "Definiciones del vocabulario del programa, con enlaces a las clases que lo usan.", units=list(gloss_units))
    volumes["guias-de-rol"] = Volume("guias-de-rol", "Guías de rol", "Rutas profesionales de ingeniería de software",
                                     "Las guías de los roles profesionales y su relación con las partes y clases del programa.", units=list(role_units))
    for vol in volumes.values():
        vol.toc = []
    return volumes


# --------------------------------------------------------------- composición HTML --
def process_volume(vol: Volume, stats: dict) -> None:
    present = {u.key for u in vol.units}
    all_ids: set[str] = set()
    for unit in vol.units:
        unit.html, unit.ids = prefix_ids(unit.html, unit.key)
        all_ids |= unit.ids
    for unit in vol.units:
        unit.html = rewrite_links(unit.html, unit, present, all_ids, stats)
        unit.html = link_bare_references(unit.html, present, stats)
        unit.html = absolutize_images(unit.html, unit, stats)
        unit.html = re.sub(r"<script\b.*?</script>", "", unit.html, flags=re.S)


def page_rules(vol: Volume, prov: dict) -> str:
    foot = css_str(vol.title)
    rules = [
        "@page { @top-left { content: \"%s\"; font: 7.5pt 'Segoe UI', Arial, sans-serif; color: #5a6773; vertical-align: bottom; padding-bottom: 3mm; }"
        " @bottom-left { content: \"%s\"; font: 7.5pt 'Segoe UI', Arial, sans-serif; color: #5a6773; vertical-align: top; padding-top: 4mm; }"
        " @bottom-right { content: counter(page); font: 8pt 'Segoe UI', Arial, sans-serif; color: #102a43; font-weight: 600; vertical-align: top; padding-top: 4mm; } }"
        % (css_str(PROGRAM), foot),
        "@page cover { @top-left { content: none } @bottom-left { content: none } @bottom-right { content: none } }",
    ]
    seen_parts: set[str] = set()
    for unit in vol.units:
        if unit.kind in {"part", "class"} and unit.part and unit.part not in seen_parts and unit.kind == "part":
            seen_parts.add(unit.part)
    titles = {u.part: u.title for u in vol.units if u.kind == "part"}
    for unit in vol.units:
        name = unit.key.replace("--", "-")
        if unit.kind == "part":
            rules.append('@page %s { @top-right { content: "Parte %s"; %s } }' % (name, unit.part, HDR_RIGHT))
        elif unit.kind == "class":
            head = f"Parte {unit.part} · {titles.get(unit.part, '')}"
            head = head if len(head) <= 62 else head[:59].rstrip() + "…"
            rules.append('@page %s { @top-left { content: "%s"; %s } @top-right { content: "%s"; %s } }'
                         % (name, css_str(head), HDR_LEFT, unit.sid, HDR_RIGHT))
        elif unit.kind in {"case", "cases-index"}:
            rules.append('@page %s { @top-right { content: "Casos de estudio"; %s } }' % (name, HDR_RIGHT))
        elif unit.kind == "role":
            rules.append('@page %s { @top-right { content: "Guías de rol"; %s } }' % (name, HDR_RIGHT))
        elif unit.kind == "glossary":
            rules.append('@page %s { @top-right { content: "Glosario"; %s } }' % (name, HDR_RIGHT))
    if any(u.kind in {"gl-letter", "gl-entry"} for u in vol.units):  # las entradas comparten un único nombre de página
        rules.append('@page glossary { @top-right { content: "Glosario"; %s } }' % HDR_RIGHT)
    return "\n".join(rules)


HDR_LEFT = "font: 7.5pt 'Segoe UI', Arial, sans-serif; color: #5a6773; vertical-align: bottom; padding-bottom: 3mm;"
HDR_RIGHT = "font: 700 7.5pt 'Segoe UI', Arial, sans-serif; color: #d85845; vertical-align: bottom; padding-bottom: 3mm;"


def build_toc(vol: Volume, pages: dict[str, int] | None) -> str:
    def pg(key: str) -> str:
        return f'<span class="pg">{pages.get(key, "") if pages else "0000"}</span>'

    stage_titles = vol_stage_titles()
    out: list[str] = []
    current: str | None = None
    for unit in vol.units:
        if unit.kind == "gl-entry":
            continue  # 2.700 entradas no caben en un índice: lo encabezan las letras
        if unit.kind in {"part", "class"}:
            group = f"Etapa {unit.stage} · {stage_titles.get(unit.stage, '')}" if len(vol.stages) > 1 else None
        else:
            group = {"case": "Casos de estudio", "cases-index": "Casos de estudio", "role": "Guías de rol", "glossary": "Glosario", "gl-letter": "Glosario"}[unit.kind]
            if len(vol.units) == len([u for u in vol.units if u.kind == unit.kind]) and group == vol.title:
                group = None
        if group and group != current:
            out.append(f'<li class="toc-stage">{esc(group)}</li>')
        if group:
            current = group
        if unit.kind == "part":
            out.append(f'<li class="toc-part"><a href="#{unit.key}">Parte {esc(unit.part)} — {esc(unit.title)}</a><span class="lead"></span>{pg(unit.key)}</li>')
        elif unit.kind == "class":
            out.append(f'<li class="toc-item"><span class="toc-id">{esc(unit.sid)}</span><a href="#{unit.key}">{esc(unit.title)}</a><span class="lead"></span>{pg(unit.key)}</li>')
        else:
            out.append(f'<li class="toc-item"><a href="#{unit.key}">{esc(unit.title)}</a><span class="lead"></span>{pg(unit.key)}</li>')
    return "<ol>" + "".join(out) + "</ol>"


_STAGE_TITLES: dict[str, str] = {}


def vol_stage_titles() -> dict[str, str]:
    if not _STAGE_TITLES:
        _STAGE_TITLES.update({s["id"]: s["title"] for s in load_curriculum()["stages"]})
    return _STAGE_TITLES


def counts_of(vol: Volume) -> dict[str, int]:
    return {
        "parts": sum(u.kind == "part" for u in vol.units),
        "classes": sum(u.kind == "class" for u in vol.units),
        "cases": sum(u.kind == "case" for u in vol.units),
        "roles": sum(u.kind == "role" and u.key != "roles-index" for u in vol.units),
        "glossary_pages": sum(u.kind == "glossary" for u in vol.units),
        "glossary_entries": sum(u.kind == "gl-entry" for u in vol.units),
    }


MARKER = "https://book.invalid/#"  # enlace a otro tramo del libro; se convierte en salto interno al unir los tramos


def compose_html(vol: Volume, prov: dict, css: str, pages: dict[str, int] | None, extra_facts: dict,
                 units: list[Unit] | None = None, first_page: int = 1) -> str:
    """HTML de impresión de un volumen, o de un tramo suyo (``units``); solo el primer tramo lleva portada e índice."""
    chunk = units if units is not None else vol.units
    front = units is None or (bool(units) and units[0] is vol.units[0])
    local = {u.key for u in chunk}
    counts = counts_of(vol)
    facts = []
    if counts["classes"]:
        facts += [(counts["parts"], "partes"), (counts["classes"], "clases")]
    if counts["roles"]:
        facts.append((counts["roles"], "guías de rol"))
    if counts["cases"]:
        facts.append((counts["cases"], "casos de estudio"))
    if counts["glossary_entries"]:
        facts.append((counts["glossary_entries"], "términos de glosario"))
    facts = facts[:4]
    date = prov["date"][:10]
    cover = (
        '<section class="cover"><div class="kicker">Programa profesional · español</div>'
        f"<h1>{esc(PROGRAM)}</h1>"
        f'<div class="volume">{esc(vol.title)}</div><div class="vol-desc">{esc(vol.description)}</div>'
        '<div class="facts">' + "".join(f"<div><strong>{n}</strong><span>{esc(label)}</span></div>" for n, label in facts) + "</div>"
        f'<div class="edition">Edición generada el {esc(date)} desde el commit <code>{esc(prov["short"])}</code>'
        f'{" (con cambios sin confirmar)" if prov["dirty"] else ""}<br>{esc(LICENSE_LINE)}<br>{esc(PAGES)}</div></section>'
    )
    howto = (
        '<section class="front"><h1>Cómo usar este volumen</h1>'
        f"<p>{esc(vol.title)}: {esc(vol.subtitle)}. Es la versión impresa y offline del portal publicado; el portal y el repositorio siguen siendo la fuente viva.</p>"
        "<h2>Navegación</h2><ul>"
        "<li>El panel de marcadores de tu lector PDF sigue la jerarquía del volumen, etapa, parte y clase.</li>"
        "<li>Cada entrada del índice, cada referencia <code>SE-nnn</code> y cada enlace a otra clase, caso o término de este volumen salta dentro del mismo PDF.</li>"
        "<li>Los enlaces a material que no está en este volumen abren la página equivalente del portal; los externos abren la fuente original.</li>"
        "<li>Las figuras son vectoriales: acércalas sin perder nitidez.</li></ul>"
        "<h2>Alcance y límites honestos</h2>"
        "<p>El contenido se genera tal como está publicado en el repositorio; este documento no añade revisión propia. "
        "El programa declara que sus clases están desarrolladas «a falta de revisión editorial humana independiente»; el PDF hereda esa condición. "
        "Los laboratorios y scripts enlazados viven en el repositorio y no se incluyen en el PDF.</p>"
        "<h2>Licencia y procedencia</h2>"
        f"<p>{esc(LICENSE_LINE)}. Texto completo en <a href=\"{GH_BLOB}LICENSE-CONTENT.md\">LICENSE-CONTENT.md</a>. "
        f"Generado con <code>scripts/build_pdf.py</code> a partir del commit <code>{esc(prov['short'])}</code>; las instrucciones de reproducción están en "
        f"<a href=\"{GH_BLOB}docs/PDF.md\">docs/PDF.md</a>.</p></section>"
    )
    toc = f'<section class="front toc"><h1>Contenido</h1>{build_toc(vol, pages)}</section>'
    body: list[str] = []
    for unit in chunk:
        name = unit.key.replace("--", "-")
        inner = f'<div class="body">{unit.html}</div>'
        if unit.kind == "part":
            body.append(
                f'<section class="part" id="{unit.key}" style="page:{name}"><header class="part-opener"><p class="eyebrow"><a class="self" href="#{unit.key}">{esc(unit.eyebrow)}</a></p>'
                f'<h1>{esc(unit.title)}</h1><p class="meta">{esc(unit.meta)}</p></header>{inner}</section>'
            )
        elif unit.kind == "class":
            body.append(
                f'<section class="class" id="{unit.key}" style="page:{name}"><header class="class-opener"><p class="eyebrow"><a class="self" href="#{unit.key}">{esc(unit.eyebrow)}</a></p>'
                f"<h2>{esc(unit.title)}</h2></header>{inner}</section>"
            )
        elif unit.kind == "gl-letter":
            body.append(f'<section class="gl-letter" id="{unit.key}" style="page:glossary"><h2><a class="self" href="#{unit.key}">{esc(unit.title)}</a></h2></section>')
        elif unit.kind == "gl-entry":
            body.append(f'<section class="gl-entry" id="{unit.key}" style="page:glossary"><h3 class="gl-term"><a class="self" href="#{unit.key}">{esc(unit.title)}</a></h3>'
                        f'<span class="gl-id" aria-hidden="true">gl:{esc(unit.key[3:])}</span>{inner}</section>')
        else:
            lead = f'<p class="lead-in">{esc(unit.meta)}</p>' if unit.meta else ""
            body.append(
                f'<section class="class" id="{unit.key}" style="page:{name}"><header class="class-opener"><p class="eyebrow"><a class="self" href="#{unit.key}">{esc(unit.eyebrow)}</a></p>'
                f"<h2>{esc(unit.title)}</h2>{lead}</header>{inner}</section>"
            )
    counter = f"\nhtml {{ counter-set: page {first_page - 1}; }}" if first_page > 1 else ""
    document = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        f"<title>{esc(PROGRAM)} — {esc(vol.title)}</title><style>{css}\n{page_rules(vol, prov)}{counter}</style></head><body>"
        + (cover + howto + toc if front else "") + "\n".join(body) + "</body></html>"
    )
    if len(local) < len(vol.units):  # tramo: los enlaces a unidades de otros tramos pasan por el marcador
        def reroute(match: re.Match[str]) -> str:
            target = match.group(1)
            return match.group(0) if target.split("--")[0] in local else f'href="{MARKER}{target}"'
        document = re.sub(r'href="#([^"]+)"', reroute, document)
    return document


# ------------------------------------------------------------------ navegador ----
def find_browser(explicit: str | None) -> str:
    candidates = [explicit, os.environ.get("PDF_BROWSER")]
    candidates += [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for name in ("microsoft-edge", "microsoft-edge-stable", "google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome", "msedge"):
        found = shutil.which(name)
        if found:
            candidates.append(found)
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise SystemExit("No se encontró Microsoft Edge/Chrome/Chromium; usa --browser o PDF_BROWSER (ver docs/PDF.md).")


def print_to_pdf(browser: str, html_path: Path, pdf_path: Path, timeout: int) -> None:
    profile = Path(tempfile.mkdtemp(prefix="pdf-profile-"))
    cmd = [
        browser, "--headless=new", "--disable-gpu", "--no-first-run", "--disable-extensions", "--allow-file-access-from-files",
        f"--user-data-dir={profile}", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}", html_path.as_uri(),
    ]
    try:
        subprocess.run(cmd, check=True, timeout=timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        wait_for_pdf(pdf_path, timeout)
    finally:
        shutil.rmtree(profile, ignore_errors=True)


def wait_for_pdf(pdf_path: Path, timeout: int) -> None:
    """El navegador puede devolver el control antes de terminar de escribir: espera a un PDF completo y estable."""
    deadline = time.time() + min(timeout, 900)
    last = -1
    while time.time() < deadline:
        if pdf_path.exists():
            size = pdf_path.stat().st_size
            if size > 10_000 and size == last:
                with open(pdf_path, "rb") as handle:
                    handle.seek(max(0, size - 64))
                    if b"%%EOF" in handle.read():
                        return
            last = size
        time.sleep(2)
    raise SystemExit(f"El navegador no produjo un PDF completo: {pdf_path}")


# --------------------------------------------------------------- posproceso -------
def anchor_pages(doc, keys: list[str]) -> dict[str, int]:
    """Página (1-based) de cada ancla, vía destinos con nombre del PDF."""
    names = doc.resolve_names()
    pages: dict[str, int] = {}
    for key in keys:
        dest = names.get(key)
        if dest is not None:
            pages[key] = int(dest["page"]) + 1
    return pages


def finalize(doc, out: Path, vol: Volume, prov: dict, pages: dict[str, int]) -> dict:
    """Marcadores, metadatos e idioma sobre el documento ya completo, y guardado final."""
    keys = [u.key for u in vol.units]
    missing = [k for k in keys if k not in pages]
    if missing:
        raise SystemExit(f"{vol.slug}: {len(missing)} anclas sin destino en el PDF, p. ej. {missing[:5]}")
    toc: list[list] = [[1, vol.title, 1]]
    stage_titles = vol_stage_titles()
    seen_group: str | None = None
    for unit in vol.units:
        page = pages[unit.key]
        if unit.kind in {"part", "class"}:
            if len(vol.stages) > 1 and unit.stage != seen_group:
                seen_group = unit.stage
                toc.append([2, f"Etapa {unit.stage} · {stage_titles[unit.stage]}", page])
            base = 3 if len(vol.stages) > 1 else 2
            if unit.kind == "part":
                toc.append([base, f"Parte {unit.part} · {unit.title}", page])
            else:
                toc.append([base + 1, f"{unit.sid} · {unit.title}", page])
        elif unit.kind == "gl-entry":
            continue  # las entradas no entran en los marcadores: serían 2.700 y el índice son las letras
        else:
            group = {"case": "Casos de estudio", "cases-index": "Casos de estudio", "role": "Guías de rol", "glossary": "Glosario", "gl-letter": "Glosario"}[unit.kind]
            flat = group == vol.title  # el volumen ya es el grupo: sin nivel intermedio repetido
            if seen_group != group and not flat:
                seen_group = group
                toc.append([2, group, page])
            toc.append([2 if flat else 3, unit.title, page])
    # PyMuPDF exige que el primer nivel sea 1 y que no se salte niveles
    fixed: list[list] = []
    last = 0
    for level, title, page in toc:
        level = min(level, last + 1)
        fixed.append([level, title, page])
        last = level
    doc.set_toc(fixed)
    stamp = dt.datetime.fromisoformat(prov["date"]).astimezone(dt.timezone.utc).strftime("D:%Y%m%d%H%M%SZ")
    doc.set_metadata({
        "title": f"{PROGRAM} — {vol.title}",
        "author": "Vladimir Acuña",
        "subject": vol.subtitle,
        "keywords": "ingeniería de software, curso, español, SE-001, programa profesional",
        "creator": "scripts/build_pdf.py",
        "producer": "Microsoft Edge/Chromium + PyMuPDF",
        "creationDate": stamp,
        "modDate": stamp,
    })
    cat = doc.pdf_catalog()
    doc.xref_set_key(cat, "Lang", "(es)")
    doc.xref_set_key(cat, "PageMode", "/UseOutlines")
    doc.xref_set_key(cat, "ViewerPreferences", "<</DisplayDocTitle true>>")
    doc.save(out, garbage=2, deflate=True)
    count = len(doc)
    doc.close()
    return {"pages": count, "anchors": pages}


def plan_chunks(units: list[Unit], limit: int) -> list[list[Unit]]:
    """Reparte las unidades en tramos de tamaño acotado, cortando solo entre partes o unidades sueltas.

    Un navegador imprime sin problema ~3.800 páginas de una vez, pero un libro de ~8.500 no
    termina de forma fiable: los tramos se imprimen por separado y se unen después.
    """
    groups: list[list[Unit]] = []
    for unit in units:
        if unit.kind == "class" and groups and groups[-1][0].kind in {"part", "class"}:
            groups[-1].append(unit)
        else:
            groups.append([unit])
    chunks: list[list[Unit]] = []
    size = 0
    for group in groups:
        weight = sum(len(u.html) for u in group)
        if chunks and size + weight > limit:
            chunks.append(list(group))
            size = weight
        elif chunks:
            chunks[-1] += group
            size += weight
        else:
            chunks.append(list(group))
            size = weight
    return chunks


def build_chunked(vol: Volume, chunks: list[list[Unit]], prov: dict, css: str, args, browser: str, work: Path, extra: dict):
    """Imprime cada tramo con su numeración de página y los une; devuelve el documento y la página de cada ancla."""
    import fitz

    docs: list = []
    offsets: list[int] = []
    total = 0
    for index, chunk in enumerate(chunks):
        html_path = work / f"{vol.slug}.{index:02d}.html"
        raw = work / f"{vol.slug}.{index:02d}.raw.pdf"
        html_path.write_text(compose_html(vol, prov, css, None, extra, chunk, total + 1), encoding="utf-8")
        print(f"[{vol.slug}] tramo {index + 1}/{len(chunks)}: {len(chunk)} unidades, HTML {html_path.stat().st_size / 1e6:.1f} MB", flush=True)
        print_to_pdf(browser, html_path, raw, args.timeout)
        docs.append(fitz.open(raw))
        offsets.append(total)
        total += len(docs[-1])
    names: dict[str, tuple[int, object]] = {}
    for doc, offset in zip(docs, offsets):
        for name, dest in doc.resolve_names().items():
            names[name] = (offset + int(dest["page"]), dest["to"])
    pages = {key: names[key][0] + 1 for key in (u.key for u in vol.units) if key in names}
    if args.two_pass and len(pages) == len(vol.units):  # índice con números: se vuelve a imprimir el primer tramo
        html_path = work / f"{vol.slug}.00.html"
        html_path.write_text(compose_html(vol, prov, css, pages, extra, chunks[0], 1), encoding="utf-8")
        raw = work / f"{vol.slug}.00.raw.pdf"
        print(f"[{vol.slug}] pasada 2 del primer tramo (números del índice)", flush=True)
        docs[0].close()
        print_to_pdf(browser, html_path, raw, args.timeout)
        docs[0] = fitz.open(raw)
        if len(docs[0]) != offsets[1]:
            raise SystemExit(f"{vol.slug}: el primer tramo cambió de {offsets[1]} a {len(docs[0])} páginas al añadir los números del índice")
    merged = fitz.open()
    for doc in docs:
        merged.insert_pdf(doc, links=False, annots=False)
    broken = 0
    for doc, offset in zip(docs, offsets):
        for local, page in enumerate(doc):
            target_page = merged[offset + local]
            for link in page.get_links():
                kind = link["kind"]
                if kind in (fitz.LINK_NAMED, fitz.LINK_GOTO):
                    destination, point = offset + link.get("page", -1), link.get("to")
                    if link.get("page", -1) < 0:
                        broken += 1
                        continue
                elif kind == fitz.LINK_URI and link["uri"].startswith(MARKER):
                    hit = names.get(link["uri"][len(MARKER):])
                    if hit is None:
                        broken += 1
                        continue
                    destination, point = hit
                    kind = fitz.LINK_GOTO
                else:
                    target_page.insert_link({"kind": fitz.LINK_URI, "from": link["from"], "uri": link["uri"]}) if kind == fitz.LINK_URI else None
                    continue
                target_page.insert_link({"kind": fitz.LINK_GOTO, "from": link["from"], "page": destination, "to": fitz.Point(point) if point else fitz.Point(0, 0)})
    for doc in docs:
        doc.close()
    if broken:
        raise SystemExit(f"{vol.slug}: {broken} enlaces internos sin destino al unir los tramos")
    return merged, pages


def build_volume(vol: Volume, prov: dict, args, browser: str, work: Path, extra: dict) -> dict:
    css = (PDF_DIR / "print.css").read_text(encoding="utf-8")
    name = f"{FILE_PREFIX}_{vol.slug}.pdf"
    vol = copy.deepcopy(vol)  # las unidades se comparten entre volúmenes y process_volume las reescribe
    stats = {"repo": 0, "bare_linked": 0, "bare_portal": 0, "internal": 0, "portal": 0, "external": 0, "unwrapped": 0, "images": 0, "remote_images": 0,
             "missing_images": [], "image_files": set()}
    process_volume(vol, stats)
    raw = work / f"{vol.slug}.raw.pdf"
    started = time.time()
    import fitz
    chunks = plan_chunks(vol.units, args.chunk_bytes)
    out = Path(args.out) / name
    out.parent.mkdir(parents=True, exist_ok=True)
    if len(chunks) == 1:
        html_path = work / f"{vol.slug}.html"
        html_path.write_text(compose_html(vol, prov, css, None, extra), encoding="utf-8")
        print(f"[{vol.slug}] pasada 1: {len(vol.units)} unidades, HTML {html_path.stat().st_size / 1e6:.1f} MB", flush=True)
        print_to_pdf(browser, html_path, raw, args.timeout)
        doc = fitz.open(raw)
        pages = anchor_pages(doc, [u.key for u in vol.units])
        doc.close()
        if args.two_pass and len(pages) == len(vol.units):
            html_path.write_text(compose_html(vol, prov, css, pages, extra), encoding="utf-8")
            print(f"[{vol.slug}] pasada 2 (números de página del índice)", flush=True)
            print_to_pdf(browser, html_path, raw, args.timeout)
        doc = fitz.open(raw)
        pages = anchor_pages(doc, [u.key for u in vol.units])
    else:
        doc, pages = build_chunked(vol, chunks, prov, css, args, browser, work, extra)
    result = finalize(doc, out, vol, prov, pages)
    sha = hashlib.sha256(out.read_bytes()).hexdigest()
    info = {
        "file": name, "title": vol.title, "pages": result["pages"], "bytes": out.stat().st_size, "sha256": sha,
        "counts": counts_of(vol), "links": {k: v for k, v in stats.items() if isinstance(v, int)},
        "figures": len(stats["image_files"]), "missing_images": stats["missing_images"],
        "seconds": round(time.time() - started), "commit": prov["commit"], "date": prov["date"],
        "units": [{"key": u.key, "kind": u.kind, "title": u.title, "page": result["anchors"][u.key]} for u in vol.units],
        "figure_files": sorted(stats["image_files"]),
    }
    print(f"[{vol.slug}] {info['pages']} páginas, {info['bytes'] / 1e6:.1f} MB, {info['seconds']} s, enlaces {info['links']}", flush=True)
    if not args.keep_work:
        raw.unlink(missing_ok=True)
    return info


def glossary_entries() -> int:
    inventory = ROOT / "glosario" / "INVENTARIO.md"
    if not inventory.exists():
        return 0
    text = inventory.read_text(encoding="utf-8")
    match = re.search(r"(\d[\d.]*)\s+(?:entradas|términos|conceptos)", text)
    return int(match.group(1).replace(".", "")) if match else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "build" / "pdf"), help="carpeta de salida de los PDF")
    parser.add_argument("--volumes", default="all", help="lista separada por comas (slug o prefijo) o 'all'")
    parser.add_argument("--parts", help="restringe a estas partes (p. ej. 00,01); solo para pruebas")
    parser.add_argument("--browser", help="ruta de Edge/Chrome/Chromium")
    parser.add_argument("--timeout", type=int, default=7200, help="segundos máximos por impresión")
    parser.add_argument("--one-pass", dest="two_pass", action="store_false", help="omite la segunda pasada del índice")
    parser.add_argument("--chunk-mb", type=float, default=7.0, help="tamaño de HTML a partir del cual un volumen se imprime por tramos")
    parser.add_argument("--keep-work", action="store_true", help="conserva HTML y PDF intermedios")
    parser.add_argument("--work", help="carpeta de trabajo (por defecto, temporal)")
    parser.add_argument("--manifest", help="escribe aquí el manifiesto JSON de lo construido")
    parser.add_argument("--list", action="store_true", help="solo lista los volúmenes")
    args = parser.parse_args()
    args.chunk_bytes = int(args.chunk_mb * 1e6)
    args.out = str(Path(args.out).resolve())
    if args.work:
        args.work = str(Path(args.work).resolve())
    import fitz

    fitz.TOOLS.mupdf_display_errors(False)  # avisos de enlaces sin destino en los tramos: se cuentan y se rechazan abajo

    curriculum = load_curriculum()
    only = {p.strip().zfill(2) for p in args.parts.split(",")} if args.parts else None
    volumes = build_volumes(curriculum, only)
    if args.list:
        for vol in volumes.values():
            print(vol.slug, counts_of(vol))
        return 0
    wanted = list(volumes) if args.volumes == "all" else [
        slug for slug in volumes if any(slug == w or slug.startswith(w) for w in args.volumes.split(","))
    ]
    if not wanted:
        raise SystemExit(f"Ningún volumen coincide con {args.volumes!r}; disponibles: {', '.join(volumes)}")
    prov = provenance()
    browser = find_browser(args.browser)
    work = Path(args.work) if args.work else Path(tempfile.mkdtemp(prefix="pdf-build-"))
    work.mkdir(parents=True, exist_ok=True)
    extra = {"glossary_entries": glossary_entries()}
    manifest = {"program": PROGRAM, "commit": prov["commit"], "date": prov["date"], "dirty": prov["dirty"],
                "browser": subprocess.run([browser, "--version"], capture_output=True, text=True).stdout.strip(),
                "volumes": []}
    try:
        for slug in wanted:
            manifest["volumes"].append(build_volume(volumes[slug], prov, args, browser, work, extra))
    finally:
        if not args.keep_work and not args.work:
            shutil.rmtree(work, ignore_errors=True)
    target = Path(args.manifest) if args.manifest else Path(args.out) / "manifest.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():  # conserva los volúmenes ya construidos desde el mismo commit
        try:
            previous = json.loads(target.read_text(encoding="utf-8"))
            if previous.get("commit") == manifest["commit"] and previous.get("dirty") == manifest["dirty"]:
                built = {v["file"] for v in manifest["volumes"]}
                manifest["volumes"] = [v for v in previous["volumes"] if v["file"] not in built and (target.parent / v["file"]).exists()] + manifest["volumes"]
        except (ValueError, KeyError):
            pass
    target.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Manifiesto: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
