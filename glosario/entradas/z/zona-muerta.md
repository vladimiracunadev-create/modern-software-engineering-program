# Zona muerta

[↑ Glosario](../../README.md) · [← Zona gris](./zona-gris.md) · [Β →](../c/concepto.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Intervalo de la entrada en que un filtro no cambia su salida, por truncado.

Definición de trabajo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md).

## Por qué importa

La clase donde se define, [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), existe con este propósito: la clase existe para que presupuestes un dispositivo con tres recursos escasos —energía, memoria no volátil y precisión numérica— y descubras cuál de ellos manda antes de escribir código: cuántos años dura una pila, cuánto dura una flash y cuánto error introduce un filtro de enteros.

## Cómo funciona

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

Sin unidad de coma flotante, un filtro de paso bajo `y += (x − y) >> k` es barato y suele bastar. Pero el desplazamiento a la derecha trunca hacia menos infinito: hacia arriba, cuando `x − y` es menor que 2^k, la diferencia desplazada es cero y el filtro se detiene antes de la entrada, con una zona muerta de 2^k − 1 cuentas. Hacia abajo trunca a más negativo y llega exacto. Redondear (sumando la mitad antes de desplazar) reduce la zona y la hace simétrica en teoría; en la práctica deja un error residual de otro signo. La conclusión es elegir con conocimiento del sesgo.

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

Cuando el procesador tiene unidad de coma flotante y el coste es aceptable, o cuando el rango dinámico lo exige. Si usas enteros, calcula el error de truncado y la zona muerta.

## Ejemplo

Ejemplo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sección «Preguntas frecuentes»):

Cuando el procesador tiene unidad de coma flotante y el coste es aceptable, o cuando el rango dinámico lo exige. Si usas enteros, calcula el error de truncado y la zona muerta.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El filtro «se pega» cerca de la entrada** — causa: zona muerta del truncado. Corrección: redondear o aumentar la resolución interna. ([SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el error es de un filtro con ganancia 2^−k y entrada constante; con una señal que cambia, la zona muerta se mezcla con la dinámica. ([SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Filtro](../f/filtro.md), [Intervalo](../i/intervalo.md), [Ciclo de trabajo](../c/ciclo-de-trabajo.md), [Corriente media](../c/corriente-media.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Reparto del desgaste](../r/reparto-del-desgaste.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

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

[↑ Glosario](../../README.md) · [← Zona gris](./zona-gris.md) · [Β →](../c/concepto.md)
