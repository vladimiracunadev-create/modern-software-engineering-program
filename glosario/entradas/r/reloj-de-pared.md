# Reloj de pared

[↑ Glosario](../../README.md) · [← Relleno por lotes](./relleno-por-lotes.md) · [Reloj lógico →](./reloj-logico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Reloj que da la hora del sistema y puede ajustarse hacia atrás o adelante al sincronizarse.

Definición de trabajo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md).

## Por qué importa

En [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), el tema «Reloj de pared y monotónico» importa porque una duración negativa o una expiración errónea nacen de elegir mal.

## Cómo funciona

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

El **reloj de pared** dice qué hora es según el sistema: se sincroniza con servidores de tiempo y por eso puede saltar, hacia adelante o hacia atrás, al corregirse. El **reloj monotónico** solo avanza: su valor absoluto no significa nada, pero la diferencia entre dos lecturas del mismo nodo es una duración fiable. La regla es sencilla: duraciones, tiempos de espera y expiraciones locales, con el monotónico; marcas que se muestran a una persona o que se comparan con un calendario, con el de pared. El segundo, además, difiere entre nodos: la sincronización por red (el protocolo NTP de la RFC 5905) tiene un error que depende de la red y puede dejar relojes a decenas o cientos de milisegundos entre sí.

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

El monotónico, porque un ajuste del reloj de pared no debe acortar ni alargar la espera. Y recuerda su resolución: con 15,6 ms, un tiempo límite de 10 ms no es observable.

## Ejemplo

Ejemplo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sección «Preguntas frecuentes»):

El monotónico, porque un ajuste del reloj de pared no debe acortar ni alargar la espera. Y recuerda su resolución: con 15,6 ms, un tiempo límite de 10 ms no es observable.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Duraciones negativas o enormes en el registro** — causa: duración medida con el reloj de pared. Corrección: usar el monotónico. ([SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El monotónico, porque un ajuste del reloj de pared no debe acortar ni alargar la espera. ([SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Ocurrió antes de](../o/ocurrio-antes-de.md), [Reloj monotónico](./reloj-monotonico.md), [Reloj vectorial](./reloj-vectorial.md), [Sucesos concurrentes](../s/sucesos-concurrentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-297](../../../classes/part-24-software-especializado-y-dominios/se-297-sistemas-geoespaciales-y-temporales/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-437](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-437-perfiles-benchmarks-y-errores-de-medicion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Lamport, «Time, clocks, and the ordering of events…»](https://doi.org/10.1145/359545.359563) — orden parcial y relojes lógicos; autoridad: artículo original (1978).
- [Kulkarni et al., «Logical Physical Clocks»](https://cse.buffalo.edu/tech-reports/2014-04.pdf) — reloj híbrido; autoridad: informe técnico de los autores.
- [RFC 5905: NTP versión 4](https://www.rfc-editor.org/rfc/rfc5905) — sincronización de relojes y su error; autoridad: IETF.
- [Python: time](https://docs.python.org/3/library/time.html) — relojes y resolución; autoridad: documentación de Python.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — pérdida de escrituras con marcas de pared; autoridad: autor del libro.

---

[↑ Glosario](../../README.md) · [← Relleno por lotes](./relleno-por-lotes.md) · [Reloj lógico →](./reloj-logico.md)
