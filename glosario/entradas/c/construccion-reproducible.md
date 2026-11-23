# Construcción reproducible

[↑ Glosario](../../README.md) · [← Constitución](./constitucion.md) · [Constructor de datos →](./constructor-de-datos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md)

## Definición

Construcción que, con el mismo código y las mismas herramientas, produce artefactos idénticos bit a bit.

Definición de trabajo de [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md): Construcción que produce los mismos bytes a partir de las mismas fuentes.
- En [SE-408 — Proyecto: plataforma mínima reproducible](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-408-proyecto-plataforma-minima-reproducible/README.md): Proceso que, con las mismas entradas, produce siempre los mismos bytes.

## Por qué importa

En [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), el tema «Construcción reproducible» importa porque sin ella, no se sabe qué se probó.

En [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), el tema «Construcción reproducible» importa porque si la construcción varía, no se puede comparar lo revisado con lo publicado.

## Cómo funciona

Según [SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md), en la sección «Construcción reproducible»:

Una construcción es **reproducible** si, dado el mismo código fuente y las mismas herramientas, produce un artefacto idéntico bit a bit. Cuando no lo es, no se puede verificar que lo que se despliega es lo que se probó, ni comparar artefactos de dos construcciones para ver si cambió algo. Las causas habituales son tres. Las **fechas** incrustadas: la fecha de modificación de los archivos fuente o del momento de construcción. El **orden** en que se leen o se empaquetan los archivos, que depende del sistema. Y las **rutas** absolutas del equipo que construye.

## Ejemplo

Ejemplo de [SE-212 — Docs as code, revisión y publicación](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md) (sección «Ejemplo profesional»):

La documentación de la plataforma de entregas se construye en cada pull request: un comprobador de enlaces y anclas con la regla del sitio, un linter de Markdown consciente de los bloques de código, los comprobadores de las clases anteriores (opciones del README, grafo de ADR, diagrama frente a importaciones, ejemplos de la API, linter de runbooks) y una construcción reproducible cuya huella se publica junto a la página. La revisión humana mira exactitud, tarea de la audiencia y tipo de página, con una lista corta.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-527 — Taller: estabilizar antes de modernizar](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md)) son:

- **La suite sale roja y verde sin cambios** — causa: pruebas inestables. Corrección: cuarentena con dueño y plazo, y corregir la causa.
- **Un defecto intermitente llega a producción** — causa: reintentos globales que lo escondieron. Corrección: eliminar los reintentos globales y repetir solo lo nuevo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una construcción reproducible no es un fin en sí misma: es la condición para que una huella signifique algo. ([SE-527](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-527-taller-estabilizar-antes-de-modernizar/README.md))

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
