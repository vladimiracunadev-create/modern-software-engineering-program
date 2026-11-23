"""Deterministic Mermaid -> SVG renderer for the program's published diagrams.

The content under ``content/`` keeps writing diagrams as fenced ``mermaid`` blocks
(that is the editable source). Every *publication* (``classes/``, ``roles/``, the
portal under ``site/``) replaces each block with a static SVG drawn here, with the
typography, colours and shapes of ``scripts/figure_kit.py``. No JavaScript, no
network, no third-party package: the same source always yields the same bytes.

Supported subset (anything else raises ``MermaidError`` so a build never ships a
silently degraded figure):

* ``flowchart`` / ``graph`` with ``LR``, ``RL``, ``TD``, ``TB``, ``BT`` directions;
  node shapes ``[ ]``, ``( )``, ``([ ])``, ``(( ))``, ``[[ ]]``, ``[( )]``, ``{ }``;
  edges ``-->``, ``---``, ``-.->``, ``==>``, ``-- text -->``, ``-. text .->`` and
  ``-->|text|``; chains ``A --> B --> C``; fan-in/out with ``&``; ``subgraph``;
  ``classDef`` / ``class`` / ``:::``.
* ``stateDiagram-v2``: converted to the same graph model (states are rounded
  nodes, ``[*]`` is a start or end marker, transitions keep their text) and drawn
  by the same layout, so no information is lost.
* ``sequenceDiagram``: drawn by its own small renderer (participants, solid and
  dashed messages, self messages and ``Note over``).

Layout: ranks by longest path after removing the last-listed edge of every cycle
(removed edges are drawn as dashed coral return arrows); ranks are laid out left
to right, and a chain too long for the reading width is folded into a serpentine
of equal rows; edges are routed orthogonally and never cross a node.
"""
from __future__ import annotations

import hashlib
import heapq
import html
import math
import os
import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

try:  # imported both as ``scripts.mermaid_render`` and from inside scripts/
    import figure_kit as fk
except ModuleNotFoundError:  # pragma: no cover - package-style import
    from scripts import figure_kit as fk

ROOT = Path(__file__).resolve().parents[1]
FIGURES_DIR = ROOT / "site" / "assets" / "figures"
RENDER_VERSION = 1

FS = 15  # node and message text
LFS = 14  # edge labels
LINE_H = FS * 1.28
LLINE_H = LFS * 1.28
MAX_W = 940  # same reading width as the other program figures
PAD = 22
NODE_WIDTHS = (190, 170, 150, 130)
WRAP_WIDTHS = (170, 150, 190, 130)  # folded rows read best with mid-width nodes
LABEL_WRAP = 118
KINDS = ("gold", "teal", "navy", "coral", "grey")  # classDef order -> kit palette kinds
ARROW = "#32505f"
RETURN = "#c0432f"


class MermaidError(ValueError):
    """The source uses syntax outside the supported subset, or cannot be laid out."""


# =============================================================================
# Text metrics
# =============================================================================
def tw(value: str, size: float = FS, weight: int = 400) -> float:
    """Estimated width: the kit's metric, widening symbols and emoji, ignoring joiners."""
    plain = "".join(ch for ch in value if ch not in "️‍")
    extra = sum(0.75 for ch in plain if ord(ch) >= 0x2190)
    return fk.text_width(plain, size, weight) + extra * size * fk.CHAR_W


def wrap(text: str, size: float, max_w: float) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        current = ""
        for word in paragraph.split():
            candidate = f"{current} {word}" if current else word
            if not current or tw(candidate, size) <= max_w:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines or [""]


