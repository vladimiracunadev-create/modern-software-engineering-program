"""Genera la superficie «Glosario»: entradas, índices, inventario y páginas del portal.

* ``glosario/entradas/<letra>/<slug>.md``: una entrada por concepto del inventario;
* ``glosario/README.md``, ``glosario/indice/<letra>.md``, ``glosario/familias/<etapa>.md``,
  ``glosario/INVENTARIO.md``: puntos de entrada e inventario;
* ``glosario/curado/<slug>.md``: texto escrito a mano (fuente editable, solo se lee aquí);
* ``glosario/casos.json``: dónde aparece cada concepto en los casos (se refresca con
  ``--refresh-cases``; la comprobación no lo exige para no acoplar el glosario al ritmo de los casos);
* ``site/glosario/**``: el portal, con búsqueda por término.

``python scripts/build_glossary.py`` escribe, ``--check`` verifica. ``build_phase2`` importa
``readme_section()`` para el bloque del README raíz.
"""
from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cross_references  # noqa: E402
import glossary_compose as gc  # noqa: E402
import glossary_data as data  # noqa: E402

PROGRAM_NAME = "Programa de Ingeniería de Software Moderna"
GITHUB_BLOB = "https://github.com/vladimiracunadev-create/modern-software-engineering-program/blob/main/"
CASES_JSON = ROOT / "glosario" / "casos.json"
STAGE_LABEL = {stage["id"]: stage["title"] for stage in data.program()["stages"]}
ROLES_FAMILY = ("R", "Rutas por rol")


# --------------------------------------------------------------------------- datos derivados
def load_cases() -> dict[str, list[list[str]]]:
    if CASES_JSON.is_file():
        return json.loads(CASES_JSON.read_text(encoding="utf-8"))
    return {}


def refresh_cases() -> dict[str, list[list[str]]]:
    from cases_data import CASES

    texts = {case["slug"]: (ROOT / f"casos/{case['kind']}/{case['slug']}.md").read_text(encoding="utf-8") for case in CASES
             if (ROOT / f"casos/{case['kind']}/{case['slug']}.md").is_file()}
    prepared = {slug: f" {data.key_of(data.plain(text))} " for slug, text in texts.items()}
    result: dict[str, list[list[str]]] = {}
    for concept in data.inventory().values():
        if "role" in concept.kinds:
            continue
        keys = [k for k in concept.keys if len(k.replace(" ", "")) > 3]
        hits = []
        for case in CASES:
            haystack = prepared.get(case["slug"], "")
            if sum(haystack.count(f" {key} ") for key in keys) >= 2:
                hits.append([case["kind"], case["slug"], case["name"]])
        if hits:
            result[concept.slug] = hits[:5]
    return dict(sorted(result.items()))


def family_of(concept: data.Concept) -> tuple[str, str]:
    if concept.role:
        return ROLES_FAMILY
    first = data.classes()[concept.classes[0]]
    return first.stage, STAGE_LABEL[first.stage]


def origin_part(concept: data.Concept) -> str:
    return data.classes()[concept.classes[0]].part if concept.classes else ""


def depth_label(entry: gc.Entry) -> str:
    return "desarrollada" if entry.developed else "compuesta desde las clases"


def tier_label(concept: data.Concept) -> str:
    return data.tier_of(concept)


# --------------------------------------------------------------------------- entradas
def short_definition(entry: gc.Entry) -> str:
    first = entry.sections["Definición"].split("\n\n")[0]
    first = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", first).replace("**", "").strip()
    words = first.split()
    return " ".join(words[:28]) + ("…" if len(words) > 28 else "")


def entries() -> list[gc.Entry]:
    curated = gc.load_curated()
    cases = load_cases()
    result = []
    for concept in data.inventory().values():
        hits = [tuple(hit) for hit in cases.get(concept.slug, [])]
        result.append(gc.compose(concept, curated, hits))
    return result


def entry_markdown(entry: gc.Entry, previous: gc.Entry | None, following: gc.Entry | None) -> str:
    concept = entry.concept
    base = f"{gc.ENTRY_DIR}/{data.letter_of(concept.slug)}"
    nav = ["[↑ Glosario](../../README.md)"]
    if previous:
        nav.append(f"[← {previous.concept.name}]({cross_references.relative_link(base, gc.entry_path(previous.concept))})")
    if following:
        nav.append(f"[{following.concept.name} →]({cross_references.relative_link(base, gc.entry_path(following.concept))})")
    nav_line = " · ".join(nav)
    stage, stage_name = family_of(concept)
    origin = origin_part(concept)
    meta = [
        f"**Tipo:** {data.kind_of(concept)}",
        f"**Nivel:** {tier_label(concept)}",
        f"**Profundidad:** {depth_label(entry)}",
        f"**Familia:** {stage} — {stage_name}" if stage != "R" else f"**Familia:** {stage_name}",
    ]
    if origin:
        meta.append(f"**Primera aparición:** Parte {origin}")
    lines = [f"# {concept.name}", "", nav_line, "", "> " + " · ".join(meta), ""]
    for name in gc.SECTIONS:
        lines += [f"## {name}", "", entry.sections[name].strip(), ""]
    lines += ["---", "", nav_line, ""]
    text = "\n".join(lines)
    return cross_references.resolve(text, base)


