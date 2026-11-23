# Informe de entrega

[↑ Glosario](../../README.md) · [← Informe de decisión](./informe-de-decision.md) · [Informe de límites →](./informe-de-limites.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Documento que dice qué se comprobó, qué no puede comprobarse y qué quedó pendiente.

Definición de trabajo de [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md).

## Por qué importa

La clase donde se define, [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), existe con este propósito: el proyecto existe para entregar un portal documental que otra persona pueda mantener sin ti: páginas con dueño y tipo, decisiones registradas, una API con ejemplos que se ejecutan, runbooks seguros de repetir, un glosario, comprobaciones automáticas, versiones coherentes consigo mismas y un paquete cuya huella se reproduce en dos sistemas, junto con un informe que dice qué se comprobó y qué no.

## Cómo funciona

Según [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md):

El portal de la plataforma de entregas se entrega con un repositorio con tres etiquetas (`v1`, `v2`, `v3`), una política de páginas retiradas (cada página retirada deja una página mínima con el aviso y el enlace a su sucesora durante dos versiones), un paquete zip determinista cuya huella se publica con el informe, y una auditoría que ejecuta los comprobadores de la parte y los ejemplos de la API contra el servicio de pruebas. El informe de entrega tiene tres secciones: lo comprobado (con la salida de cada comprobador), lo inferido (la validez de la regla de ancla del sitio publicado) y lo no ejecutado (la publicación real y la experiencia de quienes lo leen).

## Ejemplo

Ejemplo de [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) (sección «Ejemplo profesional»):

El portal de la plataforma de entregas se entrega con un repositorio con tres etiquetas (`v1`, `v2`, `v3`), una política de páginas retiradas (cada página retirada deja una página mínima con el aviso y el enlace a su sucesora durante dos versiones), un paquete zip determinista cuya huella se publica con el informe, y una auditoría que ejecuta los comprobadores de la parte y los ejemplos de la API contra el servicio de pruebas.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md)) son:

- **Una versión nueva tiene enlaces rotos que ya tenía la anterior** — causa: nadie los corrigió al etiquetar. Corrección: bloquear la etiqueta con la auditoría de enlaces.
- **Las huellas del paquete difieren entre Windows y Linux** — causa: campos de sistema de origen, orden o saltos de línea. Corrección: fijar orden, fecha, permisos y sistema de origen, y normalizar los saltos de línea.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md)) son: Las definiciones son operativas para el portal; no reemplazan las de las fuentes enlazadas abajo. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se publicó ningún sitio real ni se midió a ningún lector: el portal de diez páginas, el árbol de 30 páginas y los 12 defectos sembrados son construcciones del autor, y los enlaces entre versiones no se midieron.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Documento](../d/documento.md), [Paquete reproducible](../p/paquete-reproducible.md), [Política de enlaces entre versiones](../p/politica-de-enlaces-entre-versiones.md), [Portal documental](../p/portal-documental.md), [Versión etiquetada](../v/version-etiquetada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-352](../../../classes/part-29-datos-persistencia-y-recuperacion/se-352-restricciones-invariantes-y-consistencia/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/) — convención de versiones; autoridad: especificación SemVer.
- [Read the Docs: versiones](https://docs.readthedocs.com/platform/stable/versions.html) — publicación de varias versiones de documentación; autoridad: Read the Docs.
- [mike: versionado de documentación con MkDocs](https://github.com/jimporter/mike) — herramienta de ejemplo de versiones desde Git; autoridad: proyecto mike.
- [Keep a Changelog](https://keepachangelog.com/) — convención de registro de cambios; autoridad: proyecto Keep a Changelog.
- [GitHub Pages: documentación](https://docs.github.com/en/pages) — publicación de sitios estáticos desde un repositorio; autoridad: GitHub Docs.

---

[↑ Glosario](../../README.md) · [← Informe de decisión](./informe-de-decision.md) · [Informe de límites →](./informe-de-limites.md)
