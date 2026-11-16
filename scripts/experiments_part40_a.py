"""Experimentos de las clases SE-481 a SE-486 (Parte 40): metodologías de desarrollo.

Uso: python scripts/experiments_part40_a.py [481|482|483|484|485|486]

No se invoca ningún modelo de lenguaje. Todo es código ejecutado de verdad con la biblioteca
estándar sobre el núcleo de *Avisos* (`experiments_part40_lab.py`): mutantes, oráculos, un ciclo
rojo-verde-refactor, dos estilos de pruebas, un ejecutor de escenarios y un recuento léxico del corpus.
"""
from __future__ import annotations

import itertools
import re
import sys
import unittest.mock as um
from pathlib import Path

import experiments_part40_lab as L


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


def pct(x, d=1):
    return f"{100 * x:.{d}f} %".replace(".", ",")


REAL = [m for m in L.MUTANTS if not m[4]]
REAL_IDS = [m[0] for m in REAL]


# ====================================================================== SE-481
def e481():
    print("SE-481 — mapa de metodologías: qué mutantes mata cada tipo de oráculo")
    matrix, base = L.kill_matrix()
    labels = list(L.ORACLES)
    print("  todos los oráculos pasan con el original:", all(base.values()))
    print("  mutantes:", len(L.MUTANTS), "de los cuales equivalentes:", sum(m[4] for m in L.MUTANTS))
    rows = [["Oráculo", "Mata", "Solo él", "Tiempo (ms)"]]
    versions = L.all_versions()
    for label in labels:
        killed = {k for k in REAL_IDS if matrix[k][label]}
        others = {k for k in REAL_IDS if any(matrix[k][o] for o in labels if o != label)}
        ms = L.timed(lambda lab=label: L.ORACLES[lab](versions["ORIGINAL"]))
        rows.append([label, f"{len(killed)} de {len(REAL_IDS)}", len(killed - others), f"{ms:.2f}"])
    table(rows)
    survivors = [k for k in REAL_IDS if not any(matrix[k].values())]
    print("  mutantes no equivalentes que ningún oráculo mata:", survivors)
    print("  equivalentes (sobreviven a todos):", [m[0] for m in L.MUTANTS if m[4]], [not any(matrix[m[0]].values()) for m in L.MUTANTS if m[4]])
    print("  por parejas (unión de muertes):")
    pairs = []
    for a, b in itertools.combinations(labels, 2):
        n = sum(1 for k in REAL_IDS if matrix[k][a] or matrix[k][b])
        pairs.append((n, a, b))
    for n, a, b in sorted(pairs, reverse=True)[:5]:
        print(f"    {a} + {b}: {n} de {len(REAL_IDS)}")
    print("  los que no mata cada oráculo:")
    for label in labels:
        print(f"    {label}: {[k for k in REAL_IDS if not matrix[k][label]]}")


# ====================================================================== SE-482
V0 = "def due_reminders(deliveries, now, silenced, sent):\n    return []\n"
V1 = '''def due_reminders(deliveries, now, silenced, sent):
    out = []
    for d in deliveries:
        if d["due"] - now <= 72:
            out.append((d["id"], 72))
    return out
'''
V2 = '''def due_reminders(deliveries, now, silenced, sent):
    out = []
    for d in deliveries:
        if d["due"] - now <= 72 and (d["id"], 72) not in sent:
            out.append((d["id"], 72))
    return out
'''
V3 = '''def due_reminders(deliveries, now, silenced, sent):
    out = []
    for d in deliveries:
        if d["submitted"]:
            continue
        if d["due"] - now <= 72 and (d["id"], 72) not in sent:
            out.append((d["id"], 72))
    return out
'''
V4 = '''def due_reminders(deliveries, now, silenced, sent):
    out = []
    for d in deliveries:
        if d["submitted"] or d["due"] - now <= 0:
            continue
        if d["due"] - now <= 72 and (d["id"], 72) not in sent:
            out.append((d["id"], 72))
    return out
'''
V5 = L.SOURCE.replace('        if (d["student"], d["course"]) in silenced and offset != 1:\n            continue\n', "")
V6 = L.SOURCE.replace('(d["student"], d["course"]) in silenced', 'd["student"] in [s for s, c in silenced]')
V7 = L.SOURCE
VERSIONS = [V0, V1, V2, V3, V4, V5, V6, V7]


