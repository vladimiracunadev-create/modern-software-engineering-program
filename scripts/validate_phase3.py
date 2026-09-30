from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = [
    "## Ficha", "## Prerrequisitos", "## Problema auténtico",
    "## Objetivos observables", "## Mapa conceptual",
    "## Conceptos y decisiones", "## Ejemplo mínimo",
    "## Ejemplo profesional", "## Práctica guiada", "## Ejercicios",
    "## Fallo controlado y diagnóstico", "## Entorno y archivos clave",
    "## Seguridad, ética y accesibilidad", "## Transferencia",
    "## Evaluación y evidencia", "## Fuentes", "## Límites y siguiente paso",
]


def main() -> int:
    program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    source_catalog = json.loads((ROOT / "sources/phase3.json").read_text(encoding="utf-8"))
    source_ids = {source["id"] for source in source_catalog["sources"]}
    statuses = Counter()
    hashes = set()
    failures: list[str] = []
    draft_count = 0

    for part in program["parts"]:
        for lesson in part["lessons"]:
            statuses[lesson["status"]] += 1
            directory = ROOT / lesson["path"]
            if lesson["number"] > 180:
                continue
            draft_count += 1
            readme = directory / "README.md"
            activity_path = directory / "activity.yaml"
            rubric_path = directory / "rubric.json"
            for path in (readme, activity_path, rubric_path):
                if not path.is_file():
                    failures.append(f"missing phase 3 file: {path.relative_to(ROOT)}")
            if not all(path.is_file() for path in (readme, activity_path, rubric_path)):
                continue
            text = readme.read_text(encoding="utf-8")
            if "Estado: **PLANNED · BORRADOR EN REVISIÓN**" not in text or "Pendiente de desarrollar" in text:
                failures.append(f"invalid maturity content: {lesson['id']}")
            missing = [section for section in REQUIRED_SECTIONS if section not in text]
            if missing:
                failures.append(f"missing sections {lesson['id']}: {missing}")
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if digest in hashes:
                failures.append(f"duplicate class document: {lesson['id']}")
            hashes.add(digest)

            activity = json.loads(activity_path.read_text(encoding="utf-8"))
            rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
            if activity.get("class_id") != lesson["id"] or activity.get("status") != "PLANNED":
                failures.append(f"activity contract drift: {lesson['id']}")
            if not set(activity.get("source_ids", [])).issubset(source_ids):
                failures.append(f"unresolved phase 3 source: {lesson['id']}")
            if rubric.get("class_id") != lesson["id"] or rubric.get("passing_score") != 12:
                failures.append(f"rubric contract drift: {lesson['id']}")
            if sum(item.get("max", 0) for item in rubric.get("criteria", [])) != rubric.get("maximum_score"):
                failures.append(f"rubric score drift: {lesson['id']}")

    if statuses != Counter({"PLANNED": 480}):
        failures.append(f"unexpected maturity counts: {dict(statuses)}")
    if draft_count != 180 or len(hashes) != 180:
        failures.append(f"expected 180 unique phase 3 drafts, found {draft_count}/{len(hashes)}")
    if failures:
        print("\n".join(failures[:80]), file=sys.stderr)
        return 1
    print("PHASE3_REBUILD_OK: 180 unique drafts audited, 0 GUIDED claims, 360 contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
