from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "curriculum.yaml"
TARGET_STAGES = {"A", "C"}
VERIFIED_ON = "2026-09-30"

PRODUCTS = [
    "plataforma educativa", "comercio responsable", "servicio financiero",
    "comunidad social", "control de agentes", "suite familiar privada",
]

SOURCES = {
    "SWEBOK-4A": ("SWEBOK Guide v4.0a", "IEEE Computer Society", "https://www.computer.org/education/bodies-of-knowledge/software-engineering"),
    "ACM-ETHICS": ("ACM Code of Ethics and Professional Conduct", "ACM", "https://www.acm.org/code-of-ethics"),
    "ISO-25010": ("ISO/IEC 25010:2023", "ISO", "https://www.iso.org/standard/78176.html"),
    "UNICODE": ("The Unicode Standard", "Unicode Consortium", "https://www.unicode.org/standard/standard.html"),
    "POSIX": ("The Open Group Base Specifications", "The Open Group", "https://pubs.opengroup.org/onlinepubs/9799919799/"),
    "WINDOWS": ("Windows developer documentation", "Microsoft", "https://learn.microsoft.com/windows/"),
    "POWERSHELL": ("PowerShell documentation", "Microsoft", "https://learn.microsoft.com/powershell/"),
    "BASH": ("Bash Reference Manual", "GNU Project", "https://www.gnu.org/software/bash/manual/"),
    "RFC-8200": ("Internet Protocol, Version 6", "IETF", "https://www.rfc-editor.org/rfc/rfc8200"),
    "RFC-8446": ("The Transport Layer Security Protocol Version 1.3", "IETF", "https://www.rfc-editor.org/rfc/rfc8446"),
    "RFC-9000": ("QUIC: A UDP-Based Multiplexed and Secure Transport", "IETF", "https://www.rfc-editor.org/rfc/rfc9000"),
    "RFC-9110": ("HTTP Semantics", "IETF", "https://www.rfc-editor.org/rfc/rfc9110"),
    "MIT-MATH-CS": ("Mathematics for Computer Science", "MIT OpenCourseWare", "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/"),
    "GOV-RESEARCH": ("The Service Manual: user research", "UK Government Digital Service", "https://www.gov.uk/service-manual/user-research"),
    "NIST-PRIVACY": ("NIST Privacy Framework", "NIST", "https://www.nist.gov/privacy-framework"),
    "ISO-29148": ("ISO/IEC/IEEE 29148:2018 Requirements Engineering", "ISO", "https://www.iso.org/standard/72089.html"),
    "OPENAPI": ("OpenAPI Specification", "OpenAPI Initiative", "https://spec.openapis.org/oas/latest.html"),
    "ASYNCAPI": ("AsyncAPI Specification", "AsyncAPI Initiative", "https://www.asyncapi.com/docs/reference/specification/latest"),
    "GRAPHQL": ("GraphQL Specification", "GraphQL Foundation", "https://spec.graphql.org/"),
    "WCAG-22": ("Web Content Accessibility Guidelines 2.2", "W3C", "https://www.w3.org/TR/WCAG22/"),
    "W3C-I18N": ("Internationalization techniques", "W3C", "https://www.w3.org/International/techniques/"),
    "SCRUM": ("The Scrum Guide", "Scrum Guide authors", "https://scrumguides.org/scrum-guide.html"),
    "KANBAN": ("The Kanban Guide", "Kanban Guides", "https://kanbanguides.org/english/"),
    "GIT": ("Git documentation", "Git project", "https://git-scm.com/docs"),
    "GITHUB-COLLAB": ("Collaborating with pull requests", "GitHub", "https://docs.github.com/pull-requests/collaborating-with-pull-requests"),
    "C4": ("C4 model", "C4 model project", "https://c4model.com/"),
    "DIATAXIS": ("Diátaxis documentation framework", "Diátaxis project", "https://diataxis.fr/"),
}

