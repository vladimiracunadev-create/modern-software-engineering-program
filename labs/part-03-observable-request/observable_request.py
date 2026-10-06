"""Laboratorio local para observar una peticion y fallos por fase.

No modifica DNS, rutas, certificados ni firewall del sistema. Todo el trafico real
se limita a 127.0.0.1; DNS, confianza TLS y perdida se modelan mediante adaptadores
deterministas para que la practica sea portable y no requiera privilegios.
"""

from __future__ import annotations

import argparse
import json
import socket
import threading
import time
import uuid
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ALLOWED_HOST = "127.0.0.1"
LAB_NAME = "service.test"
SCENARIOS = (
    "healthy",
    "dns_failure",
    "connection_refused",
    "tls_name_mismatch",
    "latency_timeout",
    "transient_loss",
    "http_503",
)


class LabFailure(Exception):
    """Fallo tipado cuya fase es parte del contrato observable."""

    def __init__(self, phase: str, code: str, detail: str):
        super().__init__(detail)
        self.phase = phase
        self.code = code
        self.detail = detail


@dataclass
class Timeline:
    started: float = field(default_factory=time.monotonic)
    events: list[dict[str, Any]] = field(default_factory=list)

    def add(self, phase: str, outcome: str, evidence: str) -> None:
        self.events.append(
            {
                "offset_ms": round((time.monotonic() - self.started) * 1000, 3),
                "phase": phase,
                "outcome": outcome,
                "evidence": evidence,
            }
        )


class LabResolver:
    """Resolver en memoria: nunca consulta ni cambia el DNS del host."""

    def resolve(self, name: str, fail: bool = False) -> str:
        if fail:
            raise LabFailure("dns", "name_not_found", f"{name} no existe en el mapa local")
        if name != LAB_NAME:
            raise LabFailure("dns", "name_not_allowed", "solo se permite el nombre de laboratorio")
        return ALLOWED_HOST


class _Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    transient_count = 0

    def do_GET(self) -> None:  # noqa: N802 - API de BaseHTTPRequestHandler
        request_id = self.headers.get("X-Request-ID", "missing")
        if self.path == "/slow":
            time.sleep(0.08)
        if self.path == "/transient" and type(self).transient_count == 0:
            type(self).transient_count += 1
            body = json.dumps({"status": "degraded", "request_id": request_id}).encode()
            self.send_response(503)
        else:
            body = json.dumps({"status": "ok", "request_id": request_id}).encode()
            self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Request-ID", request_id)
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            pass

    def log_message(self, _format: str, *_args: object) -> None:
        return


class LocalService:
    """Servidor de contexto que garantiza apagado y union del hilo."""

    def __enter__(self) -> "LocalService":
        _Handler.transient_count = 0
        self.server = ThreadingHTTPServer((ALLOWED_HOST, 0), _Handler)
        self.server.daemon_threads = True
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        return self

    @property
    def port(self) -> int:
        return int(self.server.server_address[1])

    def __exit__(self, *_args: object) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        if self.thread.is_alive():
            raise RuntimeError("el servidor local no termino")


def redact_headers(headers: dict[str, str]) -> dict[str, str]:
    sensitive = {"authorization", "cookie", "set-cookie", "proxy-authorization"}
    return {key: "[REDACTED]" if key.lower() in sensitive else value for key, value in headers.items()}


def _closed_local_port() -> int:
    probe = socket.socket()
    probe.bind((ALLOWED_HOST, 0))
    port = int(probe.getsockname()[1])
    probe.close()
    return port


def run_scenario(scenario: str) -> dict[str, Any]:
    if scenario not in SCENARIOS:
        raise ValueError(f"escenario desconocido: {scenario}")

    timeline = Timeline()
    request_id = uuid.uuid4().hex
    attempts = 0
    resolver = LabResolver()

    try:
        address = resolver.resolve(LAB_NAME, fail=scenario == "dns_failure")
        timeline.add("dns", "ok", f"{LAB_NAME} -> {address} mediante mapa local")

        if scenario == "tls_name_mismatch":
            timeline.add("tls", "rejected", "SAN=other.test no coincide con service.test")
            raise LabFailure("tls", "name_mismatch", "la politica rechazo el nombre antes de HTTP")

        port = _closed_local_port() if scenario == "connection_refused" else None
        if port is not None:
            attempts = 1
            timeline.add("connect", "attempt", f"destino={ALLOWED_HOST}:{port}")
            try:
                urlopen(f"http://{ALLOWED_HOST}:{port}/health", timeout=0.2)
            except URLError as exc:
                raise LabFailure("connect", "refused", type(exc.reason).__name__) from exc

        with LocalService() as service:
            path = "/health"
            timeout = 0.5
            max_attempts = 1
            if scenario == "latency_timeout":
                path, timeout = "/slow", 0.02
            elif scenario == "transient_loss":
                max_attempts = 2
            elif scenario == "http_503":
                path, max_attempts = "/transient", 2

            last_error: LabFailure | None = None
            for attempt in range(1, max_attempts + 1):
                attempts = attempt
                if scenario == "transient_loss" and attempt == 1:
                    timeline.add("transport", "dropped", "perdida sintetica antes de enviar bytes")
                    last_error = LabFailure("transport", "synthetic_loss", "primer intento descartado")
                    continue

                url = f"http://{ALLOWED_HOST}:{service.port}{path}"
                request = Request(url, headers={"X-Request-ID": request_id})
                timeline.add("connect", "ok", f"loopback:{service.port}; intento={attempt}")
                try:
                    with urlopen(request, timeout=timeout) as response:
                        body = json.loads(response.read().decode("utf-8"))
                        timeline.add("http", "ok", f"status={response.status}")
                        timeline.add("correlation", "ok", f"request_id={body['request_id']}")
                        return _result(scenario, "recovered" if attempt > 1 else "ok", attempts, request_id, timeline)
                except HTTPError as exc:
                    timeline.add("http", "retryable", f"status={exc.code}")
                    last_error = LabFailure("http", f"status_{exc.code}", "respuesta temporal")
                    continue
                except (TimeoutError, socket.timeout) as exc:
                    raise LabFailure("http_wait", "deadline_exceeded", "sin primer byte antes del deadline") from exc

            if last_error:
                raise last_error
            raise LabFailure("client", "no_result", "no se produjo un resultado")
    except LabFailure as exc:
        timeline.add(exc.phase, "failed", f"{exc.code}: {exc.detail}")
        return _result(scenario, "failed", attempts, request_id, timeline, exc)


def _result(
    scenario: str,
    outcome: str,
    attempts: int,
    request_id: str,
    timeline: Timeline,
    failure: LabFailure | None = None,
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "scenario": scenario,
        "outcome": outcome,
        "attempts": attempts,
        "request_id": request_id,
        "failure": None if failure is None else {"phase": failure.phase, "code": failure.code},
        "events": timeline.events,
        "limits": [
            "solo el intercambio HTTP usa sockets reales en loopback",
            "DNS, TLS y perdida son modelos deterministas, no implementaciones de esos protocolos",
            "el resultado local no demuestra disponibilidad de produccion",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Traza una peticion local y fallos por fase")
    parser.add_argument("scenario", choices=(*SCENARIOS, "suite"))
    args = parser.parse_args(argv)
    result: Any = [run_scenario(name) for name in SCENARIOS] if args.scenario == "suite" else run_scenario(args.scenario)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
