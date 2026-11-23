# Error permanente

[↑ Glosario](../../README.md) · [← Error de protocolo](./error-de-protocolo.md) · [Error transitorio →](./error-transitorio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Fallo que se repite igual si se reintenta la misma solicitud.

Definición de trabajo de [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md).

## Por qué importa

En [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), el tema «Clasificación de fallos» importa porque reintentar un error permanente solo añade carga; no reintentar uno transitorio pierde trabajo.

## Cómo funciona

[SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md):

La plataforma valida en dos capas: la frontera rechaza con 422 y `type` estable todo lo que no está en la lista de permitidos (tipos exactos, rangos, campos extra, claves repetidas); el dominio rechaza con 409 o 422 las reglas del negocio (entrega fuera de plazo sin prórroga). Todos los errores comparten una forma de cuatro campos y un identificador de correlación. El contrato publicado indica qué errores son reintentables (429, 503) y cuáles no (400, 422).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)) son:

- **Una nota negativa aparece en el panel** — causa: `Infinity` o un número enorme aceptados por el validador. Corrección: rangos acotados y rechazo de valores no finitos.
- **Un cliente consigue campos que no debería tener** — causa: esquema abierto: los campos extra pasan al dominio. Corrección: esquema cerrado y lista de permitidos.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se auditó ninguna API real ni se midió a ninguna persona: las cargas, las mutaciones y la mezcla de fallos son construcciones del autor. La siguiente clase pregunta quién hace la solicitud y qué le está permitido.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Asignación masiva](../a/asignacion-masiva.md), [Deriva del contrato](../d/deriva-del-contrato.md), [Enumeración](./enumeracion.md), [Error transitorio](./error-transitorio.md), [Esquema cerrado](./esquema-cerrado.md), [Frontera de validación](../f/frontera-de-validacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-048](../../../classes/part-03-redes-internet-y-protocolos/se-048-proyecto-servicio-observable-y-tolerante-a-fallos-de-red/README.md), [SE-296](../../../classes/part-24-software-especializado-y-dominios/se-296-blockchain-consenso-y-contratos-inteligentes/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [The JSON Data Interchange Format (RFC 8259)](https://www.rfc-editor.org/rfc/rfc8259) — sintaxis JSON y casos abiertos; autoridad: IETF.
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación en el servidor con listas de permitidos; autoridad: OWASP.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — códigos de estado 4xx y 5xx; autoridad: IETF.
- [JSON Schema 2020-12: Validation](https://json-schema.org/draft/2020-12/json-schema-validation) — vocabulario de validación de datos; autoridad: proyecto JSON Schema.
- [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) — reintentos, tiempos máximos y retroceso; autoridad: Amazon Builders' Library.

---

[↑ Glosario](../../README.md) · [← Error de protocolo](./error-de-protocolo.md) · [Error transitorio →](./error-transitorio.md)
