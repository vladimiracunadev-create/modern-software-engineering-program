# Cambio rompedor

[↑ Glosario](../../README.md) · [← Cambio mínimo](./cambio-minimo.md) · [Cambio ruidoso →](./cambio-ruidoso.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Un **cambio rompedor** (*breaking change*) es un cambio que puede romper a quien usa una interfaz, y que en Conventional Commits se marca con `!` tras el tipo o con el pie `BREAKING CHANGE:` ([SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)). El término combina dos cosas: la propiedad técnica (el cambio es incompatible para algún consumidor) y la marca que lo comunica.

## Por qué importa

Si una herramienta no lo ve, un consumidor se entera al romperse. La marca alimenta el número de versión (un cambio rompedor exige subir la versión mayor) y el registro de cambios que leen los consumidores. Sin marca, el versionado miente: se publica como menor o parche algo que rompe.

## Cómo funciona

Conventional Commits ofrece **dos marcas equivalentes**: un `!` después del tipo (`feat!: ...`) o un pie `BREAKING CHANGE:` con la descripción. [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) advierte de un fallo de herramienta: si la que genera versiones o registros solo lee una de las dos marcas, ignora la otra, y un cambio marcado con `!` no aparece en el registro si la herramienta lee solo el pie. La corrección es usar una herramienta que lea ambas o fijar una por convención.

Hay un segundo fallo, más profundo: **la marca la pone una persona**. Si no sabe que un cambio rompe a un consumidor, no la pone, y ninguna herramienta la añade por sí sola. Un validador de mensajes comprueba la forma (que haya tipo, que la marca esté bien escrita) pero no sabe si el tipo o la marca son correctos. La clase lo mide con una simulación: el 100 % de detección con ambas marcas supone que las personas las pusieron.

Por eso la marca se complementa con comprobaciones objetivas del contrato: un comprobador que compare el esquema o la API nueva con la anterior y falle si hay una ruptura sin la versión mayor correspondiente (como en la política de compatibilidad de la API de entregas). La marca comunica intención; la comparación de contratos verifica el hecho.

## Ejemplo

Un commit `feat(api)!: renombrar el campo nota a calificacion` marca la ruptura con `!`. Una herramienta que genera el registro de cambios y lee solo `BREAKING CHANGE:` no lo listará; el equipo lo descubre cuando un cliente se rompe. Con una herramienta que lea ambas marcas, el cambio aparece en la sección de rupturas y la versión sube a la siguiente mayor. (Ilustración construida sobre el mecanismo de [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).)

## Errores y confusiones comunes

- **El cambio rompedor no aparece en el registro**: se marcó con `!` y la herramienta lee solo el pie.
- **No marcar porque «es pequeño»**: lo pequeño puede romper a un cliente estricto.
- **Confiar en el validador de mensajes**: no sabe si la marca es correcta.
- **Confundir marca con compatibilidad real**: hay que comparar contratos.

## Límites y cuándo no aplica

Las categorías y proporciones de [SE-199](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) son del autor, no un muestreo de mensajes reales. La convención aplica a quien consume la interfaz con versionado: para código sin consumidores externos, la distinción pesa menos. La marca no sustituye el aviso previo y la ventana de retirada que merece una ruptura real.

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