def e482():
    print("SE-482 — ciclo rojo-verde-refactor sobre ocho pruebas")
    tests = L.TDD_TESTS
    fns = [L.load(v) if "OFFSETS" in v else None for v in VERSIONS]
    # las versiones sin OFFSETS no lo necesitan
    fns = [L.load(v) for v in VERSIONS]

    def passes(test, fn):
        try:
            test(fn)
            return True
        except Exception:  # noqa: BLE001
            return False

    rows = [["Paso", "Prueba nueva", "Roja con la versión anterior", "Verde con la nueva", "Anteriores siguen verdes"]]
    for k, test in enumerate(tests):
        prev = fns[k]
        new = fns[k]  # V_k pasa t_k ; V_(k-1) debe fallar
        red = not passes(test, fns[k - 1]) if k > 0 else not passes(test, L.load("def due_reminders(a, b, c, d):\n    raise NotImplementedError\n"))
        green = passes(test, fns[k])
        regress = all(passes(t, fns[k]) for t in tests[:k])
        rows.append([k + 1, test.__name__, "sí" if red else "no", "sí" if green else "no", "sí" if regress else "no"])
    table(rows)
    print("  versión final idéntica al original:", VERSIONS[-1] == L.SOURCE)
    print("  curva de mutantes muertos tras cada prueba (de 18):")
    versions = L.all_versions()
    for k in range(1, len(tests) + 1):
        killed = sum(1 for m in REAL_IDS if not L.oracle_tdd(versions[m], k))
        print(f"    {k} pruebas: {killed}")
    # sobrevivientes de las ocho pruebas
    survivors = [m for m in REAL_IDS if L.oracle_tdd(versions[m])]
    print("  sobreviven a las ocho:", survivors, [dict((x[0], x[3]) for x in L.MUTANTS)[s] for s in survivors])
    # añadir pruebas en el límite (refactor del conjunto: los sobrevivientes piden pruebas)
    extra = []

    def t09(fn):
        assert fn([L.delivery("a", 100)], 100, frozenset(), set()) == []

    def t10(fn):
        assert fn([L.delivery("a", 100)], 27, frozenset(), set()) == []
        assert fn([L.delivery("a", 100)], 28, frozenset(), set()) == [("a", 72)]

    def t11(fn):
        assert fn([L.delivery("a", 100)], 70, frozenset(), {("a", 24)}) == []
        assert fn([L.delivery("a", 100)], 75, frozenset(), {("a", 72)}) == []
        assert fn([L.delivery("a", 100)], 76, frozenset(), {("a", 72)}) == [("a", 24)]

    extra = [t09, t10, t11]
    tests2 = tests + extra
    print("  tras añadir tres pruebas guiadas por los sobrevivientes:")
    for t in extra:
        ok = all(passes(t, versions["ORIGINAL"]) for _ in [0])
        print(f"    {t.__name__} pasa con el original: {ok}")
    killed = sum(1 for m in REAL_IDS if any(not passes(t, versions[m]) for t in tests2))
    print(f"    mutantes muertos: {killed} de {len(REAL_IDS)}")


# ====================================================================== SE-483
class FakeRepo:
    def __init__(self, deliveries):
        self.deliveries = deliveries
        self.sent = set()

    def pending_deliveries(self):
        return [d for d in self.deliveries if not d["submitted"]]

    def all_deliveries(self):
        return list(self.deliveries)

    def mark_sent(self, delivery_id, offset):
        self.sent.add((delivery_id, offset))

    def sent_for(self, delivery_id):
        return {o for (i, o) in self.sent if i == delivery_id}


class FakeChannel:
    def __init__(self, fail_for=()):
        self.messages = []
        self.fail_for = set(fail_for)

    def send(self, student, text):
        if student in self.fail_for:
            raise ConnectionError("canal caído")
        self.messages.append((student, text))


class FakeClock:
    def __init__(self, t):
        self.t = t

    def now(self):
        return self.t


