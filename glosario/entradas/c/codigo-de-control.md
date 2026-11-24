# Código de control

[↑ Glosario](../../README.md) · [← Código de conducta](./codigo-de-conducta.md) · [Código de estado →](./codigo-de-estado.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Un **código de control** (también «código de detección de errores») son bits redundantes que se añaden a una trama para detectar errores de transmisión. La paridad, la suma de verificación y el CRC son los ejemplos de [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (microcontroladores, periféricos y buses). Detectar no es corregir: el código dice que algo está mal, no qué bit lo está.

## Por qué importa

Un bus o un radioenlace corrompe bits; sin control, el receptor actúa sobre datos falsos. Pero los tres códigos de la clase detectan *clases distintas* de error, y elegir el equivocado deja pasar tramas absurdas. La decisión profesional es qué errores se espera detectar y qué código los cubre, y declararlo.

## Cómo funciona

Según [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md):

- **Paridad.** Un bit que hace par el número de unos. Detecta cualquier cantidad *impar* de bits invertidos y ninguna cantidad par: dos bits invertidos pasan sin ser vistos.
- **Suma de 8 bits.** Detecta muchos errores, pero puede cancelarse: dos bits invertidos en posiciones iguales de dos bytes, en sentidos opuestos, dejan la suma igual.
- **CRC** (comprobación de redundancia cíclica). Trata la trama como un polinomio y la divide por uno generador; el resto se envía como control. Con un polinomio de grado 8 detecta toda ráfaga de hasta 8 bits y, en tramas cortas, todo error de uno a tres bits. Koopman y Chakravarty, citados por la clase, muestran que la elección del polinomio decide cuántos errores de varios bits se detectan.

El receptor recalcula el control sobre lo recibido y lo compara con el que llegó; si difieren, descarta la trama o pide reenvío.

## Ejemplo

El nodo ambiental de la sala de estudio (caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)) deja en [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) la lectura de cada sensor con su eficiencia de bus, su código de control y su factor de sobremuestreo justificados. Ilustración propia: un bit de paridad sobre el byte `0110 0101` (cuatro unos) con paridad par es 0; si el ruido invierte dos bits, la paridad sigue siendo correcta y el error pasa; un CRC-8 sí lo detectaría.

## Errores y confusiones comunes

- **Tramas absurdas pasan el control:** se usó paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre ([SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md)).
- **Confundir detectar con corregir:** para corregir hacen falta códigos distintos, que añaden más redundancia.
- **Confundirlo con una firma o un hash criptográfico:** un CRC detecta errores accidentales; no protege contra un atacante que recalcula el control.
- **El bus «es lento» aunque el reloj es alto:** es otro problema de la clase (lecturas de un byte con mucho encabezado), no del control.

## Límites y cuándo no aplica

Ningún código de control detecta *todos* los errores: un CRC bien elegido deja una probabilidad residual de que un error pase. No sirve como autenticación (esa pertenece a la firma digital y a la raíz de confianza). Y añade bits a cada trama, lo que reduce la eficiencia del bus; en tramas muy cortas el control puede ser una fracción grande del total.

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
