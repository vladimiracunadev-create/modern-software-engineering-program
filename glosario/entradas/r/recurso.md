# Recurso

[↑ Glosario](../../README.md) · [← Recursión, evaluación y efectos](./recursion-evaluacion-y-efectos.md) · [Recurso huérfano →](./recurso-huerfano.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Un **recurso** es, en el diseño de APIs, algo con identidad que el sistema puede nombrar y sobre lo que puede actuar mediante métodos ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)). [SE-042](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) lo precisa como el objetivo conceptual identificado por una URI. En el trabajo con agentes ([SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md)) es un dato que un servidor expone y que la aplicación decide cómo incorporar al contexto. Es sustantivo, no acción.

## Por qué importa

Modelar bien los recursos decide la forma de toda la API: qué URL existen, qué métodos tienen sentido, qué se puede cachear y cómo se evitan conflictos de edición. [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) lo muestra con dos fallos concretos: pérdidas silenciosas de cambios por escrituras ciegas y datos viejos servidos por la caché.

## Cómo funciona

En HTTP, la URL identifica al recurso, no a la acción ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)). «Entrega» es un recurso; «subirEntrega» es una acción que pertenece al método (`POST` sobre la colección). Modelar acciones como recursos (`/entregas/42/apelaciones`) es legítimo cuando la acción crea algo con identidad propia que luego se consulta; ahí el sustantivo es la apelación.

Un recurso editable por varias personas necesita control de concurrencia: el servidor entrega un validador (`ETag`) con cada representación y el cliente lo devuelve en `If-Match` al modificar; si el recurso cambió, el servidor responde `412` y el cliente relee. La caché también necesita validador e invalidación: sin ellos, sirve datos viejos tras editar. En [SE-571](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md), un recurso expuesto por un servidor no entra al contexto del modelo automáticamente: la aplicación decide si y cómo.

## Ejemplo

```text
GET  /entregas/42           -> 200, ETag: "v7"
PUT  /entregas/42           If-Match: "v7"   -> 200 ("v8")
PUT  /entregas/42           If-Match: "v7"   -> 412 Precondition Failed (otra persona editó antes)
```

## Errores y confusiones comunes

- **Un docente pierde su cambio sin error.** Causa: `PUT` ciego sobre un recurso editable por varias personas; corrección: `ETag`, `If-Match` y `412` con releer ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)).
- **La caché sirve datos viejos tras editar.** Causa: respuesta cacheable sin validador ni invalidación; corrección: `ETag` y revalidación, evitando TTL largos en recursos editables ([SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md)).
- **Verbos en las URL.** `/subirEntrega` mezcla acción y recurso.

## Límites y cuándo no aplica

No todo encaja como recurso: operaciones de procesamiento puro o comandos con muchos pasos a veces se modelan mejor como acciones o como un proceso con estado. En otros contextos, «recurso» designa CPU, memoria o conexiones (recursos de cómputo); esta entrada trata el sentido de identidad nombrada. Y en un taller, [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) usa «recursos» para los archivos que se comparan tras verificar un invariante.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md), [SE-022](../../../classes/part-01-computadores-y-representacion-de-informacion/se-022-rendimiento-consumo-energetico-y-limites-fisicos/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contextos](../c/contextos.md), [Sobre](../s/sobre.md), [Alcance](../a/alcance.md), [Diagnóstico](../d/diagnostico.md), [ETag](../e/etag.md), [Fixture](../f/fixture.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-023 — Taller: observar un programa desde el código hasta la máquina](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.
- [SE-042 — HTTP, semántica, caché y negociación](../../../classes/part-03-redes-internet-y-protocolos/se-042-http-semantica-cache-y-negociacion/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-242 — REST y semántica de recursos](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-571 — MCP, recursos, prompts, tools y confianza](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-571-mcp-recursos-prompts-tools-y-confianza/README.md) — [Parte 47](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/README.md), SPEC, agentes y ciclo de vida agentic.

**También se usa en** (166 clases más lo mencionan; las que más):

[SE-407](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-407-taller-desplegar-y-destruir-un-entorno-seguro/README.md), [SE-402](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-402-infraestructura-como-codigo-y-estado/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md), [SE-321](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-321-resiliencia-bulkhead-sidecar-ambassador-y-degradacion/README.md), [SE-486](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-486-infraestructura-como-codigo-en-pipeline/README.md), [SE-487](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-487-gitops-y-reconciliacion/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-235](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-235-rendimiento-web-y-presupuestos/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [Amazon](../../../casos/exito/amazon.md), [Stripe](../../../casos/exito/stripe.md), [Slack](../../../casos/exito/slack.md), [Shopify](../../../casos/exito/shopify.md).

## Sinónimos y traducción

**Forma en inglés o término técnico original:** «Recursos».

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) — descripción de recursos y métodos de una API; autoridad: OpenAPI Initiative.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — métodos seguros e idempotentes, `ETag`, 412 y 428; autoridad: IETF.
- [HTTP Caching (RFC 9111)](https://www.rfc-editor.org/rfc/rfc9111) — reutilización y revalidación de respuestas cacheadas; autoridad: IETF.
- [Python: sqlite3](https://docs.python.org/3/library/sqlite3.html) — transacciones y consultas del experimento de paginación; autoridad: Python Software Foundation.
- [SQLite: The Query Planner](https://www.sqlite.org/queryplanner.html) — cómo un índice sirve a una consulta por rango; autoridad: SQLite.

---

[↑ Glosario](../../README.md) · [← Recursión, evaluación y efectos](./recursion-evaluacion-y-efectos.md) · [Recurso huérfano →](./recurso-huerfano.md)
