# Corrutina

[↑ Glosario](../../README.md) · [← Corriente media](./corriente-media.md) · [Corte →](./corte.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Función que puede suspenderse en un `await` y reanudarse después, gestionada por un bucle de eventos.

Definición de trabajo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md).

## Por qué importa

La clase donde se define, [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), existe con este propósito: la clase existe para que distingas tres ideas que se usan como sinónimos y resuelven problemas distintos: la concurrencia (varias cosas en curso a la vez), el paralelismo (varias cosas ejecutándose a la vez en hardware distinto) y la asincronía (un modo de escribir programas que esperan sin ocupar un hilo), y para que decidas cuál necesita un servicio antes de pagar su costo en complejidad.

## Cómo funciona

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

En `asyncio` un solo hilo ejecuta un bucle de eventos; cada corrutina corre hasta el siguiente `await` y entrega el control al bucle, que elige otra lista para continuar. Es concurrencia sin intercalaciones arbitrarias: dos corrutinas solo se alternan en puntos de `await`, lo que elimina muchas carreras de la clase siguiente. El precio es la **cooperación**: si una corrutina calcula durante cuatrocientos milisegundos sin `await`, las demás, incluido el latido de salud, esperan. La asincronía no hace el cálculo más rápido ni usa más núcleos; hace barata la espera. Por eso conviene para servicios con mucha entrada y salida y por eso un cálculo pesado dentro del bucle es un defecto que no falla una prueba pequeña y sí falla en producción.

Según [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md):

El equipo del servicio de entregas clasifica sus tareas en una tabla antes de tocar el código: guardar el archivo (espera de disco), consultar el estado del curso (espera de red), calcular la similitud contra entregas anteriores (cálculo de 300 ms) y enviar el acuse (espera de red). Las tres esperas pasan a corrutinas con un límite de 50 conexiones simultáneas. El cálculo de similitud no se trocea dentro del bucle: se envía a un grupo de procesos de tamaño igual al número de núcleos menos uno, y el servicio sigue respondiendo mientras tanto. El latido de salud sale de una tarea propia que no comparte código con el cálculo.

## Ejemplo

Ejemplo de [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) (sección «Ejemplo profesional»):

El equipo del servicio de entregas clasifica sus tareas en una tabla antes de tocar el código: guardar el archivo (espera de disco), consultar el estado del curso (espera de red), calcular la similitud contra entregas anteriores (cálculo de 300 ms) y enviar el acuse (espera de red). Las tres esperas pasan a corrutinas con un límite de 50 conexiones simultáneas. El cálculo de similitud no se trocea dentro del bucle: se envía a un grupo de procesos de tamaño igual al número de núcleos menos uno, y el servicio sigue respondiendo mientras tanto. El latido de salud sale de una tarea propia que no comparte código con el cálculo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El latido de salud se detiene a ratos** — causa: una corrutina calcula sin `await`. Corrección: trocear con `await` o sacar el cálculo del bucle. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En `asyncio` un solo hilo ejecuta un bucle de eventos; cada corrutina corre hasta el siguiente `await` y entrega el control al bucle, que elige otra lista para continuar. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))
- Ambos solapan esperas; la ventaja de `async` es el costo por tarea: miles de corrutinas caben donde miles de hilos serían caros, y no hay intercalaciones arbitrarias entre `await`. ([SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Función](../f/funcion.md), [Concurrencia](./concurrencia.md), [GIL](../g/gil.md), [Ley de Amdahl](../l/ley-de-amdahl.md), [Paralelismo](../p/paralelismo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-385 — Concurrencia, paralelismo y asincronía](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-079](../../../classes/part-06-paradigmas-de-programacion/se-079-programacion-orientada-a-eventos/README.md), [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md), [SE-075](../../../classes/part-06-paradigmas-de-programacion/se-075-orientacion-a-objetos-mensajes-y-encapsulacion/README.md), [SE-076](../../../classes/part-06-paradigmas-de-programacion/se-076-programacion-funcional-composicion-e-inmutabilidad/README.md), [SE-077](../../../classes/part-06-paradigmas-de-programacion/se-077-programacion-declarativa-y-basada-en-reglas/README.md), [SE-078](../../../classes/part-06-paradigmas-de-programacion/se-078-programacion-logica-y-resolucion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: asyncio](https://docs.python.org/3/library/asyncio.html) — bucle de eventos y corrutinas; autoridad: documentación de Python.
- [Python: desarrollo con asyncio](https://docs.python.org/3/library/asyncio-dev.html) — modo de depuración y código bloqueante; autoridad: documentación de Python.
- [Python: glosario](https://docs.python.org/3/glossary.html) — definición del bloqueo global del intérprete; autoridad: documentación de Python.
- [Python: concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) — ejecutores de hilos y procesos; autoridad: documentación de Python.
- [Amdahl, «Validity of the single processor approach…»](https://doi.org/10.1145/1465482.1465560) — límite de aceleración; autoridad: artículo original (1967).

---

[↑ Glosario](../../README.md) · [← Corriente media](./corriente-media.md) · [Corte →](./corte.md)
