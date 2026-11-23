# Propietario de código

[↑ Glosario](../../README.md) · [← Propietario](./propietario.md) · [Propietario de un campo →](./propietario-de-un-campo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Persona o equipo responsable de una ruta y a quien se pide revisión cuando cambia.

Definición de trabajo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Por qué importa

En [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), el tema «Propietarios de código» importa porque deciden quién debe ver cada cambio; un hueco deja un cambio sin revisión con dueño.

## Cómo funciona

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), en la sección «Propietarios de código»:

Un archivo CODEOWNERS asocia patrones de ruta con personas o equipos. Cuando un PR toca una ruta, la plataforma pide revisión a los propietarios y, si la protección de rama lo exige, requiere su aprobación. Un propietario es una responsabilidad, no un privilegio: debe ser alguien que pueda revisar y que exista. Una ruta sin propietario es un cambio sin responsable, y la regla `*` al principio cubre ese riesgo a cambio de que todo caiga en el mismo equipo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

En la plataforma, el archivo de propietarios tiene un comentario por regla con su motivo, una regla `*` al principio para que ninguna ruta quede sin dueño y reglas específicas al final. Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y falla si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son:

- **Un PR no pide revisión a quien debería** — causa: una regla posterior cubre la ruta. Corrección: poner lo específico después de lo general y probar rutas clave.
- **Hay rutas sin propietario** — causa: no hay regla `*` ni reglas para esa carpeta. Corrección: añadir una regla por defecto y revisar las métricas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El modelo de coincidencia simplifica el de una plataforma, las rutas, equipos y mensajes son del autor y no se midió el efecto de ninguna convención en ningún equipo. La siguiente clase pregunta qué cambia cuando quien contribuye no pertenece al equipo y cómo se gobierna un proyecto abierto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Revisión](../r/revision.md), [Ruta](../r/ruta.md), [Cambio rompedor](../c/cambio-rompedor.md), [Convención de mensajes](../c/convencion-de-mensajes.md), [Regla muerta](../r/regla-muerta.md), [Revisiones a ignorar](../r/revisiones-a-ignorar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-196](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-196-pull-requests-y-revision-basada-en-riesgo/README.md), [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md), [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Propietarios de código».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: acerca de los propietarios de código](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — sintaxis, precedencia y protección de rama; autoridad: GitHub Docs.
- [gitignore](https://git-scm.com/docs/gitignore) — formato de patrones del que parte la sintaxis de CODEOWNERS; autoridad: documentación de Git.
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — especificación de la convención; autoridad: especificación de la convención.
- [git-blame](https://git-scm.com/docs/git-blame) — atribución e `--ignore-rev`; autoridad: documentación de Git.
- [Semantic Versioning 2.0.0](https://semver.org/) — relación entre cambios rompedores y versión mayor; autoridad: especificación de SemVer.

---

[↑ Glosario](../../README.md) · [← Propietario](./propietario.md) · [Propietario de un campo →](./propietario-de-un-campo.md)
