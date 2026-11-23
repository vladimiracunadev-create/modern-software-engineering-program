# Blob

[↑ Glosario](../../README.md) · [← Blast radius](./blast-radius.md) · [Bloom filter →](./bloom-filter.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Contenido de un archivo, sin nombre ni permisos.

Definición de trabajo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md).

## Por qué importa

En [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), el tema «Blobs, árboles y commits» importa porque separa contenido, estructura e historia; permite entender qué cambia al renombrar o mover.

## Cómo funciona

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Un blob es el contenido de un archivo sin nombre ni permisos. Un árbol es una lista de entradas (modo, nombre, identificador) que da nombre y estructura a blobs y a otros árboles. Un commit apunta a un árbol, a cero o más padres y lleva autoría, fecha y mensaje. El nombre del archivo vive en el árbol, no en el blob: por eso un renombre cambia el árbol y deja intacto el blob. Y por eso un commit no «contiene un cambio»: contiene la instantánea completa, y el cambio es la diferencia con el padre calculada al pedirla.

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

En el repositorio de la plataforma, el módulo `penal.py` se renombra a `reglas/penalizacion.py` en un commit que no cambia su contenido. La revisión muestra el renombre porque Git compara dos árboles y detecta que un blob desapareció de una ruta y apareció idéntico en otra. Una persona que quiere recuperar una versión anterior del archivo no necesita «deshacer el renombre»: pide el blob de ese commit con `git show <commit>:ruta` o restaura la ruta antigua desde ese árbol.

## Ejemplo

Ejemplo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sección «Ejemplo mínimo»):

El fragmento crea un repositorio temporal, guarda dos archivos con el mismo contenido y cuenta los blobs. Antes de ejecutarlo, predice cuántos objetos de cada tipo habrá.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md)) son:

- **Se pierde trabajo tras `git restore`** — causa: el cambio estaba solo en el árbol de trabajo. Corrección: agregar o confirmar antes de ejecutar comandos que sobrescriben.
- **`git diff` aparece vacío pese a haber cambios** — causa: los cambios ya están en el índice. Corrección: usar `git diff --cached` o `git diff HEAD`.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un blob es el contenido de un archivo sin nombre ni permisos. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Permiso](../p/permiso.md), [Árbol](../a/arbol.md), [Índice](../i/indice.md), [Objeto](../o/objeto.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-194](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-194-commits-atomicos-historial-y-recuperacion/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Pro Git: Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) — formato de blobs, árboles y commits; autoridad: Pro Git.
- [git-hash-object](https://git-scm.com/docs/git-hash-object) — cálculo del identificador de un contenido; autoridad: documentación de Git.
- [git-status](https://git-scm.com/docs/git-status) — formato corto y significado de los códigos de dos letras; autoridad: documentación de Git.
- [git-gc](https://git-scm.com/docs/git-gc) — recolección de objetos y empaquetado; autoridad: documentación de Git.
- [Pro Git: Packfiles](https://git-scm.com/book/en/v2/Git-Internals-Packfiles) — almacenamiento con deltas; autoridad: Pro Git.

---

[↑ Glosario](../../README.md) · [← Blast radius](./blast-radius.md) · [Bloom filter →](./bloom-filter.md)