class ReminderService:
    """Versión base: el cómo de cada colaboración es privado del servicio."""

    def __init__(self, repo, channel, clock):
        self.repo, self.channel, self.clock = repo, channel, clock

    def candidates(self):
        return self.repo.pending_deliveries()

    def now(self):
        return self.clock.now()

    def run(self):
        for d in self.candidates():
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            done = self.repo.sent_for(d["id"])
            pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
            if not pending:
                continue
            offset = min(pending)
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue
            for o in L.OFFSETS:
                if o >= offset:
                    self.repo.mark_sent(d["id"], o)


class R1ClockOnce(ReminderService):  # refactor: leer el reloj una sola vez por ejecución
    def run(self):
        t = self.clock.now()
        self.now = lambda: t
        super().run()


class R2AllThenFilter(ReminderService):  # refactor: pedir todas y filtrar en el servicio
    def candidates(self):
        return [d for d in self.repo.all_deliveries() if not d["submitted"]]


class R3ExtractHelper(ReminderService):  # refactor: extraer el cálculo del umbral
    @staticmethod
    def _offset(remaining, done):
        pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
        return min(pending) if pending else None

    def run(self):
        for d in self.candidates():
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            offset = self._offset(remaining, self.repo.sent_for(d["id"]))
            if offset is None:
                continue
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue
            for o in L.OFFSETS:
                if o >= offset:
                    self.repo.mark_sent(d["id"], o)


class R4ReadOrder(ReminderService):  # refactor: leer lo registrado antes de calcular el tiempo restante
    def run(self):
        for d in self.candidates():
            done = self.repo.sent_for(d["id"])
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
            if not pending:
                continue
            offset = min(pending)
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue
            for o in sorted(L.OFFSETS, reverse=True):
                if o >= offset:
                    self.repo.mark_sent(d["id"], o)


class R5RenamedPort(ReminderService):  # cambio de interfaz: el puerto de registro cambia de nombre
    def run(self):
        for d in self.candidates():
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            done = self.repo.sent_for(d["id"])
            pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
            if not pending:
                continue
            offset = min(pending)
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue
            for o in L.OFFSETS:
                if o >= offset:
                    self.repo.record_notice(d["id"], o)


class D1NoMark(ReminderService):  # defecto: no registra el envío
    def run(self):
        original = self.repo.mark_sent
        self.repo.mark_sent = lambda i, o: None
        try:
            super().run()
        finally:
            self.repo.mark_sent = original


class D2MarkBeforeSend(ReminderService):  # defecto: marca antes de enviar y pierde el aviso si el canal falla
    def run(self):
        for d in self.candidates():
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            done = self.repo.sent_for(d["id"])
            pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
            if not pending:
                continue
            offset = min(pending)
            for o in L.OFFSETS:
                if o >= offset:
                    self.repo.mark_sent(d["id"], o)
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue


class D3AllCandidates(ReminderService):  # defecto: incluye entregas ya entregadas
    def candidates(self):
        return self.repo.all_deliveries()


class D4WrongRecipient(ReminderService):  # defecto: avisa a un estudiante fijo
    def run(self):
        original = self.channel.send
        self.channel.send = lambda student, text: original("e-docente", text)
        try:
            super().run()
        finally:
            self.channel.send = original


class D5RetryForever(ReminderService):  # defecto: reintenta enviando dos veces
    def run(self):
        original = self.channel.send

        def twice(student, text):
            original(student, text)
            original(student, text)

        self.channel.send = twice
        try:
            super().run()
        finally:
            self.channel.send = original


class D6MarkOne(ReminderService):  # defecto: registra solo el umbral enviado y deja pasar los anteriores
    def run(self):
        for d in self.candidates():
            remaining = d["due"] - self.now()
            if remaining <= 0:
                continue
            done = self.repo.sent_for(d["id"])
            pending = [o for o in L.OFFSETS if remaining <= o and not any(s <= o for s in done)]
            if not pending:
                continue
            offset = min(pending)
            try:
                self.channel.send(d["student"], f"Entrega {d['id']} vence en {remaining} h")
            except ConnectionError:
                continue
            self.repo.mark_sent(d["id"], offset)


REFACTORS = {"R1 leer el reloj una vez": R1ClockOnce, "R2 pedir todas y filtrar en el servicio": R2AllThenFilter,
             "R3 extraer el cálculo del umbral": R3ExtractHelper, "R4 leer lo registrado antes del reloj": R4ReadOrder}
