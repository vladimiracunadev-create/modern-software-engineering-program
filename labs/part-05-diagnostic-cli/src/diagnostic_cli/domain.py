"""Valores inmutables y resultados explícitos del dominio diagnóstico."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Generic, TypeVar


class Outcome(str, Enum):
    FAIL = "fail"
    OK = "ok"
    BLOCKED = "blocked"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Probe:
    identifier: str
    cost: int
    authorized: bool
    outcomes: tuple[tuple[str, Outcome], ...]

    def outcome_for(self, hypothesis: str) -> Outcome | None:
        return dict(self.outcomes).get(hypothesis)


@dataclass(frozen=True)
class DiagnosticSpec:
    decision: str
    budget: int
    hypotheses: tuple[str, ...]
    probes: tuple[Probe, ...]

    def probe(self, identifier: str) -> Probe | None:
        return next((probe for probe in self.probes if probe.identifier == identifier), None)


@dataclass(frozen=True)
class Observation:
    test_id: str
    result: Outcome


@dataclass(frozen=True)
class State:
    candidates: tuple[str, ...]
    spent: int = 0
    used: frozenset[str] = frozenset()


@dataclass(frozen=True)
class DomainError:
    code: str
    detail: str


T = TypeVar("T")


@dataclass(frozen=True)
class Result(Generic[T]):
    """Un éxito o un fallo esperado; nunca ambos ni ninguno."""

    value: T | None = None
    error: DomainError | None = None

    def __post_init__(self) -> None:
        if (self.value is None) == (self.error is None):
            raise ValueError("Result requires exactly one of value or error")

    @property
    def is_ok(self) -> bool:
        return self.error is None

    @classmethod
    def ok(cls, value: T) -> Result[T]:
        return cls(value=value)

    @classmethod
    def fail(cls, code: str, detail: str) -> Result[T]:
        return cls(error=DomainError(code, detail))
