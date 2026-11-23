#!/usr/bin/env python3
"""Enriquece y verifica las rutas profesionales sin reemplazar su contenido manual."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote

import cross_references
import program_state as ps
from role_profiles import (
    DEVELOPED,
    PART_CONTEXT,
    PART_STATUS,
    PLANNED_BY_ROLE,
    PLANNED_PARTS,
    PROFILES,
    SOURCES,
)


ROOT = Path(__file__).resolve().parents[1]
ROLE_ROOT = ROOT / "roles"
CURRICULUM = ROOT / "curriculum.yaml"
VISUAL_START = "<!-- role-visual:start -->"
VISUAL_END = "<!-- role-visual:end -->"
DEPTH_START = "<!-- role-depth:start -->"
DEPTH_END = "<!-- role-depth:end -->"
MAIN_START = "<!-- role-map:start -->"
MAIN_END = "<!-- role-map:end -->"
INDEX_START = "<!-- role-index-depth:start -->"
INDEX_END = "<!-- role-index-depth:end -->"


# Agrupación gruesa de las guías para el README raíz: (familia, [(archivo, foco en una línea)]).
ROLE_GROUPS: list[tuple[str, list[tuple[str, str]]]] = [
    (
        '💻 Construcción de productos y sistemas',
        [
            ('software-engineer.md', 'ciclo de vida de extremo a extremo'),
            ('systems-programmer.md', 'memoria, procesos, concurrencia y recursos'),
            ('backend-engineer.md', 'servicios, dominio, datos y operación'),
            ('frontend-engineer.md', 'interfaces accesibles, rápidas y mantenibles'),
            ('full-stack-engineer.md', 'fragmentos verticales con contratos y despliegue'),
            ('mobile-engineer.md', 'ciclo de vida, offline, sincronización y distribución'),
            ('desktop-engineer.md', 'integración nativa, instalación y actualización'),
            ('embedded-iot-engineer.md', 'firmware, RTOS, energía, telemetría y OTA'),
            ('safety-critical-software-engineer.md', 'hazards, controles y assurance'),
            ('saas-product-platform-engineer.md', 'tenencia, planes, uso facturable y economía unitaria'),
        ],
    ),
    (
        '🔗 APIs, datos y sistemas distribuidos',
        [
            ('api-engineer.md', 'contratos, compatibilidad, experiencia y gobernanza'),
            ('data-engineer.md', 'pipelines, contratos, calidad y lineage'),
            ('database-reliability-engineer.md', 'capacidad, migraciones y recuperación'),
            ('distributed-systems-engineer.md', 'consistencia, coordinación y fallos parciales'),
        ],
    ),
    (
        '🧪 Calidad, inclusión y análisis',
        [
            ('qa-test-engineer.md', 'riesgo, exploración y automatización'),
            ('performance-engineer.md', 'profiling, carga, percentiles y capacidad'),
            ('accessibility-engineer.md', 'WCAG, tecnología asistiva y prevención de barreras'),
            ('internationalization-engineer.md', 'Unicode, locales, tiempo, RTL y localización'),
            ('requirements-engineer.md', 'elicitación, reglas y trazabilidad'),
        ],
    ),
    (
        '🚀 Cloud, entrega, confiabilidad y plataforma',
        [
            ('devops-engineer.md', 'entrega repetible, cadena de suministro y rollback'),
            ('build-release-engineer.md', 'artefactos, procedencia, firma y promoción'),
            ('cloud-engineer.md', 'IAM, infraestructura, automatización y recuperación'),
            ('site-reliability-engineer.md', 'SLO, capacidad, incidentes y aprendizaje'),
            ('observability-engineer.md', 'logs, métricas, trazas y diagnóstico'),
            ('platform-engineer.md', 'IDP, golden paths y autoservicio'),
            ('developer-experience-engineer.md', 'tooling, onboarding y feedback loops'),
            ('chaos-resilience-engineer.md', 'hipótesis de estado estable, inyección de fallos y diseño para degradar'),
        ],
    ),
    (
        '🔐 Gobierno, economía y sostenibilidad',
        [
            ('security-engineer.md', 'secure design, AppSec y respuesta'),
            ('compliance-engineer.md', 'obligación, control, prueba y evidencia'),
            ('finops-engineer.md', 'costes unitarios, forecast y decisiones de valor'),
            ('green-software-engineer.md', 'eficiencia, carbono y GreenOps medidos'),
            ('technical-writer.md', 'información técnica usable y mantenible'),
            ('open-source-innersource-engineer.md', 'contribución, governance y ownership'),
        ],
    ),
    (
        '🏛️ Arquitectura, evolución y liderazgo',
        [
            ('legacy-modernization-engineer.md', 'arqueología, compatibilidad y retiro'),
            ('software-architect.md', 'atributos, límites, trade-offs y evolución'),
            ('solutions-architect.md', 'contexto, integración, adopción y transición'),
            ('technical-product-engineer.md', 'discovery, economía y factibilidad'),
            ('technical-leadership.md', 'influencia, RFC, arquitectura y mentoring'),
            ('engineering-manager.md', 'personas, flujo, riesgo y sostenibilidad'),
            ('cto.md', 'estrategia, organización, portafolio y riesgo'),
        ],
    ),
    (
        '🤖 Ingeniería con inteligencia artificial',
        [
            ('ai-augmented-software-engineer.md', 'desarrollo con agentes, evals y guardrails'),
            ('ai-systems-engineer.md', 'productos con modelos, datasets, fallback y operación'),
            ('agentic-harness-engineer.md', 'harness, contexto, herramientas, bucles, evaluación y recuperación de agentes'),
            ('domain-methodology-engineer.md', 'TDD, BDD, ATDD, DDD, contratos y SDD como práctica de equipo'),
            ('mlops-ml-platform-engineer.md', 'datos, entrenamiento reproducible, servicio, deriva y reversión de modelos'),
            ('ai-governance-responsible-ai-engineer.md', 'riesgo, equidad, supervisión humana, regulación y evidencia de IA'),
        ],
    ),
    (
        '⚙️ Runtimes y plataformas modernas',
        [
            ('runtime-systems-engineer.md', 'WebAssembly, eBPF, aceleradores, sandboxes y hardware seguro'),
        ],
    ),
]


# Filas nuevas de la tabla de roles/README.md: (familia, nombre, misión corta). Las filas existentes conservan su texto
# y solo se recalcula la columna «Ruta principal» a partir del núcleo de cada perfil.
INDEX_ROWS_NEW = {
    "saas-product-platform-engineer.md": ("Producto digital", "SaaS / Product Platform Engineer", "aislar, medir, limitar y cobrar el uso de un producto compartido por muchos clientes"),
    "chaos-resilience-engineer.md": ("Confiabilidad", "Chaos & Resilience Engineer", "demostrar con experimentos controlados que el sistema cumple su tarea útil cuando falla"),
}


def collapse_parts(part_ids: list[str]) -> str:
    """«01, 23, 32–33» a partir de los números de parte del núcleo."""

    numbers = sorted(int(part) for part in part_ids)
    chunks: list[str] = []
    start = prev = numbers[0]
    for number in [*numbers[1:], None]:
        if number is not None and number == prev + 1:
            prev = number
            continue
        chunks.append(f"{start:02d}" if start == prev else f"{start:02d}–{prev:02d}")
        if number is not None:
            start = prev = number
    return ", ".join(chunks)


def render_index_table(text: str) -> str:
    """Recalcula la columna «Ruta principal», añade filas de roles nuevos y los conteos de la prosa."""

    lines = text.splitlines()
    out: list[str] = []
    last_row = -1
    for line in lines:
        match = re.search(r"\]\(([a-z0-9-]+\.md)\) \|", line)
        if line.startswith("| ") and match and match.group(1) in PROFILES:
            cells = line.split(" | ")
            cells[-1] = collapse_parts(list(PROFILES[match.group(1)]["core"])) + " |"
            line = " | ".join(cells)
            last_row = len(out)
        out.append(line)
    present = "\n".join(out)
    for filename, (family, name, mission) in INDEX_ROWS_NEW.items():
        if f"]({filename})" in present:
            continue
        row = f"| {family} | [{name}]({filename}) | {mission} | {collapse_parts(list(PROFILES[filename]['core']))} |"
        out.insert(last_row + 1, row)
        last_row += 1
    result = "\n".join(out) + ("\n" if text.endswith("\n") else "")
    count = len(PROFILES)
    developed = ps.developed_parts()
    planned = ps.planned_parts()
    if planned:
        state = f"{len(developed)} de {ps.PLANNED_PART_COUNT} partes publicadas, {ps.part_ranges(developed)}; {ps.the_parts(planned)} {ps.verb_planned(planned)}"
    else:
        state = f"{ps.PLANNED_PART_COUNT} partes, 00–{ps.LAST_PART_NUMBER:02d}, todas publicadas"
    text_state = re.compile(r"Las rutas convierten las partes del programa \([^)]*\)")
    result = text_state.sub(lambda _m: f"Las rutas convierten las partes del programa ({state})", result)
    result = re.sub(r"Las \d+ guías superan", f"Las {count} guías superan", result)
    result = re.sub(r"## Mapa de \d+ roles", f"## Mapa de {count} roles", result)
    result = re.sub(r"no son \d+ cursos ni una promesa de empleo, sino \d+ lentes", f"no son {count} cursos ni una promesa de empleo, sino {count} lentes", result)
    return result


def render_main_intro(text: str) -> str:
    count = len(PROFILES)
    text = re.sub(r"El programa ofrece \*\*\d+ guías profesionales", f"El programa ofrece **{count} guías profesionales", text)
    text = re.sub(r"No son \d+ cursos", f"No son {count} cursos", text)
    text = re.sub(r"índice y \d+ guías profesionales", f"índice y {count} guías profesionales", text)
    text = re.sub(r"\*\*\d+ rutas profesionales\*\*", f"**{count} rutas profesionales**", text)
    return text


def replace_or_insert(
    text: str,
    start: str,
    end: str,
    block: str,
    anchor: str,
) -> str:
    rendered = f"{start}\n{block.rstrip()}\n{end}\n"
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end) + r"\n?", re.S)
    if pattern.search(text):
        return pattern.sub(rendered, text, count=1)
    if anchor not in text:
        raise AssertionError(f"No se encontró el ancla editorial: {anchor}")
    return text.replace(anchor, rendered + "\n" + anchor, 1)


def load_curriculum() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, object]]]:
    payload = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    classes: dict[str, dict[str, str]] = {}
    parts: dict[str, dict[str, object]] = {}
    for part in payload["parts"]:
        parts[part["id"]] = part
        for lesson in part["lessons"]:
            classes[lesson["id"]] = {**lesson, "part": part["id"]}
    return classes, parts


def parse_identity(text: str) -> tuple[str, str]:
    first = text.splitlines()[0]
    if not first.startswith("# "):
        raise AssertionError("La guía no comienza con un título H1")
    title = first.removeprefix("# ").strip()
    mission: list[str] = []
    for line in text.splitlines()[1:]:
        if line.startswith("## "):
            break
        if line.startswith("> **Entrada habitual:**"):
            break
        if line.startswith(">"):
            value = line.removeprefix(">").strip()
            if value:
                mission.append(value)
    return title, " ".join(mission)


def class_link(class_id: str, classes: dict[str, dict[str, str]], prefix: str) -> str:
    item = classes[class_id]
    return f"[{class_id}]({prefix}{item['path']}/README.md)"


def detailed_class_link(class_id: str, classes: dict[str, dict[str, str]], prefix: str) -> str:
    item = classes[class_id]
    return f"[{class_id} · {item['title']}]({prefix}{item['path']}/README.md)"


def part_link(part_id: str, parts: dict[str, dict[str, object]], prefix: str) -> str:
    part = parts[part_id]
    return f"[Parte {part_id} · {part['title']}]({prefix}{part['path']}/README.md)"


def se_id(number: int) -> str:
    return f"SE-{number:03d}"


def planned_range(part_id: str) -> str:
    _, first, last = PLANNED_PARTS[part_id]
    return f"{first}–{last}"


def pending_for_role(filename: str) -> dict[str, str]:
    """Partes planificadas que este rol espera y que siguen sin contenido."""

    return {
        part_id: text
        for part_id, text in PLANNED_BY_ROLE[filename].items()
        if PART_STATUS[part_id] == "planificada"
    }


def new_part_support_numbers(filename: str) -> list[int]:
    """Primera, sexta y última clase de cada parte nueva ya desarrollada que el rol esperaba."""

    numbers: list[int] = []
    for part_id in sorted(PLANNED_BY_ROLE[filename]):
        if PART_STATUS[part_id] == "desarrollada":
            first = ps.part_first_class(int(part_id))
            numbers.extend([first, first + 5, first + ps.CLASSES_PER_PART - 1])
    return numbers


def developed_support(filename: str, core: dict[str, list[str]], classes: dict[str, dict[str, str]]) -> list[str]:
    """Clases desarrolladas de apoyo no repetidas en el núcleo; verifica cada id."""

    in_core = {item for ids in core.values() for item in ids}
    result: list[str] = []
    for number in [*DEVELOPED[filename], *new_part_support_numbers(filename)]:
        class_id = se_id(number)
        if class_id not in classes:
            raise AssertionError(f"Clase de apoyo inexistente en curriculum.yaml: {class_id} ({filename})")
        if PART_STATUS.get(classes[class_id]["part"]) != "desarrollada":
            raise AssertionError(f"La clase de apoyo {class_id} no pertenece a una parte desarrollada ({filename})")
        if class_id not in in_core:
            result.append(class_id)
    return result


def shield(label: str, value: str, color: str) -> str:
    encoded_label = quote(label.replace("-", "--"), safe="")
    encoded_value = quote(value.replace("-", "--"), safe="")
    return f"https://img.shields.io/badge/{encoded_label}-{encoded_value}-{color}?style=for-the-badge"


def sentence(text: str) -> str:
    """Añade mayúscula inicial sin destruir siglas como ADR, API, SLO u OIDC."""

    return text[:1].upper() + text[1:]


def render_visual(title: str, profile_data: dict[str, object]) -> str:
    family = str(profile_data["family"])
    level = str(profile_data["level"])
    core = profile_data["core"]
    assert isinstance(core, dict)
    core_parts = " · ".join(f"P{part}" for part in core)
    return f'''<div align="center">

[![Familia]({shield("familia", family, "6f42c1")})](README.md)
[![Nivel]({shield("recorrido", level, "0969da")})](../ROADMAP.md)
[![Núcleo]({shield("núcleo", core_parts, "2da44e")})](#-partes-y-clases-asociadas)

**La guía conecta trabajo real, decisiones, clases concretas y evidencia defendible.**

</div>'''


def render_role_depth(
    filename: str,
    title: str,
    mission: str,
    profile_data: dict[str, object],
    classes: dict[str, dict[str, str]],
    parts: dict[str, dict[str, object]],
) -> str:
    family = str(profile_data["family"])
    level = str(profile_data["level"])
    flow = list(profile_data["flow"])
    decisions = list(profile_data["decisions"])
    metrics = list(profile_data["metrics"])
    scenario = tuple(profile_data["scenario"])
    project = tuple(profile_data["project"])
    source_ids = list(profile_data["sources"])
    adjacent = list(profile_data["adjacent"])
    core = dict(profile_data["core"])

    flow_nodes = "\n    ".join(
        f'{chr(65 + index)}["{icon} {label}"] --> {chr(66 + index)}'
        for index, (icon, label) in enumerate(
            zip(("🎯", "🧠", "🛠️", "🔎"), flow[:-1], strict=True)
        )
    )
    flow_nodes = flow_nodes.rsplit(" --> ", 1)[0] + f' --> E["📈 {flow[-1]}"]'

    part_rows: list[str] = []
    all_class_ids: list[str] = []
    for sequence, (part_id, class_ids) in enumerate(core.items(), start=1):
        all_class_ids.extend(class_ids)
        capability, evidence = PART_CONTEXT[part_id]
        links = "<br>".join(detailed_class_link(item, classes, "../") for item in class_ids)
        part_rows.append(
            f"| {sequence} | {part_link(part_id, parts, '../')} | {PART_STATUS[part_id]} | {links} | "
            f"Profundiza **{capability}** desde la responsabilidad del rol. | {sentence(evidence)}. |"
        )
    support_ids = developed_support(filename, core, classes)
    support_rows = chr(10).join(
        f"| {detailed_class_link(item, classes, '../')} | Parte {classes[item]['part']} |"
        for item in support_ids
    )
    planned = pending_for_role(filename)
    planned_rows = chr(10).join(
        f"| **Parte {part_id} · {PLANNED_PARTS[part_id][0]}** | `{PLANNED_PARTS[part_id][1]}`–`{PLANNED_PARTS[part_id][2]}` | {text} |"
        for part_id, text in sorted(planned.items())
    ) or "| — | — | Las partes que este rol esperaba ya están desarrolladas y figuran en el núcleo o en las clases de apoyo. |"
    developed_text = f"{ps.developed_label()} ({ps.class_ranges(ps.developed_parts())})"
    extension_block = render_extension_block()

    decision_rows = "\n".join(
        f"| **{name}** | {sentence(criterion)}. | {sentence(proof)}. |"
        for name, criterion, proof in decisions
    )
    metric_rows = "\n".join(
        f"| **{name}** | {sentence(meaning)}. | {sentence(trap)}. |"
        for name, meaning, trap in metrics
    )
    source_rows = "\n".join(
        f"- [{SOURCES[source_id][0]}]({SOURCES[source_id][2]}) — **{SOURCES[source_id][1]}**. "
        "Se usa como referencia primaria u oficial; la guía no sustituye la fuente."
        for source_id in source_ids
    )
    neighbor_links: list[str] = []
    for filename in adjacent:
        neighbor_text = (ROLE_ROOT / filename).read_text(encoding="utf-8").splitlines()[0].removeprefix("# ")
        neighbor_links.append(f"[{neighbor_text}]({filename})")
    class_start = all_class_ids[0]
    class_middle = all_class_ids[len(all_class_ids) // 2]
    class_end = all_class_ids[-1]
    first_decision = decisions[0][0]
    second_decision = decisions[1][0]
    third_decision = decisions[2][0]
    scenario_title, symptom, investigation, response = scenario
    project_title, project_goal, project_artifact = project

    return f'''## 🗺️ Sistema profesional del rol

```mermaid
flowchart LR
    {flow_nodes}
    classDef intent fill:#fff3cd,stroke:#9a6700,color:#24292f
    classDef work fill:#ddf4ff,stroke:#0969da,color:#24292f
    classDef proof fill:#dafbe1,stroke:#1a7f37,color:#24292f
    class A intent
    class B,C,D work
    class E proof
```

El gráfico no representa una cascada rígida. Muestra el bucle profesional que este rol
debe poder recorrer: comprender el contexto, tomar una decisión, intervenir, observar
el efecto y convertir lo aprendido en una mejora. En **{title}**, saltar directamente a
la herramienta suele ocultar el problema, mientras que terminar sin evidencia deja la
decisión en una opinión. La misión concreta es: {mission.rstrip('.')}. Cada transición
debe conservar supuestos, responsables y una forma de volver atrás.

<table>
<tr>
<td valign="top" width="50%">

### 🎯 Responde por

- decisiones propias de la familia **{family}**;
- el resultado observable, no sólo la actividad ejecutada;
- límites, riesgos, operación y deuda residual de su intervención;
- evidencia que otra persona pueda revisar o reproducir.

</td>
<td valign="top" width="50%">

### 🤝 Coordina con

- {"; ".join(neighbor_links)};
- producto y personas usuarias cuando cambia una tarea o outcome;
- seguridad, privacidad, accesibilidad y operación según el riesgo;
- quienes mantendrán el sistema después de la entrega.

</td>
</tr>
</table>

El título no concede autoridad automática. El alcance real depende del equipo, la
industria y la criticidad. Esta guía describe un recorrido desde **{level}**, pero una
vacante se evalúa por las decisiones que permite tomar, los sistemas que pone bajo
responsabilidad y la evidencia exigida, no por el nombre del cargo.

## 🧱 Partes y clases asociadas

La ruta distingue **parte** —unidad curricular con una capacidad acumulativa— de
**clase asociada** —punto concreto donde se estudia un mecanismo o una decisión. Las
clases siguientes forman el núcleo; no eliminan los prerrequisitos indicados en sus
propias páginas ni convierten en opcional la base común.

| Orden | Parte del programa | Estado | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- | --- |
{chr(10).join(part_rows)}

### ✅ Clases ya desarrolladas que sostienen la ruta hoy

El núcleo anterior apunta a la capacidad profesional completa. Estas clases de apoyo,
de las {developed_text}, también tienen contenido desarrollado y
permiten practicar el rol desde otros ángulos:

| Clase desarrollada | Parte |
| --- | --- |
{support_rows}

**Cómo recorrerla.** Empieza por {class_link(class_start, classes, '../')} para fijar el
primer mecanismo, usa {class_link(class_middle, classes, '../')} para integrar el
centro de la especialidad y llega a {class_link(class_end, classes, '../')} cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo vigente. {ps.the_parts(ps.developed_parts())} ({ps.class_ranges(ps.developed_parts())}) {"está" if len(ps.developed_parts()) == 1 else "están"}
> desarrolladas, a falta de una revisión editorial humana independiente. Esta ruta no
> declara aprobadas esas clases ni reemplaza el [roadmap](../ROADMAP.md).

{extension_block.format(planned_rows=planned_rows)}

## ⚖️ Decisiones y trade-offs que debes defender

| Decisión recurrente | Criterio profesional | Evidencia mínima antes de defenderla |
| --- | --- | --- |
{decision_rows}

La calidad de una decisión no se juzga porque coincida con una herramienta popular.
Debe hacer explícitos contexto, restricciones, alternativas descartadas, coste de
cambio y condición de revisión. En especial, **{first_decision}**, **{second_decision}**
y **{third_decision}** cambian de respuesta cuando cambia el riesgo. Una solución
correcta en un prototipo puede ser irresponsable en un sistema regulado; una solución
robusta para un servicio crítico puede ser desperdicio en una herramienta interna.

## 🚨 Escenario profesional: {scenario_title}

**Síntoma.** {sentence(symptom)}. La respuesta madura evita convertir la primera
correlación en causa y conserva evidencia antes de modificar el sistema.

```mermaid
flowchart LR
    S["⚠️ Síntoma"] --> H["🔎 Hipótesis"]
    H --> C["🧯 Contención"]
    C --> D["🧠 Diagnóstico"]
    D --> R["🛠️ Recuperación"]
    R --> P["📚 Prevención"]
```

1. **Detectar y delimitar:** identifica quién o qué está afectado, desde cuándo y qué
   cambió. Conserva timestamps, versiones, entradas y señales suficientes para no
   destruir la escena al intentar arreglarla.
2. **Investigar:** {sentence(investigation)}. Formula al menos dos hipótesis rivales
   y define qué observación refutaría cada una.
3. **Contener:** reduce blast radius y daño sin prometer una corrección todavía. La
   contención debe ser reversible, visible y compatible con las obligaciones del
   sistema.
4. **Recuperar:** {sentence(response)}. Verifica la tarea completa, no sólo que un
   proceso volvió a estar verde.
5. **Aprender:** añade una regresión, señal o control que detecte la misma clase de
   fallo. Documenta qué deuda permanece y quién revisará la acción.

El escenario evalúa método además de resultado. Una recuperación rápida que borra la
causa, oculta pérdida de datos o deja al equipo sin mecanismo preventivo no demuestra
dominio del rol.

## 📊 Señales útiles y límites de las métricas

| Señal | Qué ayuda a observar | Trampa que debe evitarse |
| --- | --- | --- |
{metric_rows}

Ninguna señal debe convertirse en ranking individual. Combina tendencia cuantitativa,
muestreo de casos, feedback cualitativo y contexto de carga. Declara ventana,
denominador, fuente, exclusiones y quién puede actuar sobre el resultado. Si una
métrica mejora mientras el outcome o el riesgo empeoran, el sistema está optimizando
el indicador y no el trabajo.

## 🧩 Proyecto integrador del rol: {project_title}

**Propósito:** {project_goal}. El resultado esperado es **{project_artifact}**.

Entrega un expediente revisable con estas piezas:

1. **Contexto y alcance:** usuario, sistema, restricción, supuestos, fuera de alcance y
   criterio de no éxito.
2. **Decisión:** al menos dos alternativas reales, trade-offs, coste de reversión y un
   ADR o memo que indique cuándo revisar la elección.
3. **Artefacto principal:** una implementación, modelo, flujo o política coherente con
   las clases núcleo; no una captura aislada ni una presentación sin mecanismo.
4. **Fallo controlado:** introduce una condición adversa relacionada con el escenario
   anterior y conserva el resultado observado, sin inventar una ejecución.
5. **Verificación:** prueba, rúbrica, revisión o medición que pueda fallar y que conecte
   directamente con el resultado profesional.
6. **Operación y salida:** telemetría, recuperación, mantenimiento, deprecación o retiro
   según corresponda; incluye límites y deuda residual.

**Criterio de aceptación:** otra persona puede reconstruir el razonamiento, reproducir
la comprobación y distinguir claramente qué quedó demostrado de lo que sólo se propone.
El proyecto no se aprueba por cantidad de archivos ni por utilizar una marca concreta.

## 📈 Dominio esperado por alcance

| Alcance | Qué resuelve | Qué evidencia su autonomía |
| --- | --- | --- |
| **Inicial** | ejecuta una tarea acotada con criterios y acompañamiento | reproduce el caso, pregunta por supuestos y entrega evidencia legible |
| **Intermedio** | decide dentro de un componente o flujo conocido | compara alternativas, prueba fallos previsibles y coordina dependencias |
| **Senior** | conduce problemas ambiguos que cruzan sistemas o equipos | hace explícito el riesgo, diseña recuperación y mejora el mecanismo de trabajo |
| **Staff / Lead** | cambia capacidades compartidas y decisiones de largo plazo | multiplica criterio, define guardrails, mide adopción y conserva opciones futuras |

Progresar no significa alejarse de la práctica. Significa aumentar ambigüedad, horizonte,
blast radius y responsabilidad por consecuencias. La persona senior todavía debe poder
explicar el mecanismo; la persona Staff además crea condiciones para que otros lo
operen sin depender de ella.

## 🗓️ Plan de práctica 30 · 60 · 90 días

- **Días 1–30 — comprender y reproducir.** Estudia las primeras clases de cada parte,
  reproduce un caso pequeño y escribe un mapa de responsabilidades. El entregable es
  una baseline con preguntas abiertas, no una transformación prematura.
- **Días 31–60 — intervenir y fallar con control.** Construye el artefacto central,
  introduce el escenario de fallo y mide el comportamiento. Revisa el trabajo con una
  persona de una ruta vecina para descubrir supuestos de frontera.
- **Días 61–90 — operar y transferir.** Ejecuta recuperación, corrige la causa, publica
  runbook o guía de uso y presenta la decisión con trade-offs. Termina con una
  retrospectiva que separe resultado, evidencia, límites y siguiente inversión.

Este plan es una secuencia de práctica, no una promesa de empleabilidad en noventa días.
La experiencia previa, el dominio y el acceso a sistemas reales cambian el tiempo
necesario.

## 🎤 Preguntas para revisión o entrevista

1. ¿En qué contexto elegirías **{first_decision}** y qué evidencia te haría cambiar?
2. ¿Cómo distinguirías síntoma, causa y daño en el escenario **{scenario_title}**?
3. ¿Qué clase asociada usarías para diseñar el mecanismo y cuál para verificarlo?
4. ¿Qué parte de **{project_title}** no automatizarías todavía y por qué?
5. ¿Qué métrica podría mejorar mientras el sistema empeora y qué guardrail añadirías?
6. ¿Dónde termina la autoridad de este rol y cuándo debe escalar o pedir revisión?

Una respuesta fuerte usa un caso, reconoce incertidumbre y propone una comprobación.
Nombrar una herramienta sin explicar mecanismo, fallo y límite no demuestra la
competencia.

## 🔗 Fuentes primarias y oficiales

{source_rows}

Las fuentes orientan principios, vocabulario y prácticas; no convierten la guía en una
certificación ni sustituyen la documentación específica del sistema, la jurisdicción
o la tecnología utilizada.'''


def render_role_detail(
    filename: str,
    classes: dict[str, dict[str, str]],
    parts: dict[str, dict[str, object]],
    *,
    from_roles: bool,
) -> list[str]:
    """Bloque de detalle de un rol: partes núcleo, clases asociadas, apoyo y proyecto."""
    prefix = "../" if from_roles else ""
    profile_data = PROFILES[filename]
    title, mission = parse_identity((ROLE_ROOT / filename).read_text(encoding="utf-8"))
    role_href = filename if from_roles else f"roles/{filename}"
    core = dict(profile_data["core"])
    part_links = " · ".join(part_link(part_id, parts, prefix) for part_id in core)
    project = tuple(profile_data["project"])
    lines = [
        f"#### [{title}]({role_href})",
        "",
        f"> {mission}",
        "",
        f"- **🧱 Partes núcleo:** {part_links}.",
        "- **🔗 Clases asociadas:**",
    ]
    for part_id, class_ids in core.items():
        class_links = " · ".join(class_link(class_id, classes, prefix) for class_id in class_ids)
        # Solo se anota el estado cuando la parte no está desarrollada.
        marker = "" if PART_STATUS[part_id] == "desarrollada" else f" ({PART_STATUS[part_id]})"
        lines.append(f"  - **Parte {part_id}{marker}:** {class_links}.")
    support = developed_support(filename, core, classes)
    support_links = " · ".join(class_link(class_id, classes, prefix) for class_id in support)
    lines.append(f"- **✅ Ya desarrolladas de apoyo ({ps.developed_label()}):** {support_links}.")
    pending = pending_for_role(filename)
    if pending:
        planned_text = " · ".join(
            f"Parte {part_id} (`{PLANNED_PARTS[part_id][1]}`–`{PLANNED_PARTS[part_id][2]}`)"
            for part_id in sorted(pending)
        )
        lines.append(f"- **🔭 Planificada, sin clases publicadas:** {planned_text}.")
    lines.extend(
        (
            f"- **🧪 Proyecto profesional:** **{project[0]}** — {project[1]}.",
            f"- **📖 Guía completa:** [decisiones, escenario, métricas y evidencia →]({role_href})",
            "",
        )
    )
    return lines


def render_compact_map(
    classes: dict[str, dict[str, str]],
    parts: dict[str, dict[str, object]],
    *,
    from_roles: bool,
) -> str:
    """Detalle completo por rol, agrupado por familia fina (índice de roles)."""
    families: dict[str, list[str]] = {}
    for filename, profile_data in PROFILES.items():
        families.setdefault(str(profile_data["family"]), []).append(filename)
    blocks: list[str] = []
    for family, filenames in families.items():
        blocks.extend((f"### {family}", ""))
        for filename in filenames:
            blocks.extend(render_role_detail(filename, classes, parts, from_roles=from_roles))
        blocks.append("")
    return "\n".join(blocks).rstrip()


def render_grouped_map(
    classes: dict[str, dict[str, str]],
    parts: dict[str, dict[str, object]],
) -> str:
    """README raíz: una tabla por familia gruesa y el detalle colapsado debajo."""
    listed = [filename for _, roles in ROLE_GROUPS for filename, _ in roles]
    if sorted(listed) != sorted(PROFILES):
        raise AssertionError("ROLE_GROUPS no coincide con los perfiles de rol")
    blocks: list[str] = []
    for group, roles in ROLE_GROUPS:
        blocks.extend(
            (f"### {group}", "", "| Rol | Partes núcleo | Proyecto profesional |", "| --- | --- | --- |")
        )
        for filename, focus in roles:
            title, _ = parse_identity((ROLE_ROOT / filename).read_text(encoding="utf-8"))
            profile_data = PROFILES[filename]
            core = dict(profile_data["core"])
            part_cells = " · ".join(
                f"[{part_id}]({parts[part_id]['path']}/README.md)" for part_id in core
            )
            project = tuple(profile_data["project"])
            blocks.append(
                f"| [{title}](roles/{filename}) — {focus} | {part_cells} | {project[0]} |"
            )
        blocks.extend(
            (
                "",
                "<details>",
                f"<summary>Detalle por rol: clases asociadas y proyecto — {group}</summary>",
                "",
            )
        )
        for filename, _ in roles:
            blocks.extend(render_role_detail(filename, classes, parts, from_roles=False))
        blocks.extend(("</details>", ""))
    return "\n".join(blocks).rstrip()


def render_extension_block() -> str:
    """Sección de ampliación de las partes planificadas; deja `{planned_rows}` para rellenarlo por rol."""

    planned = ps.planned_parts()
    if not planned:
        return (
            ps.roles_extension_heading()
            + "\n\n> [!NOTE]\n> Todas las partes del alcance ya están desarrolladas "
            "([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)); sus clases figuran en el núcleo y en las "
            "clases de apoyo de esta guía.\n"
        )
    return (
        ps.roles_extension_heading()
        + f"""

