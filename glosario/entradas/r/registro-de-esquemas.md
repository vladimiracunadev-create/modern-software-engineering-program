# Registro de esquemas

[↑ Glosario](../../README.md) · [← Registro de decisiones](./registro-de-decisiones.md) · [Registro de eventos →](./registro-de-eventos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Servicio que guarda versiones de esquemas y verifica su compatibilidad antes de aceptar una nueva.

Definición de trabajo de [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md).

## Por qué importa

En [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), el tema «Registro de esquemas» importa porque convierte una regla de equipo en una comprobación automática.

## Cómo funciona

Según [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), en la sección «Registro de esquemas»:

Un **registro de esquemas** guarda las versiones de cada esquema y comprueba, antes de aceptar una nueva, que respete el modo de compatibilidad configurado para ese tema. El mensaje lleva el identificador de su esquema y el lector lo recupera para interpretar los datos. Así la regla pasa de estar en un documento a ser una comprobación que se ejecuta en la integración continua del productor: un cambio incompatible no llega a publicarse. No sustituye el diseño (el registro solo conoce la forma, no el sentido de un campo renombrado) ni el ensayo con los consumidores reales, pero cierra la mayor parte de los errores de forma.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md):

El equipo de la plataforma fija las reglas de evolución de `EntregaRecibida`. **Modo del registro:** compatibilidad completa, porque el log se retiene 14 días y hay consumidores que se despliegan con semanas de desfase. **Reglas:** se permite añadir campos opcionales con valor por defecto y quitar campos opcionales; se prohíbe renombrar, cambiar tipos y volver obligatorio un campo. **Lectores:** todos los consumidores usan lectores tolerantes sobre los campos que necesitan y validan su tipo; los estados desconocidos se conservan y se derivan a una cola de revisión con una alarma.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Los cambios incompatibles llegan a producción** — causa: no hay verificación automática de compatibilidad. Corrección: registro de esquemas o prueba de contrato en la integración continua. ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md))

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó Avro, Protocol Buffers, JSON Schema ni registro de esquemas: los esquemas, los lectores, el despliegue en cinco pasos del 20 % y el 6 % de valores nuevos son construcciones del autor, y los resultados no se extrapolan a ningún formato ni producto.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-379](../../../classes/part-31-integracion-eventos-y-mensajeria/se-379-webhooks-polling-y-suscripciones/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Versión de esquema](../v/version-de-esquema.md), [Esquema](../e/esquema.md), [Guarda](../g/guarda.md), [Servicio](../s/servicio.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-366](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-366-contratos-de-datos-y-evolucion-de-esquemas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Confluent: evolución de esquemas y compatibilidad](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html) — modos de compatibilidad y su verificación en un registro; autoridad: documentación de Confluent.
- [Apache Avro: especificación](https://avro.apache.org/docs/current/specification/) — resolución de esquemas entre escritor y lector; autoridad: proyecto Apache Avro.
- [Fowler, «Tolerant Reader»](https://martinfowler.com/bliki/TolerantReader.html) — lector que ignora lo que no necesita; autoridad: autor del texto.
- [Versionado semántico](https://semver.org/) — distinguir cambios compatibles e incompatibles; autoridad: especificación del proyecto.
- [CloudEvents: especificación](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md) — tipo del evento y esquema de datos como atributos; autoridad: proyecto CloudEvents de la CNCF.

---

[↑ Glosario](../../README.md) · [← Registro de decisiones](./registro-de-decisiones.md) · [Registro de eventos →](./registro-de-eventos.md)