# --------------------------------------------------------------------------- índices
def counts(items: list[gc.Entry]) -> dict[str, Counter]:
    return {
        "tipo": Counter(data.kind_of(e.concept) for e in items),
        "nivel": Counter(tier_label(e.concept) for e in items),
        "profundidad": Counter(depth_label(e) for e in items),
        "familia": Counter(family_of(e.concept)[0] for e in items),
    }


def line_for(entry: gc.Entry, base: str) -> str:
    concept = entry.concept
    first = concept.classes[0] if concept.classes else ""
    where = f" · {gc.short_class_link(first, base)}" if first else ""
    return f"- {gc.entry_link(concept, base)} — {data.kind_of(concept)} · {tier_label(concept)}{where}. {short_definition(entry)}"


def letters(items: list[gc.Entry]) -> list[str]:
    return sorted({data.letter_of(e.concept.slug) for e in items}, key=lambda l: (l == "0-9", l))


def letter_pages(items: list[gc.Entry]) -> dict[str, str]:
    by_letter: dict[str, list[gc.Entry]] = defaultdict(list)
    for e in items:
        by_letter[data.letter_of(e.concept.slug)].append(e)
    order = letters(items)
    files: dict[str, str] = {}
    for index, letter in enumerate(order):
        nav = ["[↑ Glosario](../README.md)"]
        if index:
            nav.append(f"[← {order[index - 1].upper()}]({order[index - 1]}.md)")
        if index + 1 < len(order):
            nav.append(f"[{order[index + 1].upper()} →]({order[index + 1]}.md)")
        body = "\n".join(line_for(e, "glosario/indice") for e in by_letter[letter])
        text = (f"# Glosario · índice alfabético · {letter.upper()}\n\n{' · '.join(nav)}\n\n"
                f"{len(by_letter[letter])} entradas que empiezan por {letter.upper()}.\n\n{body}\n\n---\n\n{' · '.join(nav)}\n")
        files[f"glosario/indice/{letter}.md"] = cross_references.resolve(text, "glosario/indice")
    return files


def family_pages(items: list[gc.Entry]) -> dict[str, str]:
    stages = [(sid, title) for sid, title in STAGE_LABEL.items()] + [ROLES_FAMILY]
    files: dict[str, str] = {}
    for index, (sid, title) in enumerate(stages):
        members = [e for e in items if family_of(e.concept)[0] == sid]
        nav = ["[↑ Glosario](../README.md)"]
        if index:
            nav.append(f"[← {stages[index - 1][1]}]({stages[index - 1][0].lower()}.md)")
        if index + 1 < len(stages):
            nav.append(f"[{stages[index + 1][1]} →]({stages[index + 1][0].lower()}.md)")
        lines = [f"# Glosario · familia {sid} · {title}", "", " · ".join(nav), ""]
        if sid == "R":
            lines += [f"{len(members)} guías de rol del programa, cada una con su entrada.", ""]
            lines += [line_for(e, "glosario/familias") for e in members]
        else:
            lines += [f"{len(members)} conceptos cuya primera aparición está en las partes de la etapa {sid}. "
                      "Cada sección es una parte; los conceptos troncales van primero.", ""]
            by_part: dict[str, list[gc.Entry]] = defaultdict(list)
            for e in members:
                by_part[origin_part(e.concept)].append(e)
            for part in data.program()["parts"]:
                if part["id"] not in by_part:
                    continue
                group = sorted(by_part[part["id"]], key=lambda e: (tier_label(e.concept) != "troncal", data.fold(e.concept.name)))
                lines += [f"## Parte {part['id']} — {part['title']}", "", f"{len(group)} conceptos.", ""]
                lines += [line_for(e, "glosario/familias") for e in group]
                lines.append("")
        lines += ["---", "", " · ".join(nav), ""]
        files[f"glosario/familias/{sid.lower()}.md"] = cross_references.resolve("\n".join(lines), "glosario/familias")
    return files


