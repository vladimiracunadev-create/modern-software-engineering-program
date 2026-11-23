"""Estado real del programa: qué partes existen y cuáles siguen planificadas.

Una parte está **desarrollada** si y solo si existen `content/part-NN/README.md` y los
doce archivos `content/part-NN/SE-NNN.md` de su rango. Nada más decide el estado: ni una
constante editada a mano ni un contador. Por eso añadir una parte nueva (las Partes 34 y
42 están reservadas) solo exige añadir sus archivos de contenido; los contadores, los
índices, el portal y los validadores se recalculan a partir de este módulo.

El alcance planificado (51 partes, 612 clases, `SE-001`–`SE-612`) está decidido en ADR-007,
que ordenó el programa en secuencia pedagógica y reservó las Partes 34 y 42. La numeración
histórica (49 partes, 588 clases; ADR-004 y ADR-006) se conserva en `docs/ID-MIGRATION.json`.
Los títulos de las posiciones reservadas viven en `build_program_blueprint.py` para que cada
parte nueva solo aporte contenido, no infraestructura.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

PLANNED_PART_COUNT = 51
CLASSES_PER_PART = 12
PLANNED_CLASS_COUNT = PLANNED_PART_COUNT * CLASSES_PER_PART  # 612
LAST_PART_NUMBER = PLANNED_PART_COUNT - 1  # 50
HOURS_PER_PART = 10 * 4 + 6 + 8  # diez clases, un taller y un proyecto

# Partes con contratos de actividad y rúbrica. La numeración pedagógica (ADR-007) dispersó las
# antiguas Partes 15–29 de la fase 4; por eso el alcance se declara por parte y no por rango de SE-nnn.
PHASE3_PARTS = tuple(range(0, 15))  # SE-001–SE-180
PHASE4_PARTS = (*range(15, 23), 24, 25, 27, 29, 31, 32, 33)  # 15 partes, 180 clases
CONTRACT_PARTS = PHASE3_PARTS + PHASE4_PARTS


def part_phase(part_number: int) -> int | None:
    """3 o 4 si la parte lleva contratos de actividad y rúbrica; None si no."""
    if part_number in PHASE3_PARTS:
        return 3
    if part_number in PHASE4_PARTS:
        return 4
    return None


def class_part(class_number: int) -> int:
    return (class_number - 1) // CLASSES_PER_PART


def class_phase(class_number: int) -> int | None:
    return part_phase(class_part(class_number))


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


def _join(pieces: list[str]) -> str:
    """`a`, `a y b` o `a, b y c`."""
    return pieces[0] if len(pieces) == 1 else ", ".join(pieces[:-1]) + " y " + pieces[-1]


def part_ranges(numbers: list[int]) -> str:
    """`00–22`, `00–22, 24` o `34, 42`."""
    pieces = [f"{a:02d}" if a == b else f"{a:02d}–{b:02d}" for a, b in _runs(numbers)]
    return _join(pieces)


def class_ranges(numbers: list[int], markup: bool = True) -> str:
    """Rangos de clases para las partes dadas: `SE-001`–`SE-276`."""
    pieces = []
    for first_part, last_part in _runs(numbers):
        first = f"SE-{part_first_class(first_part):03d}"
        last = f"SE-{part_last_class(last_part):03d}"
        pieces.append(f"`{first}`–`{last}`" if markup else f"{first}–{last}")
    return _join(pieces)


def parts_label(numbers: list[int]) -> str:
    """`Partes 00–22, 24`, `Parte 34` o `Partes 34, 42`."""
    word = "Parte" if len(numbers) == 1 else "Partes"
    return f"{word} {part_ranges(numbers)}"


def the_parts(numbers: list[int]) -> str:
    """`Las Partes 00–22, 24` o `La Parte 34`."""
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
        text += " Todo el alcance del programa está publicado."
    return text


def roles_extension_heading() -> str:
    """Encabezado de la sección de ampliación en las guías de rol."""
    planned = planned_parts()
    if planned:
        return f"## 🔭 Ampliación planificada: {parts_label(planned)} (sin clases publicadas)"
    return "## ✅ Ampliación completada: todas las partes del alcance"
