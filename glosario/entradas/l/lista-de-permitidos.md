# Lista de permitidos

[↑ Glosario](../../README.md) · [← Lista de escenarios](./lista-de-escenarios.md) · [Lista dinámica y capacidad →](./lista-dinamica-y-capacidad.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Política que registra únicamente los campos expresamente autorizados.

Definición de trabajo de [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md): Regla de validación que enumera lo aceptable y rechaza todo lo demás.

## Por qué importa

La clase donde se define, [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), existe con este propósito: la clase existe para que puedas ver y proteger un flujo que cruza servicios, colas y proveedores: aprenderás a medir cuántas trazas completas sobreviven cuando los saltos pierden el identificador de correlación, qué señal de un consumidor detecta cada tipo de falla (y cuál da falsas alarmas) y cuántos datos sensibles filtra cada política de registro, antes de que un incidente obligue a investigar sin datos o con demasiados.

## Cómo funciona

Según [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md):

Registrar todo filtra todo. Cada expresión regular cierra un tipo de dato y deja abierto el siguiente: tras sustituir correos aún salen 2 000 tokens, y tras sustituir ambos aún salen los 200 comentarios, porque un identificador escrito como «alumno7 [arroba] ejemplo.test» no coincide con ningún patrón. La lista de permitidos no filtra nada de lo medido porque no registra lo que no se le dijo que registrara.

Según [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md):

La plataforma valida en dos capas: la frontera rechaza con 422 y `type` estable todo lo que no está en la lista de permitidos (tipos exactos, rangos, campos extra, claves repetidas); el dominio rechaza con 409 o 422 las reglas del negocio (entrega fuera de plazo sin prórroga). Todos los errores comparten una forma de cuatro campos y un identificador de correlación. El contrato publicado indica qué errores son reintentables (429, 503) y cuáles no (400, 422). Compara el diseño con el original en tres casos: un móvil con un booleano en lugar de un número, una integración que añade un campo y una avalancha de reintentos tras un 503.

## Ejemplo

Ejemplo de [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) (sección «Ejemplo profesional»):

La plataforma valida en dos capas: la frontera rechaza con 422 y `type` estable todo lo que no está en la lista de permitidos (tipos exactos, rangos, campos extra, claves repetidas); el dominio rechaza con 409 o 422 las reglas del negocio (entrega fuera de plazo sin prórroga). Todos los errores comparten una forma de cuatro campos y un identificador de correlación. El contrato publicado indica qué errores son reintentables (429, 503) y cuáles no (400, 422). Compara el diseño con el original en tres casos: un móvil con un booleano en lugar de un número, una integración que añade un campo y una avalancha de reintentos tras un 503.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una redacción deja salir datos** — causa: las expresiones regulares no previeron un formato. Corrección: lista de permitidos como control principal y redacción como red. ([SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md))
- **Un cliente consigue campos que no debería tener** — causa: esquema abierto: los campos extra pasan al dominio. Corrección: esquema cerrado y lista de permitidos. ([SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La lista de permitidos no filtra nada de lo medido porque no registra lo que no se le dijo que registrara. ([SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Regla](../r/regla.md), [Validación](../v/validacion.md), [Asignación masiva](../a/asignacion-masiva.md), [Deriva del contrato](../d/deriva-del-contrato.md), [Enumeración](../e/enumeracion.md), [Error permanente](../e/error-permanente.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.

**También se usa en** (4 clases más lo mencionan; las que más):

[SE-401](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-401-redes-identidad-y-secretos-en-cloud/README.md), [SE-569](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-569-agentes-herramientas-permisos-y-limites-de-autoridad/README.md), [SE-579](../../../classes/part-48-harness-y-agentic-engineering/se-579-herramientas-permisos-y-superficies-de-accion/README.md), [SE-384](../../../classes/part-31-integracion-eventos-y-mensajeria/se-384-proyecto-flujo-integrado-tolerante-a-reintentos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación en el servidor con listas de permitidos; autoridad: OWASP.
- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — encabezados para propagar el contexto de una traza; autoridad: W3C.
- [OpenTelemetry: convenciones semánticas de mensajería](https://opentelemetry.io/docs/specs/semconv/messaging/) — trazas y atributos de productores y consumidores; autoridad: proyecto OpenTelemetry.
- [Google SRE: monitorización de sistemas distribuidos](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de síntomas y alarmas con acción; autoridad: Google.
- [OWASP: Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — qué registrar y qué no; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Lista de escenarios](./lista-de-escenarios.md) · [Lista dinámica y capacidad →](./lista-dinamica-y-capacidad.md)