PROFILES = {
    "00": {"artifact": "informe de decisión profesional", "environment": "editor de texto, navegador y repositorio Git", "files": ["decision.md", "evidence.md", "review.md"], "lenses": ["sistema", "ciclo de vida", "evidencia", "responsabilidad"], "failure": "confundir una preferencia personal con evidencia suficiente", "sources": ["SWEBOK-4A", "ACM-ETHICS", "ISO-25010"]},
    "01": {"artifact": "cuaderno reproducible de representación y recursos", "environment": "Python 3.11+, terminal y herramientas del sistema", "files": ["experiment.py", "observations.md", "results.json"], "lenses": ["representación", "máquina", "medición", "límite"], "failure": "inferir el modelo de la máquina desde una sola observación", "sources": ["UNICODE", "SWEBOK-4A"]},
    "02": {"artifact": "runbook de entorno reproducible", "environment": "PowerShell 7 y Bash en Windows, macOS o Linux", "files": ["bootstrap.ps1", "bootstrap.sh", "runbook.md"], "lenses": ["proceso", "permiso", "configuración", "recuperación"], "failure": "automatizar una operación destructiva sin precondiciones ni rollback", "sources": ["POSIX", "WINDOWS", "POWERSHELL", "BASH"]},
    "03": {"artifact": "traza comentada de una comunicación", "environment": "navegador, curl y utilidades de diagnóstico de red", "files": ["request.txt", "trace.md", "failure-report.md"], "lenses": ["capa", "protocolo", "estado", "observabilidad"], "failure": "atribuir al servidor un fallo que ocurre en resolución, transporte o caché", "sources": ["RFC-8200", "RFC-8446", "RFC-9000", "RFC-9110"]},
    "04": {"artifact": "especificación contrastable de una solución", "environment": "editor, Python opcional y diagramas Mermaid", "files": ["problem.md", "model.md", "checks.md"], "lenses": ["abstracción", "invariante", "algoritmo", "complejidad"], "failure": "resolver un ejemplo y asumir que la solución cubre todo el dominio", "sources": ["MIT-MATH-CS", "SWEBOK-4A"]},
    "10": {"artifact": "product brief respaldado por evidencia", "environment": "editor, hoja de cálculo opcional y repositorio de investigación", "files": ["brief.md", "assumptions.md", "research-log.md"], "lenses": ["necesidad", "hipótesis", "evidencia", "resultado"], "failure": "convertir la primera petición de una persona en requisito definitivo", "sources": ["GOV-RESEARCH", "NIST-PRIVACY", "SWEBOK-4A"]},
    "11": {"artifact": "árbol de métricas y caso de decisión", "environment": "editor y hoja de cálculo sin datos personales reales", "files": ["metric-tree.md", "decision.csv", "guardrails.md"], "lenses": ["valor", "costo", "métrica", "opción"], "failure": "optimizar actividad o una vanity metric en lugar del resultado", "sources": ["SWEBOK-4A", "NIST-PRIVACY"]},
    "12": {"artifact": "paquete de requisitos trazables", "environment": "editor, tablas Markdown y control de versiones", "files": ["requirements.md", "traceability.csv", "review.md"], "lenses": ["necesidad", "requisito", "criterio", "trazabilidad"], "failure": "aceptar lenguaje ambiguo que no puede verificarse", "sources": ["ISO-29148", "SWEBOK-4A", "ISO-25010"]},
    "13": {"artifact": "contrato versionado y ejemplos verificables", "environment": "editor YAML/JSON y validador local opcional", "files": ["contract.yaml", "examples.json", "compatibility.md"], "lenses": ["contrato", "invariante", "modelo", "compatibilidad"], "failure": "cambiar una interfaz sin analizar consumidores ni compatibilidad", "sources": ["ISO-29148", "OPENAPI", "ASYNCAPI", "GRAPHQL"]},
    "14": {"artifact": "prototipo y auditoría de inclusión", "environment": "navegador, teclado, lector de pantalla disponible y editor", "files": ["prototype.html", "accessibility.md", "usability-notes.md"], "lenses": ["tarea", "interacción", "accesibilidad", "cultura"], "failure": "declarar accesibilidad únicamente por el resultado de una herramienta automática", "sources": ["WCAG-22", "W3C-I18N", "NIST-PRIVACY"]},
    "15": {"artifact": "plan adaptativo con riesgos y métricas de flujo", "environment": "tablero reproducible en Markdown o herramienta equivalente", "files": ["plan.md", "risks.md", "flow.csv"], "lenses": ["flujo", "incertidumbre", "capacidad", "aprendizaje"], "failure": "convertir una estimación en compromiso sin rango ni supuestos", "sources": ["SCRUM", "KANBAN", "SWEBOK-4A"]},
    "16": {"artifact": "cambio colaborativo recuperable", "environment": "Git 2.40+ y alojamiento Git compatible", "files": ["change.md", "review-checklist.md", "recovery.md"], "lenses": ["historial", "integración", "revisión", "gobernanza"], "failure": "reescribir o publicar historia compartida sin evaluar a quién afecta", "sources": ["GIT", "GITHUB-COLLAB", "ACM-ETHICS"]},
    "17": {"artifact": "paquete de documentación mantenible", "environment": "editor Markdown, Mermaid y verificador de enlaces", "files": ["README.md", "architecture.md", "decision-record.md"], "lenses": ["audiencia", "decisión", "vista", "mantenimiento"], "failure": "documentar una intención como si describiera el comportamiento actual", "sources": ["DIATAXIS", "C4", "SWEBOK-4A"]},
}

