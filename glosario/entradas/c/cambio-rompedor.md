# Cambio rompedor

[↑ Glosario](../../README.md) · [← Cambio mínimo](./cambio-minimo.md) · [Cambio ruidoso →](./cambio-ruidoso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Cambio que puede romper a quien usa una interfaz y se marca con `!` o con el pie `BREAKING CHANGE`.

Definición de trabajo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Por qué importa

En [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), el tema «Cambios rompedores» importa porque si una herramienta no los ve, un consumidor se entera al romperse.

## Cómo funciona

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), en la sección «Cambios rompedores»:

Conventional Commits marca un cambio rompedor con un `!` tras el tipo o con un pie `BREAKING CHANGE:`. Si la herramienta que genera versiones o registros solo lee una de las dos marcas, ignora la otra. La marca la pone una persona: si no sabe que un cambio rompe a un consumidor, no la pone, y ninguna herramienta la añade por sí sola.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

En la plataforma, el archivo de propietarios tiene un comentario por regla con su motivo, una regla `*` al principio para que ninguna ruta quede sin dueño y reglas específicas al final. Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y falla si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cambio rompedor no aparece en el registro** — causa: se marcó con `!` y la herramienta lee solo el pie. Corrección: usar una herramienta que lea ambas marcas o fijar una. ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** las categorías y proporciones son del autor, no un muestreo de mensajes reales, y un validador que acepta el mensaje no sabe si el tipo o la marca de cambio rompedor son correctos; el 100 % de detección con ambas marcas supone que las personas las pusieron. ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Convención de mensajes](./convencion-de-mensajes.md), [Propietario de código](../p/propietario-de-codigo.md), [Regla muerta](../r/regla-muerta.md), [Revisiones a ignorar](../r/revisiones-a-ignorar.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Cambios rompedores».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Semantic Versioning 2.0.0](https://semver.org/) — relación entre cambios rompedores y versión mayor; autoridad: especificación de SemVer.
- [GitHub: acerca de los propietarios de código](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) — sintaxis, precedencia y protección de rama; autoridad: GitHub Docs.
- [gitignore](https://git-scm.com/docs/gitignore) — formato de patrones del que parte la sintaxis de CODEOWNERS; autoridad: documentación de Git.
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — especificación de la convención; autoridad: especificación de la convención.
- [git-blame](https://git-scm.com/docs/git-blame) — atribución e `--ignore-rev`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Cambio mínimo](./cambio-minimo.md) · [Cambio ruidoso →](./cambio-ruidoso.md)
