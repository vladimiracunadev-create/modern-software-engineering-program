"""Experimentos de ampliación de SE-391 y SE-393 (modelos sintéticos con semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part32_ext.py   (imprime una línea JSON por experimento)

1. Un modelo reducido de elección y replicación con la forma de Raft (mandatos, un voto por mandato, mayoría de 3 de 5,
   entradas comprometidas solo con mayoría) sometido a calendarios aleatorios de caídas, particiones y mensajes entre
   nodos. Se compara el protocolo completo con dos variantes con un fallo deliberado. No es Raft: no hay latidos,
   plazos, mensajes retrasados ni reintentos de AppendEntries; la reparación de un registro copia el registro entero
   del líder.
2. Tres réplicas de un conjunto con altas y bajas concurrentes y entrega desordenada y duplicada de las operaciones:
   conjunto que aplica en orden de llegada, conjunto con último escritor (reloj con desfase) y OR-Set (cada alta lleva
   una etiqueta única y cada baja quita las etiquetas que su origen había visto).
"""
import json
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")

N = 5
MAYORIA = 3


def correr_calendario(rng, variante, pasos=70):
    term = [0] * N
    voto = [None] * N
    registro = [[] for _ in range(N)]  # entradas (mandato, id)
    lider = [False] * N
    arriba = [True] * N
    grupo = [0] * N
    comprometido = {}  # índice -> entrada
    siguiente_id = 0
    violacion = False

    def alcanza(a, b):
        return arriba[a] and arriba[b] and grupo[a] == grupo[b]

    def al_dia(c, v):
        if variante == "sin_comparar_registro":
            return True
        lc = registro[c][-1][0] if registro[c] else 0
        lv = registro[v][-1][0] if registro[v] else 0
        return (lc, len(registro[c])) >= (lv, len(registro[v]))

    for _ in range(pasos):
        r = rng.random()
        if r < 0.16:  # elección
            c = rng.randrange(N)
            if not arriba[c]:
                continue
            term[c] += 1
            voto[c] = c
            lider[c] = False
            votos = 1
            for v in range(N):
                if v == c or not alcanza(c, v):
                    continue
                if term[c] > term[v]:
                    term[v], voto[v], lider[v] = term[c], None, False
                if term[c] == term[v] and voto[v] in (None, c) and al_dia(c, v):
                    voto[v] = c
                    votos += 1
            if votos >= MAYORIA:
                lider[c] = True
                for i, e in comprometido.items():
                    if i >= len(registro[c]) or registro[c][i] != e:
                        violacion = True
        elif r < 0.42:  # un cliente escribe en un presunto líder
            ls = [i for i in range(N) if lider[i] and arriba[i]]
            if ls:
                l = rng.choice(ls)
                siguiente_id += 1
                registro[l].append((term[l], siguiente_id))
        elif r < 0.78:  # replicación
            ls = [i for i in range(N) if lider[i] and arriba[i]]
            if ls:
                l = rng.choice(ls)
                f = rng.randrange(N)
                if f != l and alcanza(l, f):
                    if term[l] >= term[f]:
                        if term[l] > term[f]:
                            voto[f] = None
                        term[f] = term[l]
                        lider[f] = False
                        registro[f] = list(registro[l])
                    else:
                        term[l], lider[l] = term[f], False
        elif r < 0.90:  # el líder intenta comprometer
            ls = [i for i in range(N) if lider[i] and arriba[i]]
            if ls:
                l = rng.choice(ls)
                for i in range(len(registro[l]) - 1, -1, -1):
                    copias = sum(1 for n in range(N)
                                 if (n == l or alcanza(l, n)) and len(registro[n]) > i and registro[n][i] == registro[l][i])
                    actual = registro[l][i][0] == term[l]
                    if copias >= MAYORIA and (actual or variante == "comprometer_mandatos_previos"):
                        for j in range(i + 1):
                            if j in comprometido and comprometido[j] != registro[l][j]:
                                violacion = True
                            comprometido.setdefault(j, registro[l][j])
                        break
        elif r < 0.95:  # caída o recuperación
            n = rng.randrange(N)
            arriba[n] = not arriba[n]
            if not arriba[n]:
                lider[n] = False
        else:  # partición en dos grupos al azar
            grupo = [rng.randrange(2) for _ in range(N)]
    return violacion


