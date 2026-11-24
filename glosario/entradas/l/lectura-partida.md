# Lectura partida

[↑ Glosario](../../README.md) · [← Lectura obsoleta](./lectura-obsoleta.md) · [Legacy Modernization Engineer →](./legacy-modernization-engineer.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Una **lectura partida** (*torn read*) es la lectura de un valor de varios bytes que mezcla partes de dos escrituras distintas. Es el sentido de [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) (interrupciones, concurrencia y estado compartido) en microcontroladores. Aparece cuando la lectura no es atómica y algo (una interrupción) cambia el valor entre sus pasos.

## Por qué importa

Es un defecto casi invisible: casi siempre da un resultado correcto, y de vez en cuando uno absurdo, rarísimo y casi irreproducible. Quien no conoce el mecanismo atribuye el síntoma al ruido del sensor.

## Cómo funciona

[SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) da el caso: en un procesador de 8 bits, un valor de 16 bits se lee en dos instrucciones (byte alto y byte bajo). Si la interrupción actualiza el valor entre ambas, el programa obtiene un byte alto antiguo y uno bajo nuevo, o al revés.

El resultado suele ser inocuo: si el valor solo se incrementa en uno y el byte bajo no pasa de 255 a 0, el valor leído coincide con el nuevo. Pero cuando el incremento cruza un límite de byte, el valor leído difiere en 255 o 256: un salto grande.

Tres defensas de la clase:

1. **Sección crítica:** desactivar las interrupciones mientras se lee.
2. **Lectura doble:** leer hasta que dos lecturas consecutivas coincidan.
3. **Número de secuencia:** la interrupción lo incrementa antes y después de escribir; el lector repite si cambió o es impar.

## Ejemplo

Ilustración numérica: el contador vale `0x00FF` y la interrupción lo sube a `0x0100`. El programa lee el byte alto (`0x00`), llega la interrupción y escribe `0x0100`; luego lee el byte bajo (`0x00`). El valor obtenido es `0x0000`: un salto de 255 hacia atrás, que en un registro de tiempo parecería un reloj que retrocede. Es el tipo de síntoma que [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md) describe como saltos grandes rarísimos.

## Errores y confusiones comunes

- **Un valor muestra saltos grandes rarísimos:** causa, lectura partida de un valor de varios bytes; corrección, una de las tres defensas ([SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md)).
- **Pensar que se resuelve con `volatile`:** impide que el compilador reutilice el valor, pero no hace atómica la lectura.
- **Aplicarla solo a microcontroladores de 8 bits:** puede ocurrir cada vez que el ancho del valor supera lo que el procesador lee de una vez.
- **Confundirla con una condición de carrera completa:** es una de sus formas.

## Límites y cuándo no aplica

En procesadores que leen el valor completo en una instrucción atómica no ocurre. La lectura doble supone que el valor deja de cambiar entre lecturas; si cambia más rápido que el bucle de lectura, no termina. La sección crítica introduce latencia de interrupción: debe ser corta.

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
