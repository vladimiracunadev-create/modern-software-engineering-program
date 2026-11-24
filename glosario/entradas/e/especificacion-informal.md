# Especificación informal

[↑ Glosario](../../README.md) · [← Especificación formal](./especificacion-formal.md) · [Especificación semiformal →](./especificacion-semiformal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **especificación informal** es una descripción en lenguaje natural sin reglas de forma que permitan decidir mecánicamente si dos lecturas coinciden. Es el primer nivel de la escala de [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (informal, semiformal, formal). Su rasgo no es la falta de rigor del autor sino la ausencia de un procedimiento para comparar lecturas.

## Por qué importa

Cambia dónde se invierte esfuerzo de precisión. La prosa es barata y legible para todos, y es la que más lecturas admite. Un texto que dos personas leen distinto produce dos implementaciones que ambas «cumplen» la política y dan resultados diferentes. Saber que la prosa tiene este límite lleva a reforzar solo los puntos donde la ambigüedad cuesta.

## Cómo funciona

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) describe la prosa como el nivel donde empieza todo y donde casi todo se queda. Su fortaleza es que cualquiera la lee, la discute y la corrige; su debilidad, que no tiene un procedimiento para decidir si dos lecturas son la misma. Una especificación informal **bien hecha** hace tres cosas: declara sus términos («día» significa bloque de 24 horas desde el plazo), nombra sus casos límite y trae ejemplos con valores.

No se vuelve semiformal por usar viñetas: se vuelve semiformal cuando una regla de forma permite comprobar mecánicamente algo del texto, por ejemplo que cada requisito tenga identificador y criterio. Y se vuelve formal cuando admite un procedimiento de decisión sobre su significado. La clase recomienda, para una frase ambigua, enumerar las lecturas posibles, elegir una y escribirla como predicado y como ejemplos de frontera.

## Ejemplo

En [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), la política de penalización por entrega tardía admite varias lecturas: ¿un retraso de 25 horas son uno o dos días? Dos sistemas dan notas distintas para la misma entrega y ambos cumplen la frase. La corrección es declarar «día» como bloque de 24 horas, añadir ejemplos en múltiplos de 24 horas, en el tope y con nota 0, que son los puntos que más separan lecturas.

## Errores y confusiones comunes

- **Dos sistemas, notas distintas y ambos «cumplen».** La frase admite varias lecturas y nadie ejecutó ninguna; enumerar lecturas, elegir una, escribirla como predicado y ejemplos.
- **Ejemplos solo del camino típico.** Los defectos aparecen en el límite; añadir ejemplos en las fronteras.
- **Creer que informal significa mala.** Puede estar bien hecha.
- **Confundir viñetas con formalidad.** El formato no agrega decidibilidad.

## Límites y cuándo no aplica

Para reglas críticas o numéricas, la prosa sola es insuficiente: conviene un nivel superior (semiformal o formal) o ejemplos ejecutables. Para exploración inicial, en cambio, forzar formalidad temprana frena la conversación. La clase no afirma que haya un nivel correcto universal: el nivel se elige por el costo de una lectura equivocada.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Ambigüedad](../a/ambiguedad.md), [Especificación formal](./especificacion-formal.md), [Especificación semiformal](./especificacion-semiformal.md), [Mutante equivalente](../m/mutante-equivalente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md), [SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Meyer, «On formalism in specifications» (IEEE Software, 1985)](https://doi.org/10.1109/MS.1985.229776) — los defectos de las especificaciones en lenguaje natural y la progresión hacia la formalidad; autoridad: IEEE Software.
- [Hall, «Seven myths of formal methods» (IEEE Software, 1990)](https://doi.org/10.1109/52.57887) — qué aportan y qué no aportan los métodos formales; autoridad: IEEE Software.
- [Newcombe et al., «How Amazon Web Services uses formal methods» (CACM, 2015)](https://doi.org/10.1145/2699417) — experiencia industrial de especificación formal para hallar defectos de diseño; autoridad: Communications of the ACM.
- [Woodcock et al., «Formal methods: practice and experience» (ACM Computing Surveys, 2009)](https://doi.org/10.1145/1592434.1592436) — estudio de uso industrial de métodos formales y de su coste; autoridad: ACM Computing Surveys.
- [Lamport, «Who builds a house without drawing blueprints?» (CACM, 2015)](https://doi.org/10.1145/2736348) — argumento a favor de especificar antes de codificar; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Especificación formal](./especificacion-formal.md) · [Especificación semiformal →](./especificacion-semiformal.md)
