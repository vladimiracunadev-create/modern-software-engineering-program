# Complejidad esencial

[↑ Glosario](../../README.md) · [← Complejidad cognitiva](./complejidad-cognitiva.md) · [Complemento →](./complemento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md)

## Definición

La **complejidad esencial** es la que se deriva del problema que el software resuelve y no puede eliminarse sin cambiar el problema ([SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md)). Es la contraparte de la accidental: no depende de cómo se escriba el programa, sino de cuántos casos, reglas y excepciones tiene el negocio.

## Por qué importa

Si se confunde con la accidental, se intenta «simplificar» lo que no se puede simplificar y se pierden reglas del negocio. Si se ignora, se fingen soluciones simples que no cubren los casos reales. La decisión que cambia es qué se hace con ella: **se gestiona, no se elimina**. Se hace explícita, se escribe en un lugar legible y se prueba.

## Cómo funciona

El ejemplo de [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) es aritmético: si el negocio tiene cuatro zonas, tres bandas de peso y tres opciones, hay 4 × 3 × 3 = 96 casos distintos y no existe un programa correcto con menos. Se reconoce con una prueba de ablación mental: **al quitarla, cambia lo que el sistema hace**. Si se elimina un caso y el sistema deja de cumplir una regla, era esencial.

Gestionarla significa darle una forma que la deje visible. [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) propone una tabla o un conjunto de reglas: los 96 casos viven como datos en un solo lugar, no repartidos en 96 ramas. La complejidad no baja (los casos siguen siendo 96), pero deja de interactuar con otras partes. Esa separación es la que permite luego atacar la accidental sin riesgo: se conserva la lista de casos como la verdad contra la cual se comprueba la equivalencia.

## Ejemplo

Una empresa de envíos cobra según la zona de destino, la banda de peso y la opción (estándar, exprés, con seguro). Esas combinaciones son reglas de negocio: cada una produce una tarifa. Se registran en una tabla de 96 filas y se prueba que cada fila produce el valor esperado. Simplificar el código no toca la tabla; cambiar una tarifa es cambiar una fila, con su propia prueba. Ilustración del caso de `tarifas` en [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md).

## Errores y confusiones comunes

- **Una función con 96 caminos de código para 96 casos**: confundir esencial con una razón para repetir código; se corrige pasando los casos a una tabla y una regla común.
- **Se reduce la complejidad y se pierde una regla**: se simplificó sin la lista de casos del negocio.
- **Declarar esencial todo lo que duele**: parte de lo que duele es de la forma.
- **Ocultar la complejidad esencial** en código disperso: sigue ahí, pero ahora nadie la ve.

## Límites y cuándo no aplica

Lo que es esencial depende de dónde se trace la frontera del problema: si el negocio cambia sus reglas (menos zonas, menos opciones), parte de la complejidad esencial desaparece, pero eso es cambiar el problema, no el código. [SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) precisa que sus definiciones son operativas para `tarifas`, que sus análisis usan datos sintéticos y que las opciones binarias y las cinco funciones son construcciones del autor. No hay una medida universal de cuánta complejidad es esencial.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-306](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-306-code-smells-y-diagnostico-contextual/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Deriva](../d/deriva.md), [Problemas](../p/problemas.md), [Cobertura por pares](./cobertura-por-pares.md), [Complejidad accidental](./complejidad-accidental.md), [Complejidad ciclomática](./complejidad-ciclomatica.md), [Complejidad cognitiva](./complejidad-cognitiva.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-309 — Complejidad accidental y esencial](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md).

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

[↑ Glosario](../../README.md) · [← Complejidad cognitiva](./complejidad-cognitiva.md) · [Complemento →](./complemento.md)