DEFECTS = {"D1 no registra el envío": D1NoMark, "D6 registra solo el umbral enviado": D6MarkOne, "D2 marca antes de enviar": D2MarkBeforeSend,
           "D3 incluye entregas ya entregadas": D3AllCandidates, "D4 destinatario equivocado": D4WrongRecipient,
           "D5 envía dos veces": D5RetryForever}


def classical_suite(cls):
    """Estilo clásico: dobles con estado y aserciones sobre el resultado observable."""
    try:
        repo = FakeRepo([L.delivery("a", 100), L.delivery("b", 100, student="e2", submitted=True)])
        ch = FakeChannel()
        cls(repo, ch, FakeClock(76)).run()
        assert [m[0] for m in ch.messages] == ["e1"], ch.messages
        assert repo.sent_for("a") == {24, 72}, repo.sent
        cls(repo, ch, FakeClock(77)).run()
        assert len(ch.messages) == 1, "no repite"
        repo = FakeRepo([L.delivery("a", 100)])
        ch = FakeChannel(fail_for=["e1"])
        cls(repo, ch, FakeClock(99)).run()
        assert repo.sent_for("a") == set(), "no registra si el canal falla"
        ch.fail_for = set()
        cls(repo, ch, FakeClock(99.5)).run()
        assert [m[0] for m in ch.messages] == ["e1"] and repo.sent_for("a") == {1, 24, 72}
    except Exception:  # noqa: BLE001
        return False
    return True


def mockist_suite(cls):
    """Estilo de Londres: colaboradores simulados; consultas con valores fijos y verificación de órdenes."""
    try:
        d = L.delivery("a", 100)
        manager = um.Mock()
        repo, ch, clock = manager.repo, manager.channel, manager.clock
        repo.pending_deliveries.return_value = [d]
        repo.sent_for.return_value = set()
        clock.now.return_value = 76
        cls(repo, ch, clock).run()
        repo.pending_deliveries.assert_called_once_with()
        ch.send.assert_called_once()
        assert ch.send.call_args[0][0] == "e1"
        assert repo.mark_sent.call_args_list == [um.call("a", 72), um.call("a", 24)], repo.mark_sent.call_args_list
        names = [c[0] for c in manager.mock_calls if c[0] in ("channel.send", "repo.mark_sent")]
        assert names[0] == "channel.send", names
        manager2 = um.Mock()
        repo2, ch2, clock2 = manager2.repo, manager2.channel, manager2.clock
        ch2.send.side_effect = ConnectionError()
        repo2.pending_deliveries.return_value = [d]
        repo2.sent_for.return_value = set()
        clock2.now.return_value = 99
        cls(repo2, ch2, clock2).run()
        repo2.mark_sent.assert_not_called()
    except Exception:  # noqa: BLE001
        return False
    return True


def e483():
    print("SE-483 — escuelas clásica y de Londres frente a refactores y defectos")
    for name, suite in (("clásica", classical_suite), ("Londres", mockist_suite)):
        print(f"  {name}: pasa con la versión base:", suite(ReminderService))
    rows = [["Cambio", "Tipo", "Clásica", "Londres"]]
    false_fail = {"clásica": 0, "Londres": 0}
    caught = {"clásica": 0, "Londres": 0}
    for label, cls in REFACTORS.items():
        c, m = classical_suite(cls), mockist_suite(cls)
        false_fail["clásica"] += (not c)
        false_fail["Londres"] += (not m)
        rows.append([label, "refactor (conserva el comportamiento)", "pasa" if c else "FALLA", "pasa" if m else "FALLA"])
    c, m = classical_suite(R5RenamedPort), mockist_suite(R5RenamedPort)
    rows.append(["R5 cambio de interfaz (el puerto se renombra)", "cambio de contrato (no es refactor)", "pasa" if c else "FALLA", "pasa" if m else "FALLA"])
    for label, cls in DEFECTS.items():
        c, m = classical_suite(cls), mockist_suite(cls)
        caught["clásica"] += (not c)
        caught["Londres"] += (not m)
        rows.append([label, "defecto (cambia el comportamiento)", "detecta" if not c else "NO", "detecta" if not m else "NO"])
    table(rows)
    print("  falsas alarmas (refactores que rompen la prueba):", false_fail, "de", len(REFACTORS))
    print("  defectos detectados:", caught, "de", len(DEFECTS))