> [!NOTE]
> {ps.the_parts(planned)} ({ps.class_ranges(planned)}) {ps.verb_planned(planned)}; sus números están reservados desde el 23 de
> noviembre de 2026 ([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)). Todavía no
> tienen clases ni README, por lo que no se enlazan aquí y ninguna de sus clases debe
> considerarse disponible.

| Parte planificada | Rango previsto | Qué cambiará para este rol |
| --- | --- | --- |
{{planned_rows}}

Hasta que esas partes se publiquen, el rol se apoya en el núcleo y en las clases
desarrolladas de arriba. La planificación indica hacia dónde crecerá la ruta; no es
evidencia de que el contenido exista ni de que su alcance final coincida con esta
descripción."""
    )


def planned_notes() -> tuple[str, str]:
    planned = ps.planned_parts()
    if not planned:
        text = "No quedan partes planificadas sin publicar."
        return text, text
    detail = (
        f"{ps.the_parts(planned)} ({ps.class_ranges(planned)}) {ps.verb_planned(planned)}: "
        "no tienen clases publicadas, por eso se nombran sin enlace en cada ruta."
    )
    short = (
        f"{ps.the_parts(planned)} ({ps.class_ranges(planned)}) {ps.verb_planned(planned)} "
        "([ADR-007](../docs/adr/ADR-007-pedagogical-renumbering-and-new-parts.md)), sin clases publicadas: "
        "aparecen como «Planificada» y sin enlaces."
    )
    return detail, short


def render_main_map(classes: dict[str, dict[str, str]], parts: dict[str, dict[str, object]]) -> str:
    return f'''### 🧱 Partes núcleo y clases asociadas por rol

Cada fila enlaza la guía del rol y sus partes núcleo (por número de parte). El detalle
de cada familia —clases asociadas, clases de apoyo y proyecto profesional— se despliega
debajo de su tabla. Las partes núcleo son la base de la capacidad; las clases asociadas
activan decisiones concretas del rol; el proyecto permite integrarlas. No es una lista
de materias optativas: cada guía explica prerrequisitos, límites, trade-offs y evidencia.
El estado de revisión del contenido se declara una sola vez, en el encabezado.

{render_grouped_map(classes, parts)}

➡️ Cada nombre abre una guía extensa con gráficos, escenario de fallo, decisiones,
métricas, proyecto, progresión y fuentes. El [índice profesional](roles/README.md)
añade el mapa de transiciones entre familias.'''


def render_index_depth(classes: dict[str, dict[str, str]], parts: dict[str, dict[str, object]]) -> str:
    _, planned_note_index = planned_notes()
    return f'''<div align="center">

[![Rutas](https://img.shields.io/badge/rutas-{len(PROFILES)}-6f42c1?style=for-the-badge)](#mapa-de-{len(PROFILES)}-roles)
[![Clases](https://img.shields.io/badge/clases-asociadas%20y%20enlazadas-0969da?style=for-the-badge)](#-parte--clases--evidencia)
[![Evidencia](https://img.shields.io/badge/foco-decisiones%20y%20evidencia-2da44e?style=for-the-badge)](../assessments/rubric.md)

**Elige por responsabilidad y problemas a resolver, no por el nombre del cargo.**

</div>

## 🧩 Cómo está construida cada guía

```mermaid
flowchart LR
    F["🧱 Base común"] --> P["📚 Partes núcleo"]
    P --> C["🔗 Clases asociadas"]
    C --> D["⚖️ Decisiones"]
    D --> E["🧪 Evidencia"]
    E --> O["🔭 Operación y evolución"]
```

Cada ruta conserva el contenido existente y añade un mapa visual del trabajo, clases
enlazadas con propósito, trade-offs, incidente o fallo representativo, métricas con
sus trampas, proyecto integrador, niveles de alcance, plan 30/60/90, preguntas de
revisión y fuentes. La estructura común permite comparar; los mecanismos y decisiones
son específicos de cada profesión.

> [!NOTE]
> Los mapas distinguen el estado real de cada parte: {ps.part_ranges(ps.developed_parts())} desarrolladas. {planned_note_index}
> «Ya desarrolladas de apoyo» lista clases existentes de las {ps.developed_label()} con las que se puede practicar además del núcleo.

## 🧱 Parte → clases → evidencia

{render_compact_map(classes, parts, from_roles=True)}'''


def build(check: bool) -> None:
    classes, parts = load_curriculum()
    expected_files = {path.name for path in ROLE_ROOT.glob("*.md") if path.name != "README.md"}
    if set(PROFILES) != expected_files:
        missing = sorted(expected_files - set(PROFILES))
        extra = sorted(set(PROFILES) - expected_files)
        raise AssertionError(f"Perfiles desalineados. Faltan={missing}; sobran={extra}")

    changed: list[Path] = []
    for filename, profile_data in PROFILES.items():
        path = ROLE_ROOT / filename
        original = path.read_text(encoding="utf-8")
        title, mission = parse_identity(original)
        rendered = replace_or_insert(
            original,
            VISUAL_START,
            VISUAL_END,
            render_visual(title, profile_data),
            "\n> ",
        )
        rendered = replace_or_insert(
            rendered,
            DEPTH_START,
            DEPTH_END,
            render_role_depth(filename, title, mission, profile_data, classes, parts),
            "## 🧪 Evidencia de portafolio",
        )
        rendered = cross_references.resolve(rendered, "roles")
        if rendered != original:
            changed.append(path)
            if not check:
                path.write_text(rendered, encoding="utf-8", newline="\n")

    main_path = ROOT / "README.md"
    main_original = main_path.read_text(encoding="utf-8")
    main_rendered = replace_or_insert(
        main_original,
        MAIN_START,
        MAIN_END,
        render_main_map(classes, parts),
        "### 🪜 El ecosistema de carrera técnica",
    )
    main_rendered = cross_references.resolve(render_main_intro(main_rendered), "")
    if main_rendered != main_original:
        changed.append(main_path)
        if not check:
            main_path.write_text(main_rendered, encoding="utf-8", newline="\n")

    index_path = ROLE_ROOT / "README.md"
    index_original = index_path.read_text(encoding="utf-8")
    index_rendered = replace_or_insert(
        index_original,
        INDEX_START,
        INDEX_END,
        render_index_depth(classes, parts),
        "## Fuentes y criterios del mapa",
    )
    index_rendered = cross_references.resolve(render_index_table(index_rendered), "roles")
    if index_rendered != index_original:
        changed.append(index_path)
        if not check:
            index_path.write_text(index_rendered, encoding="utf-8", newline="\n")

    if check and changed:
        names = ", ".join(str(path.relative_to(ROOT)) for path in changed)
        raise AssertionError(f"ROLE_GUIDES_OUT_OF_DATE: {names}")
    action = "CHECK" if check else "BUILD"
    print(f"ROLE_GUIDES_{action}_OK: {len(PROFILES)} roles")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    build(args.check)


if __name__ == "__main__":
    main()
