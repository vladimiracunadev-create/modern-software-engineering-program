# Especificación semiformal

[↑ Glosario](../../README.md) · [← Especificación informal](./especificacion-informal.md) · [Especificidad →](./especificidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **especificación semiformal** es una descripción con estructura comprobable (una tabla de decisión, una plantilla con campos obligatorios, un diagrama con reglas de construcción) cuyo contenido sigue escrito en lenguaje natural ([SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)). Ocupa el escalón intermedio entre la informal (prosa) y la formal (notación con semántica definida).

## Por qué importa

Permite comprobar completitud sin matemática avanzada. Tablas, plantillas y diagramas con reglas de forma muestran huecos y solapes que la prosa oculta, con un costo de adopción mucho menor que el de una notación formal. Cambia lo que se puede revisar de forma mecánica antes de escribir una línea de código.

## Cómo funciona

El criterio que separa lo semiformal de lo informal es que una **regla de forma** permite comprobar algo mecánicamente. No basta con usar viñetas: una lista de viñetas sigue siendo prosa si nada obliga a que cada elemento tenga las mismas partes.

[SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) da tres formas:

- una **tabla de decisión**, que enumera combinaciones de condiciones;
- una **plantilla con campos obligatorios** («Actor / Disparador / Resultado observable / Límite»);
- un **diagrama de estados** con reglas de construcción.

Su forma se comprueba aunque su significado dependa de quien lee. La virtud práctica es la **completitud**: una tabla de condiciones puede revisarse en busca de **combinaciones sin regla (huecos)** o **con dos reglas (solapes)**, algo que en prosa exige leer con mucha atención. Una plantilla puede validarse con un programa (¿tiene cada requisito los cuatro campos?). Lo que no resuelve es el significado: cada celda sigue siendo una frase que alguien puede leer distinto.

En la plataforma de entregas, la regla de penalización se publica en tres artefactos coordinados: la prosa en la política académica (una frase con cuatro términos definidos: día, tope, base de cálculo y redondeo); la **tabla de decisión** en el documento de diseño, que cubre estado de la entrega, prórroga y tramo de retraso; y el predicado en una función de referencia con sus pruebas. La tabla es el artefacto semiformal.

## Ejemplo

Tabla con columnas «estado de la entrega» (a tiempo, tardía), «prórroga» (sí, no) y «acción»: cuatro combinaciones; se comprueba que cada una tenga exactamente una acción. Una plantilla de requisito con campos «Actor, Disparador, Resultado observable, Límite» se valida por programa: si falta el «Límite», falla con el identificador del requisito. (Ilustración de las formas descritas por [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md).)

## Errores y confusiones comunes

- **Creer que viñetas o tablas bastan** sin una regla de forma que se compruebe.
- **Dos sistemas con notas distintas y ambos «cumplen»**: la frase admite varias lecturas.
- **Ejemplos solo del camino típico**: los defectos aparecen en el límite.
- **Confundir completitud de forma con corrección de fondo.**

## Límites y cuándo no aplica

La semiformalidad comprueba estructura, no significado; una tabla completa puede ser errónea. Para reglas de muy alto riesgo puede quedarse corta y convenir una especificación formal. Con muchas condiciones, la tabla crece de forma exponencial y se vuelve inmanejable.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tablas de decisión](../t/tablas-de-decision.md), [Diagrama](../d/diagrama.md), [Estructura](./estructura.md), [Regla](../r/regla.md), [Ambigüedad](../a/ambiguedad.md), [Especificación formal](./especificacion-formal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

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

[↑ Glosario](../../README.md) · [← Especificación informal](./especificacion-informal.md) · [Especificidad →](./especificidad.md)
