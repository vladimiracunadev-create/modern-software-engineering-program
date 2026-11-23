# Tiempo de respuesta

[↑ Glosario](../../README.md) · [← Tiempo de recuperación](./tiempo-de-recuperacion.md) · [Tiempo de vida →](./tiempo-de-vida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Tiempo desde la activación de una tarea hasta su terminación, incluida la interferencia de otras.

Definición de trabajo de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md).

## Por qué importa

La clase donde se define, [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), existe con este propósito: la clase existe para que decidas si un conjunto de tareas cumple sus plazos con un análisis y no con una impresión: sabrás distinguir una cota suficiente de una condición exacta, reconocer por qué el tiempo medio de ejecución no sirve y explicar cómo una tarea que nada pide puede retrasar a la más importante.

## Cómo funciona

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

Con prioridades fijas, la tarea más prioritaria que está lista ejecuta, y expulsa a las demás. La asignación por periodo (rate-monotonic: menor periodo, mayor prioridad) es óptima entre las de prioridad fija cuando el plazo es igual al periodo (Liu y Layland). Para n tareas, si la utilización total no supera n(2^(1/n) − 1) (0,78 para 3, 0,693 para infinitas), todos los plazos se cumplen. Por encima, puede ocurrir o no. Joseph y Pandya dan la condición exacta: el tiempo de respuesta de la tarea i es el menor punto fijo de R = C_i + Σ ⌈R/T_j⌉ C_j sobre las tareas j más prioritarias; es planificable si R ≤ T_i.

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

El equipo de la plataforma analiza las tres tareas del nodo con los mejores peores casos medidos: lectura de sensores 8 ms cada 100, pantalla 20 ms cada 200 y radio 60 ms cada 500. La utilización de peor caso es 0,08 + 0,10 + 0,12 = 0,30, muy por debajo de la cota de 0,78. Con las prioridades por periodo, el análisis da tiempos de respuesta de 8, 28 y 88 ms, todos dentro del plazo. Al añadir el registro en flash protegido por un mutex, activan herencia de prioridad y acotan la sección crítica a 3 ms, de modo que el bloqueo máximo de la tarea de sensores es de 3 ms.

## Ejemplo

Ejemplo de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el tiempo de respuesta de la tarea de menor prioridad de un conjunto de dos. Antes de ejecutarlo, predice si cumple su plazo de 10.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se confía en la cota de utilización como condición necesaria** — causa: se confunde suficiente con necesaria. Corrección: aplicar el análisis exacto de tiempo de respuesta. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Se simula en pasos de 0,1 ms con y sin herencia de prioridad y se mide el tiempo de respuesta de H. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Interferencia](../i/interferencia.md), [Tarea](./tarea.md), [Terminación](./terminacion.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](../p/peor-caso-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (18 clases más lo mencionan; las que más):

[SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-261](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-261-rendimiento-bateria-y-recursos-limitados/README.md), [SE-446](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-446-iec-61508-y-niveles-de-integridad-de-seguridad/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-419](../../../classes/part-34-saas-y-plataformas-de-producto/se-419-sla-por-nivel-soporte-y-operacion-del-producto/README.md), [SE-004](../../../classes/part-00-ingenieria-de-software-como-profesion/se-004-etica-interes-publico-y-consecuencias-de-las-decisiones-tecnicas/README.md), [SE-007](../../../classes/part-00-ingenieria-de-software-como-profesion/se-007-calidad-interna-externa-y-calidad-en-uso/README.md), [SE-145](../../../classes/part-12-ingenieria-de-requisitos/se-145-elicitacion-analisis-especificacion-y-validacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Joseph y Pandya, «Finding response times in a real-time system» (The Computer Journal, 1986)](https://doi.org/10.1093/comjnl/29.5.390) — cálculo exacto del tiempo de respuesta; autoridad: The Computer Journal.
- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia y techo de prioridad; autoridad: IEEE Transactions on Computers.
- [Audsley et al., «Applying new scheduling theory to static priority pre-emptive scheduling» (Software Engineering Journal, 1993)](https://doi.org/10.1049/sej.1993.0034) — análisis con bloqueo y jitter; autoridad: Software Engineering Journal.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — planificación de tiempo real en sistemas embebidos; autoridad: autores del libro (UC Berkeley).

---

[↑ Glosario](../../README.md) · [← Tiempo de recuperación](./tiempo-de-recuperacion.md) · [Tiempo de vida →](./tiempo-de-vida.md)
