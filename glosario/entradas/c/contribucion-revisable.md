# Contribución revisable

[↑ Glosario](../../README.md) · [← Contrato y corpus de comparación](./contrato-y-corpus-de-comparacion.md) · [Contribución única →](./contribucion-unica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md)

## Definición

Conjunto de cambios, descripción, pruebas y declaraciones que otra persona puede revisar y fusionar sin preguntar al autor.

Definición de trabajo de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md).

## Por qué importa

La clase donde se define, [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md), existe con este propósito: el proyecto existe para entregar una contribución que otra persona pueda revisar, probar, atribuir, licenciar y fusionar siguiendo enlaces y comandos, sin preguntar nada a quien la escribió.

## Cómo funciona

[SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md):

La plataforma publica una guía de contribución con la lista de comprobaciones, el significado de cada umbral y quién decide si un umbral se relaja. Una contribución llega con una descripción que sigue la plantilla, commits atómicos y firmados, `Signed-off-by`, una referencia al issue y la petición de revisión al equipo dueño de `src/auth`. El validador se ejecuta en integración continua y comenta las alarmas; la mantenedora lee primero la prueba nueva y la regla de gracia, que la descripción marca como zona de atención.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md)) son:

- **El validador pasa y el comportamiento es erróneo** — causa: una prueba vacía o débil. Corrección: añadir una mutación o una lectura humana de las pruebas.
- **Una rama tiene un commit que no compila** — causa: se empujó un intermedio roto. Corrección: reordenar la rama para que cada commit pase las pruebas.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutó un experimento con repositorios temporales, claves desechables y defectos plantados por el autor en Windows y Ubuntu (WSL2) con resultados idénticos. Las doce comprobaciones se ajustaron a los trece defectos, los umbrales son arbitrarios y no se probó ningún alojamiento, protección de rama ni revisor humano. La [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md) pregunta cómo se documenta lo que esta contribución declara.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-193](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-193-modelo-de-objetos-y-areas-de-git/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](./conjunto.md), [Comprobación de forma](./comprobacion-de-forma.md), [Mutación](../m/mutacion.md), [Signed-off-by](../s/signed-off-by.md), [Solape](../s/solape.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-204 — Proyecto: contribución revisable de extremo a extremo](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-204-proyecto-contribucion-revisable-de-extremo-a-extremo/README.md) — [Parte 16](../../../classes/part-16-git-colaboracion-y-codigo-abierto/README.md), Git, colaboración y código abierto.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-205](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-205-documentacion-orientada-a-tareas-y-audiencias/README.md), [SE-203](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-203-taller-rescatar-una-integracion-conflictiva/README.md).

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

[↑ Glosario](../../README.md) · [← Contrato y corpus de comparación](./contrato-y-corpus-de-comparacion.md) · [Contribución única →](./contribucion-unica.md)
