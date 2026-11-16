"""Generate the "Casos de estudio" surface: group pages, section text and the portal pages.

* ``casos/exito/README.md`` and ``casos/fallo/README.md`` come from ``scripts/cases_data.py``;
* the 16 case files ``casos/<kind>/<slug>.md`` are written by hand (a skeleton carries
  ``SKELETON_MARKER`` until the case is written) and are only *read* here;
* ``site/casos/**`` holds the portal pages (group indexes, one page per case) and
  ``site/casos/figures/`` a copy of ``casos/figures/*.svg``.

``python scripts/build_cases.py`` writes, ``--check`` verifies. ``build_phase2`` imports
``readme_section()`` to render the README block between the parts table and the role routes.
"""
from __future__ import annotations

import argparse
import html
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from cases_data import CASES, GITHUB_BLOB, KINDS, SKELETON_MARKER, cases_of  # noqa: E402

PROGRAM_NAME = "Programa de Ingeniería de Software Moderna"
GUIDE = "casos/GUIDE.md"
GROUP_FILES = {kind: f"casos/{kind}/README.md" for kind in KINDS}
NAV_PREFIX = "[↑ "


def group_title(kind: str) -> str:
    return "Casos de éxito" if kind == "exito" else "Casos de fallo"


def case_nav(case: dict[str, str]) -> str:
    """The one-line navigation every case file carries at the top and at the bottom."""
    group = cases_of(case["kind"])
    index = group.index(case)
    parts = [f"[↑ {group_title(case['kind'])}](README.md)"]
    if index:
        parts.append(f"[← {group[index - 1]['name']}]({group[index - 1]['slug']}.md)")
    if index + 1 < len(group):
        parts.append(f"[{group[index + 1]['name']} →]({group[index + 1]['slug']}.md)")
    return " · ".join(parts)


def index_lines(kind: str) -> str:
    lines = []
    for case in cases_of(kind):
        lines.append(
            f"- [{case['name']}]({case['slug']}.md) — **{case['year']}** · {case['who']}. {case['hook']}"
        )
    return "\n".join(lines)


# --------------------------------------------------------------------------- group pages
GROUP_TEXT = {
    "exito": {
        "what": (
            "Esta página reúne ocho plataformas que lograron escala, ingresos o una posición difícil de disputar: "
            "Netflix, WhatsApp, Uber, Mercado Libre, Amazon, Spotify, Airbnb y Stripe. Cada una tiene su propio caso, "
            "escrito como un estudio completo: ficha histórica, problema, usuarios, funcionalidad de principio a fin, "
            "economía, arquitectura con esquemas, casos especiales, línea de tiempo y vínculo con las clases."
        ),
        "why": (
            "El curso enseña mecanismos (concurrencia, contratos, datos, despliegue, observabilidad) con ejemplos "
            "controlados. Un caso real muestra qué ocurre cuando esos mecanismos se combinan bajo presión de mercado, "
            "con equipos, dinero y plazos. Se construyó para contrastar la teoría con decisiones que alguien tomó, "
            "con sus costes, y para evitar dos errores opuestos: pensar que la teoría no sirve fuera del aula y "
            "creer que lo que funcionó en una empresa funcionará en cualquier otra."
        ),
        "use": [
            "Léelos **después** de las partes del curso que cada caso enlaza; sin esa base, el caso es una anécdota.",
            "Antes de leer la sección de arquitectura, intenta dibujar tú el sistema con lo que ya sabes y compáralo.",
            "Busca en cada caso la decisión que **no** harías en tu contexto y explica por qué no se transfiere.",
            "Cierra con la sección «Qué no generalizar»: es la que separa aprender de imitar.",
        ],
        "limits": (
            "Son estudios sobre fuentes públicas, no auditorías internas: lo que no es público se declara como "
            "desconocido y no se inventa. Un éxito comercial no demuestra que cada decisión técnica fuera correcta."
        ),
    },
    "fallo": {
        "what": (
            "Esta página reúne ocho fallos de plataformas y sistemas: Knight Capital, HealthCare.gov, TSB, la caída "
            "global de Meta en 2021, CrowdStrike, Therac-25, el incidente de GitLab en 2017 y Quibi. Cada uno tiene su "
            "propio caso, con lo que falló en cada instancia, la causa raíz, los factores que contribuyeron y las "
            "mejoras que debieron hacerse."
        ),
        "why": (
            "Los fallos son la evidencia más barata de por qué existen las prácticas del curso: pruebas, despliegue "
            "progresivo, respaldos verificados, observabilidad, gestión de incidentes y ética profesional. Se "
            "construyó para que cada práctica tenga un daño concreto detrás y para entrenar el análisis sin culpables: "
            "separar hechos, interpretación y lecciones."
        ),
        "use": [
            "Léelos **después** de la teoría del curso; el objetivo es reconocer los mecanismos, no juzgar a las personas.",
            "Antes de leer la causa raíz, escribe tu hipótesis sobre qué falló y qué señal habría avisado.",
            "Distingue en cada caso el detonante (lo que ocurrió ese día) de las condiciones latentes (lo que hizo posible el daño).",
            "Termina con «Mejoras que debieron hacerse» y comprueba cuáles ya existen en tu propio sistema.",
        ],
        "limits": (
            "Los informes públicos son incompletos y a veces contradictorios. Los casos citan investigaciones y "
            "post-mortems, declaran lo que no se sabe y no atribuyen intención donde la evidencia solo muestra error."
        ),
    },
}


