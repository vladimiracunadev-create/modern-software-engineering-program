# Ciclo de trabajo

[↑ Glosario](../../README.md) · [← Ciclo de dependencias](./ciclo-de-dependencias.md) · [Ciclo de vida →](./ciclo-de-vida.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

El **ciclo de trabajo** (*duty cycle*) es la fracción del tiempo que un dispositivo permanece despierto. Es la definición de [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (restricciones de memoria, energía y cómputo) para dispositivos alimentados por pila. No debe confundirse con el uso del mismo nombre en señales PWM: aquí no habla de la forma de una onda, sino de cuánto tiempo del total el dispositivo consume corriente activa.

## Por qué importa

En un dispositivo a pila, la vida útil la decide la corriente *media*, y esa media depende mucho más del tiempo despierto que de la eficiencia del código. [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) lo dice así: despertar menos y hacer más por cada despertar cambia la carga más que optimizar el código. La decisión que cambia es cada cuánto se mide y se transmite.

## Cómo funciona

Bajar el ciclo de trabajo es la palanca principal. [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) enumera cuatro acciones:

1. **Despertar menos veces.**
2. **Hacer más por cada despertar:** agrupar lecturas y envíos (idea que [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) ya había presentado).
3. **Apagar periféricos que no se usan.**
4. **Elegir el modo de reposo adecuado.**

Lo que hace que agrupar valga la pena es que cada despertar tiene un costo fijo de arranque del reloj y de la radio, que no depende de cuánto se haga. Despertar diez veces para enviar un byte paga diez veces ese costo; despertar una vez para enviar diez bytes lo paga una vez. La contrapartida es la **latencia**: un dato espera hasta el siguiente envío.

La corriente media resulta de ponderar cada fase (reposo, medición, radio) por el tiempo que dura en cada ciclo. Por eso la clase insiste en calcularla con todas las fases.

## Ejemplo

El nodo ambiental de la sala de estudio, caso conductor de la [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), decide en [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) cada cuánto mide y transmite. Una ilustración aritmética propia (no cifras de la clase): si el nodo consume 10 mA despierto y 5 µA dormido, y despierta 1 s cada 60 s, el ciclo de trabajo es 1/60 ≈ 1,7 % y la corriente media ronda 170 µA; despertar cada 600 s la baja a unos 20 µA. La vida de la pila cambia en un orden de magnitud sin tocar el código.

## Errores y confusiones comunes

- **La pila dura una fracción de lo calculado:** se usó la corriente activa o se ignoró la radio. Corrección: calcular la corriente media con todas las fases y medir con un medidor ([SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md)).
- **Vida calculada mayor que la de la propia pila:** se ignoró la autodescarga y el envejecimiento; hay que acotar con la vida útil de la pila.
- **Confundirlo con la frecuencia de reloj:** un reloj más lento no baja el ciclo de trabajo.

## Límites y cuándo no aplica

No ayuda cuando el dispositivo debe escuchar de forma continua (un receptor siempre atento) ni cuando la latencia máxima tolerada es menor que el intervalo de reposo. Reducir despertares aumenta la latencia y puede perder eventos breves entre lecturas. Las cifras de [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) son del modelo de la clase, no mediciones de un dispositivo real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-266](../../../classes/part-22-embedded-iot-y-tiempo-real/se-266-microcontroladores-perifericos-y-buses/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Dispositivo](../d/dispositivo.md), [Corriente media](./corriente-media.md), [Presupuesto de recursos](../p/presupuesto-de-recursos.md), [Reparto del desgaste](../r/reparto-del-desgaste.md), [Zona muerta](../z/zona-muerta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-267 — Restricciones de memoria, energía y cómputo](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-158](../../../classes/part-13-especificaciones-contratos-y-modelos/se-158-specification-by-example-y-bdd/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gal y Toledo, «Algorithms and data structures for flash memories» (ACM Computing Surveys, 2005)](https://doi.org/10.1145/1089733.1089735) — borrado por bloques y reparto del desgaste; autoridad: ACM Computing Surveys.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — restricciones de diseño de sistemas embebidos; autoridad: autores del libro (UC Berkeley).
- [Barr Group, «Embedded C Coding Standard»](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) — reglas de codificación para firmware; autoridad: Barr Group.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — áreas de conocimiento de ingeniería de software; autoridad: IEEE Computer Society.
- [Python: `random`](https://docs.python.org/3/library/random.html) — generador con semilla para las simulaciones; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Ciclo de dependencias](./ciclo-de-dependencias.md) · [Ciclo de vida →](./ciclo-de-vida.md)
