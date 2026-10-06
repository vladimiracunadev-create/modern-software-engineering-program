from __future__ import annotations

import argparse
import ast
import csv
import dis
import hashlib
import json
import math
import platform
import statistics
import sys
import time
import tracemalloc
import unicodedata
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Event:
    sequence: int
    message: str
    duration_ms: float
    amount_cents: int


def parse_event(payload: object, line_number: int) -> Event:
    if not isinstance(payload, dict):
        raise ValueError(f"line {line_number}: each event must be a JSON object")
    expected = {"sequence", "message", "duration_ms", "amount_cents"}
    unknown = set(payload) - expected
    missing = expected - set(payload)
    if missing or unknown:
        raise ValueError(
            f"line {line_number}: missing={sorted(missing)} unknown={sorted(unknown)}"
        )
    sequence = payload["sequence"]
    message = payload["message"]
    duration_ms = payload["duration_ms"]
    amount_cents = payload["amount_cents"]
    if isinstance(sequence, bool) or not isinstance(sequence, int) or sequence < 0:
        raise ValueError(f"line {line_number}: sequence must be a non-negative integer")
    if not isinstance(message, str) or not message:
        raise ValueError(f"line {line_number}: message must be non-empty text")
    if isinstance(duration_ms, bool) or not isinstance(duration_ms, (int, float)):
        raise ValueError(f"line {line_number}: duration_ms must be numeric")
    if not math.isfinite(float(duration_ms)) or float(duration_ms) < 0:
        raise ValueError(f"line {line_number}: duration_ms must be finite and non-negative")
    if isinstance(amount_cents, bool) or not isinstance(amount_cents, int):
        raise ValueError(f"line {line_number}: amount_cents must be an integer")
    return Event(sequence, message, float(duration_ms), amount_cents)


def iter_events(path: Path) -> Iterator[Event]:
    with path.open("r", encoding="utf-8", newline="") as source:
        seen: set[int] = set()
        for line_number, raw_line in enumerate(source, start=1):
            if not raw_line.strip():
                continue
            try:
                payload = json.loads(raw_line)
            except json.JSONDecodeError as error:
                raise ValueError(f"line {line_number}: invalid JSON: {error.msg}") from error
            event = parse_event(payload, line_number)
            if event.sequence in seen:
                raise ValueError(f"line {line_number}: duplicate sequence {event.sequence}")
            seen.add(event.sequence)
            yield event


def summarize(events: Iterable[Event]) -> dict[str, Any]:
    count = 0
    first_sequence: int | None = None
    last_sequence: int | None = None
    duration_total = 0.0
    amount_total = 0
    message_digest = hashlib.sha256()
    for event in events:
        count += 1
        first_sequence = event.sequence if first_sequence is None else first_sequence
        last_sequence = event.sequence
        duration_total = math.fsum((duration_total, event.duration_ms))
        amount_total += event.amount_cents
        normalized = unicodedata.normalize("NFC", event.message)
        message_digest.update(normalized.encode("utf-8"))
        message_digest.update(b"\0")
    if count == 0:
        raise ValueError("input contains no events")
    return {
        "count": count,
        "first_sequence": first_sequence,
        "last_sequence": last_sequence,
        "duration_mean_ms": duration_total / count,
        "amount_total_cents": amount_total,
        "messages_sha256": message_digest.hexdigest(),
    }


def canonical_hash(value: object) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def text_evidence(text: str) -> dict[str, Any]:
    nfc = unicodedata.normalize("NFC", text)
    nfd = unicodedata.normalize("NFD", text)
    return {
        "text": text,
        "code_points": [f"U+{ord(character):04X}" for character in text],
        "utf8_hex": text.encode("utf-8").hex(),
        "nfc_code_points": len(nfc),
        "nfd_code_points": len(nfd),
        "round_trip": text.encode("utf-8").decode("utf-8") == text,
    }


def binary_evidence(value: int) -> dict[str, Any]:
    if not 0 <= value <= 65_535:
        raise ValueError("binary evidence expects an unsigned 16-bit value")
    big = value.to_bytes(2, byteorder="big", signed=False)
    little = value.to_bytes(2, byteorder="little", signed=False)
    return {
        "value": value,
        "binary_16": f"{value:016b}",
        "big_endian_hex": big.hex(),
        "little_endian_hex": little.hex(),
        "big_endian_round_trip": int.from_bytes(big, "big", signed=False),
        "little_endian_round_trip": int.from_bytes(little, "little", signed=False),
    }


def translation_evidence() -> dict[str, Any]:
    source = "def add(a, b):\n    return a + b\n"
    tree = ast.parse(source)
    code = compile(source, "<part-01-lab>", "exec")
    namespace: dict[str, Any] = {}
    exec(code, namespace)
    instructions = [item.opname for item in dis.get_instructions(namespace["add"])]
    return {
        "ast_root": type(tree).__name__,
        "function_nodes": sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree)),
        "cpython_bytecode": instructions,
        "boundary": "CPython bytecode; not native ISA instructions or CPU cycles",
    }


def environment_evidence() -> dict[str, str]:
    return {
        "implementation": platform.python_implementation(),
        "python_version": platform.python_version(),
        "operating_system": platform.system(),
        "platform_release": platform.release(),
        "machine_label": platform.machine(),
        "byte_order": sys.byteorder,
    }


