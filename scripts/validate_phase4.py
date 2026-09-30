from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIRST_CLASS = 181
LAST_CLASS = 360
REQUIRED_SECTIONS = [
    "## Prerrequisitos", "## Problema auténtico", "## Objetivos observables",
    "## Temas y por qué importan", "## Mapa conceptual",
    "## Conceptos y decisiones", "## Definiciones de trabajo",
    "## Ejemplo mínimo", "## Ejemplo profesional", "## Práctica guiada",
    "## Ejercicios", "## Reto verificable",
    "## Fallo controlado y diagnóstico", "## Entorno y archivos clave",
    "## Seguridad, ética y accesibilidad", "## Transferencia",
    "## Evaluación y evidencia", "## Fuentes", "## Preguntas frecuentes",
    "## Límites y siguiente paso",
]


def main() -> int:
    program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    source_catalog = json.loads((ROOT / "sources/phase4.json").read_text(encoding="utf-8"))
    source_ids = {source["id"] for source in source_catalog["sources"]}
    failures: list[str] = []
    hashes: set[str] = set()
    count = 0

    for part in program["parts"]:
        for lesson in part["lessons"]:
            if not FIRST_CLASS <= lesson["number"] <= LAST_CLASS:
                continue
            count += 1
            directory = ROOT / lesson["path"]
            readme = directory / "README.md"
            activity_path = directory / "activity.yaml"
            rubric_path = directory / "rubric.json"
            for path in (readme, activity_path, rubric_path):
                if not path.is_file():
                    failures.append(f"missing phase 4 file: {path.relative_to(ROOT)}")
            if not all(path.is_file() for path in (readme, activity_path, rubric_path)):
                continue
            text = readme.read_text(encoding="utf-8")
            missing = [section for section in REQUIRED_SECTIONS if section not in text]
            if missing:
                failures.append(f"missing sections {lesson['id']}: {missing}")
            if "Estado: **PLANNED · BORRADOR EN REVISIÓN**" not in text:
                failures.append(f"false maturity or missing warning: {lesson['id']}")
            if "## Ficha" in text or "| Campo | Valor |" in text:
                failures.append(f"forbidden class record table: {lesson['id']}")
            if "Índice completo" not in text or f"↑ Parte {part['id']}" not in text:
                failures.append(f"missing class navigation: {lesson['id']}")
            if "{'id':" in text or "Pendiente de desarrollar" in text:
                failures.append(f"generator artifact in class: {lesson['id']}")
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if digest in hashes:
                failures.append(f"duplicate class document: {lesson['id']}")
            hashes.add(digest)

            activity = json.loads(activity_path.read_text(encoding="utf-8"))
            rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
            if activity.get("class_id") != lesson["id"] or activity.get("status") != "PLANNED":
                failures.append(f"activity contract drift: {lesson['id']}")
            if not set(activity.get("source_ids", [])).issubset(source_ids):
                failures.append(f"unresolved phase 4 source: {lesson['id']}")
            if rubric.get("class_id") != lesson["id"] or rubric.get("passing_score") != 12:
                failures.append(f"rubric contract drift: {lesson['id']}")

    target = program.get("phase_4_target", {})
    expected_target = {
        "first_class": "SE-181", "last_class": "SE-360", "classes": 180,
        "approved": 0,
    }
    if target != expected_target:
        failures.append(f"phase 4 target drift: {target}")
    if count != 180 or len(hashes) != 180:
        failures.append(f"expected 180 unique phase 4 drafts, found {count}/{len(hashes)}")
    if len(source_catalog.get("parts", {})) != 15:
        failures.append("phase 4 source catalog must cover 15 parts")
    if failures:
        print("\n".join(failures[:100]), file=sys.stderr)
        return 1
    print("PHASE4_STRUCTURE_OK: 180 drafts, 0 approved, 360 contracts, 15 sourced parts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