# ====================================================================== SE-484
FEATURE = """
Escenario: avisa a las 72 horas
  Dado una entrega que vence en la hora 100
  Cuando el reloj marca la hora 28
  Entonces se envía el aviso de 72 horas

Escenario: no repite un aviso enviado
  Dado una entrega que vence en la hora 100
  Y el aviso de 72 horas ya se envió
  Cuando el reloj marca la hora 29
  Entonces no se envía ningún aviso

Escenario: quien ya entregó no recibe avisos
  Dado una entrega que vence en la hora 100
  Y la entrega ya fue entregada
  Cuando el reloj marca la hora 76
  Entonces no se envía ningún aviso

Escenario: tras una caída solo llega el aviso más urgente
  Dado una entrega que vence en la hora 100
  Cuando el reloj marca la hora 90
  Entonces se envía el aviso de 24 horas

Escenario: un curso silenciado conserva el aviso de la última hora
  Dado una entrega que vence en la hora 100
  Y el curso está silenciado
  Cuando el reloj marca la hora 99
  Entonces se envía el aviso de 1 horas

Escenario: un curso silenciado no recibe el de 24 horas
  Dado una entrega que vence en la hora 100
  Y el curso está silenciado
  Cuando el reloj marca la hora 76
  Entonces no se envía ningún aviso

Escenario: el silencio de un curso no afecta a otro
  Dado una entrega que vence en la hora 100 en el curso c2
  Y el curso c1 está silenciado
  Cuando el reloj marca la hora 76
  Entonces se envía el aviso de 24 horas

Escenario: una entrega vencida no avisa
  Dado una entrega que vence en la hora 100
  Cuando el reloj marca la hora 101
  Entonces no se envía ningún aviso

Escenario: la interfaz es agradable
  Dado una entrega que vence en la hora 100
  Cuando el reloj marca la hora 76
  Entonces la experiencia es satisfactoria
"""

STEPS = [
    (r"una entrega que vence en la hora (\d+)$", lambda w, h: w.update(due=int(h), course="c1")),
    (r"una entrega que vence en la hora (\d+) en el curso (\w+)$", lambda w, h, c: w.update(due=int(h), course=c)),
    (r"el aviso de (\d+) horas ya se envió$", lambda w, o: w["sent"].add(("a", int(o)))),
    (r"la entrega ya fue entregada$", lambda w: w.update(submitted=True)),
    (r"el curso está silenciado$", lambda w: w["silenced"].add(("e1", "c1"))),
    (r"el curso (\w+) está silenciado$", lambda w, c: w["silenced"].add(("e1", c))),
    (r"el reloj marca la hora (\d+)$", lambda w, h: w.update(out=w["fn"]([L.delivery("a", w["due"], course=w["course"], submitted=w.get("submitted", False))], int(h), frozenset(w["silenced"]), set(w["sent"])))),
    (r"se envía el aviso de (\d+) horas$", lambda w, o: _assert(w["out"] == [("a", int(o))], f"esperaba [('a', {o})] y salió {w['out']}")),
    (r"no se envía ningún aviso$", lambda w: _assert(w["out"] == [], f"esperaba nada y salió {w['out']}")),
    (r"la experiencia es satisfactoria$", lambda w: _assert(True, "")),
]


def _assert(cond, message):
    if not cond:
        raise AssertionError(message)


def parse_feature(text):
    scenarios, current = [], None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("Escenario:"):
            current = {"name": line[len("Escenario:"):].strip(), "steps": []}
            scenarios.append(current)
        elif current and line:
            keyword, _, rest = line.partition(" ")
            current["steps"].append((keyword, rest))
    return scenarios


def bind(step_text):
    for pattern, action in STEPS:
        m = re.match(pattern, step_text)
        if m:
            return pattern, action, m.groups()
    raise LookupError(step_text)


def run_scenario(fn, scenario, skip_step=None):
    world = {"fn": fn, "silenced": set(), "sent": set()}
    for index, (keyword, text) in enumerate(scenario["steps"]):
        if index == skip_step:
            continue
        _, action, args = bind(text)
        action(world, *args)


