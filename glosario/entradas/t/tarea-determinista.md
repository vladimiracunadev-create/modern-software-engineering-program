# Tarea determinista

[↑ Glosario](../../README.md) · [← Tarea de regresión](./tarea-de-regresion.md) · [Tarea útil →](./tarea-util.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Tarea que produce la misma salida para la misma entrada, sin depender de la hora ni de la aleatoriedad.

Definición de trabajo de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md).

## Por qué importa

La clase donde se define, [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md), existe con este propósito: la clase existe para que sustituyas la promesa imposible de «exactamente una vez» por una que sí puedes cumplir: efecto único sobre el estado, logrado con operaciones idempotentes y con claves que permiten reconocer un duplicado, y para que diseñes el procesamiento por lotes y por mensajes de modo que un reintento sea una repetición inofensiva y no una segunda verdad.

## Cómo funciona

Según [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

Anexar deja 9 filas repetidas con una tarea determinista, que al menos son iguales, y 14 con una aleatoria, de las cuales 13 tienen dos valores distintos para la misma tarea: dos verdades en la salida. Escribir por clave deja 200 filas siempre; con una tarea aleatoria conserva el último valor, que es una sola verdad, aunque no la misma que el primer intento.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md):

El equipo del panel clasifica las operaciones. «Marcar una entrega como recibida» pasa de «sumar uno» a «insertar la entrega con su identificador», con clave primaria: el contador del panel se calcula contando filas, de modo que un mensaje repetido no cambia nada. «Enviar el acuse por correo» no es idempotente por naturaleza: lleva una clave `acuse-<entrega>` guardada con el resultado en la misma transacción que marca el envío, con una retención de 7 días justificada por el retraso máximo observado de reentregas.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)) son:

- **Contadores por encima de lo real** — causa: mensajes reentregados aplicados dos veces. Corrección: clave en la misma transacción que el efecto.
- **Contadores por debajo de lo real** — causa: confirmar antes de aplicar. Corrección: aplicar y recordar, luego confirmar.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna cola de mensajes, ningún sistema de procesamiento por lotes ni un servicio de pagos: las caídas del 5 %, el retraso lognormal de los duplicados y las 200 tareas son construcciones del autor. La siguiente clase usa estas piezas repetibles para repartirlas: replicación, partición y balanceo.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md), [SE-391](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-391-consenso-eleccion-y-coordinacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tarea](./tarea.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Efecto único](../e/efecto-unico.md), [Huella del cuerpo](../h/huella-del-cuerpo.md), [Idempotencia](../i/idempotencia.md), [Operaciones idempotentes](../o/operaciones-idempotentes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Helland, «Idempotence is not a medical condition»](https://doi.org/10.1145/2181796.2187821) — diseño de aplicaciones tolerantes a repeticiones; autoridad: artículo de ACM Queue (2012).
- [RFC 9110: semántica de HTTP](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes; autoridad: IETF.
- [Stripe: idempotencia](https://stripe.com/blog/idempotency) — claves enviadas por el cliente; autoridad: Stripe.
- [IETF: cabecera Idempotency-Key](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) — borrador de estandarización; autoridad: IETF (borrador).
- [Dean y Ghemawat, «MapReduce»](https://doi.org/10.1145/1327452.1327492) — reintento de tareas y salida atómica; autoridad: artículo original.

---

[↑ Glosario](../../README.md) · [← Tarea de regresión](./tarea-de-regresion.md) · [Tarea útil →](./tarea-util.md)
