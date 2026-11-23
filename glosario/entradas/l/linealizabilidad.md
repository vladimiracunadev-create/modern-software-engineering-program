# Linealizabilidad

[↑ Glosario](../../README.md) · [← Línea base](./linea-base.md) · [Linter →](./linter.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Garantía de que cada operación parece ocurrir de forma instantánea entre su inicio y su fin, en un orden compatible con el tiempo real.

Definición de trabajo de [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md).

## Por qué importa

La clase donde se define, [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), existe con este propósito: la clase existe para que conviertas «CAP» de una etiqueta en una decisión por operación: durante una partición de la red, qué peticiones se rechazan para no mostrar datos viejos, cuáles se aceptan y se reconcilian después, qué cuórum de lectura y escritura se exige y qué tipos de datos se pueden fusionar sin perder trabajo.

## Cómo funciona

Según [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md):

Gilbert y Lynch formalizaron la conjetura de Brewer: en un sistema asíncrono, ante una partición de la red, un servicio no puede ser a la vez **consistente** (en el sentido de linealizable: cada lectura ve la última escritura confirmada) y **disponible** (toda petición a un nodo vivo recibe respuesta). El resultado es estrecho: habla de una partición real, de linealizabilidad y de disponibilidad total, y no dice nada sobre sistemas sin particiones ni sobre garantías más débiles. Lo que enseña es el esqueleto de la decisión: durante la partición, un lado debe rechazar (pierde disponibilidad) o aceptar y divergir (pierde consistencia). No es una elección de producto sino una decisión por operación.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md):

El equipo clasifica las operaciones de la plataforma. Registrar una entrega: durante una partición, la réplica sin mayoría **rechaza** con un mensaje que indica reintentar en minutos, porque un acuse de recibo falso es peor que una espera; la escritura exige un cuórum de 2 de 3. Mostrar el listado de entregas propias: se permite **aceptar** con datos de hasta cinco minutos de antigüedad y con una etiqueta de «última actualización». El contador de visitas del curso es un contador por réplica que se suma al volver la red.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)) son:

- **Acuses de entrega sin registro tras una partición** — causa: reconciliación que descarta el lado perdedor. Corrección: conservar conflictos o fusionar con tipos adecuados.
- **Servicio caído para un grupo de estudiantes** — causa: rechazo por falta de mayoría sin aviso claro. Corrección: mensaje honesto y reintento guiado.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El resultado es estrecho: habla de una partición real, de linealizabilidad y de disponibilidad total, y no dice nada sobre sistemas sin particiones ni sobre garantías más débiles. ([SE-390](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Instantánea](../i/instantanea.md), [Operación](../o/operacion.md), [Consistencia eventual](../c/consistencia-eventual.md), [CRDT](../c/crdt.md), [Cuórum](../c/cuorum.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Gilbert y Lynch, «Brewer's conjecture…»](https://doi.org/10.1145/564585.564601) — el resultado formal; autoridad: artículo original (2002).
- [Brewer, «CAP twelve years later»](https://doi.org/10.1109/MC.2012.37) — la elección por operación; autoridad: autor de la conjetura.
- [Abadi, «Consistency tradeoffs in modern distributed database system design»](https://doi.org/10.1109/MC.2012.33) — PACELC; autoridad: artículo original.
- [Jepsen: modelos de consistencia](https://jepsen.io/consistency) — mapa de modelos y anomalías; autoridad: Jepsen.
- [Shapiro et al., «Conflict-free replicated data types»](https://inria.hal.science/inria-00555588) — tipos que convergen sin coordinación; autoridad: artículo de los autores.

---

[↑ Glosario](../../README.md) · [← Línea base](./linea-base.md) · [Linter →](./linter.md)
