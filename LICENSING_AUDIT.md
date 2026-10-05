# Auditoría de licencias y propiedad intelectual

**Repositorio:** `vladimiracunadev-create/modern-software-engineering-program`  
**Fecha de corte:** 2026-10-05  
**Alcance:** árbol Git, historial local, código, contenido pedagógico, catálogos,
datos estructurados, workflows, portal, activos y referencias externas.

## Resultado ejecutivo

La licencia MIT única no distinguía entre software ejecutable, 480 clases,
evaluaciones, datos editoriales, diagramas y referencias de terceros. Se implantó
una matriz equivalente en alcance a la del Programa de Ciberseguridad Moderna y
adaptada a los materiales que realmente existen aquí.

| Material propio | Licencia desde esta revisión |
| --- | --- |
| Código, scripts, workflows, CSS, JavaScript, configuraciones y esquemas ejecutables | Apache-2.0 |
| Clases, rutas, documentación pedagógica, ejercicios, evaluaciones y rúbricas | CC BY-NC-SA 4.0 |
| Ejemplos de código destinados a copiarse y ejecutarse | Apache-2.0 |
| Datos educativos y selección/estructura original de registros editoriales | CC BY-NC-SA 4.0 |
| Diagramas y activos pedagógicos propios | CC BY-NC-SA 4.0 |
| Obras, estándares, herramientas, marcas y recursos de terceros | Licencia o derecho original; fuera de la concesión del proyecto |

Las revisiones ya publicadas bajo MIT conservan esa licencia. No se reescribieron
commits ni se revocaron permisos anteriores.

## Evidencia examinada

La siguiente instantánea se tomó antes de añadir los documentos y controles de esta
auditoría. Se conserva como evidencia histórica, no como contador vivo:

- 2.533 archivos versionados y 71 commits;
- 756 archivos Markdown, incluidos 480 README de clase;
- 19 scripts o pruebas Python;
- 364 archivos YAML, 863 JSON y 522 HTML;
- cero activos binarios PNG, JPEG, GIF, WebP, SVG, iconos, PDF o PPTX;
- dos workflows existentes: validación y Pages;
- ausencia de manifests de paquetes, lockfiles, imágenes de contenedor y código
  vendorizado;
- un único autor humano en el historial Git disponible: Vladimir Acuña.

## Hallazgos y resolución

### L-01 — licencia única sin frontera material

**Impacto:** alto. MIT aparecía como licencia de código y contenido sin explicar
datos, salidas generadas ni terceros.  
**Resolución:** `LICENSE` contiene Apache-2.0 para software y
`LICENSE-CONTENT.md` delimita CC BY-NC-SA 4.0. `NOTICE` actúa como mapa de entrada.

### L-02 — afirmación pública desincronizada

**Impacto:** alto. El badge y la sección de licencia del README atribuían MIT a todo
el material original.  
**Resolución:** se sustituyeron por dos badges, una matriz visual y enlaces directos
a todos los avisos. La mención histórica de MIT se conserva sólo donde explica la
transición.

### L-03 — datos editoriales sin política específica

**Impacto:** medio. Currículo, catálogos, rúbricas, actividades y registros de
fuentes mezclaban hechos, estructura original y contratos ejecutables.  
**Resolución:** `DATA_LICENSES.md` clasifica cada familia y separa contenido CC de
esquemas y contratos Apache.

### L-04 — activos y salidas generadas sin inventario

**Impacto:** medio. No hay binarios versionados, pero sí Mermaid, CSS, JavaScript y
HTML generado.  
**Resolución:** `ASSET_LICENSES.md` registra esa ausencia y explica la licencia de
cada superficie textual o generada, además del control exigido para futuros activos.

### L-05 — herramientas y fuentes externas sin aviso central

**Impacto:** medio. Python, GitHub Actions, Mermaid, Shields.io y cientos de fuentes
se usaban o citaban sin un mapa único.  
**Resolución:** `THIRD_PARTY_NOTICES.md` distingue ejecución, automatización,
servicios, formatos y obras enlazadas. No afirma que una cita relicencie una obra.

### L-06 — transición sin prueba de no retroactividad

**Impacto:** alto. Reemplazar el archivo raíz sin historia podía sugerir que MIT
dejaba de aplicar a copias anteriores.  
**Resolución:** `docs/LICENSING_HISTORY.md` identifica el primer commit, la fecha de
transición y un procedimiento reproducible para inspeccionar cualquier revisión.

### L-07 — marcas confundibles con licencia de copyright

**Impacto:** medio. Una licencia de software o contenido no concede por sí misma el
uso promocional de nombres y logos.  
**Resolución:** `TRADEMARKS.md` permite identificación razonable y prohíbe sugerir
patrocinio, certificación o carácter oficial inexistente.

### L-08 — controles manuales sin gate automatizado

**Impacto:** medio. Los documentos podían desaparecer o volver a contradecir el
README sin que CI fallara.  
**Resolución:** `scripts/validate_licensing.py`, pruebas y los workflows verifican la
matriz, la presencia de avisos y los contratos de mantenimiento.

## Riesgos residuales

- Esta revisión técnica no demuestra acuerdos privados ni titularidad de material
  que nunca entró en Git.
- Las licencias, términos de servicios y versiones de herramientas pueden cambiar;
  el inventario debe revisarse junto con cada actualización.
- Una futura distribución con dependencias deberá producir un SBOM y avisos desde
  los componentes realmente incorporados; hoy no existe ese artefacto.
- CC BY-NC-SA 4.0 limita el uso comercial del contenido. La compatibilidad de una
  adaptación concreta requiere analizar su forma de distribución y jurisdicción.
- El uso permitido por copyright no equivale a certificación profesional,
  patrocinio, garantía técnica ni permiso para acceder a sistemas de terceros.

## Controles de mantenimiento

1. Clasificar cada contribución como software, contenido, dato, activo o tercero.
2. Rechazar material externo sin fuente, permiso, licencia compatible y atribución.
3. Actualizar avisos al cambiar acciones, dependencias, imágenes o herramientas.
4. Documentar procedencia, privacidad y licencia de todo dataset nuevo.
5. Registrar activos nuevos y conservar su fuente reproducible.
6. Incluir `LICENSE`, `LICENSE-CONTENT.md`, `NOTICE` y avisos aplicables en una
   distribución.
7. Ejecutar `python scripts/validate_licensing.py` y la suite completa antes de
   publicar.

## Documentos resultantes

- [LICENSE](LICENSE) — Apache License 2.0 para software propio.
- [LICENSE-CONTENT.md](LICENSE-CONTENT.md) — CC BY-NC-SA 4.0 para contenido.
- [NOTICE](NOTICE) — atribución y mapa de licencias.
- [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) — software y recursos externos.
- [ASSET_LICENSES.md](ASSET_LICENSES.md) — activos visuales y salidas generadas.
- [DATA_LICENSES.md](DATA_LICENSES.md) — datos y registros editoriales.
- [TRADEMARKS.md](TRADEMARKS.md) — nombres, marcas y ausencia de patrocinio.
- [docs/LICENSING_HISTORY.md](docs/LICENSING_HISTORY.md) — cronología sin
  retroactividad.

Esta auditoría es documental y técnica; no sustituye asesoría jurídica.

