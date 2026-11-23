# Prueba de resistencia

[↑ Glosario](../../README.md) · [← Prueba de regresión](./prueba-de-regresion.md) · [Prueba de restauración →](./prueba-de-restauracion.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Ejecución larga con carga moderada para encontrar fallos acumulativos.

Definición de trabajo de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md).

## Por qué importa

La clase donde se define, [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), existe con este propósito: la clase existe para que elijas la forma de carga que responde a tu pregunta (cuánto aguanta en régimen, dónde se rompe, cómo se recupera de un pico, qué se degrada con las horas) y para que sepas qué hace trampa en una prueba: un generador que deja de enviar cuando el servidor se detiene, un arranque frío mezclado con el régimen estable o una duración demasiado corta para ver una fuga.

## Cómo funciona

Según [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md):

Una **prueba de resistencia** (soak) mantiene una carga moderada durante horas para encontrar lo que se acumula: fugas de memoria o de conexiones, archivos que no se cierran, logs que llenan el disco, caches que crecen sin límite. En el simulador, una de cada 5 000 solicitudes pierde una conexión de un pool de 50. A 60 solicitudes por segundo, en cinco minutos se pierden unas tres conexiones (el 6 % del pool), una prueba de carga de esa duración no lo vería, y el pool se agota a los 67 minutos tras 241 135 solicitudes.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md):

El equipo prepara el cierre de plazo con un plan de tres pruebas. La de carga reproduce el perfil del cierre anterior con generador abierto, 60 solicitudes por segundo y cinco minutos tras descartar los dos primeros.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La memoria sube en un día y no en cinco minutos** — causa: falta prueba de resistencia. Corrección: ejecutar horas con recursos instrumentados. ([SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **prueba de resistencia** (soak) mantiene una carga moderada durante horas para encontrar lo que se acumula: fugas de memoria o de conexiones, archivos que no se cierran, logs que llenan el disco, caches que crecen sin límite. ([SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Omisión coordinada](../o/omision-coordinada.md), [Prueba de carga](./prueba-de-carga.md), [Prueba de estrés](./prueba-de-estres.md), [Prueba de pico](./prueba-de-pico.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Grafana k6: tipos de pruebas](https://grafana.com/docs/k6/latest/testing-guides/test-types/) — carga, estrés, pico y resistencia; autoridad: documentación de la herramienta.
- [Schroeder, Wierman y Harchol-Balter, «Open versus closed: a cautionary tale»](https://www.usenix.org/legacy/event/nsdi06/tech/full_papers/schroeder/schroeder.pdf) — modelos abierto y cerrado; autoridad: artículo de NSDI 2006.
- [wrk2](https://github.com/giltene/wrk2) — omisión coordinada y su corrección; autoridad: repositorio del autor de la herramienta.
- [Google SRE: Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) — sobrecarga que se amplifica y descarte de trabajo; autoridad: Google, libro de ingeniería de confiabilidad.
- [Python: heapq](https://docs.python.org/3/library/heapq.html) — cola de prioridad usada en el simulador; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Prueba de regresión](./prueba-de-regresion.md) · [Prueba de restauración →](./prueba-de-restauracion.md)
