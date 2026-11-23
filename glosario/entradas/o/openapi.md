# OpenAPI

[↑ Glosario](../../README.md) · [← Open Source & InnerSource Engineer](./open-source-innersource-engineer.md) · [Operabilidad →](./operabilidad.md)

> **Tipo:** norma o marco · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Formato de descripción de interfaces HTTP con rutas, operaciones, parámetros, respuestas y esquemas.

Definición de trabajo de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md).

## Por qué importa

En [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), el tema «OpenAPI» importa porque describe operaciones HTTP con parámetros, respuestas y esquemas, y habilita documentación y generación.

## Cómo funciona

Según [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), en la sección «OpenAPI»:

Un documento OpenAPI describe una interfaz HTTP: rutas con sus operaciones, parámetros (ruta, consulta, cabecera), cuerpos y respuestas por código, con esquemas para las cargas. Su valor es doble: es legible por personas y por herramientas, que generan documentación, clientes y pruebas. Su límite es que describe, no obliga: el servicio puede responder otra cosa y el documento seguirá siendo válido. Un contrato de este tipo incluye también la semántica HTTP (métodos, códigos, cabeceras) definida en el RFC 9110, y es en esos detalles donde aparecen las discrepancias.

## Ejemplo

Ejemplo de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sección «Ejemplo profesional»):

En la plataforma, el documento OpenAPI de la API de entregas y el documento AsyncAPI de los eventos viven en el repositorio, versionados con el código. Un linter de integración continua verifica la forma (identificadores únicos, parámetros, respuestas de error). Una prueba contractual (`SE-166`) comprueba que el servicio responda lo que el documento promete, incluida la respuesta 201 de `crearEntrega`. El documento de eventos declara la semántica de entrega («al menos una vez», sin orden global) y exige identificador y versión en cada mensaje; los consumidores son idempotentes por diseño. La política de GraphQL, donde se use, fija profundidad máxima y coste máximo.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)) son:

- **Un cliente generado falla contra el servicio real** — causa: el documento y el servicio divergieron. Corrección: añadir pruebas contractuales contra el servicio y ejecutarlas en integración continua.
- **Las notificaciones salen duplicadas** — causa: el consumidor no es idempotente y la entrega es «al menos una vez». Corrección: identificador único por evento y descarte de identificadores vistos.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún linter real ni un servidor GraphQL o un broker, la medición de resolvedores es un cálculo y las tasas de duplicado y reordenamiento son supuestos. La siguiente clase pregunta cómo cambia un contrato sin romper a quien ya lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Esquema](../e/esquema.md), [Interfaz](../i/interfaz.md), [Operación](./operacion.md), [Parámetro](../p/parametro.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Contrato de interfaz](../c/contrato-de-interfaz.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-210](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-210-api-docs-ejemplos-y-contratos-publicados/README.md), [SE-252](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-252-proyecto-servicio-contractual-operable/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-165](../../../classes/part-13-especificaciones-contratos-y-modelos/se-165-spec-first-spec-anchored-y-spec-as-source/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — formato de descripción de interfaces HTTP; autoridad: OpenAPI Initiative.
- [GraphQL Specification](https://spec.graphql.org/) — lenguaje, tipos y ejecución; autoridad: GraphQL Foundation.
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest) — descripción de interfaces basadas en mensajes; autoridad: AsyncAPI Initiative.
- [CloudEvents](https://cloudevents.io/) — envoltura estándar de eventos con identificador, tipo y origen; autoridad: CNCF.
- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) — métodos, códigos de estado y cabeceras; autoridad: IETF.

---

[↑ Glosario](../../README.md) · [← Open Source & InnerSource Engineer](./open-source-innersource-engineer.md) · [Operabilidad →](./operabilidad.md)
