# Enumeración

[↑ Glosario](../../README.md) · [← Entropía de una cadena](./entropia-de-una-cadena.md) · [Enumeración de identificadores →](./enumeracion-de-identificadores.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Conjunto cerrado de valores válidos de un campo.

Definición de trabajo de [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md).

## Por qué importa

La clase donde se define, [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), existe con este propósito: la clase existe para que decidas qué se valida en la frontera del servicio y qué en el dominio, que midas qué deja pasar un validador escrito con buena fe, que mantengas una forma de error única y que clasifiques los fallos para que el cliente sepa si reintentar.

## Cómo funciona

Según [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md):

El contrato de salida también se comprueba: la respuesta real debe cumplir el esquema. Un ejemplo parcial (comprobar el `id` y el `estado`) deja pasar un campo renombrado o uno nuevo; un esquema abierto no ve campos extra; uno cerrado no ve un valor fuera de la enumeración. Cada capa añade una clase de defecto detectable y todas pueden medirse con mutaciones de una respuesta de referencia.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md):

La plataforma valida en dos capas: la frontera rechaza con 422 y `type` estable todo lo que no está en la lista de permitidos (tipos exactos, rangos, campos extra, claves repetidas); el dominio rechaza con 409 o 422 las reglas del negocio (entrega fuera de plazo sin prórroga). Todos los errores comparten una forma de cuatro campos y un identificador de correlación. El contrato publicado indica qué errores son reintentables (429, 503) y cuáles no (400, 422).

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)) son:

- **Una nota negativa aparece en el panel** — causa: `Infinity` o un número enorme aceptados por el validador. Corrección: rangos acotados y rechazo de valores no finitos.
- **Un cliente consigue campos que no debería tener** — causa: esquema abierto: los campos extra pasan al dominio. Corrección: esquema cerrado y lista de permitidos.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un ejemplo parcial (comprobar el `id` y el `estado`) deja pasar un campo renombrado o uno nuevo; un esquema abierto no ve campos extra; uno cerrado no ve un valor fuera de la enumeración. ([SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Valor](../v/valor.md), [Asignación masiva](../a/asignacion-masiva.md), [Deriva del contrato](../d/deriva-del-contrato.md), [Error permanente](./error-permanente.md), [Error transitorio](./error-transitorio.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (48 clases más lo mencionan; las que más):

[SE-380](../../../classes/part-31-integracion-eventos-y-mensajeria/se-380-compatibilidad-de-esquemas-y-registros/README.md), [SE-157](../../../classes/part-13-especificaciones-contratos-y-modelos/se-157-especificacion-informal-semiformal-y-formal/README.md), [SE-219](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-219-configuracion-flags-archivos-y-precedencia/README.md), [SE-146](../../../classes/part-12-ingenieria-de-requisitos/se-146-requisitos-funcionales-y-reglas-de-negocio/README.md), [SE-395](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-395-taller-reproducir-una-carrera-y-un-fallo-parcial/README.md), [SE-269](../../../classes/part-22-embedded-iot-y-tiempo-real/se-269-interrupciones-concurrencia-y-estado-compartido/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-459](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-459-autorizacion-recursos-y-minimo-privilegio/README.md).

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

[↑ Glosario](../../README.md) · [← Entropía de una cadena](./entropia-de-una-cadena.md) · [Enumeración de identificadores →](./enumeracion-de-identificadores.md)
