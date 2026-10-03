"""Replace opaque fictional case names with descriptive technical labels.

The old aliases are recorded in docs/CASE-LABEL-CORRECTION.md. The migration is
scoped to one content part at a time so each part can be validated and committed
independently.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LABELS = {
    "Pulso": ("analizador local de eventos", "el analizador local de eventos"),
    "Faro": ("kit de diagnóstico multiplataforma", "el kit de diagnóstico multiplataforma"),
    "Nexo": ("petición observable de extremo a extremo", "la petición observable de extremo a extremo"),
    "Atlas": ("modelo de decisión diagnóstica", "el modelo de decisión diagnóstica"),
    "Brújula": ("CLI diagnóstica", "la CLI diagnóstica"),
    "Prisma": ("motor de reglas comparado", "el motor de reglas comparado"),
    "Orbe": ("biblioteca de estructuras y algoritmos", "la biblioteca de estructuras y algoritmos"),
    "Lupa": ("entorno reproducible de diagnóstico", "el entorno reproducible de diagnóstico"),
    "Constelación": ("producto reutilizable con SDK y CLI", "el producto reutilizable con SDK y CLI"),
}
GENITIVE = {
    "Pulso": "del analizador local de eventos",
    "Faro": "del kit de diagnóstico multiplataforma",
    "Nexo": "de la petición observable de extremo a extremo",
    "Atlas": "del modelo de decisión diagnóstica",
    "Brújula": "de la CLI diagnóstica",
    "Prisma": "del motor de reglas comparado",
    "Orbe": "de la biblioteca de estructuras y algoritmos",
    "Lupa": "del entorno reproducible de diagnóstico",
    "Constelación": "del producto reutilizable con SDK y CLI",
}
CODE_ALIASES = {
    "pulso": "event_analyzer",
    "faro": "diagnostic_kit",
    "nexo": "observable_request",
    "atlas": "decision_model",
    "brújula": "diagnostic_cli",
    "compass": "diagnostic_cli",
    "prisma": "rule_engine",
    "orbe": "algorithm_library",
    "lupa": "diagnostic_environment",
    "constelación": "engineering_sdk",
    "constellation": "engineering_sdk",
}


def replace_labels(text: str) -> str:
    text = text.replace("el **SDK y la CLI versionados de la Parte 09**", "el **producto reutilizable con SDK y CLI de la Parte 09**")
    text = text.replace("**SDK y CLI versionados**", "**producto reutilizable con SDK y CLI**")
    text = text.replace("El SDK y la CLI versionados", "El producto reutilizable con SDK y CLI")
    text = text.replace("el SDK y la CLI versionados", "el producto reutilizable con SDK y CLI")
    text = text.replace("del SDK y la CLI versionados", "del producto reutilizable con SDK y CLI")
    text = text.replace("Faro-01", "incidente-de-diagnóstico-01")
    for old, replacement in GENITIVE.items():
        text = text.replace(f"caso {old}", f"caso {replacement}")
        text = text.replace(f"de **{old}**", f"{replacement.replace('de ', 'de **', 1).replace('del ', 'del **', 1)}**")
        text = text.replace(f"de `{old}`", f"{replacement}")
        text = text.replace(f"de {old}", replacement)
    for old, (display, phrase) in LABELS.items():
        text = text.replace(f"**{old}**", f"**{display}**")
        text = text.replace(f"`{old}`", phrase)
        text = text.replace(f"sobre {old}", f"sobre {phrase}")
        text = text.replace(f"para {old}", f"para {phrase}")
        text = text.replace(f"con {old}", f"con {phrase}")
        text = text.replace(f"en {old}", f"en {phrase}")
        text = text.replace(f"desde {old}", f"desde {phrase}")
        text = text.replace(old, phrase)
        # Normalize files already migrated by an earlier version of this script.
        text = text.replace(f"**{phrase}**", f"**{display}**")
        capital = phrase[0].upper() + phrase[1:]
        text = text.replace(capital, phrase)
        text = re.sub(
            rf"(^|[.!?]\s+|\n\n)({re.escape(phrase)})",
            lambda match: match.group(1) + capital,
            text,
        )
    continuity = {
        "Esta clase continúa **petición observable de extremo a extremo**, la petición observable de la Parte 3.":
            "Esta clase continúa la **petición observable de extremo a extremo de la Parte 3**.",
        "Esta clase continúa **motor de reglas comparado**, el caso conductor de la Parte 06.":
            "Esta clase continúa el **motor de reglas comparado de la Parte 06**.",
        "Esta clase continúa **biblioteca de estructuras y algoritmos**, el caso conductor de la Parte 07.":
            "Esta clase continúa la **biblioteca de estructuras y algoritmos de la Parte 07**.",
        "Esta clase continúa **entorno reproducible de diagnóstico**, el caso conductor de la Parte 08.":
            "Esta clase continúa el **entorno reproducible de diagnóstico de la Parte 08**.",
        "Esta clase continúa **producto reutilizable con SDK y CLI**, el caso conductor de la Parte 09.":
            "Esta clase continúa el **producto reutilizable con SDK y CLI de la Parte 09**.",
        "Esta clase continúa **modelo de decisión diagnóstica**, el planificador de diagnóstico que recibe la evidencia de la petición observable de extremo a extremo y la convierte en una siguiente decisión explicable.":
            "Esta clase continúa el **modelo de decisión diagnóstica**, que convierte la evidencia de la petición observable de extremo a extremo en una siguiente decisión explicable.",
    }
    for before, after in continuity.items():
        text = text.replace(before, after)
    text = text.replace("caso el modelo de decisión diagnóstica", "caso del modelo de decisión diagnóstica")
    text = text.replace(
        "Esta clase construye **CLI diagnóstica**, la implementación incremental de la especificación el modelo de decisión diagnóstica.",
        "Esta clase construye la **CLI diagnóstica**, implementación incremental de la especificación del modelo de decisión diagnóstica.",
    )
    text = text.replace("especificación el modelo de decisión diagnóstica", "especificación del modelo de decisión diagnóstica")
    text = text.replace("CLI la CLI diagnóstica", "CLI diagnóstica")
    text = text.replace("como **CLI diagnóstica**", "como una **CLI diagnóstica**")
    for old, new in CODE_ALIASES.items():
        text = text.replace(old.upper(), new.upper())
        text = text.replace(old, new)
        text = re.sub(rf"\b{re.escape(old.upper())}\b", new.upper(), text)
        text = re.sub(rf"\b{re.escape(old)}\b", new, text, flags=re.IGNORECASE)
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--part", type=int, required=True, choices=range(1, 10))
    args = parser.parse_args()
    directory = ROOT / "content" / f"part-{args.part:02d}"
    for path in sorted(directory.glob("*.md")):
        before = path.read_text(encoding="utf-8")
        after = replace_labels(before)
        if after != before:
            path.write_text(after, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
