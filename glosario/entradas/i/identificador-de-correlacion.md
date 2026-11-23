# Identificador de correlación

[↑ Glosario](../../README.md) · [← Identificabilidad](./identificabilidad.md) · [Identificador de sesión →](./identificador-de-sesion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Valor que enlaza una respuesta con su solicitud.

Definición de trabajo de [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md): Valor que acompaña a un flujo y permite unir los registros y tramos de componentes distintos.
- En [SE-244 — Validación, errores y contratos consistentes](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-244-validacion-errores-y-contratos-consistentes/README.md): Valor que une la respuesta al cliente con el registro interno de la misma solicitud.
- En [SE-494 — Logs estructurados y correlación](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md): Valor que se propaga entre servicios para unir las líneas y los spans de una misma petición.
- En [SE-308 — Diseño para cambio, prueba y operación](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-308-diseno-para-cambio-prueba-y-operacion/README.md): Valor único de una solicitud que se registra en cada evento que la toca.

## Por qué importa

En [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), el tema «Identificador de correlación» importa porque asocia respuesta y solicitud sin depender del orden

## Cómo funciona

Según [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md):

Una **traza** es el recorrido de una petición o de un flujo por varios componentes; cada paso es un **tramo** (span) con un padre. Para unir tramos de procesos distintos hace falta que cada uno reciba y reenvíe un **identificador de correlación** o un contexto de traza. W3C Trace Context estandariza esto en un encabezado, `traceparent`, que lleva el identificador de la traza y del tramo padre. La propiedad crítica es que la cadena se rompe en el primer eslabón que no reenvía el contexto: un solo servicio que lo ignora hace que las trazas posteriores aparezcan como flujos independientes. Por eso la propagación se prueba, no se supone.

Según [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md):

Registra síntoma, entrada mínima, hipótesis, observación que descarta cada hipótesis, causa, corrección y prueba de regresión. **Síntoma:** en la herramienta de trazas, la entrega aparece en dos flujos distintos y la segunda mitad no tiene origen. **Hipótesis rivales:** (a) el mensaje fue enviado dos veces; (b) se perdió un tramo por muestreo; (c) un servicio generó una correlación nueva. **Prueba:** busca en cada servicio el identificador de correlación de la entrega; si el segundo servicio registra otro identificador para el mismo mensaje, la causa es la regeneración. **Conclusión:** el servicio no propagó el contexto recibido. **Regresión:** extraer el contexto del mensaje y reenviarlo, y una prueba de integración que publique un mensaje con un identificador conocido y compruebe que aparece idéntico en los registros de todos los servicios.

## Ejemplo

Ejemplo de [SE-382 — Observabilidad y seguridad de integraciones](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md) (sección «Ejemplo mínimo»):

El fragmento inyecta un identificador de correlación en un mensaje y lo extrae en el consumidor. Antes de ejecutarlo, predice qué ocurre si el productor olvida inyectarlo.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para unir tramos de procesos distintos hace falta que cada uno reciba y reenvíe un **identificador de correlación** o un contexto de traza. ([SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md))

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
