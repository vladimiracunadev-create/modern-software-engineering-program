from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".txt"}
SKIP_PARTS = {".git", "__pycache__", "node_modules", ".venv"}
SUSPICIOUS = (
    "\u006d\u00c3",
    "\u0069\u006e\u0066\u006f\u0072\u006d\u0061\u0063\u0069\u00c3",
    "\u00e2\u20ac\u201d",
    "\u00e2\u20ac\u201c",
    "\u00f0\u0178",
    "\u00c2\u00b7",
)


def validate() -> list[str]:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        data = path.read_bytes()
        name = path.relative_to(ROOT).as_posix()
        if data.startswith(b"\xef\xbb\xbf"):
            failures.append(f"UTF-8 BOM: {name}")
        if b"\x00" in data:
            failures.append(f"NUL byte: {name}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append(f"invalid UTF-8: {name}: {error}")
            continue
        if any(token in text for token in SUSPICIOUS):
            failures.append(f"possible mojibake: {name}")
    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1
    print("ENCODING_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