def feature_oracle(fn, scenarios=None, drop=None):
    scenarios = scenarios if scenarios is not None else parse_feature(FEATURE)
    try:
        for s in scenarios:
            run_scenario(fn, s)
    except Exception:  # noqa: BLE001
        return False
    return True


def e484():
    print("SE-484 — escenarios Gherkin ejecutados contra los mutantes")
    scenarios = parse_feature(FEATURE)
    steps = [(k, t) for s in scenarios for k, t in s["steps"]]
    patterns = {bind(t)[0] for _, t in steps}
    print(f"  escenarios: {len(scenarios)}; pasos: {len(steps)}; definiciones de paso distintas: {len(patterns)}")
    print(f"  reutilización: {len(steps) / len(patterns):.2f} pasos por definición".replace(".", ","))
    versions = L.all_versions()
    print("  el original pasa todo:", feature_oracle(versions["ORIGINAL"]))
    killed = [m for m in REAL_IDS if not feature_oracle(versions[m])]
    print(f"  mutantes muertos por los escenarios: {len(killed)} de {len(REAL_IDS)}; sobreviven {[m for m in REAL_IDS if m not in killed]}")
    # qué pasos «Entonces» importan: quitar cada Entonces de un escenario y contar lo que se pierde
    print("  contribución de cada escenario (mutantes que solo él mata):")
    rows = [["Escenario", "Mutantes que mata", "Solo él"]]
    per = {}
    for s in scenarios:
        ok_set = set()
        for m in REAL_IDS:
            try:
                run_scenario(versions[m], s)
            except Exception:  # noqa: BLE001
                ok_set.add(m)
        per[s["name"]] = ok_set
    for name, ks in per.items():
        others = set().union(*[v for n, v in per.items() if n != name])
        rows.append([name, len(ks), len(ks - others)])
    table(rows)
    # un paso «Entonces» vaciado: ¿cuántos mutantes dejan de morir?
    print("  si se reemplaza el «Entonces» de cada escenario por un paso que no afirma nada:")
    full = len(killed)
    for s in scenarios:
        stripped = {"name": s["name"], "steps": [st for st in s["steps"] if st[0] != "Entonces"] + [("Entonces", "la experiencia es satisfactoria")]}
        trial = [x if x is not s else stripped for x in scenarios]
        k = sum(1 for m in REAL_IDS if not feature_oracle(versions[m], trial))
        print(f"    {s['name']}: {k} de {len(REAL_IDS)} (pierde {full - k})")


# ====================================================================== SE-485
def classes_of_remaining():
    return [100, 73, 72, 71, 25, 24, 23, 2, 1, 0.5, 0, -1]


def example_oracle(fn, examples):
    try:
        for deliveries, now, silenced, sent in examples:
            assert fn(deliveries, now, silenced, sent) == L.reference(deliveries, now, silenced, sent)
    except Exception:  # noqa: BLE001
        return False
    return True


def make_example(remaining, submitted=False, silenced=False, sent=()):
    d = L.delivery("a", 100 + 0, submitted=submitted)
    now = 100 - remaining
    sil = frozenset({("e1", "c1")}) if silenced else frozenset()
    return ([d], now, sil, {("a", o) for o in sent})


def e485():
    print("SE-485 — ejemplos de aceptación: típicos, de frontera, combinatorios y al azar")
    versions = L.all_versions()
    typical = [make_example(r) for r in (100, 48, 10)] + [make_example(10, submitted=True), make_example(10, silenced=True)]
    boundary = [make_example(r) for r in classes_of_remaining()]
    combos = [make_example(r, s, z, sent)
              for r in classes_of_remaining()
              for s in (False, True)
              for z in (False, True)
              for sent in ((), (72,), (24,))]
    rng = L.random.Random(485)
    import random as _r
    rnd = []
    for _ in range(20):
        rnd.append(make_example(rng.choice(range(-5, 120)), rng.random() < 0.3, rng.random() < 0.3,
                                rng.choice([(), (72,), (24,), (1,)])))
    sets = {"5 típicos": typical, "12 de frontera": boundary, "20 al azar": rnd,
            f"{len(combos)} combinatorios": combos}
    rows = [["Conjunto de ejemplos", "Ejemplos", "Mutantes muertos", "Sobreviven"]]
    for name, ex in sets.items():
        killed = [m for m in REAL_IDS if not example_oracle(versions[m], ex)]
        rows.append([name, len(ex), f"{len(killed)} de {len(REAL_IDS)}", ", ".join(m for m in REAL_IDS if m not in killed) or "ninguno"])
    table(rows)
    both = boundary + typical
    killed = [m for m in REAL_IDS if not example_oracle(versions[m], both)]
    print(f"  frontera + típicos ({len(both)}): {len(killed)} de {len(REAL_IDS)}")
    print("  el original pasa todos los conjuntos:", all(example_oracle(versions["ORIGINAL"], e) for e in sets.values()))
    print("  nota: los resultados esperados salen de un modelo escrito aparte; un ejemplo real los redacta una persona.")


