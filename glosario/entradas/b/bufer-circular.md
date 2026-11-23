# Búfer circular

[↑ Glosario](../../README.md) · [← Búfer](./bufer.md) · [Búfer de audio →](./bufer-de-audio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Cola de capacidad fija con índices de lectura y escritura que dan la vuelta.

Definición de trabajo de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

## Por qué importa

La clase donde se define, [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), existe con este propósito: la clase existe para que compartas datos entre una interrupción y el bucle principal sin perder incrementos, sin leer valores partidos y sin desbordar búferes, y para que sepas qué defectos de concurrencia encuentra una prueba corta y cuáles solo encuentra una enumeración de todos los intercalados.

## Cómo funciona

Según [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

Un búfer circular desacopla a quien produce (una interrupción) de quien consume (el bucle). Su tamaño no se decide por la tasa media sino por la parada más larga del consumidor: durante una parada de 100 ms con 0,5 muestras por milisegundo se acumulan 50 muestras. Un búfer pequeño pierde datos justo cuando el sistema está ocupado, que es cuando más importan. Además hay que decidir qué ocurre al llenarse: descartar lo nuevo, descartar lo viejo o contar las pérdidas y avisar.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

El equipo de la plataforma escribe una regla de datos compartidos del nodo. El contador de pulsaciones lo escribe solo la interrupción y el bucle lo lee con una sección crítica de dos instrucciones, de modo que el bucle nunca lo escribe. La temperatura de 16 bits la escribe la interrupción con un número de secuencia: se incrementa antes y después de escribir; el bucle repite la lectura hasta ver el mismo número par dos veces.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)) son:

- **Un contador pierde incrementos de forma intermitente** — causa: lectura-modificación-escritura sin protección. Corrección: un solo escritor o sección crítica.
- **Un valor muestra saltos grandes rarísimos** — causa: lectura partida de varios bytes. Corrección: sección crítica, lectura doble o número de secuencia.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)) son: Las definiciones son operativas para el nodo de la sala. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres simulaciones con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún procesador, ensamblador ni analizador de interrupciones: las posiciones, la probabilidad de 1/20 y el proceso de llegadas del búfer son construcciones del autor. La siguiente clase saca esos datos del dispositivo por una red que se corta.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Atomicidad](../a/atomicidad.md), [Lectura partida](../l/lectura-partida.md), [Rutina de interrupción](../r/rutina-de-interrupcion.md), [Sección crítica](../s/seccion-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — interrupciones, hilos y condiciones de carrera en sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para datos compartidos; autoridad: Barr Group.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — bloqueo por recursos compartidos; autoridad: IEEE Transactions on Computers.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Búfer](./bufer.md) · [Búfer de audio →](./bufer-de-audio.md)
