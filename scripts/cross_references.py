"""Resolución de referencias cruzadas: un único mecanismo para toda la publicación.

Las menciones ``SE-nnn`` y ``Parte NN`` en prosa se convierten en enlaces a la clase o a la
parte publicada y los nombres de parte se normalizan al título oficial. La fuente de verdad
es ``curriculum.yaml``; el H1 de ``content/part-NN/README.md`` debe coincidir con su ``title``
(lo comprueba ``tests/test_cross_references.py``).

El paso es una función pura sobre texto Markdown:

* no toca bloques de código, código en línea, encabezados, imágenes, enlaces ya existentes,
  URL ni etiquetas HTML;
* es idempotente (una mención que ya es enlace no se vuelve a enlazar) y determinista
  (solo depende del texto, del directorio de destino y de ``curriculum.yaml``);
* trata igual la prosa, las listas y las celdas de tabla.

Lo usan ``build_phase2``, ``build_phase3``, ``build_phase4``, ``build_cases`` y
``build_role_guides`` al publicar, y la CLI::

    python scripts/cross_references.py --audit      # cuenta las menciones desnudas
    python scripts/cross_references.py --write casos
"""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import sys
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Nombres abreviados o retirados de cada parte. Se reescriben al título oficial cuando
# acompañan a "Parte NN" (tras un guion largo o entre paréntesis). Se comparan tras el
# prefijo de la referencia, nunca en prosa libre, para no alterar frases como «backend y APIs».
RETIRED_PART_NAMES: dict[str, tuple[str, ...]] = {
    "00": ("Profesión",),
    "01": ("Computadores y representación de la información", "Computadores y representación", "Computadores"),
    "02": (
        "Sistemas operativos y entorno de trabajo",
        "Sistemas operativos, terminal y automatización",
        "Sistemas operativos y terminal",
    ),
    "03": ("Redes, internet y protocolos", "Redes e internet", "Redes"),
    "04": ("Pensamiento computacional",),
    "06": ("Paradigmas",),
    "07": ("Estructuras y algoritmos",),
    "08": ("Entornos y depuración",),
    "09": ("Paquetes y automatización",),
    "10": ("Discovery",),
    "11": ("Economía y métricas",),
    "12": ("Requisitos",),
    "13": ("Especificaciones y contratos",),
    "14": ("Experiencia, accesibilidad e i18n", "UX, accesibilidad e i18n"),
    "15": ("Procesos y estimación",),
    "16": ("Git y colaboración",),
    "17": ("Documentación",),
    "18": ("CLI, TUI y servicios",),
    "19": ("Web, front-end y aplicaciones progresivas", "Web, frontend y aplicaciones progresivas", "Web y frontend"),
    "20": ("Backend y APIs",),
    "21": ("Software móvil, de escritorio y multiplataforma", "Móvil y escritorio"),
    "22": ("Embedded, IoT y edge",),
    "24": ("Dominios especializados",),
    "25": ("Diseño y refactorización",),
    "27": ("Arquitectura",),
    "29": ("Datos",),
    "31": ("Integración y eventos",),
    "32": ("Sistemas distribuidos",),
    "33": ("Cloud y plataforma",),
    "35": ("Testing",),
    "38": ("Seguridad, privacidad y compliance",),
    "39": ("Build, release y supply chain", "Supply chain y release"),
    "40": ("CI/CD y Platform Engineering",),
    "43": ("Legacy y retiro",),
    "44": ("Liderazgo",),
    "45": ("Metodologías de TDD a ODD",),
    "46": ("Desarrollo asistido por IA", "Ingeniería asistida por IA"),
    "47": ("SPEC y agentes",),
}

# Documentos que narran migraciones o historia: conservan IDs y nombres antiguos y no se
# resuelven ni se auditan.
HISTORICAL_PREFIXES = (
    "docs/ID-MIGRATION",
    "docs/adr/",
    "docs/PART-EXECUTION-TRACKER.md",
    "CHANGELOG.md",
)

