"""Composición de las entradas del glosario a partir de lo que las clases ya enseñan.

Cada entrada tiene un esquema único (``SECTIONS``). Las secciones salen de dos capas:

* **curada** (``glosario/curado/<slug>.md``): texto escrito a mano para un concepto; sustituye por
  completo a la sección homónima;
* **compuesta**: texto que se toma, con atribución a la clase, de lo que ya enseña el programa
  (definiciones de trabajo, explicaciones de «Conceptos y decisiones», ejemplos, errores, límites,
  fuentes). Nunca se inventa una afirmación: si la clase no dice nada específico del término, la
  sección lo declara y remite al contexto de la clase.
"""
from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import cross_references
import glossary_data as data
from glossary_data import ROOT, Class, Concept, key_of, paragraphs, plain, sentences

CURATED_DIR = ROOT / "glosario" / "curado"
ENTRY_DIR = "glosario/entradas"

SECTIONS = [
    "Definición",
    "Por qué importa",
    "Cómo funciona",
    "Ejemplo",
    "Errores y confusiones comunes",
    "Límites y cuándo no aplica",
    "Relación con otros conceptos",
    "Dónde se enseña",
    "Sinónimos y traducción",
    "Fuentes",
]
CONFUSION_MARKERS = ("se confunde con", "se confunden", "no es lo mismo", "no es sinónimo", "no son sinónimos", "no equivale", "no es equivalente", "no es un sinónimo")
LIMIT_MARKERS = ("no ", "solo ", "sólo ", "depende", "límite", "salvo", "excepto", "deja de", "sin ")
MAX_CLASSES_LISTED = 30
DEVELOPED_SECTIONS = ("Definición", "Por qué importa", "Cómo funciona", "Ejemplo", "Errores y confusiones comunes", "Límites y cuándo no aplica")


# --------------------------------------------------------------------------- utilidades
@lru_cache(maxsize=None)
def padded(text: str) -> str:
    return f" {key_of(text)} "


def has_key(text: str, keys: set[str]) -> bool:
    haystack = padded(text)
    return any(f" {key} " in haystack for key in keys if key)


def lower_first(text: str) -> str:
    """Minúscula inicial salvo en siglas, nombres con mayúsculas internas o números."""
    word = text.split(" ", 1)[0] if text else ""
    if not word or any(ch.isupper() for ch in word[1:]) or word[0].isdigit() or word.isupper():
        return text
    return text[0].lower() + text[1:]


def finish(text: str) -> str:
    text = text.strip()
    return text if text.endswith((".", "?", "!", ")", "»")) else text.rstrip(";:,") + "."


def clip(paragraph: str, words: int = 120) -> str:
    """Recorta en una frontera de frase sin superar ``words`` palabras (si cabe, no recorta)."""
    if len(paragraph.split()) <= words:
        return paragraph
    out: list[str] = []
    count = 0
    for sentence in sentences(paragraph):
        size = len(sentence.split())
        if out and count + size > words:
            break
        out.append(sentence)
        count += size
    text = " ".join(out)
    return text if text.endswith((".", "?", "!", ":", ";")) else text.rstrip(",;:") + "."


def sentence_case(text: str) -> str:
    text = text.strip()
    if not text:
        return text
    text = text[0].upper() + text[1:]
    return text if text.endswith((".", "?", "!")) else text.rstrip(";:,") + "."


def class_link(class_id: str, base_dir: str) -> str:
    ref = cross_references.load_index().lessons[class_id]
    return f"[{class_id} — {ref.title}]({cross_references.relative_link(base_dir, ref.path)})"


def short_class_link(class_id: str, base_dir: str) -> str:
    ref = cross_references.load_index().lessons[class_id]
    return f"[{class_id}]({cross_references.relative_link(base_dir, ref.path)})"


def part_of(class_id: str) -> tuple[str, str]:
    cls = data.classes()[class_id]
    title = next(part["title"] for part in data.program()["parts"] if part["id"] == cls.part)
    return cls.part, title


