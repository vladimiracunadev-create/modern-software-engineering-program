# Evidencia de validación del laboratorio

- **Fecha:** 2026-10-06
- **Entorno local observado:** CPython 3.12.9, Windows 11, AMD64
- **Datos:** cinco eventos ficticios versionados en `data/events.jsonl`
- **Red:** no utilizada
- **Dependencias externas:** ninguna

## Comprobaciones conservadas

| Comando | Criterio | Resultado local |
| --- | --- | --- |
| `python -m unittest discover -s tests -v` | seis pruebas sin fallos | PASS: 6/6 en 0,620 s |
| `python lab.py inspect --input data/events.jsonl` | JSON válido y resumen funcional estable | PASS: `summary_sha256` = `6ff71dd36b4babd1a300dfade8b9c573669d522cfffa552c240d54ea604ad6a0` |
| `python lab.py benchmark --input data/events.jsonl --repeat 7 --output work/samples.csv` | 14 muestras y un hash funcional compartido | PASS: 7 muestras por modo y el mismo `summary_sha256` |
| `python lab.py report --input data/events.jsonl --repeat 7 --output work/report.json` | informe reproducible con límites explícitos | PASS: informe generado; energía marcada como no medida |

La evidencia local no demuestra portabilidad por sí sola. El workflow del repositorio
vuelve a ejecutar las pruebas admitidas en las versiones y sistemas declarados por su
matriz. Los tiempos concretos no se versionan como promesas de rendimiento.