SE_RE = re.compile(r"(?<![\w/\\.\-])SE-(\d{3})(?![\w]|\.\w|-(?!SE-))")
# "Parte 5", "Parte 05"; el plural admite listas: "Partes 24–25, 27 y 29".
PARTE_RE = re.compile(
    r"(?<![\w/\\.\-])(Partes?)\s+(\d{1,2})(?![\d\w]|\.\d)"
    r"((?:(?:\s*,\s*|\s+y\s+|\s+e\s+|\s+a\s+|\s*[–-]\s*|\s*/\s*)\d{1,2}(?![\d\w]|\.\d))*)"
)
LIST_ITEM_RE = re.compile(r"(\s*,\s*|\s+y\s+|\s+e\s+|\s+a\s+|\s*[–-]\s*|\s*/\s*)(\d{1,2})")

# Tramos que no son prosa dentro de una línea.
PROTECTED_INLINE = re.compile(
    r"""
      (?P<code>(?P<tick>`+)(?:(?!(?P=tick)).)+?(?P=tick))      # código en línea
    | (?P<image>!\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)]*\))          # imagen
    | (?P<link>\[(?:[^\[\]]|\[[^\]]*\])*\]\([^)]*\))            # enlace en línea
    | (?P<refuse>\[(?:[^\[\]]|\[[^\]]*\])*\]\[[^\]]*\])         # enlace por referencia
    | (?P<auto><[A-Za-z][A-Za-z0-9+.-]*:[^>\s]*>)                # <https://...>
    | (?P<url>https?://[^\s<>)\]]+)                              # URL suelta
    | (?P<comment><!--.*?-->)                                    # comentario HTML
    | (?P<tag></?[A-Za-z][^>]*>)                                 # etiqueta HTML
    """,
    re.VERBOSE | re.DOTALL,
)

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}(\s|$)")
REFDEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s")
RAW_BLOCK_RE = re.compile(r"^\s{0,3}<(svg|pre|script|style)\b", re.IGNORECASE)
LINK_PARTS_RE = re.compile(r"^\[(?P<label>.*)\]\((?P<target>[^)]*)\)$", re.DOTALL)
PART_TARGET_RE = re.compile(r"(?:^|/)(?:part-(\d\d)-[^/)\s]+/(?:README\.md)?|parts/(\d\d)\.html|(\d\d)\.html)(?:#[^)\s]*)?$")
LESSON_TARGET_RE = re.compile(r"(?:/|^)se-(\d{3})-[^/)\s]+/(?:README\.md)?(?:#[^)\s]*)?$")
LESSON_LABEL_RE = re.compile(r"^(?P<head>SE-(?P<id>\d{3})\s*[—·]\s*)(?P<title>[^\[\]→]+?)$")


@dataclass(frozen=True)
class Reference:
    id: str
    title: str
    path: str  # README publicado, relativo a la raíz del repositorio


@dataclass
class Index:
    parts: dict[str, Reference] = field(default_factory=dict)
    lessons: dict[str, Reference] = field(default_factory=dict)


@lru_cache(maxsize=1)
def load_index() -> Index:
    program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    index = Index()
    for part in program["parts"]:
        index.parts[part["id"]] = Reference(part["id"], part["title"], f"{part['path']}/README.md")
        for lesson in part["lessons"]:
            index.lessons[lesson["id"]] = Reference(lesson["id"], lesson["title"], f"{lesson['path']}/README.md")
    return index


def is_historical(relative_path: str) -> bool:
    return relative_path.replace("\\", "/").startswith(HISTORICAL_PREFIXES)


def relative_link(base_dir: str, target: str) -> str:
    """Enlace relativo POSIX desde el directorio ``base_dir`` hasta ``target``."""
    result = posixpath.relpath(target, base_dir or ".")
    return result if result.startswith(".") else f"./{result}"


def part_id_of(number: str) -> str:
    return number.zfill(2)


# ------------------------------------------------------------------------- segmentación
Segment = tuple[str, str]  # (clase, texto); clase "prose" o la del tramo protegido


