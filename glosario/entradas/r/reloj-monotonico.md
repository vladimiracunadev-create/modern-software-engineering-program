# Reloj monotónico

[↑ Glosario](../../README.md) · [← Reloj lógico](./reloj-logico.md) · [Reloj vectorial →](./reloj-vectorial.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Reloj que solo avanza y sirve para medir duraciones locales.

Definición de trabajo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md).

## Por qué importa

La clase donde se define, [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), existe con este propósito: la clase existe para que dejes de usar la hora como si fuera un orden: que sepas cuándo basta un reloj monotónico para medir una duración, cuándo una marca de tiempo de pared ordena mal los sucesos de dos máquinas y qué ofrece cada reloj lógico (Lamport, vectorial, híbrido) para decidir qué ocurrió antes de qué, y qué sucesos son simplemente concurrentes.

## Cómo funciona

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

El **reloj de pared** dice qué hora es según el sistema: se sincroniza con servidores de tiempo y por eso puede saltar, hacia adelante o hacia atrás, al corregirse. El **reloj monotónico** solo avanza: su valor absoluto no significa nada, pero la diferencia entre dos lecturas del mismo nodo es una duración fiable. La regla es sencilla: duraciones, tiempos de espera y expiraciones locales, con el monotónico; marcas que se muestran a una persona o que se comparan con un calendario, con el de pared. El segundo, además, difiere entre nodos: la sincronización por red (el protocolo NTP de la RFC 5905) tiene un error que depende de la red y puede dejar relojes a decenas o cientos de milisegundos entre sí.

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

El equipo de calificaciones separa tres usos del tiempo. Las expiraciones de sesión y los tiempos límite usan el reloj monotónico de cada servidor. Las marcas que ve el estudiante («entregado el 12 de noviembre a las 23:58») usan la hora de pared del servidor que recibió la entrega, registrada como dato y no usada para decidir. Para reconciliar las réplicas de calificaciones, cada versión de una nota lleva un vector con un contador por servidor: si los vectores son comparables, gana el posterior; si son incomparables, se conservan ambas versiones y se pide a la docente resolver, con un aviso. Se descarta «gana la marca más alta» porque el equipo midió que el desfase entre sus servidores puede superar la separación entre correcciones consecutivas.

## Ejemplo

Ejemplo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) (sección «Ejemplo profesional»):

El equipo de calificaciones separa tres usos del tiempo. Las expiraciones de sesión y los tiempos límite usan el reloj monotónico de cada servidor. Las marcas que ve el estudiante («entregado el 12 de noviembre a las 23:58») usan la hora de pared del servidor que recibió la entrega, registrada como dato y no usada para decidir. Para reconciliar las réplicas de calificaciones, cada versión de una nota lleva un vector con un contador por servidor: si los vectores son comparables, gana el posterior; si son incomparables, se conservan ambas versiones y se pide a la docente resolver, con un aviso.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md)) son:

- **Una escritura reciente pierde frente a una antigua** — causa: comparación de marcas de pared entre nodos. Corrección: vector o reloj híbrido.
- **Duraciones negativas o enormes en el registro** — causa: duración medida con el reloj de pared. Corrección: usar el monotónico.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **reloj monotónico** solo avanza: su valor absoluto no significa nada, pero la diferencia entre dos lecturas del mismo nodo es una duración fiable. ([SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Locale](../l/locale.md), [Ocurrió antes de](../o/ocurrio-antes-de.md), [Reloj de pared](./reloj-de-pared.md), [Reloj vectorial](./reloj-vectorial.md), [Sucesos concurrentes](../s/sucesos-concurrentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-094](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-094-complejidad-empirica-benchmarks-y-perfiles/README.md), [SE-006](../../../classes/part-00-ingenieria-de-software-como-profesion/se-006-evidencia-incertidumbre-y-pensamiento-critico-en-ingenieria/README.md), [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md).

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

[↑ Glosario](../../README.md) · [← Reloj lógico](./reloj-logico.md) · [Reloj vectorial →](./reloj-vectorial.md)
