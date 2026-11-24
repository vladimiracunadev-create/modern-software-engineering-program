# Peor caso de ejecución

[↑ Glosario](../../README.md) · [← Peor caso](./peor-caso.md) · [Percentil →](./percentil.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

El **peor caso de ejecución** (*WCET*, *worst-case execution time*) es la cota superior del tiempo de cómputo de una tarea sobre todas las entradas y estados posibles. Es el sentido de [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sistemas de tiempo real y deadlines); [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) lo llama el insumo más difícil de obtener para planificar. No es el tiempo promedio ni el mayor observado en pruebas: es un límite que ninguna ejecución posible debe superar.

## Por qué importa

El análisis de planificación (si las tareas cumplen sus plazos) usa el peor caso, no el medio. Con la media, un plazo se incumple con una frecuencia que depende de la variabilidad. [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) lo dice: si un trabajo se pasa de su periodo, retrasa al siguiente y la sobrecarga se encadena; por eso la utilización media no basta, importa la cola de la distribución.

## Cómo funciona

Hay dos caminos para obtenerlo, y ambos tienen incertidumbre:

- **Análisis estático:** deriva una cota a partir del código y del modelo del procesador. Es segura si el modelo es fiel, pero puede ser pesimista.
- **Medición con entradas extremas:** ejecuta la tarea con las entradas más desfavorables conocidas. Da un *límite inferior* del peor caso: lo que se observó, no lo que puede ocurrir.

Las fuentes de incertidumbre son cachés, ramas poco frecuentes y esperas de periféricos. Por eso la medición necesita un margen y el análisis estático, un modelo de hardware.

## Ejemplo

El laboratorio de [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) ordena 8 elementos con salida anticipada: 56 pasos de mediana, 80 pasos como máximo observado en 1000 entradas al azar y 84 pasos en el peor caso real (entrada en orden inverso), que 1000 entradas aleatorias no generan. La marca de agua observada queda 4,8 % por debajo del peor caso real. Moraleja: el máximo observado subestima el WCET cuando el peor caso es raro.

## Errores y confusiones comunes

- **Usar el promedio o la mediana** para verificar plazos.
- **Tomar el máximo observado en pruebas como WCET.**
- **Ignorar la interferencia:** el WCET «sin interferencias» no incluye el efecto de otras tareas ni interrupciones; se suma en el análisis de planificación.
- **Confundirlo con latencia de cola:** esta es estadística sobre peticiones; el WCET es una cota para tareas de tiempo real.

## Límites y cuándo no aplica

En procesadores modernos con cachés, predicción de saltos y varios núcleos, obtener una cota ajustada es difícil. Para sistemas sin plazos duros (la mayoría del software de negocio) no se calcula; se usan percentiles. Las cifras de la clase son de un laboratorio con una ordenación pequeña, no de un procesador real.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Peor caso](./peor-caso.md), [Cota](../c/cota.md), [Estado](../e/estado.md), [Interferencia](../i/interferencia.md), [Herencia de prioridad](../h/herencia-de-prioridad.md), [Inversión de prioridad](../i/inversion-de-prioridad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-451 — RTOS y planificación de tiempo real](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

**Sinónimos, siglas y variantes que usa el programa:** «WCET».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Joseph y Pandya, «Finding response times in a real-time system» (The Computer Journal, 1986)](https://doi.org/10.1093/comjnl/29.5.390) — cálculo exacto del tiempo de respuesta; autoridad: The Computer Journal.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia y techo de prioridad; autoridad: IEEE Transactions on Computers.
- [Audsley et al., «Applying new scheduling theory to static priority pre-emptive scheduling» (Software Engineering Journal, 1993)](https://doi.org/10.1049/sej.1993.0034) — análisis con bloqueo y jitter; autoridad: Software Engineering Journal.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — planificación de tiempo real en sistemas embebidos; autoridad: autores del libro (UC Berkeley).

---

[↑ Glosario](../../README.md) · [← Peor caso](./peor-caso.md) · [Percentil →](./percentil.md)
