"""Validación estricta en la frontera JSON/JSONL."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable, TextIO

from .domain import DiagnosticSpec, Observation, Outcome, Probe, Result

MAX_INPUT_BYTES = 1_000_000


def _strict_int(value: object) -> bool:
    # bool hereda de int en Python; el contrato externo no acepta esa coerción.
    return type(value) is int


def parse_spec(payload: object) -> Result[DiagnosticSpec]:
    if not isinstance(payload, dict):
        return Result.fail("invalid_spec", "la especificación debe ser un objeto JSON")
    decision = payload.get("decision")
    budget = payload.get("budget")
    hypotheses = payload.get("hypotheses")
    tests = payload.get("tests")
    if not isinstance(decision, str) or not decision.strip():
        return Result.fail("invalid_decision", "decision debe ser texto no vacío")
    if not _strict_int(budget) or budget < 0:
        return Result.fail("invalid_budget", "budget debe ser un entero no negativo")
    if not isinstance(hypotheses, list) or len(hypotheses) < 2:
        return Result.fail("invalid_hypotheses", "se requieren al menos dos hipótesis")
    if any(not isinstance(item, str) or not item for item in hypotheses):
        return Result.fail("invalid_hypotheses", "cada hipótesis debe ser texto no vacío")
    if len(set(hypotheses)) != len(hypotheses):
        return Result.fail("duplicate_hypothesis", "las hipótesis deben ser únicas")
    if not isinstance(tests, list) or not tests:
        return Result.fail("invalid_tests", "se requiere al menos una prueba")

    probes: list[Probe] = []
    identifiers: set[str] = set()
    for index, raw in enumerate(tests):
        if not isinstance(raw, dict):
            return Result.fail("invalid_test", f"tests[{index}] debe ser un objeto")
        identifier = raw.get("id")
        cost = raw.get("cost")
        authorized = raw.get("authorized")
        outcomes = raw.get("outcomes")
        if not isinstance(identifier, str) or not identifier:
            return Result.fail("invalid_test_id", f"tests[{index}].id debe ser texto no vacío")
        if identifier in identifiers:
            return Result.fail("duplicate_test", identifier)
        if not _strict_int(cost) or cost <= 0:
            return Result.fail("invalid_cost", identifier)
        if type(authorized) is not bool:
            return Result.fail("invalid_authorization", identifier)
        if not isinstance(outcomes, dict) or set(outcomes) != set(hypotheses):
            return Result.fail("incomplete_outcomes", identifier)
        parsed_outcomes: list[tuple[str, Outcome]] = []
        try:
            for hypothesis in hypotheses:
                parsed_outcomes.append((hypothesis, Outcome(outcomes[hypothesis])))
        except (TypeError, ValueError):
            return Result.fail("invalid_outcome", identifier)
        identifiers.add(identifier)
        probes.append(Probe(identifier, cost, authorized, tuple(parsed_outcomes)))
    return Result.ok(DiagnosticSpec(decision.strip(), budget, tuple(hypotheses), tuple(probes)))


def parse_observation(payload: object, *, line: int) -> Result[Observation]:
    if not isinstance(payload, dict):
        return Result.fail("invalid_observation", f"línea {line}: se esperaba un objeto")
    test_id = payload.get("test_id")
    if not isinstance(test_id, str) or not test_id:
        return Result.fail("invalid_observation", f"línea {line}: test_id inválido")
    try:
        outcome = Outcome(payload.get("result"))
    except (TypeError, ValueError):
        return Result.fail("invalid_observation", f"línea {line}: result inválido")
    return Result.ok(Observation(test_id, outcome))


def load_json_document(path: Path) -> Result[object]:
    try:
        if path.stat().st_size > MAX_INPUT_BYTES:
            return Result.fail("input_too_large", f"{path} supera {MAX_INPUT_BYTES} bytes")
        text = path.read_text(encoding="utf-8")
        return Result.ok(json.loads(text, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value))))
    except FileNotFoundError:
        return Result.fail("not_found", str(path))
    except UnicodeDecodeError as error:
        return Result.fail("invalid_encoding", f"{path}:{error.start}")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        return Result.fail("invalid_json", f"{path}: {error}")


def iter_json_lines(stream: TextIO) -> Iterable[Result[Observation]]:
    consumed = 0
    for line_number, raw_line in enumerate(stream, start=1):
        consumed += len(raw_line.encode("utf-8"))
        if consumed > MAX_INPUT_BYTES:
            yield Result.fail("input_too_large", f"línea {line_number}")
            return
        if not raw_line.strip():
            continue
        try:
            payload = json.loads(raw_line, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
        except (json.JSONDecodeError, ValueError) as error:
            yield Result.fail("invalid_jsonl", f"línea {line_number}: {error}")
            return
        yield parse_observation(payload, line=line_number)
