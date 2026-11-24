# Sección crítica

[↑ Glosario](../../README.md) · [← Sdk](./sdk.md) · [Seccionamiento →](./seccionamiento.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Una **sección crítica** es un tramo de código que accede a un dato compartido y se protege para que ningún otro contexto lo interrumpa o acceda al mismo dato a la vez. [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) (interrupciones, concurrencia y estado compartido) la presenta en microcontroladores, donde el otro contexto es una interrupción; [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) y [SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md) la presentan en hilos: el tramo debe ejecutarse sin que otro hilo acceda al mismo dato.

## Por qué importa

Es la herramienta básica para que el estado compartido no se corrompa: sin perder incrementos, sin leer valores partidos y sin desbordar búferes ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)). La decisión práctica es qué protege exactamente y por cuánto tiempo.

## Cómo funciona

El mecanismo depende del contexto:

- **Con una interrupción (microcontrolador):** se desactivan las interrupciones durante el tramo, o se usa una instrucción atómica. [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) lo ofrece, junto a la lectura doble y al número de secuencia, como defensa contra la lectura partida.
- **Con hilos ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)):** se usa un cerrojo (*lock*) que un solo hilo puede tener a la vez; los demás esperan.

Principios de diseño:

1. **Mantenerla corta.** Cuanto más dura, más latencia de interrupción (en embebidos) o más contención (en hilos).
2. **Proteger el dato, no el código:** cada dato compartido debe tener un único cerrojo asociado.
3. **No bloquear dentro:** esperar entrada/salida con el cerrojo tomado bloquea a todos.
4. **Ordenar los cerrojos** si hay varios, para evitar interbloqueos.

[SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) añade que una prueba corta encuentra algunos defectos de concurrencia y solo una **enumeración de todos los intercalados** encuentra otros.

## Ejemplo

El equipo de la plataforma en [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) escribe una regla de datos compartidos del nodo: qué datos comparte la interrupción con el bucle principal y cómo se protege cada uno. Ilustración propia del caso de lectura partida: el programa principal desactiva las interrupciones, copia el valor de 16 bits, las reactiva, y trabaja con la copia.

## Errores y confusiones comunes

- **Proteger solo algunos accesos** al dato; uno sin protección rompe todo.
- **Secciones críticas largas** que bloquean la interrupción o a otros hilos.
- **Confundirla con una operación atómica:** la atómica la hace el hardware en una instrucción; la sección crítica protege varios pasos.
- **Tomar dos cerrojos en distinto orden** en rutas diferentes.

## Límites y cuándo no aplica

No ayuda con datos que no se comparten. Desactivar interrupciones no protege de otros núcleos. En lugar de proteger, a veces conviene evitar el compartir (pasar mensajes, copiar). Una sección crítica correcta no garantiza el rendimiento: la contención se mide aparte.

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