def clean_label(raw: str) -> str:
    text = raw.strip()
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        text = text[1:-1]
    text = re.sub(r"<br\s*/?>|\\n", "\n", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("#quot;", '"')
    return "\n".join(" ".join(part.split()) for part in text.split("\n")).strip()


# =============================================================================
# Graph model and parsing
# =============================================================================
@dataclass
class Node:
    id: str
    label: str
    shape: str = "rect"
    cls: str | None = None
    sub: str | None = None
    order: int = 0
    # layout
    lines: list[str] = field(default_factory=list)
    w: float = 0.0
    h: float = 0.0
    rank: int = 0
    pos: int = 0
    cx: float = 0.0
    cy: float = 0.0
    seg: int = 0

    @property
    def rect(self) -> tuple[float, float, float, float]:
        return (self.cx - self.w / 2, self.cy - self.h / 2, self.cx + self.w / 2, self.cy + self.h / 2)


@dataclass
class Edge:
    src: str
    dst: str
    label: str = ""
    style: str = "solid"  # solid | dotted | thick
    arrow: bool = True
    both: bool = False
    idx: int = 0
    back: bool = False
    points: list[tuple[float, float]] = field(default_factory=list)


@dataclass
class Sub:
    id: str
    title: str
    parent: str | None


@dataclass
class Graph:
    kind: str  # flow | state
    direction: str = "LR"
    nodes: dict[str, Node] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    subs: dict[str, Sub] = field(default_factory=dict)
    classdefs: list[str] = field(default_factory=list)


ID = r"[A-Za-z_]\w*"
ID_RE = re.compile(ID)
SHAPES = (
    ("[(", ")]", "cyl"), ("((", "))", "circle"), ("([", "])", "stadium"), ("[[", "]]", "sub"),
    ("[", "]", "rect"), ("{", "}", "diamond"), ("(", ")", "round"),
)
EDGE_RE = re.compile(
    r"(?P<op><-->|-\.->|-\.-(?![\w.])|==>|-->|---|--o|--x)"
    r"|--\s+(?P<t1>.+?)\s+(?P<e1>-->|---)"
    r"|-\.\s*(?P<t2>[^>]*?)\s*\.->"
    r"|==\s+(?P<t4>.+?)\s+==>"
)
LABEL_RE = re.compile(r"\s*\|(?P<t>[^|]*)\|")


def _skip(text: str, pos: int) -> int:
    while pos < len(text) and text[pos] in " \t":
        pos += 1
    return pos


def _node_ref(text: str, pos: int, g: Graph, sub_stack: list[str]) -> tuple[str, int]:
    m = ID_RE.match(text, pos)
    if not m:
        raise MermaidError(f"expected a node id at {text[pos:pos + 20]!r} in {text!r}")
    nid, pos = m.group(0), m.end()
    label = shape = None
    for opener, closer, name in SHAPES:
        if text.startswith(opener, pos):
            start = pos + len(opener)
            if start < len(text) and text[start] == '"':
                end_quote = text.find('"', start + 1)
                if end_quote < 0 or not text.startswith(closer, end_quote + 1):
                    raise MermaidError(f"unterminated quoted label in {text!r}")
                label, pos = text[start:end_quote + 1], end_quote + 1 + len(closer)
            else:
                end = text.find(closer, start)
                if end < 0:
                    raise MermaidError(f"unterminated node label in {text!r}")
                label, pos = text[start:end], end + len(closer)
            shape = name
            break
    cls = None
    if text.startswith(":::", pos):
        m2 = ID_RE.match(text, pos + 3)
        if not m2:
            raise MermaidError(f"bad class suffix in {text!r}")
        cls, pos = m2.group(0), m2.end()
    node = g.nodes.get(nid)
    if node is None:
        node = Node(nid, nid, order=len(g.nodes), sub=sub_stack[-1] if sub_stack else None)
        g.nodes[nid] = node
    if label is not None:
        node.label, node.shape = clean_label(label), shape or "rect"
    if cls:
        node.cls = cls
    return nid, pos


def parse_flow(lines: list[str], header: str) -> Graph:
    parts = header.split()
    g = Graph("flow", parts[1].upper() if len(parts) > 1 else "TB")
    if g.direction not in {"LR", "RL", "TD", "TB", "BT"}:
        raise MermaidError(f"unsupported direction {g.direction!r}")
    sub_stack: list[str] = []
    classes: dict[str, list[str]] = {}
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("%%"):
            continue
        low = line.split()[0]
        if low == "subgraph":
            rest = line[len("subgraph"):].strip()
            m = re.fullmatch(rf"({ID})\s*\[(.*)\]", rest)
            sid, title = (m.group(1), clean_label(m.group(2))) if m else (clean_label(rest), clean_label(rest))
            g.subs[sid] = Sub(sid, title, sub_stack[-1] if sub_stack else None)
            sub_stack.append(sid)
            continue
        if line == "end":
            if not sub_stack:
                raise MermaidError("'end' without subgraph")
            sub_stack.pop()
            continue
        if low == "direction":
            continue
        if low == "classDef":
            name = line.split()[1]
            if name not in g.classdefs:
                g.classdefs.append(name)
            continue
        if low == "class":
            _, ids, name = line.split(None, 2)
            for nid in ids.split(","):
                classes.setdefault(name.strip(), []).append(nid.strip())
            continue
        if low in {"style", "linkStyle", "click"}:
            continue
        _statement(line, g, sub_stack)
    if sub_stack:
        raise MermaidError("unclosed subgraph")
    for name, ids in classes.items():
        for nid in ids:
            if nid in g.nodes:
                g.nodes[nid].cls = name
    return g


def _statement(line: str, g: Graph, sub_stack: list[str]) -> None:
    pos = 0
    previous: list[str] | None = None
    pending: dict | None = None
    while True:
        group: list[str] = []
        while True:
            pos = _skip(line, pos)
            nid, pos = _node_ref(line, pos, g, sub_stack)
            group.append(nid)
            pos = _skip(line, pos)
            if line.startswith("&", pos):
                pos += 1
                continue
            break
        if previous is not None and pending is not None:
            for src in previous:
                for dst in group:
                    g.edges.append(Edge(src, dst, pending["label"], pending["style"], pending["arrow"],
                                        pending["both"], len(g.edges)))
        if pos >= len(line):
            return
        m = EDGE_RE.match(line, pos)
        if not m:
            raise MermaidError(f"unsupported syntax at {line[pos:pos + 24]!r} in {line!r}")
        pos = m.end()
        op = m.group("op") or m.group("e1") or ("-.->" if m.group("t2") is not None else "==>")
        text = m.group("t1") or m.group("t2") or m.group("t4") or ""
        lm = LABEL_RE.match(line, pos)
        if lm:
            text, pos = lm.group("t"), lm.end()
        pending = {
            "label": clean_label(text),
            "style": "dotted" if op.startswith("-.") else "thick" if op.startswith("==") else "solid",
            "arrow": op not in {"---", "-.-"},
            "both": op == "<-->",
        }
        previous = group


def parse_state(lines: list[str]) -> Graph:
    g = Graph("state", "LR")
    counters = {"start": 0, "end": 0}

    def state(token: str, role: str) -> str:
        token = token.strip()
        if token == "[*]":
            counters[role] += 1
            nid = f"__{role}{counters[role]}"
            g.nodes[nid] = Node(nid, "", role, order=len(g.nodes))
            return nid
        if not ID_RE.fullmatch(token):
            raise MermaidError(f"unsupported state name {token!r}")
        if token not in g.nodes:
            g.nodes[token] = Node(token, token.replace("_", " "), "round", order=len(g.nodes))
        return token

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("%%"):
            continue
        if line.startswith("direction"):
            g.direction = line.split()[1].upper()
            continue
        m = re.fullmatch(r"(\[\*\]|\w+)\s*-->\s*(\[\*\]|\w+)\s*(?::\s*(.*))?", line)
        if m:
            src = state(m.group(1), "start")
            dst = state(m.group(2), "end")
            g.edges.append(Edge(src, dst, clean_label(m.group(3) or ""), idx=len(g.edges)))
            continue
        m = re.fullmatch(r"(\w+)\s*:\s*(.+)", line)
        if m:
            state(m.group(1), "start")
            g.nodes[m.group(1)].label = clean_label(m.group(2))
            continue
        m = re.fullmatch(r'state\s+"(.+)"\s+as\s+(\w+)', line)
        if m:
            state(m.group(2), "start")
            g.nodes[m.group(2)].label = clean_label(m.group(1))
            continue
        raise MermaidError(f"unsupported state diagram syntax: {line!r}")
    return g


# -- sequence diagrams --------------------------------------------------------
@dataclass
class SeqItem:
    kind: str  # message | note
    a: str
    b: str
    text: str
    dashed: bool = False
    arrow: bool = True


@dataclass
class Sequence:
    names: list[str] = field(default_factory=list)
    labels: dict[str, str] = field(default_factory=dict)
    items: list[SeqItem] = field(default_factory=list)


MSG_RE = re.compile(r"(?P<a>\w+)\s*(?P<op>-->>|->>|--x|-x|--\)|-\)|-->|->)\s*(?P<b>\w+)\s*:\s*(?P<t>.*)")
NOTE_RE = re.compile(r"Note\s+(?P<where>over|left of|right of)\s+(?P<who>\w+(?:\s*,\s*\w+)?)\s*:\s*(?P<t>.*)")


def parse_sequence(lines: list[str]) -> Sequence:
    seq = Sequence()

    def declare(name: str, label: str | None = None) -> None:
        if name not in seq.names:
            seq.names.append(name)
        if label is not None:
            seq.labels[name] = label
        seq.labels.setdefault(name, name)

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("%%") or line == "autonumber":
            continue
        m = re.fullmatch(r"(?:participant|actor)\s+(\w+)(?:\s+as\s+(.+))?", line)
        if m:
            declare(m.group(1), clean_label(m.group(2)) if m.group(2) else None)
            continue
        m = NOTE_RE.fullmatch(line)
        if m:
            who = [w.strip() for w in m.group("who").split(",")]
            for name in who:
                declare(name)
            seq.items.append(SeqItem("note", who[0], who[-1], clean_label(m.group("t"))))
            continue
        m = MSG_RE.fullmatch(line)
        if m:
            declare(m.group("a"))
            declare(m.group("b"))
            op = m.group("op")
            seq.items.append(SeqItem("message", m.group("a"), m.group("b"), clean_label(m.group("t")),
                                     dashed=op.startswith("--"), arrow=op.endswith((">>", "x", ")"))))
            continue
        raise MermaidError(f"unsupported sequence diagram syntax: {line!r}")
    if not seq.names or not seq.items:
        raise MermaidError("empty sequence diagram")
    return seq


def parse(source: str) -> Graph | Sequence:
    lines = [ln.rstrip() for ln in source.replace("\r\n", "\n").split("\n")]
    while lines and (not lines[0].strip() or lines[0].strip().startswith("%%")):
        lines.pop(0)
    if not lines:
        raise MermaidError("empty diagram")
    header = lines[0].strip()
    word = header.split()[0]
    if word in {"flowchart", "graph"}:
        return parse_flow(lines[1:], header)
    if word == "stateDiagram-v2" or word == "stateDiagram":
        return parse_state(lines[1:])
    if word == "sequenceDiagram":
        return parse_sequence(lines[1:])
    raise MermaidError(f"unsupported diagram type {word!r}")


# =============================================================================
# Layout
# =============================================================================
Point = tuple[float, float]
Rect = tuple[float, float, float, float]


def break_cycles(g: Graph) -> None:
    """Mark as ``back`` the last-listed edge of every cycle until the rest is a DAG."""
    for edge in g.edges:
        edge.back = edge.src == edge.dst
    while True:
        adjacency: dict[str, list[Edge]] = {nid: [] for nid in g.nodes}
        for edge in g.edges:
            if not edge.back:
                adjacency[edge.src].append(edge)
        state: dict[str, int] = {}
        stack: list[Edge] = []
        cycle: list[Edge] | None = None

        def visit(nid: str) -> bool:
            nonlocal cycle
            state[nid] = 1
            for edge in adjacency[nid]:
                if state.get(edge.dst) == 1:
                    start = next((i for i, e in enumerate(stack) if e.src == edge.dst), len(stack))
                    cycle = stack[start:] + [edge]
                    return True
                if edge.dst not in state:
                    stack.append(edge)
                    if visit(edge.dst):
                        return True
                    stack.pop()
            state[nid] = 2
            return False

        for nid in g.nodes:
            if nid not in state and visit(nid):
                break
        if cycle is None:
            return
        max(cycle, key=lambda e: e.idx).back = True


def assign_ranks(g: Graph) -> list[list[Node]]:
    forward = [e for e in g.edges if not e.back]
    preds: dict[str, list[str]] = {nid: [] for nid in g.nodes}
    succs: dict[str, list[str]] = {nid: [] for nid in g.nodes}
    for e in forward:
        preds[e.dst].append(e.src)
        succs[e.src].append(e.dst)
    rank: dict[str, int] = {}

    def depth(nid: str) -> int:
        if nid not in rank:
            rank[nid] = 0  # guards recursion; the graph is acyclic here
            rank[nid] = max((depth(p) + 1 for p in preds[nid]), default=0)
        return rank[nid]

    for nid in g.nodes:
        depth(nid)
    for nid in g.nodes:  # pull sources next to their first consumer
        if not preds[nid] and succs[nid]:
            rank[nid] = min(rank[s] for s in succs[nid]) - 1
    low = min(rank.values())
    for nid in rank:
        rank[nid] -= low
    ranks: list[list[Node]] = [[] for _ in range(max(rank.values()) + 1)]
    for nid, node in g.nodes.items():
        node.rank = rank[nid]
        ranks[node.rank].append(node)
    order_ranks(g, ranks, preds, succs)
    return ranks


def order_ranks(g: Graph, ranks: list[list[Node]], preds, succs) -> None:
    for rank_nodes in ranks:
        for i, node in enumerate(rank_nodes):
            node.pos = i

    for _ in range(3):
        for r in range(1, len(ranks)):
            sweep_rank(g, ranks, r, preds)
        for r in range(len(ranks) - 2, -1, -1):
            sweep_rank(g, ranks, r, succs)
    if g.subs:
        keep_groups_together(g, ranks)


def sweep_rank(g: Graph, ranks, r: int, use) -> None:
    rank_nodes = ranks[r]
    keys = {}
    for node in rank_nodes:
        near = [g.nodes[n] for n in use[node.id]]
        keys[node.id] = (sum((n.pos + 0.5) / len(ranks[n.rank]) for n in near) / len(near)) if near \
            else (node.pos + 0.5) / len(rank_nodes)
    rank_nodes.sort(key=lambda n: (keys[n.id], n.pos))
    for i, node in enumerate(rank_nodes):
        node.pos = i


def top_sub(g: Graph, node: Node) -> str | None:
    sid = node.sub
    while sid is not None and g.subs[sid].parent is not None:
        sid = g.subs[sid].parent
    return sid


def group_key(g: Graph, ranks, key, bucket: list[Node]) -> float:
    if isinstance(key, tuple):  # solo node
        node = bucket[0]
        return (node.pos + 0.5) / len(ranks[node.rank])
    members = [n for n in g.nodes.values() if top_sub(g, n) == key]
    return sum((n.pos + 0.5) / len(ranks[n.rank]) for n in members) / len(members)


def keep_groups_together(g: Graph, ranks: list[list[Node]]) -> None:
    for rank_nodes in ranks:
        buckets: dict[object, list[Node]] = {}
        for node in rank_nodes:
            buckets.setdefault(top_sub(g, node) or ("solo", node.id), []).append(node)
        ordered = sorted(buckets.items(), key=lambda kv: group_key(g, ranks, kv[0], kv[1]))
        rank_nodes[:] = [n for _, bucket in ordered for n in bucket]
        for i, node in enumerate(rank_nodes):
            node.pos = i


def size_nodes(g: Graph, max_w: float) -> None:
    for node in g.nodes.values():
        if node.shape in {"start", "end"}:
            node.lines, node.w, node.h = [], 26.0, 26.0
            continue
        node.lines = wrap(node.label, FS, max_w - 28)
        text_w = max(tw(line) for line in node.lines)
        text_h = len(node.lines) * LINE_H
        if node.shape == "diamond":
            height = max(1.8 * text_h + 16, 62.0)
            width = text_w + 28
            for i, line in enumerate(node.lines):
                a = tw(line) / 2 + 3
                b = abs((i - (len(node.lines) - 1) / 2) * LINE_H) + LINE_H * 0.5
                width = max(width, 2 * a / (1 - 2 * b / height))
            node.w, node.h = math.ceil(width + 6), math.ceil(height)
        else:
            node.w = max(math.ceil(text_w + 28), 76)
            node.h = max(math.ceil(text_h + 22 + (12 if node.shape == "cyl" else 0)), 44)


def chip_size(label: str) -> tuple[list[str], float, float]:
    lines = wrap(label, LFS, LABEL_WRAP)
    return lines, math.ceil(max(tw(line, LFS) for line in lines) + 12), math.ceil(len(lines) * LLINE_H + 6)


def overlaps(a: Rect, b: Rect, margin: float = 0.0) -> bool:
    return a[0] < b[2] + margin and b[0] < a[2] + margin and a[1] < b[3] + margin and b[1] < a[3] + margin


def seg_hits_rect(p: Point, q: Point, r: Rect) -> bool:
    (x1, y1), (x2, y2) = p, q
    if abs(x1 - x2) < 1e-6:
        return r[0] < x1 < r[2] and min(y1, y2) < r[3] and max(y1, y2) > r[1]
    return r[1] < y1 < r[3] and min(x1, x2) < r[2] and max(x1, x2) > r[0]


def inflate(r: Rect, d: float) -> Rect:
    return (r[0] - d, r[1] - d, r[2] + d, r[3] + d)


@dataclass
class Layout:
    graph: Graph
    ranks: list[list[Node]]
    k: int  # ranks per row (LR) ; 0 for TD
    rows: int
    gaps: list[float]
    chips: dict[int, tuple[list[str], float, float]]


def edge_needs(g: Graph) -> dict[int, tuple[list[str], float, float]]:
    return {e.idx: chip_size(e.label) for e in g.edges if e.label}


def prepare(g: Graph):
    break_cycles(g)
    ranks = assign_ranks(g)
    return ranks, edge_needs(g)


def build_layout(g: Graph, ranks, chips, max_w: int, mode: str, reserve: float) -> Layout | None:
    """mode: ``row`` (as written), ``down`` (an LR diagram too wide for one row, drawn top-down) or ``wrap``."""
    horizontal = g.direction in {"LR", "RL"}
    hard = any(e.back for e in g.edges) or any(g.nodes[e.dst].rank - g.nodes[e.src].rank > 1
                                                for e in g.edges if not e.back)
    avail = MAX_W - 2 * PAD - (84 if hard else 0) - reserve
    extra = 30 if g.subs else 0
    size_nodes(g, max_w)
    if mode == "down":
        return place_td(g, ranks, chips, avail, extra, force=False)
    if horizontal:
        return place_lr(g, ranks, chips, avail, extra, allow_wrap=(mode == "wrap"))
    return place_td(g, ranks, chips, avail, extra, force=(mode == "wrap"))


def rank_gap_needs(g: Graph, ranks, chips, extra: float) -> list[float]:
    needs = [46.0 + extra] * max(len(ranks) - 1, 0)
    for e in g.edges:
        if e.back or not e.label:
            continue
        u, v = g.nodes[e.src], g.nodes[e.dst]
        if v.rank == u.rank + 1:
            needs[u.rank] = max(needs[u.rank], chips[e.idx][1] + 24 + extra)
    return needs


def place_lr(g: Graph, ranks, chips, avail: float, extra: float, allow_wrap: bool) -> Layout | None:
    count = len(ranks)
    col_w = [max(n.w for n in r) for r in ranks]
    needs = rank_gap_needs(g, ranks, chips, extra)
    single = sum(col_w) + sum(needs)
    if single <= avail:
        k = count
    elif not allow_wrap:
        return None
    else:
        k = pick_row_length(g, ranks, col_w, needs, avail)
    rows = math.ceil(count / k)
    slot_w = [0.0] * k
    slot_gap = [46.0 + extra] * max(k - 1, 0)
    for r in range(count):
        seg, p = divmod(r, k)
        slot = p if seg % 2 == 0 else k - 1 - p
        slot_w[slot] = max(slot_w[slot], col_w[r])
        if p < k - 1 and r + 1 < count:
            left = slot if seg % 2 == 0 else slot - 1
            slot_gap[left] = max(slot_gap[left], needs[r])
    slot_x = []
    cursor = 0.0
    for c in range(k):
        slot_x.append(cursor + slot_w[c] / 2)
        cursor += slot_w[c] + (slot_gap[c] if c < k - 1 else 0)
    wrap_chip = max((chips[e.idx][2] for e in g.edges if e.idx in chips and not e.back
                     and g.nodes[e.dst].rank == g.nodes[e.src].rank + 1
                     and g.nodes[e.dst].rank % k == 0 and g.nodes[e.dst].rank > 0), default=0)
    block_gap = max(58.0 + extra, wrap_chip + 30)
    lane_gap = 24.0 + extra + (14 if any(e.back for e in g.edges) else 0)
    heights = []
    lane_h: list[list[float]] = []
    for seg in range(rows):
        members = ranks[seg * k:(seg + 1) * k]
        most = max(len(r) for r in members)
        lanes = [0.0] * most
        for r in members:
            if len(r) == most:
                for i, node in enumerate(r):
                    lanes[i] = max(lanes[i], node.h)
        lane_h.append(lanes)
        grid = sum(lanes) + lane_gap * (most - 1)
        heights.append(max([grid] + [sum(n.h for n in r) + lane_gap * (len(r) - 1) for r in members]))
    top = 0.0
    preds: dict[str, list[Node]] = {nid: [] for nid in g.nodes}
    for e in g.edges:
        if not e.back:
            preds[e.dst].append(g.nodes[e.src])
    for seg in range(rows):
        most = len(lane_h[seg])
        centers = []
        y = top + (heights[seg] - (sum(lane_h[seg]) + lane_gap * (most - 1))) / 2
        for h in lane_h[seg]:
            centers.append(y + h / 2)
            y += h + lane_gap
        for r in range(seg * k, min((seg + 1) * k, count)):
            p = r - seg * k
            slot = p if seg % 2 == 0 else k - 1 - p
            nodes = ranks[r]
            for node in nodes:
                node.seg = seg
                node.cx = round(slot_x[slot], 1)
            if len(nodes) == most:
                for node, cy in zip(nodes, centers):
                    node.cy = round(cy, 1)
                continue
            if len(nodes) == 1:
                near = [n.cy for n in preds[nodes[0].id] if n.seg == seg and n.rank == r - 1]
                if near:
                    cy = sum(near) / len(near)
                    nodes[0].cy = round(min(max(cy, top + nodes[0].h / 2), top + heights[seg] - nodes[0].h / 2), 1)
                    continue
            stack = sum(n.h for n in nodes) + lane_gap * (len(nodes) - 1)
            y = top + (heights[seg] - stack) / 2
            for node in nodes:
                node.cy = round(y + node.h / 2, 1)
                y += node.h + lane_gap
        top += heights[seg] + block_gap
    if g.direction == "RL":
        width = cursor
        for node in g.nodes.values():
            node.cx = round(width - node.cx, 1)
    return Layout(g, ranks, k, rows, needs, chips)


def pick_row_length(g: Graph, ranks, col_w, needs, avail: float) -> int:
    count = len(ranks)
    best_k, best_cost = 1, math.inf
    for k in range(1, count):
        slot_w = [0.0] * k
        slot_gap = [46.0] * max(k - 1, 0)
        for r in range(count):
            seg, p = divmod(r, k)
            slot = p if seg % 2 == 0 else k - 1 - p
            slot_w[slot] = max(slot_w[slot], col_w[r])
            if p < k - 1 and r + 1 < count:
                left = slot if seg % 2 == 0 else slot - 1
                slot_gap[left] = max(slot_gap[left], needs[r])
        if sum(slot_w) + sum(slot_gap) > avail:
            continue
        rows = math.ceil(count / k)
        penalty = 0
        for cut in range(k, count, k):
            penalty += 60 if len(ranks[cut - 1]) > 1 else 0
            penalty += 40 if len(ranks[cut]) > 1 else 0
        cost = rows * 100 + (k * rows - count) * 12 + penalty
        if cost < best_cost:
            best_k, best_cost = k, cost
    return best_k


def place_td(g: Graph, ranks, chips, avail: float, extra: float, force: bool = False) -> Layout | None:
    gap_x = 34.0 + extra
    widths = [sum(n.w for n in r) + gap_x * (len(r) - 1) for r in ranks]
    if max(widths) > avail and not force:
        return None
    needs = [58.0 + extra] * max(len(ranks) - 1, 0)
    for e in g.edges:
        if not e.back and e.label and g.nodes[e.dst].rank == g.nodes[e.src].rank + 1:
            needs[g.nodes[e.src].rank] = max(needs[g.nodes[e.src].rank], chips[e.idx][2] + 34 + extra)
    center = max(widths) / 2
    y = 0.0
    ys = []
    for r, rank_nodes in enumerate(ranks):
        row_h = max(n.h for n in rank_nodes)
        ys.append(y + row_h / 2)
        y += row_h + (needs[r] if r < len(needs) else 0)
    for r, rank_nodes in enumerate(ranks):  # initial: centred row
        x = center - widths[r] / 2
        for node in rank_nodes:
            node.cx = x + node.w / 2
            x += node.w + gap_x
            node.cy = ys[r]
    for _ in range(4):
        for r in list(range(1, len(ranks))) + list(range(len(ranks) - 2, -1, -1)):
            align_row(g, ranks, r, gap_x, forward=r > 0)
    for node in g.nodes.values():
        node.cx, node.cy = round(node.cx, 1), round(node.cy, 1)
    if g.subs:
        repair_groups(Layout(g, ranks, 0, len(ranks), needs, chips))
    if g.direction == "BT":
        top = max(n.cy for n in g.nodes.values())
        for node in g.nodes.values():
            node.cy = round(top - node.cy, 1)
    return Layout(g, ranks, 0, len(ranks), needs, chips)


def repair_groups(layout: Layout) -> None:
    """Push colliding groups (and strangers inside a group) apart, then restore row spacing."""
    g = layout.graph
    for _ in range(40):
        rects = group_rects(layout, check=False)
        moved = False
        tops = [sid for sid in rects if g.subs[sid].parent is None]
        for i, a in enumerate(tops):
            for b in tops[i + 1:]:
                if not overlaps(rects[a], rects[b]):
                    continue
                left, right = (a, b) if rects[a][0] + rects[a][2] <= rects[b][0] + rects[b][2] else (b, a)
                dx = rects[left][2] + 26 - rects[right][0]
                for n in g.nodes.values():
                    if top_sub(g, n) == right:
                        n.cx += dx
                moved = True
        for sid in tops:
            for n in g.nodes.values():
                if top_sub(g, n) == sid or not overlaps(inflate(n.rect, -1), rects[sid]):
                    continue
                if n.cx >= (rects[sid][0] + rects[sid][2]) / 2:
                    n.cx += rects[sid][2] + 22 - n.rect[0]
                else:
                    n.cx -= n.rect[2] - rects[sid][0] + 22
                moved = True
        for rank_nodes in layout.ranks:
            ordered = sorted(rank_nodes, key=lambda n: n.cx)
            for a, b in zip(ordered, ordered[1:]):
                least = a.cx + (a.w + b.w) / 2 + 34
                if b.cx < least:
                    b.cx = least
                    moved = True
        if not moved:
            break
    low = min(n.rect[0] for n in g.nodes.values())
    for n in g.nodes.values():
        n.cx = round(n.cx - low + 60, 1)


def align_row(g: Graph, ranks, r: int, gap_x: float, forward: bool) -> None:
    rank_nodes = ranks[r]
    desired = {}
    for node in rank_nodes:
        near = [g.nodes[e.src if e.dst == node.id else e.dst] for e in g.edges
                if not e.back and node.id in (e.src, e.dst)
                and abs(g.nodes[e.src if e.dst == node.id else e.dst].rank - node.rank) == 1]
        desired[node.id] = sum(n.cx for n in near) / len(near) if near else node.cx
    xs = [desired[n.id] for n in rank_nodes]
    for i in range(1, len(rank_nodes)):
        least = xs[i - 1] + (rank_nodes[i - 1].w + rank_nodes[i].w) / 2 + gap_x
        xs[i] = max(xs[i], least)
    shift = (sum(desired[n.id] for n in rank_nodes) - sum(xs)) / len(xs)
    for node, x in zip(rank_nodes, xs):
        node.cx = x + shift


# -- routing -------------------------------------------------------------------
def simplify(points: list[Point]) -> list[Point]:
    out: list[Point] = []
    for p in points:
        if out and abs(out[-1][0] - p[0]) < 1e-6 and abs(out[-1][1] - p[1]) < 1e-6:
            continue
        out.append(p)
    changed = True
    while changed and len(out) > 2:
        changed = False
        for i in range(1, len(out) - 1):
            a, b, c = out[i - 1], out[i], out[i + 1]
            if (abs(a[0] - b[0]) < 1e-6 and abs(b[0] - c[0]) < 1e-6) or (abs(a[1] - b[1]) < 1e-6 and abs(b[1] - c[1]) < 1e-6):
                del out[i]
                changed = True
                break
    return out


def port(node: Node, side: str) -> Point:
    x0, y0, x1, y1 = node.rect
    return {"right": (x1, node.cy), "left": (x0, node.cy), "top": (node.cx, y0), "bottom": (node.cx, y1)}[side]


NORMAL = {"right": (1, 0), "left": (-1, 0), "top": (0, -1), "bottom": (0, 1)}


def exit_point(node: Node, side: str) -> Point:
    px, py = port(node, side)
    dx, dy = NORMAL[side]
    return (px + dx * 14, py + dy * 14)


def seg_cost(p: Point, q: Point, drawn: list[tuple[Point, Point]]) -> float:
    """Penalty for running along or across routes that are already drawn."""
    cost = 0.0
    px, py = p
    qx, qy = q
    vertical = abs(px - qx) < 1e-6
    for (ax, ay), (bx, by) in drawn:
        a_vertical = abs(ax - bx) < 1e-6
        if vertical and a_vertical:
            if abs(px - ax) < 1e-6:
                overlap = min(max(py, qy), max(ay, by)) - max(min(py, qy), min(ay, by))
                if overlap > 0:
                    cost += overlap * 1.5
        elif not vertical and not a_vertical:
            if abs(py - ay) < 1e-6:
                overlap = min(max(px, qx), max(ax, bx)) - max(min(px, qx), min(ax, bx))
                if overlap > 0:
                    cost += overlap * 1.5
        elif vertical:  # p-q vertical, a-b horizontal
            if min(ax, bx) < px < max(ax, bx) and min(py, qy) < ay < max(py, qy):
                cost += 45
        else:
            if min(ay, by) < py < max(ay, by) and min(px, qx) < ax < max(px, qx):
                cost += 45
    return cost


def route_astar(g: Graph, u: Node, v: Node, drawn: list, port_use: dict, bounds: Rect) -> list[Point]:
    obstacles = [inflate(n.rect, 8) for n in g.nodes.values()]
    xs = {bounds[0], bounds[2]}
    ys = {bounds[1], bounds[3]}
    for n in g.nodes.values():
        x0, y0, x1, y1 = n.rect
        xs.update((x0 - 14, n.cx, x1 + 14))
        ys.update((y0 - 14, n.cy, y1 + 14))
    for d in (28, 46):
        xs.update((bounds[0] + 44 - d, bounds[2] - 44 + d))
        ys.update((bounds[1] + 44 - d, bounds[3] - 44 + d))
    for axis_values, low, high in ((xs, 0, 2), (ys, 1, 3)):
        spans = sorted((o[low], o[high]) for o in obstacles)
        merged: list[list[float]] = []
        for a, b in spans:
            if merged and a <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], b)
            else:
                merged.append([a, b])
        for left, right in zip(merged, merged[1:]):
            if right[0] - left[1] > 10:
                axis_values.add(round((left[1] + right[0]) / 2, 1))
    xl, yl = sorted(round(x, 1) for x in xs), sorted(round(y, 1) for y in ys)
    xi = {x: i for i, x in enumerate(xl)}
    yi = {y: i for i, y in enumerate(yl)}

    def cell(p: Point) -> tuple[int, int]:
        return xi[round(p[0], 1)], yi[round(p[1], 1)]

    blocked_cache: dict = {}
    cost_cache: dict = {}
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def blocked(a: tuple[int, int], b: tuple[int, int]) -> bool:
        key = (a, b)
        if key not in blocked_cache:
            p, q = (xl[a[0]], yl[a[1]]), (xl[b[0]], yl[b[1]])
            blocked_cache[key] = any(seg_hits_rect(p, q, o) for o in obstacles)
        return blocked_cache[key]

    def step_cost(a: tuple[int, int], b: tuple[int, int]) -> float:
        key = (a, b)
        if key not in cost_cache:
            p, q = (xl[a[0]], yl[a[1]]), (xl[b[0]], yl[b[1]])
            cost_cache[key] = abs(p[0] - q[0]) + abs(p[1] - q[1]) + seg_cost(p, q, drawn)
        return cost_cache[key]

    sides = ("right", "left", "top", "bottom")
    heap: list = []
    best: dict = {}
    parent: dict = {}
    counter = 0
    for side in sides:
        e = exit_point(u, side)
        state = (cell(e), dirs.index(NORMAL[side]))
        start_cost = 150.0 * port_use.get((u.id, side), 0)
        best[state] = start_cost
        parent[state] = (None, side, e)
        heapq.heappush(heap, (start_cost, counter, state))
        counter += 1
    goals = {}
    for side in sides:
        goals.setdefault(cell(exit_point(v, side)), []).append(side)
    goal_list = list(goals)
    found = None
    end_side = None
    while heap:
        f, _, state = heapq.heappop(heap)
        if state[0] == "goal":
            found, end_side = state[1], state[2]
            break
        (cx_i, cy_i), d = state
        gcost = best[state]
        if (cx_i, cy_i) in goals:
            for side in goals[(cx_i, cy_i)]:
                counter += 1
                heapq.heappush(heap, (gcost + 150.0 * port_use.get((v.id, side), 0), counter, ("goal", state, side)))
        for nd, (dx, dy) in enumerate(dirs):
            if (dx, dy) == (-dirs[d][0], -dirs[d][1]):
                continue
            nx, ny = cx_i + dx, cy_i + dy
            if not (0 <= nx < len(xl) and 0 <= ny < len(yl)) or blocked((cx_i, cy_i), (nx, ny)):
                continue
            cost = gcost + step_cost((cx_i, cy_i), (nx, ny)) + (26 if nd != d else 0)
            nstate = ((nx, ny), nd)
            if cost < best.get(nstate, math.inf) - 1e-9:
                best[nstate] = cost
                parent[nstate] = (state, None, None)
                h = min(abs(xl[nx] - xl[gx]) + abs(yl[ny] - yl[gy]) for gx, gy in goal_list)
                counter += 1
                heapq.heappush(heap, (cost + h, counter, nstate))
    if found is None:
        raise MermaidError(f"no route between {u.id} and {v.id}")
    chain = []
    state = found
    while state is not None:
        prev, side, e = parent[state]
        chain.append((state, side, e))
        state = prev
    chain.reverse()
    start_side, start_exit = chain[0][1], chain[0][2]
    pts = [port(u, start_side), start_exit]
    pts.extend((xl[s[0][0]], yl[s[0][1]]) for s, _, _ in chain[1:])
    pts.append(port(v, end_side))
    path = simplify(pts)
    port_use[(u.id, start_side)] = port_use.get((u.id, start_side), 0) + 1
    port_use[(v.id, end_side)] = port_use.get((v.id, end_side), 0) + 1
    return path


