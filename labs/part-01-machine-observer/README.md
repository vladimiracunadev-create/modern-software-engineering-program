# Laboratorio de la Parte 01 — observar un programa por capas

Este laboratorio acompaña `SE-013`–`SE-024`. No simula una CPU ni pretende medir
energía: ofrece un programa pequeño y verificable que permite observar, con límites
explícitos, representación, traducción, runtime, memoria, proceso y tiempo.

## Pregunta integradora

¿Qué puede afirmarse sobre un programa local a partir de interfaces portables de
Python y qué conclusiones exigirían instrumentos de sistema o hardware adicionales?

El caso usa confirmaciones de matrícula **ficticias**. El mismo conjunto se procesa de
dos formas: materializando todos los registros o consumiéndolos como flujo. Ambas deben
producir el mismo resumen funcional antes de comparar recursos o tiempos.

## Relación con las clases

| Clase | Observación o evidencia en el laboratorio |
| --- | --- |
| `SE-013` | `platform`, implementación, arquitectura expuesta y orden de bytes |
| `SE-014` | serialización big-endian de la secuencia y round trip |
| `SE-015` | puntos de código, UTF-8 y normalización NFC/NFD |
| `SE-016` | suma monetaria en centavos y promedio temporal aproximado |
| `SE-017` | bytecode de CPython separado de una ISA física |
| `SE-018` | pico de asignaciones Python de materialización y streaming |
| `SE-019` | tiempo de pared y CPU del proceso, sin atribuirlos al scheduler |
| `SE-020` | AST y bytecode versionados de la función analizada |
| `SE-021` | objetos rastreados por `tracemalloc`, no RSS ni memoria nativa |
| `SE-022` | muestras crudas, unidad funcional y prohibición de inferir energía |
| `SE-023` | dossier que separa observado, inferido y no medido |
| `SE-024` | informe reproducible con hashes, entorno y revisión |

## Entorno y ejecución

Requisito mínimo: CPython 3.11 o posterior. El laboratorio usa solo la biblioteca
estándar y no instala paquetes.

```text
python lab.py inspect --input data/events.jsonl
python lab.py benchmark --input data/events.jsonl --repeat 7 --output work/samples.csv
python lab.py report --input data/events.jsonl --output work/report.json
python -m unittest discover -s tests -v
```

Los comandos `inspect` y `report` validan esquema, UTF-8 y secuencias antes de emitir
resultados. `benchmark` conserva cada muestra; no elimina valores ni declara una
variante ganadora. El directorio `work/` es desechable y no debe contener datos reales.

## Criterios de aceptación

1. las variantes materializada y streaming producen el mismo `summary_sha256`;
2. una secuencia repetida, un importe no entero o un JSON inválido termina con error;
3. el informe distingue hechos observados de interpretaciones permitidas;
4. las mediciones incluyen versión, plataforma, unidad funcional y datos crudos;
5. ninguna salida afirma instrucciones nativas, nivel de caché, julios o emisiones.

## Fallos deliberados

- Duplica `sequence` en una copia del fixture: la carga debe rechazarse.
- Cambia `encoding="utf-8"` por uno incompatible en una copia local: conserva los
  bytes originales y explica el mojibake antes de reparar.
- Compara tiempos de una sola ejecución: la revisión debe rechazar la conclusión por
  falta de repetición y por orden no controlado.

## Limpieza y recuperación

Detén cualquier ejecución con `Ctrl+C`. El programa no cambia configuración global ni
accede a red. Para limpiar, elimina únicamente `labs/part-01-machine-observer/work/`
después de comprobar la ruta. Conserva fuera de `work/` el código, fixture y pruebas.

## Límites honestos

`tracemalloc` observa asignaciones Python; no mide RSS, cachés físicas ni memoria del
kernel. `process_time_ns` no incluye espera como el tiempo de pared. El bytecode es un
detalle de CPython que cambia entre versiones. Sin un medidor o modelo validado no se
derivan energía ni carbono desde la duración.
