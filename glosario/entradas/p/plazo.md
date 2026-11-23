# Plazo

[↑ Glosario](../../README.md) · [← Playbook](./playbook.md) · [Plazo de gracia →](./plazo-de-gracia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md)

## Definición

Instante límite, relativo a la activación de una tarea, en el que debe haber terminado.

Definición de trabajo de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md).

## Por qué importa

En [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), el tema «Plazos y tipos de tiempo real» importa porque un plazo duro tiene consecuencias que uno blando no tiene; cambia cuánto margen se exige.

## Cómo funciona

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

Una tarea periódica tiene un periodo (cada cuánto se activa), un tiempo de cómputo y un plazo (cuándo debe haber terminado, a menudo igual al periodo). En un sistema de tiempo real duro, incumplir un plazo es un fallo del sistema (un freno, un marcapasos); en uno blando, degrada la calidad (una pantalla que se refresca tarde). «Tiempo real» no es «rápido»: es «predecible con respecto a un plazo». Una alarma de CO₂ que llega en 100 ms siempre es de tiempo real; una que llega en 10 ms casi siempre y en 2 s a veces no lo es.

Según [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md):

El equipo de la plataforma analiza las tres tareas del nodo con los mejores peores casos medidos: lectura de sensores 8 ms cada 100, pantalla 20 ms cada 200 y radio 60 ms cada 500. La utilización de peor caso es 0,08 + 0,10 + 0,12 = 0,30, muy por debajo de la cota de 0,78. Con las prioridades por periodo, el análisis da tiempos de respuesta de 8, 28 y 88 ms, todos dentro del plazo. Al añadir el registro en flash protegido por un mutex, activan herencia de prioridad y acotan la sección crítica a 3 ms, de modo que el bloqueo máximo de la tarea de sensores es de 3 ms.

## Ejemplo

Ejemplo de [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula el tiempo de respuesta de la tarea de menor prioridad de un conjunto de dos. Antes de ejecutarlo, predice si cumple su plazo de 10.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un plazo se incumple a veces con baja utilización media** — causa: tiempo de ejecución variable y análisis con la media. Corrección: usar el peor caso o un percentil alto y medir la cola. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))
- **La sobrecarga ocasional se propaga a varios plazos** — causa: trabajos que se pasan retrasan a los siguientes. Corrección: abortar o degradar trabajos tardíos y vigilar el encadenamiento. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En un sistema de tiempo real duro, incumplir un plazo es un fallo del sistema (un freno, un marcapasos); en uno blando, degrada la calidad (una pantalla que se refresca tarde). ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))
- Con plazos menores que el periodo conviene la asignación por plazo, y con prioridades dinámicas (el plazo más cercano primero) se puede llegar a utilización 1, a costa de un planificador más complejo. ([SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-267](../../../classes/part-22-embedded-iot-y-tiempo-real/se-267-restricciones-de-memoria-energia-y-computo/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Activación](../a/activacion.md), [Instante](../i/instante.md), [Límite](../l/limite.md), [Tarea](../t/tarea.md), [Inversión de prioridad](../i/inversion-de-prioridad.md), [Peor caso de ejecución](./peor-caso-de-ejecucion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-268 — Sistemas de tiempo real y deadlines](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.

**También se usa en** (223 clases más lo mencionan; las que más):

[SE-184](../../../classes/part-15-procesos-planificacion-y-estimacion/se-184-lean-teoria-de-colas-y-limites-de-trabajo/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-358](../../../classes/part-29-datos-persistencia-y-recuperacion/se-358-privacidad-retencion-y-ciclo-de-vida-del-dato/README.md), [SE-315](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-315-gof-estructurales-adapter-decorator-facade-proxy-y-composite/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md), [SE-490](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-490-metricas-dora-y-mejora-sin-gaming/README.md), [SE-525](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-525-retiro-archivado-y-disposicion-de-sistemas/README.md), [SE-222](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-222-daemons-servicios-y-ciclo-de-vida/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md), [Amazon](../../../casos/exito/amazon.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [HealthCare.gov](../../../casos/fallo/healthcare-gov.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Liu y Layland, «Scheduling algorithms for multiprogramming in a hard-real-time environment» (JACM, 1973)](https://doi.org/10.1145/321738.321743) — planificación por prioridades por periodo y cota de utilización; autoridad: Journal of the ACM.
- [Joseph y Pandya, «Finding response times in a real-time system» (The Computer Journal, 1986)](https://doi.org/10.1093/comjnl/29.5.390) — cálculo exacto del tiempo de respuesta; autoridad: The Computer Journal.
- [Sha, Rajkumar y Lehoczky, «Priority inheritance protocols» (IEEE Transactions on Computers, 1990)](https://doi.org/10.1109/12.57058) — herencia y techo de prioridad; autoridad: IEEE Transactions on Computers.
- [Audsley et al., «Applying new scheduling theory to static priority pre-emptive scheduling» (Software Engineering Journal, 1993)](https://doi.org/10.1049/sej.1993.0034) — análisis con bloqueo y jitter; autoridad: Software Engineering Journal.
- [Lee y Seshia, «Introduction to Embedded Systems»](https://ptolemy.berkeley.edu/books/leeseshia/) — planificación de tiempo real en sistemas embebidos; autoridad: autores del libro (UC Berkeley).

---

[↑ Glosario](../../README.md) · [← Playbook](./playbook.md) · [Plazo de gracia →](./plazo-de-gracia.md)
