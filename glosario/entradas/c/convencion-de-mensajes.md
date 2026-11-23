# Convención de mensajes

[↑ Glosario](../../README.md) · [← Convalidación](./convalidacion.md) · [Convergencia →](./convergencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Forma común de los mensajes de commit legible por máquinas.

Definición de trabajo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Por qué importa

En [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), el tema «Convención de mensajes» importa porque alimenta registros de cambios y versionado; una forma común se comprueba.

## Cómo funciona

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), en la sección «Convención de mensajes»:

Una convención como Conventional Commits fija una forma legible por máquinas: un tipo (`feat`, `fix`, `docs`…), un alcance opcional y una descripción. Sirve para generar registros de cambios, decidir el número de versión y filtrar el historial. Su valor depende de que se cumpla, y por eso se comprueba en un gancho local o en integración continua. Es una convención de forma: no sabe si el tipo es el correcto.

## Ejemplo

Ejemplo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sección «Caso conductor»):

El repositorio de la plataforma de entregas es el caso conductor de la [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md). Esta clase deja el archivo de propietarios, la convención de mensajes y la lista de revisiones a ignorar. `SE-200` abre el proyecto a contribuciones externas y necesita estas reglas para recibirlas y `SE-202` protege la rama con ellas. Cambia después un solo dato, el orden de dos reglas, y revisa qué rutas cambian de propietario.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son:

- **Un PR no pide revisión a quien debería** — causa: una regla posterior cubre la ruta. Corrección: poner lo específico después de lo general y probar rutas clave.
- **Hay rutas sin propietario** — causa: no hay regla `*` ni reglas para esa carpeta. Corrección: añadir una regla por defecto y revisar las métricas.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El modelo de coincidencia simplifica el de una plataforma, las rutas, equipos y mensajes son del autor y no se midió el efecto de ninguna convención en ningún equipo. La siguiente clase pregunta qué cambia cuando quien contribuye no pertenece al equipo y cómo se gobierna un proyecto abierto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio rompedor](./cambio-rompedor.md), [Propietario de código](../p/propietario-de-codigo.md), [Regla muerta](../r/regla-muerta.md), [Revisiones a ignorar](../r/revisiones-a-ignorar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md), [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GitHub: acerca de los propietarios de código](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — sintaxis, precedencia y protección de rama; autoridad: GitHub Docs.
- [gitignore](https://git-scm.com/docs/gitignore) — formato de patrones del que parte la sintaxis de CODEOWNERS; autoridad: documentación de Git.
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — especificación de la convención; autoridad: especificación de la convención.
- [git-blame](https://git-scm.com/docs/git-blame) — atribución e `--ignore-rev`; autoridad: documentación de Git.
- [Semantic Versioning 2.0.0](https://semver.org/) — relación entre cambios rompedores y versión mayor; autoridad: especificación de SemVer.

---

[↑ Glosario](../../README.md) · [← Convalidación](./convalidacion.md) · [Convergencia →](./convergencia.md)
