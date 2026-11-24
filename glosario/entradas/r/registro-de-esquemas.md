# Registro de esquemas

[↑ Glosario](../../README.md) · [← Registro de decisiones](./registro-de-decisiones.md) · [Registro de eventos →](./registro-de-eventos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md)

## Definición

Un **registro de esquemas** es un servicio que guarda las versiones de cada esquema y verifica su compatibilidad antes de aceptar una nueva ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)). Convierte una regla de compatibilidad que vivía en un documento en una comprobación automática.

## Por qué importa

En un sistema de mensajes, productores y consumidores evolucionan por separado. Un cambio incompatible de un productor rompe a los consumidores que no se han actualizado. La decisión que cambia es dónde se detecta el problema: en la integración continua del productor, antes de publicar, y no en producción cuando un consumidor falla.

## Cómo funciona

[SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) describe el mecanismo en tres piezas:

1. **Versiones**: el registro guarda cada versión de cada esquema.
2. **Modo de compatibilidad configurado por tema**: hacia atrás (los lectores nuevos leen datos viejos), hacia adelante (los lectores viejos leen datos nuevos) o ambos.
3. **Verificación previa**: antes de aceptar una versión nueva, el registro comprueba que respete el modo configurado; si no, la rechaza.

El mensaje lleva el **identificador de su esquema** y el lector lo recupera del registro para interpretar los datos. Así la regla pasa de estar en un documento a ser una comprobación que se ejecuta en la integración continua del productor: un cambio incompatible no llega a publicarse.

La clase es explícita con su alcance. El registro **solo conoce la forma**, no el sentido: un campo renombrado o un cambio de unidad que conserve el tipo pasa la verificación y rompe a los consumidores (cambio semántico). Tampoco sustituye el ensayo con los consumidores reales (por ejemplo, la prueba de contrato). Pero cierra la mayor parte de los errores de forma. Se relaciona con el contrato de datos y con el patrón de expandir y contraer para cambios incompatibles.

## Ejemplo

El productor quiere eliminar un campo obligatorio del esquema de `entrega`. El registro, configurado en compatibilidad hacia atrás, rechaza la versión porque los lectores nuevos no podrían leer los datos viejos que tienen ese campo. El productor lo hace opcional primero, espera la migración y luego lo retira en una fase posterior. Razonamiento de [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md).

## Errores y confusiones comunes

- **Los cambios incompatibles llegan a producción**: no hay verificación automática de compatibilidad; se corrige con un registro de esquemas o una prueba de contrato en la integración continua.
- **Creer que el registro valida el significado**: solo valida la forma.
- **Elegir un modo de compatibilidad sin saber quién despliega primero**: hacia atrás o hacia adelante dependen del orden de actualización.
- **No guardar el identificador del esquema en el mensaje**.

## Límites y cuándo no aplica

[SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) precisa que no usó Avro, Protocol Buffers, JSON Schema ni un registro real: los esquemas, los lectores, el despliegue en cinco pasos del 20 % y el 6 % de valores nuevos son construcciones del autor, y los resultados no se extrapolan a ningún formato ni producto. Para un sistema con un solo productor y un solo consumidor que se despliegan juntos, el registro añade infraestructura que puede no compensar.

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
