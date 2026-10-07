"""Política pura: no abre archivos, no imprime y no conoce argparse."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable

from .domain import DiagnosticSpec, Observation, Probe, Result, State


@dataclass(frozen=True)
class TimelineEntry:
    test_id: str
    result: str
    remaining: tuple[str, ...]
    spent: int


@dataclass(frozen=True)
class DiagnosticReport:
    schema_version: int
    decision: str
    status: str
    candidates: tuple[str, ...]
    spent: int
    remaining_budget: int
    next_test: str | None
    timeline: tuple[TimelineEntry, ...]
    limits: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def apply_observation(spec: DiagnosticSpec, state: State, observation: Observation) -> Result[State]:
    probe = spec.probe(observation.test_id)
    if probe is None:
        return Result.fail("unknown_test", observation.test_id)
    if not probe.authorized:
        return Result.fail("unauthorized_test", probe.identifier)
    if probe.identifier in state.used:
        return Result.fail("duplicate_observation", probe.identifier)
    if state.spent + probe.cost > spec.budget:
        return Result.fail("budget_exceeded", probe.identifier)
    candidates = tuple(
        candidate
        for candidate in state.candidates
        if probe.outcome_for(candidate) == observation.result
    )
    if not candidates:
        return Result.fail("contradictory_observation", f"{probe.identifier}:{observation.result.value}")
    if not set(candidates).issubset(state.candidates):
        raise AssertionError("candidate subset invariant violated")
    return Result.ok(State(candidates, state.spent + probe.cost, state.used | {probe.identifier}))


def _partition_size(probe: Probe, candidates: tuple[str, ...]) -> int:
    groups: dict[str, int] = {}
    for candidate in candidates:
        outcome = probe.outcome_for(candidate)
        key = "missing" if outcome is None else outcome.value
        groups[key] = groups.get(key, 0) + 1
    return max(groups.values(), default=0)


def select_next(spec: DiagnosticSpec, state: State) -> Probe | None:
    remaining_budget = spec.budget - state.spent
    options: list[tuple[float, int, int, str, Probe]] = []
    for probe in spec.probes:
        if probe.identifier in state.used or not probe.authorized or probe.cost > remaining_budget:
            continue
        eliminated = len(state.candidates) - _partition_size(probe, state.candidates)
        options.append((eliminated / probe.cost, eliminated, -probe.cost, probe.identifier, probe))
    return max(options, key=lambda item: item[:4])[-1] if options else None


def run_diagnosis(spec: DiagnosticSpec, observations: Iterable[Result[Observation]]) -> Result[DiagnosticReport]:
    state = State(spec.hypotheses)
    timeline: list[TimelineEntry] = []
    max_steps = len(spec.probes)
    for step, parsed in enumerate(observations, start=1):
        if step > max_steps:
            return Result.fail("too_many_observations", f"máximo {max_steps}")
        if not parsed.is_ok:
            return Result(error=parsed.error)
        assert parsed.value is not None
        applied = apply_observation(spec, state, parsed.value)
        if not applied.is_ok:
            return Result(error=applied.error)
        assert applied.value is not None
        state = applied.value
        timeline.append(TimelineEntry(parsed.value.test_id, parsed.value.result.value, state.candidates, state.spent))
    recommendation = select_next(spec, state)
    report = DiagnosticReport(
        schema_version=1,
        decision=spec.decision,
        status="resolved" if len(state.candidates) == 1 else "inconclusive",
        candidates=state.candidates,
        spent=state.spent,
        remaining_budget=spec.budget - state.spent,
        next_test=None if recommendation is None else recommendation.identifier,
        timeline=tuple(timeline),
        limits=(
            "la salida depende de las hipótesis y outcomes declarados",
            "la heurística local no garantiza una secuencia global óptima",
            "la ejecución local no demuestra comportamiento de producción",
        ),
    )
    return Result.ok(report)
