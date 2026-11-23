"""Inventario del glosario: extrae los conceptos de las clases, los normaliza y los agrupa.

El glosario es una superficie propia (``glosario/``), no son clases ni roles y no cambia los
contadores del programa. Este módulo solo *lee* ``content/``, ``roles/`` y ``casos/`` y
produce, de forma determinista, el inventario de conceptos y todo lo que las entradas necesitan
(definiciones, explicaciones, errores, fuentes, clases donde se enseña).

Fuentes del inventario, por orden de autoridad:

* ``definition``: viñetas ``- **término:** definición`` de «Definiciones de trabajo» de cada clase;
* ``glossary``: términos en negrita del apartado «Glosario» de la clase;
* ``topic``: filas de la tabla «Temas y por qué importan» que son términos (no preguntas ni frases);
* ``role``: las guías de ``roles/``.

Dos redacciones son el mismo concepto cuando comparten alguna clave normalizada (minúsculas, sin
tildes, singular, sin paréntesis) o cuando una sigla entre paréntesis coincide con otro término.
"""
from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------- normalización
STOP_LEAD = {
    "que", "como", "cuando", "por", "donde", "quien", "cual", "cuales", "cuanto", "cuantos", "para",
    "limite", "limites", "ejemplo", "ejemplos", "caso", "casos", "error", "errores", "decision",
    "decisiones", "el", "la", "los", "las", "un", "una", "se", "si", "no", "hay", "ante", "sin",
}
# Frases sueltas que son titulares de tema, no términos.
NOT_TERMS = {"", "tema", "concepto", "area", "elemento", "dimension", "interna", "perspectiva", "momento"}


def fold(text: str) -> str:
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(ch for ch in text if unicodedata.category(ch) != "Mn")


def stem(word: str) -> str:
    if len(word) <= 3:
        return word
    if word.endswith("ces"):
        return word[:-3] + "z"
    if word.endswith(("ciones", "siones")):
        return word[:-2]
    if word.endswith(("ores", "ades", "udes")):
        return word[:-2]
    if word.endswith(("ss", "is", "us")) or not word.endswith("s"):
        return word
    return word[:-1]


@lru_cache(maxsize=None)
def key_of(text: str) -> str:
    """Clave de comparación: minúsculas, sin tildes ni puntuación, palabras en singular."""
    text = re.sub(r"`", "", fold(text))
    words = re.sub(r"[^a-z0-9ñ+#]+", " ", text).split()
    return " ".join(stem(word) for word in words)


def slugify(text: str) -> str:
    text = fold(text).replace("+", " mas ").replace("#", " sharp ")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:70].strip("-") or "concepto"


def variants_of(raw: str) -> tuple[str, list[str]]:
    """(término base, alias) de una redacción: separa paréntesis y alternativas con barra."""
    raw = raw.replace("`", "").strip(" :.")
    aliases: list[str] = []
    match = re.match(r"^(?P<base>.+?)\s*\((?P<alias>[^()]+)\)\s*$", raw)
    base = raw
    if match:
        base, alias = match.group("base").strip(), match.group("alias").strip()
        if len(alias.split()) <= 4 and not alias.lower().startswith(("de ", "del ", "con ", "para ", "en ")):
            aliases.append(alias)
        else:
            base = raw
    return base, aliases


# --------------------------------------------------------------------------- lectura de clases
@dataclass
class Class:
    id: str
    title: str
    part: str
    path: str  # README publicado
    stage: str = ""
    sections: dict[str, str] = field(default_factory=dict)
    h3: dict[str, str] = field(default_factory=dict)  # título (sin número) -> texto
    definitions: list[tuple[str, str]] = field(default_factory=list)
    glossary_terms: list[tuple[str, str]] = field(default_factory=list)
    topics: list[tuple[str, str]] = field(default_factory=list)
    errors: list[tuple[str, str, str]] = field(default_factory=list)
    sources: list[tuple[str, str, str]] = field(default_factory=list)  # (título, url, nota)
    prerequisites: list[str] = field(default_factory=list)
    closing_definitions: str = ""
    body: str = ""


@lru_cache(maxsize=1)
def program() -> dict:
    return json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))


