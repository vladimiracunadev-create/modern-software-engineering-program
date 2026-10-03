from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = ROOT / "curriculum.yaml"
TARGET_LAST_CLASS = 180
VERIFIED_ON = "2026-09-30"
EDITORIAL_LESSON_IDS = {f"SE-{number:03d}" for number in range(1, 85)}

PRODUCTS = [
    "plataforma educativa", "comercio responsable", "servicio financiero",
    "comunidad social", "control de agentes", "suite familiar privada",
]

SOURCES = {
    "SWEBOK-4A": ("SWEBOK Guide v4.0a", "IEEE Computer Society", "https://www.computer.org/education/bodies-of-knowledge/software-engineering"),
    "RISCV-ISA": ("RISC-V Ratified ISA Specifications", "RISC-V International", "https://docs.riscv.org/reference/isa/"),
    "UNICODE-17": ("The Unicode Standard 17.0", "Unicode Consortium", "https://www.unicode.org/versions/Unicode17.0.0/"),
    "PYTHON-3": ("Python 3 Documentation", "Python Software Foundation", "https://docs.python.org/3/"),
    "JVM-SE25": ("Java Virtual Machine Specification SE 25", "Oracle and JCP", "https://docs.oracle.com/javase/specs/jvms/se25/html/"),
    "LLVM-DOCS": ("LLVM Documentation", "LLVM Project", "https://llvm.org/docs/"),
    "GSF-SCI": ("Software Carbon Intensity Specification", "Green Software Foundation", "https://greensoftware.foundation/standards/sci/"),
    "ACM-ETHICS": ("ACM Code of Ethics and Professional Conduct", "ACM", "https://www.acm.org/code-of-ethics"),
    "ISO-25010": ("ISO/IEC 25010:2023", "ISO", "https://www.iso.org/standard/78176.html"),
    "UNICODE": ("The Unicode Standard", "Unicode Consortium", "https://www.unicode.org/standard/standard.html"),
    "POSIX": ("The Open Group Base Specifications", "The Open Group", "https://pubs.opengroup.org/onlinepubs/9799919799/"),
    "WINDOWS": ("Windows developer documentation", "Microsoft", "https://learn.microsoft.com/windows/"),
    "POWERSHELL": ("PowerShell documentation", "Microsoft", "https://learn.microsoft.com/powershell/"),
    "BASH": ("Bash Reference Manual", "GNU Project", "https://www.gnu.org/software/bash/manual/"),
    "SYSTEMD": ("systemd Manual Pages", "systemd project", "https://www.freedesktop.org/software/systemd/man/latest/"),
    "WSL": ("Windows Subsystem for Linux Documentation", "Microsoft", "https://learn.microsoft.com/windows/wsl/"),
    "RFC-8200": ("Internet Protocol, Version 6", "IETF", "https://www.rfc-editor.org/rfc/rfc8200"),
    "RFC-8446": ("The Transport Layer Security Protocol Version 1.3", "IETF", "https://www.rfc-editor.org/rfc/rfc8446"),
    "RFC-9000": ("QUIC: A UDP-Based Multiplexed and Secure Transport", "IETF", "https://www.rfc-editor.org/rfc/rfc9000"),
    "RFC-9110": ("HTTP Semantics", "IETF", "https://www.rfc-editor.org/rfc/rfc9110"),
    "MIT-MATH-CS": ("Mathematics for Computer Science", "MIT OpenCourseWare", "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/"),
    "GOV-RESEARCH": ("The Service Manual: user research", "UK Government Digital Service", "https://www.gov.uk/service-manual/user-research"),
    "NIST-PRIVACY": ("NIST Privacy Framework", "NIST", "https://www.nist.gov/privacy-framework"),
    "NIST-SSDF-800-218": ("Secure Software Development Framework", "NIST", "https://csrc.nist.gov/pubs/sp/800/218/final"),
    "ISO-29148": ("ISO/IEC/IEEE 29148:2018 Requirements Engineering", "ISO", "https://www.iso.org/standard/72089.html"),
    "OPENAPI": ("OpenAPI Specification", "OpenAPI Initiative", "https://spec.openapis.org/oas/latest.html"),
    "ASYNCAPI": ("AsyncAPI Specification", "AsyncAPI Initiative", "https://www.asyncapi.com/docs/reference/specification/latest"),
    "GRAPHQL": ("GraphQL Specification", "GraphQL Foundation", "https://spec.graphql.org/"),
    "WCAG-22": ("Web Content Accessibility Guidelines 2.2", "W3C", "https://www.w3.org/TR/WCAG22/"),
    "W3C-I18N": ("Internationalization techniques", "W3C", "https://www.w3.org/International/techniques/"),
    "SCRUM": ("The Scrum Guide", "Scrum Guide authors", "https://scrumguides.org/scrum-guide.html"),
    "KANBAN": ("The Kanban Guide", "Kanban Guides", "https://kanbanguides.org/english/"),
    "GIT": ("Git documentation", "Git project", "https://git-scm.com/docs"),
    "PYTHON": ("Python 3 documentation", "Python Software Foundation", "https://docs.python.org/3/"),
    "RUST": ("The Rust Programming Language", "Rust project", "https://doc.rust-lang.org/stable/book/"),
    "DEVCONTAINERS": ("Development Containers Specification", "Dev Container Specification maintainers", "https://containers.dev/implementors/spec/"),
    "SEMVER": ("Semantic Versioning 2.0.0", "Semantic Versioning project", "https://semver.org/"),
    "SPDX": ("SPDX License List", "Linux Foundation", "https://spdx.org/licenses/"),
    "GITHUB-COLLAB": ("Collaborating with pull requests", "GitHub", "https://docs.github.com/pull-requests/collaborating-with-pull-requests"),
    "C4": ("C4 model", "C4 model project", "https://c4model.com/"),
    "DIATAXIS": ("Diátaxis documentation framework", "Diátaxis project", "https://diataxis.fr/"),
    "WHATWG-HTML": ("HTML Living Standard", "WHATWG", "https://html.spec.whatwg.org/"),
    "W3C-MANIFEST": ("Web Application Manifest", "W3C", "https://www.w3.org/TR/appmanifest/"),
    "ANDROID": ("Android Developers", "Google", "https://developer.android.com/docs"),
    "APPLE": ("Apple Developer Documentation", "Apple", "https://developer.apple.com/documentation/"),
    "ELECTRON": ("Electron documentation", "OpenJS Foundation", "https://www.electronjs.org/docs/latest/"),
    "ZEPHYR": ("Zephyr Project documentation", "Linux Foundation", "https://docs.zephyrproject.org/latest/"),
    "FREERTOS": ("FreeRTOS documentation", "FreeRTOS", "https://www.freertos.org/Documentation/RTOS_book.html"),
    "JUPYTER": ("Jupyter documentation", "Project Jupyter", "https://docs.jupyter.org/en/latest/"),
    "GODOT": ("Godot Engine documentation", "Godot Engine", "https://docs.godotengine.org/en/stable/"),
    "POSTGRESQL": ("PostgreSQL documentation", "PostgreSQL Global Development Group", "https://www.postgresql.org/docs/current/"),
    "SQLITE": ("SQLite documentation", "SQLite project", "https://www.sqlite.org/docs.html"),
    "CLOUDEVENTS": ("CloudEvents specification", "Cloud Native Computing Foundation", "https://cloudevents.io/"),
    "RAFT": ("In Search of an Understandable Consensus Algorithm", "Stanford University", "https://raft.github.io/raft.pdf"),
    "GO-MEMORY": ("The Go Memory Model", "Go project", "https://go.dev/ref/mem"),
    "KUBERNETES": ("Kubernetes documentation", "Cloud Native Computing Foundation", "https://kubernetes.io/docs/"),
    "OCI": ("Open Container Initiative specifications", "Open Container Initiative", "https://opencontainers.org/release-notices/overview/"),
    "TERRAFORM": ("Terraform language documentation", "HashiCorp", "https://developer.hashicorp.com/terraform/language"),
    "AWS-WAF": ("AWS Well-Architected Framework", "Amazon Web Services", "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html"),
}

