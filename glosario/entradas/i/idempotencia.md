# Idempotencia

[↑ Glosario](../../README.md) · [← IaaS](./iaas.md) · [Idempotente →](./idempotente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Una operación es **idempotente** cuando ejecutarla una vez o varias veces con la misma intención deja el sistema en el mismo estado. La idea no pide que la operación «no haga nada» la segunda vez ni que tarde lo mismo: [SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md) precisa que idempotente es respecto del *efecto observable*, y [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) lo ilustra con operaciones HTTP: `PUT /entregas/42` con el cuerpo completo es idempotente, `POST /entregas` no lo es porque cada llamada crea otra entrega, «sumar 1 a un contador» no lo es y «fijar el contador a 5» sí. Las demás clases usan el mismo sentido con matices de contexto: en automatización ([SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md), [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md)) es poder reejecutar un script sin acumular cambios, en mensajería ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md)) es que un consumidor trate igual un mensaje repetido y en datos ([SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md)) que una transformación pueda reejecutarse sin duplicar filas.

## Por qué importa

Toda red y todo proceso fallan en el peor momento: tras confirmar una escritura y antes de que la respuesta llegue. Quien llama no puede distinguir «no se ejecutó» de «se ejecutó y no me enteré», y la única reacción segura es reintentar. Si la operación no es idempotente, cada reintento puede cobrar dos veces, crear dos entregas o enviar dos mensajes. La idempotencia es lo que convierte el reintento, que es una necesidad, en una decisión sin riesgo. Además abarata el diseño: [SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) muestra que un consumidor que tolera duplicados hace aceptable una garantía de entrega más barata («al menos una vez») en vez de exigir «exactamente una vez».

## Cómo funciona

Hay dos caminos. El primero es elegir operaciones **naturalmente idempotentes**: «fijar a 5» en vez de «sumar 1», reemplazar un contenido canónico en vez de añadirle algo, crear-si-falta en vez de crear. El segundo es **volver idempotente** una operación que no lo es, asociándole una **clave de idempotencia**, según [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md):

1. El cliente genera la clave por *intención* (una por cada «quiero crear esta entrega») y la reutiliza en todos los intentos de esa intención.
2. El servidor guarda la clave junto con el efecto y la respuesta **en la misma transacción**, y una restricción única de la base de datos impide dos filas con la misma clave.
3. Si llega la misma clave con la misma carga, el servidor devuelve la respuesta guardada sin repetir el efecto; si llega con otra carga, es un error del cliente (422), cosa que se distingue con una huella (hash) del contenido.
4. La unicidad se garantiza donde está el estado: comprobar «¿existe la clave?» y luego insertar deja una ventana de carrera; la restricción única la cierra, porque el segundo `insert` falla.

La clave no puede vivir para siempre: debe cubrir el reintento más tardío de un cliente legítimo (una aplicación móvil sin conexión puede reintentar horas o días después), y alargarla cuesta almacenamiento ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md), sobre la ventana de retención). [SE-392](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) extiende el mismo razonamiento al procesamiento distribuido, donde el reintento lo hace el propio sistema.

## Ejemplo

En la simulación de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) (datos sintéticos, base de datos real, semilla fija) se crean 5 000 entregas y, tras confirmar cada escritura, la respuesta se pierde con probabilidad *p*; el cliente reintenta hasta tres veces. Sin clave de idempotencia, una pérdida de respuesta del 1 % duplica el 0,82 % de las entregas, la del 5 % el 5,30 % y la del 20 % el 23,84 %. Con clave y un índice único parcial, el segundo `insert` falla con `IntegrityError`, se devuelve la respuesta guardada y los duplicados son el 0 % en los tres casos. En el mismo experimento, de 6 000 reintentos con retardos que llegan hasta 7 días, el 66,9 % llega con la clave ya caducada si su tiempo de vida es de 10 minutos y el 16,9 % si es de 48 horas: la ventana es una decisión medible.

## Errores y confusiones comunes

- **Reintentar sin clave una operación que cobra.** Entregas duplicadas tras un error de red: el `POST` no llevaba clave de idempotencia. Corrección de [SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md): clave por intención y restricción única.
- **Una clave nueva en cada intento.** El servidor no puede reconocer el reintento y crea un duplicado; la protección supone que el cliente reutiliza la clave.
- **Confundir idempotente con atómico.** Una operación puede ser idempotente y quedar a medias, o atómica y no idempotente. [SE-224](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) pide separar qué parte del diseño dependía de cada una.
- **Pensar que la garantía de entrega sustituye al consumidor.** Un comando («abre la puerta») duplicado puede ser peligroso aunque el transporte prometa «una vez»; la idempotencia debe diseñarse ([SE-270](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md)).
- **Confundir con determinismo.** Idempotente habla del estado final tras repetir, no de que cada ejecución haga el mismo trabajo ni devuelva la misma latencia ([SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md)).

## Límites y cuándo no aplica