def table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    out += ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join(out)


def inventory_markdown(items: list[gc.Entry]) -> str:
    inv = data.inventory()
    classes = data.classes()
    c = counts(items)
    raw_def = sum(len(cls.definitions) for cls in classes.values())
    raw_glossary = sum(len(cls.glossary_terms) for cls in classes.values())
    raw_topics = sum(len(cls.topics) for cls in classes.values())
    raw_topic_terms = sum(1 for cls in classes.values() for topic, _ in cls.topics if data.term_like(topic))
    forms = {form for concept in inv.values() for form in concept.forms}
    merged = sum(1 for concept in inv.values() if len({f for f in concept.forms}) > 1)
    origin = Counter()
    for concept in inv.values():
        origin["rol" if concept.role else "+".join(sorted(k for k in concept.kinds))] += 1
    kind_names = {"definition": "definición de trabajo", "glossary": "glosario de la clase", "topic": "tema de la clase"}
    by_source = Counter()
    for concept in inv.values():
        if concept.role:
            by_source["guía de rol"] += 1
        elif "definition" in concept.kinds:
            by_source["definición de trabajo"] += 1
        elif "glossary" in concept.kinds:
            by_source["glosario de la clase"] += 1
        else:
            by_source["tema de la clase (en dos o más clases)"] += 1
    part_rows = []
    for part in data.program()["parts"]:
        members = [e for e in items if origin_part(e.concept) == part["id"]]
        troncal = sum(1 for e in members if tier_label(e.concept) == "troncal")
        part_rows.append([f"Parte {part['id']} — {part['title']}", str(len(members)), str(troncal), str(len(members) - troncal)])
    family_rows = [[f"{sid} — {title}", str(c["familia"].get(sid, 0))] for sid, title in STAGE_LABEL.items()] + [[ROLES_FAMILY[1], str(c["familia"].get("R", 0))]]
    sample = sorted(((len(set(concept.forms)), concept.name, sorted(set(concept.forms))[:4]) for concept in inv.values() if len(set(concept.forms)) > 2), reverse=True)[:12]
    lines = [
        "# Inventario de conceptos del glosario",
        "",
        "[↑ Glosario](README.md)",
        "",
        "> Este archivo lo genera `scripts/build_glossary.py` a partir de las clases publicadas; no se edita a mano.",
        "",
        "## Resultado",
        "",
        f"El inventario contiene **{len(items)} conceptos**, cada uno con su entrada: {c['nivel']['troncal']} troncales y {c['nivel']['apoyo']} de apoyo. "
        f"Salen de {len(classes)} clases y {len([e for e in items if e.concept.role])} guías de rol.",
        "",
        "## Cómo se extrajo",
        "",
        "1. **Definiciones de trabajo.** Cada viñeta `- **término:** definición` del apartado «Definiciones de trabajo» (y del «Glosario» cuando es una lista) de las clases es una aparición de un término.",
        "2. **Glosarios en prosa.** Los términos en negrita del apartado «Glosario» de las clases que lo redactan como párrafo.",
        "3. **Temas.** Las filas de la tabla «Temas y por qué importan» que son términos: una a cuatro palabras, sin preguntas ni frases con coma, ni «y»/«o». Solo cuentan si el término ya está definido o el tema se repite en otra clase.",
        "4. **Guías de rol.** Una entrada por guía de `roles/`.",
        "",
        "Los términos en negrita sueltos de la prosa, los títulos de clase y los conceptos de los casos de estudio no crean entradas por sí solos: "
        "los títulos de clase son listas de temas (ya cubiertas por el apartado de temas) y la negrita de la prosa marca énfasis, no definición. "
        "Los casos se enlazan desde las entradas cuando mencionan el concepto (`glosario/casos.json`).",
        "",
        "## Normalización",
        "",
        "Dos redacciones son el mismo concepto si comparten alguna clave: minúsculas, sin tildes ni puntuación, palabras en singular, "
        "con el paréntesis separado como alias (`reversión (rollback)` aporta `reversión` y `rollback`) y con las siglas unidas a su expansión.",
        "",
        table(["Medida", "Valor"], [
            ["Definiciones de trabajo leídas", str(raw_def)],
            ["Términos en glosarios en prosa", str(raw_glossary)],
            ["Filas de temas leídas", str(raw_topics)],
            ["Filas de temas con forma de término", str(raw_topic_terms)],
            ["Redacciones distintas tras separar paréntesis", str(len(forms))],
            ["Conceptos tras normalizar y deduplicar (sin roles)", str(len(inv) - len([e for e in items if e.concept.role]))],
            ["Conceptos con más de una redacción unificada", str(merged)],
        ]),
        "",
        "Conceptos que más variantes unificaron:",
        "",
        "\n".join(f"- {name}: {', '.join(variants)}" for _, name, variants in sample),
        "",
        "## Criterio de tipificación",
        "",
        "La tipificación es léxica y determinista: no es un juicio editorial.",
        "",
        "- **Nivel troncal:** el concepto estructura una parte: lo definen o lo titulan tres o más clases, o es a la vez tema, sección y definición de una misma clase, "
        "o lo definen dos clases y además es tema o sección. También son troncales las guías de rol. El resto es **de apoyo**.",
        "- **Profundidad:** *desarrollada* si todas las secciones principales de la entrada están escritas a mano en `glosario/curado/`; "
        "*compuesta desde las clases* si la entrada reúne, con atribución, lo que las clases ya enseñan sobre el término.",
        "- **Tipo:** sigla (nombre en mayúsculas), norma o marco (nombra un estándar), métrica (tasa, latencia, cobertura…), "
        "práctica o técnica (empieza por prueba, revisión, despliegue…), rol profesional y concepto (el resto).",
        "",
        "## Conteos",
        "",
        "Por nivel:",
        "",
        table(["Nivel", "Entradas"], [[k, str(v)] for k, v in sorted(c["nivel"].items())]),
        "",
        "Por profundidad:",
        "",
        table(["Profundidad", "Entradas"], [[k, str(v)] for k, v in sorted(c["profundidad"].items())]),
        "",
        "Por tipo:",
        "",
        table(["Tipo", "Entradas"], [[k, str(v)] for k, v in sorted(c["tipo"].items(), key=lambda kv: -kv[1])]),
        "",
        "Por origen del concepto:",
        "",
        table(["Origen", "Entradas"], [[k, str(v)] for k, v in sorted(by_source.items(), key=lambda kv: -kv[1])]),
        "",
        "Por familia (etapa de la primera clase donde aparece):",
        "",
        table(["Familia", "Entradas"], family_rows),
        "",
        "Por parte de primera aparición:",
        "",
        table(["Parte", "Entradas", "Troncales", "De apoyo"], part_rows),
        "",
        "---",
        "",
        "[↑ Glosario](README.md)",
        "",
    ]
    return cross_references.resolve("\n".join(lines), "glosario")


