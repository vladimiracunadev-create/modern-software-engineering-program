"""Generate every static SVG figure into content/part-XX/figures/.

Figure definitions live in ``scripts/figures_partXX_<letter>.py`` modules that
export a ``FIGURES`` mapping of file name to builder. Run
``python scripts/build_figures.py`` to regenerate and ``--check`` to verify that
the committed files match the definitions.
"""
from __future__ import annotations

import argparse
import importlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def collect() -> dict[Path, object]:
    figures: dict[Path, object] = {}
    for module_path in sorted((ROOT / "scripts").glob("figures_part[0-9][0-9]_*.py")):
        part = re.match(r"figures_part(\d\d)_", module_path.name).group(1)
        module = importlib.import_module(module_path.stem)
        for name, builder in module.FIGURES.items():
            target = ROOT / "content" / f"part-{part}" / "figures" / name
            if target in figures:
                raise SystemExit(f"duplicate figure {name}")
            figures[target] = builder
    return figures


FIGURES = {path.name: builder for path, builder in collect().items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    figures = collect()
    for path, builder in figures.items():
        svg = builder().svg()
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != svg:
                stale.append(path.name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(svg, encoding="utf-8", newline="\n")
    if stale:
        print("FIGURES_STALE: " + ", ".join(stale), file=sys.stderr)
        return 1
    print(("FIGURES_CHECK_OK" if args.check else "FIGURES_BUILD_OK") + f": {len(figures)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