La clave protege el efecto que está en la base de datos; un efecto externo que ocurre fuera de la transacción (un correo, un cobro) puede repetirse igualmente ([SE-246](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md)). La idempotencia de un script sobre archivos locales no se hereda a un servicio remoto: crear un recurso o enviar un mensaje necesita además identidad de operación, y su idempotencia depende del servicio ([SE-114](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md)). Una operación cuyo efecto no tolera repetición y no admite clave exige otra defensa, como deduplicación o exclusión ([SE-028](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md)). Y los porcentajes citados salen de una simulación con distribuciones supuestas, no de una medición de clientes reales: lo transferible es el método.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-019](../../../classes/part-01-computadores-y-representacion-de-informacion/se-019-procesos-hilos-interrupciones-y-entrada-salida/README.md), [SE-027](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-027-usuarios-grupos-permisos-y-elevacion-de-privilegios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Efecto](../e/efecto.md), [Estado](../e/estado.md), [Idempotente](./idempotente.md), [Intención](./intencion.md), [Alcance](../a/alcance.md), [Código de salida](../c/codigo-de-salida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-028 — Procesos, señales, servicios y tareas programadas](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-028-procesos-senales-servicios-y-tareas-programadas/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-040 — TCP, UDP, QUIC y decisiones de transporte](../../../classes/part-03-redes-internet-y-protocolos/se-040-tcp-udp-quic-y-decisiones-de-transporte/README.md) — [Parte 03](../../../classes/part-03-redes-internet-y-protocolos/README.md), Redes, Internet y protocolos.
- [SE-114 — Scripting repetible y tareas idempotentes](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-114-scripting-repetible-y-tareas-idempotentes/README.md) — [Parte 09](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/README.md), Bibliotecas, paquetes, SDK y automatización.
- [SE-211 — Runbooks, playbooks y documentación operacional](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-211-runbooks-playbooks-y-documentacion-operacional/README.md) — [Parte 17](../../../classes/part-17-documentacion-y-conocimiento-tecnico/README.md), Documentación y conocimiento técnico.
- [SE-224 — Automatización idempotente y reanudable](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-224-automatizacion-idempotente-y-reanudable/README.md) — [Parte 18](../../../classes/part-18-cli-tui-servicios-y-automatizacion/README.md), CLI, TUI, servicios y automatización.
- [SE-246 — Idempotencia, reintentos y deduplicación](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-246-idempotencia-reintentos-y-deduplicacion/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.
- [SE-260 — Offline-first y resolución de conflictos](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-260-offline-first-y-resolucion-de-conflictos/README.md) — [Parte 21](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/README.md), Software móvil, escritorio y multiplataforma.
- [SE-270 — Protocolos IoT y conectividad intermitente](../../../classes/part-22-embedded-iot-y-tiempo-real/se-270-protocolos-iot-y-conectividad-intermitente/README.md) — [Parte 22](../../../classes/part-22-embedded-iot-y-tiempo-real/README.md), Embedded, IoT y tiempo real.
- [SE-290 — Ingeniería de datos y procesamiento analítico](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md) — [Parte 24](../../../classes/part-24-software-especializado-y-dominios/README.md), Software especializado y dominios.
- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-364 — Transformación y orquestación idempotente con backfills](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.
- [SE-392 — Idempotencia y procesamiento distribuido](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-392-idempotencia-y-procesamiento-distribuido/README.md) — [Parte 32](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/README.md), Concurrencia y sistemas distribuidos.
- [SE-400 — Serverless y ejecución gestionada](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-400-serverless-y-ejecucion-gestionada/README.md) — [Parte 33](../../../classes/part-33-cloud-plataforma-e-infraestructura/README.md), Cloud, plataforma e infraestructura.
- [SE-438 — Timeouts, retries, backoff y jitter](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-438-timeouts-retries-backoff-y-jitter/README.md) — [Parte 36](../../../classes/part-36-calidad-rendimiento-y-resiliencia/README.md), Calidad, rendimiento y resiliencia.
- [SE-523 — Migraciones de datos sin interrupción](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-523-migraciones-de-datos-sin-interrupcion/README.md) — [Parte 43](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/README.md), Mantenimiento y modernización legacy.
- [SE-596 — Ejecución durable, reintentos e idempotencia](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-596-ejecucion-durable-reintentos-e-idempotencia/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

**También se usa en** (71 clases más lo mencionan; las que más):

[SE-417](../../../classes/part-34-saas-y-plataformas-de-producto/se-417-pagos-idempotencia-y-conciliacion/README.md), [SE-294](../../../classes/part-24-software-especializado-y-dominios/se-294-fintech-contabilidad-e-invariantes-monetarias/README.md), [SE-171](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-171-interaccion-affordances-y-retroalimentacion/README.md), [SE-264](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-264-proyecto-cliente-multiplataforma-con-sincronizacion/README.md), [SE-575](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-575-taller-detener-recuperar-y-evaluar-un-agente/README.md), [SE-237](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-237-pwa-cache-offline-y-sincronizacion/README.md), [SE-319](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-319-enterprise-integration-patterns-como-lenguaje-comun/README.md), [SE-420](../../../classes/part-34-saas-y-plataformas-de-producto/se-420-taller-y-proyecto-integrador-producto-saas-minimo-con-evidencia/README.md).

**Aparece en los casos de estudio:** [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md), [Spotify](../../../casos/exito/spotify.md), [Airbnb](../../../casos/exito/airbnb.md), [Stripe](../../../casos/exito/stripe.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [RFC 9110: Idempotent Methods](https://www.rfc-editor.org/rfc/rfc9110.html#name-idempotent-methods) — definición de idempotencia; autoridad: IETF.
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) — Api pública, versiones, prereleases y compatibilidad declarada; autoridad: Semantic Versioning project.
- [Python Packaging User Guide: Specifications](https://packaging.python.org/en/latest/specifications/) — Metadata, nombres, versiones, dependencias y artefactos de distribución; autoridad: Python Packaging Authority.
- [pylock.toml Specification](https://packaging.python.org/en/latest/specifications/pylock-toml/) — Lock files para instalaciones reproducibles y selección por entorno; autoridad: Python Packaging Authority.
- [Python Standard Library](https://docs.python.org/3/library/index.html) — Argparse, importlib.metadata, subprocess y apis de automatización; autoridad: Python Software Foundation.

---

[↑ Glosario](../../README.md) · [← IaaS](./iaas.md) · [Idempotente →](./idempotente.md)
