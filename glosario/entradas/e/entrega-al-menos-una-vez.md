# Entrega al menos una vez

[↑ Glosario](../../README.md) · [← Entradas no confiables](./entradas-no-confiables.md) · [Entrega al menos una vez / como máximo una vez →](./entrega-al-menos-una-vez-como-maximo-una-vez.md)

> **Tipo:** práctica o técnica · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Garantía de que un mensaje llegará una o más veces, nunca cero, sin impedir los duplicados.

Definición de trabajo de [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-319 — Enterprise Integration Patterns como lenguaje común](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md): El mensaje llega una o más veces; no se pierde, puede duplicarse.
- En [SE-241 — Responsabilidades y fronteras del backend](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-241-responsabilidades-y-fronteras-del-backend/README.md): Garantía de que un mensaje llega una o más veces; exige que quien lo recibe tolere duplicados.
- En [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md): Garantía de que cada mensaje llega una o más veces.

## Por qué importa

En [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), el tema «Entrega al menos una vez» importa porque un evento puede llegar repetido; el efecto no debe.

## Cómo funciona

Según [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md), en la sección «Entrega al menos una vez»:

Las colas y los sistemas de eventos suelen garantizar que un mensaje se entrega al menos una vez: si el consumidor no confirma, se reenvía. No pueden saber si el consumidor procesó el mensaje y perdió la confirmación o no llegó a procesarlo. Por tanto el manejador puede ver el mismo evento dos o más veces. La defensa es la **idempotencia**: procesar un evento repetido produce el mismo estado que procesarlo una vez, por ejemplo guardando el identificador del evento y descartando los ya vistos. CloudEvents formaliza que el identificador, junto con la fuente, distingue un evento de otro y que un reenvío puede conservar su identificador, precisamente lo que permite reconocerlo.

Según [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md), en la sección «Entrega al menos una vez»:

La cola no puede saber si el trabajador cayó antes o después de ejecutar el efecto, solo que no confirmó. Para no perder, vuelve a entregar; el costo es que el efecto puede ocurrir más de una vez. Un handler **ingenuo** inserta la nota cada vez; uno **idempotente** comprueba si el trabajo ya tiene efecto (restricción única por identificador de trabajo, `SE-246`) y no repite. El resultado exactamente una vez es una propiedad del efecto, no de la cola.

## Ejemplo

Ejemplo de [SE-247 — Jobs, colas y procesamiento diferido](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sección «Preguntas frecuentes»):

Como propiedad del efecto sí, como garantía de la cola no. Se consigue con entrega al menos una vez y un handler idempotente; algunos sistemas lo llaman procesamiento efectivamente único.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un correo o un cobro se repite** — causa: manejador no idempotente con entrega al menos una vez. Corrección: guardar el identificador del evento con el efecto. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))
- **La nota se registra dos veces** — causa: handler no idempotente con entrega al menos una vez. Corrección: restricción única por identificador de trabajo. ([SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Las colas y los sistemas de eventos suelen garantizar que un mensaje se entrega al menos una vez: si el consumidor no confirma, se reenvía. ([SE-400](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md))

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
