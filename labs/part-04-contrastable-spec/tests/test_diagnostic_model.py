from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from diagnostic_model import (  # noqa: E402
    ModelState,
    SpecificationError,
    apply_observation,
    implication_counterexamples,
    load_json,
    operation_counts,
    reachable,
    run_model,
    select_test,
    transition,
    validate_spec,
)


SPEC_PATH = LAB / "cases" / "incident-spec.json"
OBS_PATH = LAB / "cases" / "observations.json"


class DiagnosticModelTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = load_json(SPEC_PATH)

    def test_reference_spec_is_complete(self) -> None:
        self.assertEqual([], validate_spec(self.spec))

    def test_missing_outcome_is_rejected(self) -> None:
        self.spec["tests"][0]["outcomes"].pop("dns")
        self.assertIn("incomplete_outcomes:resolve", validate_spec(self.spec))

    def test_unresolved_requirement_conflict_is_visible(self) -> None:
        self.spec["requirements"].append({"id": "live_only", "text": "usar producción"})
        self.spec["conflicts"] = [["authorized_only", "live_only"]]
        self.assertIn("unresolved_conflict:authorized_only:live_only", validate_spec(self.spec))

    def test_implication_has_one_false_row(self) -> None:
        self.assertEqual([{"premise": True, "conclusion": False}], implication_counterexamples())

    def test_graph_walk_terminates_with_cycle(self) -> None:
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        self.assertEqual(["a", "b", "c"], reachable(graph, "a"))

    def test_state_machine_rejects_impossible_transition(self) -> None:
        self.assertEqual("tested", transition("proposed", "test"))
        with self.assertRaisesRegex(SpecificationError, "illegal_transition"):
            transition("confirmed", "reopen")

    def test_selector_excludes_unauthorized_test(self) -> None:
        selected = select_test(self.spec, self.spec["hypotheses"], set(), 5)
        self.assertTrue(selected["authorized"])
        self.assertNotEqual("production-capture", selected["id"])

    def test_observation_preserves_subset_invariant(self) -> None:
        initial = ModelState(list(self.spec["hypotheses"]))
        next_state = apply_observation(self.spec, initial, "resolve", "ok")
        self.assertEqual(["tls", "http"], next_state.candidates)
        self.assertTrue(set(next_state.candidates).issubset(initial.candidates))

    def test_contradictory_observation_fails_loudly(self) -> None:
        with self.assertRaisesRegex(SpecificationError, "contradictory_observation"):
            apply_observation(self.spec, ModelState(list(self.spec["hypotheses"])), "resolve", "impossible")

    def test_budget_is_a_precondition(self) -> None:
        state = ModelState(["tls", "http"], spent=4)
        with self.assertRaisesRegex(SpecificationError, "budget_exceeded"):
            apply_observation(self.spec, state, "handshake", "fail")

    def test_reference_case_resolves_and_keeps_trace(self) -> None:
        result = run_model(self.spec, load_json(OBS_PATH))
        self.assertEqual("resolved", result["status"])
        self.assertEqual(["tls"], result["candidates"])
        self.assertEqual(3, result["spent"])
        self.assertEqual(2, len(result["timeline"]))

    def test_operation_counts_separate_theory_from_timing(self) -> None:
        counts = operation_counts(4)
        self.assertEqual({"n": 4, "linear": 4, "pairwise": 6}, counts[-1])

    def test_cli_output_is_machine_readable(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(LAB / "diagnostic_model.py"), str(SPEC_PATH), str(OBS_PATH)],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual("resolved", json.loads(completed.stdout)["status"])


if __name__ == "__main__":
    unittest.main()
