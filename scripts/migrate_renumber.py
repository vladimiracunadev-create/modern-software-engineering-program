"""Migración atómica a la secuencia pedagógica (ADR-007).

Pasa el programa de 49 partes / 588 clases (numeración histórica por orden de
aparición) a 51 partes / 612 clases en orden pedagógico, con las Partes 34 y 42
reservadas y planificadas. Las Partes 00–22 conservan número y clases.

Subcomandos:

    python scripts/migrate_renumber.py dry-run [--report RUTA]
        Calcula TODOS los cambios (renombres, reescrituras, avisos) sin escribir
        nada y verifica los conteos de origen (588 clases, 49 partes, 45 roles,
        16 casos).
    python scripts/migrate_renumber.py apply
        Aplica los renombres y las reescrituras. Exige un árbol limpio y la
        etiqueta de respaldo. Después hay que regenerar (build_*.py).
    python scripts/migrate_renumber.py verify
        Comprueba el resultado: conteos nuevos, ningún nombre antiguo huérfano.
    python scripts/migrate_renumber.py emit-map
        Escribe docs/ID-MIGRATION.json y docs/ID-MIGRATION.md a partir de la
        etiqueta de respaldo (numeración antigua) y del blueprint nuevo.

La herramienta es de un solo uso: queda como evidencia y para poder auditar el mapa.
Las reglas de reescritura se aplican en una sola pasada (sustitución simultánea), por lo
que ningún identificador se transforma dos veces.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAG = "pre-reorder-2026-11-23"
CLASSES_PER_PART = 12

# nuevo número de parte -> número antiguo (None = parte nueva, planificada)
NEW_TO_OLD: dict[int, int | None] = {n: n for n in range(0, 23)}
NEW_TO_OLD.update({
    23: 48, 24: 23, 25: 24, 26: 43, 27: 25, 28: 44, 29: 26, 30: 45, 31: 27, 32: 28, 33: 29,
    34: None, 35: 30, 36: 31, 37: 47, 38: 32, 39: 33, 40: 34, 41: 35, 42: None, 43: 36, 44: 37,
    45: 40, 46: 38, 47: 39, 48: 41, 49: 42, 50: 46,
})
OLD_TO_NEW: dict[int, int] = {old: new for new, old in NEW_TO_OLD.items() if old is not None}
NEW_PART_COUNT = len(NEW_TO_OLD)  # 51
OLD_PART_COUNT = len(OLD_TO_NEW)  # 49
OLD_CLASS_COUNT = OLD_PART_COUNT * CLASSES_PER_PART  # 588
NEW_CLASS_COUNT = NEW_PART_COUNT * CLASSES_PER_PART  # 612
RESERVED_PARTS = [n for n, old in NEW_TO_OLD.items() if old is None]  # [34, 42]


def map_part(old: int) -> int:
    return OLD_TO_NEW.get(old, old)


def map_class(old: int) -> int:
    """SE-nnn antiguo (1..588) -> SE-nnn nuevo; fuera de rango no cambia."""
    if not 1 <= old <= OLD_CLASS_COUNT:
        return old
    old_part, offset = divmod(old - 1, CLASSES_PER_PART)
    return map_part(old_part) * CLASSES_PER_PART + offset + 1


assert len(set(OLD_TO_NEW.values())) == OLD_PART_COUNT
assert sorted(set(NEW_TO_OLD) - set(RESERVED_PARTS)) == sorted(OLD_TO_NEW.values())
assert sorted(map_class(n) for n in range(1, OLD_CLASS_COUNT + 1)) == sorted(
    n for n in range(1, NEW_CLASS_COUNT + 1)
    if (n - 1) // CLASSES_PER_PART not in RESERVED_PARTS
)

# --- clasificación de archivos ------------------------------------------------------------

# Árboles que se borran y regeneran (classes/, site/): no se reescriben.
GENERATED_TREES = ("classes/", "site/")
# Documentos históricos: conservan los IDs antiguos; solo se corrigen los destinos de enlace
# para que sigan resolviendo a la clase migrada. Reciben una nota que remite al mapa.
HISTORICAL = (
    "docs/adr/ADR-002-", "docs/adr/ADR-003-", "docs/adr/ADR-004-", "docs/adr/ADR-005-",
    "docs/adr/ADR-006-", "CHANGELOG.md", "docs/PART-EXECUTION-TRACKER.md",
    "docs/PROGRAM-COVERAGE-AUDIT-", "docs/PHASE3-CONTENT-AUDIT.md", "docs/PHASE4-CONTENT-AUDIT.md",
    "docs/METHODOLOGY-GAP-AUDIT-", "docs/CASE-LABEL-CORRECTION.md", "docs/LICENSING_HISTORY.md",
)
# Ni se reescriben ni se marcan: el mapa y su documentación, esta herramienta y los guiones
# de una sola vez que documentan hechos pasados.
EXEMPT = (
    "scripts/migrate_renumber.py", "docs/ID-MIGRATION.", "docs/adr/ADR-007-",
    "scripts/retire_fictional_case_labels.py", "scripts/enrich_pedagogical_traceability.py",
    "sources/pedagogical/", "schemas/",
)
TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".yaml", ".yml", ".txt", ".js", ".html", ".css", ".jsonc", ".toml",
    ".ps1", ".sh", ".tsv", ".rs", "",
}
BINARY_SUFFIXES = {".svg", ".png", ".jpg", ".pdf", ".ico", ".gif", ".webp"}

# --- patrones --------------------------------------------------------------------------------

BOUND = r"(?<![A-Za-z0-9_])"
CLASS_RE = re.compile(BOUND + r"(SE|se)-(\d{3})(?!\d)")
PART_DIR_RE = re.compile(BOUND + r"part-(\d\d)(?!\d)")
PART_SCRIPT_RE = re.compile(r"(?<=_)part(\d\d)(?!\d)")
# «Parte 24», «Partes 40–44», «Partes 23, 24 y 25», «Parte 40/41»
PARTE_RE = re.compile(
    r"\b([Pp]artes?)(\s+)(\d\d)((?:\s*(?:[–—-]|,|/|\by\b|\be\b|\ba\b|\bal\b|\bhasta\b)\s*\d\d(?!\d))*)(?!\d)"
)
PARTE_TAIL_NUM = re.compile(r"\d\d")
PARTE_TAIL_SEP = re.compile(r"(\s*(?:[–—-]|,|/|\by\b|\be\b|\ba\b|\bal\b|\bhasta\b)\s*)(\d\d)")
LINK_TARGET_RE = re.compile(r"(\]\()([^)\s]*)((?:\s+\"[^\"]*\")?\))")
HREF_RE = re.compile(r"((?:href|src)=\")([^\"]*)(\")")
# rangos de clases: SE-361–SE-372, `SE-361`–`SE-372`, SE-361..SE-372, SE-361 a SE-372
CLASS_RANGE_RE = re.compile(
    r"SE-(\d{3})`?\s*(?:–|—|-|\.\.|…|\ba\b|\bhasta\b)\s*`?SE-(\d{3})"
)
PART_ID_RE = re.compile(r"^\s+\"(\d\d)\":", re.M)


def fmt_runs(numbers: list[int]) -> str:
    runs: list[tuple[int, int]] = []
    for n in sorted(set(numbers)):
        if runs and runs[-1][1] == n - 1:
            runs[-1] = (runs[-1][0], n)
        else:
            runs.append((n, n))
    pieces = [f"{a:02d}" if a == b else f"{a:02d}–{b:02d}" for a, b in runs]
    if len(pieces) > 1:
        return ", ".join(pieces[:-1]) + " y " + pieces[-1]
    return pieces[0]


class Flags:
    """Casos que una máquina no debe decidir sola: se listan para revisión humana."""

    def __init__(self) -> None:
        self.items: list[dict[str, str]] = []

    def add(self, path: str, kind: str, text: str) -> None:
        self.items.append({"path": path, "kind": kind, "text": text[:160]})


def rewrite_text(text: str, path: str, flags: Flags | None = None, links_only: bool = False) -> str:
    """Una sola pasada: cada ID antiguo se sustituye una vez por su valor nuevo."""

    def sub_class(match: re.Match[str]) -> str:
        return f"{match.group(1)}-{map_class(int(match.group(2))):03d}"

    def sub_part_dir(match: re.Match[str]) -> str:
        return f"part-{map_part(int(match.group(1))):02d}"

    def sub_part_script(match: re.Match[str]) -> str:
        return f"part{map_part(int(match.group(1))):02d}"

    def sub_parte(match: re.Match[str]) -> str:
        word, space, first, tail = match.groups()
        old_numbers = [int(first)] + [int(n) for n in PARTE_TAIL_NUM.findall(tail)]
        if any(n >= OLD_PART_COUNT for n in old_numbers):
            return match.group(0)
        # Rango «A–B»: se expande al conjunto antiguo y se vuelve a agrupar en el nuevo.
        if tail and re.fullmatch(r"\s*(?:[–—-]|\ba\b|\bal\b|\bhasta\b)\s*\d\d", tail):
            lo, hi = old_numbers
            old_set = list(range(lo, hi + 1))
            new_set = [map_part(n) for n in old_set]
            if new_set == list(range(new_set[0], new_set[0] + len(new_set))):
                return f"{word}{space}{new_set[0]:02d}–{new_set[-1]:02d}"
            if flags is not None:
                flags.add(path, "range-split", match.group(0))
            return word[0] + "artes" + f"{space}{fmt_runs(new_set)}"
        if flags is not None and any(map_part(n) != n for n in old_numbers):
            around = text[max(0, match.start() - 60):match.end() + 60]
            if re.search(r"ISO|IEC|IEEE|RFC|norma|est[aá]ndar|NIST|OWASP", around):
                flags.add(path, "parte-near-standard", " ".join(around.split()))
        mapped_first = f"{map_part(int(first)):02d}"
        out = f"{word}{space}{mapped_first}"
        if tail:
            out += PARTE_TAIL_SEP.sub(lambda m: m.group(1) + f"{map_part(int(m.group(2))):02d}", tail)
        return out

    def convert(chunk: str) -> str:
        chunk = CLASS_RE.sub(sub_class, chunk)
        chunk = PART_DIR_RE.sub(sub_part_dir, chunk)
        chunk = PART_SCRIPT_RE.sub(sub_part_script, chunk)
        return chunk

    if links_only:
        text = LINK_TARGET_RE.sub(lambda m: m.group(1) + convert(m.group(2)) + m.group(3), text)
        return HREF_RE.sub(lambda m: m.group(1) + convert(m.group(2)) + m.group(3), text)

    if flags is not None:
        for match in CLASS_RANGE_RE.finditer(text):
            lo, hi = int(match.group(1)), int(match.group(2))
            if lo <= OLD_CLASS_COUNT and hi <= OLD_CLASS_COUNT and lo <= hi:
                new_lo, new_hi = map_class(lo), map_class(hi)
                if new_hi - new_lo != hi - lo or (hi - lo >= CLASSES_PER_PART - 1 and (lo - 1) // 12 != (hi - 1) // 12):
                    flags.add(path, "class-range", match.group(0))
    text = PARTE_RE.sub(sub_parte, text)
    return convert(text)


def rewrite_path(path: str) -> str:
    """Nuevo nombre de archivo o carpeta para una ruta rastreada."""
    if path.startswith(GENERATED_TREES) or path.startswith("labs/"):
        return path
    return convert_path(path)


def convert_path(path: str) -> str:
    path = PART_DIR_RE.sub(lambda m: f"part-{map_part(int(m.group(1))):02d}", path)
    path = PART_SCRIPT_RE.sub(lambda m: f"part{map_part(int(m.group(1))):02d}", path)
    path = CLASS_RE.sub(lambda m: f"{m.group(1)}-{map_class(int(m.group(2))):03d}", path)
    return path


# --- git y sistema de archivos ------------------------------------------------------------

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8")


def tracked_files() -> list[str]:
    return [line for line in git("ls-files").splitlines() if line]


def is_text(path: str) -> bool:
    suffix = Path(path).suffix.lower()
    return suffix not in BINARY_SUFFIXES and (suffix in TEXT_SUFFIXES or suffix == "")


def classify(path: str) -> str:
    if path.startswith(GENERATED_TREES):
        return "generated-tree"
    if any(path.startswith(prefix) for prefix in EXEMPT):
        return "exempt"
    if any(path.startswith(prefix) for prefix in HISTORICAL):
        return "historical"
    if not is_text(path):
        return "binary"
    return "living"


# --- conteos --------------------------------------------------------------------------------

def count_state() -> dict[str, int]:
    content = ROOT / "content"
    part_dirs = sorted(p for p in content.glob("part-*") if p.is_dir())
    class_files = [f for p in part_dirs for f in p.glob("SE-*.md")]
    roles = [p for p in (ROOT / "roles").glob("*.md") if p.name != "README.md"]
    cases = [p for kind in ("exito", "fallo") for p in (ROOT / "casos" / kind).glob("*.md") if p.name != "README.md"]
    return {
        "parts_with_content": len(part_dirs),
        "classes_with_content": len(class_files),
        "roles": len(roles),
        "cases": len(cases),
    }


def plan() -> dict:
    files = tracked_files()
    renames: dict[str, str] = {}
    for path in files:
        target = rewrite_path(path)
        if target != path:
            renames[path] = target
    flags = Flags()
    rewrites: dict[str, str] = {}
    categories: Counter[str] = Counter()
    for path in files:
        kind = classify(path)
        categories[kind] += 1
        if kind in ("generated-tree", "exempt", "binary"):
            continue
        file_path = ROOT / path
        try:
            original = file_path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        updated = rewrite_text(original, path, flags, links_only=(kind == "historical"))
        if updated != original:
            rewrites[path] = updated
    return {"files": files, "renames": renames, "rewrites": rewrites, "flags": flags, "categories": categories}


def verify_source_counts() -> list[str]:
    problems = []
    state = count_state()
    expected = {"parts_with_content": OLD_PART_COUNT, "classes_with_content": OLD_CLASS_COUNT, "roles": 45, "cases": 16}
    for key, value in expected.items():
        if state[key] != value:
            problems.append(f"{key}: esperado {value}, hay {state[key]}")
    return problems


# --- subcomandos --------------------------------------------------------------------------------

def cmd_dry_run(args: argparse.Namespace) -> int:
    problems = verify_source_counts()
    if problems:
        print("CONTEOS DE ORIGEN INESPERADOS:\n  " + "\n  ".join(problems), file=sys.stderr)
        return 1
    result = plan()
    renames, rewrites, flags = result["renames"], result["rewrites"], result["flags"]
    by_dir: Counter[str] = Counter()
    for old in renames:
        by_dir["/".join(old.split("/")[:2]) if old.startswith("content/") else old.split("/")[0]] += 1
    figure_renames = sum(1 for old in renames if "/figures/" in old and old.startswith("content/"))
    print("== Origen verificado: 588 clases migradas, 49 partes, 45 roles, 16 casos intactos")
    print(f"== Etiqueta de respaldo: {TAG}: {'presente' if git('tag', '--list', TAG).strip() else 'AUSENTE'}")
    print(f"== Archivos rastreados: {len(result['files'])}  ({dict(result['categories'])})")
    print(f"== Renombres: {len(renames)}  (figuras: {figure_renames}; carpetas de contenido movidas: "
          f"{len({o.split('/')[1] for o in renames if o.startswith('content/')})})")
    print(f"== Archivos que se reescriben: {len(rewrites)}")
    kinds = Counter(item["kind"] for item in flags.items)
    print(f"== Avisos para revisión: {dict(kinds)}")
    class_moves = sum(1 for n in range(1, OLD_CLASS_COUNT + 1) if map_class(n) != n)
    print(f"== Clases con ID distinto: {class_moves} de {OLD_CLASS_COUNT}; partes con número distinto: "
          f"{sum(1 for o, n in OLD_TO_NEW.items() if o != n)} de {OLD_PART_COUNT}")
    print(f"== Resultado: {NEW_PART_COUNT} partes y {NEW_CLASS_COUNT} clases (huecos reservados: partes {RESERVED_PARTS})")
    if args.report:
        report = {
            "renames": renames,
            "rewrites": sorted(rewrites),
            "flags": flags.items,
            "categories": dict(result["categories"]),
        }
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"== Informe completo: {args.report}")
    return 0


def cmd_apply(args: argparse.Namespace) -> int:
    if git("status", "--porcelain").strip():
        print("El árbol de trabajo no está limpio; confirma o descarta los cambios antes de migrar.", file=sys.stderr)
        return 1
    if not git("tag", "--list", TAG).strip():
        print(f"Falta la etiqueta de respaldo {TAG}.", file=sys.stderr)
        return 1
    problems = verify_source_counts()
    if problems:
        print("CONTEOS DE ORIGEN INESPERADOS:\n  " + "\n  ".join(problems), file=sys.stderr)
        return 1
    result = plan()
    renames, rewrites = result["renames"], result["rewrites"]

    # 1. Contenido reescrito en su sitio actual (antes de mover, para leer la ruta antigua).
    for path, updated in rewrites.items():
        (ROOT / path).write_text(updated, encoding="utf-8", newline="\n")

    # 2. Renombres en dos fases por una carpeta de paso, para evitar colisiones.
    staging = Path(tempfile.mkdtemp(prefix="renumber-", dir=ROOT))
    try:
        moved: list[tuple[Path, str]] = []
        for index, (old, new) in enumerate(sorted(renames.items())):
            source = ROOT / old
            if not source.is_file():
                continue
            holder = staging / f"{index:06d}"
            os.replace(source, holder)
            moved.append((holder, new))
        for holder, new in moved:
            destination = ROOT / new
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(holder, destination)
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    # 3. Limpieza de carpetas vacías de contenido y scripts.
    for base in (ROOT / "content", ROOT / "scripts"):
        for directory in sorted((p for p in base.rglob("*") if p.is_dir()), reverse=True):
            if not any(directory.iterdir()):
                directory.rmdir()

    # 4. Los árboles generados se borran: los reconstruyen los generadores.
    subprocess.check_call(["git", "rm", "-r", "-q", "--ignore-unmatch", "classes/part-*", "site/classes", "site/parts"], cwd=ROOT)
    for leftover in list((ROOT / "classes").glob("part-*")) + [ROOT / "site/classes", ROOT / "site/parts"]:
        if leftover.exists():
            shutil.rmtree(leftover, ignore_errors=True)
    print(f"MIGRACION_APLICADA: {len(renames)} renombres, {len(rewrites)} archivos reescritos")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    problems: list[str] = []
    state = count_state()
    expected = {"parts_with_content": NEW_PART_COUNT - len(RESERVED_PARTS), "classes_with_content": OLD_CLASS_COUNT, "roles": 45, "cases": 16}
    for key, value in expected.items():
        if state[key] != value:
            problems.append(f"{key}: esperado {value}, hay {state[key]}")
    for number in RESERVED_PARTS:
        if (ROOT / "content" / f"part-{number:02d}").exists():
            problems.append(f"la parte reservada {number:02d} no debe tener contenido todavía")
    # cada clase vive en la carpeta de su parte
    seen: Counter[str] = Counter()
    for path in sorted((ROOT / "content").glob("part-*/SE-*.md")):
        part = int(path.parent.name.split("-")[1])
        number = int(path.stem.split("-")[1])
        seen[path.stem] += 1
        if (number - 1) // CLASSES_PER_PART != part:
            problems.append(f"{path.relative_to(ROOT)} no está en la parte de su número")
        first = path.read_text(encoding="utf-8").splitlines()[0]
        if not first.startswith(f"# {path.stem} —"):
            problems.append(f"{path.relative_to(ROOT)}: encabezado inesperado: {first[:60]}")
    problems += [f"ID duplicado: {k}" for k, v in seen.items() if v > 1]
    # figuras: el prefijo de cada archivo es la clase de su carpeta
    for svg in (ROOT / "content").glob("part-*/figures/*.svg"):
        part = int(svg.parent.parent.name.split("-")[1])
        match = re.match(r"se-(\d{3})-", svg.name)
        if not match or (int(match.group(1)) - 1) // CLASSES_PER_PART != part:
            problems.append(f"figura fuera de su parte: {svg.relative_to(ROOT)}")
    if problems:
        print("VERIFICACION_FALLIDA:\n  " + "\n  ".join(problems[:60]), file=sys.stderr)
        return 1
    print(f"VERIFICACION_OK: {state}")
    return 0


def _load_old_program() -> dict:
    return json.loads(git("show", f"{TAG}:curriculum.yaml"))


def cmd_emit_map(args: argparse.Namespace) -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    import build_program_blueprint as blueprint  # noqa: PLC0415

    old = _load_old_program()
    old_parts = {int(part["id"]): part for part in old["parts"]}
    new_plan = {int(part["id"]): part for part in blueprint.build_full_plan()}
    old_titles = {lesson["id"]: lesson for part in old["parts"] for lesson in part["lessons"]}
    new_titles = {lesson["id"]: lesson for part in new_plan.values() for lesson in part["lessons"]}

    parts = []
    for new_number in range(NEW_PART_COUNT):
        old_number = NEW_TO_OLD[new_number]
        new_part = new_plan[new_number]
        parts.append({
            "new": f"{new_number:02d}",
            "old": None if old_number is None else f"{old_number:02d}",
            "title": new_part["title"],
            "status": "reserved-planned" if old_number is None else "developed",
            "old_path": None if old_number is None else old_parts[old_number]["path"],
            "new_path": new_part["path"],
            "first_class": new_part["lessons"][0]["id"],
            "last_class": new_part["lessons"][-1]["id"],
            "old_first_class": None if old_number is None else old_parts[old_number]["lessons"][0]["id"],
            "old_last_class": None if old_number is None else old_parts[old_number]["lessons"][-1]["id"],
            "changed": old_number != new_number,
        })
    classes = []
    for number in range(1, OLD_CLASS_COUNT + 1):
        old_id = f"SE-{number:03d}"
        new_id = f"SE-{map_class(number):03d}"
        old_lesson, new_lesson = old_titles[old_id], new_titles[new_id]
        if old_lesson["title"] != new_lesson["title"]:
            raise SystemExit(f"El título de {old_id} no coincide con {new_id}: {old_lesson['title']} / {new_lesson['title']}")
        classes.append({
            "old": old_id,
            "new": new_id,
            "title": new_lesson["title"],
            "changed": old_id != new_id,
            "old_path": old_lesson["path"],
            "new_path": new_lesson["path"],
            "old_url": f"classes/{old_id}.html",
            "new_url": f"classes/{new_id}.html",
        })
    payload = {
        "schema_version": 1,
        "decision": "docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md",
        "backup_tag": TAG,
        "old_scope": {"parts": OLD_PART_COUNT, "classes": OLD_CLASS_COUNT},
        "new_scope": {"parts": NEW_PART_COUNT, "classes": NEW_CLASS_COUNT},
        "reserved_parts": [f"{n:02d}" for n in RESERVED_PARTS],
        "rules": {
            "class_id": "new = 12 * new_part + (old - 12 * old_part)",
            "figures": "content/part-NN/figures/se-NNN-<nombre>.svg conserva <nombre>; cambian NN y NNN",
            "experiments": "scripts/figures_partNN_*.py y scripts/experiments_partNN_*.py cambian NN",
        },
        "parts": parts,
        "classes": classes,
    }
    out = ROOT / "docs" / "ID-MIGRATION.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")

    lines = [
        "# Mapa de migración de identificadores (ADR-007)",
        "",
        "Este mapa se generó con `scripts/migrate_renumber.py emit-map` y vive también en",
        "[`ID-MIGRATION.json`](ID-MIGRATION.json), que es la fuente que leen las páginas",
        "de redirección del portal. La decisión y sus razones están en",
        "[ADR-007](adr/ADR-007-pedagogical-renumbering-and-new-parts.md).",
        "",
        "## Cómo usarlo",
        "",
        "- Una referencia anterior al 2026-11-23 (`SE-nnn` o «Parte NN») usa la numeración histórica",
        "  por orden de aparición. Busca la parte en la primera tabla; el ID nuevo de una clase es",
        "  `ID nuevo = 12 × parte nueva + posición dentro de la parte` (la posición no cambia).",
        "- Las Partes 00–22 conservan número y clases. Cambian las Partes antiguas 23–48.",
        "- Las Partes 34 y 42 son huecos reservados: aún no tienen clases (`SE-409`–`SE-420`",
        "  y `SE-505`–`SE-516`). Los IDs que antes ocupaban esos números se movieron a otras partes.",
        f"- La etiqueta Git `{TAG}` conserva el árbol anterior completo, con la numeración histórica.",
        "- Una URL antigua `classes/SE-nnn.html` ya no corresponde a la misma clase cuando el número",
        "  cambió: el portal ofrece `site/legacy/` con una página por cada ID y parte antiguos que",
        "  enlaza su destino actual. Las direcciones vacantes (partes 34 y 42) muestran `404.html`,",
        "  que explica el cambio.",
        "",
        "## Partes",
        "",
        "| Parte nueva | Parte antigua | Título | Clases nuevas | Clases antiguas | Estado |",
        "| ---: | ---: | --- | --- | --- | --- |",
    ]
    for part in parts:
        old_label = "—" if part["old"] is None else part["old"]
        old_range = "—" if part["old"] is None else f"{part['old_first_class']}–{part['old_last_class']}"
        status = "reservada, planificada" if part["old"] is None else ("desarrollada, renumerada" if part["changed"] else "desarrollada, sin cambios")
        lines.append(f"| {part['new']} | {old_label} | {part['title']} | {part['first_class']}–{part['last_class']} | {old_range} | {status} |")
    lines += [
        "",
        "## Clases que cambian de ID",
        "",
        "Las clases se mueven por partes completas de doce (diez clases, un taller y un proyecto) y",
        "conservan su posición. La tabla por clase está en [`ID-MIGRATION.json`](ID-MIGRATION.json)",
        "(`classes[]`: `old`, `new`, `old_path`, `new_path`, `old_url`, `new_url`); aquí van los rangos.",
        "",
        "| Rango antiguo | Rango nuevo | Parte nueva |",
        "| --- | --- | --- |",
    ]
    for part in parts:
        if part["changed"] and part["old"] is not None:
            lines.append(f"| {part['old_first_class']}–{part['old_last_class']} | {part['first_class']}–{part['last_class']} | {part['new']} · {part['title']} |")
    lines += [
        "",
        "## Rutas, figuras y archivos",
        "",
        "| Elemento | Regla |",
        "| --- | --- |",
        "| Carpeta de contenido | `content/part-AA/` pasa a `content/part-NN/` |",
        "| Clase fuente | `content/part-AA/SE-aaa.md` pasa a `content/part-NN/SE-nnn.md` |",
        "| Figuras | `content/part-AA/figures/se-aaa-<nombre>.svg` pasa a `content/part-NN/figures/se-nnn-<nombre>.svg` |",
        "| Clase generada | `classes/part-AA-<parte>/se-aaa-<clase>/` pasa a `classes/part-NN-<parte>/se-nnn-<clase>/` |",
        "| Portal | `site/classes/SE-aaa.html` y `site/parts/AA.html` pasan a los números nuevos |",
        "| Guiones | `scripts/figures_partAA_*.py` y `scripts/experiments_partAA_*.py` pasan a `partNN` |",
        "| Documentos históricos | ADR-002 a ADR-006, CHANGELOG, tracker y auditorías fechadas conservan los IDs antiguos; sus enlaces apuntan a la clase migrada |",
        "",
    ]
    (ROOT / "docs" / "ID-MIGRATION.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"MAPA_EMITIDO: {len(parts)} partes, {len(classes)} clases")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    dry = sub.add_parser("dry-run")
    dry.add_argument("--report", default="")
    dry.set_defaults(func=cmd_dry_run)
    sub.add_parser("apply").set_defaults(func=cmd_apply)
    sub.add_parser("verify").set_defaults(func=cmd_verify)
    sub.add_parser("emit-map").set_defaults(func=cmd_emit_map)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
