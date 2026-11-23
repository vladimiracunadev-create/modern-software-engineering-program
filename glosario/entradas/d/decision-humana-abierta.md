# Decisión humana abierta

[↑ Glosario](../../README.md) · [← Decisión declarada](./decision-declarada.md) · [Decisión irreversible (de un sentido) →](./decision-irreversible-de-un-sentido.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Punto que el contrato no cierra, registrado con responsable, fecha y evidencia que lo modificaría.

Definición de trabajo de [SE-167 — Taller: convertir intención en contrato comprobable](../../../classes/part-13-especificaciones-contratos-y-modelos/se-167-taller-convertir-intencion-en-contrato-comprobable/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-228 — Proyecto: herramienta operable multiplataforma](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-228-proyecto-herramienta-operable-multiplataforma/README.md): Punto que el paquete no puede resolver y que debe tomar una persona con autoridad.

## Por qué importa

En [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), el tema «Decisiones humanas abiertas» importa porque lo que ninguna herramienta decide queda con nombre y fecha.

## Cómo funciona

Según [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), en la sección «Decisiones humanas abiertas»:

El paquete lista lo que sigue pendiente: qué pérdida de intención es aceptable en un conflicto, qué plazo de desconexión se tolera, qué capacidades se excluyen en una plataforma, qué telemetría se considera aceptable. Cada decisión abierta tiene un responsable, una fecha y la evidencia que la cerraría; sin ellas, el paquete aparenta estar cerrado.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md):

El equipo del cliente de entregas arma el paquete con una carpeta por artefacto y un índice con identificadores. Una prueba de extremo a extremo lanza un servidor local, desconecta el cliente, hace cuarenta ediciones, reconecta con un canal que pierde y duplica y exige que el estado del servidor coincida con el esperado. Un validador comprueba presencia, enlaces entre artefactos y huellas; las mutaciones del propio paquete miden su alcance.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md)) son:

- **El servidor aplica más operaciones de las pedidas** — causa: reintento sin clave de idempotencia. Corrección: identificador único por operación y deduplicación en el servidor.
- **Se pierden operaciones tras una desconexión larga** — causa: no hay registro persistente ni reintento. Corrección: registro de operaciones en almacenamiento local y reintento.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md)) son: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): las cifras deterministas fueron idénticas y los tiempos del servidor local se informan por sistema. No se compiló, firmó ni publicó ningún cliente y no se midió ninguna persona ni dispositivo. La siguiente parte lleva el razonamiento a software embebido y de tiempo real.

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
