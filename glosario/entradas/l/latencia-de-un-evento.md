# Latencia de un evento

[↑ Glosario](../../README.md) · [← Latencia de red](./latencia-de-red.md) · [LCOM4 →](./lcom4.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Tiempo entre que ocurre un evento y el firmware empieza a atenderlo.

Definición de trabajo de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md).

## Por qué importa

La clase donde se define, [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), existe con este propósito: la clase existe para que distingas qué decide el hardware, qué decide el firmware y qué puede probarse sin ninguno de los dos, y para que elijas una arquitectura de firmware por lo que garantiza sobre la respuesta a un evento, no por costumbre.

## Cómo funciona

[SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

El equipo de la plataforma separa el firmware del nodo en dos módulos. `hal.py` (simulado aquí) expone `leer_canal(n)` y `leer_boton()`; `logica.py` contiene el antirrebote, el promedio con acumulador de 32 bits, la alarma de CO₂ y la decisión de cuándo enviar. Las pruebas en el equipo de desarrollo ejecutan `logica.py` con secuencias generadas, incluidas las de rebotes y las de lecturas al máximo. En el dispositivo real solo se comprueban la latencia del botón con una interrupción y el consumo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)) son:

- **El botón «a veces» no responde** — causa: sondeo en un bucle con tareas lentas. Corrección: medir la vuelta más larga y atender el botón por interrupción o acotar el bucle.
- **Un promedio sale en cero o muy bajo con señales altas** — causa: desbordamiento del acumulador. Corrección: escribir la condición de rango y usar un tipo más ancho.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún microcontrolador, compilador de firmware ni banco de pruebas: las duraciones del bucle, el ruido de las lecturas y las variantes del antirrebote son construcciones del autor. La siguiente clase baja a los periféricos y buses por los que el nodo habla con sus sensores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Firmware](../f/firmware.md), [Capa de acceso al hardware](../c/capa-de-acceso-al-hardware.md), [Desbordamiento](../d/desbordamiento.md), [Mutante equivalente](../m/mutante-equivalente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — sistemas embebidos y ciberfísicos con el tiempo en la semántica; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para firmware; autoridad: Barr Group.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `struct`](https://docs.python.org/3/library/struct.html) — empaquetado de enteros con ancho definido; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Latencia de red](./latencia-de-red.md) · [LCOM4 →](./lcom4.md)
