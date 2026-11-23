# Regla muerta

[↑ Glosario](../../README.md) · [← Regla mecanizable](./regla-mecanizable.md) · [Regla semántica →](./regla-semantica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Regla de propietarios que nunca gana porque otras, posteriores, cubren todo lo que ella cubre.

Definición de trabajo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md).

## Por qué importa

La clase donde se define, [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md), existe con este propósito: la clase existe para que las reglas de colaboración (cómo se escribe un mensaje, quién responde por qué parte del código, quién debe revisar qué) sean explícitas, comprobables y auditables, y no un acuerdo tácito que solo conocen las personas que llevan tiempo en el equipo.

## Cómo funciona

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

Compara el caso normal con un archivo editado a mano durante meses: la práctica es apropiada cuando las métricas de huecos y reglas muertas se revisan cada vez que cambia el archivo; es peligrosa cuando nadie sabe que reordenar dos líneas cambia a quién se pide revisión de 520 rutas.

Según [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md):

Traslada el análisis a otra asignación de responsabilidad por patrones (por ejemplo, reglas de enrutamiento de alertas o de etiquetado de recursos): decide qué sería la regla general, la específica y el orden, y cómo detectarías huecos y reglas muertas. La transferencia está lograda cuando puedes explicar qué parte de la evaluación dependía de «el último gana», no cuando las reglas se parecen.

## Ejemplo

Ejemplo de [SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md) (sección «Ejemplo profesional»):

Compara el caso normal con un archivo editado a mano durante meses: la práctica es apropiada cuando las métricas de huecos y reglas muertas se revisan cada vez que cambia el archivo; es peligrosa cuando nadie sabe que reordenar dos líneas cambia a quién se pide revisión de 520 rutas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son:

- **Un PR no pide revisión a quien debería** — causa: una regla posterior cubre la ruta. Corrección: poner lo específico después de lo general y probar rutas clave.
- **Hay rutas sin propietario** — causa: no hay regla `*` ni reglas para esa carpeta. Corrección: añadir una regla por defecto y revisar las métricas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-199 — Convenciones, ownership y CODEOWNERS](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-199-convenciones-ownership-y-codeowners/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con repositorios temporales y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. El modelo de coincidencia simplifica el de una plataforma, las rutas, equipos y mensajes son del autor y no se midió el efecto de ninguna convención en ningún equipo. La siguiente clase pregunta qué cambia cuando quien contribuye no pertenece al equipo y cómo se gobierna un proyecto abierto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-198](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-198-issues-discusiones-y-trazabilidad-del-cambio/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Propietario](../p/propietario.md), [Regla](./regla.md), [Cambio rompedor](../c/cambio-rompedor.md), [Convención de mensajes](../c/convencion-de-mensajes.md), [Propietario de código](../p/propietario-de-codigo.md), [Revisiones a ignorar](./revisiones-a-ignorar.md).
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

[↑ Glosario](../../README.md) · [← Regla mecanizable](./regla-mecanizable.md) · [Regla semántica →](./regla-semantica.md)
