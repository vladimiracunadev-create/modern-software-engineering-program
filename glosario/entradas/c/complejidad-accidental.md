# Complejidad accidental

[↑ Glosario](../../README.md) · [← Complejidad](./complejidad.md) · [Complejidad ciclomática →](./complejidad-ciclomatica.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

La **complejidad accidental** es la que introduce la solución elegida y puede reducirse con otra forma de resolver lo mismo ([SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)). Frente a la esencial, que viene del problema, esta viene de cómo se escribió el programa. La distinción es de Brooks, que la usó para decir que las herramientas pueden atacar la primera clase de complejidad y no la segunda.

## Por qué importa

Cuando un código es difícil, la pregunta útil es si la dificultad viene del problema o de la forma de la solución. Si viene de la forma, hay trabajo que se puede quitar sin cambiar lo que el sistema hace; si viene del problema, intentar quitarla rompe reglas del negocio. La decisión que cambia es dónde se invierte el esfuerzo de simplificar y dónde se debe respetar la complejidad.

## Cómo funciona

[SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) enumera sus fuentes típicas: estado mutable que hay que seguir, banderas que interactúan, anidamiento que repite casos, capas sin razón y nombres que obligan a traducir. Se reconoce con una prueba concreta: **el mismo comportamiento se puede escribir con menos partes que interactúan**. Si al simplificar el comportamiento observable es idéntico, lo eliminado era accidental.

Se reduce **cambiando la forma**, y siempre con una red de pruebas ([SE-307](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-307-refactorizacion-segura-apoyada-por-pruebas/README.md)) que garantice que el comportamiento no cambió. El ejemplo de la clase es una función de tarifas con cuatro zonas, tres bandas de peso y tres opciones: 96 casos. Escrita con un camino de código por caso, tiene 96 caminos; pasando los casos a una tabla y una regla común, el comportamiento es el mismo con mucho menos código que interactúa. Los 96 casos siguen existiendo (eso es complejidad esencial); lo que desaparece es la repetición.

## Ejemplo

Una función de `tarifas` anidada con un `if` por cada combinación de zona, banda y opción acumula 96 ramas. Se reescribe como una tabla de tarifas base más una regla de recargos. La complejidad ciclomática baja y los 96 resultados son idénticos, comprobados con una prueba que recorre todos los casos. Es el análisis con datos sintéticos que describe [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

## Errores y confusiones comunes

- **Una función con 96 caminos de código para 96 casos**: cada caso tiene su propio código; se corrige pasando los casos a una tabla y una regla común.
- **Se reduce la complejidad y se pierde una regla**: se simplificó sin la lista de casos del negocio; se corrige escribiendo los casos antes y comprobando la equivalencia.
- **Llamar accidental a lo que es del negocio**: simplificar una regla real es cambiar el sistema.
- **Simplificar sin pruebas**: no hay forma de saber si el comportamiento se conservó.

## Límites y cuándo no aplica

La frontera entre accidental y esencial no es automática: depende de qué se considere «el problema», y dos personas pueden clasificar distinto. [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) advierte que sus definiciones son operativas para `tarifas` y que sus análisis usan código de ejemplo con datos sintéticos; no se midió ningún proyecto real ni se validó la complejidad cognitiva con personas. Reducir la complejidad accidental tiene costo (tiempo, riesgo de regresión), y la clase siguiente pone precio a la que se decide no reducir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Cobertura por pares](./cobertura-por-pares.md), [Complejidad ciclomática](./complejidad-ciclomatica.md), [Complejidad cognitiva](./complejidad-cognitiva.md), [Complejidad esencial](./complejidad-esencial.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Moseley y Marks, «Out of the Tar Pit» (2006)](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — estado y complejidad accidental; autoridad: sus autores.
- [Brooks, «No Silver Bullet» (IEEE Computer, 1987)](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer.
- [McCabe, «A Complexity Measure» (IEEE TSE, 1976)](https://doi.org/10.1109/TSE.1976.233837) — complejidad ciclomática; autoridad: IEEE Transactions on Software Engineering.
- [Campbell, «Cognitive Complexity» (SonarSource)](https://www.sonarsource.com/docs/CognitiveComplexity.pdf) — medida cognitiva; autoridad: SonarSource.
- [Kuhn, Wallace y Gallo, «Software fault interactions and implications for software testing» (IEEE TSE, 2004)](https://doi.org/10.1109/TSE.2004.24) — interacciones de pocas variables en los fallos; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Complejidad](./complejidad.md) · [Complejidad ciclomática →](./complejidad-ciclomatica.md)