def experimento_consenso():
    salida = {}
    for variante in ("completo", "sin_comparar_registro", "comprometer_mandatos_previos"):
        rng = random.Random(343)
        total = 20000
        malos = sum(correr_calendario(rng, variante) for _ in range(total))
        salida[variante] = {"calendarios": total, "con_violacion": malos, "pct": round(100 * malos / total, 2)}
    return salida


# ------------------------------------------------------------------ conjuntos replicados
def correr_conjunto(rng, diseno, operaciones=12, elementos=3):
    """Devuelve (convergen, coincide_con_alta_gana)."""
    # Cada réplica conserva lo que ha recibido; antes de emitir su operación recibe, con probabilidad 0,5, cada
    # operación pendiente de las demás (en orden aleatorio). Las bajas llevan las etiquetas que su origen había visto.
    ops = []
    recibidas = [set() for _ in range(3)]
    for k in range(operaciones):
        r = rng.randrange(3)
        pendientes = [o for o in ops if o["origen"] != r and o["k"] not in recibidas[r]]
        rng.shuffle(pendientes)
        for o in pendientes:
            if rng.random() < 0.5:
                recibidas[r].add(o["k"])
        e = rng.randrange(elementos)
        tipo = "alta" if rng.random() < 0.6 else "baja"
        vistas = {o["k"] for o in ops if o["elem"] == e and o["tipo"] == "alta"
                  and (o["origen"] == r or o["k"] in recibidas[r])}
        ops.append({"k": k, "origen": r, "elem": e, "tipo": tipo, "ts": k + rng.choice([0, 0, 0, -3, 3]),
                    "observa": vistas if tipo == "baja" else set()})
        recibidas[r].add(k)
    # Especificación «el alta gana»: e está si algún alta no fue observada por ninguna baja.
    esperado = set()
    for e in range(elementos):
        observadas = set().union(*[o["observa"] for o in ops if o["elem"] == e and o["tipo"] == "baja"] or [set()])
        if any(o["k"] not in observadas for o in ops if o["elem"] == e and o["tipo"] == "alta"):
            esperado.add(e)
    estados = []
    for r in range(3):
        orden = list(ops)
        rng.shuffle(orden)
        orden += rng.sample(ops, 5)  # entregas duplicadas
        if diseno == "ingenuo":
            s = set()
            for o in orden:
                (s.add if o["tipo"] == "alta" else s.discard)(o["elem"])
        elif diseno == "ultimo_escritor":
            ult = {}
            for o in orden:
                if o["elem"] not in ult or o["ts"] >= ult[o["elem"]][0]:
                    ult[o["elem"]] = (o["ts"], o["tipo"])
            s = {e for e, (_, t) in ult.items() if t == "alta"}
        else:  # OR-Set: unión de etiquetas de altas menos unión de etiquetas observadas por bajas
            altas, quitadas = {}, set()
            for o in orden:
                if o["tipo"] == "alta":
                    altas.setdefault(o["elem"], set()).add(o["k"])
                else:
                    quitadas |= o["observa"]
            s = {e for e, ts in altas.items() if ts - quitadas}
        estados.append(frozenset(s))
    return len(set(estados)) == 1, all(set(s) == esperado for s in estados)


def experimento_conjuntos():
    salida = {}
    for diseno in ("ingenuo", "ultimo_escritor", "or_set"):
        rng = random.Random(345)
        total = 5000
        div = incumple = 0
        for _ in range(total):
            conv, cumple = correr_conjunto(rng, diseno)
            div += not conv
            incumple += not cumple
        salida[diseno] = {"corridas": total, "divergen_pct": round(100 * div / total, 1),
                          "incumplen_alta_gana_pct": round(100 * incumple / total, 1)}
    return salida


if __name__ == "__main__":
    print(json.dumps({"consenso": experimento_consenso()}, ensure_ascii=False))
    print(json.dumps({"conjuntos": experimento_conjuntos()}, ensure_ascii=False))
