# Comprobación automática

[↑ Glosario](../../README.md) · [← Comprensión](./comprension.md) · [Comprobación de calidad →](./comprobacion-de-calidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Verificación ejecutada por una máquina antes o durante la revisión humana.

Definición de trabajo de [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).

## Por qué importa

En [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), el tema «Comprobaciones automáticas» importa porque liberan a la persona de lo que una máquina comprueba y dejan para ella el sentido.

## Cómo funciona

Según [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), en la sección «Comprobaciones automáticas»:

Compilación, pruebas, análisis estático, formato, licencias y secretos son comprobaciones que no necesitan a una persona. Deben ejecutarse antes de pedir una revisión humana, de modo que la lectura se dedique al sentido (¿es esta la regla correcta?, ¿se probó el caso límite?). Una comprobación automática detecta forma y no intención, y por eso no sustituye la lectura de los archivos de mayor riesgo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md):

En la plataforma, la plantilla de PR pide qué cambia, por qué, cómo se probó y qué archivos merecen más atención. Un flujo de integración continua ejecuta formato, pruebas, análisis estático y búsqueda de secretos antes de asignar revisora. El CODEOWNERS, tema de `SE-199`, añade como revisor obligatorio al equipo dueño de las migraciones cuando un PR toca `migraciones/`. La revisora abre primero los archivos marcados como riesgo alto, lee la descripción y, tras las correcciones, usa `range-diff` para ver lo cambiado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md)) son:

- **Comentarios de estilo y defectos que se escapan** — causa: la lectura sigue el orden del diff. Corrección: ordenar por riesgo y automatizar el estilo.
- **Hay que releer todo tras cada corrección** — causa: la rama se reescribió sin mostrar lo cambiado. Corrección: usar `range-diff` o commits de corrección.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una comprobación automática detecta forma y no intención, y por eso no sustituye la lectura de los archivos de mayor riesgo. ([SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-195](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-195-ramas-integracion-rebase-y-conflictos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Revisión](../r/revision.md), [Verificación](../v/verificacion.md), [Pila de PR](../p/pila-de-pr.md), [Pull request](../p/pull-request.md), [Range-diff](../r/range-diff.md), [Triaje por riesgo](../t/triaje-por-riesgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-196 — Pull requests y revisión basada en riesgo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (37 clases más lo mencionan; las que más):

[SE-212](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-212-docs-as-code-revision-y-publicacion/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), [SE-101](../../../classes/part-08-entornos-herramientas-y-depuracion/se-101-repl-notebooks-y-desarrollo-exploratorio/README.md), [SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-258](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-258-interaccion-tactil-teclado-mouse-y-accesibilidad/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-442](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-442-calidad-de-experiencia-y-presupuestos/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Comprobaciones automáticas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Sadowski et al., «Modern code review: a case study at Google» (ICSE-SEIP, 2018)](https://doi.org/10.1145/3183519.3183525) — práctica de revisión en una organización grande; autoridad: ACM/IEEE ICSE-SEIP.
- [Bacchelli y Bird, «Expectations, outcomes, and challenges of modern code review» (ICSE, 2013)](https://doi.org/10.1109/ICSE.2013.6606617) — expectativas y dificultades de la revisión; autoridad: IEEE ICSE.
- [Google Engineering Practices: code review](https://google.github.io/eng-practices/review/) — guía de revisión y tamaño de cambios; autoridad: Google.
- [git-range-diff](https://git-scm.com/docs/git-range-diff) — comparación entre series de commits; autoridad: documentación de Git.
- [git-rebase](https://git-scm.com/docs/git-rebase) — `--update-refs`, `--onto` y `--autosquash`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Comprensión](./comprension.md) · [Comprobación de calidad →](./comprobacion-de-calidad.md)
