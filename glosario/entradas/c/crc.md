# CRC

[↑ Glosario](../../README.md) · [← Cota de bucle](./cota-de-bucle.md) · [CRDT →](./crdt.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Código de redundancia cíclica; resto de dividir la trama, vista como un polinomio, por un polinomio generador.

Definición de trabajo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

## Por qué importa

En [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), el tema «Códigos de control» importa porque paridad, suma y CRC detectan clases de error distintas.

## Cómo funciona

Según [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md):

Un código de control añade bits redundantes para detectar errores. La paridad es un bit que hace par el número de unos: detecta cualquier cantidad impar de bits invertidos y ninguna cantidad par. La suma de 8 bits detecta muchos errores pero puede cancelarse: dos bits invertidos en posiciones iguales de dos bytes, en sentidos opuestos, dejan la suma igual. Un CRC trata la trama como un polinomio y divide por uno generador: con un polinomio de grado 8 detecta toda ráfaga de hasta 8 bits y, para tramas cortas, todo error de uno a tres bits. Koopman y Chakravarty muestran que la elección del polinomio decide cuántos errores de varios bits detecta.

Según [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md):

El equipo de la plataforma decide tres cosas con los números de la clase. Para el sensor de CO₂ lee 6 bytes por lectura de una vez, no uno por uno, para pasar de 20,5 % a 57,1 % de eficiencia. Para las tramas de radio y de bus cambia la suma de 8 bits por un CRC-8 porque la suma deja pasar el 6 % de los errores de dos bits y el CRC ninguno en tramas de ocho bytes. Para la batería promedia 16 lecturas, que reducen el error eficaz de 0,58 a 0,15 LSB con el ruido que el convertidor ya tiene, y verifica en el dispositivo que ese ruido existe antes de confiar en el resultado.

## Ejemplo

Ejemplo de [SE-266 — Microcontroladores, periféricos y buses](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma decide tres cosas con los números de la clase. Para el sensor de CO₂ lee 6 bytes por lectura de una vez, no uno por uno, para pasar de 20,5 % a 57,1 % de eficiencia. Para las tramas de radio y de bus cambia la suma de 8 bits por un CRC-8 porque la suma deja pasar el 6 % de los errores de dos bits y el CRC ninguno en tramas de ocho bytes.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Tramas absurdas pasan el control** — causa: paridad o suma para errores de varios bits. Corrección: usar un CRC y declarar qué errores cubre. ([SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un CRC trata la trama como un polinomio y divide por uno generador: con un polinomio de grado 8 detecta toda ráfaga de hasta 8 bits y, para tramas cortas, todo error de uno a tres bits. ([SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Generador](../g/generador.md), [Trama](../t/trama.md), [Vista](../v/vista.md), [Código de control](./codigo-de-control.md), [Eficiencia de un bus](../e/eficiencia-de-un-bus.md), [LSB](../l/lsb.md).
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

[↑ Glosario](../../README.md) · [← Cota de bucle](./cota-de-bucle.md) · [CRDT →](./crdt.md)