def simple_route(layout: Layout, e: Edge) -> list[Point] | None:
    g = layout.graph
    u, v = g.nodes[e.src], g.nodes[e.dst]
    if v.rank != u.rank + 1:
        return None
    if layout.k:  # horizontal flow
        if u.seg == v.seg:
            dx = 1 if (u.seg % 2 == 0) != (g.direction == "RL") else -1
            a = (u.cx + dx * u.w / 2, u.cy)
            b = (v.cx - dx * v.w / 2, v.cy)
            mid = round(a[0] + dx * 16, 1) if e.label else round((a[0] + b[0]) / 2, 1)
            pts = [a, (mid, a[1]), (mid, b[1]), b]
        else:
            a, b = (u.cx, u.cy + u.h / 2), (v.cx, v.cy - v.h / 2)
            mid = round(a[1] + 16, 1) if e.label else round((a[1] + b[1]) / 2, 1)
            pts = [a, (a[0], mid), (b[0], mid), b]
    else:
        a, b = (u.cx, u.cy + u.h / 2), (v.cx, v.cy - v.h / 2)
        if g.direction == "BT":
            a, b = (u.cx, u.cy - u.h / 2), (v.cx, v.cy + v.h / 2)
        sign = -1 if g.direction == "BT" else 1
        mid = round(a[1] + sign * 16, 1) if e.label else round((a[1] + b[1]) / 2, 1)
        pts = [a, (a[0], mid), (b[0], mid), b]
    if len(pts) == 4:
        (ax, ay), (bx, by) = pts[0], pts[-1]
        if abs(ax - bx) < 9 and abs(pts[1][0] - pts[1][0]) < 1e-6 and abs(pts[0][0] - pts[1][0]) < 1e-6:
            mx = round((ax + bx) / 2, 1)  # vertical flow, nearly aligned: draw it straight
            pts = [(mx, ay), (mx, by)]
        elif abs(ay - by) < 9 and abs(pts[0][1] - pts[1][1]) < 1e-6:
            my = round((ay + by) / 2, 1)  # horizontal flow, nearly aligned
            pts = [(ax, my), (bx, my)]
    pts = simplify([(round(x, 1), round(y, 1)) for x, y in pts])
    for other in g.nodes.values():
        if other.id in (u.id, v.id):
            continue
        r = inflate(other.rect, 4)
        if any(seg_hits_rect(p, q, r) for p, q in zip(pts, pts[1:])):
            return None
    for node in (u, v):
        r = inflate(node.rect, -2)
        if any(seg_hits_rect(p, q, r) for p, q in zip(pts, pts[1:])):
            return None
    return pts


