# Índice

[↑ Glosario](../../README.md) · [← Indicadores y demora](./indicadores-y-demora.md) · [Índice como proyección →](./indice-como-proyeccion.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Instantánea que se prepara para el próximo commit; vive entre el árbol de trabajo y HEAD.

Definición de trabajo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md).

## Por qué importa

La clase donde se define, [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), existe con este propósito: la clase existe para que una persona deje de usar Git como una lista de comandos que a veces funciona y lo use como lo que es: una base de objetos direccionada por contenido, tres áreas donde un cambio puede estar y referencias que apuntan a commits.

## Cómo funciona

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Un cambio puede estar en el árbol de trabajo (archivos en disco), en el índice (la instantánea que se prepara para el próximo commit) o en HEAD (el último commit). `git add` copia del árbol de trabajo al índice, `git commit` convierte el índice en un commit, `git restore` sobrescribe el árbol de trabajo desde el índice y `git restore --staged` sobrescribe el índice desde HEAD. El código de dos letras de `git status --porcelain` es una comparación por pares: la primera letra es índice contra HEAD y la segunda árbol de trabajo contra índice. Saber en qué área está un cambio es saber qué comando puede perderlo.

Según [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md):

Porque compara dos pares: la primera letra es el índice frente a HEAD y la segunda el árbol de trabajo frente al índice. `AM` significa agregado y modificado después de agregarlo.

## Ejemplo

Ejemplo de [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) (sección «Preguntas frecuentes»):

Porque compara dos pares: la primera letra es el índice frente a HEAD y la segunda el árbol de trabajo frente al índice. `AM` significa agregado y modificado después de agregarlo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`git diff` aparece vacío pese a haber cambios** — causa: los cambios ya están en el índice. Corrección: usar `git diff --cached` o `git diff HEAD`. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el diagrama describe archivos de texto sin conflictos, sin submódulos y sin `assume-unchanged`; durante una fusión conflictiva aparecen otros códigos (como `UU`) y el índice contiene tres versiones del mismo archivo. ([SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Árbol de trabajo](../a/arbol-de-trabajo.md), [Árbol](../a/arbol.md), [Instantánea](./instantanea.md), [Trabajo](../t/trabajo.md), [Blob](../b/blob.md), [Objeto](../o/objeto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-193 — Modelo de objetos y áreas de Git](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (580 clases más lo mencionan; las que más):

[SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md), [SE-093](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-093-indices-probabilisticas-y-estructuras-persistentes/README.md), [SE-350](../../../classes/part-29-datos-persistencia-y-recuperacion/se-350-relacional-documental-clave-valor-grafos-y-series/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-111](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-111-resolucion-de-dependencias-y-lockfiles/README.md), [SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Stripe](../../../casos/exito/stripe.md), [Discord](../../../casos/exito/discord.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

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

[↑ Glosario](../../README.md) · [← Indicadores y demora](./indicadores-y-demora.md) · [Índice como proyección →](./indice-como-proyeccion.md)
