# N+1

[↑ Glosario](../../README.md) · [← Mutante superviviente](../m/mutante-superviviente.md) · [Namespace →](./namespace.md)

> **Tipo:** sigla · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Patrón en el que una lista de N elementos genera N consultas adicionales además de la inicial.

Definición de trabajo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md): Patrón en que una consulta inicial desencadena una consulta adicional por cada fila.
- En [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md): Patrón de una consulta inicial más una consulta por cada elemento de su resultado.

## Por qué importa

En [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), el tema «Resolvedores y N+1» importa porque resolver por campo convierte una lista de N en N+1 consultas si no se agrupan.

## Cómo funciona

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

**Cómo leer la figura.** Cada barra es el número de sentencias que la base recibió para producir el mismo listado. **Dónde deja de valer:** la base es `sqlite3` en memoria, sin red; con una base remota cada consulta suma una latencia de red y la diferencia se amplifica, y con un ORM que precarga por defecto el problema aparece en otro lugar. El número 201 es el patrón N+1 en un caso, no una constante.

Según [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md):

Muchos ORM implementan ambos (una sesión que agrupa cambios y un acceso por consulta). El patrón sigue siendo útil como interfaz del dominio que no depende del ORM; y el N+1 sigue pudiendo ocurrir. Mide las consultas de todos modos.

## Ejemplo

Ejemplo de [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) (sección «Preguntas frecuentes»):

Muchos ORM implementan ambos (una sesión que agrupa cambios y un acceso por consulta). El patrón sigue siendo útil como interfaz del dominio que no depende del ORM; y el N+1 sigue pudiendo ocurrir. Mide las consultas de todos modos.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **La pantalla es lenta con muchos elementos y rápida con pocos** — causa: una consulta por elemento (N+1). Corrección: contar consultas por solicitud y cargar por lotes. ([SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md))
- **Un informe tarda minutos y cada consulta es rápida** — causa: patrón N+1. Corrección: una sola consulta agregada o un `JOIN`. ([SE-353](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El número 201 es el patrón N+1 en un caso, no una constante. ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md))
- El patrón sigue siendo útil como interfaz del dominio que no depende del ORM; y el N+1 sigue pudiendo ocurrir. ([SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Patrón](../p/patron.md), [Resultado](../r/resultado.md), [Active Record](../a/active-record.md), [Alias](../a/alias.md), [Atomicidad](../a/atomicidad.md), [Carga por lotes](../c/carga-por-lotes.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-318 — Repository, Unit of Work y Active Record](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-353 — Consultas, índices y patrones de acceso](../../../classes/part-29-datos-persistencia-y-recuperacion/se-353-consultas-indices-y-patrones-de-acceso/README.md) — [Parte 29](../../../classes/part-29-datos-persistencia-y-recuperacion/README.md), Datos, persistencia y recuperación.

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

[↑ Glosario](../../README.md) · [← Mutante superviviente](../m/mutante-superviviente.md) · [Namespace →](./namespace.md)
