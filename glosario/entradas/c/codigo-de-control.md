# Código de control

[↑ Glosario](../../README.md) · [← Código de conducta](./codigo-de-conducta.md) · [Código de estado →](./codigo-de-estado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Bits redundantes añadidos a una trama para detectar errores; la paridad, la suma y el CRC son ejemplos.

Definición de trabajo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

## Por qué importa

En [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), el tema «Códigos de control» importa porque paridad, suma y CRC detectan clases de error distintas.

## Cómo funciona

Según [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), en la sección «Códigos de control»:

Un código de control añade bits redundantes para detectar errores. La paridad es un bit que hace par el número de unos: detecta cualquier cantidad impar de bits invertidos y ninguna cantidad par. La suma de 8 bits detecta muchos errores pero puede cancelarse: dos bits invertidos en posiciones iguales de dos bytes, en sentidos opuestos, dejan la suma igual. Un CRC trata la trama como un polinomio y divide por uno generador: con un polinomio de grado 8 detecta toda ráfaga de hasta 8 bits y, para tramas cortas, todo error de uno a tres bits. Koopman y Chakravarty muestran que la elección del polinomio decide cuántos errores de varios bits detecta.

## Ejemplo

Ejemplo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sección «Caso conductor»):

El nodo ambiental de una sala de estudio continúa como caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md). Esta clase deja el segundo artefacto: la lectura de cada sensor con su eficiencia de bus, su código de control y su factor de sobremuestreo justificados. `SE-267` convertirá esas decisiones en energía y memoria. Cambia después una sola cosa, el tamaño de lectura del sensor de CO₂, y observa cuánto cambia el tiempo despierto.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son:

- **El bus «es lento» aunque el reloj es alto** — causa: lecturas de un byte con mucho encabezado. Corrección: leer varios bytes por transacción y calcular la eficiencia.
- **Tramas absurdas pasan el control** — causa: paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún bus, sensor ni convertidor: la cuenta de ciclos, los errores inyectados y el ruido gaussiano son construcciones del autor. La siguiente clase pasa de la lectura de un dato a su coste en memoria, energía y cómputo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Paridad](../p/paridad.md), [Trama](../t/trama.md), [CRC](./crc.md), [Eficiencia de un bus](../e/eficiencia-de-un-bus.md), [LSB](../l/lsb.md), [Sobremuestreo](../s/sobremuestreo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «Códigos de control».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Koopman y Chakravarty, «CRC polynomial selection for embedded networks» (DSN, 2004)](https://doi.org/10.1109/DSN.2004.1311885) — selección de polinomios CRC; autoridad: IEEE DSN.
- [Texas Instruments, nota de aplicación SLVA704 sobre I²C](https://www.ti.com/lit/an/slva704/slva704.pdf) — estructura de la transacción I²C; autoridad: Texas Instruments.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — periféricos y modelos de sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — `crc32` para comparar con una implementación propia; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla y ruido gaussiano; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Código de conducta](./codigo-de-conducta.md) · [Código de estado →](./codigo-de-estado.md)