def entry_path(concept: Concept) -> str:
    return f"{ENTRY_DIR}/{data.letter_of(concept.slug)}/{concept.slug}.md"


def entry_link(concept: Concept, base_dir: str, label: str | None = None) -> str:
    return f"[{label or concept.name}]({cross_references.relative_link(base_dir, entry_path(concept))})"


# --------------------------------------------------------------------------- índices auxiliares
@lru_cache(maxsize=1)
def by_class() -> dict[str, list[Concept]]:
    result: dict[str, list[Concept]] = defaultdict(list)
    for concept in data.inventory().values():
        for class_id in concept.classes:
            result[class_id].append(concept)
    return result


@lru_cache(maxsize=1)
def key_lookup() -> dict[str, Concept]:
    result: dict[str, Concept] = {}
    for concept in data.inventory().values():
        for key in concept.keys:
            if len(key.replace(" ", "")) > 3:
                result.setdefault(key, concept)
    return result


def concepts_in(text: str, exclude: Concept) -> list[Concept]:
    words = key_of(text).split()
    found: dict[str, Concept] = {}
    table = key_lookup()
    for size in range(1, data.MAX_WORDS + 1):
        for start in range(len(words) - size + 1):
            concept = table.get(" ".join(words[start:start + size]))
            if concept and concept.key != exclude.key:
                found.setdefault(concept.key, concept)
    return sorted(found.values(), key=lambda c: (-len(c.key.split()), c.key))


def strength(concept: Concept, class_id: str) -> float:
    score = 0.0
    cls = data.classes().get(class_id)
    if cls and any(key_of(title) == concept.key for title in cls.h3):
        score += 4
    if any(cid == class_id for cid, *_ in concept.topic_rows):
        score += 3
    if any(cid == class_id for cid, *_ in concept.defs):
        score += 1
    return score + min(data.mentions().get(concept.key, {}).get(class_id, 0) / 10, 2)


@lru_cache(maxsize=None)
def _ranked(key: str) -> tuple[str, ...]:
    concept = data.inventory()[key]
    return tuple(sorted(concept.classes, key=lambda class_id: (-strength(concept, class_id), class_id)))


def ranked_ids(concept: Concept) -> list[str]:
    return list(_ranked(concept.key))


def classes_text(concept: Concept) -> list[Class]:
    return [data.classes()[class_id] for class_id in ranked_ids(concept) if class_id in data.classes()]


# --------------------------------------------------------------------------- curado
def load_curated() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    if not CURATED_DIR.is_dir():
        return result
    for path in sorted(CURATED_DIR.glob("*.md")):
        text = re.sub(r"`(SE-\d{3})`", r"\1", path.read_text(encoding="utf-8"))
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
        result[path.stem] = sections
    return result


# --------------------------------------------------------------------------- secciones compuestas
def _definitions(concept: Concept, base: str) -> str:
    distinct: dict[str, list[str]] = {}
    rank = {class_id: index for index, class_id in enumerate(ranked_ids(concept))}
    for class_id, _, text in sorted(concept.defs, key=lambda item: (rank.get(item[0], 99), item[0])):
        distinct.setdefault(sentence_case(text), []).append(class_id)
    if distinct:
        items = list(distinct.items())
        lead, classes = items[0]
        out = [f"{lead}", "", f"Definición de trabajo de {class_link(classes[0], base)}."]
        if len(items) > 1:
            out += ["", "El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:", ""]
            for text, ids in items[1:5]:
                out.append(f"- En {class_link(ids[0], base)}: {text}")
        return "\n".join(out)
    for class_id, text in concept.glossary[:1]:
        return f"{sentence_case(text)}\n\nTomado del glosario de {class_link(class_id, base)}."
    for cls in classes_text(concept):
        for title, body in cls.h3.items():
            if key_of(title) == concept.key and paragraphs(body):
                return f"{clip(paragraphs(body)[0], 90)}\n\nExplicación de la sección «{title}» de {class_link(cls.id, base)}."
    for class_id, topic, why in concept.topic_rows[:1]:
        return f"{sentence_case(why)}\n\nEs uno de los temas de {class_link(class_id, base)}, donde se enseña como «{topic}»."
    return "Concepto del programa sin definición de trabajo propia; consulta las clases enlazadas en «Dónde se enseña»."


