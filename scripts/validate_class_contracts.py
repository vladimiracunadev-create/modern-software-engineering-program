from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_phase2 import REQUIRED_CLASS_SECTIONS


def main() -> int:
    program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    failures: list[str] = []
    checked = 0
    for part in program["parts"]:
        for lesson in part["lessons"]:
            directory = ROOT / lesson["path"]
            readme = directory / "README.md"
            metadata_path = directory / "lesson.json"
            if not readme.exists() or not metadata_path.exists():
                failures.append(f"missing class files: {lesson['id']}")
                continue
            text = readme.read_text(encoding="utf-8")
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if metadata["id"] != lesson["id"] or metadata["status"] != lesson["status"]:
                failures.append(f"metadata drift: {lesson['id']}")
            missing = [section for section in REQUIRED_CLASS_SECTIONS if section not in text]
            if missing:
                failures.append(f"contract sections missing: {lesson['id']}: {missing}")
            if lesson["status"] != "PLANNED" and "Pendiente de desarrollar" in text:
                failures.append(f"non-planned class still contains placeholders: {lesson['id']}")
            checked += 1
    if failures:
        print("\n".join(failures[:50]), file=sys.stderr)
        return 1
    if checked != 480:
        print(f"Expected 480 classes, checked {checked}", file=sys.stderr)
        return 1
    print(f"CLASS_CONTRACTS_OK: {checked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