def readme_markdown(items: list[gc.Entry]) -> str:
    c = counts(items)
    n = len(items)
    order = letters(items)
    by_letter = Counter(data.letter_of(e.concept.slug) for e in items)
    letter_links = " · ".join(f"[{l.upper()}](indice/{l}.md) ({by_letter[l]})" for l in order)
    family_lines = "\n".join(
        f"- [{sid} — {title}](familias/{sid.lower()}.md): {c['familia'].get(sid, 0)} entradas" for sid, title in STAGE_LABEL.items()
    ) + f"\n- [{ROLES_FAMILY[1]}](familias/r.md): {c['familia'].get('R', 0)} entradas"
    developed = c["profundidad"].get("desarrollada", 0)
    text = f"""# Glosario del programa

[↑ Programa](../README.md) · [Inventario](INVENTARIO.md) · [Guía editorial](GUIDE.md)

> Esta superficie no son clases ni roles: no cuenta en las clases ni en las partes del programa. Es el vocabulario
> del programa, cada término vinculado a las clases donde se enseña.

## Qué es

El glosario reúne **{n} conceptos** del programa, cada uno con una entrada que lo define con precisión, explica por qué
importa y cómo funciona, da un ejemplo, advierte de errores y límites, lo relaciona con otros conceptos, dice dónde se enseña y
con qué fuentes. Los conceptos salen de las definiciones de trabajo, los glosarios y los temas de las 612 clases, y de las
guías de rol; el [inventario](INVENTARIO.md) explica cómo se extrajeron y cómo se normalizaron.

## Para qué sirve

- **Resolver un término** que aparece en una clase sin haber leído las anteriores: la entrada da el sentido que usa el programa
  y los prerrequisitos.
- **Distinguir conceptos que se parecen**: cada entrada declara con qué se confunde y dónde deja de valer.
- **Volver a las clases**: «Dónde se enseña» enlaza las clases que lo desarrollan y las que solo lo usan; las clases, a su vez,
  enlazan sus conceptos al final.

## Cómo se usa

1. Busca el término en el [portal](../site/glosario/index.html) (búsqueda por término y por sigla) o en el índice alfabético.
2. Lee la **Definición** y **Por qué importa**; si el término es nuevo, sigue «Prerrequisito» antes de seguir.
3. Contrasta con **Límites** y **Errores y confusiones comunes** antes de aplicarlo a tu caso.
4. Abre las clases de «Dónde se enseña» para el mecanismo completo y la práctica: el glosario resume, no sustituye a las clases.

## Cómo se lee una entrada

Todas las entradas siguen el mismo esquema:

| Sección | Qué responde |
| --- | --- |
| Definición | qué significa el término en el programa y, si hay varios sentidos, cuál usa cada clase |
| Por qué importa | qué decisión profesional cambia |
| Cómo funciona | el mecanismo y la causa, tomados de la explicación de la clase |
| Ejemplo | un caso concreto de las clases |
| Errores y confusiones comunes | qué se hace mal y con qué se confunde |
| Límites y cuándo no aplica | dónde deja de valer |
| Relación con otros conceptos | prerrequisitos, «ver también» y «se confunde con» |
| Dónde se enseña | las clases (y casos) que lo definen, desarrollan o usan |
| Sinónimos y traducción | variantes, siglas y forma en inglés |
| Fuentes | las fuentes de las clases que lo respaldan |

Una entrada es **desarrollada** cuando todas sus secciones principales están escritas a mano para el concepto; es **compuesta**
cuando reúne, con atribución a la clase, lo que el programa ya enseña sobre el término y declara cuándo la clase no dice nada específico.
El nivel **troncal** marca los conceptos que estructuran una parte; los de **apoyo** completan el vocabulario.

## Conteos

| Medida | Entradas |
| --- | --- |
| Conceptos con entrada | {n} |
| Troncales | {c['nivel']['troncal']} |
| De apoyo | {c['nivel']['apoyo']} |
| Desarrolladas | {developed} |
| Compuestas desde las clases | {n - developed} |
| Siglas | {c['tipo'].get('sigla', 0)} |
| Guías de rol | {c['tipo'].get('rol profesional', 0)} |

El detalle por tipo, parte y familia está en el [inventario](INVENTARIO.md).

## Índice alfabético

{letter_links}

## Índice por familias

Cada familia agrupa los conceptos por la etapa donde aparecen por primera vez y, dentro de ella, por parte.

{family_lines}

## Límites

El glosario no inventa definiciones: todo concepto se apoya en lo que las clases ya enseñan y en las fuentes de esas clases.
Cuando un término tiene varios sentidos, la entrada indica el que usa el programa. Un término que ninguna clase define no tiene
entrada; las entradas compuestas pueden ser más breves que la clase y no reemplazan la práctica ni la evidencia de las clases.
No se afirma revisión humana independiente.

[↑ Programa](../README.md) · [Inventario](INVENTARIO.md) · [Guía editorial](GUIDE.md)
"""
    return cross_references.resolve(text, "glosario")