def group_markdown(kind: str) -> str:
    info, text = KINDS[kind], GROUP_TEXT[kind]
    other = "fallo" if kind == "exito" else "exito"
    use = "\n".join(f"{i}. {item}" for i, item in enumerate(text["use"], 1))
    return f"""# Casos de estudio · {info['title']}

[↑ Programa](../../README.md) · [Guía de casos](../GUIDE.md) · [{group_title(other)} →](../{other}/README.md)

> Esta superficie no son clases ni roles: no cuenta en las 540 clases ni en las 45 partes. Es la realidad
> frente a la teoría del curso.

## Qué es

{text['what']}

## Por qué se construyó

{text['why']}

## Cómo usar esta página pedagógicamente

{use}

## Cómo se lee un caso

Todos los casos siguen el mismo esquema (definido en la [guía de casos](../GUIDE.md)) para poder
compararlos: ficha histórica, contexto y problema, mercado y usuarios, funcionalidad de principio a fin,
negocio y economía, arquitectura y esquemas, casos especiales, línea de tiempo,{' qué falló, causa raíz y mejoras,' if kind == 'fallo' else ''} vínculo con el curso, qué no generalizar y fuentes públicas.
Las afirmaciones llevan fuente; lo inferido se marca como interpretación.

## Mapa visual

![Mapa de {info['title'].lower()}: cada columna nombra una tensión de ingeniería, los casos que la ilustran y las partes del curso que dan herramientas para analizarla](../figures/{kind}-mapa.svg)

**Cómo leer el mapa.** Cada columna es una tensión de ingeniería; las cajas blancas son los casos que mejor
la ilustran y la caja gris inferior nombra las partes del curso con las herramientas para analizarla. La
agrupación es orientativa: sirve para elegir por dónde empezar, no para clasificar de forma excluyente.

## Índice de casos

{index_lines(kind)}

## Límites

{text['limits']}

[↑ Programa](../../README.md) · [Guía de casos](../GUIDE.md) · [{group_title(other)} →](../{other}/README.md)
"""


def skeleton(case: dict[str, str]) -> str:
    """Minimal valid case file, published until the session that owns the case replaces it."""
    nav = case_nav(case)
    return f"""# {case['name']}

{nav}

{SKELETON_MARKER}

> **Estado: en elaboración.** Este caso sigue el esquema de la [guía de casos](../GUIDE.md) y se publicará completo
> en un commit propio. Ficha provisional: {case['who']} · {case['year']} · {case['place']}.

{case['hook']}

---

{nav}
"""