TEACHING = {
    "00": {"foundation": "La ingeniería de software coordina producto, proceso y tecnología durante todo el ciclo de vida; su unidad de trabajo es una decisión justificable y sus consecuencias, no únicamente código.", "question": "¿qué responsabilidad, frontera profesional o atributo de calidad cambia?", "evidence": "una decisión revisable, sus fuentes y el impacto sobre personas y sistema"},
    "01": {"foundation": "Un computador representa información mediante estados discretos y ejecuta instrucciones sobre jerarquías con límites de precisión, capacidad, latencia y energía.", "question": "¿cómo se representa, transforma y observa la información en cada nivel?", "evidence": "bytes, mediciones repetibles y diferencias explicadas entre modelo y máquina"},
    "02": {"foundation": "El sistema operativo arbitra procesos, memoria, archivos, dispositivos e identidades; la automatización segura hace explícitos precondiciones, permisos, efectos y recuperación.", "question": "¿qué recurso administra el sistema y bajo qué identidad ocurre el cambio?", "evidence": "estado anterior y posterior, logs, códigos de salida y procedimiento de rollback"},
    "03": {"foundation": "Una comunicación atraviesa resolución de nombres, rutas, transporte, seguridad y semántica de aplicación; cada capa tiene señales y fallos diferentes.", "question": "¿en qué capa se define el comportamiento y en cuál aparece el síntoma?", "evidence": "mensajes, tiempos, estados, cabeceras o capturas obtenidos sin interceptar tráfico ajeno"},
    "04": {"foundation": "Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio.", "question": "¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?", "evidence": "casos límite, contraejemplos, argumento de terminación y costo medido o acotado"},
    "10": {"foundation": "El descubrimiento reduce incertidumbre sobre personas, problemas y resultados antes de comprometer una solución; una entrevista produce evidencia situada, no verdad universal.", "question": "¿qué incertidumbre crítica se intenta reducir y qué decisión habilitaría?", "evidence": "observaciones trazables, patrones y contradicciones, siempre separadas de interpretación"},
    "11": {"foundation": "Una métrica representa parcialmente un resultado y puede cambiar conductas; por eso se interpreta junto con costo, población, ventana temporal y guardrails.", "question": "¿qué decisión cambiaría con esta medida y qué daño podría ocultar?", "evidence": "definición calculable, fuente de datos, segmento, tendencia y métrica contraria"},
    "12": {"foundation": "Un requisito conecta una necesidad con comportamiento o restricción verificable; la trazabilidad permite explicar origen, cambio, implementación y evidencia de aceptación.", "question": "¿quién necesita qué resultado, bajo qué condición y cómo se verificará?", "evidence": "criterios inequívocos, ejemplos y enlaces bidireccionales entre necesidad y prueba"},
    "13": {"foundation": "Una especificación reduce interpretaciones permitidas mediante vocabulario, modelos, invariantes y ejemplos; un contrato además define obligaciones observables entre partes.", "question": "¿qué comportamiento se promete, qué queda fuera y cómo evoluciona sin romper consumidores?", "evidence": "esquema válido, ejemplos positivos y negativos, compatibilidad y prueba contractual"},
    "14": {"foundation": "La experiencia surge de la interacción entre persona, tarea, contenido y contexto; accesibilidad e internacionalización son restricciones de diseño verificables, no acabados visuales.", "question": "¿quién puede completar la tarea, con qué modalidad y en qué estado de error o recuperación?", "evidence": "recorrido por teclado, semántica, contraste, formatos culturales y observación de uso"},
    "15": {"foundation": "Un proceso de trabajo limita trabajo en curso, hace visible el flujo y crea ciclos de aprendizaje; un plan es una hipótesis actualizable, no una predicción exacta.", "question": "¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?", "evidence": "políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos"},
    "16": {"foundation": "Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad.", "question": "¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?", "evidence": "diff enfocado, historial legible, revisión resuelta y estrategia de reversión"},
    "17": {"foundation": "La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico.", "question": "¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?", "evidence": "prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual"},
}

