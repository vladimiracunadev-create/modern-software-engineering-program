# Carrera de datos

[↑ Glosario](../../README.md) · [← Cargas adversarias](./cargas-adversarias.md) · [Carrera entre peticiones →](./carrera-entre-peticiones.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Acceso concurrente a una posición de memoria, con al menos una escritura y sin sincronización que ordene los accesos.

Definición de trabajo de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md).

## Por qué importa

La clase donde se define, [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), existe con este propósito: la clase existe para que veas una carrera de datos como lo que es, una propiedad del orden de ejecución y no del código, y para que elijas con evidencia entre un cerrojo, un cerrojo más fino o evitar el estado compartido, sabiendo qué defecto nuevo introduce cada elección: el interbloqueo y la contención.

## Cómo funciona

Según [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md):

Una **carrera de datos** ocurre cuando dos tareas acceden a la misma posición de memoria, al menos una escribe y no hay sincronización que las ordene. Una **condición de carrera** es más general: el resultado depende del orden de pasos, aunque cada acceso esté protegido; por ejemplo, comprobar si queda cupo y luego descontarlo en dos pasos protegidos por separado. En `contador += 1` hay tres pasos: leer, sumar, escribir. Si dos hilos leen el mismo valor antes de que cualquiera escriba, uno de los incrementos desaparece. El GIL de CPython evita que se corrompa la estructura interna del intérprete, no que tu programa pierda un incremento: la secuencia sigue siendo de varios pasos y el intérprete puede cambiar de hilo entre ellos.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md):

El equipo del panel de la docente no añade un cerrojo global. Primero separa dos casos: el contador de entregas recibidas pasa a una operación atómica de la base (`UPDATE curso SET entregas = entregas + 1`), que no necesita cerrojo en el programa; el cupo de la tarea, que implica leer, comprobar y descontar, se protege con una transacción que bloquea esa fila.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md)) son:

- **Contadores que a veces están un poco bajos** — causa: leer-sumar-escribir sin sincronizar. Corrección: operación atómica o sección crítica.
- **El servicio se congela y no hay error** — causa: espera circular entre cerrojos. Corrección: orden global de adquisición.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **carrera de datos** ocurre cuando dos tareas acceden a la misma posición de memoria, al menos una escribe y no hay sincronización que las ordene. ([SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-351](../../../classes/part-29-datos-persistencia-y-recuperacion/se-351-transacciones-aislamiento-y-concurrencia/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contención](./contencion.md), [Interbloqueo](../i/interbloqueo.md), [Orden global de adquisición](../o/orden-global-de-adquisicion.md), [Sección crítica](../s/seccion-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-386 — Memoria compartida, locks y condiciones de carrera](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (14 clases más lo mencionan; las que más):

[SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md), [SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-080](../../../classes/part-06-paradigmas-de-programacion/se-080-programacion-reactiva-y-flujos/README.md).

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

[↑ Glosario](../../README.md) · [← Cargas adversarias](./cargas-adversarias.md) · [Carrera entre peticiones →](./carrera-entre-peticiones.md)