PROFILES = {
    "00": {"artifact": "informe de decisión profesional", "environment": "editor de texto, navegador y repositorio Git", "files": ["decision.md", "evidence.md", "review.md"], "lenses": ["sistema", "ciclo de vida", "evidencia", "responsabilidad"], "failure": "confundir una preferencia personal con evidencia suficiente", "sources": ["SWEBOK-4A", "ACM-ETHICS", "ISO-25010"]},
    "01": {"artifact": "cuaderno reproducible de representación y recursos", "environment": "Python 3.11+, terminal y herramientas del sistema", "files": ["experiment.py", "observations.md", "results.json"], "lenses": ["representación", "máquina", "medición", "límite"], "failure": "inferir el modelo de la máquina desde una sola observación", "sources": ["RISCV-ISA", "UNICODE-17", "PYTHON-3", "JVM-SE25", "LLVM-DOCS", "GSF-SCI"]},
    "02": {"artifact": "kit de diagnóstico multiplataforma", "environment": "PowerShell 7 y Bash en Windows, macOS o Linux", "files": ["faro.ps1", "faro.sh", "support-matrix.md"], "lenses": ["proceso", "permiso", "configuración", "recuperación"], "failure": "automatizar una operación destructiva sin precondiciones ni rollback", "sources": ["POSIX", "WINDOWS", "POWERSHELL", "BASH", "SYSTEMD", "WSL"]},
    "03": {"artifact": "traza comentada de una comunicación", "environment": "navegador, curl y utilidades de diagnóstico de red", "files": ["request.txt", "trace.md", "failure-report.md"], "lenses": ["capa", "protocolo", "estado", "observabilidad"], "failure": "atribuir al servidor un fallo que ocurre en resolución, transporte o caché", "sources": ["RFC-8200", "RFC-8446", "RFC-9000", "RFC-9110"]},
    "04": {"artifact": "especificación contrastable de una solución", "environment": "editor, Python opcional y diagramas Mermaid", "files": ["problem.md", "model.md", "checks.md"], "lenses": ["abstracción", "invariante", "algoritmo", "complejidad"], "failure": "resolver un ejemplo y asumir que la solución cubre todo el dominio", "sources": ["MIT-MATH-CS", "SWEBOK-4A"]},
    "05": {"artifact": "programa pequeño con pruebas y decisiones explicadas", "environment": "Python 3.11+, editor, terminal y Git", "files": ["main.py", "test_main.py", "README.md"], "lenses": ["valor", "control", "función", "prueba"], "failure": "confundir que un ejemplo se ejecute con que sea correcto para el dominio", "sources": ["PYTHON", "RUST", "SWEBOK-4A"]},
    "06": {"artifact": "comparación semántica entre paradigmas", "environment": "Python 3.11+ y un segundo lenguaje elegido", "files": ["case.md", "implementation-a.py", "comparison.md"], "lenses": ["estado", "composición", "efecto", "modelo"], "failure": "forzar un paradigma por moda aunque complique el problema", "sources": ["PYTHON", "SWEBOK-4A"]},
    "07": {"artifact": "implementación medida con casos límite", "environment": "Python 3.11+, unittest y temporizador monotónico", "files": ["algorithm.py", "test_algorithm.py", "benchmark.md"], "lenses": ["estructura", "invariante", "complejidad", "carga"], "failure": "elegir una estructura por costumbre sin medir la carga relevante", "sources": ["MIT-MATH-CS", "PYTHON", "SWEBOK-4A"]},
    "08": {"artifact": "entorno reproducible y sesión de diagnóstico", "environment": "editor o IDE, Python 3.11+, Git y contenedor opcional", "files": ["environment.md", "reproduction.md", "diagnosis.md"], "lenses": ["observación", "reproducción", "aislamiento", "diagnóstico"], "failure": "cambiar varias variables a la vez y perder la causa del fallo", "sources": ["PYTHON", "DEVCONTAINERS", "SWEBOK-4A"]},
    "09": {"artifact": "paquete y CLI con contrato público", "environment": "Python 3.11+, entorno virtual y Git", "files": ["pyproject.toml", "cli.py", "compatibility.md"], "lenses": ["contrato", "versión", "dependencia", "experiencia"], "failure": "romper consumidores mediante un cambio presentado como compatible", "sources": ["PYTHON", "SEMVER", "SPDX", "SWEBOK-4A"]},
    "10": {"artifact": "product brief respaldado por evidencia", "environment": "editor, hoja de cálculo opcional y repositorio de investigación", "files": ["brief.md", "assumptions.md", "research-log.md"], "lenses": ["necesidad", "hipótesis", "evidencia", "resultado"], "failure": "convertir la primera petición de una persona en requisito definitivo", "sources": ["GOV-RESEARCH", "NIST-PRIVACY", "SWEBOK-4A"]},
    "11": {"artifact": "árbol de métricas y caso de decisión", "environment": "editor y hoja de cálculo sin datos personales reales", "files": ["metric-tree.md", "decision.csv", "guardrails.md"], "lenses": ["valor", "costo", "métrica", "opción"], "failure": "optimizar actividad o una vanity metric en lugar del resultado", "sources": ["SWEBOK-4A", "NIST-PRIVACY"]},
    "12": {"artifact": "paquete de requisitos trazables", "environment": "editor, tablas Markdown y control de versiones", "files": ["requirements.md", "traceability.csv", "review.md"], "lenses": ["necesidad", "requisito", "criterio", "trazabilidad"], "failure": "aceptar lenguaje ambiguo que no puede verificarse", "sources": ["ISO-29148", "SWEBOK-4A", "ISO-25010"]},
    "13": {"artifact": "contrato versionado y ejemplos verificables", "environment": "editor YAML/JSON y validador local opcional", "files": ["contract.yaml", "examples.json", "compatibility.md"], "lenses": ["contrato", "invariante", "modelo", "compatibilidad"], "failure": "cambiar una interfaz sin analizar consumidores ni compatibilidad", "sources": ["ISO-29148", "OPENAPI", "ASYNCAPI", "GRAPHQL"]},
    "14": {"artifact": "prototipo y auditoría de inclusión", "environment": "navegador, teclado, lector de pantalla disponible y editor", "files": ["prototype.html", "accessibility.md", "usability-notes.md"], "lenses": ["tarea", "interacción", "accesibilidad", "cultura"], "failure": "declarar accesibilidad únicamente por el resultado de una herramienta automática", "sources": ["WCAG-22", "W3C-I18N", "NIST-PRIVACY"]},
    "15": {"artifact": "plan adaptativo con riesgos y métricas de flujo", "environment": "tablero reproducible en Markdown o herramienta equivalente", "files": ["plan.md", "risks.md", "flow.csv"], "lenses": ["flujo", "incertidumbre", "capacidad", "aprendizaje"], "failure": "convertir una estimación en compromiso sin rango ni supuestos", "sources": ["SCRUM", "KANBAN", "SWEBOK-4A"]},
    "16": {"artifact": "cambio colaborativo recuperable", "environment": "Git 2.40+ y alojamiento Git compatible", "files": ["change.md", "review-checklist.md", "recovery.md"], "lenses": ["historial", "integración", "revisión", "gobernanza"], "failure": "reescribir o publicar historia compartida sin evaluar a quién afecta", "sources": ["GIT", "GITHUB-COLLAB", "ACM-ETHICS"]},
    "17": {"artifact": "paquete de documentación mantenible", "environment": "editor Markdown, Mermaid y verificador de enlaces", "files": ["README.md", "architecture.md", "decision-record.md"], "lenses": ["audiencia", "decisión", "vista", "mantenimiento"], "failure": "documentar una intención como si describiera el comportamiento actual", "sources": ["DIATAXIS", "C4", "SWEBOK-4A"]},
    "18": {"artifact": "interfaz textual operable y automatización supervisada", "environment": "Python 3.11+, terminal, pseudo-TTY y gestor de procesos", "files": ["app.py", "service.md", "operations.md"], "lenses": ["interfaz", "proceso", "señal", "automatización"], "failure": "dejar un proceso sin límites, observación ni estrategia de terminación", "sources": ["PYTHON", "POSIX", "SWEBOK-4A"]},
    "19": {"artifact": "experiencia web progresiva accesible", "environment": "navegador moderno, DevTools, servidor local y auditor de accesibilidad", "files": ["index.html", "app.js", "manifest.webmanifest"], "lenses": ["documento", "estado", "navegación", "progresividad"], "failure": "depender de JavaScript o red sin diseñar estados alternativos", "sources": ["WHATWG-HTML", "W3C-MANIFEST", "WCAG-22", "RFC-9110"]},
    "20": {"artifact": "servicio con contrato y procesamiento recuperable", "environment": "Python 3.11+, servidor HTTP local, curl y cola simulada", "files": ["openapi.yaml", "service.py", "recovery.md"], "lenses": ["contrato", "solicitud", "trabajo", "idempotencia"], "failure": "reintentar una operación no idempotente y duplicar efectos", "sources": ["OPENAPI", "ASYNCAPI", "RFC-9110", "SWEBOK-4A"]},
    "21": {"artifact": "comparación de ciclo de vida entre plataformas cliente", "environment": "Android Studio, Xcode o Electron según plataforma elegida", "files": ["lifecycle.md", "prototype.md", "distribution.md"], "lenses": ["plataforma", "ciclo de vida", "estado", "distribución"], "failure": "suponer que cerrar, suspender y terminar una aplicación son el mismo evento", "sources": ["ANDROID", "APPLE", "ELECTRON", "ISO-25010"]},
    "22": {"artifact": "prototipo embebido con presupuesto y análisis temporal", "environment": "simulador o placa autorizada, toolchain declarada y analizador de trazas", "files": ["firmware.md", "timing.csv", "safety.md"], "lenses": ["recurso", "tiempo", "interrupción", "seguridad"], "failure": "bloquear una tarea crítica o incumplir un deadline sin señal observable", "sources": ["ZEPHYR", "FREERTOS", "NIST-SSDF-800-218", "SWEBOK-4A"]},
    "23": {"artifact": "prototipo especializado con restricciones de dominio", "environment": "Jupyter o Godot según el caso, datos sintéticos y control de versiones", "files": ["domain.md", "prototype.md", "validation.md"], "lenses": ["dominio", "modelo", "restricción", "validación"], "failure": "trasladar una métrica técnica a una conclusión de dominio sin validación", "sources": ["JUPYTER", "GODOT", "ISO-25010", "SWEBOK-4A"]},
    "24": {"artifact": "refactorización protegida por caracterización y decisión de diseño", "environment": "Python 3.11+, pruebas, analizador estático y Git", "files": ["characterization.py", "design.md", "refactoring.md"], "lenses": ["responsabilidad", "acoplamiento", "cambio", "deuda"], "failure": "refactorizar y cambiar comportamiento al mismo tiempo sin caracterización", "sources": ["SWEBOK-4A", "ISO-25010", "PYTHON"]},
    "25": {"artifact": "dossier de arquitectura con decisiones y escenarios", "environment": "editor Markdown, Mermaid y repositorio de ADR", "files": ["context.md", "architecture.md", "adr.md"], "lenses": ["límite", "atributo", "escenario", "decisión"], "failure": "elegir un estilo arquitectónico antes de identificar fuerzas y atributos", "sources": ["C4", "ISO-25010", "SWEBOK-4A"]},
    "26": {"artifact": "modelo persistente con garantías y recuperación probadas", "environment": "PostgreSQL o SQLite, cliente SQL y datos sintéticos", "files": ["schema.sql", "queries.sql", "recovery.md"], "lenses": ["modelo", "transacción", "índice", "recuperación"], "failure": "confundir persistencia exitosa con durabilidad o recuperabilidad verificadas", "sources": ["POSTGRESQL", "SQLITE", "SWEBOK-4A"]},
    "27": {"artifact": "flujo de integración con contrato, reintento y reconciliación", "environment": "broker local o simulador, validador de esquemas y trazas", "files": ["asyncapi.yaml", "flow.md", "reconciliation.md"], "lenses": ["mensaje", "evento", "entrega", "consistencia"], "failure": "procesar dos veces un mensaje y producir efectos no reconciliables", "sources": ["ASYNCAPI", "CLOUDEVENTS", "OPENAPI", "SWEBOK-4A"]},
    "28": {"artifact": "experimento distribuido con fallos y garantías declaradas", "environment": "procesos locales o contenedores, reloj monotónico y trazas correlacionadas", "files": ["model.md", "experiment.py", "failure-trace.md"], "lenses": ["concurrencia", "orden", "partición", "consenso"], "failure": "inferir orden global o exactamente-una-vez desde observaciones locales", "sources": ["RAFT", "GO-MEMORY", "ISO-25010", "SWEBOK-4A"]},
    "29": {"artifact": "plataforma reproducible con infraestructura declarativa", "environment": "contenedores OCI, Kubernetes local y Terraform en modo plan", "files": ["Containerfile", "platform.md", "main.tf"], "lenses": ["recurso", "imagen", "declaración", "plataforma"], "failure": "aplicar infraestructura sin revisar plan, estado, permisos ni costo", "sources": ["KUBERNETES", "OCI", "TERRAFORM", "AWS-WAF", "NIST-SSDF-800-218"]},
}