def side_of(node: Node, p: Point) -> str:
    x0, y0, x1, y1 = node.rect
    if abs(p[0] - x1) < 1.5:
        return "right"
    if abs(p[0] - x0) < 1.5:
        return "left"
    return "top" if abs(p[1] - y0) < 1.5 else "bottom"


def route_all(layout: Layout) -> None:
    g = layout.graph
    boxes = [n.rect for n in g.nodes.values()]
    bounds = (min(b[0] for b in boxes) - 60, min(b[1] for b in boxes) - 60,
              max(b[2] for b in boxes) + 60, max(b[3] for b in boxes) + 60)
    drawn: list[tuple[Point, Point]] = []
    port_use: dict = {}
    hard: list[Edge] = []
    for e in g.edges:
        u, v = g.nodes[e.src], g.nodes[e.dst]
        if e.src == e.dst:
            x0, y0, x1, y1 = u.rect
            e.points = [(x1 - 14, y0), (x1 - 14, y0 - 22), (x1 + 18, y0 - 22), (x1 + 18, u.cy), (x1, u.cy)]
            continue
        pts = None if e.back else simple_route(layout, e)
        if pts is None:
            hard.append(e)
            continue
        e.points = pts
        drawn.extend(zip(pts, pts[1:]))
        for node, p in ((u, pts[0]), (v, pts[-1])):
            key = (node.id, side_of(node, p))
            port_use[key] = port_use.get(key, 0) + 1
    for e in sorted(hard, key=lambda e: (e.back, e.idx)):
        e.points = route_astar(g, g.nodes[e.src], g.nodes[e.dst], drawn, port_use, bounds)
        drawn.extend(zip(e.points, e.points[1:]))


