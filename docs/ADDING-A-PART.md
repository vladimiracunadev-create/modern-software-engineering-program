# Cómo añadir una parte nueva (Partes 40–48)

Procedimiento operativo derivado de [ADR-005](adr/ADR-005-publish-parts-40-44-from-content.md) y
[ADR-006](adr/ADR-006-extend-program-parts-45-48-and-roles.md).
Una parte entra en el programa cuando existe su contenido completo; no hay que editar
constantes, contadores ni tablas compartidas. Antes de empezar, lee `AGENTS.md`,
[`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md) y la nota de traspaso de la parte
anterior si existe.

## Qué define el programa y qué lo cumple

- **Títulos y rangos fijos.** `scripts/build_program_blueprint.py` ya define las 49 partes
  y sus 588 títulos: Parte 40 = `SE-481`–`SE-492`, 41 = `SE-493`–`SE-504`,
  42 = `SE-505`–`SE-516`, 43 = `SE-517`–`SE-528`, 44 = `SE-529`–`SE-540` (todas desarrolladas) y,
  planificadas por ADR-006, Parte 45 = `SE-541`–`SE-552`, 46 = `SE-553`–`SE-564`,
  47 = `SE-565`–`SE-576` y 48 = `SE-577`–`SE-588`. El primer
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

## Partes 45–48: rangos y títulos finales (ADR-006)

Estos títulos y rangos están fijados en el blueprint y no cambian sin un ADR. Las cuatro partes
nacen **planificadas**: no existen en `classes/`, `site/` ni en las guías de rol hasta que exista
su contenido completo (`content/part-NN/README.md` más los doce `SE-NNN.md`).

### Parte 45 — Ingeniería de datos y plataformas de datos (`SE-541`–`SE-552`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-541` | clase | Del dato operacional al analítico |
| `SE-542` | clase | Ingesta batch y streaming |
| `SE-543` | clase | Modelado analítico: hechos, dimensiones y granularidad |
| `SE-544` | clase | Transformación y orquestación idempotente con backfills |
| `SE-545` | clase | Calidad y observabilidad de datos |
| `SE-546` | clase | Contratos de datos y evolución de esquemas |
| `SE-547` | clase | Linaje, catálogo y metadatos |
| `SE-548` | clase | Warehouse, lake, lakehouse y formatos columnares |
| `SE-549` | clase | Gobierno, privacidad y retención de datos |
| `SE-550` | clase | Costos y operación de plataformas de datos |
| `SE-551` | taller | Taller: reparar un pipeline defectuoso |
| `SE-552` | proyecto | Proyecto: plataforma de datos mínima gobernada |

### Parte 46 — Machine learning en producción y MLOps (`SE-553`–`SE-564`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-553` | clase | Ciclo de vida de ML y por qué falla en producción |
| `SE-554` | clase | Datos de entrenamiento, etiquetas y feature stores |
| `SE-555` | clase | Experimentos y entrenamiento reproducible |
| `SE-556` | clase | Evaluación, sesgos y validación de modelos |
| `SE-557` | clase | Ajuste fino, adaptación y costo |
| `SE-558` | clase | Servir modelos: latencia, lotes y GPU |
| `SE-559` | clase | Despliegue seguro de modelos: shadow, canary y rollback |
| `SE-560` | clase | Monitoreo, deriva y reentrenamiento |
| `SE-561` | clase | Seguridad y robustez de sistemas de ML |
| `SE-562` | clase | Gobierno de IA y regulación: EU AI Act, ISO 42001 y NIST AI RMF |
| `SE-563` | taller | Taller: degradar y recuperar un modelo |
| `SE-564` | proyecto | Proyecto: sistema de ML operable con evidencia |

### Parte 47 — Sistemas críticos, tiempo real y normas de seguridad (`SE-565`–`SE-576`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-565` | clase | Riesgo, peligro y seguridad funcional: HARA, FMEA, FTA y STPA |
| `SE-566` | clase | IEC 61508 y niveles de integridad de seguridad |
| `SE-567` | clase | Automoción: ISO 26262 y niveles ASIL |
| `SE-568` | clase | Aviación: DO-178C, DO-254 y ARP4754 |
| `SE-569` | clase | Dispositivos médicos: IEC 62304 |
| `SE-570` | clase | Casos de seguridad y trazabilidad |
| `SE-571` | clase | RTOS y planificación de tiempo real |
| `SE-572` | clase | Codificación segura: MISRA y CERT |
| `SE-573` | clase | Verificación formal y model checking: TLA+, SPARK y Alloy |
| `SE-574` | clase | Verificación y cobertura: MC/DC, HIL y SIL |
| `SE-575` | taller | Taller: analizar un fallo real frente a las normas |
| `SE-576` | proyecto | Proyecto: paquete de aseguramiento de un controlador |

### Parte 48 — Runtimes y plataformas modernas (`SE-577`–`SE-588`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-577` | clase | WebAssembly y WASI |
| `SE-578` | clase | WebAssembly en servidor y borde: component model |
| `SE-579` | clase | eBPF: observabilidad, red y seguridad en el kernel |
| `SE-580` | clase | GPU y aceleradores: modelo de ejecución |
| `SE-581` | clase | Rendimiento y costo en aceleradores |
| `SE-582` | clase | Contenedores, microVM y sandboxes |
| `SE-583` | clase | Hardware seguro: TEE y atestación |
| `SE-584` | clase | Computación cuántica para ingenieros de software |
| `SE-585` | clase | Criptografía poscuántica y migración |
| `SE-586` | clase | Confianza cero en la práctica |
| `SE-587` | taller | Taller: elegir y aislar un runtime para una carga no confiable |
| `SE-588` | proyecto | Proyecto: plataforma de ejecución aislada con evidencia |

### Qué debe hacer cada sesión de contenido

- **Parte 45** (datos): usa `SE-278`, `SE-313`–`SE-324` y `SE-325`–`SE-336` como antecedentes y
  evita duplicarlos; esta parte trata la plataforma de datos como disciplina propia.
- **Parte 46** (ML): se apoya en `SE-279`, `SE-457`–`SE-468` y `SE-505`–`SE-516`; trata
  el modelo como artefacto operado, con costo de aceleradores y gobierno de IA.
- **Parte 47** (críticos): se apoya en `SE-265`–`SE-276`, `SE-283` y `SE-160`; explica las normas
  sin reproducir su texto protegido y declara que no sustituye una certificación.
- **Parte 48** (runtimes): se apoya en `SE-021`, `SE-350`–`SE-352` y `SE-389`; trata WebAssembly,
  eBPF, GPU, microVM, TEE, criptografía poscuántica y confianza cero con modelo de amenaza y medición.
- **Ampliaciones de clases existentes** (CRDT y consenso, software verde, InnerSource): se hacen
  dentro del ID existente (`SE-260`, `SE-343`, `SE-022`, `SE-200`), sin renumerar ni añadir IDs.
- **Roles:** las guías de las tres rutas nuevas (`mlops-ml-platform-engineer.md`,
  `ai-governance-responsible-ai-engineer.md`, `runtime-systems-engineer.md`) y las de los roles
  afectados ya declaran qué cambiará con cada parte (`PLANNED_BY_ROLE` en `scripts/role_profiles.py`).
  Al publicarse una parte, `build_role_guides.py` enlaza su primera, sexta y última clase sin más edición.
