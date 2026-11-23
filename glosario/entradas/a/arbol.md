# Árbol

[↑ Glosario](../../README.md) · [← Aproximación](./aproximacion.md) · [Árbol de accesibilidad →](./arbol-de-accesibilidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Lista de entradas con modo, nombre e identificador que da estructura a blobs y a otros árboles.

Definición de trabajo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md).

## Por qué importa

La clase donde se define, [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), existe con este propósito: la clase existe para que una persona deje de usar Git como una lista de comandos que a veces funciona y lo use como lo que es: una base de objetos direccionada por contenido, tres áreas donde un cambio puede estar y referencias que apuntan a commits.

## Cómo funciona

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Un blob es el contenido de un archivo sin nombre ni permisos. Un árbol es una lista de entradas (modo, nombre, identificador) que da nombre y estructura a blobs y a otros árboles. Un commit apunta a un árbol, a cero o más padres y lleva autoría, fecha y mensaje. El nombre del archivo vive en el árbol, no en el blob: por eso un renombre cambia el árbol y deja intacto el blob. Y por eso un commit no «contiene un cambio»: contiene la instantánea completa, y el cambio es la diferencia con el padre calculada al pedirla.

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

En el repositorio de la plataforma, el módulo `penal.py` se renombra a `reglas/penalizacion.py` en un commit que no cambia su contenido. La revisión muestra el renombre porque Git compara dos árboles y detecta que un blob desapareció de una ruta y apareció idéntico en otra. Una persona que quiere recuperar una versión anterior del archivo no necesita «deshacer el renombre»: pide el blob de ese commit con `git show <commit>:ruta` o restaura la ruta antigua desde ese árbol.

## Ejemplo

Ejemplo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sección «Ejemplo mínimo»):

Debe haber un blob (los dos archivos lo comparten), un árbol y un commit. Registra versión de Git y salida, y repite con `git mv a.txt c.txt` para comprobar que el blob no cambia.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se pierde trabajo tras `git restore`** — causa: el cambio estaba solo en el árbol de trabajo. Corrección: agregar o confirmar antes de ejecutar comandos que sobrescriben. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El nombre del archivo vive en el árbol, no en el blob: por eso un renombre cambia el árbol y deja intacto el blob. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Blob](../b/blob.md), [Estructura](../e/estructura.md), [Índice](../i/indice.md), [Objeto](../o/objeto.md), [Referencia](../r/referencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (94 clases más lo mencionan; las que más):

[SE-143](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-143-taller-disenar-un-arbol-de-metricas/README.md), [SE-088](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-088-arboles-tries-y-estructuras-jerarquicas/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-469](../../../classes/part-39-build-release-y-cadena-de-suministro/se-469-build-reproducible-y-hermetico/README.md), [SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-578](../../../classes/part-48-harness-y-agentic-engineering/se-578-instrucciones-de-repositorio-y-cumplimiento-determinista/README.md).

**Aparece en los casos de estudio:** [Knight Capital](../../../casos/fallo/knight-capital.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Therac-25](../../../casos/fallo/therac-25.md), [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md), [Quibi](../../../casos/fallo/quibi.md).

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

[↑ Glosario](../../README.md) · [← Aproximación](./aproximacion.md) · [Árbol de accesibilidad →](./arbol-de-accesibilidad.md)
