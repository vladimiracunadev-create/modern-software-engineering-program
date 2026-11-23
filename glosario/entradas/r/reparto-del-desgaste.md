# Reparto del desgaste

[↑ Glosario](../../README.md) · [← Reparto de costo compartido](./reparto-de-costo-compartido.md) · [Repetición →](./repeticion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Política que distribuye las escrituras entre los bloques de una flash para igualar sus borrados.

Definición de trabajo de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md).

## Por qué importa

La clase donde se define, [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), existe con este propósito: la clase existe para que presupuestes un dispositivo con tres recursos escasos —energía, memoria no volátil y precisión numérica— y descubras cuál de ellos manda antes de escribir código: cuántos años dura una pila, cuánto dura una flash y cuánto error introduce un filtro de enteros.

## Cómo funciona

Según [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

Una flash se programa por bytes o páginas pero se borra por sectores completos, y cada sector soporta un número limitado de borrados. Escribir siempre en el mismo sector convierte cada registro en un borrado. El reparto del desgaste (wear leveling) rota las escrituras: el **dinámico** reparte entre los sectores libres y deja los de datos fríos intactos; el **estático** también mueve los datos fríos para usar todos. Gal y Toledo describen estructuras con registro circular que borran un sector solo cuando se llena. La vida pasa de días a décadas, con la advertencia de que existen otros límites como la retención de datos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md):

El equipo de la plataforma reescribe el presupuesto del nodo. Para la energía, pasa de despertar cada 10 s a cada 60 s y agrupa seis lecturas en un envío: la vida estimada pasa de unos 200 a más de 1000 días con 5 µA de reposo, y los 5 µA se validan con un medidor antes de aceptarlos. Para la flash, guarda los registros en un anillo sobre todos los sectores libres y deja la configuración, que casi no cambia, en un sector aparte con una copia.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)) son:

- **La pila dura una fracción de lo calculado** — causa: se usó la corriente activa o se ignoró la radio. Corrección: calcular la corriente media con todas las fases y medir con un medidor.
- **La vida calculada de la pila supera la de la propia pila** — causa: se ignoró la autodescarga y el envejecimiento. Corrección: añadir la autodescarga y acotar con la vida útil de la pila.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres cálculos y simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió consumo, no se usó una pila ni una flash reales: las corrientes, la autodescarga, la resistencia de los sectores y el tamaño de los registros son supuestos del autor. La siguiente clase añade los plazos que el firmware debe cumplir.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo de trabajo](../c/ciclo-de-trabajo.md), [Corriente media](../c/corriente-media.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Zona muerta](../z/zona-muerta.md).
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

[↑ Glosario](../../README.md) · [← Reparto de costo compartido](./reparto-de-costo-compartido.md) · [Repetición →](./repeticion.md)