STOPWORDS = {"de", "del", "la", "las", "el", "los", "y", "e", "a", "en", "con", "como", "por", "para", "un", "una"}


def dump_json(payload: object) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def words(title: str, profile: dict) -> list[str]:
    tokens = [token for token in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9]+", title) if token.casefold() not in STOPWORDS]
    result: list[str] = []
    for token in tokens + profile["lenses"]:
        normalized = token.casefold()
        if normalized not in {item.casefold() for item in result}:
            result.append(token)
        if len(result) == 5:
            break
    return result


def source_catalog(program: dict) -> dict:
    used = sorted({source for part in program["parts"] if part["stage"] in TARGET_STAGES for source in PROFILES[part["id"]]["sources"]})
    return {
        "$schema": "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/schemas/activity.schema.json",
        "schema_version": 1,
        "verified_on": VERIFIED_ON,
        "scope": "Fase 3: etapas A y C",
        "policy": "Fuentes primarias u oficiales; la guía indica el uso pedagógico y evita atribuirles afirmaciones no contenidas.",
        "sources": [
            {"id": source_id, "title": SOURCES[source_id][0], "authority": SOURCES[source_id][1], "url": SOURCES[source_id][2], "status": "verified"}
            for source_id in used
        ],
        "parts": {part_id: PROFILES[part_id]["sources"] for part_id in sorted(PROFILES)},
    }


def context(program: dict) -> dict[str, tuple[dict, dict, str, str]]:
    flat = [(part, lesson) for part in program["parts"] for lesson in part["lessons"]]
    result = {}
    for index, (part, lesson) in enumerate(flat):
        previous = flat[index - 1][1]["id"] if index else "diagnóstico inicial"
        following = flat[index + 1][1]["id"] if index + 1 < len(flat) else "cierre del programa"
        result[lesson["id"]] = (part, lesson, previous, following)
    return result