def _regions(text: str) -> list[tuple[int, int, str]]:
    """Regiones (inicio, fin, clase) de nivel bloque; "prose" son párrafos, listas y tablas."""
    lines = text.split("\n")
    starts: list[int] = []
    cursor = 0
    for line in lines:
        starts.append(cursor)
        cursor += len(line) + 1

    def end_of(last: int) -> int:
        return starts[last] + len(lines[last])

    regions: list[tuple[int, int, str]] = []
    prose_first: int | None = None
    prose_last = 0
    index = 0

    def close_prose() -> None:
        nonlocal prose_first
        if prose_first is not None:
            regions.append((starts[prose_first], end_of(prose_last), "prose"))
            prose_first = None

    if lines and lines[0].strip() == "---":
        stop = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        if stop is not None:
            regions.append((0, end_of(stop), "frontmatter"))
            index = stop + 1
    while index < len(lines):
        line = lines[index]
        fence = FENCE_RE.match(line)
        raw_kind = ""
        last = index
        if fence:
            raw_kind = "fence"
            char = fence.group(1)[0]
            width = len(fence.group(1))
            last = index + 1
            while last < len(lines):
                closing = FENCE_RE.match(lines[last])
                if closing and closing.group(1)[0] == char and len(closing.group(1)) >= width and lines[last].strip() == closing.group(1):
                    break
                last += 1
            last = min(last, len(lines) - 1)
        elif "<!--" in line and "-->" not in line.split("<!--", 1)[1]:
            raw_kind = "comment"
            last = next((i for i in range(index, len(lines)) if "-->" in lines[i]), len(lines) - 1)
        elif RAW_BLOCK_RE.match(line):
            raw_kind = "rawhtml"
            tag = RAW_BLOCK_RE.match(line).group(1).lower()
            last = next((i for i in range(index, len(lines)) if f"</{tag}>" in lines[i].lower()), len(lines) - 1)
        elif HEADING_RE.match(line):
            raw_kind = "heading"
        elif REFDEF_RE.match(line):
            raw_kind = "refdef"
        if raw_kind:
            close_prose()
            regions.append((starts[index], end_of(last), raw_kind))
            index = last + 1
        elif not line.strip():
            close_prose()
            index += 1
        else:
            if prose_first is None:
                prose_first = index
            prose_last = index
            index += 1
    close_prose()
    return regions


def segments(text: str) -> list[Segment]:
    """Divide el documento en tramos de prosa y tramos protegidos, sin perder ni un carácter."""
    result: list[Segment] = []
    cursor = 0
    for start, end, kind in _regions(text):
        if start > cursor:
            result.append(("prose", text[cursor:start]))
        chunk = text[start:end]
        if kind == "prose":
            position = 0
            for match in PROTECTED_INLINE.finditer(chunk):
                if match.start() > position:
                    result.append(("prose", chunk[position : match.start()]))
                result.append((match.lastgroup if match.lastgroup != "tick" else "code", match.group(0)))
                position = match.end()
            if position < len(chunk):
                result.append(("prose", chunk[position:]))
        else:
            result.append((kind, chunk))
        cursor = end
    if cursor < len(text):
        result.append(("prose", text[cursor:]))
    return result


# ----------------------------------------------------------------------------- resolución
def _target(kind: str, ref_id: str, base_dir: str, html_mode: bool) -> str | None:
    """Destino relativo: el README publicado (Markdown) o la página equivalente del portal (HTML)."""
    index = load_index()
    if kind == "lesson":
        if ref_id not in index.lessons:
            return None
        path = f"site/classes/{ref_id}.html" if html_mode else index.lessons[ref_id].path
    else:
        if ref_id not in index.parts:
            return None
        path = f"site/parts/{ref_id}.html" if html_mode else index.parts[ref_id].path
    return relative_link(base_dir, path)


def _anchor(label: str, href: str, html_mode: bool) -> str:
    return f'<a href="{href}">{html.escape(label)}</a>' if html_mode else f"[{label}]({href})"


