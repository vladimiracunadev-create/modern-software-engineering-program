# Corriente media

[↑ Glosario](../../README.md) · [← Corrida](./corrida.md) · [Corrutina →](./corrutina.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Carga consumida en un ciclo dividida por su duración; determina la vida de una pila.

Definición de trabajo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md).

## Por qué importa

En [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), el tema «Presupuesto de energía» importa porque la corriente media, no la activa, fija la vida; el reposo domina si se despierta poco.

## Cómo funciona

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

La vida de una pila es su capacidad dividida por la corriente media. La corriente media es la carga de cada ciclo (activo, radio, reposo) dividida por el periodo. Con 15 mA durante 120 ms y 80 mA durante 40 ms de radio, un ciclo cuesta 5,0 mA·s de actividad; el reposo añade microamperios durante casi todo el periodo. Cuando el periodo es corto, manda lo activo; cuando es largo, manda el reposo, y entonces 2 µA frente a 100 µA es una diferencia de casi nueve veces en vida. Hay que añadir la autodescarga de la pila y, en la práctica, la temperatura y el envejecimiento, que aquí no se modelan.

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

Traslada el análisis a otro dispositivo (por ejemplo, un rastreador de activos con GPS): cambia las corrientes y el periodo, y conserva el procedimiento de calcular la corriente media, repartir las escrituras y declarar los supuestos. La transferencia está lograda cuando puedes explicar qué parte del presupuesto dependía del dispositivo y cuál no, no cuando las tablas se parecen.

## Ejemplo

Ejemplo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sección «Ejemplo mínimo»):

Con 88,3 µA de media la pila dura unos 1133 días sin contar la autodescarga (1098 con ella). Registra versión, comando y salida; duplica la corriente media y predice cuánto baja la vida.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La pila dura una fracción de lo calculado** — causa: se usó la corriente activa o se ignoró la radio. Corrección: calcular la corriente media con todas las fases y medir con un medidor. ([SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió consumo, no se usó una pila ni una flash reales: las corrientes, la autodescarga, la resistencia de los sectores y el tamaño de los registros son supuestos del autor. La siguiente clase añade los plazos que el firmware debe cumplir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](./ciclo.md), [Ciclo de trabajo](./ciclo-de-trabajo.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Reparto del desgaste](../r/reparto-del-desgaste.md), [Zona muerta](../z/zona-muerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md).

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

[↑ Glosario](../../README.md) · [← Corrida](./corrida.md) · [Corrutina →](./corrutina.md)
