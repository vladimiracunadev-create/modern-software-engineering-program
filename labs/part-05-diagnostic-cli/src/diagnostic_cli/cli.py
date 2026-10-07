"""Adaptador de terminal con stdout, stderr y códigos de salida estables."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from .engine import run_diagnosis
from .parsing import iter_json_lines, load_json_document, parse_spec

EXIT_OK = 0
EXIT_INVALID_INPUT = 3
EXIT_DOMAIN_REFUSAL = 4
EXIT_IO = 5


def _error(stream: TextIO, code: str, detail: str) -> None:
    # ASCII escapado conserva el mismo JSON en consolas con codepages distintas.
    print(json.dumps({"error": code, "detail": detail}, ensure_ascii=True, sort_keys=True), file=stream)


def main(argv: list[str] | None = None, *, stdout: TextIO = sys.stdout, stderr: TextIO = sys.stderr) -> int:
    parser = argparse.ArgumentParser(description="Selecciona la próxima prueba diagnóstica autorizada")
    parser.add_argument("spec", type=Path, help="especificación JSON")
    parser.add_argument("observations", type=Path, help="observaciones JSONL")
    args = parser.parse_args(argv)

    document = load_json_document(args.spec)
    if not document.is_ok:
        assert document.error is not None
        _error(stderr, document.error.code, document.error.detail)
        return EXIT_IO if document.error.code == "not_found" else EXIT_INVALID_INPUT
    specification = parse_spec(document.value)
    if not specification.is_ok:
        assert specification.error is not None
        _error(stderr, specification.error.code, specification.error.detail)
        return EXIT_INVALID_INPUT
    try:
        with args.observations.open("r", encoding="utf-8") as stream:
            assert specification.value is not None
            report = run_diagnosis(specification.value, iter_json_lines(stream))
    except (FileNotFoundError, OSError, UnicodeDecodeError) as error:
        _error(stderr, "observation_io", str(error))
        return EXIT_IO
    if not report.is_ok:
        assert report.error is not None
        _error(stderr, report.error.code, report.error.detail)
        input_codes = {"invalid_jsonl", "invalid_observation", "input_too_large"}
        return EXIT_INVALID_INPUT if report.error.code in input_codes else EXIT_DOMAIN_REFUSAL
    assert report.value is not None
    print(json.dumps(report.value.to_dict(), ensure_ascii=True, sort_keys=True), file=stdout)
    return EXIT_OK


def entrypoint() -> None:
    raise SystemExit(main())
