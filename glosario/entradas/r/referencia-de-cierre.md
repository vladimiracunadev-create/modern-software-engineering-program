# Referencia de cierre

[↑ Glosario](../../README.md) · [← Referencia de API](./referencia-de-api.md) · [Referencia débil →](./referencia-debil.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Palabra clave seguida del identificador de un issue que lo cierra al integrarse en la rama por defecto.

Definición de trabajo de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

## Por qué importa

La clase donde se define, [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md), existe con este propósito: la clase existe para que cada cambio del repositorio se pueda atar al motivo que lo originó y cada motivo a los cambios que lo atendieron, de modo que alguien pueda preguntar «¿por qué está esto así?» y «¿qué falta de lo que se pidió?» sin depender de la memoria de nadie.

## Cómo funciona

[SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md):

En la plataforma, la plantilla de issue pide versión, pasos con los valores exactos, resultado esperado y observado. Los commits llevan un pie `Refs: #42` y la descripción del PR repite `Fixes #42` en la forma documentada. Un trabajo de integración continua construye la matriz de trazabilidad cada semana: cuenta commits de `main` sin referencia, issues cerrados sin commit en `main` y cierres cuyo PR se integró con squash sin cuerpo. El resultado alimenta una conversación sobre el proceso, no un indicador de personas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se vinculan cosas que no cierran nada** — causa: regla ingenua sobre cualquier `#número`. Corrección: usar palabras clave y distinguir referencia de cierre. ([SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. La regla estricta modela la sintaxis documentada y no el analizador de ninguna plataforma, las plantillas y probabilidades son del autor y no se midió ningún alojamiento, proyecto ni persona. La siguiente clase pregunta cómo se acuerdan las convenciones que hacen estos vínculos coherentes y quién responde por cada parte del código.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-197](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-197-trunk-based-gitflow-y-estrategias-hibridas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Issue](../i/issue.md), [Huérfano](../h/huerfano.md), [Pie de commit](../p/pie-de-commit.md), [Trazabilidad](../t/trazabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-198 — Issues, discusiones y trazabilidad del cambio](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: vincular un PR con un issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) — palabras clave, sintaxis y condiciones; autoridad: GitHub Docs.
- [GitHub: plantillas de issues y PR](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates) — plantillas para pedir contexto; autoridad: GitHub Docs.
- [git-interpret-trailers](https://git-scm.com/docs/git-interpret-trailers) — pies de commit estructurados; autoridad: documentación de Git.
- [Gotel y Finkelstein, «An analysis of the requirements traceability problem» (ICRE, 1994)](https://doi.org/10.1109/ICRE.1994.292398) — definición y problemas de la trazabilidad; autoridad: IEEE ICRE.
- [git-log](https://git-scm.com/docs/git-log) — consulta del historial para la matriz; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Referencia de API](./referencia-de-api.md) · [Referencia débil →](./referencia-debil.md)
