from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import build_phase3 as shared
import program_state as ps


ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "curriculum.yaml"


def source_catalog(program: dict) -> dict:
    part_ids = {
        part["id"]
        for part in program["parts"]
        if ps.part_phase(int(part["id"])) == 4
    }
    used = sorted(
        {
            source_id
            for part_id in part_ids
            for source_id in shared.PROFILES[part_id]["sources"]
        }
    )
    return {
        "schema_version": 1,
        "verified_on": shared.VERIFIED_ON,
        "scope": "Fase 4: quince partes con contratos de actividad y rúbrica (180 clases)",
        "policy": (
            "Fuentes primarias u oficiales; cada borrador explica su uso, "
            "pero requiere revisión técnica individual antes de ser aprobado."
        ),
        "sources": [
            {
                "id": source_id,
                "title": shared.SOURCES[source_id][0],
                "authority": shared.SOURCES[source_id][1],
                "url": shared.SOURCES[source_id][2],
                "status": "verified",
            }
            for source_id in used
        ],
        "parts": {
            part_id: shared.PROFILES[part_id]["sources"]
            for part_id in sorted(part_ids)
        },
    }


def expected_files(program: dict) -> dict[Path, str]:
    result = {ROOT / "sources/phase4.json": shared.dump_json(source_catalog(program))}
    entries = shared.context(program)
    for part in program["parts"]:
        if ps.part_phase(int(part["id"])) != 4:
            continue
        if part["id"] not in shared.PROFILES or part["id"] not in shared.TEACHING:
            raise ValueError(f"Missing phase 4 teaching profile for part {part['id']}")
        for lesson in part["lessons"]:
            _, _, previous, following = entries[lesson["id"]]
            directory = ROOT / lesson["path"]
            if lesson["id"] in shared.PUBLISHED_EDITORIAL_IDS:
                markdown = shared.published_markdown(part, lesson, previous, following)
            else:
                markdown = shared.lesson_readme(part, lesson, previous, following)
            result[directory / "README.md"] = markdown
            result[directory / "activity.yaml"] = shared.dump_json(shared.activity(part, lesson))
            result[directory / "rubric.json"] = shared.dump_json(shared.rubric(part, lesson))
            result[ROOT / "site/classes" / f"{lesson['id']}.html"] = shared.site_page(
                part, lesson, markdown, previous, following
            )
    # Partes sin contratos de actividad (las que llegaron después de la fase 4) con texto
    # editorial íntegro en content/: se publican (README y página del portal) sin actividad
    # ni rúbrica, porque los contratos de actividad cubren solo las fases 3 y 4.
    for part in program["parts"]:
        if ps.part_phase(int(part["id"])) is not None:
            continue
        for lesson in part["lessons"]:
            if not (ROOT / "content" / f"part-{part['id']}" / f"{lesson['id']}.md").is_file():
                continue
            _, _, previous, following = entries[lesson["id"]]
            markdown = shared.published_markdown(part, lesson, previous, following)
            result[ROOT / lesson["path"] / "README.md"] = markdown
            result[ROOT / "site/classes" / f"{lesson['id']}.html"] = shared.site_page(
                part, lesson, markdown, previous, following
            )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    program = json.loads(PROGRAM_PATH.read_text(encoding="utf-8"))
    files = expected_files(program)
    stale: list[str] = []
    for path, content in files.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        print("PHASE4_STALE: " + ", ".join(stale[:30]), file=sys.stderr)
        return 1
    action = "PHASE4_CHECK_OK" if args.check else "PHASE4_BUILD_OK"
    print(f"{action}: 180 class documents, 360 activity/rubric contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
