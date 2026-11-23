# Capa de acceso al hardware

[↑ Glosario](../../README.md) · [← Capa anticorrupción](./capa-anticorrupcion.md) · [Capa de cascada →](./capa-de-cascada.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Módulo que aísla los registros y periféricos detrás de una interfaz que puede reemplazarse por datos simulados.

Definición de trabajo de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md).

## Por qué importa

En [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), el tema «Capa de acceso al hardware» importa porque aislar los registros permite comprobar la lógica sin dispositivo.

## Cómo funciona

Según [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), en la sección «Capa de acceso al hardware»:

Si la lógica lee directamente un registro, no se puede ejecutar sin el chip. Una capa fina de acceso (leer un canal del convertidor, escribir un pin) con una interfaz que el equipo de desarrollo puede reemplazar por datos simulados permite comprobar el antirrebote, el promedio y las alarmas con pruebas automáticas rápidas. La capa no elimina las pruebas con hardware: reduce lo que solo ellas pueden ver (tiempos reales, ruido, consumo). Es el mismo principio de contratos y dobles de `SE-166`, aplicado a un chip.

## Ejemplo

Caso medido en la sección «Capa de acceso al hardware» de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

Si la lógica lee directamente un registro, no se puede ejecutar sin el chip. Una capa fina de acceso (leer un canal del convertidor, escribir un pin) con una interfaz que el equipo de desarrollo puede reemplazar por datos simulados permite comprobar el antirrebote, el promedio y las alarmas con pruebas automáticas rápidas. La capa no elimina las pruebas con hardware: reduce lo que solo ellas pueden ver (tiempos reales, ruido, consumo). Es el mismo principio de contratos y dobles de `SE-166`, aplicado a un chip.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)) son:

- **El botón «a veces» no responde** — causa: sondeo en un bucle con tareas lentas. Corrección: medir la vuelta más larga y atender el botón por interrupción o acotar el bucle.
- **Un promedio sale en cero o muy bajo con señales altas** — causa: desbordamiento del acumulador. Corrección: escribir la condición de rango y usar un tipo más ancho.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún microcontrolador, compilador de firmware ni banco de pruebas: las duraciones del bucle, el ruido de las lecturas y las variantes del antirrebote son construcciones del autor. La siguiente clase baja a los periféricos y buses por los que el nodo habla con sus sensores.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Interfaz](../i/interfaz.md), [Módulo](../m/modulo.md), [Registro](../r/registro.md), [Simulado](../s/simulado.md), [Desbordamiento](../d/desbordamiento.md), [Firmware](../f/firmware.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md).

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

[↑ Glosario](../../README.md) · [← Capa anticorrupción](./capa-anticorrupcion.md) · [Capa de cascada →](./capa-de-cascada.md)
