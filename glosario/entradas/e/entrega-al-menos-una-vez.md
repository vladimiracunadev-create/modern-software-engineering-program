# Entrega al menos una vez

[↑ Glosario](../../README.md) · [← Entradas no confiables](./entradas-no-confiables.md) · [Entrega al menos una vez / como máximo una vez →](./entrega-al-menos-una-vez-como-maximo-una-vez.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

La **entrega al menos una vez** (*at-least-once delivery*) es la garantía de que un mensaje llegará una o más veces, nunca cero, sin impedir los duplicados. Es el sentido de [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-241](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md), [SE-362](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) y [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md): el mensaje no se pierde, pero puede repetirse, y quien lo recibe debe tolerar duplicados.

## Por qué importa

Es la garantía que ofrecen en la práctica la mayoría de colas y sistemas de eventos, porque es la que se puede cumplir sin coordinación costosa. Cambia el diseño del receptor: no se pregunta «¿llegará dos veces?» sino «¿qué pasa cuando llegue dos veces?». Ignorarlo produce cobros dobles, correos repetidos o contadores inflados.

## Cómo funciona

[SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) explica el origen: si el consumidor no confirma, el mensaje se reenvía. La cola no puede saber si el consumidor procesó el mensaje y perdió la confirmación, o si nunca llegó a procesarlo ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md): no sabe si el trabajador cayó antes o después de ejecutar el efecto, solo que no confirmó). Para no perder, reentrega. Consecuencia: el manejador puede ver el mismo evento dos o más veces.

La defensa es la **idempotencia**: procesar un evento repetido produce el mismo estado que procesarlo una vez, por ejemplo guardando el identificador del evento y descartando los ya vistos. [SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) cita CloudEvents: el identificador, junto con la fuente, distingue un evento de otro, y un reenvío puede conservar su identificador, justo lo que permite reconocerlo. En [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), la **inbox** (tabla con el identificador como clave primaria) lo implementa con `INSERT OR IGNORE` en la misma transacción que el efecto.

## Ejemplo

Un trabajador recibe «enviar certificado 42», lo envía y cae antes de confirmar. La cola reentrega y el trabajador vuelve a recibirlo. Si guarda el identificador del mensaje en la misma transacción que el efecto, el segundo intento se descarta. Ilustración propia; el patrón está en [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) y [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md).

## Errores y confusiones comunes

- **Suponer «exactamente una vez»:** casi nunca se ofrece de extremo a extremo; se logra combinando al menos una vez con receptor idempotente.
- **Hacer efectos no idempotentes en el manejador** (enviar dinero, enviar un correo) sin clave de deduplicación.
- **Confirmar antes de procesar,** que convierte la garantía en «como máximo una vez» y pierde mensajes.
- **Confundirla con idempotencia:** la entrega es del transporte; la idempotencia es del receptor.

## Límites y cuándo no aplica

Si el efecto es inofensivo repetido, el problema desaparece sin más. Si el efecto no se puede deduplicar (un sistema externo que no acepta claves), hace falta otro diseño. La garantía describe al transporte; el orden de los mensajes es otro asunto que no ofrece.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-240](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-240-proyecto-aplicacion-web-accesible-y-offline/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Garantía](../g/garantia.md), [Backend](../b/backend.md), [Cola de cartas muertas](../c/cola-de-cartas-muertas.md), [Cola larga](../c/cola-larga.md), [Contrato público](../c/contrato-publico.md), [Frontera de confirmación](../f/frontera-de-confirmacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md) — [Parte 26](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/README.md), Patrones de diseño, empresariales y de resiliencia.
- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.

**También se usa en** (17 clases más lo mencionan; las que más):

[SE-413](../../../classes/part-34-saas-y-plataformas-de-producto/se-413-medicion-de-uso-y-facturacion-por-consumo/README.md), [SE-163](../../../classes/part-13-especificaciones-contratos-y-modelos/se-163-openapi-asyncapi-graphql-y-contratos-de-eventos/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md), [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), [SE-330](../../../classes/part-27-arquitectura-de-software-y-dominio/se-330-event-driven-cqrs-y-event-sourcing/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-378](../../../classes/part-31-integracion-eventos-y-mensajeria/se-378-cdc-etl-elt-y-sincronizacion/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [AWS Lambda: entorno de ejecución](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html) — fases de un entorno y su reutilización; autoridad: documentación del proveedor.
- [Google Cloud Run: documentación](https://cloud.google.com/run/docs) — servicio gestionado con escalado automático; autoridad: documentación del proveedor.
- [Serverless Computing: One Step Forward, Two Steps Back](https://arxiv.org/abs/1812.03651) — límites del modelo; autoridad: artículo de investigación (CIDR 2019).
- [CloudEvents](https://cloudevents.io/) — identificación de eventos y reenvíos; autoridad: proyecto de la Cloud Native Computing Foundation.
- [Python: opciones de línea de comandos](https://docs.python.org/3/using/cmdline.html) — medición del tiempo de importación; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Entradas no confiables](./entradas-no-confiables.md) · [Entrega al menos una vez / como máximo una vez →](./entrega-al-menos-una-vez-como-maximo-una-vez.md)
