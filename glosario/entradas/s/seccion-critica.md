# Sección crítica

[↑ Glosario](../../README.md) · [← Sdk](./sdk.md) · [Seccionamiento →](./seccionamiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Tramo de código que accede a un dato compartido y se protege para que ningún otro contexto lo interrumpa.

Definición de trabajo de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md): Tramo de código que debe ejecutarse sin que otro hilo acceda al mismo dato.
- En [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md): Fragmento que accede a un dato compartido y debe ejecutarse sin interferencia.

## Por qué importa

La clase donde se define, [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), existe con este propósito: la clase existe para que compartas datos entre una interrupción y el bucle principal sin perder incrementos, sin leer valores partidos y sin desbordar búferes, y para que sepas qué defectos de concurrencia encuentra una prueba corta y cuáles solo encuentra una enumeración de todos los intercalados.

## Cómo funciona

Según [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

En un procesador de 8 bits, un valor de 16 bits se lee en dos instrucciones. Si la interrupción lo actualiza entre ambas, el programa obtiene un byte alto antiguo y uno bajo nuevo. El resultado es casi siempre inocuo: si el valor solo se incrementa en uno y el byte bajo no pasa de 255 a 0, el valor leído es el nuevo. Pero cuando el incremento cruza un límite de byte, el valor leído difiere en 255 o 256: un salto grande, rarísimo y casi irreproducible. Se evita con una sección crítica, con lectura doble hasta que dos lecturas coincidan o con un número de secuencia que la interrupción incrementa antes y después de escribir.

Según [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

El equipo de la plataforma escribe una regla de datos compartidos del nodo. El contador de pulsaciones lo escribe solo la interrupción y el bucle lo lee con una sección crítica de dos instrucciones, de modo que el bucle nunca lo escribe. La temperatura de 16 bits la escribe la interrupción con un número de secuencia: se incrementa antes y después de escribir; el bucle repite la lectura hasta ver el mismo número par dos veces. Las lecturas del sensor van a un búfer de 128 muestras (el doble de lo necesario para una parada de 100 ms) con un contador de pérdidas que se envía con los datos. Además, la duración máxima de las secciones críticas (6 µs) forma parte del análisis de plazos de `SE-268`.

## Ejemplo

Ejemplo de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) (sección «Ejemplo profesional»):

El equipo de la plataforma escribe una regla de datos compartidos del nodo. El contador de pulsaciones lo escribe solo la interrupción y el bucle lo lee con una sección crítica de dos instrucciones, de modo que el bucle nunca lo escribe. La temperatura de 16 bits la escribe la interrupción con un número de secuencia: se incrementa antes y después de escribir; el bucle repite la lectura hasta ver el mismo número par dos veces. Las lecturas del sensor van a un búfer de 128 muestras (el doble de lo necesario para una parada de 100 ms) con un contador de pérdidas que se envía con los datos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un contador pierde incrementos de forma intermitente** — causa: lectura-modificación-escritura sin protección. Corrección: un solo escritor o sección crítica. ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))
- **Un valor muestra saltos grandes rarísimos** — causa: lectura partida de varios bytes. Corrección: sección crítica, lectura doble o número de secuencia. ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))
- **Una sección crítica rompe plazos** — causa: duración no acotada. Corrección: medirla y acotarla, o cambiar a un diseño sin bloqueo. ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se ejecuta la vuelta para cada posición, sin y con una sección crítica que enmascara las interrupciones entre `load` y `store` (la rutina se atiende al salir). ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Fragmento](../f/fragmento.md), [Hilo](../h/hilo.md), [Interferencia](../i/interferencia.md), [Atomicidad](../a/atomicidad.md), [Búfer circular](../b/bufer-circular.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-305 — Patrones funcionales, reactivos y concurrentes](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-453](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-453-verificacion-formal-y-model-checking-tla-spark-y-alloy/README.md).

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

[↑ Glosario](../../README.md) · [← Sdk](./sdk.md) · [Seccionamiento →](./seccionamiento.md)