def place_chips(layout: Layout) -> dict[int, Rect]:
    g = layout.graph
    placed: dict[int, Rect] = {}
    nodes = [inflate(n.rect, 3) for n in g.nodes.values()]
    for e in g.edges:
        if not e.label:
            continue
        _, cw, ch = layout.chips[e.idx]
        segs = list(zip(e.points, e.points[1:]))
        candidates = []
        ordered = sorted(segs, key=lambda s: -(abs(s[0][0] - s[1][0]) + abs(s[0][1] - s[1][1])))
        if not e.back and len(segs) > 1:
            ordered = [segs[-1]] + [sg for sg in ordered if sg is not segs[-1]]
        fractions = (0.5, 0.4, 0.6, 0.3, 0.7, 0.2, 0.8, 0.1, 0.9)
        for a, b in ordered:
            vertical = abs(a[0] - b[0]) < 1e-6
            for t in fractions:
                mx, my = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
                if vertical:
                    candidates.append((mx + cw / 2 + 6, my, 0))
                    candidates.append((mx - cw / 2 - 6, my, 0))
                else:
                    candidates.append((mx, my - ch / 2 - 4, 0))
                    candidates.append((mx, my + ch / 2 + 4, 0))
        for a, b in ordered:
            for t in fractions:
                candidates.append(((a[0] + (b[0] - a[0]) * t), (a[1] + (b[1] - a[1]) * t), 0))
        mids = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in ordered]
        ring = sorted(((dx, dy) for dx in range(-120, 121, 12) for dy in range(-70, 71, 10)),
                      key=lambda d: (math.hypot(*d), d))
        for mx, my in mids:  # last resort: the nearest free spot around the line
            candidates.extend((mx + dx, my + dy, 0) for dx, dy in ring)
        choice = None
        others = [seg for other in g.edges if other.idx != e.idx for seg in zip(other.points, other.points[1:])]
        for strict in (True, False):
            for cx, cy, _ in candidates:
                rect = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
                if any(overlaps(rect, n) for n in nodes) or any(overlaps(rect, other, 2) for other in placed.values()):
                    continue
                if strict and any(seg_hits_rect(a, b, inflate(rect, 1)) for a, b in others):
                    continue
                choice = rect
                break
            if choice is not None:
                break
        if choice is None:
            raise MermaidError(f"cannot place the label {e.label!r} without overlap")
        placed[e.idx] = tuple(round(c, 1) for c in choice)  # type: ignore[assignment]
    return placed


