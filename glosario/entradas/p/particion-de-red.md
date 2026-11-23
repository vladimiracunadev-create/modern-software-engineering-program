# Partición de red

[↑ Glosario](../../README.md) · [← Partición](./particion.md) · [Particiones y fronteras →](./particiones-y-fronteras.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md)

## Definición

Situación en que dos grupos de nodos no pueden comunicarse entre sí.

Definición de trabajo de [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md).

## Por qué importa

La clase donde se define, [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md), existe con este propósito: la clase existe para que conviertas «CAP» de una etiqueta en una decisión por operación: durante una partición de la red, qué peticiones se rechazan para no mostrar datos viejos, cuáles se aceptan y se reconcilian después, qué cuórum de lectura y escritura se exige y qué tipos de datos se pueden fusionar sin perder trabajo.

## Cómo funciona

[SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md):

El equipo clasifica las operaciones de la plataforma. Registrar una entrega: durante una partición, la réplica sin mayoría **rechaza** con un mensaje que indica reintentar en minutos, porque un acuse de recibo falso es peor que una espera; la escritura exige un cuórum de 2 de 3. Mostrar el listado de entregas propias: se permite **aceptar** con datos de hasta cinco minutos de antigüedad y con una etiqueta de «última actualización». El contador de visitas del curso es un contador por réplica que se suma al volver la red.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)) son:

- **Acuses de entrega sin registro tras una partición** — causa: reconciliación que descarta el lado perdedor. Corrección: conservar conflictos o fusionar con tipos adecuados.
- **Servicio caído para un grupo de estudiantes** — causa: rechazo por falta de mayoría sin aviso claro. Corrección: mensaje honesto y reintento guiado.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos en Windows y Ubuntu (WSL2) con resultados idénticos. No se probó ninguna base de datos distribuida ni se verificó la linealizabilidad de ningún sistema: la partición de una réplica, la carga y la regla de reconciliación son construcciones del autor, y los cuórums se enumeraron sobre un modelo sin retrasos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-389](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-389-fallos-parciales-y-modelos-de-red/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Consistencia eventual](../c/consistencia-eventual.md), [CRDT](../c/crdt.md), [Cuórum](../c/cuorum.md), [Linealizabilidad](../l/linealizabilidad.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-390 — Consistencia, disponibilidad y particiones](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-390-consistencia-disponibilidad-y-particiones/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-355](../../../classes/part-29-datos-persistencia-y-recuperacion/se-355-replicacion-particion-y-distribucion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

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

[↑ Glosario](../../README.md) · [← Partición](./particion.md) · [Particiones y fronteras →](./particiones-y-fronteras.md)