GUIDE_TEXT = """# Guía editorial del glosario

[↑ Glosario](README.md) · [Inventario](INVENTARIO.md)

## Reglas

1. **No inventar.** Cada afirmación de una entrada se apoya en lo que una clase enseña o en una fuente verificada. Si un término es ambiguo, la entrada dice qué sentido usa el programa.
2. **Una entrada por concepto.** Variantes de singular y plural, siglas y expansión, y términos en español e inglés comparten entrada.
3. **Esquema único.** Las diez secciones de [la lectura de una entrada](README.md#cómo-se-lee-una-entrada), siempre en el mismo orden.
4. **Enlazar, no repetir.** La entrada resume y remite a las clases; no copia lecciones enteras.
5. **Referencias.** Escribe `SE-nnn` y `Parte NN` como texto: la publicación las enlaza.

## Dónde vive cada cosa

| Ruta | Qué contiene | ¿Se edita a mano? |
| --- | --- | --- |
| `glosario/curado/<slug>.md` | texto escrito a mano de un concepto (secciones `## Definición`, `## Por qué importa`, …) | sí |
| `glosario/entradas/<letra>/<slug>.md` | entrada publicada | no, la genera `scripts/build_glossary.py` |
| `glosario/README.md`, `INVENTARIO.md`, `indice/`, `familias/` | puntos de entrada e inventario | no |
| `glosario/casos.json` | dónde aparece cada concepto en los casos | no, `--refresh-cases` |
| `site/glosario/` | páginas del portal con búsqueda | no |

## Cómo desarrollar una entrada

1. Busca el `slug` del concepto en [`INVENTARIO.md`](INVENTARIO.md) o en el índice.
2. Crea `glosario/curado/<slug>.md` con las secciones que quieras sustituir (las demás siguen compuestas desde las clases).
   Una entrada **desarrollada** escribe al menos Definición, Por qué importa, Cómo funciona, Ejemplo, Errores y confusiones comunes
   y Límites y cuándo no aplica. Entrada troncal larga: entre 400 y 900 palabras; entrada de apoyo: entre 150 y 350.
3. Ejecuta `python scripts/build_glossary.py` y `python scripts/validate_glossary.py`.
4. Una figura propia solo si muestra un patrón, una relación o un mecanismo que el texto no da; usa `scripts/figure_kit.py`,
   sin repetir una tabla y con texto alternativo sin corchetes.

[↑ Glosario](README.md) · [Inventario](INVENTARIO.md)
"""


