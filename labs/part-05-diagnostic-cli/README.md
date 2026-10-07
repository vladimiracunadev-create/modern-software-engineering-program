# Laboratorio — CLI diagnóstica empaquetada y contrastada

Este laboratorio convierte la especificación de la Parte 04 en un programa con fronteras explícitas. No es una demostración aislada: separa valores de dominio, política pura, parsing y terminal; conserva salida JSON en `stdout`, diagnósticos en `stderr` y códigos de salida documentados.

## Competencias observables

- rechazar coerciones y estados externos inválidos antes de entrar al dominio;
- recorrer observaciones JSONL con límite de tamaño y número de pasos;
- devolver fallos esperados mediante `Result` sin capturar defectos indiscriminadamente;
- conservar estado inmutable y el invariante de subconjunto de candidatos;
- probar reglas, fronteras, CLI y propiedades sin depender de red ni servicios;
- compilar un puerto Rust y contrastarlo con casos compartidos, sin fingir que ambos lenguajes tienen la misma arquitectura;
- entregar metadatos de paquete y un comando reproducible desde un checkout limpio.

## Arquitectura

```text
JSON/JSONL → parsing.py → domain.py → engine.py → cli.py → stdout/stderr
                                  ↘ contrato TSV ↙
                                  puerto Rust
```

`engine.py` no abre archivos ni imprime. `parsing.py` limita la entrada a 1 MB, rechaza `NaN`/`Infinity`, valida esquema y evita que `true` pase como presupuesto entero. `cli.py` traduce fallos en un contrato observable:

| Código | Significado |
|---:|---|
| `0` | cálculo válido; puede ser resuelto o inconcluso |
| `2` | uso inválido detectado por `argparse` |
| `3` | documento o registro externo inválido |
| `4` | observación rechazada por una regla del dominio |
| `5` | archivo ausente o fallo de I/O |

## Ejecutar la ruta feliz

Desde `labs/part-05-diagnostic-cli`:

```bash
PYTHONPATH=src python -m diagnostic_cli cases/incident-spec.json cases/observations.jsonl
```

En PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m diagnostic_cli cases/incident-spec.json cases/observations.jsonl
```

La salida válida contiene `"status": "resolved"` y `"candidates": ["tls"]`. No contiene mensajes diagnósticos.

## Ejecutar las pruebas

Desde la raíz del repositorio:

```bash
python -m unittest discover -s labs/part-05-diagnostic-cli/tests -v
```

La suite ejecuta quince contratos. El último compila `ports/diagnostic_core.rs` cuando `rustc` está disponible; CI lo exige explícitamente. En un equipo sin Rust se omite solo ese contraste y el informe debe declararlo.

Para repetir el contraste manual:

```bash
rustc labs/part-05-diagnostic-cli/ports/diagnostic_core.rs -o diagnostic_core
./diagnostic_core labs/part-05-diagnostic-cli/cases/contract-cases.tsv
```

## Fallos que deben observarse

1. cambia `budget` por `true`: el parser responde `invalid_budget`, aunque Python considere `bool` subtipo de `int`;
2. elimina un outcome: la especificación se rechaza antes del cálculo;
3. repite una prueba o usa `production-capture`: el dominio devuelve un rechazo explícito;
4. rompe la segunda línea JSONL: el error conserva su número de línea y no produce una salida parcial válida;
5. altera un caso TSV: Python/Rust dejan de compartir el contrato observable y la revisión debe decidir si cambió la regla o solo el puerto.

## Límites honestos

- El formato y los límites pertenecen a este contrato educativo; no son un estándar universal de CLI.
- El adaptador Rust implementa el núcleo mínimo de filtrado sobre fixtures TSV, no el parser JSON ni todo el paquete Python.
- Las pruebas no demuestran corrección para entradas infinitas ni seguridad de producción.
- El laboratorio no mide rendimiento: contar y limitar pasos no equivale a benchmark.
- `setuptools` aparece como backend de construcción, pero las pruebas no descargan ni publican paquetes.

## Fuentes primarias

- [Python Language Reference](https://docs.python.org/3/reference/)
- [Python `json` library](https://docs.python.org/3/library/json.html)
- [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259)
- [The Rust Programming Language](https://doc.rust-lang.org/stable/book/)
