# Complejidad ciclomática

[↑ Glosario](../../README.md) · [← Complejidad accidental](./complejidad-accidental.md) · [Complejidad cognitiva →](./complejidad-cognitiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

Número de caminos independientes de una función.

Definición de trabajo de [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md): Número de caminos independientes que atraviesan una función.

## Por qué importa

La clase donde se define, [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md), existe con este propósito: la clase existe para que separes la complejidad que viene del problema (las reglas del negocio, que no se pueden quitar) de la que añade la solución (anidamiento, banderas, combinaciones sin límite), y para que midas la segunda, la reduzcas con una forma mejor y reconozcas el momento en que lo que queda ya es esencial.

## Cómo funciona

Según [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md):

La complejidad ciclomática cuenta caminos independientes y es fácil de calcular y de relacionar con el número mínimo de pruebas. No distingue un camino plano de uno anidado. Las medidas cognitivas intentan acercarse a la dificultad de leer: penalizan más el anidamiento y las rupturas del flujo. Ninguna distingue lo esencial de lo accidental: una regla de 96 casos bien escrita puede tener una complejidad alta y ser simple de leer.

Según [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md):

Las herramientas convierten olores en números: líneas, parámetros, profundidad de anidamiento, complejidad ciclomática. Un umbral (más de 25 líneas, más de 5 parámetros) es una convención que reduce el espacio de búsqueda y arrastra falsas alarmas. Cada medida confunde cosas distintas: el largo mezcla lógica con datos; la cantidad de parámetros mezcla un objeto de transferencia con una función mal definida. La medida orienta la lectura; no la sustituye.

## Ejemplo

Ejemplo de [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) (sección «Ejemplo mínimo»):

El fragmento mide la complejidad ciclomática de una función. Antes de ejecutarlo, predice el valor.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)) son:

- **Una función con 96 caminos de código para 96 casos** — causa: cada caso tiene su propio código. Corrección: pasar los casos a una tabla y una regla común.
- **Se reduce la complejidad y se pierde una regla** — causa: se simplificó sin la lista de casos del negocio. Corrección: escribir los casos antes y comprobar la equivalencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se calcula la complejidad ciclomática y una complejidad cognitiva simplificada: cada `if`, bucle o manejador suma uno más el nivel de anidamiento; un `elif` suma uno sin penalizar; cada operador booleano suma uno. ([SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-301](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-301-cohesion-acoplamiento-y-encapsulacion/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Función](../f/funcion.md), [Cobertura por pares](./cobertura-por-pares.md), [Complejidad accidental](./complejidad-accidental.md), [Complejidad cognitiva](./complejidad-cognitiva.md), [Complejidad esencial](./complejidad-esencial.md), [Duplicación accidental](../d/duplicacion-accidental.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-306 — Code smells y diagnóstico contextual](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-322](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-322-antipatrones-y-deuda-de-diseno/README.md), [SE-313](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-313-criterios-para-usar-un-catalogo-de-patrones/README.md), [SE-311](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-311-taller-refactorizar-sin-alterar-comportamiento/README.md), [SE-323](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-323-taller-refactorizar-con-patrones-y-medir-su-costo/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-518](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-518-arqueologia-de-codigo-y-recuperacion-de-conocimiento/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [McCabe, «A Complexity Measure» (IEEE TSE, 1976)](https://doi.org/10.1109/TSE.1976.233837) — complejidad ciclomática; autoridad: IEEE Transactions on Software Engineering.
- [Brooks, «No Silver Bullet» (IEEE Computer, 1987)](https://doi.org/10.1109/MC.1987.1663532) — complejidad esencial y accidental; autoridad: IEEE Computer.
- [Moseley y Marks, «Out of the Tar Pit» (2006)](https://curtclifton.net/papers/MoseleyMarks06a.pdf) — estado y complejidad accidental; autoridad: sus autores.
- [Campbell, «Cognitive Complexity» (SonarSource)](https://www.sonarsource.com/docs/CognitiveComplexity.pdf) — medida cognitiva; autoridad: SonarSource.
- [Kuhn, Wallace y Gallo, «Software fault interactions and implications for software testing» (IEEE TSE, 2004)](https://doi.org/10.1109/TSE.2004.24) — interacciones de pocas variables en los fallos; autoridad: IEEE Transactions on Software Engineering.

---

[↑ Glosario](../../README.md) · [← Complejidad accidental](./complejidad-accidental.md) · [Complejidad cognitiva →](./complejidad-cognitiva.md)
