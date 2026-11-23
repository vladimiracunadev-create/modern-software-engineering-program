"""Experimento de ampliación de SE-562: verificador de una ficha de sistema de IA frente a obligaciones de alto riesgo.

Datos sintéticos, semilla fija, solo biblioteca estándar.
Uso: python scripts/experiments_part46_ext.py   (imprime una línea JSON)

La ficha es un diccionario con el caso de uso, el nivel de riesgo declarado y siete campos de evidencia que
corresponden, de forma simplificada, a los requisitos de los artículos 9 a 15 del Reglamento (UE) 2024/1689 para
sistemas de alto riesgo. El verificador (1) clasifica el caso de uso por palabras clave de las áreas del anexo III
y avisa si el nivel declarado es menor, y (2) exige los siete campos si el nivel es alto. Se aplican 200 mutaciones:
borrar un campo, declarar «mínimo» un caso de alto riesgo con su redacción literal y declarar «mínimo» un caso de alto
riesgo redactado con otras palabras. No es asesoría legal ni una evaluación de conformidad.
"""
import json
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")

CAMPOS = ["gestion_de_riesgos", "gobernanza_de_datos", "documentacion_tecnica", "registro_de_eventos",
          "transparencia_al_usuario", "supervision_humana", "exactitud_robustez_ciberseguridad"]
PALABRAS_ALTO = ["selección de personal", "calificación de estudiantes", "solvencia crediticia", "acceso a beneficios",
                 "biometría", "infraestructura crítica"]
CASOS = [  # (redacción literal, redacción con otras palabras)
    ("filtra candidatos en la selección de personal", "ordena currículos y propone a quién entrevistar"),
    ("apoya la calificación de estudiantes", "sugiere la nota de las pruebas escritas"),
    ("estima la solvencia crediticia", "decide cuánto dinero se presta a una persona"),
    ("prioriza el acceso a beneficios públicos", "determina quién recibe una ayuda social primero"),
    ("verifica identidad por biometría", "reconoce la cara de quien entra al edificio"),
    ("gestiona infraestructura crítica de agua", "regula la presión de la red de agua de la ciudad"),
]


def ficha_valida(caso):
    f = {"caso_de_uso": caso, "riesgo_declarado": "alto"}
    f.update({c: "descrito" for c in CAMPOS})
    return f


def verificar(f):
    avisos = set()
    if f["riesgo_declarado"] != "alto" and any(p in f["caso_de_uso"] for p in PALABRAS_ALTO):
        avisos.add("nivel_subestimado")
    if f["riesgo_declarado"] == "alto":
        for c in CAMPOS:
            if not f.get(c):
                avisos.add("falta_" + c)
    return avisos


def main():
    rng = random.Random(466)
    resultado = {"borrar_campo": [0, 0], "minimo_redaccion_literal": [0, 0], "minimo_otras_palabras": [0, 0]}
    por_campo = {c: [0, 0] for c in CAMPOS}
    for _ in range(200):
        literal, otra = rng.choice(CASOS)
        tipo = rng.choice(list(resultado))
        if tipo == "borrar_campo":
            f = ficha_valida(literal)
            c = rng.choice(CAMPOS)
            f[c] = ""
            ok = ("falta_" + c) in verificar(f)
            por_campo[c][0] += ok
            por_campo[c][1] += 1
        else:
            f = ficha_valida(literal if tipo == "minimo_redaccion_literal" else otra)
            f["riesgo_declarado"] = "mínimo"
            ok = "nivel_subestimado" in verificar(f)
        resultado[tipo][0] += ok
        resultado[tipo][1] += 1
    # una ficha íntegra y correcta no debe producir avisos
    sin_avisos = all(not verificar(ficha_valida(c[0])) for c in CASOS)
    print(json.dumps({"detectadas_de_aplicadas": resultado, "por_campo_borrado": por_campo,
                      "fichas_correctas_sin_avisos": sin_avisos}, ensure_ascii=False))


if __name__ == "__main__":
    main()
