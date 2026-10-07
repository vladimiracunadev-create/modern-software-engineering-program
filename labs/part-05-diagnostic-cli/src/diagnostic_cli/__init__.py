"""Núcleo público de la CLI diagnóstica de la Parte 05."""

from .domain import DiagnosticSpec, Observation, Outcome, Probe, Result, State
from .engine import DiagnosticReport, apply_observation, run_diagnosis

__all__ = [
    "DiagnosticReport",
    "DiagnosticSpec",
    "Observation",
    "Outcome",
    "Probe",
    "Result",
    "State",
    "apply_observation",
    "run_diagnosis",
]
