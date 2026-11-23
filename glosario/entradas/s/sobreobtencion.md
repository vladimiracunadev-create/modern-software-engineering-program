# Sobreobtención

[↑ Glosario](../../README.md) · [← Sobremuestreo](./sobremuestreo.md) · [Sobreventa →](./sobreventa.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Recibir más campos de los que la pantalla utiliza.

Definición de trabajo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md).

## Por qué importa

En [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), el tema «Sobreobtención y subobtención» importa porque pedir de más desperdicia ancho de banda; pedir de menos obliga a viajes adicionales.

## Cómo funciona

Según [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md):

La **sobreobtención** ocurre cuando la representación trae campos que el cliente no usa; la **subobtención**, cuando una pantalla necesita datos de varios recursos y hace varios viajes. Los dos son costos reales en redes lentas, pero tienen remedios distintos: seleccionar campos reduce lo primero, componer en el servidor reduce lo segundo. El riesgo de optimizar la pantalla actual es acoplar el servidor a ella: cada rediseño de la pantalla pide un cambio de servidor.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md):

La plataforma publica tres superficies: una API de recursos para integraciones externas, con caché y paginación por clave; un punto de consulta con selección de campos para el panel docente, con límite de 10 000 nodos, paginación obligatoria en toda lista anidada y carga por lotes en los resolvedores; y llamadas con contrato estricto entre el servicio de entregas y el de notas. Compara el diseño con el original en tres casos: un móvil con red débil, un rediseño del panel y un cliente que anida cinco niveles de golpe.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md)) son:

- **La pantalla es lenta con muchos elementos y rápida con pocos** — causa: una consulta por elemento (N+1). Corrección: contar consultas por solicitud y cargar por lotes.
- **El móvil descarga megabytes para mostrar una lista corta** — causa: recursos completos que la pantalla no usa. Corrección: seleccionar campos o diseñar una respuesta para la pantalla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La **sobreobtención** ocurre cuando la representación trae campos que el cliente no usa; la **subobtención**, cuando una pantalla necesita datos de varios recursos y hace varios viajes. ([SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alias](../a/alias.md), [Carga por lotes](../c/carga-por-lotes.md), [Coste de una consulta](../c/coste-de-una-consulta.md), [Fanout](../f/fanout.md), [Introspección](../i/introspeccion.md), [Llamada a procedimiento remoto](../l/llamada-a-procedimiento-remoto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [GraphQL Specification](https://spec.graphql.org/) — modelo de consulta y resolución de campos; autoridad: GraphQL Foundation.
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html) — riesgos de profundidad, coste y exposición del esquema; autoridad: OWASP.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — semántica de métodos y representaciones; autoridad: IETF.
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de interfaces de recursos; autoridad: OpenAPI Initiative.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — consultas parametrizadas del experimento; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← Sobremuestreo](./sobremuestreo.md) · [Sobreventa →](./sobreventa.md)
