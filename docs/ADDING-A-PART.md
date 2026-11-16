# Cómo añadir una parte nueva (Partes 40–44)

Procedimiento operativo derivado de [ADR-005](adr/ADR-005-publish-parts-40-44-from-content.md).
Una parte entra en el programa cuando existe su contenido completo; no hay que editar
constantes, contadores ni tablas compartidas. Antes de empezar, lee `AGENTS.md`,
[`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md) y la nota de traspaso de la parte
anterior si existe.

## Qué define el programa y qué lo cumple

- **Títulos y rangos fijos.** `scripts/build_program_blueprint.py` ya define las 45 partes
  y sus 540 títulos: Parte 40 = `SE-481`–`SE-492`, 41 = `SE-493`–`SE-504`,
  42 = `SE-505`–`SE-516`, 43 = `SE-517`–`SE-528`, 44 = `SE-529`–`SE-540`. El primer
  encabezado de cada clase debe ser exactamente `# SE-NNN — <título del blueprint>`; si un
  título necesita cambiar, se cambia en el blueprint (un solo lugar) y se regenera.
- **Estado derivado.** Una parte está desarrollada si existen `content/part-NN/README.md`
  y los doce `content/part-NN/SE-NNN.md`. Con menos, sigue planificada (y el validador
  avisa si el contenido está a medias).

Cada clase debe llevar las dieciséis secciones del contrato (`REQUIRED_CLASS_SECTIONS` en
`scripts/build_phase2.py`: Prerrequisitos, Problema auténtico, … Fuentes, Límites y siguiente
paso); `validate_class_contracts.py` lo exige. El modelo de profundidad y forma es
`content/part-39/`.

## Archivos que añade cada parte (y solo esos)

| Ruta | Contenido |
| --- | --- |
| `content/part-NN/README.md` | guía de la parte (con «Evidencia medida y límites») |
| `content/part-NN/SE-NNN.md` ×12 | clases íntegras; figuras como `](figures/<archivo>.svg)` |
| `content/part-NN/part.json` | `{"sources": ["ID", …], "extra_sources": [{…}]}`: fuentes iniciales de la parte; `extra_sources` usa el formato de `sources/baseline.json` (`id`, `title`, `authority`, `url`, `status`, `used_for`) y sirve para fuentes que no están en la línea base |
| `scripts/figures_partNN_a.py`, `_b.py` | diccionario `FIGURES` (nombre de archivo → constructor); tres figuras por clase |
| `scripts/experiments_partNN_*.py` | experimentos reproducibles (semilla fija o mediciones reales) |
| `content/part-NN/figures/*.svg` | las genera `build_figures.py`; no se escriben a mano |

Además, en archivos compartidos y **solo en sus propias líneas**:

- `docs/PART-EXECUTION-TRACKER.md`: una fila de la parte (hash del commit con CI verde).
- `CHANGELOG.md`: una entrada al inicio.
- `docs/MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md`: cambiar `[ ]` por `[x]` en las 12
  casillas de la parte (el validador exige `[x]` si y solo si existe el contenido).

No se editan `README.md`, `ROADMAP.md`, `STATUS.md`, `classes/`, `site/`, `catalog.json`,
`curriculum.yaml`, `roles/` ni los scripts de generación o validación: se regeneran.
`tests/test_figures.py` ya incluye automáticamente toda parte desarrollada.

## Comandos, en este orden

```bash
python scripts/build_figures.py           # SVG de las figuras nuevas
python scripts/build_program_blueprint.py # curriculum.yaml y catalog.json
python scripts/build_phase2.py            # índices, STATUS, portal, README de estado
python scripts/build_phase3.py            # portal de clases y figuras
python scripts/build_phase4.py            # README de clase y páginas de las partes nuevas
python scripts/build_role_guides.py       # guías de rol y mapas del README
git ls-files -m | grep "figures/" | xargs -r git checkout --   # ruido de saltos de línea en Windows
```

Después se valida igual que en CI:

```bash
python scripts/validate_class_contracts.py
python scripts/validate_phase3.py
python scripts/validate_phase4.py
python scripts/validate_encoding.py
python scripts/validate_site.py
python scripts/validate_licensing.py
python scripts/validate_repository.py --strict
python -m unittest discover -s tests
npx --yes markdownlint-cli2@0.23.0 "**/*.md"
```

Los siete `--check` de CI (blueprint, fases 2–4, figuras y guías de rol) deben pasar sin
cambios pendientes. Un commit por parte; `git fetch` y rebase antes del push.

## Trabajo en paralelo y conflictos

Las partes se desarrollan en sesiones separadas. Sus archivos propios no chocan. Los
archivos generados sí cambian en cada parte (contadores y listas); si un rebase los
marca en conflicto, no se editan a mano: se toma cualquiera de las dos versiones y se
repiten los comandos de generación, y luego se añade el resultado. El tracker, el
CHANGELOG y el plan maestro solo requieren conservar ambas filas o casillas.

## Reglas para evitar falsos positivos de seguridad

- Sin rutas `/tmp` literales: usar `tempfile`.
- Sin cadenas con forma de token o clave: escribir `<TOKEN_EJEMPLO>`.
- Sin caracteres de ancho cero reales en el código fuente (Bandit B613): usar escapes.
- Alt text de figuras sin corchetes (MD039) y con las secciones
  «Cómo leer la figura» y «Dónde deja de valer».