def group_rects(layout: Layout, check: bool = True) -> dict[str, Rect]:
    g = layout.graph
    rects: dict[str, Rect] = {}

    def members(sid: str) -> list[Node]:
        out = [n for n in g.nodes.values() if n.sub == sid]
        for child in g.subs.values():
            if child.parent == sid:
                out.extend(members(child.id))
        return out

    def depth(sid: str) -> int:
        return 0 if g.subs[sid].parent is None else 1 + depth(g.subs[sid].parent)

    for sid in sorted(g.subs, key=lambda s: -depth(s)):
        nodes = members(sid)
        if not nodes:
            continue
        child_rects = [rects[c.id] for c in g.subs.values() if c.parent == sid and c.id in rects]
        x0 = min([n.rect[0] for n in nodes] + [r[0] for r in child_rects]) - 16
        y0 = min([n.rect[1] for n in nodes] + [r[1] for r in child_rects]) - 34
        x1 = max([n.rect[2] for n in nodes] + [r[2] for r in child_rects]) + 16
        y1 = max([n.rect[3] for n in nodes] + [r[3] for r in child_rects]) + 16
        need = tw(g.subs[sid].title, 14, 700) + 28
        if x1 - x0 < need:
            x1 = x0 + need
        rects[sid] = (x0, y0, x1, y1)
    if not check:
        return rects
    for sid, rect in rects.items():
        inside = {n.id for n in g.nodes.values() if n.sub == sid}
        for child in g.subs.values():
            if child.parent == sid:
                inside |= {n.id for n in g.nodes.values() if n.sub == child.id}
        for n in g.nodes.values():
            if n.id not in inside and overlaps(inflate(n.rect, -1), rect):
                raise MermaidError(f"group {sid!r} overlaps node {n.id!r}")
    ids = list(rects)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            nested = g.subs[a].parent == b or g.subs[b].parent == a
            if not nested and overlaps(rects[a], rects[b]):
                raise MermaidError(f"groups {a!r} and {b!r} overlap")
    return rects


# =============================================================================
# Drawing
# =============================================================================
def esc(value: str) -> str:
    return html.escape(value, quote=True)


def rounded_path(points: list[Point], radius: float = 9.0) -> str:
    if len(points) == 2:
        (x1, y1), (x2, y2) = points
        return f"M{x1:g},{y1:g} L{x2:g},{y2:g}"
    d = [f"M{points[0][0]:g},{points[0][1]:g}"]
    for i in range(1, len(points) - 1):
        (ax, ay), (bx, by), (cx, cy) = points[i - 1], points[i], points[i + 1]
        r = min(radius, math.dist((ax, ay), (bx, by)) / 2, math.dist((bx, by), (cx, cy)) / 2)
        if r < 1:
            d.append(f"L{bx:g},{by:g}")
            continue
        l1, l2 = math.dist((ax, ay), (bx, by)), math.dist((bx, by), (cx, cy))
        p1 = (bx + (ax - bx) / l1 * r, by + (ay - by) / l1 * r)
        p2 = (bx + (cx - bx) / l2 * r, by + (cy - by) / l2 * r)
        d.append(f"L{p1[0]:.1f},{p1[1]:.1f} Q{bx:g},{by:g} {p2[0]:.1f},{p2[1]:.1f}")
    d.append(f"L{points[-1][0]:g},{points[-1][1]:g}")
    return " ".join(d)


def node_kind(g: Graph, node: Node) -> str:
    if node.shape in {"start", "end"}:
        return "navy"
    if node.cls and node.cls in g.classdefs:
        return KINDS[g.classdefs.index(node.cls) % len(KINDS)]
    return "gold" if node.shape == "diamond" else "teal"


def draw_node(f: fk.Fig, g: Graph, n: Node) -> None:
    fill, stroke, ink = fk.PALETTE[node_kind(g, n)]
    x0, y0, x1, y1 = n.rect
    attrs = f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"'
    shift = 0.0
    if n.shape == "diamond":
        f.parts.append(f'<polygon points="{n.cx:g},{y0:g} {x1:g},{n.cy:g} {n.cx:g},{y1:g} {x0:g},{n.cy:g}" {attrs}/>')
    elif n.shape == "start":
        f.parts.append(f'<circle cx="{n.cx:g}" cy="{n.cy:g}" r="11" fill="#102a43" stroke="#102a43" stroke-width="1.6"/>')
        return
    elif n.shape == "end":
        f.parts.append(f'<circle cx="{n.cx:g}" cy="{n.cy:g}" r="12" fill="#ffffff" stroke="#102a43" stroke-width="1.6"/>'
                       f'<circle cx="{n.cx:g}" cy="{n.cy:g}" r="7" fill="#102a43"/>')
        return
    elif n.shape == "circle":
        f.parts.append(f'<ellipse cx="{n.cx:g}" cy="{n.cy:g}" rx="{n.w / 2:g}" ry="{n.h / 2:g}" {attrs}/>')
    elif n.shape == "cyl":
        w, h = n.w, n.h
        f.parts.append(f'<path d="M{x0:g},{y0 + 7:g} v{h - 14:g} a{w / 2:g},7 0 0 0 {w:g},0 v{-(h - 14):g}" {attrs}/>'
                       f'<ellipse cx="{n.cx:g}" cy="{y0 + 7:g}" rx="{w / 2:g}" ry="7" {attrs}/>')
        shift = 7.0
    else:
        radius = {"round": 18, "stadium": n.h / 2}.get(n.shape, 10)
        f.parts.append(f'<rect x="{x0:g}" y="{y0:g}" width="{n.w:g}" height="{n.h:g}" rx="{min(radius, n.h / 2):g}" {attrs}/>')
        if n.shape == "sub":
            for x in (x0 + 8, x1 - 8):
                f.parts.append(f'<line x1="{x:g}" y1="{y0:g}" x2="{x:g}" y2="{y1:g}" stroke="{stroke}" stroke-width="1.6"/>')
    top = n.cy + shift / 2 - len(n.lines) * LINE_H / 2 + FS * 0.92
    f.text(n.cx, round(top, 1), "\n".join(n.lines), FS, "middle", 400, ink)


def draw_edge(f: fk.Fig, e: Edge) -> None:
    color = RETURN if e.back else ARROW
    dash = ' stroke-dasharray="7 5"' if (e.back or e.style == "dotted") else ""
    width = 3.0 if e.style == "thick" else 1.8
    marker = (' marker-end="url(#arrow-coral)"' if e.back else ' marker-end="url(#arrow)"') if e.arrow else ""
    if e.both:
        marker += ' marker-start="url(#arrow)"'
    f.parts.append(f'<path d="{rounded_path(e.points)}" fill="none" stroke="{color}" stroke-width="{width:g}"{dash}{marker}/>')


def draw_chip(f: fk.Fig, rect: Rect, lines: list[str], back: bool) -> None:
    x0, y0, x1, y1 = rect
    f.parts.append(f'<rect x="{x0:g}" y="{y0:g}" width="{x1 - x0:g}" height="{y1 - y0:g}" rx="4" fill="#ffffff"/>')
    first = y0 + 3 + LFS * 0.92
    f.text((x0 + x1) / 2, round(first, 1), "\n".join(lines), LFS, "middle", 400, "#5c1f14" if back else "#142231")


@dataclass
class Rendered:
    svg: str
    title: str
    alt: str
    desc: str
    reading: str
    width: int
    height: int
    texts: list[tuple[Rect, list[str], float, str]] = field(default_factory=list)  # node rect, lines, size, shape


def quoted(label: str) -> str:
    return "«" + " ".join(label.split()) + "»"


