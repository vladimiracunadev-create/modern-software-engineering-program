# Especificación formal

[↑ Glosario](../../README.md) · [← Especificación del experimento](./especificacion-del-experimento.md) · [Especificación informal →](./especificacion-informal.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción en una notación con semántica definida, ejecutable o comprobable por una herramienta, en un dominio acotado o con una demostración.

Definición de trabajo de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md).

## Por qué importa

En [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), el tema «Especificación formal» importa porque un predicado sin ambigüedad se comprueba mecánicamente en un dominio acotado, a cambio de esfuerzo y de leerse con dificultad.

## Cómo funciona

Según [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), en la sección «Especificación formal»:

Un predicado como `nota_final(n, h) = redondear(n · (1 − min(0,10 · ⌈h/24⌉, 0,50)))` para `h > 0` no admite lecturas: fija el redondeo, el tope y el cálculo del número de días. Su valor es que se ejecuta: el predicado se transforma en una función de referencia con la que comparar cualquier implementación en todo un dominio acotado. El coste es doble: escribirlo exige acordar antes todos los puntos abiertos, y leerlo exige formación. Hall recuerda que formal no es sinónimo de correcto: la especificación puede describir con exactitud algo que nadie quería.

## Ejemplo

Ejemplo de [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) (sección «Preguntas frecuentes»):

No: la especificación formal da la referencia contra la que se prueba y permite comprobar todo un dominio acotado, pero hay que ejecutar esa comparación contra la implementación. Y no protege de especificar lo que nadie quería: el predicado de la clase es exacto y podría ser el equivocado.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)) son:

- **Dos sistemas dan notas distintas para la misma entrega y ambos «cumplen» la política** — causa: la frase admite varias lecturas y nadie ejecutó ninguna. Corrección: enumerar las lecturas, elegir una, y escribirla como predicado y como ejemplos de frontera.
- **Los ejemplos de la política son todos del camino típico y los defectos aparecen en el límite** — causa: se eligió el ejemplo más natural y no el que más separa lecturas. Corrección: añadir ejemplos en múltiplos de 24 horas, en el tope y en nota 0.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia académica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos salvo los tiempos de enumeración. No se midió a ningún equipo ni persona: las dieciséis lecturas y el defecto de frontera son construcciones del autor. La siguiente clase pregunta cómo los ejemplos con significado se convierten en la especificación que todos revisan.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-156](../../../classes/part-12-ingenieria-de-requisitos/se-156-proyecto-especificacion-de-requisitos-revisable/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dominio](../d/dominio.md), [Herramientas](../h/herramientas.md), [Semántica](../s/semantica.md), [Ambigüedad](../a/ambiguedad.md), [Especificación informal](./especificacion-informal.md), [Especificación semiformal](./especificacion-semiformal.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-157 — Especificación informal, semiformal y formal](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Newcombe et al., «How Amazon Web Services uses formal methods» (CACM, 2015)](https://doi.org/10.1145/2699417) — experiencia industrial de especificación formal para hallar defectos de diseño; autoridad: Communications of the ACM.
- [Meyer, «On formalism in specifications» (IEEE Software, 1985)](https://doi.org/10.1109/MS.1985.229776) — los defectos de las especificaciones en lenguaje natural y la progresión hacia la formalidad; autoridad: IEEE Software.
- [Hall, «Seven myths of formal methods» (IEEE Software, 1990)](https://doi.org/10.1109/52.57887) — qué aportan y qué no aportan los métodos formales; autoridad: IEEE Software.
- [Woodcock et al., «Formal methods: practice and experience» (ACM Computing Surveys, 2009)](https://doi.org/10.1145/1592434.1592436) — estudio de uso industrial de métodos formales y de su coste; autoridad: ACM Computing Surveys.
- [Lamport, «Who builds a house without drawing blueprints?» (CACM, 2015)](https://doi.org/10.1145/2736348) — argumento a favor de especificar antes de codificar; autoridad: Communications of the ACM.

---

[↑ Glosario](../../README.md) · [← Especificación del experimento](./especificacion-del-experimento.md) · [Especificación informal →](./especificacion-informal.md)
