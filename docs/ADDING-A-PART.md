# Cómo desarrollar una parte reservada (Partes 34 y 42)

Procedimiento operativo derivado de [ADR-005](adr/ADR-005-publish-parts-40-44-from-content.md),
[ADR-006](adr/ADR-006-extend-program-parts-45-48-and-roles.md) y
[ADR-007](adr/ADR-007-pedagogical-renumbering-and-new-parts.md). Una parte entra en el
programa cuando existe su contenido completo; no hay que editar constantes, contadores ni
tablas compartidas. Antes de empezar, lee `AGENTS.md`,
[`PEDAGOGICAL-STANDARD.md`](PEDAGOGICAL-STANDARD.md) y la nota de traspaso de la parte
anterior si existe. Las citas anteriores al 2026-11-23 usan la numeración histórica: el mapa
está en [`ID-MIGRATION.md`](ID-MIGRATION.md).

## Qué define el programa y qué lo cumple

- **Títulos y rangos fijos.** `scripts/build_program_blueprint.py` ya define las 51 partes y
  sus 612 títulos en secuencia pedagógica; las Partes 00–22 conservan el número de siempre.
  La regla de ID es `12 × parte + posición` (la posición va de 1 a 12). Las partes por
  desarrollar son la **34** (`SE-409`–`SE-420`, etapa E) y la **42** (`SE-505`–`SE-516`,
  etapa G). El primer encabezado de cada clase debe ser exactamente
  `# SE-NNN — <título del blueprint>`; si un título necesita cambiar, se cambia en el
  blueprint (un solo lugar) con un ADR y se regenera.
- **Estado derivado.** Una parte está desarrollada si existen `content/part-NN/README.md`
  y los doce `content/part-NN/SE-NNN.md`. Con menos, sigue planificada (y el validador
  avisa si el contenido está a medias). Mientras una parte esté planificada, su hueco no
  rompe nada: la navegación anterior/siguiente salta a la clase desarrollada vecina y el
  portal sirve la página `404.html`, que explica el cambio de numeración, en las URL vacantes.

Cada clase debe llevar las dieciséis secciones del contrato (`REQUIRED_CLASS_SECTIONS` en
`scripts/build_phase2.py`: Prerrequisitos, Problema auténtico, … Fuentes, Límites y siguiente
paso); `validate_class_contracts.py` lo exige. El modelo de profundidad y forma es
`content/part-47/`.

## Archivos que añade cada parte (y solo esos)

| Ruta | Contenido |
| --- | --- |
| `content/part-NN/README.md` | guía de la parte (con «Evidencia medida y límites») |
| `content/part-NN/SE-NNN.md` ×12 | clases íntegras; figuras como `](figures/<archivo>.svg)` |
| `content/part-NN/part.json` | `{"sources": ["ID", …], "extra_sources": [{…}]}`: fuentes iniciales de la parte; `extra_sources` usa el formato de `sources/baseline.json` (`id`, `title`, `authority`, `url`, `status`, `used_for`) y sirve para fuentes que no están en la línea base |
| `scripts/figures_partNN_a.py`, `_b.py` | diccionario `FIGURES` (nombre de archivo → constructor); tres figuras por clase |
| `scripts/experiments_partNN_*.py` | experimentos reproducibles (semilla fija o mediciones reales) |
| `content/part-NN/figures/*.svg` | las genera `build_figures.py`; no se escriben a mano |
| `roles/<rol>.md` y su perfil | solo si la parte crea un rol (ver abajo) |

Además, en archivos compartidos y **solo en sus propias líneas**:

- `docs/PART-EXECUTION-TRACKER.md`: una fila de la parte (hash del commit con CI verde).
- `CHANGELOG.md`: una entrada al inicio.
- `docs/MASTER-CURRICULUM-IMPLEMENTATION-PLAN.md`: cambiar `[ ]` por `[x]` en las 12
  casillas de la parte (el validador exige `[x]` si y solo si existe el contenido).

No se editan `README.md`, `ROADMAP.md`, `STATUS.md`, `classes/`, `site/`, `catalog.json`,
`curriculum.yaml` ni los scripts de generación o validación: se regeneran.
`tests/test_figures.py` y `tests/test_navigation_gaps.py` ya incluyen automáticamente toda
parte desarrollada.

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

## Partes reservadas: rangos y títulos fijos (ADR-007)

Estos títulos y rangos están fijados en el blueprint y no cambian sin un ADR. Las dos partes
nacieron **planificadas**: no existen en `classes/`, `site/` (salvo la página-aviso de la URL
vacante) ni en las guías de rol hasta que exista su contenido completo
(`content/part-NN/README.md` más los doce `SE-NNN.md`).

