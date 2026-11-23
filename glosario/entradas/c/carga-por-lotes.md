# Carga por lotes

[↑ Glosario](../../README.md) · [← Carga operacional](./carga-operacional.md) · [Carga útil →](./carga-util.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Agrupación en una consulta de las peticiones de datos que se producen en la misma ronda de resolución.

Definición de trabajo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md).

## Por qué importa

La clase donde se define, [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), existe con este propósito: la clase existe para que elijas el estilo de interfaz (recursos HTTP, llamadas a procedimientos o consultas con selección de campos) por lo que cada uno cuesta y por lo que traslada al cliente o al servidor, y para que midas cuántos bytes, viajes y consultas a la base de datos produce una pantalla concreta en cada estilo.

## Cómo funciona

Según [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md):

**Cómo leer la figura.** Cada par de barras compara el resolvedor ingenuo (coral) con el que agrupa (verde) para el mismo número de cursos. **Dónde deja de valer:** SQLite en memoria hace barata cada consulta; con una base de datos remota cada consulta suma una latencia de red y el efecto sería mayor. La carga por lotes tiene su propio costo: una lista de identificadores muy larga o una consulta que no usa un índice puede ser peor que varias pequeñas.

Según [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md):

La plataforma publica tres superficies: una API de recursos para integraciones externas, con caché y paginación por clave; un punto de consulta con selección de campos para el panel docente, con límite de 10 000 nodos, paginación obligatoria en toda lista anidada y carga por lotes en los resolvedores; y llamadas con contrato estricto entre el servicio de entregas y el de notas. Compara el diseño con el original en tres casos: un móvil con red débil, un rediseño del panel y un cliente que anida cinco niveles de golpe.

## Ejemplo

Ejemplo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sección «Ejemplo profesional»):

La plataforma publica tres superficies: una API de recursos para integraciones externas, con caché y paginación por clave; un punto de consulta con selección de campos para el panel docente, con límite de 10 000 nodos, paginación obligatoria en toda lista anidada y carga por lotes en los resolvedores; y llamadas con contrato estricto entre el servicio de entregas y el de notas. Compara el diseño con el original en tres casos: un móvil con red débil, un rediseño del panel y un cliente que anida cinco niveles de golpe.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md)) son:

- **La pantalla es lenta con muchos elementos y rápida con pocos** — causa: una consulta por elemento (N+1). Corrección: contar consultas por solicitud y cargar por lotes.
- **El móvil descarga megabytes para mostrar una lista corta** — causa: recursos completos que la pantalla no usa. Corrección: seleccionar campos o diseñar una respuesta para la pantalla.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La carga por lotes tiene su propio costo: una lista de identificadores muy larga o una consulta que no usa un índice puede ser peor que varias pequeñas. ([SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Agrupación](../a/agrupacion.md), [Resolución](../r/resolucion.md), [Alias](../a/alias.md), [Coste de una consulta](./coste-de-una-consulta.md), [Fanout](../f/fanout.md), [Introspección](../i/introspeccion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md).

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

[↑ Glosario](../../README.md) · [← Carga operacional](./carga-operacional.md) · [Carga útil →](./carga-util.md)
