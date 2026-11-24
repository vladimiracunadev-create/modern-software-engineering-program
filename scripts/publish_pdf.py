#!/usr/bin/env python3
"""Registra y publica los PDF verificados: sumas, manifiesto, docs/PDF.md y GitHub Release.

Los PDF no entran en git (pesan decenas de MB y el repositorio es público: no se puede
limpiar el historial sin reescribirlo). En el repositorio solo quedan ``pdf/manifest.json``,
``pdf/SHA256SUMS`` y la tabla de ``docs/PDF.md``; los binarios van como activos de un Release.

Uso::

    python scripts/publish_pdf.py --dir build/pdf                       # registra y lista los activos
    python scripts/publish_pdf.py --dir build/pdf --create-release      # además crea el Release

Antes de registrar ejecuta ``scripts/verify_pdf.py --release``: un volumen que no pasa la
verificación no se publica.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_pdf as bp  # noqa: E402

START, END = "<!-- pdf-volumes:start -->", "<!-- pdf-volumes:end -->"
ORDER = ["libro-completo"] + [f"etapa-{c}" for c in "abcdefgh"] + ["casos-de-estudio", "glosario", "guias-de-rol"]


def slug_of(entry: dict) -> str:
    return entry["file"].removeprefix(bp.FILE_PREFIX + "_").removesuffix(".pdf")


def sort_key(entry: dict) -> int:
    slug = slug_of(entry)
    for i, prefix in enumerate(ORDER):
        if slug == prefix or slug.startswith(prefix + "-"):
            return i
    return len(ORDER)


def human(size: int) -> str:
    return f"{size / 1e6:.1f} MB" if size < 1e9 else f"{size / 1e9:.2f} GB"


def release_tag(manifest: dict) -> str:
    return f"pdf-{manifest['date'][:10]}-{manifest['commit'][:8]}"


def download_url(tag: str, name: str, latest: bool = False) -> str:
    base = f"https://github.com/{bp.REPO}/releases"
    return f"{base}/latest/download/{name}" if latest else f"{base}/download/{tag}/{name}"


def lean_manifest(manifest: dict) -> dict:
    volumes = []
    for entry in sorted(manifest["volumes"], key=sort_key):
        volumes.append({k: entry[k] for k in ("file", "title", "pages", "bytes", "sha256", "counts", "figures")})
        volumes[-1]["links"] = entry["links"]
    return {"program": manifest["program"], "commit": manifest["commit"], "date": manifest["date"],
            "browser": manifest.get("browser", ""), "tag": release_tag(manifest), "volumes": volumes}


def table(manifest: dict) -> str:
    tag = release_tag(manifest)
    rows = ["| Volumen | Contenido | Páginas | Tamaño | SHA-256 | Descarga |", "| --- | --- | ---: | ---: | --- | --- |"]
    for entry in sorted(manifest["volumes"], key=sort_key):
        c = entry["counts"]
        parts = []
        if c["classes"]:
            parts.append(f"{c['parts']} partes · {c['classes']} clases")
        if c["roles"]:
            parts.append(f"{c['roles']} guías de rol")
        if c["cases"]:
            parts.append(f"{c['cases']} casos")
        if c["glossary_pages"]:
            parts.append("glosario")
        rows.append(f"| **{entry['title']}** | {' · '.join(parts)} | {entry['pages']:,} | {human(entry['bytes'])} | "
                    f"`{entry['sha256'][:16]}…` | [PDF]({download_url(tag, entry['file'], True)}) |".replace(",", "."))
    return "\n".join(rows)


def update_docs(manifest: dict) -> None:
    path = ROOT / "docs" / "PDF.md"
    text = path.read_text(encoding="utf-8")
    block = (f"{START}\n"
             f"Edición generada el **{manifest['date'][:10]}** desde el commit `{manifest['commit'][:8]}` "
             f"(release [`{release_tag(manifest)}`](https://github.com/{bp.REPO}/releases/tag/{release_tag(manifest)})).\n\n"
             f"{table(manifest)}\n\n"
             f"Sumas SHA-256 completas: [`pdf/SHA256SUMS`](../pdf/SHA256SUMS) y [`pdf/manifest.json`](../pdf/manifest.json).\n"
             f"{END}")
    if START in text:
        text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    path.write_text(text, encoding="utf-8")


def update_readme(manifest: dict) -> None:
    """Lista de descargas del README (región ``pdf-downloads``), con enlace estable a la última edición."""
    tag = release_tag(manifest)
    by_slug = {slug_of(e): e for e in manifest["volumes"]}

    def link(slug: str, label: str) -> str:
        e = by_slug[slug]
        return f"[{label}]({download_url(tag, e['file'], True)}) ({e['pages']:,} págs · {human(e['bytes'])})".replace(",", ".")

    stages = [s for s in by_slug if s.startswith("etapa-")]
    lines = [
        f"Edición del {manifest['date'][:10]} (commit `{manifest['commit'][:8]}`, release "
        f"[`{tag}`](https://github.com/{bp.REPO}/releases/tag/{tag})); sumas SHA-256 en [`pdf/SHA256SUMS`](pdf/SHA256SUMS):",
        "",
        f"- 📘 {link('libro-completo', '**Libro completo**')}: clases, guías de rol, casos de estudio y glosario.",
        "- 📗 Por etapa: " + " · ".join(link(s, s.split("-")[1].upper()) for s in stages) + ".",
        f"- 🏛️ {link('casos-de-estudio', 'Casos de estudio')} · 📖 {link('glosario', 'Glosario')} · 🧭 {link('guias-de-rol', 'Guías de rol')}.",
    ]
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    block = "<!-- pdf-downloads:start -->" + chr(10) + chr(10).join(lines) + chr(10) + "<!-- pdf-downloads:end -->"
    text = re.sub(r"<!-- pdf-downloads:start -->.*?<!-- pdf-downloads:end -->", lambda _: block, text, flags=re.S)
    path.write_text(text, encoding="utf-8", newline=chr(10))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dir", default=str(ROOT / "build" / "pdf"))
    parser.add_argument("--create-release", action="store_true", help="crea el Release de GitHub con los PDF y las sumas")
    parser.add_argument("--skip-verify", action="store_true", help="solo para pruebas locales")
    args = parser.parse_args()
    directory = Path(args.dir)
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("dirty"):
        raise SystemExit("El manifiesto declara árbol sucio: genera de nuevo desde un commit limpio.")
    if not args.skip_verify:
        code = subprocess.run([sys.executable, str(ROOT / "scripts" / "verify_pdf.py"), "--dir", str(directory), "--release"]).returncode
        if code:
            raise SystemExit("La verificación falló: no se publica nada.")
    manifest["volumes"] = sorted(manifest["volumes"], key=sort_key)
    pdf_dir = ROOT / "pdf"
    (pdf_dir / "manifest.json").write_text(json.dumps(lean_manifest(manifest), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    sums = "".join(f"{e['sha256']}  {e['file']}\n" for e in manifest["volumes"])
    (pdf_dir / "SHA256SUMS").write_text(sums, encoding="utf-8", newline="\n")
    update_docs(manifest)
    update_readme(manifest)
    tag = release_tag(manifest)
    assets = [directory / e["file"] for e in manifest["volumes"]] + [pdf_dir / "SHA256SUMS"]
    print(f"Release: {tag}\nActivos que se publicarán ({len(assets)}):")
    for asset in assets:
        print(f"  {asset.name}  {asset.stat().st_size:>12,} bytes")
    if not args.create_release:
        return 0
    head = bp.git("rev-parse", "HEAD")
    notes = (f"PDF del {bp.PROGRAM}, generados el {manifest['date'][:10]} desde el commit {manifest['commit']}.\n\n"
             f"{len(manifest['volumes'])} volúmenes, verificados con `scripts/verify_pdf.py` (páginas, partes, clases, casos, glosario, "
             f"figuras, enlaces internos y marcadores). Sumas SHA-256 en `SHA256SUMS`. Reproducción y límites: docs/PDF.md.\n\n"
             f"Commit del repositorio al publicar: {head}.")
    cmd = ["gh", "release", "create", tag, *map(str, assets), "--repo", bp.REPO, "--title", f"PDF {manifest['date'][:10]} · {manifest['commit'][:8]}",
           "--notes", notes, "--target", manifest["commit"]]
    subprocess.run(cmd, check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
