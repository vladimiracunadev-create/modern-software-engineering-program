# Evidencia de validación — Parte 05

## Contratos verificables

| Contrato | Evidencia automatizada |
|---|---|
| tipos externos estrictos | `test_parse_rejects_boolean_budget_without_silent_integer_coercion` |
| esquema completo | `test_parse_rejects_incomplete_outcome_map` |
| transformación sin mutación accidental | `test_apply_observation_returns_new_state_without_mutating_input` |
| resultado explícito consistente | `test_explicit_result_rejects_impossible_state` |
| autorización, repetición y presupuesto | pruebas de rechazo del dominio |
| JSONL localizable | `test_stream_reports_malformed_line_with_location` |
| terminación acotada | máximo de observaciones igual al número de pruebas |
| invariante de candidatos | propiedad de subconjunto para todos los outcomes declarados |
| contrato de terminal | pruebas de stdout, stderr y códigos `0`, `3`, `4`, `5` |
| paquete | lectura reproducible de `pyproject.toml` |
| transferencia | compilación de Rust y cuatro casos TSV comunes |

## Comandos de aceptación

```bash
python -m unittest discover -s labs/part-05-diagnostic-cli/tests -v
python -m compileall -q labs/part-05-diagnostic-cli/src
```

CI añade la compilación obligatoria de `diagnostic_core.rs` en Ubuntu. En Windows y macOS vuelve a ejecutar la suite Python para demostrar que rutas, encoding y códigos no dependen del shell.

## Resultado esperado

- quince pruebas aprobadas cuando existe `rustc`;
- catorce aprobadas y una omisión declarada cuando el compilador no está instalado;
- cuatro líneas equivalentes producidas por el puerto Rust;
- cero escritura fuera de archivos temporales creados por la suite;
- cero red, secretos o acceso a producción.

## Lo que no se afirma

No se afirma que el paquete haya sido publicado, que el algoritmo sea óptimo, que Rust y Python compartan modelo de memoria, ni que las fixtures representen todos los incidentes posibles. La evidencia protege el contrato declarado y deja esas fronteras visibles.
