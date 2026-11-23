# Bandeja de salida

[↑ Glosario](../../README.md) · [← Banda muerta](./banda-muerta.md) · [Bandera de funcionalidad →](./bandera-de-funcionalidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md)

## Definición

Tabla de eventos que se confirma en la misma transacción que el dato y que un proceso aparte aplica a otro sistema.

Definición de trabajo de [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md).

## Por qué importa

En [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md), el tema «Bandeja de salida y reproducción» importa porque convierte una escritura frágil en una reparable y ordenada.

## Cómo funciona

Según [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md):

Los **reintentos** reparan el primer tipo de fallo (el almacén responde la tercera vez) y no el segundo: reintentar no restablece el orden y puede empeorarlo si el reintento de una escritura vieja llega tras una nueva. Una **bandeja de salida** (outbox) cambia la estructura: la aplicación escribe en una sola base, y en la misma transacción registra el cambio en una tabla de eventos; un proceso aparte lee esa tabla y aplica los cambios al segundo almacén, con reintentos hasta que lo logre. Como el registro y el dato se confirman juntos, no hay estado en que uno exista sin el otro.

Según [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo sustituye la doble escritura de mejor esfuerzo por una bandeja de salida: la aplicación escribe la nota y, en la misma transacción, un evento con la clave y un número de secuencia; un reproductor aplica los eventos al almacén nuevo con reintentos y descarta los de secuencia menor. Mientras tanto, una reconciliación nocturna calcula sumas por bloques de 1 000 claves en los dos almacenes: con una tasa esperada de divergencia de unas diez entre cien mil, el costo ronda las diez mil filas por noche (lo medido en la tabla), y se complementa con una muestra aleatoria del 1 % que vigila los casos fuera de los bloques.

## Ejemplo

Ejemplo de [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo sustituye la doble escritura de mejor esfuerzo por una bandeja de salida: la aplicación escribe la nota y, en la misma transacción, un evento con la clave y un número de secuencia; un reproductor aplica los eventos al almacén nuevo con reintentos y descarta los de secuencia menor.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los almacenes difieren sin errores en los registros** — causa: la segunda escritura falla y se ignora. Corrección: bandeja de salida con reintentos y métrica de retraso. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **bandeja de salida** (outbox) cambia la estructura: la aplicación escribe en una sola base, y en la misma transacción registra el cambio en una tabla de eventos; un proceso aparte lee esa tabla y aplica los cambios al segundo almacén, con reintentos hasta que lo logre. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))
- La bandeja de salida acepta una pequeña latencia entre copias a cambio de independencia. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-523](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evento](../e/evento.md), [Proceso](../p/proceso.md), [Transacción](../t/transaccion.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md), [Doble escritura](../d/doble-escritura.md), [Lector tolerante](../l/lector-tolerante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «outbox».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Patrón Transactional Outbox](https://microservices.io/patterns/data/transactional-outbox.html) — evento confirmado con el dato; autoridad: catálogo de patrones de microservicios.
- [Kleppmann, «Designing Data-Intensive Applications»](https://dataintensive.net/) — consistencia, orden y registros de cambios; autoridad: libro de referencia (ISBN 9781449373320).
- [Fowler, «TolerantReader»](https://martinfowler.com/bliki/TolerantReader.html) — lectura tolerante a cambios de formato; autoridad: autor del texto.
- [Hyrum's Law](https://www.hyrumslaw.com/) — dependencia de comportamientos observables; autoridad: autor de la observación.

---

[↑ Glosario](../../README.md) · [← Banda muerta](./banda-muerta.md) · [Bandera de funcionalidad →](./bandera-de-funcionalidad.md)