# --------------------------------------------------------------------------- README section
def readme_section() -> str:
    exito, fallo = len(cases_of("exito")), len(cases_of("fallo"))
    return f"""## 🏛️ Casos de estudio: la realidad frente a la teoría

Además de las partes y los roles, el programa ofrece una superficie propia: **casos de estudio** de plataformas
reales. No son clases ni roles, no crean partes y no cambian las 540 clases: se leen **después** de la teoría para
ver cómo se combinan sus mecanismos con equipos, dinero y plazos. Cada caso sigue un esquema único (ficha
histórica, problema, usuarios, funcionalidad de principio a fin, economía, arquitectura con esquemas, casos
especiales, línea de tiempo, vínculo con las clases, qué no generalizar y fuentes públicas) descrito en la
[guía de casos]({GUIDE}).

- 🚀 [**Plataformas exitosas**](casos/exito/README.md): {exito} casos, de Netflix a Stripe.
- 🧯 [**Plataformas y sistemas que fallaron**](casos/fallo/README.md): {fallo} casos, de Knight Capital a Quibi.
"""


# --------------------------------------------------------------------------- portal
def site_target(source_dir: str, target: str, case_files: set[str]) -> str:
    """Rewrite a relative Markdown link of a case file for site/casos/<kind>/<page>.html."""
    path, _, anchor = target.partition("#")
    suffix = f"#{anchor}" if anchor else ""
    resolved = posixpath.normpath(posixpath.join(source_dir, path))
    class_match = re.fullmatch(r"classes/part-\d\d-[^/]+/(se-(\d{3})-[^/]+)/README\.md", resolved)
    if class_match:
        return f"../../classes/SE-{class_match.group(2)}.html{suffix}"
    part_match = re.fullmatch(r"classes/part-(\d\d)-[^/]+/README\.md", resolved)
    if part_match:
        return f"../../parts/{part_match.group(1)}.html{suffix}"
    if resolved in {"README.md"}:
        return f"../../index.html{suffix}"
    if resolved in case_files:
        kind, name = resolved.split("/")[1:3]
        page = "index.html" if name == "README.md" else name.removesuffix(".md") + ".html"
        here = source_dir.split("/")[1]
        return (f"./{page}" if kind == here else f"../{kind}/{page}") + suffix
    if resolved.startswith("casos/figures/"):
        return f"../figures/{resolved.rsplit('/', 1)[1]}"
    return GITHUB_BLOB + resolved + suffix


LINK = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')


def case_html_markdown(markdown: str, source: str) -> str:
    case_files = {f"casos/{c['kind']}/{c['slug']}.md" for c in CASES} | {
        f"casos/{k}/README.md" for k in KINDS
    }
    source_dir = posixpath.dirname(source)

    def replace(match: re.Match[str]) -> str:
        bang, label, target, caption = match.groups()
        if bang or re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|\.\./figures/)", target):
            return match.group(0)
        return f"[{label}]({site_target(source_dir, target, case_files)}{caption})"

    lines = [line for line in markdown.splitlines() if not line.startswith(NAV_PREFIX)]
    body = "\n".join(lines)
    body = body.replace(SKELETON_MARKER, "")
    return LINK.sub(replace, body)


def page(title: str, description: str, eyebrow: str, nav: str, hero: str, body: str, toc: str, source_url: str) -> str:
    return (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="description" content="{html.escape(description)}">'
        f"<title>{html.escape(title)}</title>"
        '<link rel="stylesheet" href="../../assets/styles.css"></head><body>'
        '<a class="skip" href="#content">Saltar al contenido</a>'
        f'<main class="lesson" id="content">{nav}'
        f'<header class="lesson-hero"><p class="eyebrow">{html.escape(eyebrow)}</p><h1>{html.escape(title)}</h1><p>{html.escape(hero)}</p></header>'
        f'<div class="lesson-shell"><nav class="lesson-toc" aria-label="Contenido de la página"><strong>En esta página</strong><ol>{toc}</ol></nav>'
        f'<article class="lesson-content">{body}</article></div>'
        f'<p class="source-link"><a href="{source_url}">Ver el archivo fuente en GitHub</a></p>{nav}</main>'
        f"<footer>{PROGRAM_NAME} · Casos de estudio: la realidad frente a la teoría</footer></body></html>\n"
    )


