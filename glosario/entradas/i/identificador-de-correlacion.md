# Identificador de correlación

[↑ Glosario](../../README.md) · [← Identificabilidad](./identificabilidad.md) · [Identificador de sesión →](./identificador-de-sesion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Un **identificador de correlación** es un valor que enlaza una respuesta con su solicitud, o que acompaña a un flujo para unir los registros y tramos de componentes distintos. El programa lo define de formas cercanas: en [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), asocia respuesta y solicitud sin depender del orden; en [SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md), une la respuesta al cliente con el registro interno de la misma solicitud; en [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) y [SE-308](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md), se propaga entre servicios y se registra en cada evento que la solicitud toca.

## Por qué importa

Sin él, depurar un incidente distribuido es adivinar qué línea de qué servicio pertenece a qué petición. Con él, a partir de una queja de un cliente («esta petición falló») se recupera toda la historia en todos los componentes.

## Cómo funciona

[SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) lo explica con trazas. Una **traza** es el recorrido de una petición por varios componentes; cada paso es un **tramo** (*span*) con un padre. Para unir tramos de procesos distintos, cada uno debe recibir y reenviar un identificador o un contexto de traza. W3C Trace Context lo estandariza en un encabezado, `traceparent`, que lleva el identificador de la traza y del tramo padre.

Cómo se usa en la práctica:

1. **Generar** el identificador en el borde, si la petición no lo trae.
2. **Propagarlo** en cada llamada saliente (encabezado o metadato del mensaje).
3. **Registrarlo** en cada línea de log ([SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), logs estructurados).
4. **Devolverlo** al cliente en la respuesta o en el error ([SE-244](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md)), para que lo cite al reportar un problema.

La propiedad crítica: la cadena se rompe en el primer eslabón que no reenvía el contexto; un solo servicio que lo ignore hace que las trazas posteriores aparezcan como flujos independientes. Por eso la propagación se prueba, no se supone.

## Ejemplo

Ilustración propia: la persona recibe un error con `id: 7f3a…`; soporte busca ese valor en los registros del gateway, del servicio de entregas y de la cola, y reconstruye en un solo vistazo dónde se detuvo. En mensajería ([SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md)), una respuesta lleva el identificador de la solicitud, y quien la recibe sabe a cuál pertenece aunque lleguen desordenadas.

## Errores y confusiones comunes

- **Un servicio que no propaga el contexto,** y la traza se corta.
- **Usar datos personales como identificador:** debe ser opaco.
- **Confundirlo con un identificador de idempotencia:** aquel agrupa los registros de un flujo; este evita repetir un efecto.
- **No devolverlo al cliente,** de modo que no puede citarlo.

## Límites y cuándo no aplica

Une lo que se registró, pero no registra lo que nadie registró. Una petición que se fragmenta en trabajo asíncrono exige decidir si hereda el identificador o crea uno nuevo enlazado. Generarlo y propagarlo consume algo de ancho de banda; con un solo servicio su valor es menor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-242](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-242-rest-y-semantica-de-recursos/README.md), [SE-243](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-243-rpc-graphql-y-seleccion-de-interfaz/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Evento](../e/evento.md), [Flujo](../f/flujo.md), [Registro](../r/registro.md), [Asignación masiva](../a/asignacion-masiva.md), [Decisión oculta](../d/decision-oculta.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md) — [Parte 25](../../../classes/part-25-diseno-patrones-y-refactorizacion/README.md), Diseño, patrones y refactorización.
- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) — [Parte 31](../../../classes/part-31-integracion-eventos-y-mensajeria/README.md), Integración, eventos y mensajería.
- [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (9 clases más lo mencionan; las que más):

[SE-033](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-033-logs-del-sistema-y-diagnostico-de-fallos/README.md), [SE-047](../../../classes/part-03-redes-internet-y-protocolos/se-047-taller-seguir-una-peticion-de-extremo-a-extremo/README.md), [SE-044](../../../classes/part-03-redes-internet-y-protocolos/se-044-proxies-balanceadores-gateways-y-cdn/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-046](../../../classes/part-03-redes-internet-y-protocolos/se-046-captura-medicion-y-diagnostico-de-trafico/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-245](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-245-autenticacion-autorizacion-y-contexto/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — encabezados para propagar el contexto de una traza; autoridad: W3C.
- [OpenTelemetry: convenciones semánticas de mensajería](https://opentelemetry.io/docs/specs/semconv/messaging/) — trazas y atributos de productores y consumidores; autoridad: proyecto OpenTelemetry.
- [Google SRE: monitorización de sistemas distribuidos](https://sre.google/sre-book/monitoring-distributed-systems/) — señales de síntomas y alarmas con acción; autoridad: Google.
- [OWASP: Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) — qué registrar y qué no; autoridad: OWASP.
- [OWASP: Seguridad de APIs](https://owasp.org/www-project-api-security/) — riesgos de las interfaces; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Identificabilidad](./identificabilidad.md) · [Identificador de sesión →](./identificador-de-sesion.md)
