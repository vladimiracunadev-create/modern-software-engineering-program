# Firmware

[↑ Glosario](../../README.md) · [← Firmantes permitidos](./firmantes-permitidos.md) · [FIT →](./fit.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Programa almacenado en la memoria no volátil de un dispositivo que controla su hardware y se actualiza con procedimientos propios.

Definición de trabajo de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md).

## Por qué importa

En [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), el tema «Hardware, firmware y software» importa porque decide quién es dueño de cada defecto y dónde puede probarse.

## Cómo funciona

Según [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

El **hardware** es el microcontrolador, los sensores, los buses y la alimentación; fija qué es posible y qué cuesta. El **firmware** es el programa que vive en la memoria del dispositivo y habla con ese hardware; se actualiza con más dificultad que una aplicación y su fallo suele dejar el dispositivo mudo. El **software embebido** es el conjunto: firmware y componentes que corren junto al dispositivo. Un defecto puede ser de cualquiera de los tres y el síntoma casi nunca lo dice: un promedio erróneo puede venir de un sensor ruidoso, de un acumulador que desborda o de un cableado. Diagnosticar es separar capas, igual que en una red.

Según [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

El equipo de la plataforma separa el firmware del nodo en dos módulos. `hal.py` (simulado aquí) expone `leer_canal(n)` y `leer_boton()`; `logica.py` contiene el antirrebote, el promedio con acumulador de 32 bits, la alarma de CO₂ y la decisión de cuándo enviar. Las pruebas en el equipo de desarrollo ejecutan `logica.py` con secuencias generadas, incluidas las de rebotes y las de lecturas al máximo. En el dispositivo real solo se comprueban la latencia del botón con una interrupción y el consumo. Documentan además la condición del acumulador como una aserción en tiempo de compilación.

## Ejemplo

Ejemplo de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma separa el firmware del nodo en dos módulos. `hal.py` (simulado aquí) expone `leer_canal(n)` y `leer_boton()`; `logica.py` contiene el antirrebote, el promedio con acumulador de 32 bits, la alarma de CO₂ y la decisión de cuándo enviar. Las pruebas en el equipo de desarrollo ejecutan `logica.py` con secuencias generadas, incluidas las de rebotes y las de lecturas al máximo. En el dispositivo real solo se comprueban la latencia del botón con una interrupción y el consumo. Documentan además la condición del acumulador como una aserción en tiempo de compilación.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)) son:

- **El botón «a veces» no responde** — causa: sondeo en un bucle con tareas lentas. Corrección: medir la vuelta más larga y atender el botón por interrupción o acotar el bucle.
- **Un promedio sale en cero o muy bajo con señales altas** — causa: desbordamiento del acumulador. Corrección: escribir la condición de rango y usar un tipo más ancho.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un procesador puede traducir internamente instrucciones a operaciones más simples, y el firmware o un hipervisor añaden capas que la figura omite; el principio es la lista de ventanas y límites, no el número de filas. ([SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md))

## Relación con otros conceptos

- **Prerrequisito:** ninguno declarado en las clases.
- **Ver también:** [Control](../c/control.md), [Dispositivo](../d/dispositivo.md), [ABI](../a/abi.md), [Arquitectura](../a/arquitectura.md), [Capa de acceso al hardware](../c/capa-de-acceso-al-hardware.md), [Desbordamiento](../d/desbordamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-013 — Arquitectura básica de un computador moderno](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md), [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md), [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md), [SE-283](../../../classes/part-23-runtimes-y-plataformas-modernas/se-283-hardware-seguro-tee-y-atestacion/README.md), [SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para firmware; autoridad: Barr Group.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — sistemas embebidos y ciberfísicos con el tiempo en la semántica; autoridad: autores del libro (UC Berkeley).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `struct`](https://docs.python.org/3/library/struct.html) — empaquetado de enteros con ancho definido; autoridad: documentación de Python.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Firmantes permitidos](./firmantes-permitidos.md) · [FIT →](./fit.md)
