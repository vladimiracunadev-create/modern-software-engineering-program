"""Experimento de ampliación de SE-513: curva de aprendizaje y contaminación de la evaluación al ajustar un modelo.

Datos sintéticos, semilla fija, solo biblioteca estándar. Analogía deliberadamente pequeña: no se ajusta ningún
modelo de lenguaje; se entrena un clasificador de texto con memoria (vecino más próximo) para mostrar qué le ocurre a
una medida cuando el conjunto de evaluación comparte ejemplos con el de entrenamiento.
Uso: python scripts/experiments_part42_ext.py   (imprime una línea JSON)

Tarea: clasificar «tickets» de 12 palabras en 4 categorías. Cada categoría tiene 40 palabras propias (probabilidad
0,35 por posición) y el resto sale de un vocabulario común de 300 palabras. El 5 % de las etiquetas de
entrenamiento es erróneo. Evaluación limpia: 1 000 ejemplos nuevos. Evaluación contaminada: 1 000 ejemplos de los
cuales la mitad son copias de ejemplos de entrenamiento (con la etiqueta con que se entrenó).
"""
import json
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")

CLASES = 4
COMUNES = [f"c{i}" for i in range(300)]
PROPIAS = {k: [f"k{k}_{i}" for i in range(40)] for k in range(CLASES)}


def ejemplo(rng, clase):
    return frozenset(rng.choice(PROPIAS[clase]) if rng.random() < 0.35 else rng.choice(COMUNES) for _ in range(12))


def generar(rng, n, ruido=0.0):
    datos = []
    for _ in range(n):
        k = rng.randrange(CLASES)
        etiqueta = k if rng.random() >= ruido else rng.choice([c for c in range(CLASES) if c != k])
        datos.append((ejemplo(rng, k), etiqueta, k))
    return datos


def vecino(entrenamiento, x):
    mejor, etiqueta = -1.0, None
    for d, y, _ in entrenamiento:
        s = len(d & x) / len(d | x)
        if s > mejor:
            mejor, etiqueta = s, y
    return etiqueta


def bayes(entrenamiento):
    conteo = {k: {} for k in range(CLASES)}
    prior = [0] * CLASES
    for d, y, _ in entrenamiento:
        prior[y] += 1
        for w in d:
            conteo[y][w] = conteo[y].get(w, 0) + 1
    totales = [sum(c.values()) + 340 for c in conteo.values()]

    def predecir(x):
        mejor, etiqueta = None, None
        import math
        for k in range(CLASES):
            s = math.log((prior[k] + 1) / (len(entrenamiento) + CLASES))
            for w in x:
                s += math.log((conteo[k].get(w, 0) + 1) / totales[k])
            if mejor is None or s > mejor:
                mejor, etiqueta = s, k
        return etiqueta
    return predecir


def main():
    tamanos = [10, 30, 100, 300, 1000, 3000]
    salida = {"tamanos": tamanos, "vecino_limpia": [], "vecino_contaminada": [], "bayes_limpia": [], "bayes_contaminada": []}
    for n in tamanos:
        rng = random.Random(513 + n)
        ent = generar(rng, n, ruido=0.05)
        limpia = generar(rng, 1000)
        copias = [ent[rng.randrange(n)] for _ in range(500)]
        contaminada = [(d, y, k) for d, y, k in limpia[:500]] + copias  # la etiqueta de la copia es la de entrenamiento
        modelo = bayes(ent)
        for nombre, evaluacion in (("limpia", limpia), ("contaminada", contaminada)):
            salida["vecino_" + nombre].append(round(100 * sum(vecino(ent, d) == (y if nombre == "contaminada" and (d, y, k) in copias else k)
                                                              for d, y, k in evaluacion) / len(evaluacion), 1))
            salida["bayes_" + nombre].append(round(100 * sum(modelo(d) == (y if nombre == "contaminada" and (d, y, k) in copias else k)
                                                             for d, y, k in evaluacion) / len(evaluacion), 1))
    print(json.dumps(salida, ensure_ascii=False))


if __name__ == "__main__":
    main()
