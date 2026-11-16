"""Laboratorio común de la Parte 40: el núcleo de *Avisos*, sus mutantes y varios oráculos.

Todo se ejecuta de verdad con la biblioteca estándar; no se invoca ningún modelo de lenguaje.
`due_reminders` es el código bajo prueba. Un *mutante* es una copia del código con un cambio
mínimo (un operador, un umbral, una condición); un oráculo «mata» al mutante si falla con él.
"""
from __future__ import annotations

import importlib.util
import random
import tempfile
import time
from pathlib import Path

OFFSETS = (72, 24, 1)

SOURCE = '''
OFFSETS = (72, 24, 1)

def due_reminders(deliveries, now, silenced, sent):
    out = []
    for d in deliveries:
        if d["submitted"]:
            continue
        remaining = d["due"] - now
        if remaining <= 0:
            continue
        done = [o for (i, o) in sent if i == d["id"]]
        pending = [o for o in OFFSETS if remaining <= o and not any(s <= o for s in done)]
        if not pending:
            continue
        offset = min(pending)
        if (d["student"], d["course"]) in silenced and offset != 1:
            continue
        out.append((d["id"], offset))
    return out
'''

# (nombre, texto original, texto mutado, descripción, equivalente)
MUTANTS = [
    ("M01", 'if remaining <= 0:', 'if remaining < 0:', "avisa en el instante exacto del vencimiento", False),
    ("M02", 'remaining <= o and', 'remaining < o and', "no avisa cuando faltan exactamente 72, 24 o 1 horas", False),
    ("M03", 'if d["submitted"]:\n            continue', 'if False:\n            continue', "avisa a quien ya entregó", False),
    ("M04", 'offset = min(pending)', 'offset = max(pending)', "envía el aviso más antiguo en vez del más urgente", False),
    ("M05", 'not any(s <= o for s in done)', 'not any(s < o for s in done)', "repite el aviso ya enviado", False),
    ("M06", 'offset != 1', 'offset != 24', "el silencio deja pasar el de 24 horas y bloquea el de 1", False),
    ("M07", 'if (d["student"], d["course"]) in silenced and offset != 1:', 'if False:', "ignora el silencio", False),
    ("M08", '(d["student"], d["course"]) in silenced', 'd["student"] in [s for s, c in silenced]', "silencia a la persona en todos sus cursos", False),
    ("M09", 'OFFSETS = (72, 24, 1)', 'OFFSETS = (72, 24, 2)', "cambia el último aviso a 2 horas", False),
    ("M10", 'if not pending:\n            continue', 'if False:\n            continue', "falla con una lista vacía", False),
    ("M11", 'if i == d["id"]]', 'if i != d["id"]]', "mira los envíos de otras entregas", False),
    ("M12", 'not any(s <= o for s in done)', 'not any(s >= o for s in done)', "invierte la comparación de avisos ya enviados", False),
    ("M13", 'remaining = d["due"] - now', 'remaining = now - d["due"]', "invierte el signo del tiempo restante", False),
    ("M14", 'in silenced and offset != 1', 'in silenced or offset != 1', "silencia todo si el curso está silenciado o el aviso no es el último", False),
    ("M15", 'if d["submitted"]:', 'if not d["submitted"]:', "avisa solo a quien ya entregó", False),
    ("M16", 'remaining <= o and', 'remaining <= o + 1 and', "avisa una hora antes de lo debido", False),
    ("M17", 'out.append((d["id"], offset))', 'out.append((d["student"], offset))', "devuelve el estudiante en vez de la entrega", False),
    ("M18", 'offset = min(pending)', 'offset = pending[0]', "toma el primero de la lista, que es el más antiguo", False),
    ("M19", 'OFFSETS = (72, 24, 1)', 'OFFSETS = (72, 1, 24)', "reordena los umbrales (equivalente: se usa min)", True),
    ("M20", 'offset != 1', 'offset > 1', "cambia != por > (equivalente: los umbrales son 72, 24, 1)", True),
]


_COUNTER = [0]


