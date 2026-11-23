# Interbloqueo

[↑ Glosario](../../README.md) · [← Intensidad aritmética](./intensidad-aritmetica.md) · [Intercalación →](./intercalacion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Situación en que un grupo de tareas espera cada una un recurso que retiene otra del grupo.

Definición de trabajo de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md).

## Por qué importa

En [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), el tema «Interbloqueo» importa porque un cerrojo mal ordenado detiene el servicio sin dejar error.

## Cómo funciona

Según [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), en la sección «Interbloqueo»:

Un **interbloqueo** (*deadlock*) detiene a un grupo de tareas que se esperan unas a otras. Coffman y colaboradores identificaron cuatro condiciones necesarias: exclusión mutua, retención y espera (se retiene un recurso mientras se pide otro), ausencia de expropiación y espera circular. Basta eliminar una para que no ocurra. La más práctica de eliminar es la espera circular imponiendo un **orden global de adquisición**: todos los cerrojos se toman siempre en el mismo orden (por ejemplo, por identificador creciente). Un tiempo límite al adquirir no previene el interbloqueo: lo convierte en un error que hay que manejar, liberando lo tomado y reintentando con otro orden.

## Ejemplo

Ejemplo de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) (sección «Preguntas frecuentes»):

Evita el bloqueo eterno, no el interbloqueo: ambos hilos fallan o uno falla y el otro sigue, según una carrera de temporización. Hay que decidir qué hacer al fallar: liberar lo tomado, registrar y reintentar con orden fijo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)) son:

- **Contadores que a veces están un poco bajos** — causa: leer-sumar-escribir sin sincronizar. Corrección: operación atómica o sección crítica.
- **El servicio se congela y no hay error** — causa: espera circular entre cerrojos. Corrección: orden global de adquisición.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un tiempo límite al adquirir no previene el interbloqueo: lo convierte en un error que hay que manejar, liberando lo tomado y reintentando con otro orden. ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Recurso](../r/recurso.md), [Tarea](../t/tarea.md), [Carrera de datos](../c/carrera-de-datos.md), [Contención](../c/contencion.md), [Orden global de adquisición](../o/orden-global-de-adquisicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md), [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-451](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-451-rtos-y-planificacion-de-tiempo-real/README.md).

**Aparece en los casos de estudio:** [Therac-25](../../../casos/fallo/therac-25.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Coffman, Elphick y Shoshani, «System deadlocks»](https://doi.org/10.1145/356586.356588) — condiciones del interbloqueo; autoridad: artículo original (ACM Computing Surveys, 1971).
- [Python: threading](https://docs.python.org/3/library/threading.html) — cerrojos, barreras y tiempos límite; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — alcance del GIL; autoridad: documentación de Python.
- [Go: el detector de carreras](https://go.dev/doc/articles/race_detector) — qué ve y qué no ve una detección dinámica; autoridad: documentación oficial de Go.
- [Hoare, «Communicating sequential processes»](https://doi.org/10.1145/359576.359585) — alternativa de paso de mensajes que se retoma en la clase siguiente; autoridad: artículo original (1978).

---

[↑ Glosario](../../README.md) · [← Intensidad aritmética](./intensidad-aritmetica.md) · [Intercalación →](./intercalacion.md)
