# Ocurrió antes de

[↑ Glosario](../../README.md) · [← Obsolescencia](./obsolescencia.md) · [ODD →](./odd.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Relación de orden parcial entre sucesos definida por el orden en un proceso y por el envío y la recepción de mensajes.

Definición de trabajo de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md).

## Por qué importa

La clase donde se define, [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), existe con este propósito: la clase existe para que dejes de usar la hora como si fuera un orden: que sepas cuándo basta un reloj monotónico para medir una duración, cuándo una marca de tiempo de pared ordena mal los sucesos de dos máquinas y qué ofrece cada reloj lógico (Lamport, vectorial, híbrido) para decidir qué ocurrió antes de qué, y qué sucesos son simplemente concurrentes.

## Cómo funciona

Según [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

Lamport definió la relación «ocurrió antes de» sin usar relojes: un suceso ocurre antes que otro si están en el mismo proceso en ese orden, o si uno es el envío de un mensaje y el otro su recepción, o si hay una cadena de estas relaciones. Dos sucesos que no están relacionados por ninguna cadena son **concurrentes**: ninguno pudo influir en el otro, y que uno tenga una hora anterior no significa nada. Es un **orden parcial**: algunos pares están ordenados y otros no. La consecuencia práctica es que preguntar «¿cuál fue primero?» puede tener como respuesta correcta «ninguno». Un sistema que fuerza una respuesta decide por azar, y si lo hace al sincronizar dos réplicas descarta una escritura.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md):

El equipo de calificaciones separa tres usos del tiempo. Las expiraciones de sesión y los tiempos límite usan el reloj monotónico de cada servidor. Las marcas que ve el estudiante («entregado el 12 de noviembre a las 23:58») usan la hora de pared del servidor que recibió la entrega, registrada como dato y no usada para decidir.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md)) son:

- **Una escritura reciente pierde frente a una antigua** — causa: comparación de marcas de pared entre nodos. Corrección: vector o reloj híbrido.
- **Duraciones negativas o enormes en el registro** — causa: duración medida con el reloj de pared. Corrección: usar el monotónico.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lamport definió la relación «ocurrió antes de» sin usar relojes: un suceso ocurre antes que otro si están en el mismo proceso en ese orden, o si uno es el envío de un mensaje y el otro su recepción, o si hay una cadena de estas relaciones. ([SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-387](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-387-actores-canales-y-structured-concurrency/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Proceso](../p/proceso.md), [Relación](../r/relacion.md), [Reloj de pared](../r/reloj-de-pared.md), [Reloj monotónico](../r/reloj-monotonico.md), [Reloj vectorial](../r/reloj-vectorial.md), [Sucesos concurrentes](../s/sucesos-concurrentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-388 — Tiempo, relojes y orden parcial](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md).

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

[↑ Glosario](../../README.md) · [← Obsolescencia](./obsolescencia.md) · [ODD →](./odd.md)
