# Objeto

[↑ Glosario](../../README.md) · [← Objetivo táctil](./objetivo-tactil.md) · [Objeto alcanzable →](./objeto-alcanzable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Unidad inmutable de la base de Git (blob, árbol, commit o etiqueta anotada) identificada por el hash de su contenido.

Definición de trabajo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md): Recurso sobre el que se evalúa la solicitud.

## Por qué importa

En [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), el tema «Objetos direccionados por contenido» importa porque explica por qué un identificador cambia con cualquier byte y por qué dos contenidos iguales comparten objeto.

## Cómo funciona

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Git guarda cada objeto bajo el hash de su contenido precedido por una cabecera con el tipo y el tamaño. Por eso el identificador no se asigna: se calcula. Dos consecuencias prácticas: el mismo contenido en cualquier lugar del repositorio es un solo objeto, y cambiar un byte produce un identificador sin relación con el anterior. La propiedad también hace que los objetos sean inmutables: no se «edita» un commit, se crea otro, y lo que llamamos editar la historia es construir objetos nuevos y mover un nombre.

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Conceptualmente, instantáneas completas: cada commit apunta a un árbol entero. El empaquetado usa diferencias entre objetos parecidos para ahorrar espacio, pero eso es un detalle de almacenamiento que no cambia lo que Git muestra.

## Ejemplo

Ejemplo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sección «Ejemplo mínimo»):

El fragmento crea un repositorio temporal, guarda dos archivos con el mismo contenido y cuenta los blobs. Antes de ejecutarlo, predice cuántos objetos de cada tipo habrá.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se cree que dos copias de un archivo ocupan el doble** — causa: se supone que se guardan copias, no objetos por contenido. Corrección: contar objetos con `git cat-file --batch-all-objects --batch-check`. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Dos consecuencias prácticas: el mismo contenido en cualquier lugar del repositorio es un solo objeto, y cambiar un byte produce un identificador sin relación con el anterior. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))
- El empaquetado usa diferencias entre objetos parecidos para ahorrar espacio, pero eso es un detalle de almacenamiento que no cambia lo que Git muestra. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-026](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-026-sistemas-de-archivos-rutas-enlaces-y-metadatos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Árbol](../a/arbol.md), [Base](../b/base.md), [Blob](../b/blob.md), [Etiqueta](../e/etiqueta.md), [ACL](../a/acl.md), [Autenticación](../a/autenticacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-027 — Usuarios, grupos, permisos y elevación de privilegios](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (105 clases más lo mencionan; las que más):

[SE-021](../../../classes/part-01-computadores-y-representacion-de-informacion/se-021-runtimes-maquinas-virtuales-y-recoleccion-de-basura/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-314](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-314-gof-creacionales-factory-builder-singleton-y-prototype/README.md), [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-329](../../../classes/part-27-arquitectura-de-software-y-dominio/se-329-domain-driven-design-estrategico-y-tactico/README.md), [SE-316](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-316-gof-conductuales-strategy-observer-command-state-y-template-method/README.md), [SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

**Aparece en los casos de estudio:** [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-gc](https://git-scm.com/docs/git-gc) — recolección de objetos y empaquetado; autoridad: documentación de Git.
- [git-cat-file](https://git-scm.com/docs/git-cat-file) — inspección de objetos usada en los experimentos.
- [git-count-objects](https://git-scm.com/docs/git-count-objects) — recuento de objetos sueltos y empaquetados.
- [Pro Git: Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) — formato de blobs, árboles y commits; autoridad: Pro Git.
- [git-hash-object](https://git-scm.com/docs/git-hash-object) — cálculo del identificador de un contenido; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Objetivo táctil](./objetivo-tactil.md) · [Objeto alcanzable →](./objeto-alcanzable.md)