# --------------------------------------------------------------------------- README raíz
def fmt(number: int) -> str:
    return f"{number:,}".replace(",", ".") if number >= 10000 else str(number)


def summary() -> dict[str, int]:
    """Conteos baratos (sin componer las entradas) para el README raíz, STATUS y las pruebas."""
    inventory = data.inventory()
    tiers = Counter(data.tier_of(concept) for concept in inventory.values())
    slugs = {concept.slug for concept in inventory.values()}
    curated = gc.load_curated()
    developed = sum(1 for slug, sections in curated.items() if slug in slugs and all(name in sections for name in gc.DEVELOPED_SECTIONS))
    return {
        "total": len(inventory),
        "troncal": tiers["troncal"],
        "apoyo": tiers["apoyo"],
        "desarrolladas": developed,
        "letras": len({data.letter_of(concept.slug) for concept in inventory.values()}),
    }


def readme_section() -> str:
    c = summary()
    return f"""## 📖 Glosario: el vocabulario del programa

Además de las partes, los roles y los casos, el programa ofrece una superficie propia: un **glosario profundo** con
{fmt(c['total'])} conceptos ({c['troncal']} troncales y {fmt(c['apoyo'])} de apoyo). No son clases ni roles y no cambian el
número de clases: cada entrada define el término, explica por qué importa y cómo funciona, advierte de errores y límites, lo
relaciona con otros conceptos y enlaza las clases y los casos donde se enseña. Se consulta cuando una clase usa un término que no
dominas y se usa para volver a la clase que lo desarrolla.

- 🔎 [**Buscar un término en el portal**](https://vladimiracunadev-create.github.io/modern-software-engineering-program/glosario/index.html), con búsqueda por término y por sigla.
- 🔤 [**Índice alfabético y por familias**](glosario/README.md): cómo se lee una entrada, conteos y accesos a todas las entradas.
- 🧮 [**Inventario**](glosario/INVENTARIO.md): de dónde salen los conceptos, cómo se normalizaron y cómo se tipifican.
"""


# --------------------------------------------------------------------------- portal
LINK = re.compile(r'(!?)\[([^\]]*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')


def site_target(source_dir: str, target: str) -> str:
    path, _, anchor = target.partition("#")
    suffix = f"#{anchor}" if anchor else ""
    resolved = posixpath.normpath(posixpath.join(source_dir, path)) if path else ""
    class_match = re.fullmatch(r"classes/part-\d\d-[^/]+/(se-(\d{3})-[^/]+)/README\.md", resolved)
    if class_match:
        return f"../../classes/SE-{class_match.group(2)}.html{suffix}"
    part_match = re.fullmatch(r"classes/part-(\d\d)-[^/]+/README\.md", resolved)
    if part_match:
        return f"../../parts/{part_match.group(1)}.html{suffix}"
    entry_match = re.fullmatch(r"glosario/entradas/([^/]+)/([^/]+)\.md", resolved)
    if entry_match:
        return f"../{entry_match.group(1)}/{entry_match.group(2)}.html{suffix}"
    if resolved == "glosario/README.md":
        return f"../index.html{suffix}"
    if resolved == "README.md":
        return f"../../index.html{suffix}"
    case_match = re.fullmatch(r"casos/(exito|fallo)/([^/]+)\.md", resolved)
    if case_match:
        page = "index.html" if case_match.group(2) == "README" else case_match.group(2) + ".html"
        return f"../../casos/{case_match.group(1)}/{page}{suffix}"
    if resolved.startswith("glosario/") and resolved.endswith(".md"):
        return f"../index.html{suffix}"
    return GITHUB_BLOB + resolved + suffix


def entry_html_markdown(markdown: str, concept: data.Concept) -> str:
    source_dir = f"{gc.ENTRY_DIR}/{data.letter_of(concept.slug)}"
    lines = [line for line in markdown.splitlines() if not line.startswith("[↑ Glosario]")]

    def replace(match: re.Match[str]) -> str:
        bang, label, target, caption = match.groups()
        if bang or re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target):
            return match.group(0)
        return f"[{label}]({site_target(source_dir, target)}{caption})"

    return LINK.sub(replace, "\n".join(lines))


