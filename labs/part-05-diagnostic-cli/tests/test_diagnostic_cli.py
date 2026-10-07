from __future__ import annotations

import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
SRC = LAB / "src"
sys.path.insert(0, str(SRC))

from diagnostic_cli.cli import EXIT_DOMAIN_REFUSAL, EXIT_INVALID_INPUT, EXIT_IO, EXIT_OK, main
from diagnostic_cli.domain import DiagnosticSpec, Observation, Outcome, Probe, Result, State
from diagnostic_cli.engine import apply_observation, run_diagnosis
from diagnostic_cli.parsing import iter_json_lines, load_json_document, parse_spec


class DiagnosticCliTests(unittest.TestCase):
    def setUp(self) -> None:
        document = load_json_document(LAB / "cases" / "incident-spec.json")
        self.assertTrue(document.is_ok)
        parsed = parse_spec(document.value)
        self.assertTrue(parsed.is_ok)
        assert parsed.value is not None
        self.spec = parsed.value

    def test_parse_rejects_boolean_budget_without_silent_integer_coercion(self) -> None:
        payload = json.loads((LAB / "cases" / "incident-spec.json").read_text(encoding="utf-8"))
        payload["budget"] = True
        parsed = parse_spec(payload)
        self.assertEqual("invalid_budget", parsed.error.code)

    def test_parse_rejects_incomplete_outcome_map(self) -> None:
        payload = json.loads((LAB / "cases" / "incident-spec.json").read_text(encoding="utf-8"))
        del payload["tests"][0]["outcomes"]["http"]
        parsed = parse_spec(payload)
        self.assertEqual("incomplete_outcomes", parsed.error.code)

    def test_apply_observation_returns_new_state_without_mutating_input(self) -> None:
        before = State(self.spec.hypotheses)
        result = apply_observation(self.spec, before, Observation("resolve", Outcome.OK))
        self.assertEqual(("dns", "tls", "http"), before.candidates)
        self.assertEqual(frozenset(), before.used)
        self.assertEqual(("tls", "http"), result.value.candidates)

    def test_explicit_result_rejects_impossible_state(self) -> None:
        with self.assertRaises(ValueError):
            Result(value="success", error=Result.fail("x", "y").error)

    def test_domain_refuses_unauthorized_probe(self) -> None:
        result = apply_observation(
            self.spec,
            State(self.spec.hypotheses),
            Observation("production-capture", Outcome.UNKNOWN),
        )
        self.assertEqual("unauthorized_test", result.error.code)

    def test_domain_refuses_duplicate_observation(self) -> None:
        state = State(("tls", "http"), spent=1, used=frozenset({"resolve"}))
        result = apply_observation(self.spec, state, Observation("resolve", Outcome.OK))
        self.assertEqual("duplicate_observation", result.error.code)

    def test_stream_reports_malformed_line_with_location(self) -> None:
        parsed = list(iter_json_lines(io.StringIO('{"test_id":"resolve","result":"ok"}\n{bad}\n')))
        self.assertTrue(parsed[0].is_ok)
        self.assertEqual("invalid_jsonl", parsed[1].error.code)
        self.assertIn("línea 2", parsed[1].error.detail)

    def test_empty_stream_is_inconclusive_and_recommends_probe(self) -> None:
        result = run_diagnosis(self.spec, [])
        self.assertEqual("inconclusive", result.value.status)
        self.assertEqual("handshake", result.value.next_test)

    def test_candidate_set_is_monotonic_for_every_declared_outcome(self) -> None:
        for probe in self.spec.probes:
            if not probe.authorized:
                continue
            for outcome in Outcome:
                result = apply_observation(self.spec, State(self.spec.hypotheses), Observation(probe.identifier, outcome))
                if result.is_ok:
                    self.assertTrue(set(result.value.candidates).issubset(self.spec.hypotheses))

    def test_cli_success_keeps_machine_output_separate_from_diagnostics(self) -> None:
        stdout, stderr = io.StringIO(), io.StringIO()
        code = main(
            [str(LAB / "cases" / "incident-spec.json"), str(LAB / "cases" / "observations.jsonl")],
            stdout=stdout,
            stderr=stderr,
        )
        self.assertEqual(EXIT_OK, code)
        self.assertEqual("", stderr.getvalue())
        self.assertEqual(["tls"], json.loads(stdout.getvalue())["candidates"])

    def test_cli_invalid_json_uses_stderr_and_stable_exit_code(self) -> None:
        with tempfile.TemporaryDirectory(dir=LAB) as directory:
            bad = Path(directory) / "bad.json"
            bad.write_text("{bad", encoding="utf-8")
            stdout, stderr = io.StringIO(), io.StringIO()
            code = main([str(bad), str(LAB / "cases" / "observations.jsonl")], stdout=stdout, stderr=stderr)
        self.assertEqual(EXIT_INVALID_INPUT, code)
        self.assertEqual("", stdout.getvalue())
        self.assertEqual("invalid_json", json.loads(stderr.getvalue())["error"])

    def test_cli_missing_observations_is_io_failure(self) -> None:
        stdout, stderr = io.StringIO(), io.StringIO()
        code = main(
            [str(LAB / "cases" / "incident-spec.json"), str(LAB / "cases" / "missing.jsonl")],
            stdout=stdout,
            stderr=stderr,
        )
        self.assertEqual(EXIT_IO, code)
        self.assertEqual("observation_io", json.loads(stderr.getvalue())["error"])

    def test_cli_contradiction_is_domain_refusal(self) -> None:
        with tempfile.TemporaryDirectory(dir=LAB) as directory:
            observations = Path(directory) / "contradiction.jsonl"
            observations.write_text('{"test_id":"resolve","result":"blocked"}\n', encoding="utf-8")
            stdout, stderr = io.StringIO(), io.StringIO()
            code = main(
                [str(LAB / "cases" / "incident-spec.json"), str(observations)],
                stdout=stdout,
                stderr=stderr,
            )
        self.assertEqual(EXIT_DOMAIN_REFUSAL, code)
        self.assertEqual("contradictory_observation", json.loads(stderr.getvalue())["error"])

    def test_package_metadata_exposes_cli_and_python_floor(self) -> None:
        import tomllib

        metadata = tomllib.loads((LAB / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertEqual(">=3.11", metadata["project"]["requires-python"])
        self.assertEqual("diagnostic_cli.cli:entrypoint", metadata["project"]["scripts"]["diagnostic-cli"])

    @unittest.skipUnless(shutil.which("rustc"), "rustc no está disponible en este entorno")
    def test_rust_port_compiles_and_matches_shared_contract_cases(self) -> None:
        with tempfile.TemporaryDirectory(dir=LAB) as directory:
            executable = Path(directory) / ("diagnostic_core.exe" if os.name == "nt" else "diagnostic_core")
            subprocess.run(
                ["rustc", str(LAB / "ports" / "diagnostic_core.rs"), "-o", str(executable)],
                check=True,
                capture_output=True,
                text=True,
            )
            completed = subprocess.run(
                [str(executable), str(LAB / "cases" / "contract-cases.tsv")],
                check=True,
                capture_output=True,
                text=True,
            )
        self.assertEqual(
            [
                "resolve_dns|ok|dns|1",
                "resolve_not_dns|ok|tls,http|1",
                "handshake_tls|ok|tls|3",
                "request_http|ok|http|5",
            ],
            completed.stdout.splitlines(),
        )


if __name__ == "__main__":
    unittest.main()