# ====================================================================== SE-486
ROOT = Path(__file__).resolve().parents[1]
SENSES = {
    "tarea o trabajo de una persona estudiante": re.compile(r"estudiant|docente|curso|vencimiento|vence|entregada|aviso", re.I),
    "liberar o desplegar software": re.compile(r"entrega continua|continuous delivery|despliegu|pipeline|release|CI/CD|rollback|canar", re.I),
    "hacer llegar un mensaje o resultado": re.compile(r"entrega (del )?(mensaje|evento|evidencia|resultado)|at-least-once|al menos una vez|exactamente una vez|cola|broker", re.I),
}


def e486():
    print("SE-486 — polisemia de «entrega» en el corpus del programa y traducción entre contextos")
    pattern = re.compile(r"[^.\n]*\bentreg\w+[^.\n]*", re.I)
    counts = {k: 0 for k in SENSES}
    unclassified = 0
    total = 0
    parts_by_sense = {k: set() for k in SENSES}
    for path in sorted((ROOT / "content").glob("part-*/SE-*.md")):
        part = path.parent.name
        if int(part.split("-")[1]) >= 40:
            continue  # el corpus medido son las Partes 00-39, para que el recuento no cambie al añadir partes
        text = path.read_text(encoding="utf-8")
        for m in pattern.finditer(text):
            sentence = m.group(0)
            total += 1
            labels = [k for k, rx in SENSES.items() if rx.search(sentence)]
            if len(labels) == 1:
                counts[labels[0]] += 1
                parts_by_sense[labels[0]].add(part)
            elif not labels:
                unclassified += 1
            else:
                # varios sentidos en la misma frase: la ambigüedad que un glosario debe resolver
                counts.setdefault("ambigua (varios sentidos a la vez)", 0)
                counts["ambigua (varios sentidos a la vez)"] += 1
    print(f"  frases con «entrega» en content/part-00..39/SE-*.md: {total}")
    for k, v in counts.items():
        extra = f", en {len(parts_by_sense[k])} partes" if k in parts_by_sense else ""
        print(f"    {k}: {v}{extra}")
    print(f"    sin sentido reconocible por las reglas: {unclassified}")

    # traducción entre dos contextos con una capa anticorrupción mínima
    academico = [{"entrega_id": f"E{i}", "estudiante": f"e{i % 3}", "vence_en": 20 + i, "estado": "pendiente" if i % 4 else "recibida"} for i in range(8)]

    def traducir(item):
        return {"id": item["entrega_id"], "student": item["estudiante"], "due": item["vence_en"],
                "submitted": item["estado"] == "recibida", "course": "c1"}

    traducidos = [traducir(i) for i in academico]
    avisos = L.load(L.SOURCE)(traducidos, 0, frozenset(), set())
    print(f"  8 entregas del contexto académico traducidas: {sum(t['submitted'] for t in traducidos)} recibidas, {len(avisos)} avisos")
    # sin traducción, el contexto Avisos lee el estado como si fuera booleano
    crudo_out = L.load(L.SOURCE)([{**i, "id": i["entrega_id"], "student": i["estudiante"], "course": "c1", "due": i["vence_en"], "submitted": i["estado"]} for i in academico], 0, frozenset(), set())
    print(f"  sin traducir (estado como texto): {len(crudo_out)} avisos; los textos «pendiente» y «recibida» cuentan ambos como verdaderos")


if __name__ == "__main__":
    which = sys.argv[1:] or ["481", "482", "483", "484", "485", "486"]
    for key in which:
        globals()[f"e{key}"]()
        print()