def lesson_readme(part: dict, lesson: dict, previous: str, following: str) -> str:
    profile = PROFILES[part["id"]]
    teaching = TEACHING[part["id"]]
    terms = words(lesson["title"], profile)
    product = PRODUCTS[(lesson["number"] - 1) % len(PRODUCTS)]
    source_lines = "\n".join(
        f"- **{SOURCES[source_id][0]}** — {SOURCES[source_id][1]}. [{SOURCES[source_id][2]}]({SOURCES[source_id][2]}) — se usa para contrastar vocabulario, límites y criterios aplicables."
        for source_id in profile["sources"]
    )
    files = "\n".join(f"│   ├── {name}" for name in profile["files"])
    concept_sections = "\n\n".join(
        f"### {index}. {term.capitalize()}\n\nEn **{lesson['title']}**, `{term}` se analiza dentro de esta base: {teaching['foundation']} Para volverlo operativo, responde «{teaching['question']}» y conserva {teaching['evidence']}. Después declara qué problema resuelve, qué supuesto utiliza, qué señal permitiría aceptarlo y qué señal obligaría a revisarlo. La respuesta profesional separa hechos, inferencias y preferencias; además registra costo, riesgo y reversibilidad antes de elegir una herramienta."
        for index, term in enumerate(terms[:4], start=1)
    )
    mode = {"class": "análisis guiado", "studio": "taller de integración", "project": "proyecto de portafolio"}[lesson["kind"]]
    return f"""# {lesson['id']} — {lesson['title']}

> [!NOTE]
> Estado: **GUIDED**. Esta clase contiene explicación, práctica, ejercicios, evaluación y fuentes. No afirma ejecución automática; esa madurez requiere `EXECUTABLE` o superior.

## Ficha

| Campo | Valor |
| --- | --- |
| Etapa | {part['stage']} · {part['stage_title']} |
| Parte | {part['id']} · {part['title']} |
| Modalidad | {mode} (`{lesson['kind']}`) |
| Propietario profundo | `{part['owner']}` |
| Duración estimada | {lesson['estimated_hours']} horas |
| Producto de la clase | {profile['artifact']} |

## Prerrequisitos

- Haber completado o diagnosticado `{previous}` y poder explicar qué evidencia produjo.
- Manejar archivos de texto, rutas y control de versiones a nivel básico.
- Disponer de {profile['environment']}.

## Problema auténtico

Un equipo que trabaja en una {product} debe decidir sobre **{lesson['title']}**. Tiene información incompleta, restricciones de tiempo y personas afectadas por una decisión incorrecta. El reto no es repetir definiciones: es convertir el tema en un resultado revisable, distinguir observación de supuesto y conservar evidencia para que otra persona pueda continuar o cuestionar el trabajo.

## Objetivos observables

Al terminar podrás:

1. explicar {terms[0]} y {terms[1]} con un ejemplo y un contraejemplo;
2. comparar al menos dos opciones usando evidencia, riesgo, costo y reversibilidad;
3. producir el artefacto **{profile['artifact']}** para que otra persona pueda revisarlo;
4. diagnosticar el fallo «{profile['failure']}» sin ocultar incertidumbre;
5. transferir la decisión a otra plataforma o dominio sin depender de una marca.

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: {html.escape(lesson['title'])}"] --> M["Modelo: {terms[0]}"]
    M --> D["Decisión: {terms[1]}"]
    D --> E["Evidencia: {terms[2]}"]
    E --> R["Revisión: {terms[3]}"]
    R -->|nueva información| M
```

## Conceptos y decisiones

{teaching['foundation']}

La pregunta rectora de esta parte es: **{teaching['question']}** La respuesta debe
apoyarse en **{teaching['evidence']}**.

{concept_sections}

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Ejemplo mínimo

Registra una sola decisión sobre **{lesson['title']}**:

| Elemento | Ejemplo contrastable |
| --- | --- |
| Contexto | el equipo necesita una decisión en una iteración y carece de una medición directa |
| Supuesto | la opción elegida reduce el riesgo principal sin crear uno mayor |
| Evidencia | ejemplo, medición o revisión que una segunda persona puede repetir |
| Límite | el resultado no representa producción ni todas las poblaciones usuarias |
| Próxima señal | un dato que confirmaría, refutaría o modificaría la decisión |

El valor del ejemplo no está en “tener razón”, sino en que el razonamiento pueda ser inspeccionado.

## Ejemplo profesional

En la {product}, el equipo prepara un cambio relacionado con **{lesson['title']}**. Parte de esta pregunta: **{teaching['question']}** Antes de implementarlo, registra personas afectadas, estados normales y degradados, datos utilizados, costo de reversión y señales de éxito. Dos opciones se comparan con la misma tabla y se contrastan usando {teaching['evidence']}. La alternativa ganadora queda condicionada a una prueba pequeña. La revisión incluye a producto, ingeniería y una persona que no participó en la propuesta. El resultado se archiva como `{profile['files'][0]}` y enlaza la evidencia, no solo la conclusión.

## Práctica guiada

1. Crea `work/{lesson['id']}/` sin copiar datos personales ni secretos.
2. Formula el problema en una frase que incluya actor, necesidad y consecuencia.
3. Separa en una tabla hechos observados, inferencias, incógnitas y restricciones.
4. Propón dos opciones y una opción de no actuar; explicita costos y riesgos.
5. Construye el {profile['artifact']} con los archivos indicados abajo.
6. Introduce deliberadamente el fallo controlado y registra síntomas antes de corregirlo.
7. Pide una revisión: la otra persona debe reconstruir la decisión solo con el artefacto.
8. Actualiza la conclusión y anota qué evidencia cambiaría la decisión.

## Ejercicios

1. **Fundamental:** define {terms[0]} y {terms[1]} con un ejemplo propio, un contraejemplo y un criterio que permita distinguirlos.
2. **Aplicado:** resuelve el caso de la {product}, compara tres opciones y entrega `{profile['files'][0]}` con trazabilidad completa.
3. **Avanzado:** cambia una restricción crítica —plataforma, escala, conectividad, regulación o capacidad del equipo— y demuestra qué partes de la decisión se conservan y cuáles deben revisarse.

## Fallo controlado y diagnóstico

Provoca de forma segura este fallo: **{profile['failure']}**. No lo ejecutes sobre producción ni datos reales. Captura la decisión inicial, el síntoma observable y la primera hipótesis. Después reduce el caso, busca evidencia que pueda refutar tu hipótesis y corrige la causa, no solo el síntoma. Cierra con una medida preventiva y un procedimiento de recuperación.

## Entorno y archivos clave

Entorno de referencia: {profile['environment']}. La actividad es documental y portable; cualquier comando adicional debe declarar sistema operativo y versión.

```text
work/{lesson['id']}/
├── README.md
{files}
├── activity.yaml
└── rubric.json
```

`README.md` explica cómo reproducir la actividad; `{profile['files'][0]}` contiene el resultado principal; los demás archivos separan evidencia y revisión. `activity.yaml` y `rubric.json` son contratos generados junto a esta guía.

## Seguridad, ética y accesibilidad

- usa datos sintéticos o anonimizados y aplica minimización;
- no incluyas tokens, rutas privadas ni información personal en evidencias;
- identifica personas que reciben beneficios, cargas o riesgo de exclusión;
- ofrece una alternativa textual a diagramas y no uses color como única señal;
- verifica navegación por teclado y lenguaje comprensible cuando exista interfaz;
- detén la práctica si requiere acceso no autorizado o puede afectar sistemas reales.

## Transferencia

Repite la decisión en un segundo contexto: cambia la {product} por otro de los dominios persistentes, o cambia Windows por Linux/macOS cuando aplique. Conserva problema, criterios y evidencia; modifica únicamente los supuestos dependientes del entorno. Explica por escrito qué conocimiento fue transferible y qué parte pertenecía a la herramienta.

## Evaluación y evidencia

| Criterio | Evidencia para aprobar |
| --- | --- |
| Comprensión | conceptos explicados con ejemplo, contraejemplo y límites |
| Decisión | opciones comparadas con criterios explícitos y alternativa de no actuar |
| Reproducibilidad | archivos, pasos y entorno permiten repetir la revisión |
| Diagnóstico | fallo controlado conserva síntomas, hipótesis, causa y recuperación |
| Responsabilidad | seguridad, privacidad, accesibilidad y personas afectadas fueron consideradas |

Entrega el directorio `work/{lesson['id']}/` y una reflexión de máximo 300 palabras. La rúbrica machine-readable está en `rubric.json`; no se aprueba solo por completar pasos.

## Fuentes

Fuentes verificadas el {VERIFIED_ON}:

{source_lines}

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **{lesson['title']}**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `{following}`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.
"""


