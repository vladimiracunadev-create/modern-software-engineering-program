# Módulo 13 — Modernización legacy

## Objetivos

- caracterizar un sistema antes de modificarlo;
- separar actualización, refactor, replatform y reescritura;
- migrar por capacidades reversibles;
- preservar reglas y continuidad.

## Contenidos

Arqueología de código y datos; pruebas de caracterización; observabilidad; seams; anti-corruption layer; strangler; migración de datos; doble escritura y reconciliación; feature flags; retiro.

## Laboratorio

Selecciona una capacidad legacy. Captura contrato real, métricas y fallos. Introduce fachada, migra una lectura en sombra, compara respuestas y define corte/rollback. Solo migra escritura después de resolver idempotencia y datos.

## Criterio

Cada incremento reduce incertidumbre y puede revertirse sin pérdida de operación.
