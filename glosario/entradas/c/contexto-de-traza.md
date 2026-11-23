# Contexto de traza

[↑ Glosario](../../README.md) · [← Contexto de trabajo](./contexto-de-trabajo.md) · [Contexto de uso →](./contexto-de-uso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Identificadores de traza y de span que viajan con la petición y permiten enlazar spans.

Definición de trabajo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md).

## Por qué importa

La clase donde se define, [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), existe con este propósito: la clase existe para que expliques cómo una traza sigue una petición a través de varios servicios, qué hay que hacer en cada frontera para que no se rompa, cómo se lee la ruta crítica para saber qué optimizar y qué se pierde al muestrear.

## Cómo funciona

[SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo hace el inventario de fronteras de la API de entregas: pasarela → API (HTTP, propaga solo), API → cola (el cliente de mensajería no copia propiedades), cola → trabajador (el trabajador lee el mensaje sin contexto), trabajador → hilo de procesamiento de archivos (grupo de hilos sin contexto) y trabajador → almacenamiento (HTTP, propaga solo). Tres de las cinco fronteras necesitan trabajo explícito.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md)) son:

- **Hay trazas huérfanas de 3 segundos** — causa: contexto perdido en un grupo de hilos o en una cola. Corrección: copiar el contexto explícitamente y probar la frontera.
- **Una traza está completa pero la mejora no llega** — causa: se optimizó un span fuera de la ruta crítica. Corrección: calcular la ruta crítica antes de elegir.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md)) son: Las definiciones son operativas para la API de entregas. No convierten términos con una historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con tiempo virtual y semillas fijas en Windows y Ubuntu (WSL2) con resultados idénticos.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Span](../s/span.md), [Traza](../t/traza.md), [Muestreo](../m/muestreo.md), [Muestreo de cola](../m/muestreo-de-cola.md), [Propagación de contexto](../p/propagacion-de-contexto.md), [Ruta crítica](../r/ruta-critica.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C Trace Context](https://www.w3.org/TR/trace-context/) — formato y reglas de `traceparent`; autoridad: Recomendación del W3C.
- [OpenTelemetry: propagación de contexto](https://opentelemetry.io/docs/concepts/context-propagation/) — cómo viaja el contexto; autoridad: proyecto OpenTelemetry (CNCF).
- [OpenTelemetry: muestreo](https://opentelemetry.io/docs/concepts/sampling/) — muestreo de cabeza y de cola; autoridad: proyecto OpenTelemetry (CNCF).
- [Sigelman et al., «Dapper»](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/) — trazado distribuido de bajo coste; autoridad: informe técnico de Google Research.
- [Python: re](https://docs.python.org/3/library/re.html) — expresiones regulares usadas para validar el formato; autoridad: documentación de Python.

---

[↑ Glosario](../../README.md) · [← Contexto de trabajo](./contexto-de-trabajo.md) · [Contexto de uso →](./contexto-de-uso.md)
