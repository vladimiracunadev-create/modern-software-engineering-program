# Índice de archivos del programa

| Superficie | Ruta | Cantidad esperada |
| --- | --- | ---: |
| Manifiesto canónico | `curriculum.yaml` | 1 |
| Catálogo resumido | `catalog.json` | 1 |
| Índice general | `classes/README.md` | 1 |
| Índice de rutas profesionales | `roles/README.md` | 1 |
| Guías profesionales | `roles/*.md` (sin `README.md`) | 45 |
| Perfiles fuente de las rutas | `scripts/role_profiles.py` | 45 perfiles |
| Generador verificable de rutas | `scripts/build_role_guides.py` | 1 |
| Licencia de software | `LICENSE` | Apache-2.0 |
| Licencia de contenido | `LICENSE-CONTENT.md` | CC BY-NC-SA 4.0 |
| Avisos e inventarios de propiedad intelectual | `NOTICE`, `*_LICENSES.md`, `THIRD_PARTY_NOTICES.md`, `TRADEMARKS.md` | 5 documentos |
| Auditoría e historia de licencias | `LICENSING_AUDIT.md`, `docs/LICENSING_HISTORY.md` | 2 documentos |
| Arquitectura de automatización | `docs/WORKFLOW-ARCHITECTURE.md` | 3 workflows |
| Validador de licencias | `scripts/validate_licensing.py` | 1 |
| Índices de parte | `classes/part-*/README.md` | 47 |
| Materiales de clase | `classes/part-*/se-*/README.md` | 564 |
| Metadatos de clase | `classes/part-*/se-*/lesson.json` | 564 |
| Fuentes por clase | `sources/class-sources.json` | 564 entradas |
| Fuentes verificadas de fase 3 | `sources/phase3.json` | 15 partes |
| Contratos de actividad de fase 3 | `classes/part-*/se-*/activity.yaml` | 180 contratos |
| Rúbricas de fase 3 | `classes/part-*/se-*/rubric.json` | 180 contratos |
| Contratos de actividad de fase 4 | `classes/part-15..29/se-*/activity.yaml` | 180 contratos |
| Rúbricas de fase 4 | `classes/part-15..29/se-*/rubric.json` | 180 contratos |
| Índice de laboratorios ejecutables | `labs/README.md` | 1 |
| Laboratorio validado de la Parte 01 | `labs/part-01-machine-observer/` | código, fixture, 6 pruebas y evidencia |
| Laboratorio validado de la Parte 02 | `labs/part-02-cross-platform-diagnostic-kit/` | núcleo, 2 adaptadores, 10 pruebas y evidencia |
| Páginas del sitio | `site/**/*.html` (sin `site/casos/`) | 612 |
| Casos de estudio | `casos/GUIDE.md`, `casos/{exito,fallo}/*.md` | 1 guía, 2 páginas de grupo y 16 casos |
| Páginas de casos | `site/casos/**/*.html` | 18 |

Todos los conteos se validan contra `curriculum.yaml`.