def _split_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current, buffer, fence = None, [], False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if not fence and line.startswith("## "):
            if current is not None:
                sections[current] = "\n".join(buffer).strip()
            current, buffer = line[3:].strip(), []
        elif current is not None:
            buffer.append(line)
    if current is not None:
        sections[current] = "\n".join(buffer).strip()
    return sections


def _split_h3(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    current, buffer, fence = None, [], False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if not fence and line.startswith("### "):
            if current is not None:
                result[current] = "\n".join(buffer).strip()
            current, buffer = re.sub(r"^\d+\.\s*", "", line[4:].strip()), []
        elif current is not None:
            buffer.append(line)
    if current is not None:
        result[current] = "\n".join(buffer).strip()
    return result


LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")


def plain(text: str) -> str:
    """Texto sin enlaces ni imágenes, listo para citar."""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = LINK.sub(r"\1", text)
    return re.sub(r"[ \t]+", " ", text).strip()


def paragraphs(text: str) -> list[str]:
    return list(_paragraphs(text))


@lru_cache(maxsize=None)
def _paragraphs(text: str) -> tuple[str, ...]:
    """Párrafos de prosa: sin código, tablas, imágenes, citas, listas ni HTML."""
    result, buffer, fence = [], [], False

    def flush() -> None:
        if buffer:
            result.append(plain(" ".join(buffer)))
            buffer.clear()

    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            flush()
            fence = not fence
            continue
        stripped = line.strip()
        if fence or not stripped:
            flush()
            continue
        if stripped.startswith(("|", "![", ">", "<", "- ", "* ", "#", "$$")) or re.match(r"^\d+\.\s", stripped):
            flush()
            continue
        buffer.append(stripped)
    flush()
    return tuple(p for p in result if len(p.split()) >= 6)


def sentences(paragraph: str) -> list[str]:
    parts = re.split(r"(?<=[.!?:;])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«(`*])", paragraph)
    return [p.strip() for p in parts if p.strip()]


def _table_rows(text: str) -> list[list[str]]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[-\s|:]+\|?$", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append(cells)
    return rows[1:] if rows else rows


def _read_class(path: Path, meta: dict, stage: str, part: str) -> Class:
    text = path.read_text(encoding="utf-8")
    cls = Class(id=meta["id"], title=meta["title"], part=part, path=f"{meta['path']}/README.md", stage=stage)
    cls.body = text
    cls.sections = _split_sections(text)
    cls.h3 = _split_h3(cls.sections.get("Conceptos y decisiones", ""))
    block = cls.sections.get("Definiciones de trabajo", "")
    for term, definition in re.findall(r"^- \*\*([^*]+)\*\*\s*(.*)$", block, re.M):
        cls.definitions.append((term.strip(" :"), plain(definition.strip())))
    tail = [p for p in block.split("\n\n") if p.strip() and not p.lstrip().startswith("- ")]
    cls.closing_definitions = plain(" ".join(tail))
    glossary = cls.sections.get("Glosario", "").split("\n---")[0]
    bullets = re.findall(r"^- \*\*([^*]+)\*\*\s*(.*)$", glossary, re.M)
    if bullets:  # glosario en lista: solo añade lo que no esté ya en «Definiciones de trabajo»
        known = {key_of(term) for term, _ in cls.definitions}
        for term, definition in bullets:
            if key_of(term.strip(" :")) not in known:
                cls.definitions.append((term.strip(" :"), plain(definition.strip())))
    else:
        for term in re.findall(r"\*\*([^*]+)\*\*", glossary):
            sentence = next((s for s in sentences(plain(glossary)) if term in s), plain(glossary))
            cls.glossary_terms.append((term.strip(" :"), sentence.replace("**", "")))
    for row in _table_rows(cls.sections.get("Temas y por qué importan", "")):
        if len(row) >= 2:
            cls.topics.append((plain(row[0]).replace("**", ""), plain(row[1])))
    for row in _table_rows(cls.sections.get("Errores comunes y cómo corregirlos", "")):
        if len(row) >= 3:
            cls.errors.append((plain(row[0]), plain(row[1]), plain(row[2])))
    for line in cls.sections.get("Fuentes", "").splitlines():
        found = re.match(r"^- \[([^\]]+)\]\(([^)]+)\)\s*(?:[—-]\s*(.*))?$", line.strip())
        if found:
            cls.sources.append((found.group(1), found.group(2), (found.group(3) or "").strip()))
    cls.prerequisites = re.findall(r"SE-\d{3}", cls.sections.get("Prerrequisitos", ""))
    return cls


@lru_cache(maxsize=1)
def classes() -> dict[str, Class]:
    result: dict[str, Class] = {}
    for part in program()["parts"]:
        for lesson in part["lessons"]:
            source = ROOT / "content" / f"part-{part['id']}" / f"{lesson['id']}.md"
            if source.is_file():
                result[lesson["id"]] = _read_class(source, lesson, part["stage"], part["id"])
    return result


# --------------------------------------------------------------------------- inventario
@dataclass
class Concept:
    key: str
    name: str
    slug: str = ""
    kinds: set[str] = field(default_factory=set)
    forms: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    keys: set[str] = field(default_factory=set)
    defs: list[tuple[str, str, str]] = field(default_factory=list)  # (clase, término tal cual, definición)
    glossary: list[tuple[str, str]] = field(default_factory=list)
    topic_rows: list[tuple[str, str, str]] = field(default_factory=list)  # (clase, tema, por qué)
    h3_classes: list[str] = field(default_factory=list)
    classes: list[str] = field(default_factory=list)  # clases que lo definen o titulan, por orden
    role: str = ""  # slug de la guía de rol


def term_like(topic: str) -> bool:
    key = key_of(topic)
    words = key.split()
    if not 1 <= len(words) <= 4 or key in NOT_TERMS:
        return False
    if fold(topic.split()[0]).strip("¿?:,") in STOP_LEAD or "?" in topic:
        return False
    if "," in topic or " y " in topic.lower() or " o " in topic.lower():
        return False
    return not re.search(r"\b(?:de|del|en|con|para|por)$", fold(topic))


def _content_words(text: str) -> set[str]:
    return {word for word in key_of(text).split() if len(word) > 3}


def similar(a: str, b: str) -> bool:
    """Dos definiciones se parecen si comparten al menos el 30 % de las palabras de contenido de la más corta."""
    first, second = _content_words(a), _content_words(b)
    if not first or not second:
        return False
    return len(first & second) / min(len(first), len(second)) >= 0.3


class _Groups:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def find(self, key: str) -> str:
        self.parent.setdefault(key, key)
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

    def union(self, a: str, b: str) -> None:
        self.parent[self.find(b)] = self.find(a)


@lru_cache(maxsize=1)
def inventory() -> dict[str, Concept]:
    """Concepto por clave canónica, en orden estable (alfabético por nombre mostrado)."""
    groups = _Groups()
    occurrences: list[tuple[str, str, str, str, str]] = []  # (kind, raw, clase, texto, extra)
    for cls in classes().values():
        for term, definition in cls.definitions:
            occurrences.append(("definition", term, cls.id, definition, ""))
        for term, sentence in cls.glossary_terms:
            occurrences.append(("glossary", term, cls.id, sentence, ""))
        for topic, why in cls.topics:
            if term_like(topic):
                occurrences.append(("topic", topic, cls.id, why, ""))
    # 1) grupos por claves compartidas: término base y siglas; un alias que es una palabra (p. ej. un
    #    anglicismo) solo une dos términos si sus definiciones se parecen, para no fundir sentidos distintos
    texts: dict[str, list[str]] = defaultdict(list)
    for kind, raw, class_id, text, _ in occurrences:
        base, aliases = variants_of(raw)
        base_key = key_of(base)
        if not base_key or base_key in NOT_TERMS:
            continue
        groups.find(base_key)
        for alias in aliases:
            alias_key = key_of(alias)
            if alias_key and alias_key not in NOT_TERMS and (alias.isupper() or ACRONYM.match(alias)):
                groups.union(base_key, alias_key)
    for kind, raw, class_id, text, _ in occurrences:
        base, _aliases = variants_of(raw)
        texts[groups.find(key_of(base))].append(text)
    for kind, raw, class_id, text, _ in occurrences:
        base, aliases = variants_of(raw)
        base_key = key_of(base)
        for alias in aliases:
            alias_key = key_of(alias)
            if not alias_key or alias_key in NOT_TERMS or alias.isupper() or ACRONYM.match(alias):
                continue
            other = groups.find(alias_key)
            if other == groups.find(base_key):
                continue
            known = texts.get(other, [])
            if not known or any(similar(text, other_text) for other_text in known):
                groups.union(base_key, alias_key)
    # 2) los temas solo cuentan si coinciden con un término definido o se repiten en otra clase
    defined = {groups.find(key_of(variants_of(raw)[0])) for kind, raw, *_ in occurrences if kind in {"definition", "glossary"}}
    topic_count: dict[str, set[str]] = defaultdict(set)
    for kind, raw, class_id, *_ in occurrences:
        if kind == "topic":
            topic_count[groups.find(key_of(variants_of(raw)[0]))].add(class_id)
    concepts: dict[str, Concept] = {}
    for kind, raw, class_id, text, _ in occurrences:
        base, aliases = variants_of(raw)
        canonical = groups.find(key_of(base))
        if kind == "topic" and canonical not in defined and len(topic_count[canonical]) < 2:
            continue
        concept = concepts.setdefault(canonical, Concept(key=canonical, name=""))
        concept.kinds.add(kind)
        concept.forms.append(base)
        for alias in aliases:
            concept.aliases.append(alias)
            concept.forms.append(alias)
        concept.keys.add(key_of(base))
        concept.keys.update(key_of(alias) for alias in aliases if groups.find(key_of(alias)) == canonical)
        if kind == "definition":
            concept.defs.append((class_id, raw, text))
        elif kind == "glossary":
            concept.glossary.append((class_id, text))
        else:
            concept.topic_rows.append((class_id, raw, text))
        if class_id not in concept.classes:
            concept.classes.append(class_id)
    # nombre mostrado: la forma base más frecuente, con la primera letra en mayúscula
    for concept in concepts.values():
        counts: dict[str, int] = defaultdict(int)
        for form in concept.forms:
            counts[form] += 1
        bases = [form for form in concept.forms if key_of(form) == concept.key] or concept.forms
        best = max(dict.fromkeys(bases), key=lambda form: (sum(1 for f in bases if f == form), -len(form)))
        concept.name = best[0].upper() + best[1:] if best[0].islower() else best
        concept.aliases = sorted({a for a in concept.aliases if key_of(a) != concept.key})
        spelled = sorted({f for f in concept.forms if f != best and key_of(f) not in {key_of(a) for a in concept.aliases}})
        concept.aliases = list(dict.fromkeys(concept.aliases + [f for f in spelled if fold(f) != fold(best)]))
        concept.classes.sort()
    # h3 que titulan el concepto
    for cls in classes().values():
        for title in cls.h3:
            canonical = next((c for c in (key_of(title),) if c in concepts), None)
            if canonical:
                concepts[canonical].h3_classes.append(cls.id)
                if cls.id not in concepts[canonical].classes:
                    concepts[canonical].classes.append(cls.id)
    # roles
    for path in sorted((ROOT / "roles").glob("*.md")):
        if path.name == "README.md":
            continue
        role_text = path.read_text(encoding="utf-8")
        title = re.sub(r"^#\s*\S+\s+", "", role_text.splitlines()[0]).strip()
        role_classes = []
        for number in re.findall(r"classes/part-\d\d-[^/]+/se-(\d{3})-", role_text):
            if f"SE-{number}" in classes() and f"SE-{number}" not in role_classes:
                role_classes.append(f"SE-{number}")
        canonical = key_of(title)
        concept = concepts.setdefault(canonical, Concept(key=canonical, name=title))
        concept.kinds.add("role")
        concept.role = path.stem
        concept.classes = sorted(role_classes[:12])
        concept.keys.add(canonical)
    # slugs únicos y estables
    used: dict[str, str] = {}
    for concept in sorted(concepts.values(), key=lambda c: (fold(c.name), c.key)):
        base = slugify(concept.name)
        slug, index = base, 2
        while slug in used and used[slug] != concept.key:
            slug, index = f"{base}-{index}", index + 1
        used[slug] = concept.key
        concept.slug = slug
    return dict(sorted(concepts.items(), key=lambda item: (fold(item[1].name), item[0])))


def letter_of(slug: str) -> str:
    return slug[0] if slug[0].isalpha() else "0-9"


# --------------------------------------------------------------------------- tipificación
ACRONYM = re.compile(r"^[A-ZÁÉÍÓÚ0-9][A-ZÁÉÍÓÚ0-9/\-+.]{1,9}$")
STANDARD = re.compile(
    r"\b(ISO|IEC|IEEE|RFC|NIST|OWASP|WCAG|ASVS|SLSA|SWEBOK|GDPR|RGPD|DO-\d+|ARP\d+|SOC ?2|PCI|HIPAA|STRIDE|MITRE|CVE|CWE|CVSS|OAuth|OIDC|OpenAPI|SemVer|SPDX|CycloneDX|SBOM)\b",
    re.I,
)
PRACTICE = re.compile(
    r"^(prueba|pruebas|revisi[oó]n|refactorizaci[oó]n|an[aá]lisis|an[aá]lisis|desarrollo|despliegue|estrategia|patr[oó]n|"
    r"lanzamiento|migraci[oó]n|dise[nñ]o|modelado|medici[oó]n|gesti[oó]n|automatizaci[oó]n|integraci[oó]n|"
    r"experimento|ejercicio|programaci[oó]n|inyecci[oó]n|monitoreo|planificaci[oó]n|reproducci[oó]n|"
    r"depuraci[oó]n|entrega|auditor[ií]a|simulaci[oó]n|verificaci[oó]n|validaci[oó]n)\b",
    re.I,
)
METRIC = re.compile(
    r"\b(tasa|latencia|rendimiento|throughput|cobertura|presupuesto de error|ratio|[ií]ndice|puntuaci[oó]n|"
    r"m[eé]trica|percentil|p99|p95|mttr|mtbf|mttd|slo|sli|sla|apdex|utilizaci[oó]n|saturaci[oó]n|frecuencia de)\b",
    re.I,
)


def kind_of(concept: Concept) -> str:
    """Tipo de entrada. Reglas léxicas declaradas en ``glosario/README.md`` (no son juicio editorial)."""
    if "role" in concept.kinds:
        return "rol profesional"
    name = concept.name
    if ACRONYM.match(name) or any(ACRONYM.match(alias) for alias in concept.aliases) and len(name.split()) <= 2 and name.isupper():
        return "sigla"
    if STANDARD.search(name):
        return "norma o marco"
    if METRIC.search(name):
        return "métrica"
    if PRACTICE.match(fold(name)):
        return "práctica o técnica"
    return "concepto"


def tier_of(concept: Concept) -> str:
    """Troncal: estructura una parte (varias clases lo definen, o es tema y sección a la vez)."""
    if "role" in concept.kinds:
        return "troncal"
    definers = {class_id for class_id, *_ in concept.defs}
    topics = {class_id for class_id, *_ in concept.topic_rows}
    sections = set(concept.h3_classes)
    if len(definers | topics | sections) >= 3:
        return "troncal"
    if definers & topics & sections:
        return "troncal"
    if len(definers) >= 2 and (topics or sections):
        return "troncal"
    return "apoyo"


# --------------------------------------------------------------------------- menciones
MAX_WORDS = 6


def _prose_only(text: str) -> str:
    out, fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
            continue
        if not fence and not line.startswith(("[←", "[↑", "|")):
            out.append(line)
    return "\n".join(out)


@lru_cache(maxsize=1)
def mentions() -> dict[str, dict[str, int]]:
    """Menciones del texto de las clases por concepto: {clave: {clase: n}} (sin siglas de 3 letras o menos)."""
    index: dict[int, dict[str, str]] = defaultdict(dict)
    for concept in inventory().values():
        for key in concept.keys:
            words = key.split()
            if 1 <= len(words) <= MAX_WORDS and len(key.replace(" ", "")) > 3:
                index[len(words)][key] = concept.key
    result: dict[str, dict[str, int]] = defaultdict(dict)
    for cls in classes().values():
        words = key_of(_prose_only(plain(cls.body))).split()
        counts: dict[str, int] = defaultdict(int)
        for size, table in index.items():
            for start in range(len(words) - size + 1):
                found = table.get(" ".join(words[start:start + size]))
                if found:
                    counts[found] += 1
        for key, number in counts.items():
            result[key][cls.id] = number
    return dict(result)
