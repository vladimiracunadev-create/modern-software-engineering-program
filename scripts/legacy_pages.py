"""Páginas de compatibilidad del portal tras la renumeración (ADR-007).

Se generan a partir de `docs/ID-MIGRATION.json` y solo dependen del estado real del programa:

- `site/legacy/index.html`: mapa de partes y clases antiguas hacia las actuales.
- `site/legacy/classes/SE-nnn.html` y `site/legacy/parts/NN.html`: una página por cada
  identificador antiguo, con un aviso y un enlace a su destino actual. No redirigen solas
  (sin actualización automática) para que quien llega con un identificador antiguo vea el cambio.
- `site/404.html`: GitHub Pages la sirve para cualquier dirección inexistente; explica el cambio de
  numeración y enlaza el mapa. Cubre las URL antiguas que quedaron vacantes (`classes/SE-409.html`,
  `parts/34.html`, etc.), que no pueden redirigir a otra clase sin ocupar un número reservado.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

try:
    import program_state as ps
except ModuleNotFoundError:  # importado como scripts.legacy_pages
    from scripts import program_state as ps

ROOT = Path(__file__).resolve().parents[1]
MIGRATION_PATH = ROOT / "docs" / "ID-MIGRATION.json"
PROGRAM_NAME = "Programa de Ingeniería de Software Moderna"
DATE = "23 de noviembre de 2026"


def load_migration() -> dict:
    return json.loads(MIGRATION_PATH.read_text(encoding="utf-8"))


def _page(title: str, description: str, css: str, body: str) -> str:
    return (
        '<!doctype html>\n<html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="description" content="{html.escape(description, quote=True)}">'
        f"<title>{html.escape(title)} · {PROGRAM_NAME}</title>"
        f'<link rel="stylesheet" href="{css}"></head><body>'
        '<a class="skip" href="#content">Saltar al contenido</a>'
        f'<main class="lesson" id="content">{body}</main>'
        f"<footer>{PROGRAM_NAME}</footer></body></html>\n"
    )


def _hero(eyebrow: str, heading: str, text: str) -> str:
    return (
        f'<header class="lesson-hero"><p class="eyebrow">{html.escape(eyebrow)}</p>'
        f"<h1>{html.escape(heading)}</h1><p>{html.escape(text)}</p></header>"
    )


def _notice(text: str) -> str:
    return f'<div class="notice">{text}</div>'


def _legacy_class_page(entry: dict, developed: set[int]) -> str:
    old, new = entry["old"], entry["new"]
    note = (
        f"La numeración cambió el {DATE} (ADR-007). "
        + ("El identificador y la dirección de esta clase no cambiaron." if not entry["changed"]
           else f"Esta clase se llama ahora {new}; el identificador {old} ya no designa a esta clase.")
    )
    nav = '<p><a href="../index.html">Mapa de identificadores antiguos</a> · <a href="../../index.html">Inicio</a></p>'
    link = f'<p><a href="../../classes/{new}.html">Abrir {new} · {html.escape(entry["title"])}</a></p>'
    body = (
        _hero(f"Identificador anterior {old}", f"{old} → {new}", entry["title"])
        + _notice(html.escape(note)) + link + nav
    )
    return _page(f"{old} → {new}", f"{old} ahora es {new}: {entry['title']}", "../../assets/styles.css", body)


def _legacy_part_page(entry: dict) -> str:
    old, new = entry["old"], entry["new"]
    note = (
        f"La numeración cambió el {DATE} (ADR-007). "
        + ("Esta parte conserva su número." if not entry["changed"]
           else f"La Parte {old} es ahora la Parte {new}; el número {old} ya no designa a esta parte.")
        + f" Clases: {entry['old_first_class']}–{entry['old_last_class']} antes, {entry['first_class']}–{entry['last_class']} ahora."
    )
    nav = '<p><a href="../index.html">Mapa de identificadores antiguos</a> · <a href="../../index.html">Inicio</a></p>'
    link = f'<p><a href="../../parts/{new}.html">Abrir la Parte {new} · {html.escape(entry["title"])}</a></p>'
    body = (
        _hero(f"Parte anterior {old}", f"Parte {old} → Parte {new}", entry["title"])
        + _notice(html.escape(note)) + link + nav
    )
    return _page(f"Parte {old} → Parte {new}", f"La Parte {old} ahora es la Parte {new}: {entry['title']}", "../../assets/styles.css", body)


def _index_page(migration: dict, developed_parts: set[int]) -> str:
    rows_parts = []
    for part in migration["parts"]:
        if part["old"] is None:
            rows_parts.append(
                f"<tr><td>—</td><td>{part['new']}</td><td>{html.escape(part['title'])} (reservada)</td>"
                f"<td>{part['first_class']}–{part['last_class']}</td><td>—</td></tr>"
            )
            continue
        rows_parts.append(
            f'<tr><td><a href="parts/{part["old"]}.html">{part["old"]}</a></td>'
            f'<td><a href="../parts/{part["new"]}.html">{part["new"]}</a></td>'
            f"<td>{html.escape(part['title'])}</td>"
            f"<td>{part['first_class']}–{part['last_class']}</td>"
            f"<td>{part['old_first_class']}–{part['old_last_class']}</td></tr>"
        )
    rows_classes = []
    for entry in migration["classes"]:
        rows_classes.append(
            f'<tr><td><a href="classes/{entry["old"]}.html">{entry["old"]}</a></td>'
            f'<td><a href="../classes/{entry["new"]}.html">{entry["new"]}</a></td>'
            f"<td>{html.escape(entry['title'])}</td></tr>"
        )
    reserved = ", ".join(migration["reserved_parts"])
    body = (
        _hero("Compatibilidad", "Mapa de identificadores antiguos",
              f"Hasta el {DATE} las partes seguían el orden de aparición; desde entonces siguen el orden de estudio.")
        + _notice(
            "Las Partes 00–22 conservan número e identificadores. Las partes y clases que cambiaron se listan abajo. "
            f"Las Partes {reserved} son huecos reservados y planificados. La regla es "
            "<code>ID nuevo = 12 × parte nueva + posición dentro de la parte</code>. "
            'El mapa completo y la decisión están en <a href="https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/docs/ID-MIGRATION.md">ID-MIGRATION.md</a> '
            'y en <a href="https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md">ADR-007</a>.'
        )
        + '<h2 id="partes">Partes</h2><div class="table-wrap"><table><thead><tr><th>Parte antigua</th><th>Parte nueva</th>'
        "<th>Título</th><th>Clases nuevas</th><th>Clases antiguas</th></tr></thead><tbody>"
        + "".join(rows_parts) + "</tbody></table></div>"
        + '<h2 id="clases">Clases</h2><div class="table-wrap"><table><thead><tr><th>ID antiguo</th><th>ID nuevo</th><th>Título</th></tr></thead><tbody>'
        + "".join(rows_classes) + "</tbody></table></div>"
        + '<p><a href="../index.html">Inicio</a></p>'
    )
    return _page("Mapa de identificadores antiguos", "Equivalencia entre los identificadores de partes y clases anteriores al 23 de noviembre de 2026 y los vigentes.", "../assets/styles.css", body)


def _not_found_page() -> str:
    base = "https://vladimiracunadev-create.github.io/modern-software-engineering-program/"
    note = (
        "No hay ninguna página en esta dirección. Desde el 23 de noviembre de 2026 las partes y las clases siguen la "
        "secuencia pedagógica (ADR-007): un identificador o una dirección guardados antes pueden corresponder ahora a "
        "otra clase, o a una parte planificada que todavía no tiene clases (las Partes 34 y 42 están reservadas)."
    )
    body = (
        _hero("Error 404", "Página no encontrada", "Es posible que la dirección use la numeración anterior.")
        + _notice(html.escape(note))
        + f'<p><a href="{base}legacy/index.html">Abrir el mapa de identificadores antiguos</a> · <a href="{base}">Inicio</a></p>'
    )
    return _page("Página no encontrada", "La dirección no existe o usa la numeración anterior a ADR-007.", f"{base}assets/styles.css", body)


def expected_files(program: dict | None = None) -> dict[Path, str]:
    migration = load_migration()
    developed = set(ps.developed_parts())
    result: dict[Path, str] = {ROOT / "site/legacy/index.html": _index_page(migration, developed)}
    for entry in migration["classes"]:
        result[ROOT / "site/legacy/classes" / f"{entry['old']}.html"] = _legacy_class_page(entry, developed)
    for entry in migration["parts"]:
        if entry["old"] is not None:
            result[ROOT / "site/legacy/parts" / f"{entry['old']}.html"] = _legacy_part_page(entry)
    result[ROOT / "site/404.html"] = _not_found_page()
    return result
