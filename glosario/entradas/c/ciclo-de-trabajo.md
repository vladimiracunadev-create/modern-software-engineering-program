# Ciclo de trabajo

[↑ Glosario](../../README.md) · [← Ciclo de dependencias](./ciclo-de-dependencias.md) · [Ciclo de vida →](./ciclo-de-vida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Fracción del tiempo que un dispositivo permanece despierto.

Definición de trabajo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md).

## Por qué importa

En [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), el tema «Ciclo de trabajo» importa porque despertar menos y hacer más por despertar cambia la carga más que optimizar el código.

## Cómo funciona

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), en la sección «Ciclo de trabajo»:

El ciclo de trabajo es la fracción del tiempo que el dispositivo está despierto. Bajarlo es la palanca principal: despertar menos veces, hacer más por cada despertar (agrupar lecturas y envíos, como en `SE-266`), apagar periféricos que no se usan y elegir el modo de reposo adecuado. Cada despertar tiene un coste fijo de arranque del reloj y de la radio que no depende de cuánto se haga, lo que favorece agrupar. La contrapartida es la latencia: un dato espera hasta el siguiente envío.

## Ejemplo

Caso medido en la sección «Ciclo de trabajo» de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

El ciclo de trabajo es la fracción del tiempo que el dispositivo está despierto. Bajarlo es la palanca principal: despertar menos veces, hacer más por cada despertar (agrupar lecturas y envíos, como en `SE-266`), apagar periféricos que no se usan y elegir el modo de reposo adecuado. Cada despertar tiene un coste fijo de arranque del reloj y de la radio que no depende de cuánto se haga, lo que favorece agrupar. La contrapartida es la latencia: un dato espera hasta el siguiente envío.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)) son:

- **La pila dura una fracción de lo calculado** — causa: se usó la corriente activa o se ignoró la radio. Corrección: calcular la corriente media con todas las fases y medir con un medidor.
- **La vida calculada de la pila supera la de la propia pila** — causa: se ignoró la autodescarga y el envejecimiento. Corrección: añadir la autodescarga y acotar con la vida útil de la pila.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió consumo, no se usó una pila ni una flash reales: las corrientes, la autodescarga, la resistencia de los sectores y el tamaño de los registros son supuestos del autor. La siguiente clase añade los plazos que el firmware debe cumplir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Corriente media](./corriente-media.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Reparto del desgaste](../r/reparto-del-desgaste.md), [Zona muerta](../z/zona-muerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gal y Toledo, «Algorithms and data structures for flash memories» (ACM Computing Surveys, 2005)](https://doi.org/10.1145/1089733.1089735) — borrado por bloques y reparto del desgaste; autoridad: ACM Computing Surveys.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — restricciones de diseño de sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para firmware; autoridad: Barr Group.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ciclo de dependencias](./ciclo-de-dependencias.md) · [Ciclo de vida →](./ciclo-de-vida.md)
