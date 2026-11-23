# Eficiencia de un bus

[↑ Glosario](../../README.md) · [← Efectos en los bordes](./efectos-en-los-bordes.md) · [Ejecución durable →](./ejecucion-durable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Fracción de los ciclos de reloj de una transacción que transportan datos útiles.

Definición de trabajo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

## Por qué importa

La clase donde se define, [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), existe con este propósito: la clase existe para que razones sobre lo que ocurre entre el microcontrolador y un sensor: cuánto cuesta realmente leer un dato por un bus, qué errores de bits detecta cada código de control y cuánta resolución de verdad aporta un convertidor, de modo que elijas un periférico por sus números y no por su hoja de marketing.

## Cómo funciona

[SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md):

El equipo de la plataforma decide tres cosas con los números de la clase. Para el sensor de CO₂ lee 6 bytes por lectura de una vez, no uno por uno, para pasar de 20,5 % a 57,1 % de eficiencia. Para las tramas de radio y de bus cambia la suma de 8 bits por un CRC-8 porque la suma deja pasar el 6 % de los errores de dos bits y el CRC ninguno en tramas de ocho bytes.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son:

- **El bus «es lento» aunque el reloj es alto** — causa: lecturas de un byte con mucho encabezado. Corrección: leer varios bytes por transacción y calcular la eficiencia.
- **Tramas absurdas pasan el control** — causa: paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún bus, sensor ni convertidor: la cuenta de ciclos, los errores inyectados y el ruido gaussiano son construcciones del autor. La siguiente clase pasa de la lectura de un dato a su coste en memoria, energía y cómputo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ciclo](../c/ciclo.md), [Transacción](../t/transaccion.md), [Código de control](../c/codigo-de-control.md), [CRC](../c/crc.md), [LSB](../l/lsb.md), [Sobremuestreo](../s/sobremuestreo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Koopman y Chakravarty, «CRC polynomial selection for embedded networks» (DSN, 2004)](https://doi.org/10.1109/DSN.2004.1311885) — selección de polinomios CRC; autoridad: IEEE DSN.
- [Texas Instruments, nota de aplicación SLVA704 sobre I²C](https://www.ti.com/lit/an/slva704/slva704.pdf) — estructura de la transacción I²C; autoridad: Texas Instruments.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — periféricos y modelos de sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Python: `zlib`](https://docs.python.org/3/library/zlib.html) — `crc32` para comparar con una implementación propia; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla y ruido gaussiano; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Efectos en los bordes](./efectos-en-los-bordes.md) · [Ejecución durable →](./ejecucion-durable.md)