def _name_alternatives(part_id: str) -> list[str]:
    official = load_index().parts[part_id].title
    names = {official, *RETIRED_PART_NAMES.get(part_id, ())}
    return sorted(names, key=len, reverse=True)


def _name_tail(prose: str, end: int, part_id: str) -> tuple[str, str, int] | None:
    """Reconoce «— Nombre» o «(Nombre)» tras una mención; devuelve (apertura, cierre, fin)."""
    for opener, closer in ((r"\s+[—–]\s+", ""), (r"\s+-\s+", ""), (r"\s*\(", ")")):
        match = re.compile(opener).match(prose, end)
        if not match:
            continue
        for name in _name_alternatives(part_id):
            stop = match.end() + len(name)
            if prose.startswith(name, match.end()) and not re.match(r"[\wáéíóúüñÁÉÍÓÚÜÑ]", prose[stop : stop + 1] or " "):
                if closer and prose[stop : stop + 1] != ")":
                    continue
                tail_end = stop + (1 if closer else 0)
                return match.group(0), closer, tail_end
    return None


def _resolve_prose(prose: str, base_dir: str, html_mode: bool = False) -> str:
    def lesson(match: re.Match[str]) -> str:
        lesson_id = f"SE-{match.group(1)}"
        href = _target("lesson", lesson_id, base_dir, html_mode)
        return _anchor(lesson_id, href, html_mode) if href else match.group(0)

    prose = SE_RE.sub(lesson, prose)
    output: list[str] = []
    position = 0
    for match in PARTE_RE.finditer(prose):
        word, first, rest = match.group(1), match.group(2), match.group(3)
        if part_id_of(first) not in load_index().parts:
            continue
        output.append(prose[position : match.start()])
        position = match.end()
        if word == "Parte" or not rest:
            part_id = part_id_of(first)
            href = _target("part", part_id, base_dir, html_mode)
            tail = _name_tail(prose, match.end(), part_id) if word == "Parte" else None
            if tail:
                opener, closer, tail_end = tail
                separator = " — " if opener.strip() in {"—", "–", "-"} else " ("
                label = f"{word} {first}{separator}{load_index().parts[part_id].title}{closer}"
                output.append(_anchor(label, href, html_mode))
                position = tail_end
            else:
                output.append(_anchor(f"{word} {first}", href, html_mode))
            continue
        # lista de partes: "Partes 24–25, 27 y 29"
        pieces = [f"{word} "]
        numbers = [(None, first)] + [(m.group(1), m.group(2)) for m in LIST_ITEM_RE.finditer(rest)]
        for separator, number in numbers:
            href = _target("part", part_id_of(number), base_dir, html_mode)
            if separator is not None:
                pieces.append(separator)
            pieces.append(_anchor(number, href, html_mode) if href else number)
        output.append("".join(pieces))
    output.append(prose[position:])
    return "".join(output)


def _fix_link_label(link: str) -> str:
    """Normaliza etiquetas de enlaces: «Parte NN — alias» y «SE-nnn — título» → título oficial."""
    parts = LINK_PARTS_RE.match(link)
    if not parts:
        return link
    target = parts.group("target")
    lesson_match = LESSON_TARGET_RE.search(target)
    if lesson_match:  # «SE-nnn — Título»: el título citado debe ser el real de la clase
        reference = load_index().lessons.get(f"SE-{lesson_match.group(1)}")
        label_match = LESSON_LABEL_RE.match(parts.group("label"))
        if reference and label_match and label_match.group("id") == lesson_match.group(1) and label_match.group("title") != reference.title:
            return f"[{label_match.group('head')}{reference.title}]({target})"
        return link
    target_match = PART_TARGET_RE.search(target)
    if not target_match:
        return link
    part_id = target_match.group(1) or target_match.group(2) or target_match.group(3)
    if part_id not in load_index().parts:
        return link
    official = load_index().parts[part_id].title
    label = parts.group("label")
    fixed = re.match(r"^(?P<head>(?:\*\*)?(?:la |de la )?Partes? 0*(?P<n>\d{1,2})(?:\s*[—–]\s*|\s+-\s+|\s*·\s*))(?P<name>[^\[\]]+?)(?P<tail>\*\*)?$", label)
    if fixed and part_id_of(fixed.group("n")) == part_id:
        name = fixed.group("name")
        if name != official and name in _name_alternatives(part_id):
            return f"[{fixed.group('head')}{official}{fixed.group('tail') or ''}]({target})"
    return link


