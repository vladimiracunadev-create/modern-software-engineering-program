# Orden global de adquisición

[↑ Glosario](../../README.md) · [← Orden e iteración](./orden-e-iteracion.md) · [Orden topológico →](./orden-topologico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Regla que obliga a tomar los cerrojos siempre en el mismo orden para impedir la espera circular.

Definición de trabajo de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md).

## Por qué importa

La clase donde se define, [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), existe con este propósito: la clase existe para que veas una carrera de datos como lo que es, una propiedad del orden de ejecución y no del código, y para que elijas con evidencia entre un cerrojo, un cerrojo más fino o evitar el estado compartido, sabiendo qué defecto nuevo introduce cada elección: el interbloqueo y la contención.

## Cómo funciona

Según [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md):

Un **interbloqueo** (*deadlock*) detiene a un grupo de tareas que se esperan unas a otras. Coffman y colaboradores identificaron cuatro condiciones necesarias: exclusión mutua, retención y espera (se retiene un recurso mientras se pide otro), ausencia de expropiación y espera circular. Basta eliminar una para que no ocurra. La más práctica de eliminar es la espera circular imponiendo un **orden global de adquisición**: todos los cerrojos se toman siempre en el mismo orden (por ejemplo, por identificador creciente). Un tiempo límite al adquirir no previene el interbloqueo: lo convierte en un error que hay que manejar, liberando lo tomado y reintentando con otro orden.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md):

El equipo del panel de la docente no añade un cerrojo global. Primero separa dos casos: el contador de entregas recibidas pasa a una operación atómica de la base (`UPDATE curso SET entregas = entregas + 1`), que no necesita cerrojo en el programa; el cupo de la tarea, que implica leer, comprobar y descontar, se protege con una transacción que bloquea esa fila.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El servicio se congela y no hay error** — causa: espera circular entre cerrojos. Corrección: orden global de adquisición. ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2); los conteos fueron idénticos y la versión real con tiempo límite difirió, como se declara. No se midió ningún cerrojo del sistema operativo, ninguna memoria relajada ni una carga real: las instrucciones atómicas, la popularidad Zipf y las rondas son construcciones del autor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Regla](../r/regla.md), [Carrera de datos](../c/carrera-de-datos.md), [Contención](../c/contencion.md), [Interbloqueo](../i/interbloqueo.md), [Sección crítica](../s/seccion-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-081](../../../classes/part-06-paradigmas-de-programacion/se-081-programacion-concurrente-y-actores/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: threading](https://docs.python.org/3/library/threading.html) — cerrojos, barreras y tiempos límite; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — alcance del GIL; autoridad: documentación de Python.
- [Coffman, Elphick y Shoshani, «System deadlocks»](https://doi.org/10.1145/356586.356588) — condiciones del interbloqueo; autoridad: artículo original (ACM Computing Surveys, 1971).
- [Go: el detector de carreras](https://go.dev/doc/articles/race_detector) — qué ve y qué no ve una detección dinámica; autoridad: documentación oficial de Go.
- [Hoare, «Communicating sequential processes»](https://doi.org/10.1145/359576.359585) — alternativa de paso de mensajes que se retoma en la clase siguiente; autoridad: artículo original (1978).

---

[↑ Glosario](../../README.md) · [← Orden e iteración](./orden-e-iteracion.md) · [Orden topológico →](./orden-topologico.md)
