# GraphQL

[↑ Glosario](../../README.md) · [← Granularidad de los enlaces](./granularidad-de-los-enlaces.md) · [Gravedad →](./gravedad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Lenguaje de consulta con sistema de tipos en el que el cliente elige los campos que recibe.

Definición de trabajo de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md).

## Por qué importa

En [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), el tema «GraphQL» importa porque deja al cliente elegir campos y desplaza al servidor el control del coste.

## Cómo funciona

Según [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), en la sección «GraphQL»:

GraphQL expone un sistema de tipos y un único punto de entrada; el cliente escribe una consulta que elige campos y relaciones. Esto reduce el sobreenvío de datos y los viajes de ida y vuelta, y traslada responsabilidad al servidor: una consulta anidada puede costar miles de llamadas. La especificación no fija límites de profundidad ni de coste, de modo que las guías de seguridad recomiendan imponerlos. El contrato no es solo el esquema de tipos sino también las reglas de coste que el servidor aplica.

## Ejemplo

Ejemplo de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) (sección «Ejemplo profesional»):

En la plataforma, el documento OpenAPI de la API de entregas y el documento AsyncAPI de los eventos viven en el repositorio, versionados con el código. Un linter de integración continua verifica la forma (identificadores únicos, parámetros, respuestas de error). Una prueba contractual (`SE-166`) comprueba que el servicio responda lo que el documento promete, incluida la respuesta 201 de `crearEntrega`. El documento de eventos declara la semántica de entrega («al menos una vez», sin orden global) y exige identificador y versión en cada mensaje; los consumidores son idempotentes por diseño. La política de GraphQL, donde se use, fija profundidad máxima y coste máximo.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una consulta GraphQL pequeña tarda segundos** — causa: no hay límite de profundidad ni de coste. Corrección: fijar profundidad máxima, coste máximo y paginación. ([SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md))

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún linter real ni un servidor GraphQL o un broker, la medición de resolvedores es un cálculo y las tasas de duplicado y reordenamiento son supuestos. La siguiente clase pregunta cómo cambia un contrato sin romper a quien ya lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Tipo](../t/tipo.md), [Consumidor idempotente](../c/consumidor-idempotente.md), [Contrato de interfaz](../c/contrato-de-interfaz.md), [Evento](../e/evento.md), [OpenAPI](../o/openapi.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (5 clases más lo mencionan; las que más):

[SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-164](../../../classes/part-13-especificaciones-contratos-y-modelos/se-164-compatibilidad-versionado-y-evolucion-de-contratos/README.md), [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GraphQL Specification](https://spec.graphql.org/) — lenguaje, tipos y ejecución; autoridad: GraphQL Foundation.
- [OWASP: GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) — límites de profundidad y de coste y otras defensas; autoridad: OWASP.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — formato de descripción de interfaces HTTP; autoridad: OpenAPI Initiative.
- [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest) — descripción de interfaces basadas en mensajes; autoridad: AsyncAPI Initiative.
- [CloudEvents](https://cloudevents.io/) — envoltura estándar de eventos con identificador, tipo y origen; autoridad: CNCF.

---

[↑ Glosario](../../README.md) · [← Granularidad de los enlaces](./granularidad-de-los-enlaces.md) · [Gravedad →](./gravedad.md)