def load_module(source: str):
    """Carga un texto de Python como módulo desde un archivo temporal (sin `exec`)."""
    _COUNTER[0] += 1
    name = f"avisos_variante_{_COUNTER[0]}"
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / f"{name}.py"
        path.write_text(source, encoding="utf-8", newline="\n")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    return module


def load(source: str):
    return load_module(source).due_reminders


def mutant_source(name: str) -> str:
    for mutant_id, old, new, _desc, _eq in MUTANTS:
        if mutant_id == name:
            assert old in SOURCE, name
            return SOURCE.replace(old, new, 1)
    raise KeyError(name)


def all_versions() -> dict[str, object]:
    versions = {"ORIGINAL": load(SOURCE)}
    for mutant_id, *_ in MUTANTS:
        versions[mutant_id] = load(mutant_source(mutant_id))
    return versions


def delivery(id_, due, student="e1", course="c1", submitted=False):
    return {"id": id_, "student": student, "course": course, "due": due, "submitted": submitted}


def run_timeline(fn, deliveries, silenced=frozenset(), start=0, end=100, step=1, down=()):
    """Llama a fn cada `step` horas; registra (hora, entrega, umbral). Equivale a un cron."""
    sent: set = set()
    log = []
    t = start
    while t <= end:
        if t not in down:
            for item in fn(deliveries, t, silenced, sent):
                log.append((t, item[0], item[1]))
                sent |= {(item[0], o) for o in OFFSETS if o >= item[1]}
        t += step
    return log


# ----------------------------------------------------------------- oráculos
def oracle_smoke(fn) -> bool:
    """Un único caso feliz: avisa a las 24 horas."""
    return fn([delivery("a", 100)], 76, frozenset(), set()) == [("a", 24)]


TDD_TESTS = []


def _tdd(f):
    TDD_TESTS.append(f)
    return f


@_tdd
def t01_sin_aviso_lejos(fn):
    assert fn([delivery("a", 200)], 0, frozenset(), set()) == []


@_tdd
def t02_aviso_72(fn):
    assert fn([delivery("a", 100)], 28, frozenset(), set()) == [("a", 72)]


@_tdd
def t03_no_repite(fn):
    assert fn([delivery("a", 100)], 28, frozenset(), {("a", 72)}) == []


@_tdd
def t04_entregada_no_avisa(fn):
    assert fn([delivery("a", 100, submitted=True)], 99, frozenset(), set()) == []


@_tdd
def t05_vencida_no_avisa(fn):
    assert fn([delivery("a", 100)], 101, frozenset(), set()) == []


@_tdd
def t06_caida_solo_el_urgente(fn):
    assert fn([delivery("a", 100)], 90, frozenset(), set()) == [("a", 24)]


@_tdd
def t07_silencio_deja_pasar_la_ultima_hora(fn):
    sil = frozenset({("e1", "c1")})
    assert fn([delivery("a", 100)], 99, sil, set()) == [("a", 1)]
    assert fn([delivery("a", 100)], 90, sil, set()) == []


@_tdd
def t08_silencio_es_por_curso(fn):
    sil = frozenset({("e1", "c1")})
    assert fn([delivery("a", 100, course="c2")], 90, sil, set()) == [("a", 24)]


def oracle_tdd(fn, count: int | None = None) -> bool:
    """Devuelve True si TODAS las pruebas pasan (el mutante sobrevive)."""
    for test in TDD_TESTS[: count if count is not None else len(TDD_TESTS)]:
        try:
            test(fn)
        except Exception:  # noqa: BLE001 - cualquier fallo mata al mutante
            return False
    return True


def oracle_acceptance(fn) -> bool:
    """Escenarios de aceptación con el reloj corriendo, sin mirar el interior."""
    try:
        log = run_timeline(fn, [delivery("a", 100)], end=110)
        assert log == [(28, "a", 72), (76, "a", 24), (99, "a", 1)], log
        log = run_timeline(fn, [delivery("a", 100, submitted=True)], end=110)
        assert log == [], log
        log = run_timeline(fn, [delivery("a", 100)], end=110, down=range(0, 90))
        assert log == [(90, "a", 24), (99, "a", 1)], log
        sil = frozenset({("e1", "c1")})
        log = run_timeline(fn, [delivery("a", 100)], sil, end=110)
        assert log == [(99, "a", 1)], log
        log = run_timeline(fn, [delivery("a", 100), delivery("b", 100, course="c2")], sil, end=110)
        assert [(t, i, o) for t, i, o in log if i == "b"] == [(28, "b", 72), (76, "b", 24), (99, "b", 1)], log
    except Exception:  # noqa: BLE001
        return False
    return True