def _why(concept: Concept, base: str) -> str:
    out: list[str] = []
    seen: set[str] = set()
    rank_t = {class_id: index for index, class_id in enumerate(ranked_ids(concept))}
    for class_id, topic, why in sorted(concept.topic_rows, key=lambda item: (rank_t.get(item[0], 99), item[0]))[:3]:
        if why not in seen:
            seen.add(why)
            out.append(f"En {class_link(class_id, base)}, el tema «{topic}» importa porque {lower_first(why)}")
    if out:
        return "\n\n".join(out)
    for cls in classes_text(concept)[:1]:
        rows = [(topic, why) for topic, why in cls.topics if has_key(topic, concept.keys) or has_key(why, concept.keys)]
        if rows:
            topic, why = rows[0]
            return f"En {class_link(cls.id, base)}, el tema «{topic}» importa porque {lower_first(why)}"
        point = cls.sections.get("Punto profesional y fundamento pedagógico", "")
        paras = paragraphs(point)
        if paras:
            first = sentences(paras[0].replace("**Punto profesional.**", "").strip())
            if first:
                return (f"La clase donde se define, {class_link(cls.id, base)}, existe con este propósito: "
                        f"{first[0][0].lower() + first[0][1:]}")
    return "Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña»."


def _how(concept: Concept, base: str) -> str:
    out: list[str] = []
    for cls in classes_text(concept):
        for title, body in cls.h3.items():
            if key_of(title) == concept.key or (len(key_of(title).split()) >= 2 and key_of(title) in concept.keys):
                paras = paragraphs(body)
                if paras:
                    out.append(f"Según {class_link(cls.id, base)}, en la sección «{title}»:\n\n" + "\n\n".join(clip(p, 130) for p in paras[:3]))
        if len(out) >= 2:
            break
    if out:
        return "\n\n".join(out)
    picked: list[str] = []
    for cls in classes_text(concept):
        scope = [cls.sections.get("Conceptos y decisiones", "")] + [
            text for name, text in cls.sections.items() if name in {"Preguntas frecuentes", "Fallo controlado y diagnóstico", "Ejemplo profesional", "Transferencia"}
        ]
        for block in scope:
            for paragraph in paragraphs(block):
                if has_key(paragraph, concept.keys):
                    picked.append(f"Según {class_link(cls.id, base)}:\n\n{clip(paragraph, 130)}")
                    break
            if len(picked) >= 2:
                break
        if len(picked) >= 2:
            break
    if picked:
        return "\n\n".join(picked)
    cls = next(iter(classes_text(concept)), None)
    if cls:
        closing = cls.closing_definitions
        return (f"{class_link(cls.id, base)} usa este término dentro de otro tema, sin una sección propia. "
                f"El contexto en que aparece: {clip(closing, 60) if closing else 'consulta la clase para el mecanismo completo.'}")
    return "El mecanismo se desarrolla en las clases enlazadas."


def _example(concept: Concept, base: str) -> str:
    for cls in classes_text(concept):
        for name in ("Ejemplo mínimo", "Ejemplo profesional", "Caso conductor", "Demostración guiada", "Preguntas frecuentes", "Práctica guiada"):
            block = cls.sections.get(name, "")
            for paragraph in paragraphs(block):
                if has_key(paragraph, concept.keys):
                    return f"Ejemplo de {class_link(cls.id, base)} (sección «{name}»):\n\n{clip(paragraph, 110)}"
    for cls in classes_text(concept):  # un resultado medido en la sección que titula el concepto
        for title, body in cls.h3.items():
            if has_key(title, concept.keys):
                for paragraph in paragraphs(body):
                    if re.search(r"\d", paragraph) and len(paragraph.split()) >= 15:
                        return f"Caso medido en la sección «{title}» de {class_link(cls.id, base)}:\n\n{clip(paragraph, 100)}"
    for cls in classes_text(concept):
        for name in ("Ejemplo profesional", "Ejemplo mínimo"):
            paras = [p for p in paragraphs(cls.sections.get(name, "")) if not p.startswith("Antes de ejecutar")]
            if paras:
                return (f"Contexto concreto en el que aparece el término, de la sección «{name}» de "
                        f"{class_link(cls.id, base)}:\n\n{clip(paras[0], 90)}")
    return "Los ejemplos están en las clases enlazadas en «Dónde se enseña»."