def resolve(text: str, base_dir: str) -> str:
    """Enlaza ``SE-nnn``/``Parte NN`` y normaliza nombres de parte en el Markdown ``text``.

    ``base_dir`` es el directorio (relativo a la raíz) donde vivirá el archivo resultante.
    """
    result: list[str] = []
    for kind, chunk in segments(text):
        if kind == "prose":
            result.append(_resolve_prose(chunk, base_dir))
        elif kind == "link":
            result.append(_fix_link_label(chunk))
        else:
            result.append(chunk)
    return "".join(result)


def normalize_names(text: str) -> str:
    """Solo normaliza los nombres de parte en enlaces; no enlaza menciones (fuentes editoriales)."""
    return "".join(_fix_link_label(chunk) if kind == "link" else chunk for kind, chunk in segments(text))


# ------------------------------------------------------------------------------ auditoría
@dataclass(frozen=True)
class Finding:
    kind: str  # bare-se, bare-parte, unknown-se, unknown-parte, part-name
    detail: str
    line: int


def _line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def audit_markdown(text: str) -> list[Finding]:
    """Menciones sin enlace, inexistentes o con nombre de parte distinto del oficial."""
    findings: list[Finding] = []
    index = load_index()
    offset = 0
    for kind, chunk in segments(text):
        if kind == "prose":
            for match in SE_RE.finditer(chunk):
                lesson_id = f"SE-{match.group(1)}"
                detail = lesson_id
                findings.append(Finding("unknown-se" if lesson_id not in index.lessons else "bare-se", detail, _line_of(text, offset + match.start())))
            for match in PARTE_RE.finditer(chunk):
                numbers = [match.group(2)] + [m.group(2) for m in LIST_ITEM_RE.finditer(match.group(3))]
                for number in numbers:
                    known = part_id_of(number) in index.parts
                    findings.append(Finding("bare-parte" if known else "unknown-parte", f"{match.group(1)} {number}", _line_of(text, offset + match.start())))
        elif kind == "link":
            fixed = _fix_link_label(chunk)
            if fixed != chunk:
                findings.append(Finding("part-name", chunk[:80], _line_of(text, offset)))
            for match in SE_RE.finditer(chunk):
                if f"SE-{match.group(1)}" not in index.lessons:
                    findings.append(Finding("unknown-se", f"SE-{match.group(1)}", _line_of(text, offset)))
        else:
            if kind in {"code", "fence", "heading", "rawhtml", "comment", "frontmatter", "refdef", "image", "tag", "url", "auto", "refuse", "raw"}:
                pass
        offset += len(chunk)
    return findings


def audit_part_names(text: str) -> list[Finding]:
    """«Parte NN — X» (en prosa o en el texto de un enlace) cuyo X no empieza por el título oficial."""
    findings: list[Finding] = []
    index = load_index()
    plain = re.sub(r"\]\([^)]*\)", "]", text)
    for match in re.finditer(r"Parte\s+0*(\d{1,2})\]?\s*[—–]\s+([A-ZÁÉÍÓÚÑ¿][^\n|\]\[]{2,})", plain):
        part_id = part_id_of(match.group(1))
        if part_id not in index.parts:
            continue
        official = index.parts[part_id].title
        if not match.group(2).startswith(official):
            findings.append(Finding("part-name", match.group(0)[:90], _line_of(plain, match.start())))
    return findings