def join_es(items: list[str]) -> str:
    if len(items) <= 1:
        return "".join(items)
    return ", ".join(items[:-1]) + " y " + items[-1]


def render_graph(g: Graph) -> Rendered:
    ranks, chips = prepare(g)
    error: MermaidError | None = None
    branching = max(len(r) for r in ranks) >= 2 and g.direction in {"LR", "RL"}
    for reserve in (0.0, 70.0):
        for mode in ("row", "down", "wrap"):
            if mode == "down" and not branching:
                continue
            for max_w in (WRAP_WIDTHS if mode == "wrap" else NODE_WIDTHS):
                layout = build_layout(g, ranks, chips, max_w, mode, reserve)
                if layout is None:
                    continue
                try:
                    return finish_graph(g, layout)
                except MermaidError as exc:
                    error = exc
    raise error or MermaidError("diagram does not fit the reading width")


def finish_graph(g: Graph, layout: Layout) -> Rendered:
    route_all(layout)
    chip_rects = place_chips(layout)
    groups = group_rects(layout) if g.subs else {}
    min_x = min_y = math.inf
    max_x = max_y = -math.inf

    def grow(x0: float, y0: float, x1: float, y1: float) -> None:
        nonlocal min_x, min_y, max_x, max_y
        min_x, min_y, max_x, max_y = min(min_x, x0), min(min_y, y0), max(max_x, x1), max(max_y, y1)

    for n in g.nodes.values():
        grow(*n.rect)
    for r in groups.values():
        grow(*r)
    for e in g.edges:
        for x, y in e.points:
            grow(x - 2, y - 2, x + 2, y + 2)
    for r in chip_rects.values():
        grow(*r)
    width = math.ceil(max_x - min_x + 2 * PAD)
    height = math.ceil(max_y - min_y + 2 * PAD)
    dx, dy = PAD - min_x, PAD - min_y
    if width > MAX_W + 2:
        raise MermaidError(f"diagram is {width}px wide (limit {MAX_W})")

    def shift(p: Point) -> Point:
        return (round(p[0] + dx, 1), round(p[1] + dy, 1))

    for n in g.nodes.values():
        n.cx, n.cy = round(n.cx + dx, 1), round(n.cy + dy, 1)
    for e in g.edges:
        e.points = [shift(p) for p in e.points]
    groups = {sid: (round(r[0] + dx, 1), round(r[1] + dy, 1), round(r[2] + dx, 1), round(r[3] + dy, 1)) for sid, r in groups.items()}
    chip_rects = {i: (round(r[0] + dx, 1), round(r[1] + dy, 1), round(r[2] + dx, 1), round(r[3] + dy, 1)) for i, r in chip_rects.items()}

    title, alt, desc, reading = describe_graph(g, layout)
    f = fk.Fig(width, height, title, desc)
    for sid in sorted(groups, key=lambda s: groups[s][0]):
        x0, y0, x1, y1 = groups[sid]
        f.group(x0, y0, x1 - x0, y1 - y0, g.subs[sid].title)
    for e in sorted(g.edges, key=lambda e: e.back):
        draw_edge(f, e)
    texts = []
    for n in g.nodes.values():
        draw_node(f, g, n)
        if n.lines:
            texts.append((n.rect, n.lines, FS, n.shape))
    for e in g.edges:
        if e.label:
            draw_chip(f, chip_rects[e.idx], layout.chips[e.idx][0], e.back)
    return Rendered(f.svg(), title, alt, desc, reading, width, height, texts)


def describe_graph(g: Graph, layout: Layout) -> tuple[str, str, str, str]:
    named = [n for n in g.nodes.values() if n.shape not in {"start", "end"}]
    ordered = sorted(g.nodes.values(), key=lambda n: (n.rank, n.pos))
    by_rank: list[list[str]] = []
    for n in ordered:
        if n.shape in {"start", "end"}:
            continue
        while len(by_rank) <= n.rank:
            by_rank.append([])
        by_rank[n.rank].append(quoted(n.label))
    steps = [join_es(r) for r in by_rank if r]
    noun = "estados" if g.kind == "state" else "pasos"
    kind = "Diagrama de estados" if g.kind == "state" else "Diagrama de flujo"
    returns = [e for e in g.edges if e.back]
    decisions = [n for n in g.nodes.values() if n.shape == "diamond"]

    def edge_text(e: Edge) -> str:
        a = "inicio" if g.nodes[e.src].shape == "start" else "fin" if g.nodes[e.src].shape == "end" else quoted(g.nodes[e.src].label)
        b = "fin" if g.nodes[e.dst].shape == "end" else "inicio" if g.nodes[e.dst].shape == "start" else quoted(g.nodes[e.dst].label)
        tail = f" ({e.label})" if e.label else ""
        return f"{a} lleva a {b}{tail}"

    alt = f"{kind} con {len(named)} {noun}. Recorrido: " + "; luego ".join(steps) + "."
    if returns:
        alt += " Retornos: " + "; ".join(edge_text(e) for e in returns) + "."
    if len(alt) > 650:
        alt = (f"{kind} con {len(named)} {noun}, de {steps[0]} a {steps[-1]}"
               + (f", con {len(returns)} retorno(s)" if returns else "") + ".")
    alt = re.sub(r"[\[\]\"]", "", alt.replace("|", "/"))
    desc = f"{kind} con {len(named)} {noun}. " + ". ".join(edge_text(e) for e in g.edges) + "."
    desc = re.sub(r"\s+", " ", desc)
    first, last = steps[0], steps[-1]
    title = f"{kind}: " + (first if len(steps) == 1 else f"{first} … {last}")
    title = re.sub(r"[\[\]\"]", "", title)
    sources = [n for n in named if not any(e.dst == n.id and not e.back for e in g.edges)]
    reading = f"**Cómo leer el diagrama:** empieza en {join_es([quoted(n.label) for n in sources[:3]])} y sigue las flechas"
    reading += " hasta el final del recorrido." if not returns else " hasta el final del recorrido."
    if layout.k and layout.rows > 1:
        reading += " Las filas se leen como una serpentina: de izquierda a derecha y, en la fila siguiente, de derecha a izquierda."
    if decisions:
        reading += " Los rombos son decisiones: cada salida lleva escrito su criterio."
    if returns:
        reading += " Las flechas discontinuas de color coral son retornos: " + "; ".join(edge_text(e) for e in returns) + "."
    return title, alt, desc, reading


