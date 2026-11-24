# Comprobación automática

[↑ Glosario](../../README.md) · [← Comprensión](./comprension.md) · [Comprobación de calidad →](./comprobacion-de-calidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Una **comprobación automática** es una verificación ejecutada por una máquina antes o durante la revisión humana ([SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md)). Incluye compilación, pruebas, análisis estático, formato, licencias y búsqueda de secretos. Se distingue de la revisión humana, que juzga el sentido del cambio.

## Por qué importa

Libera a la persona de lo que una máquina comprueba y deja para ella el sentido: ¿es esta la regla correcta?, ¿se probó el caso límite? Una revisora que gasta su atención en señalar un espacio de más tiene menos para detectar una regla mal aplicada. Cambia el orden del proceso: las comprobaciones se ejecutan **antes** de pedir revisión humana.

## Cómo funciona

El flujo de integración continua ejecuta las comprobaciones sobre cada cambio y devuelve un resultado objetivo. [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md) las ubica antes de la asignación de revisora: formato, pruebas, análisis estático y búsqueda de secretos. Si alguna falla, el autor corrige sin consumir tiempo ajeno.

Su virtud es la repetibilidad: la máquina aplica la misma regla a todos los cambios, sin cansarse ni preferencias. Su límite es el que la clase destaca: **detecta forma y no intención**. Una comprobación puede asegurar que el código compila, que el formato es el acordado o que no hay secretos, pero no sabe si la regla de negocio está bien, si faltan casos o si la prueba verifica algo. Por eso no sustituye la lectura de los archivos de mayor riesgo.

Las comprobaciones se combinan con el triaje por riesgo (qué leer primero) y con las comprobaciones de forma de un paquete (mensajes convencionales, commits atómicos, tamaño del PR): lo mecánico se automatiza; lo que exige juicio queda para la persona. Una comprobación que nadie hace cumplir se degrada en pocas semanas, por eso se ejecutan como requisito de integración y no como recomendación.

En la plataforma de entregas, el CODEOWNERS añade como revisor obligatorio al equipo dueño de las migraciones cuando un PR toca `migraciones/`; es una comprobación automática de que la revisión correcta ocurre.

## Ejemplo

Un PR cambia la fórmula de penalización. Las comprobaciones automáticas pasan: compila, las pruebas existentes pasan, el análisis estático no encuentra alertas y no hay secretos. Pero la regla de negocio nueva redondea mal en el empate y ninguna prueba cubre ese caso: lo detecta la revisora al leer el cambio, no la máquina. (Ilustración del límite que enseña [SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md).)

## Errores y confusiones comunes

- **Comentarios de estilo y defectos que se escapan**: se revisa a mano lo que una máquina haría; corrección: automatizar el estilo.
- **Creer que verde significa correcto.**
- **Comprobaciones lentas o inestables** que la gente aprende a ignorar.
- **Ejecutarlas después de la revisión**: la persona revisa un cambio que luego debe cambiar.

## Límites y cuándo no aplica

No detectan lo que no se escribió como regla ni la intención del cambio. En proyectos muy pequeños, mantenerlas cuesta más que el beneficio. Un conjunto de comprobaciones muy amplio puede dar falsa confianza si las pruebas son débiles.

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
