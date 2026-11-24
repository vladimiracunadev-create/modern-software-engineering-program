# OpenAPI

[↑ Glosario](../../README.md) · [← Open Source & InnerSource Engineer](./open-source-innersource-engineer.md) · [Operabilidad →](./operabilidad.md)

> **Tipo:** norma o marco · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

**OpenAPI** es un formato de descripción de interfaces HTTP: rutas con sus operaciones, parámetros, respuestas por código y esquemas de las cargas ([SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)). Un documento OpenAPI es un contrato legible por personas y por herramientas. Su compañero para interfaces basadas en eventos es AsyncAPI.

## Por qué importa

Convierte la interfaz en un artefacto que se puede versionar, revisar y verificar, en lugar de un acuerdo oral o un texto en un wiki. Habilita documentación generada, clientes generados y pruebas. Cambia una decisión de diseño: la descripción de la API se mantiene junto al código y se comprueba contra él.

## Cómo funciona

El documento enumera cada ruta y operación con sus parámetros (de ruta, consulta, cabecera), cuerpos y respuestas por código de estado, con esquemas para las cargas. Como es estructurado, una herramienta puede validar su forma, generar documentación, producir clientes en distintos lenguajes y derivar pruebas.

[SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) subraya su **límite central: describe, no obliga**. El servicio puede responder otra cosa y el documento seguirá siendo válido: documento y servicio pueden divergir sin que ninguna herramienta lo advierta. La corrección es la **prueba contractual**: una comprobación en integración continua que verifica que el servicio responde lo que el documento promete ([SE-166](../../../classes/part-13-especificaciones-contratos-y-modelos/se-166-especificaciones-ejecutables-y-pruebas-contractuales/README.md)). La clase añade que un contrato HTTP incluye además la semántica definida en RFC 9110 (métodos, códigos, cabeceras), y es en esos detalles donde aparecen las discrepancias.

En la plataforma de entregas, el documento OpenAPI de la API y el documento AsyncAPI de los eventos viven en el repositorio, versionados con el código. Un linter de integración continua verifica la forma (identificadores únicos, parámetros, respuestas de error); una prueba contractual comprueba que el servicio responda lo prometido, incluida la respuesta 201 de `crearEntrega`. El documento de eventos declara la semántica de entrega («al menos una vez», sin orden global) y exige identificador y versión en cada mensaje; los consumidores son idempotentes por diseño.

## Ejemplo

Fragmento mínimo de una operación (ilustración del formato):

```yaml
paths:
  /entregas:
    post:
      operationId: crearEntrega
      responses:
        "201":
          description: Entrega creada
```

Un cliente generado a partir de este documento llamará a `POST /entregas` y esperará un 201. Si el servicio real devuelve 200, el documento sigue siendo válido pero el cliente falla: justo el síntoma que [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) asocia a la divergencia, y que la prueba contractual detecta.

## Errores y confusiones comunes

- **Un cliente generado falla contra el servicio real**: documento y servicio divergieron; corrección: pruebas contractuales en integración continua.
- **Notificaciones duplicadas**: el consumidor no es idempotente y la entrega es «al menos una vez»; corrección: identificador único por evento y descarte de repetidos.
- **Creer que el documento valida el servicio**: lo describe.
- **Confundir OpenAPI con Swagger**: Swagger es el nombre histórico y un conjunto de herramientas; OpenAPI es la especificación.

## Límites y cuándo no aplica

No describe bien APIs que no son HTTP/REST (por ejemplo, GraphQL o gRPC tienen sus propios lenguajes de esquema). No captura reglas de negocio complejas ni orden entre llamadas. Un documento generado automáticamente del código puede heredar sus defectos; uno escrito primero puede divergir. En cualquier caso hace falta la comprobación contractual.

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
