# Prueba de pico

[↑ Glosario](../../README.md) · [← Prueba de integración](./prueba-de-integracion.md) · [Prueba de recorrido →](./prueba-de-recorrido.md)

> **Tipo:** práctica o técnica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md)

## Definición

Ráfaga súbita de carga para medir la supervivencia y el tiempo de recuperación.

Definición de trabajo de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md).

## Por qué importa

La clase donde se define, [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md), existe con este propósito: la clase existe para que elijas la forma de carga que responde a tu pregunta (cuánto aguanta en régimen, dónde se rompe, cómo se recupera de un pico, qué se degrada con las horas) y para que sepas qué hace trampa en una prueba: un generador que deja de enviar cuando el servidor se detiene, un arranque frío mezclado con el régimen estable o una duración demasiado corta para ver una fuga.

## Cómo funciona

Según [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md):

Una **prueba de pico** aplica una ráfaga súbita y mide dos cosas: si el sistema la sobrevive y cuánto tarda en volver a la normalidad. El segundo número es el que suele sorprender. Un pico de 240 solicitudes por segundo durante 20 segundos sobre una base de 60 añade unos 3 200 solicitudes de exceso (160 por segundo de más, durante 20 s) a un sistema con apenas 20 por segundo de margen. Vaciar esa cola exige 160 segundos, más de ocho veces la duración del pico: la latencia máxima llega a 41,4 s y el p95 vuelve por debajo de 200 ms 165 s después de terminar el pico.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md):

El equipo prepara el cierre de plazo con un plan de tres pruebas. La de carga reproduce el perfil del cierre anterior con generador abierto, 60 solicitudes por segundo y cinco minutos tras descartar los dos primeros.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La prueba «aguanta» y el sistema cae en el cierre** — causa: solo se hizo prueba de carga. Corrección: añadir prueba de pico y de resistencia. ([SE-435](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-435 — Carga, estrés, picos y endurance](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-435-carga-estres-picos-y-endurance/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-434](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-434-revision-analisis-estatico-y-quality-gates/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tiempo de recuperación](../t/tiempo-de-recuperacion.md), [Ráfaga](../r/rafaga.md), [Recuperación](../r/recuperacion.md), [Omisión coordinada](../o/omision-coordinada.md), [Prueba de carga](./prueba-de-carga.md), [Prueba de estrés](./prueba-de-estres.md).
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

[↑ Glosario](../../README.md) · [← Prueba de integración](./prueba-de-integracion.md) · [Prueba de recorrido →](./prueba-de-recorrido.md)
