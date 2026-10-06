# Laboratorio de la Parte 02 — kit de diagnóstico multiplataforma

Este laboratorio integra `SE-025`–`SE-036` mediante una herramienta local pequeña,
auditable y deliberadamente limitada. Enseña a distinguir observación, diagnóstico y
reparación sin convertir una práctica educativa en un agente con autoridad sobre el
equipo.

El kit prepara únicamente una carpeta `.diagnostic-kit` dentro de un workspace
desechable explícito. `inspect` es de solo lectura; `repair` repone dos archivos
conocidos; `clean` se niega a borrar si encuentra un archivo que no reconoce. No
enumera el entorno completo, usuario, hostname, procesos ni números de serie. Tampoco
instala paquetes, eleva privilegios o cambia configuración del sistema.

## Capacidades que integra

| Clases | Capacidad | Evidencia |
| --- | --- | --- |
| `SE-025`–`SE-026` | plataforma, arquitectura, separador, sensibilidad de nombres y enlaces | reporte y `capabilities.json` |
| `SE-027`–`SE-028` | autoridad limitada, ciclo de vida y códigos de salida | negativas de ownership y códigos 0/2/3 |
| `SE-029`–`SE-030` | contrato común invocable desde Bash y PowerShell | dos adaptadores mínimos |
| `SE-031` | precedencia y redacción | argumento > entorno > archivo > default; centinela oculto |
| `SE-032`–`SE-034` | runtime, procedencia declarada y límites del entorno | versión de Python y matriz CI |
| `SE-035`–`SE-036` | fallo, diagnóstico, reparación, regresión y limpieza | diez pruebas y secuencia reproducible |

La detección de case sensitivity y enlaces crea recursos sintéticos dentro de un
directorio temporal hijo y los elimina inmediatamente. Un resultado negativo significa
“no disponible bajo esta identidad y configuración”, no “la plataforma nunca lo
soporta”.

## Requisitos y compatibilidad

- Python 3.11 o posterior, solo biblioteca estándar;
- Bash para `diagnostic-kit.sh`;
- PowerShell 7 para `diagnostic-kit.ps1`;
- un directorio desechable ya existente y controlado por quien ejecuta.

La implementación Python y sus diez pruebas se ejecutan en CI sobre Linux, Windows y
macOS. El adaptador Bash se prueba en Linux y macOS; el adaptador PowerShell se prueba
en Windows. Esa matriz no demuestra todas las distribuciones, filesystems, políticas o
versiones de shell.

## Recorrido seguro

Desde la raíz del repositorio, crea un workspace dentro del laboratorio. En PowerShell:

```powershell
$work = Join-Path $PWD 'labs/part-02-cross-platform-diagnostic-kit/work'
New-Item -ItemType Directory -Force -Path $work | Out-Null
pwsh labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.ps1 prepare --workspace $work
pwsh labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.ps1 inspect --workspace $work
```

En Bash:

```bash
mkdir -p labs/part-02-cross-platform-diagnostic-kit/work
bash labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.sh prepare \
  --workspace labs/part-02-cross-platform-diagnostic-kit/work
bash labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.sh inspect \
  --workspace labs/part-02-cross-platform-diagnostic-kit/work
```

El comando `prepare` es idempotente: la segunda ejecución debe informar `unchanged`.
La salida JSON de `inspect` usa esquema 1 y distingue `healthy`, `degraded` y
`refused`.

## Fallo controlado y recuperación

1. Abre únicamente `work/.diagnostic-kit/settings.json`.
2. Sustituye su contenido por `{broken`.
3. Ejecuta `inspect`: debe devolver código 2, estado `degraded` y categoría
   `integrity`.
4. Ejecuta `repair`: restaura configuración y capacidades sin tocar el marker.
5. Repite `inspect`: debe volver a `healthy`.

Para probar el cierre seguro, añade `student-notes.txt` dentro de `.diagnostic-kit` y
ejecuta `clean`. Debe devolver código 3 y conservar el directorio. Elimina manualmente
ese archivo sintético y repite `clean`; solo entonces se eliminan los tres archivos del
kit y su directorio. Los demás archivos del workspace permanecen intactos.

## Precedencia y secreto centinela

`profile` se resuelve en el orden argumento, `DIAG_PROFILE`, `settings.json` y valor
predeterminado. Para comprobar redacción usa un valor ficticio, nunca una credencial:

```powershell
$env:DIAG_DEMO_TOKEN = 'NEVER-PRINT-THIS-SECRET'
pwsh labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.ps1 inspect --workspace $work
Remove-Item Env:DIAG_DEMO_TOKEN
```

```bash
DIAG_DEMO_TOKEN='NEVER-PRINT-THIS-SECRET' \
  bash labs/part-02-cross-platform-diagnostic-kit/diagnostic-kit.sh inspect \
  --workspace labs/part-02-cross-platform-diagnostic-kit/work
```

El valor no debe aparecer; el reporte conserva únicamente presencia, longitud y
`[REDACTED]`. Esto demuestra el contrato para la variable conocida, no que cualquier
salida arbitraria esté libre de secretos.

## Pruebas

```bash
python -m unittest discover -s labs/part-02-cross-platform-diagnostic-kit/tests -v
```

Las pruebas cubren idempotencia, esquema y minimización, precedencia, redacción,
corrupción, reparación, limpieza acotada, negativa ante archivos ajenos, workspace
ausente y marker extraño. El criterio de éxito es diez pruebas sin fallos y ausencia
del secreto centinela en la salida.

## Códigos de salida

| Código | Significado | Acción |
| ---: | --- | --- |
| 0 | operación completada o diagnóstico sano | conservar evidencia |
| 2 | precondición, configuración o integridad inválida | corregir el fixture y repetir |
| 3 | operación rechazada por seguridad | revisar ownership o archivos ajenos |

## Limpieza y límites

Ejecuta `clean` y confirma que `.diagnostic-kit` desapareció. La carpeta `work/` queda
vacía y puede retirarse manualmente. No uses como workspace el home, raíz del sistema,
un repositorio con datos sin copia o una carpeta de terceros.

La herramienta no inspecciona ACL reales, servicios, schedulers, paquetes instalados,
contenedores ni logs del sistema porque hacerlo de forma portable, segura y útil exige
autoridad y contexto que el laboratorio no puede asumir. Las clases explican esos
mecanismos y proponen prácticas controladas; este kit integra el contrato común que sí
puede verificarse en CI.

## Fuentes

- [The Open Group Base Specifications Issue 8](https://pubs.opengroup.org/onlinepubs/9799919799/), contrato POSIX.1-2024.
- [GNU Bash Reference Manual 5.3](https://www.gnu.org/software/bash/manual/), parsing, quoting y códigos de salida.
- [PowerShell documentation](https://learn.microsoft.com/powershell/), semántica y soporte multiplataforma.
- [Python 3 documentation](https://docs.python.org/3/), APIs portables usadas por el núcleo.