def page(title: str, description: str, eyebrow: str, nav: str, hero: str, body: str, toc: str, source_url: str, depth: int, extra_head: str = "", extra_end: str = "") -> str:
    css = "../" * depth + "assets/styles.css"
    return (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<meta name="description" content="{html.escape(description)}">'
        f"<title>{html.escape(title)}</title>"
        f'<link rel="stylesheet" href="{css}">{extra_head}</head><body>'
        '<a class="skip" href="#content">Saltar al contenido</a>'
        f'<main class="lesson" id="content">{nav}'
        f'<header class="lesson-hero"><p class="eyebrow">{html.escape(eyebrow)}</p><h1>{html.escape(title)}</h1><p>{html.escape(hero)}</p></header>'
        f'<div class="lesson-shell"><nav class="lesson-toc" aria-label="Contenido de la página"><strong>En esta página</strong><ol>{toc}</ol></nav>'
        f'<article class="lesson-content">{body}</article></div>'
        f'<p class="source-link"><a href="{source_url}">Ver el archivo fuente en GitHub</a></p>{nav}</main>'
        f"<footer>{PROGRAM_NAME} · Glosario</footer>{extra_end}</body></html>\n"
    )


SEARCH_SCRIPT = """<script>
(function () {
  var box = document.getElementById('glosario-buscar');
  var items = Array.prototype.slice.call(document.querySelectorAll('[data-term]'));
  var empty = document.getElementById('glosario-vacio');
  var count = document.getElementById('glosario-cuenta');
  function fold(s) { return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase(); }
  function run() {
    var q = fold(box.value.trim());
    var shown = 0;
    items.forEach(function (li) {
      var hit = !q || li.getAttribute('data-term').indexOf(q) !== -1;
      li.hidden = !hit;
      if (hit) { shown += 1; }
    });
    document.querySelectorAll('[data-letter-block]').forEach(function (block) {
      block.hidden = !block.querySelector('[data-term]:not([hidden])');
    });
    empty.hidden = shown !== 0;
    count.textContent = q ? shown + ' coincidencias' : items.length + ' conceptos';
  }
  box.addEventListener('input', run);
  run();
}());
</script>"""


