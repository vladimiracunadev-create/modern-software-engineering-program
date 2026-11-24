# Convención de mensajes

[↑ Glosario](../../README.md) · [← Convalidación](./convalidacion.md) · [Convergencia →](./convergencia.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Una **convención de mensajes** es una forma común, legible por máquinas, para los mensajes de commit. Es el sentido de [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md). El ejemplo que cita es Conventional Commits: un tipo (`feat`, `fix`, `docs`…), un alcance opcional y una descripción. Es una convención de **forma**; no dice si el contenido del mensaje es verdadero ni si el tipo elegido es el correcto.

## Por qué importa

Cambia lo que se puede automatizar sobre el historial. Con una forma común, se generan registros de cambios, se decide el número de versión y se filtra el historial sin leerlo todo. [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) añade la condición que la vuelve útil: su valor depende de que se cumpla, y por eso se comprueba en un gancho local o en integración continua.

## Cómo funciona

El mensaje se descompone en campos con significado: el tipo indica la naturaleza del cambio, el alcance opcional su zona, y la descripción el resumen. Una herramienta puede leer los tipos para decidir, por ejemplo, que un `fix` sube el parche y un `feat` la versión menor, según la política del proyecto. Un comprobador valida la forma: si el mensaje no sigue el patrón, el commit o el PR se rechaza.

La limitación es que la comprobación es sintáctica. Un mensaje `feat: ajustes` es válido en forma y pobre en contenido; un `fix` que en realidad rompe compatibilidad pasa el comprobador. Por eso la convención se complementa con revisión humana y, dentro de las doce comprobaciones de forma de [SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), con la regla de que los commits sean atómicos.

## Ejemplo

El repositorio de la plataforma de entregas es el caso conductor de la [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md). [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) deja allí el archivo de propietarios (`CODEOWNERS`), la convención de mensajes y la lista de revisiones a ignorar. [SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md) abre el proyecto a contribuciones externas y necesita estas reglas para recibirlas, y [SE-202](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-202-firmas-procedencia-y-proteccion-del-repositorio/README.md) protege la rama con ellas. Un commit del proyecto tendría la forma `fix(entregas): corrige el tope de penalización`, que una herramienta clasifica como corrección.

## Errores y confusiones comunes

- **Creer que la convención garantiza buenos mensajes.** Solo garantiza la forma.
- **Elegir el tipo por costumbre.** Un tipo equivocado produce un registro de cambios y una versión equivocados.
- **No comprobarla.** Sin gancho ni integración continua se erosiona commit a commit.
- **Confundirla con `CODEOWNERS`.** Aquella regula la forma del mensaje; esta, quién revisa qué rutas. En `CODEOWNERS`, una regla posterior cubre a una anterior: lo específico va después de lo general.

## Límites y cuándo no aplica

En un proyecto personal pequeño, el costo de imponerla puede superar su beneficio. Con una herramienta de versionado que no lee los tipos, la convención es solo una costumbre de estilo. Los experimentos de [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) usan repositorios temporales y un modelo de coincidencia simplificado respecto al de una plataforma real, con rutas, equipos y mensajes del autor.

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