# -- sequence --------------------------------------------------------------------
def render_sequence(seq: Sequence) -> Rendered:
    names = seq.names
    count = len(names)
    heads = {}
    for name in names:
        lines = wrap(seq.labels[name], FS, 170)
        heads[name] = (lines, max(110, math.ceil(max(tw(x) for x in lines) + 26)))
    head_h = max(len(lines) for lines, _ in heads.values()) * LINE_H + 20
    gaps = [(heads[names[i]][1] + heads[names[i + 1]][1]) / 2 + 26 for i in range(count - 1)]
    index = {n: i for i, n in enumerate(names)}
    wrapped: dict[int, list[str]] = {}
    for n, item in enumerate(seq.items):
        wrapped[n] = wrap(item.text, LFS, 230)
    spans = []
    for n, item in enumerate(seq.items):
        a, b = sorted((index[item.a], index[item.b]))
        need = max(tw(x, LFS) for x in wrapped[n]) + 34
        if item.kind == "message" and a == b:
            continue
        spans.append((b - a, a, b, need))
    for span, a, b, need in sorted(spans):
        if span and sum(gaps[a:b]) < need:
            add = (need - sum(gaps[a:b])) / span
            for i in range(a, b):
                gaps[i] += add
    left = heads[names[0]][1] / 2
    xs = [left]
    for gap in gaps:
        xs.append(xs[-1] + gap)
    right_extra = 0.0
    for n, item in enumerate(seq.items):
        if item.kind == "message" and item.a == item.b and index[item.a] == count - 1:
            right_extra = max(right_extra, 46 + max(tw(x, LFS) for x in wrapped[n]) - (gaps[-1] / 2 if gaps else 0))
    total = xs[-1] + heads[names[-1]][1] / 2 + max(right_extra, 0)
    if total + 2 * PAD > MAX_W + 2:
        raise MermaidError(f"sequence diagram is {math.ceil(total + 2 * PAD)}px wide (limit {MAX_W})")
    y = PAD + head_h + 18
    rows = []
    for n, item in enumerate(seq.items):
        lines = wrapped[n]
        h = len(lines) * LLINE_H + (20 if item.kind == "message" else 22)
        rows.append((y, h))
        y += h + 12
    bottom = y + 6
    width = math.ceil(total + 2 * PAD)
    height = math.ceil(bottom + PAD)
    title = "Diagrama de secuencia: " + " → ".join(seq.labels[n] for n in names[:4]) + (" …" if count > 4 else "")
    title = re.sub(r"[\[\]\"]", "", title)
    steps = []
    for item in seq.items:
        if item.kind == "message":
            steps.append(f"{seq.labels[item.a]} envía a {seq.labels[item.b]}: {item.text}" if item.a != item.b
                         else f"{seq.labels[item.a]} se autoenvía: {item.text}")
        else:
            steps.append(f"Nota sobre {seq.labels[item.a]}: {item.text}")
    desc = re.sub(r"\s+", " ", f"Diagrama de secuencia con {count} participantes y {len(seq.items)} eventos en orden. " + ". ".join(steps) + ".")
    alt = f"Diagrama de secuencia entre {join_es([seq.labels[n] for n in names])}, con {len(seq.items)} eventos de arriba abajo. " \
          + "; luego ".join(steps[:8]) + ("." if len(steps) <= 8 else "; y así hasta " + steps[-1] + ".")
    alt = re.sub(r"[\[\]\"]", "", alt.replace("|", "/"))
    if len(alt) > 700:
        alt = f"Diagrama de secuencia entre {join_es([seq.labels[n] for n in names])}, con {len(seq.items)} eventos de arriba abajo."
    reading = ("**Cómo leer el diagrama:** cada columna es un participante y el tiempo avanza hacia abajo; "
               "las flechas continuas son mensajes, las discontinuas son respuestas y los recuadros amarillos son notas.")
    f = fk.Fig(width, height, title, desc)
    texts = []
    for name, x in zip(names, xs):
        lines, w = heads[name]
        x0 = PAD + x - w / 2
        f.parts.append(f'<rect x="{x0:g}" y="{PAD:g}" width="{w:g}" height="{head_h:g}" rx="10" fill="#102a43" stroke="#102a43" stroke-width="1.6"/>')
        f.text(PAD + x, round(PAD + (head_h - len(lines) * LINE_H) / 2 + FS * 0.92, 1), "\n".join(lines), FS, "middle", 700, "#ffffff")
        texts.append(((x0, PAD, x0 + w, PAD + head_h), lines, FS, "rect"))
        f.parts.append(f'<line x1="{PAD + x:g}" y1="{PAD + head_h:g}" x2="{PAD + x:g}" y2="{bottom:g}" stroke="#8a9aa3" stroke-width="1.4" stroke-dasharray="5 4"/>')
    for n, (item, (top, h)) in enumerate(zip(seq.items, rows)):
        lines = wrapped[n]
        xa, xb = PAD + xs[index[item.a]], PAD + xs[index[item.b]]
        if item.kind == "note":
            lo, hi = min(xa, xb) - 18, max(xa, xb) + 18
            need = max(tw(x, LFS) for x in lines) + 20
            if hi - lo < need:
                mid = (lo + hi) / 2
                lo, hi = mid - need / 2, mid + need / 2
            f.parts.append(f'<rect x="{lo:g}" y="{top:g}" width="{hi - lo:g}" height="{h:g}" rx="6" fill="#f7ebc8" stroke="#a8761a" stroke-width="1.6"/>')
            f.text((lo + hi) / 2, round(top + (h - len(lines) * LLINE_H) / 2 + LFS * 0.92, 1), "\n".join(lines), LFS, "middle", 400, "#4a3209")
            texts.append(((lo, top, hi, top + h), lines, LFS, "rect"))
            continue
        ay = top + h - 8
        color = ARROW
        dash = ' stroke-dasharray="6 4"' if item.dashed else ""
        marker = ' marker-end="url(#arrow)"' if item.arrow else ""
        label_y = round(top + LFS * 0.92 + 1, 1)
        if item.a == item.b:
            f.parts.append(f'<path d="M{xa:g},{ay - 14:g} H{xa + 40:g} V{ay:g} H{xa:g}" fill="none" stroke="{color}" stroke-width="1.8"{dash}{marker}/>')
            f.text(xa + 48, label_y, "\n".join(lines), LFS, "start", 400, "#142231")
        else:
            f.parts.append(f'<line x1="{xa:g}" y1="{ay:g}" x2="{xb:g}" y2="{ay:g}" stroke="{color}" stroke-width="1.8"{dash}{marker}/>')
            f.text((xa + xb) / 2, label_y, "\n".join(lines), LFS, "middle", 400, "#142231")
    return Rendered(f.svg(), title, alt, desc, reading, width, height, texts)


# =============================================================================
# Public API
# =============================================================================
def normalise(source: str) -> str:
    return "\n".join(line.rstrip() for line in source.replace("\r\n", "\n").strip("\n").split("\n"))


def figure_name(source: str) -> str:
    digest = hashlib.sha256(normalise(source).encode("utf-8")).hexdigest()[:10]
    return f"mermaid-{digest}.svg"


@lru_cache(maxsize=None)
def _render_cached(normalised: str) -> Rendered:
    parsed = parse(normalised)
    if isinstance(parsed, Sequence):
        return render_sequence(parsed)
    return render_graph(parsed)


def fit_problems(rendered: Rendered) -> list[str]:
    """Text that would overflow its node (estimated with the figure kit's glyph metric)."""
    problems = []
    for (x0, y0, x1, y1), lines, size, shape in rendered.texts:
        height = len(lines) * size * 1.28
        if height > (y1 - y0) - 6:
            problems.append(f"{lines[0]!r}: {len(lines)} lines need {height:.0f}px of {y1 - y0:.0f}px")
        for i, line in enumerate(lines):
            half = tw(line, size) / 2
            if shape == "diamond":
                dy = abs((i - (len(lines) - 1) / 2) * size * 1.28) + size * 0.64
                if half / ((x1 - x0) / 2) + dy / ((y1 - y0) / 2) > 1.0:
                    problems.append(f"{line!r} leaves its diamond")
            elif 2 * half > (x1 - x0) - 10:
                problems.append(f"{line!r}: {2 * half:.0f}px in a {x1 - x0:.0f}px node")
    if rendered.width > MAX_W + 2:
        problems.append(f"width {rendered.width} > {MAX_W}")
    return problems


def render(source: str) -> Rendered:
    try:
        rendered = _render_cached(normalise(source))
        problems = fit_problems(rendered)
        if problems:
            raise MermaidError("text does not fit: " + "; ".join(problems[:3]))
        return rendered
    except MermaidError as error:
        first = normalise(source).split("\n", 1)[0]
        raise MermaidError(f"{error} (diagram starting with {first!r})") from error


BLOCK_RE = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)
PROSE_BLOCKERS = ("#", "-", "*", "|", ">", "!", "`", "<", "1.", "---")
REGISTRY: dict[Path, str] = {}


def mermaid_blocks(markdown: str) -> list[str]:
    return [m.group(1) for m in BLOCK_RE.finditer(markdown.replace("\r\n", "\n"))]


def register(source: str) -> str:
    """Render ``source`` and record its SVG under site/assets/figures; return the file name."""
    name = figure_name(source)
    REGISTRY[FIGURES_DIR / name] = render(source).svg
    return name


def registered_files() -> dict[Path, str]:
    return dict(sorted(REGISTRY.items(), key=lambda item: item[0].as_posix()))


def _has_reading_paragraph(rest: str) -> bool:
    for line in rest.split("\n"):
        text = line.strip()
        if text:
            return not text.startswith(PROSE_BLOCKERS)
    return False


def publish_markdown(markdown: str, doc_dir: Path) -> str:
    """Replace every mermaid block by an image of its SVG (and a reading paragraph if none follows)."""
    text = markdown.replace("\r\n", "\n")
    rel_dir = Path(os.path.relpath(FIGURES_DIR, doc_dir)).as_posix()
    out: list[str] = []
    cursor = 0
    for m in BLOCK_RE.finditer(text):
        source = m.group(1)
        rendered = render(source)
        name = register(source)
        image = f"![{rendered.alt}]({rel_dir}/{name})"
        out.append(text[cursor:m.start()])
        out.append(image)
        cursor = m.end()
        if not _has_reading_paragraph(text[cursor:]):
            out.append("\n\n" + rendered.reading)
    out.append(text[cursor:])
    return "".join(out)


def caption_for(file_name: str) -> str:
    """Short visible caption of a published diagram (its SVG title), for the portal."""
    path = FIGURES_DIR / file_name
    svg = REGISTRY.get(path) or (path.read_text(encoding="utf-8") if path.is_file() else "")
    m = re.search(r'<title id="t">(.*?)</title>', svg)
    return html.unescape(m.group(1)) if m else ""


def portal_figure(source: str) -> str:
    """HTML for the portal: the same SVG as an image, no code text."""
    rendered = render(source)
    name = register(source)
    return (
        '<figure class="lesson-figure">'
        f'<img src="../assets/figures/{name}" alt="{esc(rendered.alt)}" loading="lazy">'
        f'<figcaption aria-hidden="true">{esc(rendered.title)}</figcaption></figure>'
    )


def main() -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Render the mermaid blocks of Markdown files to SVG files.")
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--out", type=Path, required=True, help="directory for the SVG files")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    total = 0
    for path in args.files:
        for n, source in enumerate(mermaid_blocks(path.read_text(encoding="utf-8")), 1):
            rendered = render(source)
            target = args.out / f"{path.stem}-{n}-{figure_name(source)}"
            target.write_text(rendered.svg, encoding="utf-8", newline="\n")
            print(target, rendered.width, rendered.height)
            total += 1
    print(f"MERMAID_RENDER_OK: {total}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
