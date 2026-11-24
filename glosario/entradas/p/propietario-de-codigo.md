# Propietario de código

[↑ Glosario](../../README.md) · [← Propietario](./propietario.md) · [Propietario de un campo →](./propietario-de-un-campo.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Un **propietario de código** es la persona o el equipo responsable de una ruta del repositorio y a quien se pide revisión cuando cambia ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)). Se declara en un archivo `CODEOWNERS` que asocia patrones de ruta con personas o equipos. No debe confundirse con el propietario de un campo de datos ni con la propiedad de archivos en el sentido de permisos del sistema operativo.

## Por qué importa

Decide quién debe ver cada cambio. Sin propietarios declarados, la revisión depende de quién esté disponible o de quién se acuerde; un hueco deja un cambio sin revisión con dueño. Cambia el flujo de revisión: la plataforma pide revisión a la persona correcta de forma automática.

## Cómo funciona

Un archivo CODEOWNERS contiene reglas de la forma «patrón de ruta → propietarios». Cuando un pull request toca una ruta, la plataforma **pide revisión** a los propietarios correspondientes y, si la **protección de rama** lo exige, **requiere su aprobación** antes de fusionar. [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) subraya que un propietario es **una responsabilidad, no un privilegio**: debe ser alguien que pueda revisar y que exista (una cuenta o equipo real, activo).

Dos propiedades del archivo causan fallos clásicos. Primera, **el orden importa**: cuando varias reglas coinciden con una ruta, gana la última, de modo que lo específico va después de lo general. Si una regla posterior más amplia cubre la ruta, el PR no pide revisión a quien debería. Segunda, **las rutas sin regla no tienen propietario**: la solución es una regla `*` al principio que asigne un propietario por defecto, de modo que ninguna ruta quede sin dueño.

En la plataforma de entregas, el archivo tiene un comentario por regla con su motivo, la regla `*` al comienzo y reglas específicas al final (por ejemplo, el equipo dueño de `migraciones/` revisa siempre las migraciones). Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y **falla** si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe. Así el archivo deja de ser documentación y se comprueba.

## Ejemplo

```text
# propietario por defecto
*                 @equipo-plataforma
# las migraciones las revisa quien mantiene los datos
migraciones/      @equipo-datos
# la regla de penalización exige una segunda mirada
src/penal.py      @coordinacion-academica
```

Un PR que toca `migraciones/0007.sql` pide revisión a `@equipo-datos`; uno que toca `README.md` cae en la regla `*`. (Sintaxis estándar de CODEOWNERS; nombres ilustrativos.)

## Errores y confusiones comunes

- **Un PR no pide revisión a quien debería**: una regla posterior cubre la ruta; corrección: lo específico después de lo general y probar rutas clave.
- **Rutas sin propietario**: falta la regla `*`.
- **Propietarios que ya no existen** o están de baja.
- **Confundirlo con un privilegio de bloqueo** en vez de una responsabilidad.

## Límites y cuándo no aplica

[SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) declara que su modelo de coincidencia simplifica el de una plataforma real y que las rutas y equipos son del autor. Si hay un único propietario para todo, el archivo no aporta. Con muy poca gente, exigir aprobación de propietarios puede bloquear el flujo; se combina con relevos y con un indicador de cuántas personas conocen cada ruta.

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