def inspect_input(path: Path) -> dict[str, Any]:
    materialized = list(iter_events(path))
    summary_materialized = summarize(materialized)
    summary_streaming = summarize(iter_events(path))
    if summary_materialized != summary_streaming:
        raise AssertionError("materialized and streaming variants diverged")
    first = materialized[0]
    return {
        "environment": environment_evidence(),
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "summary": summary_materialized,
        "summary_sha256": canonical_hash(summary_materialized),
        "binary": binary_evidence(first.sequence),
        "text": text_evidence(first.message),
        "numeric": {
            "duration_mean_hex": summary_materialized["duration_mean_ms"].hex(),
            "amount_model": "integer cents",
            "amount_total_cents": summary_materialized["amount_total_cents"],
        },
        "translation": translation_evidence(),
        "claims": {
            "observed": [
                "the two program variants produced the same functional summary",
                "the runtime exposed platform, byte order, AST and CPython bytecode",
                "UTF-8 round trip and normalization lengths were computed",
            ],
            "inferred": [
                "streaming may reduce retained Python objects for larger inputs",
            ],
            "not_measured": [
                "native instructions and CPU cycles",
                "physical cache hits or page faults",
                "resident set size, energy and carbon emissions",
            ],
        },
    }


ITERATIONS_PER_SAMPLE = 100


def measure(path: Path, mode: str) -> tuple[int, int, str]:
    tracemalloc.start()
    wall_start = time.perf_counter_ns()
    cpu_start = time.process_time_ns()
    result_hashes: set[str] = set()
    for _ in range(ITERATIONS_PER_SAMPLE):
        if mode == "materialized":
            result = summarize(list(iter_events(path)))
        elif mode == "streaming":
            result = summarize(iter_events(path))
        else:
            raise ValueError(f"unsupported mode: {mode}")
        result_hashes.add(canonical_hash(result))
    cpu_ns = time.process_time_ns() - cpu_start
    wall_ns = time.perf_counter_ns() - wall_start
    _, peak_bytes = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    if len(result_hashes) != 1:
        raise AssertionError("repeated executions produced different summaries")
    return wall_ns, cpu_ns, f"{peak_bytes}:{result_hashes.pop()}"


def benchmark(path: Path, repeat: int) -> list[dict[str, Any]]:
    if repeat < 3:
        raise ValueError("repeat must be at least 3")
    rows: list[dict[str, Any]] = []
    for run in range(repeat):
        modes = ("materialized", "streaming") if run % 2 == 0 else ("streaming", "materialized")
        for order, mode in enumerate(modes):
            wall_ns, cpu_ns, combined = measure(path, mode)
            peak_text, summary_sha256 = combined.split(":", maxsplit=1)
            rows.append(
                {
                    "run": run + 1,
                    "order": order + 1,
                    "mode": mode,
                    "iterations": ITERATIONS_PER_SAMPLE,
                    "wall_ns": wall_ns,
                    "cpu_ns": cpu_ns,
                    "python_peak_bytes": int(peak_text),
                    "summary_sha256": summary_sha256,
                }
            )
    return rows


def benchmark_report(rows: Sequence[dict[str, Any]]) -> dict[str, Any]:
    hashes = {str(row["summary_sha256"]) for row in rows}
    if len(hashes) != 1:
        raise AssertionError("benchmark variants did not preserve the functional summary")
    by_mode: dict[str, dict[str, int]] = {}
    for mode in ("materialized", "streaming"):
        selected = [row for row in rows if row["mode"] == mode]
        by_mode[mode] = {
            "samples": len(selected),
            "median_wall_ns": int(statistics.median(int(row["wall_ns"]) for row in selected)),
            "median_cpu_ns": int(statistics.median(int(row["cpu_ns"]) for row in selected)),
            "median_python_peak_bytes": int(
                statistics.median(int(row["python_peak_bytes"]) for row in selected)
            ),
        }
    return {
        "unit_of_work": (
            f"process the complete validated JSONL fixture {ITERATIONS_PER_SAMPLE} times per sample"
        ),
        "modes": by_mode,
        "shared_summary_sha256": hashes.pop(),
        "energy_measured": False,
        "interpretation_limit": (
            "Local medians describe this runtime and fixture; they do not identify a "
            "hardware cache, scheduler cause, energy use or production performance."
        ),
    }


def write_csv(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as target:
        writer = csv.DictWriter(target, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def render_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def command_inspect(args: argparse.Namespace) -> int:
    print(render_json(inspect_input(args.input)), end="")
    return 0


def command_benchmark(args: argparse.Namespace) -> int:
    rows = benchmark(args.input, args.repeat)
    write_csv(args.output, rows)
    print(render_json(benchmark_report(rows)), end="")
    return 0


def command_report(args: argparse.Namespace) -> int:
    report = inspect_input(args.input)
    rows = benchmark(args.input, args.repeat)
    report["benchmark"] = benchmark_report(rows)
    write_text(args.output, render_json(report))
    print(f"REPORT_OK: {args.output}")
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subcommands = result.add_subparsers(dest="command", required=True)
    inspect_parser = subcommands.add_parser("inspect", help="emit deterministic evidence")
    inspect_parser.add_argument("--input", type=Path, required=True)
    inspect_parser.set_defaults(handler=command_inspect)
    benchmark_parser = subcommands.add_parser("benchmark", help="preserve raw timing samples")
    benchmark_parser.add_argument("--input", type=Path, required=True)
    benchmark_parser.add_argument("--repeat", type=int, default=7)
    benchmark_parser.add_argument("--output", type=Path, required=True)
    benchmark_parser.set_defaults(handler=command_benchmark)
    report_parser = subcommands.add_parser("report", help="write the integrated evidence report")
    report_parser.add_argument("--input", type=Path, required=True)
    report_parser.add_argument("--repeat", type=int, default=7)
    report_parser.add_argument("--output", type=Path, required=True)
    report_parser.set_defaults(handler=command_report)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    arguments = parser().parse_args(argv)
    try:
        return int(arguments.handler(arguments))
    except (OSError, ValueError, AssertionError) as error:
        print(f"LAB_ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
