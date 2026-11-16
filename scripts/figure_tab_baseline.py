"""Ratchet for figures that merely redraw a Markdown table.

``measure()`` counts, per part, the figures built with ``tab()`` (kind ``table``), the lesson
images whose alt text starts with "Tabla" and the diagrams that call ``Fig.table()``. The committed
``figure_tab_baseline.json`` holds the ceiling for each count; ``tests/test_figure_redesign.py``
fails when a count goes above it or when the file is stale (a count went below it).

    python scripts/figure_tab_baseline.py          # print the current counts
    python scripts/figure_tab_baseline.py --write  # lower the baseline to the current counts

``--write`` never raises a ceiling and never edits ``allowed_tables``.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

BASELINE = ROOT / "scripts" / "figure_tab_baseline.json"
IMAGE = re.compile(r"!\[([^\]]*)\]\(figures/([^)\s]+)\)")
CASE_IMAGE = re.compile(r"!\[([^\n]*?)\]\(\.\./figures/([^)\s]+)")
METRICS = ("tables", "table_alts", "embedded_tables")


def load() -> dict:
    return json.loads(BASELINE.read_text(encoding="utf-8"))


def measure() -> dict:
    from build_figures import collect

    allowed = set(load().get("allowed_tables", {}))
    counts = {metric: Counter() for metric in METRICS}
    kinds: dict[str, str] = {}
    for path, builder in collect().items():
        part = path.parent.parent.name.removeprefix("part-")
        fig = builder()
        kinds[path.name] = fig.kind
        if fig.kind == "table" and path.name not in allowed:
            counts["tables"][part] += 1
        elif fig.kind == "diagram" and fig.table_calls:
            counts["embedded_tables"][part] += 1
    alts: list[tuple[str, str, str]] = []
    for lesson in sorted((ROOT / "content").glob("part-*/SE-*.md")):
        part = lesson.parent.name.removeprefix("part-")
        for alt, name in IMAGE.findall(lesson.read_text(encoding="utf-8")):
            if alt.strip().lower().startswith("tabla") and name not in allowed:
                counts["table_alts"][part] += 1
            alts.append((part, name, alt))
    for case_file in sorted((ROOT / "casos").glob("*/*.md")):
        for alt, name in CASE_IMAGE.findall(case_file.read_text(encoding="utf-8")):
            if alt.strip().lower().startswith("tabla") and name not in allowed:
                counts["table_alts"]["casos"] += 1
            alts.append(("casos", name, alt))
    return {"counts": {m: dict(sorted(c.items())) for m, c in counts.items()}, "kinds": kinds, "alts": alts}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    current = measure()["counts"]
    for metric in METRICS:
        print(f"{metric}: {sum(current[metric].values())} {current[metric]}")
    if args.write:
        data = load() if BASELINE.exists() else {"schema_version": 1, "allowed_tables": {}}
        for metric in METRICS:
            old = data.get(metric, {})
            data[metric] = {part: min(old.get(part, n), n) for part, n in current[metric].items()}
        data["goal"] = "0 en todas las partes; la excepción solo entra por allowed_tables con justificación"
        BASELINE.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n", encoding="utf-8", newline="\n")
        print("BASELINE_WRITTEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
