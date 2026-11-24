# Lector tolerante

[↑ Glosario](../../README.md) · [← Lector estricto](./lector-estricto.md) · [Lectura de la propia escritura →](./lectura-de-la-propia-escritura.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Un **lector tolerante** es un consumidor que usa los campos que conoce e ignora los demás ([SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md)). [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md) y [SE-312](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-312-proyecto-evolucion-compatible-de-un-componente/README.md) lo formulan igual; [SE-524](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-524-compatibilidad-coexistencia-y-doble-escritura/README.md) añade que aplica valores por defecto a lo ausente. Se opone al lector estricto, que rechaza cualquier campo que no esté en su esquema.

## Por qué importa

La compatibilidad no es una propiedad solo del esquema: depende de **cómo** lee el consumidor. La misma evolución (añadir un campo) es compatible o no según el lector. Cambia cómo se escriben los consumidores y cómo se prueba la evolución de un contrato.

## Cómo funciona

[SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) explica que, con un lector tolerante, **añadir un campo es compatible hacia adelante**: el lector viejo ignora el campo nuevo y sigue funcionando. Con un lector estricto, no lo es: falla ante lo desconocido. La recomendación de Fowler (la «ley de Postel» aplicada a datos: sé liberal en lo que aceptas) es leer lo que se necesita y no más.

La clase incluye un fragmento que prueba si añadir un campo opcional rompe a un lector estricto viejo, y pide predecir el resultado para el tolerante y para el estricto. El resultado esperado: el tolerante sigue funcionando; el estricto falla.

[SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) precisa que el lector tolerante **no es una excusa para no validar**: tolerar campos desconocidos no significa aceptar datos incorrectos en los campos que sí se usan. Y se complementa con valores por defecto para campos ausentes, de modo que los datos viejos (sin el campo nuevo) se lean bien (compatibilidad hacia atrás).

El equipo de la plataforma fija las reglas de evolución del evento `EntregaRecibida`: modo de compatibilidad completa, porque el log se retiene 14 días y hay consumidores que se despliegan con semanas de desfase; se permite añadir campos opcionales con valor por defecto y quitar campos opcionales; se prohíbe renombrar, cambiar tipos y volver obligatorio un campo. Los lectores deben ser tolerantes por contrato, y se verifica con una prueba que añade un campo y comprueba que los consumidores siguen funcionando.

## Ejemplo

Evento versión 1: `{id, estudiante, archivo}`. Versión 2 añade `comentario`. Un consumidor tolerante extrae `id`, `estudiante` y `archivo` e ignora `comentario`. Uno estricto, que valida contra el esquema cerrado de la versión 1, lanza un error con la versión 2 y deja de procesar eventos. (Ilustración del mecanismo de [SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md) y [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md).)

## Errores y confusiones comunes

- **«Solo agrega, no puede romper»**: rompe a lectores estrictos.
- **Tolerar datos inválidos en campos usados**: tolerancia no es falta de validación.
- **No probar con un campo nuevo.**
- **Esquemas cerrados por defecto** en bibliotecas de deserialización.

## Límites y cuándo no aplica

La tolerancia solo cubre campos añadidos; renombrar o cambiar tipos rompe igual. Si el sistema debe rechazar mensajes sospechosos (por seguridad), cierta rigidez es deseable. Y para ignorar un campo hay que saber que no es crítico: ignorar silenciosamente una restricción nueva puede ser un defecto.

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
