# Decisión abierta

[↑ Glosario](../../README.md) · [← Decidibilidad](./decidibilidad.md) · [Decisión colectiva →](./decision-colectiva.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Punto que ninguna herramienta decide y que queda registrado con responsable, fecha y la evidencia que lo cerraría.

Definición de trabajo de [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md).

## Por qué importa

La clase donde se define, [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), existe con este propósito: el proyecto existe para entregar un paquete que otra persona pueda revisar sin pedir contexto: el cliente de la plataforma de entregas con su ciclo de vida, su almacenamiento, su protocolo de sincronización con operaciones idempotentes, sus permisos, su plan de distribución y su modelo de amenazas, con evidencia medida y un validador cuyos límites se conocen.

## Cómo funciona

Según [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md):

El paquete lista lo que sigue pendiente: qué pérdida de intención es aceptable en un conflicto, qué plazo de desconexión se tolera, qué capacidades se excluyen en una plataforma, qué telemetría se considera aceptable. Cada decisión abierta tiene un responsable, una fecha y la evidencia que la cerraría; sin ellas, el paquete aparenta estar cerrado.

Según [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md):

El equipo del cliente de entregas arma el paquete con una carpeta por artefacto y un índice con identificadores. Una prueba de extremo a extremo lanza un servidor local, desconecta el cliente, hace cuarenta ediciones, reconecta con un canal que pierde y duplica y exige que el estado del servidor coincida con el esperado. Un validador comprueba presencia, enlaces entre artefactos y huellas; las mutaciones del propio paquete miden su alcance. El paquete termina con una lista de decisiones abiertas: la pérdida de intención aceptable en un conflicto del título, el plazo máximo de desconexión y las capacidades excluidas en una plataforma, cada una con responsable y fecha.

## Ejemplo

Ejemplo de [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) (sección «Ejemplo profesional»):

El equipo del cliente de entregas arma el paquete con una carpeta por artefacto y un índice con identificadores. Una prueba de extremo a extremo lanza un servidor local, desconecta el cliente, hace cuarenta ediciones, reconecta con un canal que pierde y duplica y exige que el estado del servidor coincida con el esperado. Un validador comprueba presencia, enlaces entre artefactos y huellas; las mutaciones del propio paquete miden su alcance. El paquete termina con una lista de decisiones abiertas: la pérdida de intención aceptable en un conflicto del título, el plazo máximo de desconexión y las capacidades excluidas en una plataforma, cada una con responsable y fecha.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md)) son:

- **El servidor aplica más operaciones de las pedidas** — causa: reintento sin clave de idempotencia. Corrección: identificador único por operación y deduplicación en el servidor.
- **Se pierden operaciones tras una desconexión larga** — causa: no hay registro persistente ni reintento. Corrección: registro de operaciones en almacenamiento local y reintento.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Cada decisión abierta tiene un responsable, una fecha y la evidencia que la cerraría; sin ellas, el paquete aparenta estar cerrado. ([SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Herramientas](../h/herramientas.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Decisión humana abierta](./decision-humana-abierta.md), [Paquete trazable](../p/paquete-trazable.md), [Registro de operaciones](../r/registro-de-operaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-565](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-565-de-la-intencion-a-la-especificacion-durable/README.md), [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md), [SE-167](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [IETF, «RFC 9110: HTTP Semantics»](https://www.rfc-editor.org/rfc/rfc9110) — métodos idempotentes y semántica de los reintentos; autoridad: IETF.
- [Kleppmann et al., «Local-first software» (Onward! 2019)](https://doi.org/10.1145/3359591.3359737) — datos locales, trabajo sin conexión y sincronización; autoridad: ACM SIGPLAN Onward!.
- [Shapiro et al., «Conflict-Free Replicated Data Types»](https://doi.org/10.1007/978-3-642-24550-3_29) — tipos de datos replicados que convergen; autoridad: Lecture Notes in Computer Science.
- [SQLite, «Atomic Commit In SQLite»](https://www.sqlite.org/atomiccommit.html) — transacciones atómicas del registro local; autoridad: SQLite.
- [OWASP, «MASVS»](https://mas.owasp.org/MASVS/) — requisitos de seguridad para aplicaciones móviles; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Decidibilidad](./decidibilidad.md) · [Decisión colectiva →](./decision-colectiva.md)
