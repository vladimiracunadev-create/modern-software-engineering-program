# Corte

[↑ Glosario](../../README.md) · [← Corrutina](./corrutina.md) · [Corte mínimo →](./corte-minimo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Interrupción de un flujo antes de un paso, que deja hecho lo anterior y sin hacer lo siguiente.

Definición de trabajo de [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md).

## Por qué importa

En [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), el tema «Fallos parciales de un flujo» importa porque el corte y la respuesta perdida piden defensas distintas.

## Cómo funciona

Según [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md):

Un flujo con efectos (reservar cupo, guardar entrega, cobrar una penalización, avisar, marcar completa) puede interrumpirse de dos maneras distintas. En un **corte**, el proceso se detiene antes de un paso: los efectos anteriores quedan hechos y los siguientes no. En una **respuesta perdida**, el paso se ejecutó pero el cliente no lo sabe y repite el flujo. El corte pide atomicidad o compensación (deshacer lo hecho); la respuesta perdida pide idempotencia (que repetir no cambie el estado). Confundirlos lleva a arreglar uno y dejar el otro: un cerrojo no ayuda a una respuesta perdida y una clave de idempotencia no deshace un corte.

Según [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md):

El equipo del reporte del lunes sigue el procedimiento del taller. Para el cupo duplicado, escribe el modelo de tres pasos, reproduce con el calendario mínimo de seis pasos y descubre que otra ruta (la importación masiva) también leía y escribía el cupo sin la comprobación atómica. La corrección reemplaza «leer y escribir» por `UPDATE cupo SET libres = libres - 1 WHERE libres > 0` y comprueba el número de filas afectadas; la regresión ejecuta el calendario mínimo y 200 semillas del planificador y falla antes del cambio.

## Ejemplo

Ejemplo de [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) (sección «Ejemplo profesional»):

El equipo del reporte del lunes sigue el procedimiento del taller. Para el cupo duplicado, escribe el modelo de tres pasos, reproduce con el calendario mínimo de seis pasos y descubre que otra ruta (la importación masiva) también leía y escribía el cupo sin la comprobación atómica. La corrección reemplaza «leer y escribir» por `UPDATE cupo SET libres = libres - 1 WHERE libres > 0` y comprueba el número de filas afectadas; la regresión ejecuta el calendario mínimo y 200 semillas del planificador y falla antes del cambio.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se arregla el corte con idempotencia** — causa: se confundió con la respuesta perdida. Corrección: compensación o atomicidad para el corte. ([SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El corte pide atomicidad o compensación (deshacer lo hecho); la respuesta perdida pide idempotencia (que repetir no cambie el estado). ([SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-386](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-386-memoria-compartida-locks-y-condiciones-de-carrera/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), [SE-394](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-394-caos-controlado-y-pruebas-de-distribucion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Flujo](../f/flujo.md), [Hecho](../h/hecho.md), [Interrupción](../i/interrupcion.md), [Prueba de regresión](../p/prueba-de-regresion.md), [Reproductor mínimo](../r/reproductor-minimo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-395 — Taller: reproducir una carrera y un fallo parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (69 clases más lo mencionan; las que más):

[SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-176](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-176-responsive-adaptativo-y-preferencias-del-usuario/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-148](../../../classes/part-12-ingenieria-de-requisitos/se-148-casos-de-uso-historias-y-job-stories/README.md), [SE-359](../../../classes/part-29-datos-persistencia-y-recuperacion/se-359-taller-corregir-una-migracion-peligrosa/README.md), [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Uber](../../../casos/exito/uber.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md), [TSB Bank](../../../casos/fallo/tsb.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Zeller y Hildebrandt, «Simplifying and isolating failure-inducing input»](https://doi.org/10.1109/32.988498) — reducción por delta; autoridad: artículo original (2002).
- [Musuvathi et al., CHESS](https://www.usenix.org/legacy/event/osdi08/tech/full_papers/musuvathi/musuvathi.pdf) — planificador controlado y exploración sistemática; autoridad: artículo de OSDI (2008).
- [rr: grabación y reproducción](https://rr-project.org/) — reproducción determinista de ejecuciones; autoridad: proyecto rr.
- [Helland, «Idempotence is not a medical condition»](https://doi.org/10.1145/2181796.2187821) — reintentos y respuesta perdida; autoridad: artículo de ACM Queue (2012).
- [Python: unittest](https://docs.python.org/3/library/unittest.html) — pruebas de regresión ejecutables; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Corrutina](./corrutina.md) · [Corte mínimo →](./corte-minimo.md)