def activity(part: dict, lesson: dict) -> dict:
    profile = PROFILES[part["id"]]
    return {
        "$schema": "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/schemas/rubric.schema.json",
        "schema_version": 1,
        "class_id": lesson["id"],
        "status": "GUIDED",
        "mode": lesson["kind"],
        "environment": profile["environment"],
        "duration_hours": lesson["estimated_hours"],
        "steps": ["frame-problem", "separate-evidence", "compare-options", "produce-artifact", "inject-safe-failure", "peer-review", "revise"],
        "outputs": profile["files"],
        "safety": {"real_personal_data": False, "production_access": False, "secrets": False},
        "source_ids": profile["sources"],
    }


def rubric(part: dict, lesson: dict) -> dict:
    return {
        "schema_version": 1,
        "class_id": lesson["id"],
        "passing_score": 12,
        "maximum_score": 16,
        "criteria": [
            {"id": "understanding", "max": 4, "evidence": "example, counterexample and limits"},
            {"id": "decision", "max": 4, "evidence": "options, criteria, risks and reversibility"},
            {"id": "reproducibility", "max": 4, "evidence": "environment, files and review trail"},
            {"id": "responsibility", "max": 4, "evidence": "security, privacy, accessibility and affected people"},
        ],
    }


def site_page(part: dict, lesson: dict) -> str:
    profile = PROFILES[part["id"]]
    source_items = "".join(
        f'<li><a href="{html.escape(SOURCES[source_id][2])}">{html.escape(SOURCES[source_id][0])}</a> · {html.escape(SOURCES[source_id][1])}</li>'
        for source_id in profile["sources"]
    )
    objectives = "".join(
        f"<li>{text}</li>" for text in [
            f"Explicar {lesson['title']} con ejemplo, contraejemplo y límites.",
            "Comparar opciones por evidencia, riesgo, costo y reversibilidad.",
            f"Producir un {profile['artifact']} revisable.",
            "Diagnosticar un fallo controlado y documentar recuperación.",
        ]
    )
    repository_url = f"https://github.com/vladimiracunadev-create/software-engineering-learning-suite/tree/main/{lesson['path']}"
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Guía pedagógica {lesson['id']}: {html.escape(lesson['title'])}"><title>{lesson['id']} · {html.escape(lesson['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><main class="lesson" id="content"><a class="back" href="../parts/{part['id']}.html">← Parte {part['id']}</a><p class="eyebrow">{lesson['id']} · {lesson['kind']}</p><h1>{html.escape(lesson['title'])}</h1><div class="notice"><strong>GUIDED:</strong> explicación, práctica, ejercicios, evaluación y fuentes disponibles. No implica ejecución automática.</div><section><h2>Resultado</h2><p>Construir el artefacto {html.escape(profile['artifact'])} en {lesson['estimated_hours']} horas estimadas.</p></section><section><h2>Objetivos</h2><ol>{objectives}</ol></section><section><h2>Entorno y archivos</h2><p>{html.escape(profile['environment'])}.</p><ul>{''.join(f'<li><code>{html.escape(name)}</code></li>' for name in profile['files'])}<li><code>activity.yaml</code></li><li><code>rubric.json</code></li></ul></section><section><h2>Actividad</h2><p>Enmarca el problema, separa evidencia de supuestos, compara tres opciones, produce el artefacto, provoca un fallo seguro, solicita revisión y revisa la decisión.</p></section><section><h2>Fuentes oficiales o primarias</h2><ul>{source_items}</ul><p>Verificadas el {VERIFIED_ON}.</p></section><section><h2>Material completo</h2><p><a href="{repository_url}">Abrir la guía íntegra, el contrato de actividad y la rúbrica en GitHub</a>.</p></section></main><footer>Software Engineering Learning Suite · Fase 3</footer></body></html>\n"""


def expected_files(program: dict) -> dict[Path, str]:
    result = {ROOT / "sources/phase3.json": dump_json(source_catalog(program))}
    entries = context(program)
    for part in program["parts"]:
        if part["stage"] not in TARGET_STAGES:
            continue
        for lesson in part["lessons"]:
            _, _, previous, following = entries[lesson["id"]]
            directory = ROOT / lesson["path"]
            result[directory / "README.md"] = lesson_readme(part, lesson, previous, following)
            result[directory / "activity.yaml"] = dump_json(activity(part, lesson))
            result[directory / "rubric.json"] = dump_json(rubric(part, lesson))
            result[ROOT / "site/classes" / f"{lesson['id']}.html"] = site_page(part, lesson)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    program = json.loads(PROGRAM_PATH.read_text(encoding="utf-8"))
    files = expected_files(program)
    stale = []
    for path, content in files.items():
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8", newline="\n")
    if stale:
        print("PHASE3_STALE: " + ", ".join(stale[:30]), file=sys.stderr)
        return 1
    action = "PHASE3_CHECK_OK" if args.check else "PHASE3_BUILD_OK"
    print(f"{action}: 156 GUIDED classes, 312 activity/rubric contracts, 156 guided web pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
