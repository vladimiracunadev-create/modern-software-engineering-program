# Construcción reproducible

[↑ Glosario](../../README.md) · [← Constitución](./constitucion.md) · [Constructor de datos →](./constructor-de-datos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Una **construcción reproducible** es aquella que, con el mismo código fuente y las mismas herramientas, produce artefactos idénticos bit a bit. Es el sentido de [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md); [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) y [SE-408](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) lo repiten con otras palabras («los mismos bytes a partir de las mismas fuentes»). Se distingue de una construcción meramente «repetible» (que funciona cada vez) en que el resultado debe poder compararse byte a byte.

## Por qué importa

Cambia lo que una huella puede afirmar. Según [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), cuando la construcción no es reproducible no se puede verificar que lo que se despliega es lo que se probó, ni comparar dos artefactos para ver si cambió algo. [SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) lo aplica a la documentación: si la construcción varía, no se puede comparar lo revisado con lo publicado. La reproducibilidad es la condición para que una huella publicada signifique algo.

## Cómo funciona

[SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) identifica tres causas habituales de no reproducibilidad:

- **Fechas** incrustadas: la fecha de modificación de los archivos fuente o el momento de la construcción.
- **Orden** en que se leen o se empaquetan los archivos, que depende del sistema.
- **Rutas absolutas** del equipo que construye.

La corrección es eliminar cada dependencia ambiental: fijar o normalizar las marcas de tiempo, ordenar de forma determinista la entrada y evitar rutas absolutas en el resultado. El verificador es simple: construir dos veces (idealmente en equipos distintos) y comparar las huellas. Si coinciden, el proceso es reproducible respecto a esa entrada; si no, la diferencia señala la causa.

## Ejemplo

La documentación de la plataforma de entregas ([SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md)) se construye en cada pull request con comprobadores de enlaces y de Markdown, y con una construcción reproducible cuya huella se publica junto a la página. La revisión humana mira exactitud, tarea de la audiencia y tipo de página; la huella permite comprobar después que lo publicado es lo revisado.

## Errores y confusiones comunes

- **Confundirla con una construcción automatizada.** Automatizar no garantiza bytes idénticos.
- **Ignorar el orden del sistema de archivos.** El mismo árbol se empaqueta distinto en dos equipos.
- **Esperar reproducibilidad con herramientas sin fijar.** «Las mismas herramientas» incluye versiones.
- **La suite sale roja y verde sin cambios.** Es inestabilidad de pruebas, no de construcción; corrección de [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md): cuarentena con dueño y plazo, y corregir la causa.

## Límites y cuándo no aplica

Según [SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), no es un fin en sí misma: es la condición para que una huella signifique algo. Si nadie compara huellas, la reproducibilidad no aporta nada. Tampoco garantiza que el artefacto sea correcto ni seguro: dos construcciones idénticas pueden ser idénticamente defectuosas. Y lograrla en proyectos con muchas dependencias puede ser costoso; en ese caso se prioriza por riesgo, empezando por lo que se despliega.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-211](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Artefacto](../a/artefacto.md), [Byte](../b/byte.md), [Herramientas](../h/herramientas.md), [Proceso](../p/proceso.md), [Ancla](../a/ancla.md), [Documentación como código](../d/documentacion-como-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-108](../../../classes/part-08-entornos-herramientas-y-depuracion/se-108-proyecto-entorno-de-desarrollo-autocontenido/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-216](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-216-proyecto-portal-documental-versionado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reproducible Builds](https://reproducible-builds.org/docs/) — causas y prácticas de la construcción reproducible; autoridad: proyecto Reproducible Builds.
- [Luo et al., «An empirical analysis of flaky tests»](https://doi.org/10.1145/2635868.2635920) — causas de las pruebas inestables; autoridad: FSE 2014.
- [Python: zipfile](https://docs.python.org/3/library/zipfile.html) — fechas y orden de los miembros de un archivo; autoridad: documentación de Python.
- [DORA: las cuatro claves](https://dora.dev/guides/dora-metrics-four-keys/) — métricas de entrega; autoridad: DORA.
- [Wilson (1927)](https://doi.org/10.1080/01621459.1927.10502953) — intervalo para una proporción; autoridad: Journal of the American Statistical Association.

---

[↑ Glosario](../../README.md) · [← Constitución](./constitucion.md) · [Constructor de datos →](./constructor-de-datos.md)
