# Decisión humana abierta

[↑ Glosario](../../README.md) · [← Decisión declarada](./decision-declarada.md) · [Decisión irreversible (de un sentido) →](./decision-irreversible-de-un-sentido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Una **decisión humana abierta** es un punto que el contrato o el paquete no puede cerrar y que debe tomar una persona con autoridad; se registra con responsable, fecha y la evidencia que la modificaría. Es el sentido de [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) y de [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md). Es lo contrario de una duda informal: tiene nombre, plazo y criterio de cierre.

## Por qué importa

Cambia si un paquete de trabajo se declara cerrado con honestidad. Según [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), lo que ninguna herramienta decide queda con nombre y fecha; sin ellas, el paquete aparenta estar cerrado cuando solo está silenciado. El defecto que previene es la decisión tomada por omisión: el primero que implementa el caso resuelve sin saber que decidía.

## Cómo funciona

El paquete lista lo que sigue pendiente. En el cliente de sincronización de [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md): qué pérdida de intención es aceptable en un conflicto, qué plazo de desconexión se tolera, qué capacidades se excluyen en una plataforma, qué telemetría se considera aceptable. Cada decisión abierta lleva tres campos: un **responsable** (persona con autoridad), una **fecha** y la **evidencia** que la cerraría o la cambiaría.

La razón de la tercera es que una decisión abierta no es una pregunta retórica: se cierra con un dato o una prueba concretos (por ejemplo, la frecuencia observada de conflictos). Así, la decisión se revisa cuando llega esa evidencia en lugar de repetirse por opinión. [SE-228](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) añade el criterio de qué entra aquí: lo que el paquete no puede resolver por sí mismo, no lo que el equipo no tuvo tiempo de resolver.

## Ejemplo

El equipo del cliente de entregas arma su paquete con una carpeta por artefacto y un índice con identificadores. Una prueba de extremo a extremo desconecta el cliente, hace cuarenta ediciones y reconecta con un canal que pierde y duplica. Aun con la prueba verde queda abierta «cuánto tiempo sin conexión se tolera antes de pedir resincronizar»: se registra con responsable, fecha y el dato (distribución de desconexiones reales) que la resolvería.

## Errores y confusiones comunes

- **Dejarla en un comentario o en la memoria de alguien.** Sin responsable ni fecha, se pierde.
- **Confundirla con un defecto.** Un defecto se corrige; una decisión abierta se decide.
- **Registrar lo que el equipo puede resolver.** Debe ser lo que el paquete no puede decidir.
- **Cerrarla sin evidencia.** Se vuelve opinión y se reabre.

## Límites y cuándo no aplica

Las clases la presentan dentro de proyectos con paquete de entrega; en trabajo pequeño puede bastar una nota en el ADR. Una lista larga de decisiones abiertas es señal de que el paquete no está listo para entregarse, no de que esté bien documentado. Los experimentos de [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) usan datos sintéticos y no sustituyen la evidencia real que cada decisión debe nombrar.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](../c/contrato.md), [Evidencia](../e/evidencia.md), [Paquete](../p/paquete.md), [Resolver](../r/resolver.md), [Bucle de contraejemplos](../b/bucle-de-contraejemplos.md), [Cláusula completa](../c/clausula-completa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md).

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

[↑ Glosario](../../README.md) · [← Decisión declarada](./decision-declarada.md) · [Decisión irreversible (de un sentido) →](./decision-irreversible-de-un-sentido.md)