def _errors(concept: Concept, base: str) -> str:
    rows: list[tuple[str, str, str, str]] = []
    for cls in classes_text(concept):
        for symptom, cause, fix in cls.errors:
            if has_key(" ".join((symptom, cause, fix)), concept.keys):
                rows.append((cls.id, symptom, cause, fix))
    if rows:
        out = ["Errores que las clases asocian con este término (síntoma → causa → corrección):", ""]
        for class_id, symptom, cause, fix in rows[:3]:
            out.append(f"- **{symptom}** — causa: {lower_first(cause.rstrip('.'))}. Corrección: {lower_first(fix.rstrip('.'))}. ({short_class_link(class_id, base)})")
        return "\n".join(out)
    cls = next(iter(classes_text(concept)), None)
    if cls and cls.errors:
        out = [f"Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ({class_link(cls.id, base)}) son:", ""]
        for symptom, cause, fix in cls.errors[:2]:
            out.append(f"- **{symptom}** — causa: {lower_first(cause.rstrip('.'))}. Corrección: {lower_first(fix.rstrip('.'))}.")
        confusions = [s for c in classes_text(concept) for s in _confusions(c, concept, base)]
        if confusions:
            out += ["", confusions[0]]
        return "\n".join(out)
    return "Las clases no registran errores específicos de este término."


def _confusions(cls: Class, concept: Concept, base: str) -> list[str]:
    found: list[str] = []
    for paragraph in paragraphs(cls.body):
        for sentence in sentences(paragraph):
            low = sentence.lower()
            if any(marker in low for marker in CONFUSION_MARKERS) and has_key(sentence, concept.keys) and len(sentence.split()) <= 60:
                found.append(f"Según {short_class_link(cls.id, base)}: {sentence}")
    return found


def _limits(concept: Concept, base: str) -> str:
    out: list[str] = []
    for cls in classes_text(concept):
        for name in ("Conceptos y decisiones", "Preguntas frecuentes", "Transferencia", "Fallo controlado y diagnóstico"):
            for paragraph in paragraphs(cls.sections.get(name, "")):
                for sentence in sentences(paragraph):
                    if has_key(sentence, concept.keys) and any(marker in f" {sentence.lower()}" for marker in LIMIT_MARKERS) and 8 <= len(sentence.split()) <= 60:
                        out.append(f"- {sentence} ({short_class_link(cls.id, base)})")
                        break
                if out:
                    break
            if len(out) >= 2:
                break
        if len(out) >= 2:
            break
    if out:
        return "Lo que las clases dicen sobre dónde deja de valer este término:\n\n" + "\n".join(out[:2])
    cls = next(iter(classes_text(concept)), None)
    if cls:
        closing = cls.closing_definitions
        limits = paragraphs(cls.sections.get("Límites y siguiente paso", ""))
        parts = []
        if closing:
            parts.append(clip(closing, 60))
        if limits:
            parts.append(clip(limits[0], 70))
        if parts:
            return (f"Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ({class_link(cls.id, base)}) son: "
                    + " ".join(parts))
    return "Las clases no declaran límites específicos para este término."


