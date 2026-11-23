# Revisiones a ignorar

[↑ Glosario](../../README.md) · [← Revisión por pares](./revision-por-pares.md) · [Revisor de coherencia →](./revisor-de-coherencia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Lista de commits (normalmente reformateos) que `git blame` salta al atribuir líneas.

Definición de trabajo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Por qué importa

La clase donde se define, [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), existe con este propósito: la clase existe para que las reglas de colaboración (cómo se escribe un mensaje, quién responde por qué parte del código, quién debe revisar qué) sean explícitas, comprobables y auditables, y no un acuerdo tácito que solo conocen las personas que llevan tiempo en el equipo.

## Cómo funciona

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

`git blame` atribuye cada línea al último commit que la tocó. Un commit que solo reformatea (cambia sangría o comillas) se queda con la autoría de miles de líneas y oculta quién conoce de verdad el código. Git permite ignorar commits concretos con `--ignore-rev` o un archivo de revisiones a ignorar. La técnica funciona cuando el reformateo no cambia el sentido; si mezcla cambios de lógica, ignorarlo también oculta esa lógica.

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

En la plataforma, el archivo de propietarios tiene un comentario por regla con su motivo, una regla `*` al principio para que ninguna ruta quede sin dueño y reglas específicas al final. Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y falla si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe. Los mensajes se validan con un gancho y con integración continua, y un archivo de revisiones a ignorar lista los reformateos masivos con una explicación.

## Ejemplo

Ejemplo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sección «Ejemplo profesional»):

En la plataforma, el archivo de propietarios tiene un comentario por regla con su motivo, una regla `*` al principio para que ninguna ruta quede sin dueño y reglas específicas al final. Un trabajo de integración continua carga el archivo, lo evalúa sobre las rutas del repositorio y falla si hay una ruta sin propietario, una regla que nunca gana o un propietario que no existe. Los mensajes se validan con un gancho y con integración continua, y un archivo de revisiones a ignorar lista los reformateos masivos con una explicación.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El bot de formato figura como autor** — causa: su commit no se ignora en `blame`. Corrección: versionar la lista de revisiones a ignorar y configurar Git. ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- No hace falta ni conviene: el archivo de revisiones a ignorar corrige la atribución sin reescribir. ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cambio rompedor](../c/cambio-rompedor.md), [Convención de mensajes](../c/convencion-de-mensajes.md), [Propietario de código](../p/propietario-de-codigo.md), [Regla muerta](./regla-muerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

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

[↑ Glosario](../../README.md) · [← Revisión por pares](./revision-por-pares.md) · [Revisor de coherencia →](./revisor-de-coherencia.md)
