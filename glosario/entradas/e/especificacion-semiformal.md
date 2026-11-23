# Especificación semiformal

[↑ Glosario](../../README.md) · [← Especificación informal](./especificacion-informal.md) · [Especificidad →](./especificidad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción con estructura comprobable (tabla de decisión, plantilla con campos obligatorios, diagrama con reglas de construcción) cuyo contenido sigue escrito en lenguaje natural.

Definición de trabajo de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md).

## Por qué importa

En [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), el tema «Especificación semiformal» importa porque tablas, plantillas y diagramas con reglas de forma permiten comprobar completitud sin matemática avanzada.

## Cómo funciona

Según [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), en la sección «Especificación semiformal»:

Una tabla de decisión, una plantilla con campos obligatorios («Actor / Disparador / Resultado observable / Límite») o un diagrama de estados con reglas de construcción son semiformales: su forma se comprueba aunque su significado dependa de quien lee. La virtud práctica es la completitud: una tabla de condiciones puede revisarse en busca de combinaciones sin regla (huecos) o con dos reglas (solapes), algo que en prosa exige leer con atención y aun así se escapa. Su límite es que las celdas siguen escritas en lenguaje natural: «tarde con prórroga» puede significar cosas distintas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md):

La plataforma de entregas publica la regla de penalización en tres artefactos coordinados. La prosa vive en la política académica: una frase con los cuatro términos definidos (día, tope, base de cálculo, redondeo). La tabla de decisión vive en el documento de diseño y cubre estado de la entrega, prórroga y tramo de retraso. El predicado vive en una función de referencia con sus pruebas, y es contra esa función que se comparan la aplicación web, las exportaciones y el módulo de apelaciones.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)) son:

- **Dos sistemas dan notas distintas para la misma entrega y ambos «cumplen» la política** — causa: la frase admite varias lecturas y nadie ejecutó ninguna. Corrección: enumerar las lecturas, elegir una, y escribirla como predicado y como ejemplos de frontera.
- **Los ejemplos de la política son todos del camino típico y los defectos aparecen en el límite** — causa: se eligió el ejemplo más natural y no el que más separa lecturas. Corrección: añadir ejemplos en múltiplos de 24 horas, en el tope y en nota 0.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia académica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos de enumeración. No se midió a ningún equipo ni persona: las dieciséis lecturas y el defecto de frontera son construcciones del autor. La siguiente clase pregunta cómo los ejemplos con significado se convierten en la especificación que todos revisan.

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