def _relations(concept: Concept, base: str) -> str:
    own = " ".join(text for _, _, text in concept.defs) + " " + " ".join(text for _, text in concept.glossary)
    related = concepts_in(own, concept)
    peers: dict[str, Concept] = {}
    for class_id in concept.classes[:2]:
        for peer in by_class().get(class_id, []):
            if peer.key != concept.key and "definition" in peer.kinds:
                peers.setdefault(peer.key, peer)
    prerequisites: list[Concept] = []
    prereq_ids = {pid for class_id in concept.classes[:1] for pid in data.classes()[class_id].prerequisites}
    for class_id in sorted(prereq_ids):
        for peer in by_class().get(class_id, []):
            if peer.key != concept.key and any(peer.key == r.key for r in related):
                prerequisites.append(peer)
    lines: list[str] = []
    if prerequisites:
        lines.append("- **Prerrequisito:** " + ", ".join(entry_link(p, base) for p in prerequisites[:4]) + ".")
    elif prereq_ids:
        ordered = sorted(prereq_ids)[:4]
        lines.append("- **Prerrequisito:** las clases previas " + ", ".join(short_class_link(i, base) for i in ordered) + " (sin término del glosario que lo sustituya).")
    else:
        lines.append("- **Prerrequisito:** ninguno declarado en las clases.")
    see = [c for c in related if c.key not in {p.key for p in prerequisites}][:4]
    for peer in sorted(peers.values(), key=lambda c: c.key):
        if len(see) >= 6:
            break
        if all(peer.key != c.key for c in see):
            see.append(peer)
    lines.append("- **Ver también:** " + (", ".join(entry_link(c, base) for c in see) + "." if see else "las demás entradas de la misma clase."))
    confusions: list[str] = []
    for cls in classes_text(concept):
        confusions += _confusions(cls, concept, base)
    if confusions:
        lines.append("- **Se confunde con:** " + re.sub(r"^Según \[[^\]]+\]\([^)]*\): ", "", confusions[0]))
    else:
        lines.append("- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».")
    return "\n".join(lines)


def _where(concept: Concept, base: str, cases: list[tuple[str, str, str]]) -> str:
    listed = sorted(ranked_ids(concept)[:MAX_CLASSES_LISTED])
    out = []
    if concept.role:
        out.append(f"Guía de rol: [{concept.name}]({cross_references.relative_link(base, f'roles/{concept.role}.md')}).")
        out.append("")
    if listed:
        out.append("**Se define o se desarrolla en:**")
        out.append("")
        for class_id in listed:
            part_id, part_title = part_of(class_id)
            out.append(f"- {class_link(class_id, base)} — Parte {part_id}, {part_title}.")
        if len(concept.classes) > len(listed):
            out.append(f"- y {len(concept.classes) - len(listed)} clases más que lo tratan con menos peso (ver «También se usa en»).")
    uses = [(class_id, n) for class_id, n in sorted(data.mentions().get(concept.key, {}).items(), key=lambda item: (-item[1], item[0])) if class_id not in concept.classes]
    if uses:
        out += ["", f"**También se usa en** ({len(uses)} clases más lo mencionan; las que más):", ""]
        out.append(", ".join(short_class_link(class_id, base) for class_id, _ in uses[:8]) + ".")
    if cases:
        out += ["", "**Aparece en los casos de estudio:** " + ", ".join(
            f"[{name}]({cross_references.relative_link(base, f'casos/{kind}/{slug}.md')})" for kind, slug, name in cases) + "."]
    return "\n".join(out)


def _synonyms(concept: Concept) -> str:
    aliases = [a for a in concept.aliases if a]
    english = [a for a in aliases if re.fullmatch(r"[A-Za-z][A-Za-z0-9 /\-]*", a) and not a.isupper()]
    others = [a for a in aliases if a not in english]
    out = []
    if others:
        out.append("**Sinónimos, siglas y variantes que usa el programa:** " + ", ".join(f"«{a}»" for a in others) + ".")
    if english:
        out.append("**Forma en inglés o término técnico original:** " + ", ".join(f"«{a}»" for a in english) + ".")
    return "\n\n".join(out) if out else "El programa no registra sinónimos ni traducciones distintas de la forma del título."