### Parte 34 — SaaS y plataformas de producto (`SE-409`–`SE-420`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-409` | clase | SaaS como producto y como operación: del software al servicio continuo |
| `SE-410` | clase | Tenencia, organizaciones e identidad en un producto SaaS |
| `SE-411` | clase | Planes, derechos de uso y control de funcionalidades |
| `SE-412` | clase | Medición de uso, facturación y suscripciones |
| `SE-413` | clase | Activación, onboarding y ciclo de vida de la cuenta |
| `SE-414` | clase | Ciclo de vida del tenant: aprovisionamiento, migración y baja |
| `SE-415` | clase | APIs públicas, webhooks y ecosistema de integraciones |
| `SE-416` | clase | Plataformas extensibles: plugins, SDK y marketplaces |
| `SE-417` | clase | Confiabilidad como promesa comercial: SLA, SLO y créditos |
| `SE-418` | clase | Economía unitaria y costo de servir por tenant |
| `SE-419` | taller | Taller: diseñar los planes y el aislamiento de un SaaS |
| `SE-420` | proyecto | Proyecto: núcleo de un SaaS multi-tenant con facturación por uso |

### Parte 42 — Ingeniería del caos (`SE-505`–`SE-516`)

| Clase | Tipo | Título exacto |
| --- | --- | --- |
| `SE-505` | clase | Principios de la ingeniería del caos: estado estable e hipótesis |
| `SE-506` | clase | Diseñar experimentos de fallo: alcance y radio de impacto |
| `SE-507` | clase | Inyección de fallos de red, latencia y dependencias |
| `SE-508` | clase | Fallos de recursos e infraestructura: CPU, memoria, disco y nodos |
| `SE-509` | clase | Caos en Kubernetes y en plataformas cloud |
| `SE-510` | clase | Fallos de datos y de estado: réplicas, particiones y corrupción |
| `SE-511` | clase | Game days y ejercicios de respuesta a incidentes |
| `SE-512` | clase | Caos continuo: automatización en CI/CD y en producción |
| `SE-513` | clase | Seguridad y gobernanza de los experimentos: abortar, autorizar y registrar |
| `SE-514` | clase | Aprender de los experimentos: hallazgos, métricas y mejora |
| `SE-515` | taller | Taller: ejecutar un experimento de caos acotado con criterio de aborto |
| `SE-516` | proyecto | Proyecto: programa de caos de un servicio con evidencia y remediación |


### Qué debe hacer cada sesión de contenido

- **Parte 34** (SaaS): se apoya en la tenencia y el aislamiento de la Parte 28 (estilos
  arquitectónicos), en la integración de la Parte 31, en la nube de la Parte 33, en la
  economía de producto de la Parte 11 y en la observabilidad de la Parte 41; no duplica esas
  clases: trata el producto SaaS como disciplina propia (planes, medición, facturación, ciclo
  de vida del tenant y costo de servir). Cada afirmación sobre un proveedor o una norma cita
  fuente oficial vigente.
- **Parte 42** (caos): se apoya en la resiliencia de la Parte 36, en los incidentes y los SLO de
  la Parte 41 y en la concurrencia y los sistemas distribuidos de la Parte 32. Todo
  experimento declara hipótesis, radio de impacto, criterio de aborto y datos sintéticos; no
  se prueba en sistemas ajenos ni se recomienda caos sin observabilidad previa.
- **Roles:** ADR-007 decidió dos guías nuevas, *SaaS & Product Platform Engineer* (Parte 34) y
  *Chaos Engineer* (Parte 42). Se crean con su parte: perfil en `scripts/role_profiles.py`
  (con núcleo, flujo, decisiones, métricas, escenario, proyecto, fuentes y adyacentes), guía
  en `roles/` con más de 2.200 palabras y dos gráficos interpretables, y su nombre en las
  listas `EXTRA_ADJACENT` de los roles vecinos. Hoy las partes figuran como contexto
  planificado en `PLANNED_BY_ROLE`; al publicarse, `build_role_guides.py` enlaza su primera,
  sexta y última clase sin más edición. El programa tiene 45 roles hasta entonces.
- **Ampliaciones de clases existentes** (CRDT y consenso, software verde, InnerSource):
  se hacen dentro del ID existente (`SE-260`, `SE-391`, `SE-022` y
  `SE-200`), sin renumerar ni añadir IDs.