def random_state(rng: random.Random):
    n = rng.randint(1, 4)
    deliveries = []
    for k in range(n):
        deliveries.append(delivery(f"d{k}", rng.randint(0, 120), student=rng.choice(["e1", "e2"]),
                                   course=rng.choice(["c1", "c2"]), submitted=rng.random() < 0.25))
    now = rng.randint(0, 120)
    silenced = frozenset((s, c) for s in ("e1", "e2") for c in ("c1", "c2") if rng.random() < 0.3)
    sent = set()
    for d in deliveries:
        for o in OFFSETS:
            if rng.random() < 0.2:
                sent.add((d["id"], o))
    return deliveries, now, silenced, sent


def check_contract(fn, deliveries, now, silenced, sent) -> None:
    """Postcondiciones de la especificación; no calcula la respuesta esperada."""
    out = fn(deliveries, now, silenced, sent)
    ids = [i for i, _ in out]
    assert len(ids) == len(set(ids)), "más de un aviso por entrega"
    by_id = {d["id"]: d for d in deliveries}
    for i, offset in out:
        d = by_id[i]
        remaining = d["due"] - now
        assert not d["submitted"], "avisó a quien ya entregó"
        assert remaining > 0, "avisó tras el vencimiento"
        assert offset in OFFSETS and remaining <= offset, "umbral inválido"
        assert not any(s <= offset for (j, s) in sent if j == i), "repite o retrocede"
        if (d["student"], d["course"]) in silenced:
            assert offset == 1, "avisó en un curso silenciado"


def oracle_contract(fn, n: int = 400, seed: int = 40) -> bool:
    rng = random.Random(seed)
    try:
        for _ in range(n):
            check_contract(fn, *random_state(rng))
    except Exception:  # noqa: BLE001
        return False
    return True


def reference(deliveries, now, silenced, sent):
    """Especificación ejecutable escrita aparte, con una tabla de reglas en vez de listas."""
    result = []
    for d in deliveries:
        remaining = d["due"] - now
        if d["submitted"] or remaining <= 0:
            continue
        sent_here = {o for (i, o) in sent if i == d["id"]}
        floor = min(sent_here) if sent_here else 10**9
        candidates = [o for o in (1, 24, 72) if remaining <= o and o < floor]
        if not candidates:
            continue
        offset = candidates[0]
        if (d["student"], d["course"]) in silenced and offset != 1:
            continue
        result.append((d["id"], offset))
    return result


def oracle_differential(fn, n: int = 400, seed: int = 41) -> bool:
    rng = random.Random(seed)
    try:
        for _ in range(n):
            state = random_state(rng)
            assert fn(*state) == reference(*state)
    except Exception:  # noqa: BLE001
        return False
    return True


ORACLES = {
    "Caso feliz": oracle_smoke,
    "Ocho pruebas TDD": oracle_tdd,
    "Escenarios de aceptación": oracle_acceptance,
    "Contrato con 400 estados": oracle_contract,
    "Modelo de referencia": oracle_differential,
}


def kill_matrix(oracles=None):
    oracles = oracles or ORACLES
    versions = all_versions()
    matrix = {}
    for name, fn in versions.items():
        if name == "ORIGINAL":
            continue
        matrix[name] = {label: (not oracle(fn)) for label, oracle in oracles.items()}
    base = {label: oracle(versions["ORIGINAL"]) for label, oracle in oracles.items()}
    return matrix, base


def timed(callable_, repeat: int = 5) -> float:
    best = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        callable_()
        elapsed = time.perf_counter() - t0
        best = elapsed if best is None else min(best, elapsed)
    return best * 1000
