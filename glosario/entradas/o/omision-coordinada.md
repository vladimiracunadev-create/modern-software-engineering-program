# Omisión coordinada

[↑ Glosario](../../README.md) · [← Omisión](./omision.md) · [Opción →](./opcion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Subregistro de la espera causada por una pausa del servidor cuando el generador deja de enviar mientras espera respuesta.

Definición de trabajo de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md).

## Por qué importa

La clase donde se define, [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), existe con este propósito: la clase existe para que elijas la forma de carga que responde a tu pregunta (cuánto aguanta en régimen, dónde se rompe, cómo se recupera de un pico, qué se degrada con las horas) y para que sepas qué hace trampa en una prueba: un generador que deja de enviar cuando el servidor se detiene, un arranque frío mezclado con el régimen estable o una duración demasiado corta para ver una fuga.

## Cómo funciona

Según [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), en la sección «Omisión coordinada»:

El mismo sistema, con 40 solicitudes por segundo (utilización del 50 %), se detiene por completo 10 segundos entre el 60 y el 70 de una prueba de 180 s. Se mide con tres generadores: uno abierto con llegadas de Poisson y latencia contada desde la hora prevista de llegada; uno cerrado con 8 usuarios virtuales que esperan la respuesta y 0,2 s entre peticiones; y el cerrado con una corrección que rellena las muestras que habrían existido.

El sistema es el mismo y el p99 pasa de 9 071 ms a 232 ms: el generador cerrado dejó de enviar durante la pausa y el 99,85 % de sus muestras son de antes o de después. El p99,9 sí ve la pausa (9 916 ms) porque las 8 peticiones atrapadas son lo bastante lentas; el p99 no. La corrección recupera una parte porque asume un intervalo esperado entre envíos. Un informe que diga «p99 de 232 ms» con el generador cerrado afirma algo que ninguna persona real vivió.

**Cómo leer la figura.** Cada fila es un generador de carga observando el mismo servidor con la misma pausa; el cuadrado es la mediana, el triángulo el percentil 99 y el rombo el percentil 99,9, en escala logarítmica. Mira primero dónde cae el triángulo: en el generador cerrado se queda en 232 ms, lejos de los 9 071 del abierto. **Dónde deja de valer:** un generador cerrado es el modelo correcto cuando la población es de verdad un número fijo de personas que esperan (una sala de examen con 30 estudiantes); en ese caso no hay omisión porque no hay más llegadas. La corrección de omisión supone un intervalo esperado y no se aplica sin conocerlo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md):

El equipo prepara el cierre de plazo con un plan de tres pruebas. La de carga reproduce el perfil del cierre anterior con generador abierto, 60 solicitudes por segundo y cinco minutos tras descartar los dos primeros.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El p99 es excelente y hay quejas de pausas** — causa: omisión coordinada del generador cerrado. Corrección: generador abierto o corrección documentada. ([SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Espera](../e/espera.md), [Generador](../g/generador.md), [Prueba de carga](../p/prueba-de-carga.md), [Prueba de estrés](../p/prueba-de-estres.md), [Prueba de pico](../p/prueba-de-pico.md), [Prueba de resistencia](../p/prueba-de-resistencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [wrk2](https://github.com/giltene/wrk2) — omisión coordinada y su corrección; autoridad: repositorio del autor de la herramienta.
- [Grafana k6: tipos de pruebas](https://grafana.com/docs/k6/latest/testing-guides/test-types/) — carga, estrés, pico y resistencia; autoridad: documentación de la herramienta.
- [Schroeder, Wierman y Harchol-Balter, «Open versus closed: a cautionary tale»](https://www.usenix.org/legacy/event/nsdi06/tech/full_papers/schroeder/schroeder.pdf) — modelos abierto y cerrado; autoridad: artículo de NSDI 2006.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga que se amplifica y descarte de trabajo; autoridad: Google, libro de ingeniería de confiabilidad.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de prioridad usada en el simulador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Omisión](./omision.md) · [Opción →](./opcion.md)