def site_pages(items: list[gc.Entry]) -> dict[Path, str]:
    from build_phase3 import markdown_to_html

    result: dict[Path, str] = {}
    for index, entry in enumerate(items):
        concept = entry.concept
        previous = items[index - 1] if index else None
        following = items[index + 1] if index + 1 < len(items) else None
        markdown = entry_markdown(entry, previous, following)
        body_md = entry_html_markdown(markdown, concept)
        content, headings = markdown_to_html(body_md)
        content = re.sub(r"^<h1[^>]*>.*?</h1>", "", content, count=1, flags=re.S)
        toc = "".join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in headings if t != concept.name)
        letter = data.letter_of(concept.slug)
        prev_link = (f'<a href="../{data.letter_of(previous.concept.slug)}/{previous.concept.slug}.html">← {html.escape(previous.concept.name)}</a>' if previous else "<span>Inicio</span>")
        next_link = (f'<a href="../{data.letter_of(following.concept.slug)}/{following.concept.slug}.html">{html.escape(following.concept.name)} →</a>' if following else "<span>Fin</span>")
        nav = ('<nav class="class-nav" aria-label="Navegación del glosario">'
               f'{prev_link}<a href="../index.html">Glosario</a><a href="../../index.html">Programa</a>{next_link}</nav>')
        stage, stage_name = family_of(concept)
        source = GITHUB_BLOB + gc.entry_path(concept)
        html_page = page(
            f"{concept.name} · glosario",
            f"Glosario: {concept.name}. {short_definition(entry)}",
            f"Glosario · {data.kind_of(concept)} · {tier_label(concept)} · superficie propia, no son clases ni roles",
            nav, short_definition(entry), content, toc, source, 2,
        )
        path = ROOT / "site/glosario" / letter / f"{concept.slug}.html"
        result[path] = cross_references.resolve_html(html_page, posixpath.dirname(path.relative_to(ROOT).as_posix()))
    # índice con búsqueda
    by_letter: dict[str, list[gc.Entry]] = defaultdict(list)
    for entry in items:
        by_letter[data.letter_of(entry.concept.slug)].append(entry)
    blocks = []
    for letter in letters(items):
        rows = []
        for entry in by_letter[letter]:
            concept = entry.concept
            terms = data.fold(" ".join([concept.name, *concept.aliases]))
            rows.append(
                f'<li data-term="{html.escape(terms)}"><a href="{letter}/{concept.slug}.html">{html.escape(concept.name)}</a> '
                f'<small>{html.escape(data.kind_of(concept))} · {html.escape(tier_label(concept))}</small> — {html.escape(short_definition(entry))}</li>'
            )
        blocks.append(f'<section data-letter-block id="letra-{letter}"><h2>{letter.upper()}</h2><ul>{"".join(rows)}</ul></section>')
    letter_nav = " · ".join(f'<a href="#letra-{l}">{l.upper()}</a>' for l in letters(items))
    c = counts(items)
    search = (
        '<p><label for="glosario-buscar"><strong>Buscar un término</strong> (nombre, sigla o variante)</label><br>'
        '<input id="glosario-buscar" type="search" autocomplete="off" placeholder="Por ejemplo: idempotencia, SLO, saga" style="width:100%;max-width:32rem;padding:.5rem">'
        '</p><p id="glosario-cuenta" aria-live="polite"></p><p id="glosario-vacio" hidden>Ningún concepto coincide con la búsqueda.</p>'
    )
    intro = (
        f"<p>{len(items)} conceptos ({c['nivel']['troncal']} troncales y {c['nivel']['apoyo']} de apoyo). Cada entrada define el término, "
        "explica por qué importa y cómo funciona, advierte de errores y límites y enlaza las clases donde se enseña. "
        "No son clases ni roles: no cambian el número de clases.</p>"
        f"<p>Saltar a: {letter_nav}</p>"
    )
    body = intro + search + "".join(blocks)
    toc = "".join(f'<li><a href="#letra-{l}">{l.upper()}</a></li>' for l in letters(items))
    nav = ('<nav class="class-nav" aria-label="Navegación del glosario">'
           '<a href="../index.html">Programa</a><span>Glosario</span>'
           f'<a href="{GITHUB_BLOB}glosario/README.md">Guía y conteos</a></nav>')
    index_html = page(
        "Glosario del programa",
        f"Glosario con {len(items)} conceptos del programa, vinculados a las clases donde se enseñan.",
        "Glosario · superficie propia, no son clases ni roles", nav,
        "Busca un término y vuelve a las clases que lo enseñan.", body, toc, GITHUB_BLOB + "glosario/README.md", 1,
        extra_end=SEARCH_SCRIPT,
    )
    result[ROOT / "site/glosario/index.html"] = cross_references.resolve_html(index_html, "site/glosario")
    return result


# --------------------------------------------------------------------------- conjunto
def expected_files() -> dict[Path, str]:
    items = entries()
    files: dict[Path, str] = {}
    for index, entry in enumerate(items):
        previous = items[index - 1] if index else None
        following = items[index + 1] if index + 1 < len(items) else None
        files[ROOT / gc.entry_path(entry.concept)] = entry_markdown(entry, previous, following)
    files[ROOT / "glosario/README.md"] = readme_markdown(items)
    files[ROOT / "glosario/GUIDE.md"] = cross_references.resolve(GUIDE_TEXT, "glosario")
    files[ROOT / "glosario/INVENTARIO.md"] = inventory_markdown(items)
    for rel, text in {**letter_pages(items), **family_pages(items)}.items():
        files[ROOT / rel] = text
    files.update(site_pages(items))
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--refresh-cases", action="store_true", help="recompute glosario/casos.json from the case files")
    args = parser.parse_args()
    if args.refresh_cases:
        CASES_JSON.parent.mkdir(parents=True, exist_ok=True)
        CASES_JSON.write_text(json.dumps(refresh_cases(), ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    files = expected_files()
    stale: list[str] = []
    for path, content in files.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if not args.check:  # elimina entradas huérfanas de conceptos que ya no existen
        keep = {p for p in files}
        for folder in ("glosario/entradas", "glosario/indice", "glosario/familias", "site/glosario"):
            for old in (ROOT / folder).rglob("*"):
                if old.is_file() and old not in keep:
                    old.unlink()
    else:
        for folder in ("glosario/entradas", "site/glosario"):
            for old in (ROOT / folder).rglob("*"):
                if old.is_file() and old not in files:
                    stale.append("orphan:" + old.relative_to(ROOT).as_posix())
    if stale:
        print("GLOSSARY_STALE: " + ", ".join(stale[:30]), file=sys.stderr)
        return 1
    print(("GLOSSARY_CHECK_OK" if args.check else "GLOSSARY_BUILD_OK") + f": {len(files)} files, {len(data.inventory())} concepts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
