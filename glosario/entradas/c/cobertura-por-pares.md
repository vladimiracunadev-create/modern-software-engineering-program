# Cobertura por pares

[↑ Glosario](../../README.md) · [← Cobertura estructural](./cobertura-estructural.md) · [Code unit →](./code-unit.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Conjunto de pruebas en que cada combinación de valores de cada pareja de opciones aparece al menos una vez.

Definición de trabajo de [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

## Por qué importa

La clase donde se define, [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md), existe con este propósito: la clase existe para que separes la complejidad que viene del problema (las reglas del negocio, que no se pueden quitar) de la que añade la solución (anidamiento, banderas, combinaciones sin límite), y para que midas la segunda, la reduzcas con una forma mejor y reconozcas el momento en que lo que queda ya es esencial.

## Cómo funciona

[SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md):

El equipo no reduce la función a ciegas. Primero escribe las 96 combinaciones como una tabla en un documento y obtiene de la persona de negocio la confirmación de que son las que quiere. Después escribe la forma de tabla más tres reglas, la compara con la anidada en 2000 entradas de semilla fija además de la rejilla y mueve la tabla a un archivo de datos con una prueba que verifica que cada zona y cada banda aparece.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)) son:

- **Una función con 96 caminos de código para 96 casos** — causa: cada caso tiene su propio código. Corrección: pasar los casos a una tabla y una regla común.
- **Se reduce la complejidad y se pierde una regla** — causa: se simplificó sin la lista de casos del negocio. Corrección: escribir los casos antes y comprobar la equivalencia.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)) son: Las definiciones son operativas para `tarifas`. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la bibliografía enlazada al final. Se ejecutaron tres análisis con código de ejemplo y datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ningún proyecto real ni se validó la complejidad cognitiva con personas; la regla de tarifa, las opciones binarias y las cinco funciones son construcciones del autor. La siguiente clase pone precio a la complejidad que se decide no reducir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Al menos una vez](../a/al-menos-una-vez.md), [Combinación](./combinacion.md), [Conjunto](./conjunto.md), [Opción](../o/opcion.md), [Complejidad accidental](./complejidad-accidental.md), [Complejidad ciclomática](./complejidad-ciclomatica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Brooks, «No Silver Bullet» (IEEE Computer, 1987)](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer.
- [Moseley y Marks, «Out of the Tar Pit» (2006)](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — estado y complejidad accidental; autoridad: sus autores.
- [McCabe, «A Complexity Measure» (IEEE TSE, 1976)](https://doi.org/10.1109/TSE.1976.233837) — complejidad ciclomática; autoridad: IEEE Transactions on Software Engineering.
- [Campbell, «Cognitive Complexity» (SonarSource)](https://www.sonarsource.com/docs/CognitiveComplexity.pdf) — medida cognitiva; autoridad: SonarSource.
- [Kuhn, Wallace y Gallo, «Software fault interactions and implications for software testing» (IEEE TSE, 2004)](https://doi.org/10.1109/TSE.2004.24) — interacciones de pocas variables en los fallos; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Cobertura estructural](./cobertura-estructural.md) · [Code unit →](./code-unit.md)
