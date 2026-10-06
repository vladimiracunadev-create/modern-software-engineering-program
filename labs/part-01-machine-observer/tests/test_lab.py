from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("part01_lab", ROOT / "lab.py")
assert SPEC and SPEC.loader
lab = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = lab
SPEC.loader.exec_module(lab)
FIXTURE = ROOT / "data" / "events.jsonl"


class PartOneLabTests(unittest.TestCase):
    def test_materialized_and_streaming_paths_have_the_same_contract(self) -> None:
        materialized = lab.summarize(list(lab.iter_events(FIXTURE)))
        streaming = lab.summarize(lab.iter_events(FIXTURE))
        self.assertEqual(materialized, streaming)
        self.assertEqual(5, materialized["count"])
        self.assertEqual(7200, materialized["amount_total_cents"])

    def test_binary_contract_declares_width_and_byte_order(self) -> None:
        evidence = lab.binary_evidence(513)
        self.assertEqual("0201", evidence["big_endian_hex"])
        self.assertEqual("0102", evidence["little_endian_hex"])
        self.assertEqual(513, evidence["big_endian_round_trip"])

    def test_unicode_evidence_keeps_distinct_units_visible(self) -> None:
        evidence = lab.text_evidence("José ✓")
        self.assertTrue(evidence["round_trip"])
        self.assertIn("U+00E9", evidence["code_points"])
        self.assertGreater(evidence["nfd_code_points"], evidence["nfc_code_points"])

    def test_duplicate_sequences_fail_closed(self) -> None:
        event = {
            "sequence": 7,
            "message": "ficticio",
            "duration_ms": 1.0,
            "amount_cents": 0,
        }
        with tempfile.TemporaryDirectory(dir=ROOT, prefix=".test-") as directory:
            path = Path(directory) / "duplicate.jsonl"
            path.write_text(
                json.dumps(event) + "\n" + json.dumps(event) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "duplicate sequence"):
                list(lab.iter_events(path))

    def test_report_separates_observation_from_unmeasured_claims(self) -> None:
        report = lab.inspect_input(FIXTURE)
        self.assertIn("summary_sha256", report)
        self.assertIn("native instructions and CPU cycles", report["claims"]["not_measured"])
        self.assertIn("energy and carbon emissions", report["claims"]["not_measured"][-1])

    def test_benchmark_preserves_raw_samples_and_functional_hash(self) -> None:
        rows = lab.benchmark(FIXTURE, repeat=3)
        self.assertEqual(6, len(rows))
        self.assertEqual(1, len({row["summary_sha256"] for row in rows}))
        report = lab.benchmark_report(rows)
        self.assertFalse(report["energy_measured"])
        self.assertEqual(3, report["modes"]["streaming"]["samples"])


if __name__ == "__main__":
    unittest.main()
