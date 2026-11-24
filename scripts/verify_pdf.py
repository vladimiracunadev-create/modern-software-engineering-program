#!/usr/bin/env python3
"""Verifica los PDF generados por ``scripts/build_pdf.py`` abriéndolos y contando lo que llevan.

Que el build termine no demuestra nada: este verificador abre cada PDF y compara con las
fuentes (curriculum, páginas publicadas, registro de casos, guías de rol, glosario):

* número de páginas, metadatos, idioma y huella SHA-256 frente al manifiesto;
* partes, clases (SE-001..SE-612), casos, guías de rol y términos de glosario presentes;
* figuras: una marca invisible ``fig:<archivo>.svg`` por figura de origen, comparada con la fuente;
* texto extraído: sin ``mermaid``, sin ``SE-nnn`` sin enlazar (salvo código y rótulos), sin U+FFFD;
* enlaces internos: ninguno roto; el índice enlaza cada unidad; cada marcador llega a su destino;
* fuentes incrustadas y ningún texto fuera de la página (código o tablas cortados).

Uso::

    python scripts/verify_pdf.py --dir build/pdf [--release] [--report informe.json]

``--release`` además exige que el árbol estuviera limpio al generar (commit reproducible).
Termina con código 1 si cualquier comprobación falla.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_pdf as bp  # noqa: E402

MAX_BYTES = 450 * 1024 * 1024  # por archivo; GitHub admite 2 GiB por activo, pero un libro de ese tamaño no es razonable
SE = re.compile(r"\bSE-\d{3}\b")
MONO = re.compile(r"mono|consolas|cascadia|courier|menlo|^Type3", re.I)  # el código se imprime con Type3 o monoespaciada
SKIP_COLORS = {0xD85845, 0x5A6773, 0xFFB195}  # encabezado, id del índice y rótulos de apertura


def expected_volume(slug: str, curriculum: dict) -> dict:
    stages = {s["id"] for s in curriculum["stages"]}
    parts = curriculum["parts"]
    if slug.startswith("etapa-"):
        stage = slug.split("-")[1].upper()
        chosen = [p for p in parts if p["stage"] == stage]
    elif slug == "libro-completo":
        chosen = parts
    else:
        chosen = []
    out = {
        "parts": [p["id"] for p in chosen],
        "classes": [lesson["id"] for p in chosen for lesson in p["lessons"]],
        "cases": [], "roles": 0, "glossary": [],
    }
    with_cases = slug in {"libro-completo", "casos-de-estudio"}
    if with_cases:
        for kind in ("exito", "fallo"):
            out["cases"] += [(kind, s) for s in bp.case_listing(kind)]
    if slug in {"libro-completo", "guias-de-rol"}:
        out["roles"] = len([p for p in (ROOT / "roles").glob("*.md") if p.name != "README.md"])
    if slug in {"libro-completo", "glosario"}:
        out["glossary"] = glossary_slugs()
    assert stages
    return out


def glossary_slugs() -> list[str]:
    """Entradas del glosario publicadas (una página por concepto, sin contar el índice)."""
    gdir = bp.SITE / "glosario"
    return sorted(p.stem for p in gdir.rglob("*.html") if p.name != "index.html") if gdir.is_dir() else []


def inventory_count() -> int:
    inventory = ROOT / "glosario" / "INVENTARIO.md"
    match = re.search(r"(\d[\d.]*) conceptos", inventory.read_text(encoding="utf-8")) if inventory.exists() else None
    return int(match.group(1).replace(".", "")) if match else 0


def source_figure_counts(slug: str, curriculum: dict) -> collections.Counter:
    """Instancias de figura (por nombre de archivo) en las fuentes de este volumen."""
    only = None
    vols = bp.build_volumes(curriculum, only)
    counter: collections.Counter = collections.Counter()
    for unit in vols[slug].units:
        for src in re.findall(r"<img\b[^>]*?\bsrc=\"([^\"]+)\"", unit.html):
            if not re.match(r"^[a-z][a-z0-9+.-]*:", src, re.I):
                counter[Path(src).name] += 1
    return counter


def verify_volume(entry: dict, directory: Path, curriculum: dict, release: bool, glossary_entries: int) -> tuple[dict, list[str]]:
    import fitz

    problems: list[str] = []
    slug = entry["file"].removeprefix(bp.FILE_PREFIX + "_").removesuffix(".pdf")
    path = directory / entry["file"]
    report: dict = {"file": entry["file"], "slug": slug}
    if not path.exists():
        return report, [f"{entry['file']}: no existe"]
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    report.update(bytes=len(data), sha256=sha)
    if sha != entry["sha256"]:
        problems.append(f"{slug}: SHA-256 distinto del manifiesto")
    if len(data) > MAX_BYTES:
        problems.append(f"{slug}: {len(data) / 1e6:.0f} MB supera el límite de {MAX_BYTES // 2**20} MiB")
    doc = fitz.open(path)
    report["pages"] = len(doc)
    if len(doc) != entry["pages"]:
        problems.append(f"{slug}: {len(doc)} páginas, el manifiesto dice {entry['pages']}")
    meta = doc.metadata or {}
    if bp.PROGRAM not in (meta.get("title") or ""):
        problems.append(f"{slug}: título de metadatos sin el nombre del programa")
    if "es" not in (doc.xref_get_key(doc.pdf_catalog(), "Lang")[1] or ""):
        problems.append(f"{slug}: falta /Lang es")
    if release and entry.get("dirty"):
        problems.append(f"{slug}: generado con el árbol sucio; no apto para publicar")
    expect = expected_volume(slug, curriculum)

    # --- marcadores
    toc = doc.get_toc()
    titles = [t[1] for t in toc]
    classes_in_outline = [t[1].split(" · ")[0] for t in toc if re.match(r"^SE-\d{3} · ", t[1])]
    parts_in_outline = [t[1].split(" · ")[0].removeprefix("Parte ") for t in toc if re.match(r"^Parte \d\d · ", t[1])]
    report.update(outline=len(toc), classes=len(classes_in_outline), parts=len(parts_in_outline))
    if classes_in_outline != expect["classes"]:
        missing = sorted(set(expect["classes"]) - set(classes_in_outline))
        problems.append(f"{slug}: clases en marcadores {len(classes_in_outline)} vs esperadas {len(expect['classes'])}; faltan {missing[:5]}")
    if parts_in_outline != expect["parts"]:
        problems.append(f"{slug}: partes en marcadores {parts_in_outline} vs {expect['parts']}")
    for level, title, page in toc:
        if not (1 <= page <= len(doc)):
            problems.append(f"{slug}: marcador «{title}» apunta fuera del documento ({page})")

    # --- texto y destino de cada marcador
    page_text: list[str] = []
    for page in doc:
        page_text.append(page.get_text())
    full = "\n".join(page_text)
    for level, title, page in toc:
        if level == 1 or not (1 <= page <= len(doc)):
            continue
        if title.startswith(("Etapa ", "Casos de estudio", "Guías de rol", "Glosario")) and " · " not in title[:4]:
            continue
        probe = re.sub(r"\s+", " ", title.split(" · ", 1)[-1])[:28]
        text = re.sub(r"\s+", " ", page_text[page - 1])
        if probe not in text:
            problems.append(f"{slug}: marcador «{title[:50]}» no cae en su página ({page})")
            if len(problems) > 60:
                break
    case_count = len(expect["cases"])
    keys = set(entry_unit_keys(entry))
    for kind, slug_case in expect["cases"]:
        if f"case-{kind}-{slug_case}" not in keys:
            problems.append(f"{slug}: falta el caso {kind}/{slug_case}")
    role_keys = [k for k in keys if k.startswith("role-") and k != "roles-index"]
    if len(role_keys) != expect["roles"]:
        problems.append(f"{slug}: {len(role_keys)} guías de rol, esperadas {expect['roles']}")
    report.update(cases=len([k for k in keys if k.startswith("case-")]), roles=len(role_keys))
    if len([k for k in keys if k.startswith("case-")]) != case_count:
        problems.append(f"{slug}: casos presentes {len([k for k in keys if k.startswith('case-')])} vs {case_count}")
    if expect["glossary"]:
        entries = [k for k in keys if k.startswith("gl-") and not k.startswith("gl-letra-")]
        marks = collections.Counter(re.findall(r"gl:([a-z0-9._-]+)", full))
        report.update(glossary_entries=len(entries), glossary_marks=sum(marks.values()))
        if set(marks) != set(expect["glossary"]) or sum(marks.values()) != len(expect["glossary"]):
            missing = sorted(set(expect["glossary"]) - set(marks))
            problems.append(f"{slug}: glosario con {sum(marks.values())} entradas en el PDF vs {len(expect['glossary'])} en las fuentes; faltan {missing[:5]}")
        if glossary_entries and glossary_entries != len(expect["glossary"]):
            problems.append(f"{slug}: el inventario declara {glossary_entries} conceptos y las páginas publicadas son {len(expect['glossary'])}")
        if len(entries) != len(expect["glossary"]):
            problems.append(f"{slug}: {len(entries)} entradas en el manifiesto vs {len(expect['glossary'])}")

    # --- SE-nnn sin enlazar, enlaces internos, fuentes y desbordes
    names = doc.resolve_names()
    unresolved = 0
    broken = 0
    internal = 0
    external = 0
    prose: list[str] = []  # texto fuera de código: lo que no puede llevar sintaxis de origen
    toc_links: set[int] = set()
    toc_end = entry["units"][0]["page"]  # el índice ocupa las páginas anteriores a la primera unidad
    overflow: list[str] = []
    bad_numbers: list[str] = []
    nonembedded: set[str] = set()
    for index, page in enumerate(doc):
        links = page.get_links()
        rects = []
        for link in links:
            kind = link["kind"]
            if kind == fitz.LINK_URI:
                external += 1
            elif kind in (fitz.LINK_NAMED, fitz.LINK_GOTO):
                internal += 1
                name = link.get("nameddest") or ""
                if (kind == fitz.LINK_NAMED and name not in names) or not (0 <= link.get("page", -1) < len(doc)):
                    broken += 1
                    if broken <= 5:
                        problems.append(f"{slug}: enlace interno roto en p.{index + 1}: {name!r}")
                if index + 1 < toc_end:
                    toc_links.add(link.get("page", -1) + 1)
            if "from" in link:
                rects.append(link["from"])
        prose.extend(span["text"] for block in page.get_text("dict")["blocks"] for line in block.get("lines", [])
                     for span in line["spans"] if not MONO.search(span["font"]))
        frames: list | None = None  # marcos de figura; se calculan solo si hace falta (get_drawings es lento)
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    if not SE.search(span["text"]) or re.search(r"[/\w-]SE-\d{3}", span["text"]) or MONO.search(span["font"]) or span["color"] in SKIP_COLORS:
                        continue
                    if span["bbox"][1] < 62 or span["bbox"][3] > page.rect.height - 50:
                        continue  # encabezado y pie
                    for word in page.search_for(SE.search(span["text"]).group(0), clip=fitz.Rect(span["bbox"])):
                        if not any(r.intersects(word) for r in rects):
                            if frames is None:
                                frames = [d["rect"] for d in page.get_drawings()
                                          if d.get("color") and abs(d["color"][0] - 0.765) < 0.02 and abs(d["color"][1] - 0.839) < 0.02
                                          and d["rect"].height > 40]
                            if not any(f.contains(word) for f in frames):  # texto dentro de una figura SVG
                                unresolved += 1
        for word in page.get_text("words"):
            if word[2] > page.rect.width - 8 and index > 2:
                overflow.append(f"p.{index + 1}: «{word[4][:30]}»")
            if index > 0 and word[1] > page.rect.height - 60 and word[0] > page.rect.width - 100 and word[4].isdigit() and int(word[4]) != index + 1:
                bad_numbers.append(f"p.{index + 1} lleva el número {word[4]}")
        for font in page.get_fonts():
            if font[1] == "n/a" and font[2] != "Type3":
                nonembedded.add(font[3])
    report.update(internal_links=internal, external_links=external, broken_links=broken, unlinked_se=unresolved)
    if unresolved:
        problems.append(f"{slug}: {unresolved} menciones SE-nnn sin enlazar")
    if overflow:
        problems.append(f"{slug}: {len(overflow)} palabras fuera del margen derecho, p. ej. {overflow[:3]}")
    if bad_numbers:
        problems.append(f"{slug}: {len(bad_numbers)} páginas con numeración distinta de su posición, p. ej. {bad_numbers[:3]}")
    if nonembedded:
        problems.append(f"{slug}: fuentes no incrustadas: {sorted(nonembedded)[:5]}")
    for unit in entry["units"]:
        if unit["kind"] == "gl-entry":
            continue  # las entradas del glosario se alcanzan por letra, no desde el índice
        if unit["page"] not in toc_links:
            problems.append(f"{slug}: el índice no enlaza la unidad {unit['key']} (página {unit['page']})")
            break

    # --- texto prohibido (solo prosa: el código de ejemplo puede contener HTML, Markdown o Mermaid)
    visible = re.sub(r"(?:fig|gl):[A-Za-z0-9._-]+", "", chr(10).join(prose))
    if re.search(r"(?m)^(?:flowchart|graph|sequenceDiagram|stateDiagram(?:-v2)?)(?![\w-])|mermaid-[0-9a-f]{10}|```", visible):
        problems.append(f"{slug}: queda código de diagrama Mermaid o una valla de código en el texto")
    if chr(0xFFFD) in visible:
        problems.append(f"{slug}: caracteres de reemplazo U+FFFD en el texto")
    if re.search(r"\]\(|<img |</?(?:div|span|table)(?![\w-])", visible):
        problems.append(f"{slug}: restos de Markdown/HTML en el texto")

    # --- figuras: marca invisible por figura frente a las fuentes
    in_pdf = collections.Counter(re.findall(r"fig:([A-Za-z0-9._-]+\.svg)", full))
    from_source = source_figure_counts(slug, curriculum)
    report.update(figures=sum(in_pdf.values()), figure_files=len(in_pdf))
    if in_pdf != from_source:
        lost = from_source - in_pdf
        extra = in_pdf - from_source
        problems.append(f"{slug}: figuras distintas de la fuente: faltan {sum(lost.values())} {list(lost)[:3]}, sobran {sum(extra.values())}")
    # --- portada
    cover = re.sub(r"\s+", " ", page_text[0])
    if bp.PROGRAM not in cover or entry["commit"][:8] not in cover:
        problems.append(f"{slug}: la portada no declara programa y commit")
    doc.close()
    return report, problems


def entry_unit_keys(entry: dict) -> list[str]:
    return [u["key"] for u in entry["units"]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dir", default=str(ROOT / "build" / "pdf"))
    parser.add_argument("--manifest", help="por defecto <dir>/manifest.json")
    parser.add_argument("--release", action="store_true", help="exige árbol limpio al generar")
    parser.add_argument("--report", help="escribe el informe JSON")
    parser.add_argument("--glossary-entries", type=int, default=-1, help="conceptos esperados; por defecto, los que declara glosario/INVENTARIO.md")
    args = parser.parse_args()
    directory = Path(args.dir)
    if args.glossary_entries < 0:
        args.glossary_entries = inventory_count()
    manifest = json.loads(Path(args.manifest or directory / "manifest.json").read_text(encoding="utf-8"))
    curriculum = bp.load_curriculum()
    manifest_dirty = manifest.get("dirty")
    all_problems: list[str] = []
    reports = []
    for entry in manifest["volumes"]:
        entry["dirty"] = manifest_dirty
        report, problems = verify_volume(entry, directory, curriculum, args.release, args.glossary_entries)
        reports.append(report)
        all_problems += problems
        status = "OK " if not problems else "FALLA"
        print(f"[{status}] {report['file']}: {report.get('pages')} págs, {report.get('classes')} clases, {report.get('parts')} partes, "
              f"{report.get('cases')} casos, {report.get('roles')} roles, {report.get('figures')} figuras, "
              f"{report.get('internal_links')} enlaces internos ({report.get('broken_links')} rotos)")
        for problem in problems:
            print("   -", problem)
    if args.report:
        Path(args.report).write_text(json.dumps({"commit": manifest["commit"], "volumes": reports, "problems": all_problems},
                                                 ensure_ascii=False, indent=1), encoding="utf-8")
    print("Resultado:", "sin problemas" if not all_problems else f"{len(all_problems)} problema(s)")
    return 1 if all_problems else 0


if __name__ == "__main__":
    sys.exit(main())
