# Rutina de interrupción

[↑ Glosario](../../README.md) · [← Ruta vertical](./ruta-vertical.md) · [SaaS →](../s/saas.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Código que el procesador ejecuta al ocurrir un evento, suspendiendo el programa principal entre dos instrucciones.

Definición de trabajo de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md).

## Por qué importa

En [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), el tema «Interrupciones y contexto» importa porque la rutina de interrupción corre entre dos instrucciones cualesquiera del programa principal.

## Cómo funciona

Según [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

Una interrupción suspende el programa principal entre dos instrucciones, ejecuta su rutina y devuelve el control. El programa principal no sabe cuándo ocurrió: lo que sabe es que, entre dos instrucciones cualesquiera, el estado compartido pudo cambiar. Esa es la fuente de todos los defectos de esta clase. Una rutina de interrupción corta y sin bloqueos es la regla: guarda el dato, marca una bandera y vuelve; el trabajo se hace en el bucle principal. Lee y Seshia presentan esto como la raíz del no determinismo de los programas con interrupciones.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md):

El equipo de la plataforma escribe una regla de datos compartidos del nodo. El contador de pulsaciones lo escribe solo la interrupción y el bucle lo lee con una sección crítica de dos instrucciones, de modo que el bucle nunca lo escribe. La temperatura de 16 bits la escribe la interrupción con un número de secuencia: se incrementa antes y después de escribir; el bucle repite la lectura hasta ver el mismo número par dos veces.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)) son:

- **Un contador pierde incrementos de forma intermitente** — causa: lectura-modificación-escritura sin protección. Corrección: un solo escritor o sección crítica.
- **Un valor muestra saltos grandes rarísimos** — causa: lectura partida de varios bytes. Corrección: sección crítica, lectura doble o número de secuencia.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una rutina de interrupción corta y sin bloqueos es la regla: guarda el dato, marca una bandera y vuelve; el trabajo se hace en el bucle principal. ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Instrucción](../i/instruccion.md), [Principal](../p/principal.md), [Atomicidad](../a/atomicidad.md), [Búfer circular](../b/bufer-circular.md), [Lectura partida](../l/lectura-partida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-269 — Interrupciones, concurrencia y estado compartido](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-265](../../../classes/part-22-embedded-iot-y-tiempo-real/se-265-hardware-firmware-y-software-embebido/README.md).

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «ISR».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — interrupciones, hilos y condiciones de carrera en sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para datos compartidos; autoridad: Barr Group.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — bloqueo por recursos compartidos; autoridad: IEEE Transactions on Computers.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ruta vertical](./ruta-vertical.md) · [SaaS →](../s/saas.md)
