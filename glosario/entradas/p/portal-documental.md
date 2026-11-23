# Portal documental

[↑ Glosario](../../README.md) · [← Portafolio](./portafolio.md) · [Poscondición →](./poscondicion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Conjunto de páginas, decisiones, referencias y procedimientos con dueños, tipos y comprobaciones, publicado para varias audiencias.

Definición de trabajo de [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md).

## Por qué importa

La clase donde se define, [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md), existe con este propósito: el proyecto existe para entregar un portal documental que otra persona pueda mantener sin ti: páginas con dueño y tipo, decisiones registradas, una API con ejemplos que se ejecutan, runbooks seguros de repetir, un glosario, comprobaciones automáticas, versiones coherentes consigo mismas y un paquete cuya huella se reproduce en dos sistemas, junto con un informe que dice qué se comprobó y qué no.

## Cómo funciona

Según [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md):

Un portal documental no es un directorio de archivos: tiene audiencias que lo usan para cumplir tareas, tipos de página que se escriben de formas distintas, decisiones registradas, un glosario, una API documentada, procedimientos operativos y comprobaciones. Cada pieza tiene un dueño y una fecha. Tratarlo como producto significa decidir qué entra y qué no, quién lo mantiene, cómo se mide su salud y qué se promete. La entrega del proyecto es el portal junto con el informe que dice en qué estado está.

Según [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md):

Traslada el proyecto a otro dominio (por ejemplo, el portal documental de un servicio de reparto): cambian las páginas y los valores a verificar, se conservan el versionado desde etiquetas, la política de retirada, el paquete determinista, la auditoría con límites declarados y los indicadores con dueño. La transferencia está lograda cuando puedes explicar qué parte del portal depende de la plataforma y cuál es estructura reutilizable.

## Ejemplo

Ejemplo de [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) (sección «Caso conductor»):

Esta clase cierra el caso conductor de la [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md): el portal documental de la plataforma de entregas, con todas las piezas de las clases anteriores reunidas, versionadas y auditadas. Entrega a la [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md) una lección concreta: las opciones, las ayudas y los ejemplos de una interfaz de línea de comandos son documentación que se comprueba con las mismas técnicas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md)) son:

- **Una versión nueva tiene enlaces rotos que ya tenía la anterior** — causa: nadie los corrigió al etiquetar. Corrección: bloquear la etiqueta con la auditoría de enlaces.
- **Las huellas del paquete difieren entre Windows y Linux** — causa: campos de sistema de origen, orden o saltos de línea. Corrección: fijar orden, fecha, permisos y sistema de origen, y normalizar los saltos de línea.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un portal documental no es un directorio de archivos: tiene audiencias que lo usan para cumplir tareas, tipos de página que se escriben de formas distintas, decisiones registradas, un glosario, una API documentada, procedimientos operativos y comprobaciones. ([SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md))
- Traslada el proyecto a otro dominio (por ejemplo, el portal documental de un servicio de reparto): cambian las páginas y los valores a verificar, se conservan el versionado desde etiquetas, la política de retirada, el paquete determinista, la auditoría con límites declarados y los indicadores con dueño. ([SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Audiencia](../a/audiencia.md), [Conjunto](../c/conjunto.md), [Página](./pagina.md), [Referencia](../r/referencia.md), [Informe de entrega](../i/informe-de-entrega.md), [Paquete reproducible](./paquete-reproducible.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-216 — Proyecto: portal documental versionado](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md).

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

[↑ Glosario](../../README.md) · [← Portafolio](./portafolio.md) · [Poscondición →](./poscondicion.md)
