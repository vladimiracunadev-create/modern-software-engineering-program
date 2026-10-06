from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB))

from observable_request import SCENARIOS, LocalService, redact_headers, run_scenario  # noqa: E402


class ObservableRequestTests(unittest.TestCase):
    def test_healthy_request_is_correlated(self) -> None:
        result = run_scenario("healthy")
        self.assertEqual("ok", result["outcome"])
        self.assertEqual(["dns", "connect", "http", "correlation"], [event["phase"] for event in result["events"]])
        self.assertEqual(32, len(result["request_id"]))

    def test_dns_failure_stops_before_connect(self) -> None:
        result = run_scenario("dns_failure")
        self.assertEqual({"phase": "dns", "code": "name_not_found"}, result["failure"])
        self.assertNotIn("connect", [event["phase"] for event in result["events"]])

    def test_connection_failure_stops_before_http(self) -> None:
        result = run_scenario("connection_refused")
        self.assertEqual("connect", result["failure"]["phase"])
        self.assertNotIn("http", [event["phase"] for event in result["events"]])

    def test_tls_model_rejects_wrong_name_before_http(self) -> None:
        result = run_scenario("tls_name_mismatch")
        self.assertEqual({"phase": "tls", "code": "name_mismatch"}, result["failure"])
        self.assertNotIn("http", [event["phase"] for event in result["events"]])

    def test_latency_exhausts_read_deadline(self) -> None:
        result = run_scenario("latency_timeout")
        self.assertEqual({"phase": "http_wait", "code": "deadline_exceeded"}, result["failure"])

    def test_synthetic_loss_recovers_only_after_bounded_retry(self) -> None:
        result = run_scenario("transient_loss")
        self.assertEqual("recovered", result["outcome"])
        self.assertEqual(2, result["attempts"])
        self.assertEqual("dropped", result["events"][1]["outcome"])

    def test_http_503_recovers_and_keeps_evidence(self) -> None:
        result = run_scenario("http_503")
        self.assertEqual("recovered", result["outcome"])
        self.assertEqual(2, result["attempts"])
        self.assertTrue(any(event["evidence"] == "status=503" for event in result["events"]))

    def test_sensitive_headers_are_redacted(self) -> None:
        redacted = redact_headers({"Authorization": "secret", "Cookie": "id=1", "Accept": "application/json"})
        self.assertEqual("[REDACTED]", redacted["Authorization"])
        self.assertEqual("application/json", redacted["Accept"])

    def test_local_service_stops_its_thread(self) -> None:
        with LocalService() as service:
            thread = service.thread
            self.assertTrue(thread.is_alive())
        self.assertFalse(thread.is_alive())

    def test_every_scenario_declares_model_limits(self) -> None:
        for scenario in SCENARIOS:
            with self.subTest(scenario=scenario):
                result = run_scenario(scenario)
                self.assertEqual(3, len(result["limits"]))
                self.assertTrue(all("produccion" not in event["evidence"] for event in result["events"]))

    def test_cli_suite_is_machine_readable(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(LAB / "observable_request.py"), "suite"],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(list(SCENARIOS), [item["scenario"] for item in payload])


if __name__ == "__main__":
    unittest.main()
