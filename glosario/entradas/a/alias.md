# Alias

[↑ Glosario](../../README.md) · [← Algoritmo](./algoritmo.md) · [Aliasing →](./aliasing.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Nombre alternativo que permite pedir el mismo campo varias veces en una consulta.

Definición de trabajo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md).

## Por qué importa

La clase donde se define, [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md), existe con este propósito: la clase existe para que elijas el estilo de interfaz (recursos HTTP, llamadas a procedimientos o consultas con selección de campos) por lo que cada uno cuesta y por lo que traslada al cliente o al servidor, y para que midas cuántos bytes, viajes y consultas a la base de datos produce una pantalla concreta en cada estilo.

## Cómo funciona

Según [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md):

Es insuficiente por sí solo: una consulta de profundidad 2 con alias repetidos o listas enormes puede ser muy costosa. Se combina con límite de nodos, paginación obligatoria y tiempo máximo.

## Ejemplo

Ejemplo de [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sección «Preguntas frecuentes»):

Es insuficiente por sí solo: una consulta de profundidad 2 con alias repetidos o listas enormes puede ser muy costosa. Se combina con límite de nodos, paginación obligatoria y tiempo máximo.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md)) son:

- **La pantalla es lenta con muchos elementos y rápida con pocos** — causa: una consulta por elemento (N+1). Corrección: contar consultas por solicitud y cargar por lotes.
- **El móvil descarga megabytes para mostrar una lista corta** — causa: recursos completos que la pantalla no usa. Corrección: seleccionar campos o diseñar una respuesta para la pantalla.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se midió ninguna red ni servidor real, y ningún cliente: las descripciones, los comentarios y la distribución de profundidades son construcciones del autor. La siguiente clase pregunta cómo se valida lo que llega y cómo se comunican los errores de forma consistente.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Carga por lotes](../c/carga-por-lotes.md), [Coste de una consulta](../c/coste-de-una-consulta.md), [Fanout](../f/fanout.md), [Introspección](../i/introspeccion.md), [Llamada a procedimiento remoto](../l/llamada-a-procedimiento-remoto.md), [N+1](../n/n-mas-1.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-243 — RPC, GraphQL y selección de interfaz](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (15 clases más lo mencionan; las que más):

[SE-562](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-562-privacidad-propiedad-intelectual-y-codigo-inseguro/README.md), [SE-073](../../../classes/part-06-paradigmas-de-programacion/se-073-programacion-imperativa-y-estado-mutable/README.md), [SE-102](../../../classes/part-08-entornos-herramientas-y-depuracion/se-102-gestores-de-versiones-de-runtimes/README.md), [SE-464](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-464-secure-sdlc-abuso-y-pruebas-negativas/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-367](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-367-linaje-catalogo-y-metadatos/README.md), [SE-061](../../../classes/part-05-fundamentos-de-programacion/se-061-valores-expresiones-tipos-y-variables/README.md), [SE-110](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-110-semver-compatibilidad-y-contratos-publicos/README.md).

**Aparece en los casos de estudio:** [Incidente de base de datos de GitLab](../../../casos/fallo/gitlab-2017.md).

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

[↑ Glosario](../../README.md) · [← Algoritmo](./algoritmo.md) · [Aliasing →](./aliasing.md)