TEACHING = {
    "00": {"foundation": "La ingeniería de software coordina producto, proceso y tecnología durante todo el ciclo de vida; su unidad de trabajo es una decisión justificable y sus consecuencias, no únicamente código.", "question": "¿qué responsabilidad, frontera profesional o atributo de calidad cambia?", "evidence": "una decisión revisable, sus fuentes y el impacto sobre personas y sistema"},
    "01": {"foundation": "Un computador representa información mediante estados discretos y ejecuta instrucciones sobre jerarquías con límites de precisión, capacidad, latencia y energía.", "question": "¿cómo se representa, transforma y observa la información en cada nivel?", "evidence": "bytes, mediciones repetibles y diferencias explicadas entre modelo y máquina"},
    "02": {"foundation": "El sistema operativo arbitra procesos, memoria, archivos, dispositivos e identidades; la automatización segura hace explícitos precondiciones, permisos, efectos y recuperación.", "question": "¿qué recurso administra el sistema y bajo qué identidad ocurre el cambio?", "evidence": "estado anterior y posterior, logs, códigos de salida y procedimiento de rollback"},
    "03": {"foundation": "Una comunicación atraviesa resolución de nombres, rutas, transporte, seguridad y semántica de aplicación; cada capa tiene señales y fallos diferentes.", "question": "¿en qué capa se define el comportamiento y en cuál aparece el síntoma?", "evidence": "mensajes, tiempos, estados, cabeceras o capturas obtenidos sin interceptar tráfico ajeno"},
    "04": {"foundation": "Resolver un problema exige modelar entradas, salidas, estado, invariantes y costo; un ejemplo favorable no demuestra corrección para todo el dominio.", "question": "¿qué debe mantenerse verdadero y bajo qué conjunto de entradas?", "evidence": "casos límite, contraejemplos, argumento de terminación y costo medido o acotado"},
    "05": {"foundation": "Programar transforma entradas y estado mediante reglas explícitas; la legibilidad, los tipos y las pruebas hacen observable si el comportamiento coincide con los ejemplos del dominio.", "question": "¿qué comportamiento debe producirse para entradas normales, límites y errores?", "evidence": "ejemplos ejecutables, pruebas y salidas reproducibles"},
    "06": {"foundation": "Un paradigma organiza estado, control y composición; ninguno es universal y una solución puede combinar modelos si conserva semántica comprensible.", "question": "¿qué modelo vuelve más explícitas las reglas, efectos y cambios de estado?", "evidence": "implementaciones equivalentes, pruebas comunes y comparación de compromisos"},
    "07": {"foundation": "Una estructura de datos define operaciones y costos; un algoritmo debe preservar invariantes, terminar y comportarse dentro de límites de tiempo y espacio adecuados a la carga.", "question": "¿qué operaciones dominan la carga y qué garantía necesita cada una?", "evidence": "casos límite, pruebas de propiedades, complejidad y medición empírica"},
    "08": {"foundation": "Una herramienta de desarrollo es útil cuando hace observable y reproducible el sistema; depurar exige reducir el caso y cambiar una variable por vez.", "question": "¿qué estado debe observarse para refutar la hipótesis actual?", "evidence": "reproducción mínima, versiones, trazas y secuencia de diagnóstico"},
    "09": {"foundation": "Una biblioteca, paquete, SDK o CLI publica un contrato que otros integran; versionado, dependencias, licencias y errores forman parte de esa experiencia.", "question": "¿qué promete la interfaz y cómo sabrá un consumidor que el cambio es compatible?", "evidence": "contrato documentado, pruebas desde el consumidor, lockfile o resolución explicada y códigos de salida"},
    "10": {"foundation": "El descubrimiento reduce incertidumbre sobre personas, problemas y resultados antes de comprometer una solución; una entrevista produce evidencia situada, no verdad universal.", "question": "¿qué incertidumbre crítica se intenta reducir y qué decisión habilitaría?", "evidence": "observaciones trazables, patrones y contradicciones, siempre separadas de interpretación"},
    "11": {"foundation": "Una métrica representa parcialmente un resultado y puede cambiar conductas; por eso se interpreta junto con costo, población, ventana temporal y guardrails.", "question": "¿qué decisión cambiaría con esta medida y qué daño podría ocultar?", "evidence": "definición calculable, fuente de datos, segmento, tendencia y métrica contraria"},
    "12": {"foundation": "Un requisito conecta una necesidad con comportamiento o restricción verificable; la trazabilidad permite explicar origen, cambio, implementación y evidencia de aceptación.", "question": "¿quién necesita qué resultado, bajo qué condición y cómo se verificará?", "evidence": "criterios inequívocos, ejemplos y enlaces bidireccionales entre necesidad y prueba"},
    "13": {"foundation": "Una especificación reduce interpretaciones permitidas mediante vocabulario, modelos, invariantes y ejemplos; un contrato además define obligaciones observables entre partes.", "question": "¿qué comportamiento se promete, qué queda fuera y cómo evoluciona sin romper consumidores?", "evidence": "esquema válido, ejemplos positivos y negativos, compatibilidad y prueba contractual"},
    "14": {"foundation": "La experiencia surge de la interacción entre persona, tarea, contenido y contexto; accesibilidad e internacionalización son restricciones de diseño verificables, no acabados visuales.", "question": "¿quién puede completar la tarea, con qué modalidad y en qué estado de error o recuperación?", "evidence": "recorrido por teclado, semántica, contraste, formatos culturales y observación de uso"},
    "15": {"foundation": "Un proceso de trabajo limita trabajo en curso, hace visible el flujo y crea ciclos de aprendizaje; un plan es una hipótesis actualizable, no una predicción exacta.", "question": "¿qué incertidumbre, dependencia o cuello de botella condiciona la siguiente entrega?", "evidence": "políticas explícitas, tiempos de flujo, riesgos y revisión de resultados frente a supuestos"},
    "16": {"foundation": "Git conserva un grafo de objetos y referencias; la colaboración añade revisión, integración, ownership y normas para cambiar historia compartida con seguridad.", "question": "¿qué cambio atómico se propone, quién puede verse afectado y cómo se recupera?", "evidence": "diff enfocado, historial legible, revisión resuelta y estrategia de reversión"},
    "17": {"foundation": "La documentación sirve a una audiencia y una tarea concreta; debe diferenciar tutorial, guía, explicación, referencia, arquitectura y registro histórico.", "question": "¿quién necesita tomar qué decisión con esta vista y cuándo dejaría de ser válida?", "evidence": "prueba de recorrido, enlaces comprobados, owner, fecha y contraste con el comportamiento actual"},
    "18": {"foundation": "CLI, TUI, servicios y automatizaciones son interfaces operativas: reciben intención, administran procesos y deben exponer resultado, error, cancelación y recuperación.", "question": "¿qué contrato observa una persona o proceso consumidor y cómo termina de forma segura?", "evidence": "entradas, salida estándar y de error, códigos, señales, logs y prueba de cancelación"},
    "19": {"foundation": "La web combina documentos, navegación, estado y capacidades progresivas; una experiencia robusta conserva tarea y significado ante red lenta, fallo de script o tecnología asistiva.", "question": "¿qué puede completar la persona en cada estado de carga, error, desconexión y recuperación?", "evidence": "HTML semántico, recorrido por teclado, estados visibles, prueba sin JavaScript y auditoría manual"},
    "20": {"foundation": "Un backend coordina contratos, estado y trabajo síncrono o diferido; los límites de tiempo y los reintentos forman parte del comportamiento público.", "question": "¿qué efecto se promete, cuándo se confirma y cómo se evita duplicarlo o perderlo?", "evidence": "contrato validado, pruebas de idempotencia, trazas correlacionadas y recuperación tras timeout"},
    "21": {"foundation": "Cada plataforma cliente controla instalación, permisos, ciclo de vida, recursos y distribución; compartir código no elimina esas diferencias.", "question": "¿qué estado debe sobrevivir a pausa, cierre, actualización o pérdida de conectividad?", "evidence": "matriz de ciclo de vida, prototipo, pruebas de restauración y requisitos de distribución"},
    "22": {"foundation": "El software embebido interactúa con tiempo y mundo físico bajo presupuestos estrictos; corrección funcional y cumplimiento temporal son propiedades distintas.", "question": "¿qué deadline, recurso o estado físico convierte un retraso en fallo?", "evidence": "presupuesto medido, traza temporal, límites eléctricos simulados o declarados y estado seguro"},
    "23": {"foundation": "El software especializado hereda reglas, riesgos y evidencia del dominio; una técnica correcta puede ser inválida si el modelo no representa ese contexto.", "question": "¿qué afirmación de dominio se hace y qué validación permite sostenerla?", "evidence": "supuestos explícitos, datos sintéticos, métrica apropiada y revisión por criterio de dominio"},
    "24": {"foundation": "Diseñar distribuye responsabilidades y dependencias para facilitar cambios; refactorizar mejora esa estructura sin alterar comportamiento observable.", "question": "¿qué cambio futuro se vuelve más seguro y qué evidencia demuestra que el comportamiento se conserva?", "evidence": "pruebas de caracterización, diff enfocado, métricas interpretadas y decisión reversible"},
    "25": {"foundation": "La arquitectura expresa decisiones significativas y difíciles de cambiar frente a atributos y restricciones; un diagrama solo es una vista del razonamiento.", "question": "¿qué escenario de calidad fuerza la decisión y qué alternativa se descartó?", "evidence": "escenarios medibles, vistas coherentes, ADR y análisis de consecuencias"},
    "26": {"foundation": "Persistir datos exige modelar identidad, relaciones, concurrencia y recuperación; una consulta rápida no compensa garantías incorrectas.", "question": "¿qué invariantes deben sobrevivir a concurrencia, fallo y restauración?", "evidence": "esquema, consultas explicadas, plan de ejecución, prueba transaccional y restauración"},
    "27": {"foundation": "Integrar sistemas introduce fronteras de propiedad, tiempo y fallo; mensajes y eventos necesitan contrato, semántica de entrega y reconciliación.", "question": "¿quién posee el hecho, cuántas veces puede llegar y cómo se corrige una divergencia?", "evidence": "esquema versionado, identificadores, trazas, prueba de duplicado y procedimiento de reconciliación"},
    "28": {"foundation": "Concurrencia y distribución eliminan supuestos de orden, tiempo y conocimiento compartido; las garantías deben declararse bajo fallos concretos.", "question": "¿qué puede conocer cada participante y qué propiedad se mantiene durante una partición?", "evidence": "modelo de estados, ejecución controlada, historia de eventos y contraejemplo de una garantía más fuerte"},
    "29": {"foundation": "Cloud y platform engineering convierten recursos y políticas en productos internos declarativos; elasticidad, seguridad, costo y operación son parte del diseño.", "question": "¿qué capacidad autoservicio se ofrece y qué guardrail limita su impacto?", "evidence": "plan declarativo, política, estimación de costo, prueba de despliegue local y destrucción controlada"},
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


def display_term(term: str) -> str:
    """Start ordinary terms with a capital while preserving acronyms and product casing."""
    if term.isupper() or any(character.isupper() for character in term[1:]):
        return term
    return term[:1].upper() + term[1:]


def source_catalog(program: dict) -> dict:
    used = sorted({source for part in program["parts"] if part["lessons"][-1]["number"] <= TARGET_LAST_CLASS for source in PROFILES[part["id"]]["sources"]})
    return {
        "$schema": "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/schemas/activity.schema.json",
        "schema_version": 1,
        "verified_on": VERIFIED_ON,
        "scope": "Fase 3 en reconstrucción: SE-001 a SE-180",
        "policy": "Fuentes primarias u oficiales; la guía indica el uso pedagógico y evita atribuirles afirmaciones no contenidas.",
        "sources": [
            {"id": source_id, "title": SOURCES[source_id][0], "authority": SOURCES[source_id][1], "url": SOURCES[source_id][2], "status": "verified"}
            for source_id in used
        ],
        "parts": {part_id: PROFILES[part_id]["sources"] for part_id in sorted(PROFILES) if int(part_id) <= 14},
    }


def context(program: dict) -> dict[str, tuple[dict, dict, dict | None, dict | None]]:
    flat = [(part, lesson) for part in program["parts"] for lesson in part["lessons"]]
    result = {}
    for index, (part, lesson) in enumerate(flat):
        previous = flat[index - 1][1] if index else None
        following = flat[index + 1][1] if index + 1 < len(flat) else None
        result[lesson["id"]] = (part, lesson, previous, following)
    return result


def repository_class_url(lesson: dict) -> str:
    return (
        "https://github.com/vladimiracunadev-create/software-engineering-learning-suite/"
        f"blob/main/{lesson['path']}/README.md"
    )


def lesson_navigation(part: dict, lesson: dict, previous: dict | None, following: dict | None) -> str:
    previous_link = (
        f"[← {previous['id']} — {previous['title']}]({repository_class_url(previous)})"
        if previous else "← Inicio del programa"
    )
    following_link = (
        f"[{following['id']} — {following['title']} →]({repository_class_url(following)})"
        if following else "Fin del programa →"
    )
    portal = (
        "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/"
        f"classes/{lesson['id']}.html"
    )
    part_url = (
        "https://github.com/vladimiracunadev-create/software-engineering-learning-suite/"
        f"blob/main/{part['path']}/README.md"
    )
    index_url = (
        "https://github.com/vladimiracunadev-create/software-engineering-learning-suite/"
        "blob/main/classes/README.md"
    )
    return (
        f"{previous_link} · [↑ Parte {part['id']}]({part_url}) · "
        f"[📚 Índice completo]({index_url}) · "
        f"[🌐 Portal]({portal}) · {following_link}"
    )


def lesson_readme(part: dict, lesson: dict, previous: dict | None, following: dict | None) -> str:
    profile = PROFILES[part["id"]]
    teaching = TEACHING[part["id"]]
    terms = words(lesson["title"], profile)
    product = PRODUCTS[(lesson["number"] - 1) % len(PRODUCTS)]
    source_lines = "\n".join(
        f"- **{SOURCES[source_id][0]}** — {SOURCES[source_id][1]}. [{SOURCES[source_id][2]}]({SOURCES[source_id][2]}) — se usa para contrastar vocabulario, límites y criterios aplicables."
        for source_id in profile["sources"]
    )
    files = "\n".join(f"│   ├── {name}" for name in profile["files"])
    roles = [
        ("modelo", "delimita qué entidad, estado o relación se estudia y qué queda fuera"),
        ("mecanismo", "explica la cadena causal: qué entrada cambia qué estado y mediante qué regla"),
        ("evidencia", "define la señal observable que permite contrastar el modelo sin confundir correlación con causa"),
        ("decisión", "convierte el conocimiento en opciones comparables, límites, riesgos y condiciones de reversión"),
    ]
    concept_sections = "\n\n".join(
        f"### {index}. {display_term(term)}: {role}\n\nEn esta clase, **{term}** se estudia como {role}. Su función es {explanation}. Debe conectarse con la pregunta «{teaching['question']}» y demostrarse mediante {teaching['evidence']}. Un tratamiento superficial solo lo nombraría; un tratamiento útil identifica precondiciones, transición, resultado observable y caso en que la explicación deja de sostenerse. Aplica esa secuencia a **{lesson['title']}**, registra los supuestos y explica qué decisión concreta cambia al comprenderla."
        for index, (term, (role, explanation)) in enumerate(zip(terms[:4], roles), start=1)
    )
    topic_rows = "\n".join(
        f"| {display_term(term)} | {display_term(role)} | {display_term(explanation)}. |"
        for term, (role, explanation) in zip(terms[:4], roles)
    )
    definitions = "\n".join(
        f"- **{display_term(term)}:** concepto usado aquí como {role}; se acepta solo si puede observarse o justificarse mediante {teaching['evidence']}."
        for term, (role, _) in zip(terms[:4], roles)
    )
    navigation = lesson_navigation(part, lesson, previous, following)
    previous_label = previous["id"] if previous else "diagnóstico inicial del programa"
    following_label = following["id"] if following else "cierre del programa"
    return f"""# {lesson['id']} — {lesson['title']}

{navigation}

> [!WARNING]
> Estado: **PLANNED · BORRADOR EN REVISIÓN**. El material es visible para auditoría,
> pero aún no supera el estándar pedagógico profundo y no debe presentarse como clase terminada.

## Prerrequisitos

- Haber completado o diagnosticado `{previous_label}` y poder explicar qué evidencia produjo.
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

## Temas y por qué importan

| Tema | Función en la clase | Por qué importa |
| --- | --- | --- |
{topic_rows}

## Mapa conceptual

```mermaid
flowchart LR
    P["Problema: {html.escape(lesson['title'])}"] --> M["Modelo: {terms[0]}"]
    M --> D["Decisión: {terms[1]}"]
    D --> E["Evidencia: {terms[2]}"]
    E --> R["Revisión: {terms[3]}"]
    R -->|nueva información| M
```

El diagrama se lee de izquierda a derecha: el problema obliga a construir un
modelo; el modelo permite decidir; la decisión solo se sostiene con evidencia; y
la revisión devuelve nueva información al modelo. No es una secuencia lineal de
entrega, sino un ciclo de aprendizaje aplicado a **{lesson['title']}**.

## Conceptos y decisiones

{teaching['foundation']}

La pregunta rectora de esta parte es: **{teaching['question']}** La respuesta debe
apoyarse en **{teaching['evidence']}**.

{concept_sections}

La regla de trabajo es conservar trazabilidad: problema → supuesto → opción → decisión → evidencia → revisión. Una solución técnicamente posible puede seguir siendo inadecuada si excluye personas, desplaza riesgos o no puede mantenerse. La herramienta concreta se elige después de fijar el comportamiento y el criterio de aceptación.

## Definiciones de trabajo

{definitions}

Estas definiciones son operativas para el borrador: deberán sustituirse o
precisarse con terminología de las fuentes de la clase durante la revisión
cualitativa. No son un glosario normativo.

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

## Reto verificable

Entrega el **{profile['artifact']}** de forma que una persona que no participó en
la clase pueda reconstruir problema, supuestos, opciones, decisión y evidencia.
El reto se acepta únicamente si esa persona puede señalar una condición concreta
que cambiaría la decisión y reproducir al menos una comprobación sin pedir contexto
oral adicional.

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

## Preguntas frecuentes

### ¿Basta con definir los términos del título?

No. Debes mostrar cómo se relacionan, qué mecanismo explican, qué evidencia los
contrasta y qué decisión profesional cambia gracias a esa comprensión.

### ¿La herramienta recomendada es obligatoria?

No. El entorno de referencia hace reproducible la práctica, pero puedes usar otro
si documentas equivalencias, versiones, diferencias y procedimiento de recuperación.

### ¿Completar los archivos aprueba automáticamente la clase?

No. Los archivos son contenedores de evidencia. La aprobación depende de la calidad
del razonamiento, la reproducibilidad, el diagnóstico y la revisión contra las fuentes.

## Límites y siguiente paso

Esta guía enseña a razonar y producir evidencia sobre **{lesson['title']}**; no certifica dominio profesional ni valida una implementación productiva. El siguiente enlace curricular es `{following_label}`. Si la actividad necesita código o infraestructura real, debe avanzar a `EXECUTABLE`, añadir pruebas y documentar versiones, limpieza y recuperación.

---

{navigation}
"""


def activity(part: dict, lesson: dict) -> dict:
    profile = PROFILES[part["id"]]
    return {
        "$schema": "https://vladimiracunadev-create.github.io/software-engineering-learning-suite/schemas/rubric.schema.json",
        "schema_version": 1,
        "class_id": lesson["id"],
        "status": lesson["status"],
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


def inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(
        r"\[([^]]+)\]\((https?://[^)]+|\.{1,2}/[^)]+)\)",
        r'<a href="\2">\1</a>',
        escaped,
    )
    return escaped


def heading_id(value: str) -> str:
    plain = re.sub(r"[`*_]", "", value).casefold()
    plain = re.sub(r"[^a-z0-9áéíóúüñ]+", "-", plain).strip("-")
    return plain or "seccion"


def mermaid_to_visual(source: str) -> str:
    """Render the small flowchart subset used by lessons without a JS dependency.

    The relation view intentionally favors readable claims over decorative graph
    layout. The original Mermaid notation remains available as an accessible
    disclosure for readers who want to inspect or reuse it.
    """
    node_labels = {
        match.group(1): match.group(2).strip('"')
        for match in re.finditer(r'([A-Za-z][A-Za-z0-9_]*)\[([^]]+)\]', source)
    }
    relations: list[tuple[str, str, str]] = []
    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("flowchart"):
            continue
        parts = re.split(r"\s*(-->|---)\s*", line)
        for index in range(0, len(parts) - 2, 2):
            left_match = re.match(r"([A-Za-z][A-Za-z0-9_]*)", parts[index])
            right_match = re.match(r"([A-Za-z][A-Za-z0-9_]*)", parts[index + 2])
            if not left_match or not right_match:
                continue
            left_id, right_id = left_match.group(1), right_match.group(1)
            connector = "→" if parts[index + 1] == "-->" else "—"
            relation = (
                node_labels.get(left_id, left_id),
                connector,
                node_labels.get(right_id, right_id),
            )
            if relation not in relations:
                relations.append(relation)
    if not relations:
        return f'<pre class="mermaid-source"><code>{html.escape(source)}</code></pre>'
    rows = "".join(
        '<div class="concept-relation">'
        f'<span class="concept-node">{html.escape(left)}</span>'
        f'<span class="concept-arrow" aria-hidden="true">{connector}</span>'
        f'<span class="concept-node">{html.escape(right)}</span>'
        "</div>"
        for left, connector, right in relations
    )
    return (
        '<figure class="concept-map">'
        '<figcaption><span>Mapa visual</span><strong>Relaciones que debes poder explicar</strong></figcaption>'
        f'<div class="concept-relations">{rows}</div>'
        '<details><summary>Ver la notación fuente del diagrama</summary>'
        f'<pre class="mermaid-source"><code>{html.escape(source)}</code></pre></details>'
        "</figure>"
    )


def markdown_to_html(markdown: str) -> tuple[str, list[tuple[str, str]]]:
    lines = markdown.splitlines()
    output: list[str] = []
    headings: list[tuple[str, str]] = []
    index = 0
    in_code = False
    code_language = ""
    code_lines: list[str] = []
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_language = line[3:].strip()
                code_lines = []
            else:
                source = chr(10).join(code_lines)
                if code_language == "mermaid":
                    output.append(mermaid_to_visual(source))
                else:
                    output.append(f'<pre class="code-block"><code>{html.escape(source)}</code></pre>')
                in_code = False
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue
        if index == 0 and line.startswith("# "):
            index += 1
            continue
        heading = re.match(r"^(#{2,4})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            label = heading.group(2)
            anchor = heading_id(label)
            if level == 2:
                headings.append((anchor, re.sub(r"[`*_]", "", label)))
            output.append(f'<h{level} id="{anchor}">{inline_markdown(label)}</h{level}>')
            index += 1
            continue
        if line.startswith(">"):
            quoted = []
            while index < len(lines) and lines[index].startswith(">"):
                quoted.append(lines[index].lstrip("> "))
                index += 1
            callout_kind = ""
            if quoted and re.fullmatch(r"\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]", quoted[0], re.IGNORECASE):
                callout_kind = quoted.pop(0)[2:-1].casefold()
            callout_class = f"callout {callout_kind}".strip()
            output.append(f'<aside class="{callout_class}">{inline_markdown(" ".join(quoted))}</aside>')
            continue
        if "|" in line and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[index + 1]):
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            index += 2
            rows = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            head = "".join(f"<th>{inline_markdown(cell)}</th>" for cell in headers)
            body = "".join("<tr>" + "".join(f"<td>{inline_markdown(cell)}</td>" for cell in row) + "</tr>" for row in rows)
            output.append(f'<div class="table-wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>')
            continue
        unordered = re.match(r"^-\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            tag = "ul" if unordered else "ol"
            items = []
            pattern = r"^-\s+(.+)$" if unordered else r"^\d+\.\s+(.+)$"
            while index < len(lines):
                match = re.match(pattern, lines[index])
                if not match:
                    break
                items.append(f"<li>{inline_markdown(match.group(1))}</li>")
                index += 1
            output.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        if line.strip() == "---":
            output.append("<hr>")
            index += 1
            continue
        if not line.strip():
            index += 1
            continue
        paragraph = [line.strip()]
        index += 1
        while index < len(lines) and lines[index].strip() and not re.match(r"^(#{2,4})\s+|^>|^```|^-\s+|^\d+\.\s+", lines[index]):
            if "|" in lines[index] and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[index + 1]):
                break
            paragraph.append(lines[index].strip())
            index += 1
        output.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
    return "".join(output), headings


def site_page(
    part: dict,
    lesson: dict,
    markdown: str,
    previous: dict | None,
    following: dict | None,
) -> str:
    content, headings = markdown_to_html(markdown)
    phase = 3 if lesson["number"] <= 180 else 4
    toc = "".join(f'<li><a href="#{anchor}">{html.escape(label)}</a></li>' for anchor, label in headings)
    repository_url = f"https://github.com/vladimiracunadev-create/software-engineering-learning-suite/tree/main/{lesson['path']}"
    previous_link = f'<a href="{previous["id"]}.html">← {previous["id"]}</a>' if previous else '<span>Inicio</span>'
    following_link = f'<a href="{following["id"]}.html">{following["id"]} →</a>' if following else '<span>Fin</span>'
    navigation = f'<nav class="class-nav" aria-label="Navegación entre clases">{previous_link}<a href="../parts/{part["id"]}.html">Parte {part["id"]}</a><a href="../index.html">Índice</a>{following_link}</nav>'
    guided = lesson["status"] == "GUIDED"
    description = ("Clase guiada" if guided else "Borrador estructural") + f" {lesson['id']}: {lesson['title']}"
    notice = (
        "<strong>GUIDED:</strong> clase desarrollada y aprobada contra el estándar pedagógico."
        if guided else
        "<strong>PLANNED · EN REVISIÓN:</strong> texto íntegro del borrador estructural publicado para auditoría. No es una clase aprobada."
    )
    lesson_index = next(
        index for index, item in enumerate(part["lessons"]) if item["id"] == lesson["id"]
    )
    progress_items = []
    for index, item in enumerate(part["lessons"]):
        state_class = "is-current" if index == lesson_index else "is-complete" if index < lesson_index else ""
        label = f'{item["id"]}: {item["title"]}'
        if index == lesson_index:
            progress_items.append(f'<li><span class="{state_class}" aria-current="step">{html.escape(label)}</span></li>')
        else:
            progress_items.append(f'<li><a class="{state_class}" href="{item["id"]}.html" aria-label="{html.escape(label)}">{html.escape(label)}</a></li>')
    previous_title = previous["title"] if previous else "Inicio del programa"
    following_title = following["title"] if following else "Cierre del programa"
    context = (
        '<div class="lesson-context" aria-label="Conexión curricular">'
        f'<div class="context-card"><span>Vienes de</span><strong>{html.escape(previous_title)}</strong></div>'
        f'<div class="context-card"><span>Construyes ahora</span><strong>{html.escape(lesson["title"])}</strong></div>'
        f'<div class="context-card"><span>Conecta con</span><strong>{html.escape(following_title)}</strong></div>'
        '</div>'
    )
    progress = (
        '<nav class="lesson-progress" aria-label="Progreso dentro de la parte">'
        f'<div class="lesson-progress__label"><span>Parte {part["id"]}</span><span>Clase {lesson_index + 1} de {len(part["lessons"])}</span></div>'
        f'<ol>{"".join(progress_items)}</ol></nav>'
    )
    kind_label = {"class": "Clase", "studio": "Taller", "project": "Proyecto"}.get(
        lesson["kind"], lesson["kind"].capitalize()
    )
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="{html.escape(description)}"><title>{lesson['id']} · {html.escape(lesson['title'])}</title><link rel="stylesheet" href="../assets/styles.css"></head><body><a class="skip" href="#content">Saltar al contenido</a><main class="lesson" id="content">{navigation}<header class="lesson-hero" data-number="{lesson_index + 1:02}"><p class="eyebrow">Fase {phase} · {lesson['id']} · {html.escape(kind_label)}</p><h1>{html.escape(lesson['title'])}</h1><p>Una clase de la Parte {part['id']} — {html.escape(part['title'])}. Comprende el mecanismo, úsalo para decidir y conserva evidencia revisable.</p></header>{progress}<div class="notice">{notice}</div>{context}<div class="lesson-shell"><nav class="lesson-toc" aria-label="Contenido de la clase"><strong>En esta clase</strong><ol>{toc}</ol></nav><article class="lesson-content">{content}</article></div><p class="source-link"><a href="{repository_url}">Ver archivos fuente, actividad y rúbrica en GitHub</a></p>{navigation}</main><footer>Software Engineering Learning Suite · Fase {phase} en reconstrucción</footer></body></html>\n"""


def expected_files(program: dict) -> dict[Path, str]:
    result = {ROOT / "sources/phase3.json": dump_json(source_catalog(program))}
    entries = context(program)
    for part in program["parts"]:
        if part["lessons"][-1]["number"] > TARGET_LAST_CLASS:
            continue
        for lesson in part["lessons"]:
            _, _, previous, following = entries[lesson["id"]]
            directory = ROOT / lesson["path"]
            if lesson["id"] in EDITORIAL_LESSON_IDS:
                # Las clases revisadas editorialmente viven como fuentes
                # explícitas: el generador las publica, pero no vuelve a
                # sintetizar contenido a partir del título.
                source = ROOT / "content" / f"part-{part['id']}" / f"{lesson['id']}.md"
                markdown = source.read_text(encoding="utf-8").replace(
                    "(../../classes/",
                    "(https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/classes/",
                ).replace(
                    "(../../docs/",
                    "(https://github.com/vladimiracunadev-create/software-engineering-learning-suite/blob/main/docs/",
                ).replace(
                    "(../../site/",
                    "(https://vladimiracunadev-create.github.io/software-engineering-learning-suite/",
                )
                result[directory / "README.md"] = markdown
            else:
                markdown = lesson_readme(part, lesson, previous, following)
                result[directory / "README.md"] = markdown
            result[directory / "activity.yaml"] = dump_json(activity(part, lesson))
            result[directory / "rubric.json"] = dump_json(rubric(part, lesson))
            result[ROOT / "site/classes" / f"{lesson['id']}.html"] = site_page(
                part, lesson, markdown, previous, following
            )
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
    approved = sum(
        lesson["status"] == "GUIDED"
        for part in program["parts"] for lesson in part["lessons"]
        if lesson["number"] <= TARGET_LAST_CLASS
    )
    print(f"{action}: {180 - approved} structural drafts, {approved} guided classes, 360 activity/rubric contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
