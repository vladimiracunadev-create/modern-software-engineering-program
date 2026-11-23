# Sobremuestreo

[↑ Glosario](../../README.md) · [← Sobrecarga](./sobrecarga.md) · [Sobreobtención →](./sobreobtencion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Promedio de varias lecturas de una señal estable para reducir el ruido de cuantización y de medición.

Definición de trabajo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

## Por qué importa

La clase donde se define, [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), existe con este propósito: la clase existe para que razones sobre lo que ocurre entre el microcontrolador y un sensor: cuánto cuesta realmente leer un dato por un bus, qué errores de bits detecta cada código de control y cuánta resolución de verdad aporta un convertidor, de modo que elijas un periférico por sus números y no por su hoja de marketing.

## Cómo funciona

Según [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md):

Un convertidor de 10 bits parte el rango en 1024 niveles; con una referencia de 3,3 V, cada nivel (LSB) es de 3,2 mV. La resolución efectiva es menor por el ruido. Paradójicamente, un poco de ruido permite mejorar: si la señal ruidosa cruza varios niveles, el promedio de muchas lecturas converge al valor real, y cada factor cuatro de sobremuestreo agrega un bit. Sin ruido todas las lecturas dan el mismo nivel y promediar no ayuda. La técnica cuesta tiempo y energía: cuatro veces más lecturas por bit.

## Ejemplo

Ejemplo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sección «Caso conductor»):

El nodo ambiental de una sala de estudio continúa como caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md). Esta clase deja el segundo artefacto: la lectura de cada sensor con su eficiencia de bus, su código de control y su factor de sobremuestreo justificados. `SE-267` convertirá esas decisiones en energía y memoria. Cambia después una sola cosa, el tamaño de lectura del sensor de CO₂, y observa cuánto cambia el tiempo despierto.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son:

- **El bus «es lento» aunque el reloj es alto** — causa: lecturas de un byte con mucho encabezado. Corrección: leer varios bytes por transacción y calcular la eficiencia.
- **Tramas absurdas pasan el control** — causa: paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún bus, sensor ni convertidor: la cuenta de ciclos, los errores inyectados y el ruido gaussiano son construcciones del autor. La siguiente clase pasa de la lectura de un dato a su coste en memoria, energía y cómputo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cuantización](../c/cuantizacion.md), [Medición](../m/medicion.md), [Ruido](../r/ruido.md), [Señal](./senal.md), [Código de control](../c/codigo-de-control.md), [CRC](../c/crc.md).
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

[↑ Glosario](../../README.md) · [← Sobrecarga](./sobrecarga.md) · [Sobreobtención →](./sobreobtencion.md)
