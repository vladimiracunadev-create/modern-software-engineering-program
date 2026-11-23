# Lector tolerante

[↑ Glosario](../../README.md) · [← Lector estricto](./lector-estricto.md) · [Lectura de la propia escritura →](./lectura-de-la-propia-escritura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Consumidor que usa los campos que conoce e ignora los demás.

Definición de trabajo de [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md): Consumidor que ignora los campos que no conoce.
- En [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md): Lector que ignora lo desconocido y aplica valores por defecto a lo ausente.
- En [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md): Consumidor que extrae lo que necesita de un mensaje e ignora los campos que no conoce.
- En [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md): Consumidor que lee solo los campos que necesita y no falla ante los campos que no conoce.

## Por qué importa

En [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), el tema «Lector tolerante y estricto» importa porque la misma evolución es compatible o no según cómo lee el consumidor.

## Cómo funciona

Según [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md):

La compatibilidad no es una propiedad solo del esquema: depende de **cómo** lee el consumidor. Un **lector tolerante** usa los campos que conoce e ignora los demás (la recomendación de Fowler); un **lector estricto** rechaza cualquier campo que no esté en su esquema. Con un lector tolerante, añadir un campo es compatible hacia adelante; con uno estricto, no lo es. El lector tolerante no es una excusa para no validar: debe comprobar tipo y rango de los campos que sí usa, y no debe confiar en que un campo desconocido sea inocuo si lo reenvía a otro sistema. La regla práctica es escribir lectores tolerantes con los campos que necesitan y estrictos con sus tipos.

Según [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md):

El equipo de la plataforma fija las reglas de evolución de `EntregaRecibida`. **Modo del registro:** compatibilidad completa, porque el log se retiene 14 días y hay consumidores que se despliegan con semanas de desfase. **Reglas:** se permite añadir campos opcionales con valor por defecto y quitar campos opcionales; se prohíbe renombrar, cambiar tipos y volver obligatorio un campo. **Lectores:** todos los consumidores usan lectores tolerantes sobre los campos que necesitan y validan su tipo; los estados desconocidos se conservan y se derivan a una cola de revisión con una alarma.

## Ejemplo

Ejemplo de [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) (sección «Ejemplo mínimo»):

El fragmento prueba si añadir un campo opcional rompe a un lector estricto viejo. Antes de ejecutarlo, predice el resultado para el lector tolerante y para el estricto.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un consumidor viejo rechaza mensajes nuevos** — causa: lector estricto frente a un campo añadido. Corrección: lector tolerante para campos desconocidos. ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md))
- **Un cambio «compatible» pierde datos** — causa: el lector tolerante usa valores por defecto. Corrección: comprobar contenido y registrar los campos ausentes. ([SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md))
- **Un esquema exacto alarma por cada campo añadido** — causa: mide la forma y no el uso. Corrección: usar lectores tolerantes y contratos. ([SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **lector tolerante** usa los campos que conoce e ignora los demás (la recomendación de Fowler); un **lector estricto** rechaza cualquier campo que no esté en su esquema. ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor por defecto](../v/valor-por-defecto.md), [Valor](../v/valor.md), [Ampliar, migrar y contraer](../a/ampliar-migrar-y-contraer.md), [Compatibilidad hacia adelante](../c/compatibilidad-hacia-adelante.md), [Compatibilidad hacia atrás](../c/compatibilidad-hacia-atras.md), [Compatibilidad hacia atrás y hacia adelante](../c/compatibilidad-hacia-atras-y-hacia-adelante.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-164 — Compatibilidad, versionado y evolución de contratos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.
- [SE-312 — Proyecto: evolución compatible de un componente](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-340 — Microservicios y sus costes reales](../../../classes/part-28-estilos-arquitectonicos/se-340-microservicios-y-sus-costes-reales/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-380 — Compatibilidad de esquemas y registros](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-441 — Compatibilidad, portabilidad e interoperabilidad](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-524 — Compatibilidad, coexistencia y doble escritura](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-381](../../../classes/part-31-integracion-eventos-y-mensajeria/se-381-anti-corruption-layers-y-traduccion-de-modelos/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-343](../../../classes/part-28-estilos-arquitectonicos/se-343-data-mesh-y-propiedad-de-los-datos/README.md).

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

[↑ Glosario](../../README.md) · [← Lector estricto](./lector-estricto.md) · [Lectura de la propia escritura →](./lectura-de-la-propia-escritura.md)
