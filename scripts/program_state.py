"""Estado real del programa: qué partes existen y cuáles siguen planificadas.

Una parte está **desarrollada** si y solo si existen `content/part-NN/README.md` y los
doce archivos `content/part-NN/SE-NNN.md` de su rango. Nada más decide el estado: ni una
constante editada a mano ni un contador. Por eso añadir una parte nueva (40–48) solo
exige añadir sus archivos de contenido; los contadores, los índices, el portal y los
validadores se recalculan a partir de este módulo.

El alcance planificado (49 partes, 588 clases) está decidido en ADR-004 (Partes 00–44,
`SE-001`–`SE-540`) y ADR-006 (Partes 45–48, `SE-541`–`SE-588`). Los títulos de las
posiciones nuevas viven en `build_program_blueprint.py` para que cada parte nueva solo
aporte contenido, no infraestructura.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

PLANNED_PART_COUNT = 49
CLASSES_PER_PART = 12
PLANNED_CLASS_COUNT = PLANNED_PART_COUNT * CLASSES_PER_PART  # 588
LAST_PART_NUMBER = PLANNED_PART_COUNT - 1  # 48
HOURS_PER_PART = 10 * 4 + 6 + 8  # diez clases, un taller y un proyecto


def part_first_class(part_number: int) -> int:
    return part_number * CLASSES_PER_PART + 1


def part_last_class(part_number: int) -> int:
    return part_first_class(part_number) + CLASSES_PER_PART - 1


def class_ids(part_number: int) -> list[str]:
    return [f"SE-{number:03d}" for number in range(part_first_class(part_number), part_last_class(part_number) + 1)]


def part_content_files(part_number: int) -> list[Path]:
    directory = CONTENT / f"part-{part_number:02d}"
    return [directory / "README.md"] + [directory / f"{class_id}.md" for class_id in class_ids(part_number)]


def is_developed(part_number: int) -> bool:
    return all(path.is_file() for path in part_content_files(part_number))


def is_partial(part_number: int) -> bool:
    """Alguna pieza de contenido existe, pero no todas: no cuenta como desarrollada."""
    files = part_content_files(part_number)
    return any(path.is_file() for path in files) and not all(path.is_file() for path in files)


def developed_parts() -> list[int]:
    return [number for number in range(PLANNED_PART_COUNT) if is_developed(number)]


def planned_parts() -> list[int]:
    return [number for number in range(PLANNED_PART_COUNT) if not is_developed(number)]


def partial_parts() -> list[int]:
    return [number for number in range(PLANNED_PART_COUNT) if is_partial(number)]


def developed_class_count() -> int:
    return len(developed_parts()) * CLASSES_PER_PART


def planned_class_count() -> int:
    """Clases planificadas que todavía no tienen contenido."""
    return len(planned_parts()) * CLASSES_PER_PART


def _runs(numbers: list[int]) -> list[tuple[int, int]]:
    runs: list[tuple[int, int]] = []
    for number in sorted(numbers):
        if runs and runs[-1][1] == number - 1:
            runs[-1] = (runs[-1][0], number)
        else:
            runs.append((number, number))
    return runs


def part_ranges(numbers: list[int]) -> str:
    """`00–39` o `00–39, 41` o `40, 43–44`."""
    pieces = [f"{a:02d}" if a == b else f"{a:02d}–{b:02d}" for a, b in _runs(numbers)]
    return ", ".join(pieces)


def class_ranges(numbers: list[int], markup: bool = True) -> str:
    """Rangos de clases para las partes dadas: `SE-001`–`SE-480`."""
    pieces = []
    for first_part, last_part in _runs(numbers):
        first = f"SE-{part_first_class(first_part):03d}"
        last = f"SE-{part_last_class(last_part):03d}"
        pieces.append(f"`{first}`–`{last}`" if markup else f"{first}–{last}")
    return ", ".join(pieces)


def parts_label(numbers: list[int]) -> str:
    """`Partes 00–39`, `Parte 40` o `Partes 40, 42–44`."""
    word = "Parte" if len(numbers) == 1 else "Partes"
    return f"{word} {part_ranges(numbers)}"


def the_parts(numbers: list[int]) -> str:
    """`Las Partes 00–39` o `La Parte 40`."""
    return ("La " if len(numbers) == 1 else "Las ") + parts_label(numbers)


def verb_planned(numbers: list[int]) -> str:
    return "está **planificada**" if len(numbers) == 1 else "están **planificadas**"


def developed_label() -> str:
    return parts_label(developed_parts())


def planned_label() -> str:
    planned = planned_parts()
    return parts_label(planned) if planned else "ninguna"


def developed_hours() -> int:
    return len(developed_parts()) * HOURS_PER_PART


def planned_hours() -> int:
    return PLANNED_PART_COUNT * HOURS_PER_PART


def format_thousands(value: int) -> str:
    return f"{value:,}".replace(",", ".")


def status_sentence() -> str:
    """Frase única reutilizable en índices, README de clases y avisos."""
    developed = developed_parts()
    planned = planned_parts()
    text = (
        f"{the_parts(developed)} ({class_ranges(developed)}) contienen clases desarrolladas, "
        "con texto íntegro, figuras y evidencia reproducible, pendientes de revisión editorial humana independiente."
    )
    if planned:
        text += (
            f" {the_parts(planned)} ({class_ranges(planned)}) {verb_planned(planned)}, sin clases publicadas."
        )
    else:
        text += " No quedan partes planificadas sin publicar."
    return text


def roles_extension_heading() -> str:
    """Encabezado de la sección de ampliación en las guías de rol."""
    planned = planned_parts()
    if planned:
        return f"## 🔭 Ampliación planificada: {parts_label(planned)} (sin clases publicadas)"
    return "## ✅ Ampliación completada: Partes 40–48"