def site_pages(read) -> dict[Path, str]:
    from build_phase3 import markdown_to_html

    result: dict[Path, str] = {}
    for kind, info in KINDS.items():
        group = cases_of(kind)
        other = "fallo" if kind == "exito" else "exito"
        nav = (
            '<nav class="class-nav" aria-label="Navegación de casos">'
            f'<a href="../../index.html">Programa</a><span>{group_title(kind)}</span>'
            f'<a href="../{other}/index.html">{group_title(other)} →</a></nav>'
        )
        source = GROUP_FILES[kind]
        content, headings = markdown_to_html(case_html_markdown(read(source), source))
        toc = "".join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in headings)
        result[ROOT / "site/casos" / kind / "index.html"] = page(
            f"Casos de estudio · {info['title']}",
            f"Casos de estudio de {info['title'].lower()}: la realidad frente a la teoría del curso.",
            "Casos de estudio · superficie propia, no son clases ni roles", nav,
            "Léelos después de la teoría: cada caso enlaza las clases que lo explican.",
            content, toc, GITHUB_BLOB + source,
        )
        for index, case in enumerate(group):
            previous = group[index - 1] if index else None
            following = group[index + 1] if index + 1 < len(group) else None
            prev_link = f'<a href="{previous["slug"]}.html">← {html.escape(previous["name"])}</a>' if previous else "<span>Inicio</span>"
            next_link = f'<a href="{following["slug"]}.html">{html.escape(following["name"])} →</a>' if following else "<span>Fin</span>"
            case_nav_html = (
                '<nav class="class-nav" aria-label="Navegación entre casos">'
                f'{prev_link}<a href="index.html">{group_title(kind)}</a><a href="../../index.html">Programa</a>{next_link}</nav>'
            )
            source = f"casos/{kind}/{case['slug']}.md"
            content, headings = markdown_to_html(case_html_markdown(read(source), source))
            toc = "".join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in headings)
            result[ROOT / "site/casos" / kind / f"{case['slug']}.html"] = page(
                f"{case['name']} · caso de estudio",
                f"Caso de estudio {info['label']}: {case['name']} ({case['year']}). {case['hook']}",
                f"Caso de {info['label']} · {case['year']} · {case['who']}", case_nav_html, case["hook"],
                content, toc, GITHUB_BLOB + source,
            )
    return result


def expected_files() -> dict[Path, str]:
    def read(rel: str) -> str:
        return (ROOT / rel).read_text(encoding="utf-8")

    files: dict[Path, str] = {}
    for kind, rel in GROUP_FILES.items():
        files[ROOT / rel] = group_markdown(kind)
    # Group pages are generated first so the portal reads the fresh text.
    fresh = {rel: group_markdown(kind) for kind, rel in GROUP_FILES.items()}
    files.update(site_pages(lambda rel: fresh[rel] if rel in fresh else read(rel)))
    for svg in sorted((ROOT / "casos/figures").glob("*.svg")):
        files[ROOT / "site/casos/figures" / svg.name] = svg.read_text(encoding="utf-8")
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--init-skeletons", action="store_true", help="write the missing case files as skeletons")
    args = parser.parse_args()
    if args.init_skeletons:
        for case in CASES:
            path = ROOT / f"casos/{case['kind']}/{case['slug']}.md"
            if not path.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(skeleton(case), encoding="utf-8", newline="\n")
    files = expected_files()
    stale = []
    for path, content in files.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        print("CASES_STALE: " + ", ".join(stale[:30]), file=sys.stderr)
        return 1
    print(("CASES_CHECK_OK" if args.check else "CASES_BUILD_OK") + f": {len(files)} files, {len(CASES)} cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
