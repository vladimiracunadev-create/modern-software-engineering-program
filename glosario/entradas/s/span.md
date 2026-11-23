# Span

[↑ Glosario](../../README.md) · [← SOUP](./soup.md) · [Spec-anchored →](./spec-anchored.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md)

## Definición

Tramo de una traza con nombre, inicio, duración, atributos y referencia a su padre.

Definición de trabajo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md).

## Por qué importa

En [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), el tema «Traza y span» importa porque el modelo define qué se puede preguntar.

## Cómo funciona

Según [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md):

Una **traza** es el recorrido de una petición por un sistema; está formada por **spans**, cada uno con un nombre, un instante de inicio, una duración, atributos y una referencia a su span padre. El conjunto de relaciones padre-hijo forma un árbol. Dos tiempos describen cada span: su duración total, que incluye a sus hijos, y su **tiempo propio**, que es la duración menos el tiempo cubierto por los hijos. El tiempo propio indica dónde se gasta de verdad el tiempo (`SE-493`). Los atributos del span (endpoint, versión, estado, identificador de institución) son las dimensiones por las que se puede agrupar después, con la misma advertencia de cardinalidad y de datos personales que en las métricas.

Según [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo hace el inventario de fronteras de la API de entregas: pasarela → API (HTTP, propaga solo), API → cola (el cliente de mensajería no copia propiedades), cola → trabajador (el trabajador lee el mensaje sin contexto), trabajador → hilo de procesamiento de archivos (grupo de hilos sin contexto) y trabajador → almacenamiento (HTTP, propaga solo). Tres de las cinco fronteras necesitan trabajo explícito. Escriben una prueba por frontera: enviar un identificador en la entrada y comprobar que el span de salida lo tiene como padre.

## Ejemplo

Ejemplo de [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) (sección «Ejemplo profesional»):

Supón, como caso hipotético de la plataforma y no como medición, que el equipo hace el inventario de fronteras de la API de entregas: pasarela → API (HTTP, propaga solo), API → cola (el cliente de mensajería no copia propiedades), cola → trabajador (el trabajador lee el mensaje sin contexto), trabajador → hilo de procesamiento de archivos (grupo de hilos sin contexto) y trabajador → almacenamiento (HTTP, propaga solo). Tres de las cinco fronteras necesitan trabajo explícito. Escriben una prueba por frontera: enviar un identificador en la entrada y comprobar que el span de salida lo tiene como padre.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Una traza está completa pero la mejora no llega** — causa: se optimizó un span fuera de la ruta crítica. Corrección: calcular la ruta crítica antes de elegir. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **El muestreo de cola decide mal** — causa: los spans de una traza llegan a recolectores distintos. Corrección: enrutar por hash del identificador de traza. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una **traza** es el recorrido de una petición por un sistema; está formada por **spans**, cada uno con un nombre, un instante de inicio, una duración, atributos y una referencia a su span padre. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))
- **optimizar el span más largo cuando no está en la ruta crítica**. ([SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Atributo](../a/atributo.md), [Referencia](../r/referencia.md), [Traza](../t/traza.md), [Contexto de traza](../c/contexto-de-traza.md), [Muestreo](../m/muestreo.md), [Muestreo de cola](../m/muestreo-de-cola.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-496 — Trazas distribuidas y contexto](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md) — [Parte 41](../../../classes/part-41-observabilidad-sre-e-incidentes/README.md), Observabilidad, SRE e incidentes.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-494](../../../classes/part-41-observabilidad-sre-e-incidentes/se-494-logs-estructurados-y-correlacion/README.md), [SE-585](../../../classes/part-48-harness-y-agentic-engineering/se-585-observabilidad-y-evals-del-propio-harness/README.md), [SE-229](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-229-plataforma-web-html-semantico-y-css/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-382](../../../classes/part-31-integracion-eventos-y-mensajeria/se-382-observabilidad-y-seguridad-de-integraciones/README.md), [SE-493](../../../classes/part-41-observabilidad-sre-e-incidentes/se-493-senales-eventos-y-observabilidad-util/README.md).

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

[↑ Glosario](../../README.md) · [← SOUP](./soup.md) · [Spec-anchored →](./spec-anchored.md)