# Tramos de HTML que no son prosa enlazable: enlaces, código, encabezados, metadatos, la
# etiqueta de identidad de la propia página (eyebrow, paso actual) y cualquier etiqueta.
HTML_SKIP = re.compile(
    r"""
      <(?P<name>script|style|pre|code|svg|title|h[1-6]|a|option|textarea)\b[^>]*>.*?</(?P=name)>
    | <p\ class="eyebrow">.*?</p>
    | <span[^>]*aria-current[^>]*>.*?</span>
    | <!--.*?-->
    | <[^>]+>
    """,
    re.VERBOSE | re.DOTALL | re.IGNORECASE,
)


def _html_text_nodes(text: str) -> list[tuple[bool, str]]:
    result: list[tuple[bool, str]] = []
    position = 0
    for match in HTML_SKIP.finditer(text):
        if match.start() > position:
            result.append((True, text[position : match.start()]))
        result.append((False, match.group(0)))
        position = match.end()
    if position < len(text):
        result.append((True, text[position:]))
    return result


def resolve_html(text: str, page_dir: str) -> str:
    """Igual que :func:`resolve`, para HTML generado; ``page_dir`` es la carpeta de la página."""
    return "".join(
        _resolve_prose(chunk, page_dir, html_mode=True) if is_text else chunk
        for is_text, chunk in _html_text_nodes(text)
    )


def audit_html(text: str) -> list[Finding]:
    """Menciones desnudas en HTML publicado (se ignoran enlaces, código, encabezados y metadatos)."""
    findings: list[Finding] = []
    index = load_index()
    offset = 0
    for is_text, chunk in _html_text_nodes(text):
        if is_text:
            for match in SE_RE.finditer(chunk):
                lesson_id = f"SE-{match.group(1)}"
                kind = "unknown-se" if lesson_id not in index.lessons else "bare-se"
                findings.append(Finding(kind, lesson_id, _line_of(text, offset + match.start())))
            for match in PARTE_RE.finditer(chunk):
                findings.append(Finding("bare-parte", f"{match.group(1)} {match.group(2)}", _line_of(text, offset + match.start())))
        offset += len(chunk)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--audit", action="store_true", help="cuenta menciones desnudas en las superficies publicadas")
    parser.add_argument("--write", nargs="*", metavar="DIR", help="enlaza en sitio las fuentes Markdown de estos directorios")
    parser.add_argument("--normalize-names", nargs="*", metavar="DIR", help="normaliza en sitio los nombres de parte en enlaces de estos directorios")
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if args.write is not None and args.write:
        changed = 0
        for directory in args.write:
            for path in sorted((ROOT / directory).rglob("*.md")):
                relative = path.relative_to(ROOT).as_posix()
                if is_historical(relative):
                    continue
                before = path.read_text(encoding="utf-8")
                after = resolve(before, posixpath.dirname(relative))
                if after != before:
                    path.write_text(after, encoding="utf-8", newline="\n")
                    changed += 1
        print(f"CROSS_REFERENCES_WRITTEN: {changed} files")
        return 0
    if args.normalize_names:
        changed = 0
        for directory in args.normalize_names:
            for path in sorted((ROOT / directory).rglob("*.md")):
                if is_historical(path.relative_to(ROOT).as_posix()):
                    continue
                before = path.read_text(encoding="utf-8")
                after = normalize_names(before)
                if after != before:
                    path.write_text(after, encoding="utf-8", newline="\n")
                    changed += 1
        print(f"CROSS_REFERENCES_NAMES_NORMALIZED: {changed} files")
        return 0
    totals: dict[str, int] = {}
    for pattern in ("classes/**/*.md", "roles/*.md", "casos/**/*.md", "README.md", "content/**/*.md"):
        for path in sorted(ROOT.glob(pattern)):
            relative = path.relative_to(ROOT).as_posix()
            if is_historical(relative):
                continue
            text = path.read_text(encoding="utf-8")
            for finding in audit_markdown(text) + audit_part_names(text):
                key = f"{pattern.split('/')[0]}:{finding.kind}"
                totals[key] = totals.get(key, 0) + 1
    for key, value in sorted(totals.items()):
        print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
