from __future__ import annotations

import argparse
import html
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "curriculum.yaml"
SOURCE_PATH = ROOT / "sources/baseline.json"

REQUIRED_CLASS_SECTIONS = [
    "## Ficha",
    "## Prerrequisitos",
    "## Problema auténtico",
    "## Objetivos observables",
    "## Mapa conceptual",
    "## Conceptos y decisiones",
    "## Ejemplo mínimo",
    "## Ejemplo profesional",
    "## Práctica guiada",
    "## Ejercicios",
    "## Fallo controlado y diagnóstico",
    "## Entorno y archivos clave",
    "## Seguridad, ética y accesibilidad",
    "## Transferencia",
    "## Evaluación y evidencia",
    "## Fuentes",
    "## Límites y siguiente paso",
]

PART_SOURCE_MAP = {
    "00": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "01": ["IEEE-SWEBOK-4A"],
    "02": ["IEEE-SWEBOK-4A"],
    "03": ["IETF-RFC-9110"],
    "04": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "05": ["IEEE-SWEBOK-4A"],
    "06": ["IEEE-SWEBOK-4A"],
    "07": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "08": ["IEEE-SWEBOK-4A"],
    "09": ["IEEE-SWEBOK-4A"],
    "10": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "11": ["IEEE-SWEBOK-4A"],
    "12": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "13": ["IEEE-SWEBOK-4A", "OPENAPI-LATEST"],
    "14": ["W3C-WCAG", "ISO-25010-2023"],
    "15": ["IEEE-SWEBOK-4A"],
    "16": ["IEEE-SWEBOK-4A", "GITHUB-ACTIONS-SHA"],
    "17": ["IEEE-SWEBOK-4A"],
    "18": ["IEEE-SWEBOK-4A"],
    "19": ["W3C-WCAG", "IETF-RFC-9110"],
    "20": ["IETF-RFC-9110", "OPENAPI-LATEST"],
    "21": ["ISO-25010-2023"],
    "22": ["ISO-25010-2023", "NIST-SSDF-800-218"],
    "23": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "24": ["IEEE-SWEBOK-4A"],
    "25": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "26": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "27": ["IEEE-SWEBOK-4A", "OPENAPI-LATEST"],
    "28": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "29": ["IEEE-SWEBOK-4A", "NIST-SSDF-800-218"],
    "30": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "31": ["ISO-25010-2023"],
    "32": ["NIST-SSDF-800-218", "OWASP-ASVS"],
    "33": ["NIST-SSDF-800-218", "GITHUB-ACTIONS-SHA"],
    "34": ["NIST-SSDF-800-218", "GITHUB-ACTIONS-SHA"],
    "35": ["IEEE-SWEBOK-4A", "ISO-25010-2023"],
    "36": ["IEEE-SWEBOK-4A"],
    "37": ["IEEE-SWEBOK-4A", "ACM-IEEE-SE2014"],
    "38": ["NIST-AI-RMF", "NIST-AI-600-1", "NIST-SSDF-800-218"],
    "39": ["GITHUB-SPEC-KIT", "MCP-2026-07-28", "NIST-AI-RMF", "NIST-AI-600-1"],
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def write_generated(path: Path, content: str, check: bool, stale: list[str]) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(relative(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def class_scaffold(part: dict, lesson: dict, source_ids: list[str]) -> str:
    sources = "\n".join(f"- `{source_id}` — fuente inicial; precisar uso al construir la clase." for source_id in source_ids)
    return f"""# {lesson['id']} — {lesson['title']}

> [!WARNING]
> Estado: **PLANNED**. Este archivo es un scaffold de fase 2, no una clase terminada.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | {part['stage']} · {part['stage_title']} |
| Parte | {part['id']} · {part['title']} |
| Tipo | `{lesson['kind']}` |
| Propietario profundo | `{part['owner']}` |
| Horas estimadas | {lesson['estimated_hours']} |

## Prerrequisitos

Pendiente de desarrollar en la fase de contenido.

## Problema auténtico

Pendiente de desarrollar en la fase de contenido.

## Objetivos observables

- Pendiente de desarrollar.

## Mapa conceptual

Pendiente de desarrollar.

## Conceptos y decisiones

Pendiente de desarrollar.

## Ejemplo mínimo

Pendiente de desarrollar. No se añadirá código ornamental cuando el objetivo sea conceptual.

## Ejemplo profesional

Pendiente de desarrollar con contexto, restricciones y evidencia.

## Práctica guiada

Pendiente de desarrollar.

## Ejercicios

1. Básico — pendiente.
2. Intermedio — pendiente.
3. Avanzado — pendiente.

## Fallo controlado y diagnóstico

Pendiente de desarrollar.

## Entorno y archivos clave

Pendiente de declarar por sistema operativo, runtime, comandos, datos y recuperación.

## Seguridad, ética y accesibilidad

Pendiente de desarrollar según los riesgos reales de la clase.

## Transferencia

Pendiente de desarrollar hacia otra tecnología, plataforma o dominio.

## Evaluación y evidencia

Pendiente de desarrollar con criterios observables y conexión al portafolio.

## Fuentes

{sources}

## Límites y siguiente paso

Este scaffold solo demuestra que la clase tiene identidad, lugar y contrato. No demuestra aprendizaje ni ejecución.
"""


def class_metadata(part: dict, lesson: dict, source_ids: list[str]) -> dict:
    return {
        "schema_version": 1,
        "id": lesson["id"],
        "title": lesson["title"],
        "stage": part["stage"],
        "part": part["id"],
        "kind": lesson["kind"],
        "owner": part["owner"],
        "estimated_hours": lesson["estimated_hours"],
        "status": lesson["status"],
        "source_ids": source_ids,
        "path": lesson["path"],
    }


def part_index(part: dict) -> str:
    rows = []
    for lesson in part["lessons"]:
        folder = Path(lesson["path"]).name
        rows.append(
            f"| {lesson['id']} | [{lesson['title']}]({folder}/README.md) | "
            f"{lesson['kind']} | {lesson['estimated_hours']} | {lesson['status']} |"
        )
    return f"""# Parte {part['id']} — {part['title']}

- **Etapa:** {part['stage']} · {part['stage_title']}
- **Propietario profundo:** `{part['owner']}`
- **Estado:** doce clases planificadas; contenido pendiente.

| ID | Clase | Tipo | Horas | Estado |
| --- | --- | --- | ---: | --- |
{chr(10).join(rows)}

[Volver al índice de clases](../README.md)
"""


def classes_index(program: dict) -> str:
    rows = []
    for part in program["parts"]:
        start = part["lessons"][0]["id"]
        end = part["lessons"][-1]["id"]
        rows.append(
            f"| {part['id']} | [{part['title']}]({Path(part['path']).name}/README.md) | "
            f"{part['stage']} | {start}–{end} | `{part['owner']}` |"
        )
    return f"""# Índice de clases

> Las {program['class_count']} clases están en estado `PLANNED`. Los archivos son
> scaffolds estructurales y no deben citarse como clases terminadas.

| Parte | Título | Etapa | Clases | Propietario |
| --- | --- | --- | --- | --- |
{chr(10).join(rows)}

Generado desde [`../curriculum.yaml`](../curriculum.yaml).
"""


def source_registry(program: dict, baseline: dict) -> dict:
    baseline_ids = {item["id"] for item in baseline["sources"]}
    entries = {}
    for part in program["parts"]:
        source_ids = PART_SOURCE_MAP[part["id"]]
        unresolved = set(source_ids) - baseline_ids
        if unresolved:
            raise ValueError(f"Unknown sources for part {part['id']}: {sorted(unresolved)}")
        for lesson in part["lessons"]:
            entries[lesson["id"]] = {
                "status": "SEEDED_BASELINE",
                "source_ids": source_ids,
                "note": "Fuentes iniciales de la parte; deben ampliarse y vincularse a afirmaciones al construir la clase.",
            }
    return {
        "schema_version": 1,
        "verified_on": baseline["verified_on"],
        "class_count": len(entries),
        "classes": entries,
    }


def status_document(program: dict) -> str:
    return f"""# Estado verificable

Este archivo es generado por `scripts/build_phase2.py`. No editar manualmente.

| Superficie | Estado actual |
| --- | --- |
| Arquitectura | fases 1 y 2 completadas |
| Etapas | {len(program['stages'])} especificadas |
| Partes | {program['part_count']} indexadas |
| Clases | {program['class_count']} scaffolds `PLANNED`; 0 clases declaradas como construidas |
| Horas | {program['estimated_hours']:,} estimadas; pendientes de validación por contenido |
| Metadatos de clase | {program['class_count']} archivos generados |
| Registro bibliográfico | {program['class_count']} entradas sembradas desde fuentes base |
| Sitio | 521 páginas HTML generadas desde el manifiesto |
| Portal definitivo | catálogo navegable de fase 2; contenido pedagógico pendiente |
| Publicación | GitHub Pages mediante workflow, sujeta a verificación remota |

## Significado

La fase 2 demuestra que el programa puede generarse, navegarse y validarse sin deriva.
No demuestra que las clases estén desarrolladas. El estado `PLANNED` y los avisos de
cada scaffold son deliberados.
""".replace("2,160", "2.160")


def file_index(program: dict) -> str:
    return f"""# Índice de archivos de la fase 2

| Superficie | Ruta | Cantidad esperada |
| --- | --- | ---: |
| Manifiesto canónico | `curriculum.yaml` | 1 |
| Catálogo resumido | `catalog.json` | 1 |
| Índice general | `classes/README.md` | 1 |
| Índices de parte | `classes/part-*/README.md` | {program['part_count']} |
| Scaffolds de clase | `classes/part-*/se-*/README.md` | {program['class_count']} |
| Metadatos de clase | `classes/part-*/se-*/lesson.json` | {program['class_count']} |
| Fuentes por clase | `sources/class-sources.json` | {program['class_count']} entradas |
| Páginas del sitio | `site/**/*.html` | 521 |

Todos los conteos se validan contra `curriculum.yaml`.
"""


def site_css() -> str:
    return """:root{color-scheme:dark;--bg:#071016;--panel:#101b23;--ink:#f4f2eb;--muted:#a8b4bd;--line:#293943;--aqua:#69e2d0;--orange:#ff8c42;--max:1180px;font-family:Inter,ui-sans-serif,system-ui,sans-serif}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);line-height:1.6}a{color:var(--aqua)}.skip{position:absolute;left:-9999px}.skip:focus{left:1rem;top:1rem;background:white;color:#111;padding:.7rem;z-index:4}.hero{padding:clamp(3rem,8vw,7rem) max(1rem,calc((100% - var(--max))/2));border-bottom:1px solid var(--line);background:radial-gradient(circle at 85% 10%,#16413f,transparent 35%)}.eyebrow{color:var(--orange);text-transform:uppercase;letter-spacing:.15em;font-weight:800}.hero h1{font-size:clamp(2.8rem,8vw,7rem);line-height:.92;letter-spacing:-.055em;margin:.7rem 0}.hero p{max-width:760px;color:var(--muted)}.metrics,.stage-grid,.class-grid{display:grid;gap:1rem}.metrics{grid-template-columns:repeat(4,1fr);margin-top:2rem}.metric,.stage,.class-card,.notice{background:var(--panel);border:1px solid var(--line);padding:1.2rem}.metric strong{display:block;color:var(--aqua);font-size:1.8rem}.metric span,.meta{color:var(--muted)}main{width:min(var(--max),calc(100% - 2rem));margin:auto;padding:3rem 0 6rem}h2{font-size:clamp(1.8rem,4vw,3.6rem);line-height:1;margin:4rem 0 1.5rem}.stage-grid{grid-template-columns:repeat(2,1fr)}.stage h3{margin:.2rem 0}.toolbar{display:grid;grid-template-columns:2fr 1fr;gap:1rem;position:sticky;top:0;background:rgba(7,16,22,.95);padding:1rem 0;z-index:2}.toolbar input,.toolbar select{width:100%;background:#0b151c;border:1px solid var(--line);color:var(--ink);padding:.8rem;border-radius:.4rem;font:inherit}.class-grid{grid-template-columns:repeat(3,1fr)}.class-card h3{font-size:1.05rem;margin:.4rem 0}.badge{display:inline-block;border:1px solid #3f5a64;border-radius:999px;padding:.15rem .55rem;font-size:.75rem;color:var(--muted)}.notice{border-color:#74512c}.back{display:inline-block;margin:1rem 0}.lesson-list{padding:0;list-style:none}.lesson-list li{border-bottom:1px solid var(--line);padding:.8rem 0}.lesson{max-width:860px}.lesson section{border-top:1px solid var(--line);margin-top:2rem;padding-top:1rem}footer{border-top:1px solid var(--line);padding:2rem;text-align:center;color:var(--muted)}@media(max-width:800px){.metrics,.class-grid{grid-template-columns:repeat(2,1fr)}.stage-grid{grid-template-columns:1fr}}@media(max-width:520px){.metrics,.class-grid,.toolbar{grid-template-columns:1fr}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}\n"""


def site_js() -> str:
    return """const grid=document.querySelector('#class-grid');const result=document.querySelector('#result');const search=document.querySelector('#search');const stage=document.querySelector('#stage');let classes=[];function render(){if(!grid)return;const q=(search.value||'').toLocaleLowerCase('es');const s=stage.value;const visible=classes.filter(item=>(!s||item.stage===s)&&(!q||`${item.id} ${item.title} ${item.part_title}`.toLocaleLowerCase('es').includes(q)));grid.replaceChildren(...visible.map(item=>{const article=document.createElement('article');article.className='class-card';const meta=document.createElement('div');meta.className='meta';meta.textContent=`${item.id} · Parte ${item.part} · ${item.hours} h`;const title=document.createElement('h3');const link=document.createElement('a');link.href=item.url;link.textContent=item.title;title.append(link);const badge=document.createElement('span');badge.className='badge';badge.textContent=item.status;article.append(meta,title,badge);return article;}));result.textContent=`${visible.length} clases visibles de ${classes.length}.`;}if(grid){fetch('assets/catalog.json').then(r=>{if(!r.ok)throw new Error('No se pudo cargar el catálogo');return r.json();}).then(data=>{classes=data.classes;render();}).catch(error=>{result.textContent=error.message;});search.addEventListener('input',render);stage.addEventListener('change',render);}\n"""


def site_index(program: dict) -> str:
    stage_options = "".join(
        f'<option value="{stage["id"]}">{stage["id"]} · {html.escape(stage["title"])}</option>'
        for stage in program["stages"]
    )
    stage_cards = []
    for stage in program["stages"]:
        parts = [part for part in program["parts"] if part["stage"] == stage["id"]]
        links = " · ".join(
            f'<a href="parts/{part["id"]}.html">{part["id"]}</a>' for part in parts
        )
        stage_cards.append(
            f'<article class="stage"><span class="eyebrow">Etapa {stage["id"]}</span>'
            f'<h3>{html.escape(stage["title"])}</h3><p>{len(parts)} partes · {len(parts)*12} clases</p>'
            f'<p>{links}</p></article>'
        )
    return f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Programa verificable de ingeniería de software: 480 clases planificadas, SPEC, IA y agentes.">
<title>Software Engineering Learning Suite</title><link rel="stylesheet" href="assets/styles.css"></head>
<body><a class="skip" href="#content">Saltar al contenido</a><header class="hero"><p class="eyebrow">Programa profesional · fase 2</p>
<h1>Software Engineering<br>Learning Suite</h1><p>Del problema al producto operable: fundamentos, construcción, arquitectura, calidad, operación, SPEC e ingeniería con agentes.</p>
<div class="metrics"><div class="metric"><strong>8</strong><span>etapas</span></div><div class="metric"><strong>40</strong><span>partes</span></div><div class="metric"><strong>480</strong><span>clases planificadas</span></div><div class="metric"><strong>2.160</strong><span>horas estimadas</span></div></div></header>
<main id="content"><div class="notice"><strong>Estado honesto:</strong> esta publicación demuestra estructura, navegación y controles. Las clases siguen en estado <code>PLANNED</code>.</div>
<h2>Ocho etapas</h2><div class="stage-grid">{''.join(stage_cards)}</div>
<h2>Explorar las 480 clases</h2><div class="toolbar"><label>Buscar por ID o título<input id="search" type="search" placeholder="Ej.: contratos, SRE, agentes"></label><label>Filtrar por etapa<select id="stage"><option value="">Todas</option>{stage_options}</select></label></div>
<p id="result" aria-live="polite">Cargando catálogo…</p><div class="class-grid" id="class-grid"></div></main>
<footer>Generado desde curriculum.yaml · Línea base {program['baseline_date']}</footer><script src="assets/app.js"></script></body></html>\n"""


def part_page(part: dict) -> str:
    items = "".join(
        f'<li><a href="../classes/{lesson["id"]}.html">{lesson["id"]} — {html.escape(lesson["title"])}</a> '
        f'<span class="badge">{lesson["status"]}</span></li>' for lesson in part["lessons"]
    )
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Parte {part['id']} · {html.escape(part['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><main id="content"><a class="back" href="../index.html">← Volver al programa</a><p class="eyebrow">Etapa {part['stage']} · Parte {part['id']}</p><h1>{html.escape(part['title'])}</h1><p class="meta">Propietario profundo: {html.escape(part['owner'])}</p><div class="notice">Doce clases planificadas. El contenido pedagógico se construirá en fases posteriores.</div><ol class="lesson-list">{items}</ol></main><footer>Software Engineering Learning Suite</footer></body></html>\n"""


def class_page(part: dict, lesson: dict, source_ids: list[str]) -> str:
    source_list = "".join(f"<li><code>{html.escape(source_id)}</code></li>" for source_id in source_ids)
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{lesson['id']} · {html.escape(lesson['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><main class="lesson" id="content"><a class="back" href="../parts/{part['id']}.html">← Parte {part['id']}</a><p class="eyebrow">{lesson['id']} · {lesson['kind']}</p><h1>{html.escape(lesson['title'])}</h1><div class="notice"><strong>PLANNED:</strong> scaffold navegable; esta clase aún no contiene desarrollo pedagógico.</div><section><h2>Ficha</h2><p>Etapa {part['stage']} · Parte {part['id']} · {lesson['estimated_hours']} horas estimadas · propietario <code>{html.escape(part['owner'])}</code>.</p></section><section><h2>Contrato previsto</h2><p>Problema, objetivos, conceptos, ejemplos, práctica, tres ejercicios, fallo controlado, entorno, transferencia, evaluación, evidencia y límites.</p></section><section><h2>Fuentes iniciales</h2><ul>{source_list}</ul><p>Se ampliarán y vincularán a afirmaciones cuando la clase sea construida.</p></section></main><footer>Software Engineering Learning Suite</footer></body></html>\n"""


def validate_scaffold(path: Path, lesson: dict, failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing scaffold: {relative(path)}")
        return
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"# {lesson['id']} — {lesson['title']}"):
        failures.append(f"identity drift: {relative(path)}")
    missing = [section for section in REQUIRED_CLASS_SECTIONS if section not in text]
    if missing:
        failures.append(f"contract sections missing in {relative(path)}: {missing}")


def build(check: bool) -> tuple[list[str], list[str]]:
    program = load_json(PROGRAM_PATH)
    baseline = load_json(SOURCE_PATH)
    sources = source_registry(program, baseline)
    stale: list[str] = []
    failures: list[str] = []

    write_generated(ROOT / "sources/class-sources.json", dump_json(sources), check, stale)
    write_generated(ROOT / "classes/README.md", classes_index(program), check, stale)

    web_catalog = {"generated_on": program["baseline_date"], "classes": []}
    for part in program["parts"]:
        part_dir = ROOT / part["path"]
        write_generated(part_dir / "README.md", part_index(part), check, stale)
        source_ids = PART_SOURCE_MAP[part["id"]]
        write_generated(ROOT / "site/parts" / f"{part['id']}.html", part_page(part), check, stale)
        for lesson in part["lessons"]:
            lesson_dir = ROOT / lesson["path"]
            scaffold_path = lesson_dir / "README.md"
            if check:
                validate_scaffold(scaffold_path, lesson, failures)
            elif not scaffold_path.exists():
                scaffold_path.parent.mkdir(parents=True, exist_ok=True)
                scaffold_path.write_text(class_scaffold(part, lesson, source_ids), encoding="utf-8", newline="\n")
            write_generated(
                lesson_dir / "lesson.json",
                dump_json(class_metadata(part, lesson, source_ids)),
                check,
                stale,
            )
            write_generated(
                ROOT / "site/classes" / f"{lesson['id']}.html",
                class_page(part, lesson, source_ids),
                check,
                stale,
            )
            web_catalog["classes"].append({
                "id": lesson["id"],
                "title": lesson["title"],
                "part": part["id"],
                "part_title": part["title"],
                "stage": part["stage"],
                "kind": lesson["kind"],
                "hours": lesson["estimated_hours"],
                "status": lesson["status"],
                "url": f"classes/{lesson['id']}.html",
            })

    write_generated(ROOT / "site/index.html", site_index(program), check, stale)
    write_generated(ROOT / "site/assets/styles.css", site_css(), check, stale)
    write_generated(ROOT / "site/assets/app.js", site_js(), check, stale)
    write_generated(ROOT / "site/assets/catalog.json", dump_json(web_catalog), check, stale)
    write_generated(ROOT / "site/.nojekyll", "", check, stale)
    write_generated(ROOT / "STATUS.md", status_document(program), check, stale)
    write_generated(ROOT / "FILE_INDEX.md", file_index(program), check, stale)
    return stale, failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale, failures = build(args.check)
    if stale or failures:
        for message in (stale[:20] + failures[:20]):
            print(message, file=sys.stderr)
        if len(stale) + len(failures) > 40:
            print(f"... {len(stale) + len(failures) - 40} additional failures", file=sys.stderr)
        return 1
    action = "PHASE2_CHECK_OK" if args.check else "PHASE2_BUILD_OK"
    print(f"{action}: 40 parts, 480 class scaffolds, 521 HTML pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
