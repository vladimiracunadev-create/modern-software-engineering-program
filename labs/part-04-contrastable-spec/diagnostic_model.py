"""Modelo ejecutable para especificar y contrastar una decision diagnostica."""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class SpecificationError(ValueError):
    pass


def validate_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    hypotheses = spec.get("hypotheses", [])
    tests = spec.get("tests", [])
    if not spec.get("decision"):
        errors.append("missing_decision")
    if len(hypotheses) < 2 or len(hypotheses) != len(set(hypotheses)):
        errors.append("hypotheses_must_be_unique_and_plural")
    if not isinstance(spec.get("budget"), int) or spec.get("budget", 0) < 0:
        errors.append("budget_must_be_nonnegative_integer")
    test_ids = [test.get("id") for test in tests]
    if len(test_ids) != len(set(test_ids)) or any(not item for item in test_ids):
        errors.append("test_ids_must_be_unique")
    for test in tests:
        if set(test.get("outcomes", {})) != set(hypotheses):
            errors.append(f"incomplete_outcomes:{test.get('id', 'unknown')}")
        if test.get("cost", 0) <= 0:
            errors.append(f"invalid_cost:{test.get('id', 'unknown')}")
        if not isinstance(test.get("authorized"), bool):
            errors.append(f"authorization_not_explicit:{test.get('id', 'unknown')}")
    requirement_ids = {item["id"] for item in spec.get("requirements", [])}
    for left, right in spec.get("conflicts", []):
        if left in requirement_ids and right in requirement_ids:
            errors.append(f"unresolved_conflict:{left}:{right}")
    return errors


def implication_counterexamples() -> list[dict[str, bool]]:
    """Devuelve filas donde P→Q es falsa; evita afirmar el consecuente."""
    rows = []
    for premise, conclusion in itertools.product((False, True), repeat=2):
        implication = (not premise) or conclusion
        if not implication:
            rows.append({"premise": premise, "conclusion": conclusion})
    return rows


def reachable(graph: dict[str, list[str]], start: str) -> list[str]:
    if start not in graph:
        return []
    pending = [start]
    visited: set[str] = set()
    order: list[str] = []
    while pending:
        node = pending.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        pending.extend(reversed(graph.get(node, [])))
    return order


TRANSITIONS = {
    "proposed": {"test": "tested"},
    "tested": {"confirm": "confirmed", "discard": "discarded", "defer": "inconclusive"},
    "inconclusive": {"reopen": "proposed"},
    "confirmed": {},
    "discarded": {},
}


def transition(state: str, event: str) -> str:
    try:
        return TRANSITIONS[state][event]
    except KeyError as exc:
        raise SpecificationError(f"illegal_transition:{state}:{event}") from exc


def _partitions(test: dict[str, Any], candidates: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for hypothesis in candidates:
        groups.setdefault(str(test["outcomes"][hypothesis]), []).append(hypothesis)
    return groups


def select_test(spec: dict[str, Any], candidates: list[str], used: set[str], remaining_budget: int) -> dict[str, Any] | None:
    options = []
    for test in spec["tests"]:
        if test["id"] in used or not test["authorized"] or test["cost"] > remaining_budget:
            continue
        groups = _partitions(test, candidates)
        worst_remaining = max(map(len, groups.values()))
        eliminated = len(candidates) - worst_remaining
        score = eliminated / test["cost"]
        options.append((score, eliminated, -test["cost"], test["id"], test))
    if not options:
        return None
    return max(options, key=lambda item: item[:4])[4]


@dataclass
class ModelState:
    candidates: list[str]
    spent: int = 0
    used: set[str] | None = None

    def __post_init__(self) -> None:
        if self.used is None:
            self.used = set()


def apply_observation(spec: dict[str, Any], state: ModelState, test_id: str, result: str) -> ModelState:
    test = next((item for item in spec["tests"] if item["id"] == test_id), None)
    if test is None:
        raise SpecificationError(f"unknown_test:{test_id}")
    if not test["authorized"]:
        raise SpecificationError(f"unauthorized_test:{test_id}")
    if state.spent + test["cost"] > spec["budget"]:
        raise SpecificationError(f"budget_exceeded:{test_id}")
    next_candidates = [item for item in state.candidates if str(test["outcomes"][item]) == str(result)]
    if not next_candidates:
        raise SpecificationError(f"contradictory_observation:{test_id}:{result}")
    if not set(next_candidates).issubset(state.candidates):
        raise AssertionError("candidate invariant violated")
    return ModelState(next_candidates, state.spent + test["cost"], set(state.used) | {test_id})


def run_model(spec: dict[str, Any], observations: list[dict[str, str]]) -> dict[str, Any]:
    errors = validate_spec(spec)
    if errors:
        raise SpecificationError(",".join(errors))
    state = ModelState(list(spec["hypotheses"]))
    timeline = []
    previous_size = len(state.candidates)
    for observation in observations:
        state = apply_observation(spec, state, observation["test_id"], observation["result"])
        if len(state.candidates) > previous_size:
            raise AssertionError("variant did not decrease or remain stable")
        timeline.append(
            {
                "test_id": observation["test_id"],
                "result": observation["result"],
                "remaining": state.candidates,
                "spent": state.spent,
            }
        )
        previous_size = len(state.candidates)
    recommendation = select_test(spec, state.candidates, state.used or set(), spec["budget"] - state.spent)
    return {
        "schema_version": 1,
        "decision": spec["decision"],
        "status": "resolved" if len(state.candidates) == 1 else "inconclusive",
        "candidates": state.candidates,
        "spent": state.spent,
        "remaining_budget": spec["budget"] - state.spent,
        "next_test": None if recommendation is None else recommendation["id"],
        "timeline": timeline,
        "limits": [
            "la salida solo es correcta respecto de las hipotesis y outcomes declarados",
            "la puntuacion codiciosa no garantiza una secuencia global optima",
            "una medicion de tiempo no sustituye el analisis de crecimiento",
        ],
    }


def operation_counts(max_size: int) -> list[dict[str, int]]:
    """Cuenta operaciones de dos estrategias; no mide tiempo de pared."""
    return [
        {"n": n, "linear": n, "pairwise": n * (n - 1) // 2}
        for n in range(1, max_size + 1)
    ]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Ejecuta una especificacion diagnostica contrastable")
    parser.add_argument("spec", type=Path)
    parser.add_argument("observations", type=Path)
    args = parser.parse_args(argv)
    result = run_model(load_json(args.spec), load_json(args.observations))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
