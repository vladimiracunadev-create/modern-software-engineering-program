# GraphQL

[↑ Glosario](../../README.md) · [← Granularidad de los enlaces](./granularidad-de-los-enlaces.md) · [Gravedad →](./gravedad.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

**GraphQL** es un lenguaje de consulta con sistema de tipos en el que el cliente elige los campos que recibe ([SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)). El servidor expone un esquema tipado y un único punto de entrada; el cliente escribe una consulta que selecciona campos y relaciones, y recibe exactamente esa forma.

## Por qué importa

Reduce el sobreenvío de datos y los viajes de ida y vuelta, y **traslada al servidor el control del coste**. Cambia una decisión de diseño de API: en lugar de que el servidor decida qué devuelve cada ruta, el cliente decide qué pide, y el servidor debe protegerse de consultas caras.

## Cómo funciona

GraphQL expone un **sistema de tipos** y un único endpoint. El cliente escribe una consulta como esta (ilustración):

```graphql
{ entrega(id: 12) { estado estudiante { nombre } archivos { nombre tamano } } }
```

y obtiene un resultado con esa forma. Frente a una API de rutas fijas, donde obtener lo mismo exige varias llamadas o recibir campos sobrantes, la ventaja es que cada cliente pide lo que necesita.

El costo está del lado del servidor. [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) advierte que una consulta anidada puede costar miles de llamadas: si se pide cada estudiante con sus entregas, cada entrega con sus archivos y cada archivo con sus versiones, la cantidad de lecturas multiplica con cada nivel. **La especificación no fija límites de profundidad ni de coste**, de modo que las guías de seguridad recomiendan imponerlos: profundidad máxima, coste máximo por consulta y paginación. Sin ellos, una consulta pequeña puede tardar segundos o servir como vector de denegación de servicio.

El contrato (el esquema) se describe y se versiona como en otros contratos de API, y se comprueba con pruebas contractuales, como el documento OpenAPI de una API REST. A diferencia de REST, la evolución suele hacerse añadiendo campos y marcando los viejos como obsoletos, en lugar de numerar versiones.

## Ejemplo

Una consulta que pide `estudiantes { entregas { archivos { versiones { ... } } } }` en un curso de 200 estudiantes con cinco entregas, tres archivos y cuatro versiones cada uno implica del orden de 200 × 5 × 3 × 4 = 12.000 lecturas de versiones. Con un límite de profundidad de tres niveles o un coste máximo, el servidor la rechaza y el cliente debe paginar. (Cálculo ilustrativo.)

## Errores y confusiones comunes

- **Una consulta pequeña tarda segundos**: no hay límite de profundidad ni de coste; corrección: fijar profundidad máxima, coste máximo y paginación ([SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)).
- **Creer que GraphQL es «más rápido» por defecto.**
- **Exponer el esquema completo sin control de autorización por campo.**
- **Confundirlo con una base de datos**: es una capa de consulta sobre cualquier fuente.

## Límites y cuándo no aplica

Para APIs simples con pocos clientes y respuestas fijas, REST con OpenAPI es más sencillo y se cachea mejor con HTTP estándar. GraphQL complica el caché, la autorización fina y el control de coste. Los límites recomendados son una decisión de cada servicio, no una propiedad del lenguaje.

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
