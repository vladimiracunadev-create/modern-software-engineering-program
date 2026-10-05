#!/usr/bin/env python3
"""Enriquece y verifica las rutas profesionales sin reemplazar su contenido manual."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import quote

from role_profiles import PART_CONTEXT, PROFILES, SOURCES


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
            f"| {sequence} | {part_link(part_id, parts, '../')} | {links} | "
            f"Profundiza **{capability}** desde la responsabilidad del rol. | {sentence(evidence)}. |"
        )

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

| Orden | Parte del programa | Clases clave | Por qué entra en esta ruta | Evidencia de transferencia |
| ---: | --- | --- | --- | --- |
{chr(10).join(part_rows)}

**Cómo recorrerla.** Empieza por {class_link(class_start, classes, '../')} para fijar el
primer mecanismo, usa {class_link(class_middle, classes, '../')} para integrar el
centro de la especialidad y llega a {class_link(class_end, classes, '../')} cuando ya
puedas explicar cómo detectar y recuperar un fallo. Una clase se considera estudiada
sólo cuando su concepto cambia una decisión y deja evidencia; abrir todos los enlaces
no constituye competencia.

> [!IMPORTANT]
> El mapa expresa el currículo previsto. La Parte 00 está desarrollada; las partes
> posteriores conservan borradores o estructuras que deben superar revisión
> cualitativa. Esta ruta no declara terminadas esas clases ni reemplaza el
> [roadmap](../ROADMAP.md).

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


def render_compact_map(
    classes: dict[str, dict[str, str]],
    parts: dict[str, dict[str, object]],
    *,
    from_roles: bool,
) -> str:
    prefix = "../" if from_roles else ""
    families: dict[str, list[tuple[str, dict[str, object], str]]] = {}
    for filename, profile_data in PROFILES.items():
        text = (ROLE_ROOT / filename).read_text(encoding="utf-8")
        title, _ = parse_identity(text)
        family = str(profile_data["family"])
        families.setdefault(family, []).append((filename, profile_data, title))

    blocks: list[str] = []
    for family, entries in families.items():
        blocks.extend((f"### {family}", ""))
        for filename, profile_data, title in entries:
            role_href = filename if from_roles else f"roles/{filename}"
            core = dict(profile_data["core"])
            _, mission = parse_identity((ROLE_ROOT / filename).read_text(encoding="utf-8"))
            part_links = " · ".join(part_link(part_id, parts, prefix) for part_id in core)
            project = tuple(profile_data["project"])
            blocks.extend(
                (
                    f"#### [{title}]({role_href})",
                    "",
                    f"> {mission}",
                    "",
                    f"- **🧱 Partes núcleo:** {part_links}.",
                    "- **🔗 Clases asociadas:**",
                )
            )
            for part_id, class_ids in core.items():
                class_links = " · ".join(
                    class_link(class_id, classes, prefix) for class_id in class_ids
                )
                blocks.append(f"  - **Parte {part_id}:** {class_links}.")
            blocks.extend(
                (
                    f"- **🧪 Proyecto profesional:** **{project[0]}** — {project[1]}.",
                    f"- **📖 Guía completa:** [decisiones, escenario, métricas y evidencia →]({role_href})",
                    "",
                )
            )
        blocks.append("")
    return "\n".join(blocks).rstrip()


def render_main_map(classes: dict[str, dict[str, str]], parts: dict[str, dict[str, object]]) -> str:
    return f'''### 🧱 Partes núcleo y clases asociadas por rol

Este mapa separa la **parte** que desarrolla una capacidad, las **clases concretas**
que activan decisiones del rol y el **proyecto profesional** que permite integrarlas.
No es una lista de materias optativas: cada guía explica prerrequisitos, límites,
trade-offs y evidencia esperada.

{render_compact_map(classes, parts, from_roles=False)}

➡️ Cada nombre abre una guía extensa con gráficos, escenario de fallo, decisiones,
métricas, proyecto, progresión y fuentes. El [índice profesional](roles/README.md)
añade el mapa de transiciones entre familias.'''


def render_index_depth(classes: dict[str, dict[str, str]], parts: dict[str, dict[str, object]]) -> str:
    return f'''<div align="center">

[![Rutas](https://img.shields.io/badge/rutas-40-6f42c1?style=for-the-badge)](#mapa-de-40-roles)
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
            render_role_depth(title, mission, profile_data, classes, parts),
            "## 🧪 Evidencia de portafolio",
        )
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
        "### 💻 Construcción de productos y sistemas",
    )
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
