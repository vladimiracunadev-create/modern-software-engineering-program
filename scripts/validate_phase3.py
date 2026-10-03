from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SECTIONS = [
    "## Prerrequisitos", "## Problema auténtico",
    "## Objetivos observables", "## Mapa conceptual",
    "## Temas y por qué importan", "## Conceptos y decisiones",
    "## Definiciones de trabajo", "## Ejemplo mínimo",
    "## Ejemplo profesional", "## Práctica guiada", "## Ejercicios",
    "## Reto verificable", "## Preguntas frecuentes",
    "## Fallo controlado y diagnóstico", "## Entorno y archivos clave",
    "## Seguridad, ética y accesibilidad", "## Transferencia",
    "## Evaluación y evidencia", "## Fuentes", "## Límites y siguiente paso",
]
APPROVAL_SECTIONS = [
    "## Definiciones de trabajo", "## Glosario", "## Reto verificable",
    "## Preguntas frecuentes",
]
GENERIC_SENTENCE = "La respuesta profesional separa hechos, inferencias y preferencias"


def main() -> int:
    program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
    source_catalog = json.loads((ROOT / "sources/phase3.json").read_text(encoding="utf-8"))
    source_ids = {source["id"] for source in source_catalog["sources"]}
    statuses = Counter()
    hashes = set()
    failures: list[str] = []
    draft_count = 0
    generic_count = 0
    approval_section_counts = Counter()

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
            expected_marker = (
                "Estado: **GUIDED**" if lesson["status"] == "GUIDED"
                else "Estado: **PLANNED · BORRADOR EN REVISIÓN**"
            )
            if expected_marker not in text or "Pendiente de desarrollar" in text:
                failures.append(f"invalid maturity content: {lesson['id']}")
            if lesson["status"] == "GUIDED":
                for marker in (
                    "## Antes de empezar",
                    "Campus Abierto",
                    "## Errores comunes y cómo corregirlos",
                ):
                    if marker not in text:
                        failures.append(f"missing guided learning connection {lesson['id']}: {marker}")
                concept_match = re.search(
                    r"## Conceptos y decisiones\s+(.*?)\s+## Definiciones de trabajo",
                    text,
                    re.DOTALL,
                )
                if not concept_match or concept_match.group(1).count("### ") < 5:
                    failures.append(
                        f"guided class lacks topic-specific deep explanation: {lesson['id']}"
                    )
                if not re.search(
                    r"^## (Caso conductor|Demostración guiada|Integración final)",
                    text,
                    re.MULTILINE,
                ):
                    failures.append(
                        f"guided class lacks an integrated worked case: {lesson['id']}"
                    )
            missing = [section for section in REQUIRED_SECTIONS if section not in text]
            if missing:
                failures.append(f"missing sections {lesson['id']}: {missing}")
            if "## Ficha" in text or "| Campo | Valor |" in text:
                failures.append(f"forbidden class record table: {lesson['id']}")
            if "Índice completo" not in text or f"↑ Parte {part['id']}" not in text:
                failures.append(f"missing class navigation: {lesson['id']}")
            if GENERIC_SENTENCE in text:
                generic_count += 1
            for section in APPROVAL_SECTIONS:
                if section in text:
                    approval_section_counts[section] += 1
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            if digest in hashes:
                failures.append(f"duplicate class document: {lesson['id']}")
            hashes.add(digest)

            activity = json.loads(activity_path.read_text(encoding="utf-8"))
            rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
            if activity.get("class_id") != lesson["id"] or activity.get("status") != lesson["status"]:
                failures.append(f"activity contract drift: {lesson['id']}")
            if not set(activity.get("source_ids", [])).issubset(source_ids):
                failures.append(f"unresolved phase 3 source: {lesson['id']}")
            if rubric.get("class_id") != lesson["id"] or rubric.get("passing_score") != 12:
                failures.append(f"rubric contract drift: {lesson['id']}")
            if sum(item.get("max", 0) for item in rubric.get("criteria", [])) != rubric.get("maximum_score"):
                failures.append(f"rubric score drift: {lesson['id']}")

    if statuses != Counter({"GUIDED": 12, "PLANNED": 468}):
        failures.append(f"unexpected maturity counts: {dict(statuses)}")
    if draft_count != 180 or len(hashes) != 180:
        failures.append(f"expected 180 unique phase 3 drafts, found {draft_count}/{len(hashes)}")

    audit = (ROOT / "docs/PHASE3-CONTENT-AUDIT.md").read_text(encoding="utf-8")
    audit_claims = {
        "borradores que repiten el mismo párrafo genérico": generic_count,
        "clases con sección `Definiciones de trabajo`": approval_section_counts["## Definiciones de trabajo"],
        "clases con sección `Glosario`": approval_section_counts["## Glosario"],
        "clases con sección `Preguntas frecuentes`": approval_section_counts["## Preguntas frecuentes"],
        "clases con sección `Reto verificable`": approval_section_counts["## Reto verificable"],
    }
    for label, count in audit_claims.items():
        if f"| {label} | {count} |" not in audit:
            failures.append(f"phase 3 audit drift: {label} should report {count}")
    if failures:
        print("\n".join(failures[:80]), file=sys.stderr)
        return 1
    print(
        "PHASE3_STRUCTURE_OK: 168 drafts, "
        f"{generic_count} still generic, 12 approved, 360 contracts"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
