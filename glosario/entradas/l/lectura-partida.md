# Lectura partida

[↑ Glosario](../../README.md) · [← Lectura obsoleta](./lectura-obsoleta.md) · [Legacy Modernization Engineer →](./legacy-modernization-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Lectura de un valor de varios bytes que mezcla partes de dos escrituras distintas.

Definición de trabajo de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

## Por qué importa

En [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), el tema «Lecturas partidas» importa porque un valor de varios bytes puede leerse mitad antiguo y mitad nuevo.

## Cómo funciona

Según [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), en la sección «Lecturas partidas»:

En un procesador de 8 bits, un valor de 16 bits se lee en dos instrucciones. Si la interrupción lo actualiza entre ambas, el programa obtiene un byte alto antiguo y uno bajo nuevo. El resultado es casi siempre inocuo: si el valor solo se incrementa en uno y el byte bajo no pasa de 255 a 0, el valor leído es el nuevo. Pero cuando el incremento cruza un límite de byte, el valor leído difiere en 255 o 256: un salto grande, rarísimo y casi irreproducible. Se evita con una sección crítica, con lectura doble hasta que dos lecturas coincidan o con un número de secuencia que la interrupción incrementa antes y después de escribir.

## Ejemplo

Caso medido en la sección «Lecturas partidas» de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

En un procesador de 8 bits, un valor de 16 bits se lee en dos instrucciones. Si la interrupción lo actualiza entre ambas, el programa obtiene un byte alto antiguo y uno bajo nuevo. El resultado es casi siempre inocuo: si el valor solo se incrementa en uno y el byte bajo no pasa de 255 a 0, el valor leído es el nuevo. Pero cuando el incremento cruza un límite de byte, el valor leído difiere en 255 o 256: un salto grande, rarísimo y casi irreproducible.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un valor muestra saltos grandes rarísimos** — causa: lectura partida de varios bytes. Corrección: sección crítica, lectura doble o número de secuencia. ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún procesador, ensamblador ni analizador de interrupciones: las posiciones, la probabilidad de 1/20 y el proceso de llegadas del búfer son construcciones del autor. La siguiente clase saca esos datos del dispositivo por una red que se corta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Byte](../b/byte.md), [Valor](../v/valor.md), [Atomicidad](../a/atomicidad.md), [Búfer circular](../b/bufer-circular.md), [Rutina de interrupción](../r/rutina-de-interrupcion.md), [Sección crítica](../s/seccion-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Lecturas partidas».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — interrupciones, hilos y condiciones de carrera en sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para datos compartidos; autoridad: Barr Group.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — bloqueo por recursos compartidos; autoridad: IEEE Transactions on Computers.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Lectura obsoleta](./lectura-obsoleta.md) · [Legacy Modernization Engineer →](./legacy-modernization-engineer.md)