def _sources(concept: Concept) -> str:
    candidates: list[tuple[int, str, str, str]] = []
    for rank, cls in enumerate(classes_text(concept)[:4]):
        for title, url, note in cls.sources:
            relevant = has_key(f"{title} {note}", concept.keys)
            candidates.append((0 if relevant else 1 + rank, title, url, note))
    out: list[str] = []
    seen: set[str] = set()
    for _, title, url, note in sorted(candidates, key=lambda item: item[0]):
        if url in seen:
            continue
        seen.add(url)
        out.append(f"- [{title}]({url})" + (f" — {note}" if note else ""))
        if len(out) >= 5:
            break
    if not out:
        return "Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase)."
    return "Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):\n\n" + "\n".join(out)


# --------------------------------------------------------------------------- entrada completa
@dataclass
class Entry:
    concept: Concept
    sections: dict[str, str] = field(default_factory=dict)
    curated: set[str] = field(default_factory=set)

    @property
    def developed(self) -> bool:
        return all(name in self.curated for name in DEVELOPED_SECTIONS)


def role_sections(concept: Concept, base: str) -> dict[str, str]:
    text = (ROOT / "roles" / f"{concept.role}.md").read_text(encoding="utf-8")
    lead = re.search(r"^> (.+?)(?:\n>\n|\n\n)", text, re.M | re.S)
    summary = plain(re.sub(r"\n> ?", " ", lead.group(1))).strip() if lead else ""
    what = re.search(r"^## .*Qué es y por qué importa\n\n(.+?)\n\n", text, re.M | re.S)
    sections = {
        "Definición": (summary or "Ruta profesional del programa.") + f"\n\nGuía completa: [{concept.name}]({cross_references.relative_link(base, f'roles/{concept.role}.md')}).",
        "Por qué importa": plain(" ".join(what.group(1).split())) if what else "La guía de rol explica el alcance del puesto.",
        "Cómo funciona": "La guía conecta cada responsabilidad del puesto con partes y clases concretas, con evidencia y proyecto integrador; el recorrido está en la guía enlazada.",
        "Ejemplo": "La guía incluye un escenario de fallo, métricas con sus trampas y un plan 30/60/90; ábrela para el ejemplo completo.",
        "Errores y confusiones comunes": "Un rol no es un cargo ni una lista de herramientas: la guía separa responsabilidades, límites y roles adyacentes.",
        "Límites y cuándo no aplica": "Una ruta profesional no elimina prerrequisitos: las clases siguen la secuencia del programa y la guía solo ordena las de apoyo.",
    }
    return sections


def compose(concept: Concept, curated: dict[str, dict[str, str]], cases: list[tuple[str, str, str]]) -> Entry:
    base = f"{ENTRY_DIR}/{data.letter_of(concept.slug)}"
    entry = Entry(concept)
    if concept.role:
        entry.sections.update(role_sections(concept, base))
    else:
        entry.sections["Definición"] = _definitions(concept, base)
        entry.sections["Por qué importa"] = _why(concept, base)
        entry.sections["Cómo funciona"] = _how(concept, base)
        entry.sections["Ejemplo"] = _example(concept, base)
        entry.sections["Errores y confusiones comunes"] = _errors(concept, base)
        entry.sections["Límites y cuándo no aplica"] = _limits(concept, base)
    entry.sections["Relación con otros conceptos"] = _relations(concept, base) if not concept.role else "- **Prerrequisito:** las partes del núcleo de la guía.\n- **Ver también:** las demás guías del [índice de rutas](../../../roles/README.md).\n- **Se confunde con:** un cargo de empresa; la guía describe una ruta de aprendizaje, no un puesto."
    entry.sections["Dónde se enseña"] = _where(concept, base, cases)
    entry.sections["Sinónimos y traducción"] = _synonyms(concept)
    entry.sections["Fuentes"] = _sources(concept) if not concept.role else "Las fuentes de la ruta están en la sección «Fuentes» de la guía de rol enlazada."
    for name, text in curated.get(concept.slug, {}).items():
        if name in SECTIONS and text.strip():
            entry.sections[name] = text.strip()
            entry.curated.add(name)
    return entry
