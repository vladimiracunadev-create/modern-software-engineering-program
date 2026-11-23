# Reloj lógico

[↑ Glosario](../../README.md) · [← Reloj de pared](./reloj-de-pared.md) · [Reloj monotónico →](./reloj-monotonico.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Contador que ordena eventos según su causalidad sin depender de la hora física de ningún dispositivo.

Definición de trabajo de [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md).

## Por qué importa

La clase donde se define, [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md), existe con este propósito: la clase existe para que diseñes el cliente para trabajar sin conexión como caso normal, elijas una estructura de datos y una política de conflicto sabiendo qué intención sacrifica cada una, y hagas que reintentar sea seguro con operaciones idempotentes.

## Cómo funciona

Según [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md):

Resultado: con desfase **0** y **1** unidades, **0,00 %** de pares invertidos; con **5**, **0,78 %**; con **30**, **7,76 %**. Hasta que el desfase supera el intervalo mínimo entre eventos, el orden es correcto; después se degrada y no avisa. Un reloj lógico con contadores por réplica ordena lo causal sin depender de ese desfase y señala lo concurrente en lugar de ordenarlo por una hora.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md):

El equipo del cliente documenta una política de conflicto por tipo de dato. Los comentarios son un conjunto con marcas únicas: nunca se pierde uno añadido, a costa de que una baja concurrente a un alta no gane. El título del borrador usa último escritor con un contador por réplica para decidir y guarda la versión descartada 30 días con un aviso. El contador de revisiones se calcula a partir del registro de operaciones, no se sincroniza como número.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md)) son:

- **Un comentario añadido sin conexión desaparece** — causa: se copió el estado de la última réplica en llegar. Corrección: fusionar operaciones y usar una estructura que conserve altas.
- **Un contador cuenta la mitad de los cambios** — causa: se sincroniza el valor con «el último gana». Corrección: contador por réplica o recalcular del registro de operaciones.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un reloj lógico con contadores por réplica ordena lo causal sin depender de ese desfase y señala lo concurrente en lugar de ordenarlo por una hora. ([SE-260](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-256](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-256-almacenamiento-local-y-sincronizacion/README.md), [SE-259](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-259-actualizaciones-tiendas-y-distribucion-empresarial/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contador](../c/contador.md), [Dispositivo](../d/dispositivo.md), [Evento](../e/evento.md), [Conflicto](../c/conflicto.md), [Idempotencia](../i/idempotencia.md), [Offline-first](../o/offline-first.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-388](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-388-tiempo-relojes-y-orden-parcial/README.md), [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Shapiro et al., «Conflict-Free Replicated Data Types» (SSS 2011)](https://doi.org/10.1007/978-3-642-24550-3_29) — tipos de datos replicados que convergen; autoridad: Lecture Notes in Computer Science.
- [Lamport, «Time, clocks, and the ordering of events in a distributed system» (CACM, 1978)](https://doi.org/10.1145/359545.359563) — relojes lógicos y orden causal; autoridad: Communications of the ACM.
- [Kleppmann et al., «Local-first software» (Onward! 2019)](https://doi.org/10.1145/3359591.3359737) — propuesta de aplicaciones con datos locales primero; autoridad: ACM SIGPLAN Onward!.
- [Ink & Switch, «Local-first software»](https://www.inkandswitch.com/local-first/) — versión extendida del ensayo con siete ideales; autoridad: Ink & Switch.
- [IETF, «RFC 9110: HTTP Semantics» (métodos idempotentes)](https://www.rfc-editor.org/rfc/rfc9110) — definición de idempotencia de los métodos HTTP; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Reloj de pared](./reloj-de-pared.md) · [Reloj monotónico →](./reloj-monotonico.md)
