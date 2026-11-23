# Contrato de interfaz

[↑ Glosario](../../README.md) · [← Contrato de ejecución](./contrato-de-ejecucion.md) · [Contrato de la biblioteca →](./contrato-de-la-biblioteca.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md)

## Definición

Descripción de las operaciones o los mensajes que un servicio ofrece, con sus entradas, salidas, errores y garantías.

Definición de trabajo de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md).

## Por qué importa

La clase donde se define, [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), existe con este propósito: la clase existe para describir una interfaz (rutas, consultas o eventos) en un documento que otra persona o herramienta pueda leer, y para saber qué parte de esa descripción se comprueba mecánicamente y cuál depende de que el servicio la cumpla.

## Cómo funciona

[SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md):

En la plataforma, el documento OpenAPI de la API de entregas y el documento AsyncAPI de los eventos viven en el repositorio, versionados con el código. Un linter de integración continua verifica la forma (identificadores únicos, parámetros, respuestas de error). Una prueba contractual (`SE-166`) comprueba que el servicio responda lo que el documento promete, incluida la respuesta 201 de `crearEntrega`. El documento de eventos declara la semántica de entrega («al menos una vez», sin orden global) y exige identificador y versión en cada mensaje; los consumidores son idempotentes por diseño.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)) son:

- **Un cliente generado falla contra el servicio real** — causa: el documento y el servicio divergieron. Corrección: añadir pruebas contractuales contra el servicio y ejecutarlas en integración continua.
- **Las notificaciones salen duplicadas** — causa: el consumidor no es idempotente y la entrega es «al menos una vez». Corrección: identificador único por evento y descarte de identificadores vistos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún linter real ni un servidor GraphQL o un broker, la medición de resolvedores es un cálculo y las tasas de duplicado y reordenamiento son supuestos. La siguiente clase pregunta cómo cambia un contrato sin romper a quien ya lo usa.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Operación](../o/operacion.md), [Servicio](../s/servicio.md), [Consumidor idempotente](./consumidor-idempotente.md), [Evento](../e/evento.md), [GraphQL](../g/graphql.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-163 — OpenAPI, AsyncAPI, GraphQL y contratos de eventos](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md) — [Parte 13](../../../classes/part-13-especificaciones-contratos-y-modelos/README.md), Especificaciones, contratos y modelos.

**También se usa en** (8 clases más lo mencionan; las que más):

[SE-162](../../../classes/part-13-especificaciones-contratos-y-modelos/se-162-esquemas-de-datos-y-validacion/README.md), [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-161](../../../classes/part-13-especificaciones-contratos-y-modelos/se-161-maquinas-de-estado-y-model-checking-introductorio/README.md), [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), [SE-186](../../../classes/part-15-procesos-planificacion-y-estimacion/se-186-planificacion-de-entregas-y-gestion-de-dependencias/README.md), [SE-278](../../../classes/part-23-runtimes-y-plataformas-modernas/se-278-webassembly-en-servidor-y-borde-component-model/README.md), [SE-531](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-531-comunicacion-facilitacion-y-conflicto/README.md).

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

[↑ Glosario](../../README.md) · [← Contrato de ejecución](./contrato-de-ejecucion.md) · [Contrato de la biblioteca →](./contrato-de-la-biblioteca.md)
