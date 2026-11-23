# Pie de commit

[↑ Glosario](../../README.md) · [← PID](./pid.md) · [Pila de PR →](./pila-de-pr.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Línea `clave: valor` al final del mensaje de un commit, legible por herramientas.

Definición de trabajo de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

## Por qué importa

La clase donde se define, [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), existe con este propósito: la clase existe para que cada cambio del repositorio se pueda atar al motivo que lo originó y cada motivo a los cambios que lo atendieron, de modo que alguien pueda preguntar «¿por qué está esto así?» y «¿qué falta de lo que se pidió?» sin depender de la memoria de nadie.

## Cómo funciona

Según [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

Un mensaje puede referenciar un issue (`Refs #42`) o cerrarlo (`Fixes #42`) con palabras clave que la plataforma reconoce. La documentación de GitHub lista `close`, `closes`, `closed`, `fix`, `fixes`, `fixed`, `resolve`, `resolves` y `resolved`, exige repetir la palabra para cada issue y solo las interpreta cuando el cambio llega a la rama por defecto. Los pies de commit estructurados (`Refs: #42`) son legibles por herramientas como `git interpret-trailers` y no dependen de una plataforma.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

En la plataforma, la plantilla de issue pide versión, pasos con los valores exactos, resultado esperado y observado. Los commits llevan un pie `Refs: #42` y la descripción del PR repite `Fixes #42` en la forma documentada. Un trabajo de integración continua construye la matriz de trazabilidad cada semana: cuenta commits de `main` sin referencia, issues cerrados sin commit en `main` y cierres cuyo PR se integró con squash sin cuerpo. El resultado alimenta una conversación sobre el proceso, no un indicador de personas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md)) son:

- **El issue no se cierra al integrar** — causa: la sintaxis no es la reconocida o falta la palabra por cada issue. Corrección: repetir la palabra clave para cada número y usar la forma documentada.
- **El vínculo desaparece tras el squash** — causa: el mensaje final no copia el cuerpo. Corrección: generar el mensaje del squash desde la descripción del PR.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Los pies de commit estructurados (`Refs: #42`) son legibles por herramientas como `git interpret-trailers` y no dependen de una plataforma. ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Herramientas](../h/herramientas.md), [Valor](../v/valor.md), [Huérfano](../h/huerfano.md), [Issue](../i/issue.md), [Referencia de cierre](../r/referencia-de-cierre.md), [Trazabilidad](../t/trazabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers) — pies de commit estructurados; autoridad: documentación de Git.
- [git-commit](https://git-scm.com/docs/git-commit) — mensajes y pies de commit.
- [GitHub: vincular un PR con un issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) — palabras clave, sintaxis y condiciones; autoridad: GitHub Docs.
- [GitHub: plantillas de issues y PR](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) — plantillas para pedir contexto; autoridad: GitHub Docs.
- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE ICRE.

---

[↑ Glosario](../../README.md) · [← PID](./pid.md) · [Pila de PR →](./pila-de-pr.md)
