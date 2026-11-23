# Validador de presencia

[↑ Glosario](../../README.md) · [← Validador de paquete](./validador-de-paquete.md) · [Validador de referencias →](./validador-de-referencias.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md)

## Definición

Comprobación automática de que ciertos campos existen y no están vacíos; no juzga su contenido.

Definición de trabajo de [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md).

## Por qué importa

En [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), el tema «Validación del paquete» importa porque un validador de presencia detecta lo que falta, no lo que está mal.

## Cómo funciona

[SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) no desarrolla este término en una sección propia. Lo usa como pieza de su tema: Las definiciones son operativas para el cliente de la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

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

- **Prerrequisito:** las clases previas [SE-253](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-253-modelos-de-aplicacion-movil-y-de-escritorio/README.md), [SE-263](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-263-taller-adaptar-un-producto-a-dos-plataformas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación automática](../c/comprobacion-automatica.md), [Clave de idempotencia](../c/clave-de-idempotencia.md), [Decisión abierta](../d/decision-abierta.md), [Decisión humana abierta](../d/decision-humana-abierta.md), [Paquete trazable](../p/paquete-trazable.md), [Registro de operaciones](../r/registro-de-operaciones.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-264 — Proyecto: cliente multiplataforma con sincronización](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.

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

[↑ Glosario](../../README.md) · [← Validador de paquete](./validador-de-paquete.md) · [Validador de referencias →](./validador-de-referencias.md)
