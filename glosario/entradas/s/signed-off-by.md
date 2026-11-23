# Signed-off-by

[↑ Glosario](../../README.md) · [← Sidecar](./sidecar.md) · [Significando →](./significando.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Línea de un commit con la que su autora afirma el origen del cambio según el Developer Certificate of Origin.

Definición de trabajo de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Por qué importa

La clase donde se define, [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), existe con este propósito: el proyecto existe para entregar una contribución que otra persona pueda revisar, probar, atribuir, licenciar y fusionar siguiendo enlaces y comandos, sin preguntar nada a quien la escribió.

## Cómo funciona

Según [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md):

Un paquete revisable contiene una rama con commits atómicos y firmados, una descripción con el motivo (el issue), los riesgos y cómo se probó, la declaración de licencia y de origen (`Signed-off-by`), pruebas que fallan sin el cambio y la petición a los propietarios afectados. Es lo que se entrega, no solo el código. Cada elemento responde a una clase de la parte y a una pregunta que alguien haría al revisar.

Según [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md):

La plataforma publica una guía de contribución con la lista de comprobaciones, el significado de cada umbral y quién decide si un umbral se relaja. Una contribución llega con una descripción que sigue la plantilla, commits atómicos y firmados, `Signed-off-by`, una referencia al issue y la petición de revisión al equipo dueño de `src/auth`. El validador se ejecuta en integración continua y comenta las alarmas; la mantenedora lee primero la prueba nueva y la regla de gracia, que la descripción marca como zona de atención.

## Ejemplo

Ejemplo de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) (sección «Ejemplo mínimo»):

Registra versión de Git y salida, y repite con un commit sin firmar y otro sin `Signed-off-by`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md)) son:

- **El validador pasa y el comportamiento es erróneo** — causa: una prueba vacía o débil. Corrección: añadir una mutación o una lectura humana de las pruebas.
- **Una rama tiene un commit que no compila** — causa: se empujó un intermedio roto. Corrección: reordenar la rama para que cada commit pase las pruebas.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un paquete revisable contiene una rama con commits atómicos y firmados, una descripción con el motivo (el issue), los riesgos y cómo se probó, la declaración de licencia y de origen (`Signed-off-by`), pruebas que fallan sin el cambio y la petición a los propietarios afectados. ([SE-204](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Comprobación de forma](../c/comprobacion-de-forma.md), [Contribución revisable](../c/contribucion-revisable.md), [Mutación](../m/mutacion.md), [Solape](./solape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Pro Git: Contributing to a Project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project) — preparación de contribuciones; autoridad: Pro Git.
- [Developer Certificate of Origin](https://developercertificate.org/) — declaración de origen de un cambio; autoridad: Linux Foundation.
- [REUSE specification](https://reuse.software/spec/) — licencia y titularidad por archivo; autoridad: REUSE.
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/) — formato de mensajes; autoridad: especificación de la convención.
- [git-commit](https://git-scm.com/docs/git-commit) — firma y `--signoff`; autoridad: documentación de Git.

---

[↑ Glosario](../../README.md) · [← Sidecar](./sidecar.md) · [Significando →](./significando.md)
