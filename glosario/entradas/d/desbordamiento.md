# Desbordamiento

[↑ Glosario](../../README.md) · [← Desajuste de proporción de muestra](./desajuste-de-proporcion-de-muestra.md) · [Descarte de carga →](./descarte-de-carga.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Resultado de una operación que no cabe en el ancho del tipo y da la vuelta sin avisar.

Definición de trabajo de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md).

## Por qué importa

En [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md), el tema «Aritmética de ancho fijo» importa porque los desbordamientos no avisan y producen valores plausibles.

## Cómo funciona

Según [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

**Cómo leer la figura.** Cada fila es un número de lecturas y cada columna una señal media; el color más oscuro es un porcentaje mayor de ventanas erróneas, y el borde marca las celdas que fallan. La frontera de fallo se desplaza hacia menos lecturas cuanto mayor es la señal, porque lo que importa es el producto de ambas. **Dónde deja de valer:** el modelo emula la vuelta con una máscara; un compilador puede promover tipos y ocultar o cambiar el desbordamiento, y un procesador de 32 bits no lo sufriría. Lo que enseña es la condición: lecturas × máximo ≤ 65 535, comprobable antes de ejecutar nada.

Según [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** el CO₂ se muestra como un valor cercano a 1000 cuando en la sala hay más de 3000. **Hipótesis rivales:** (a) el sensor está mal calibrado; (b) la conversión a ppm tiene un error; (c) el acumulador desborda. **Prueba:** calcula el promedio con un acumulador de 32 bits sobre las mismas lecturas; si difiere en 2048 cuentas, la causa es el desbordamiento. **Conclusión:** 32 × 3000 = 96 000 > 65 535. **Regresión:** cambia el acumulador a 32 bits, añade la aserción «lecturas × máximo cabe» y una prueba con lecturas al máximo. No cambies a la vez el ancho y el número de lecturas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md):

El equipo de la plataforma separa el firmware del nodo en dos módulos. `hal.py` (simulado aquí) expone `leer_canal(n)` y `leer_boton()`; `logica.py` contiene el antirrebote, el promedio con acumulador de 32 bits, la alarma de CO₂ y la decisión de cuándo enviar. Las pruebas en el equipo de desarrollo ejecutan `logica.py` con secuencias generadas, incluidas las de rebotes y las de lecturas al máximo. En el dispositivo real solo se comprueban la latencia del botón con una interrupción y el consumo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un promedio sale en cero o muy bajo con señales altas** — causa: desbordamiento del acumulador. Corrección: escribir la condición de rango y usar un tipo más ancho. ([SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** el modelo emula la vuelta con una máscara; un compilador puede promover tipos y ocultar o cambiar el desbordamiento, y un procesador de 32 bits no lo sufriría. ([SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Operación](../o/operacion.md), [Resultado](../r/resultado.md), [Tipo](../t/tipo.md), [Capa de acceso al hardware](../c/capa-de-acceso-al-hardware.md), [Firmware](../f/firmware.md), [Latencia de un evento](../l/latencia-de-un-evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-265 — Hardware, firmware y software embebido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (11 clases más lo mencionan; las que más):

[SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-071](../../../classes/part-05-fundamentos-de-programacion/se-071-taller-transferir-una-solucion-entre-lenguajes/README.md), [SE-053](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-053-recursion-induccion-y-razonamiento-estructural/README.md), [SE-274](../../../classes/part-22-embedded-iot-y-tiempo-real/se-274-safety-seguridad-y-vida-util-prolongada/README.md), [SE-052](../../../classes/part-04-pensamiento-computacional-y-resolucion-de-problemas/se-052-invariantes-precondiciones-y-poscondiciones/README.md), [SE-175](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-175-diseno-visual-tipografia-color-y-contraste/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

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

[↑ Glosario](../../README.md) · [← Desajuste de proporción de muestra](./desajuste-de-proporcion-de-muestra.md) · [Descarte de carga →](./descarte-de-carga.md)
