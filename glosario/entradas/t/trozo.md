# Trozo

[↑ Glosario](../../README.md) · [← Troncal](./troncal.md) · [Trunk-based development →](./trunk-based-development.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Porción de un archivo que se envía y confirma como unidad.

Definición de trabajo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md).

## Por qué importa

En [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), el tema «Flujo frente a bloque» importa porque procesar por trozos acota la memoria por subida; leer todo la hace proporcional al tamaño.

## Cómo funciona

Según [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

Un **bloque** es un archivo leído entero en memoria; un **flujo** es una secuencia de trozos procesados y descartados. Para calcular una huella o guardar un archivo no hace falta tenerlo entero: se lee un trozo, se actualiza el hash o se escribe, y se continúa. La memoria pico pasa de ser proporcional al tamaño del archivo a ser proporcional al del trozo. El tamaño del trozo es un compromiso entre llamadas al sistema (trozos pequeños) y memoria por subida (trozos grandes); en la medición, trozos de 64 KiB y 1 MiB dieron el mismo tiempo.

Según [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

La plataforma recibe archivos de hasta 500 MiB por trozos de 5 MiB. Cada subida tiene un identificador, un desplazamiento consultable y un plazo de 24 horas; el cliente envía la huella al empezar. El servidor escribe en un directorio temporal, calcula la huella en flujo, rechaza la subida si el tamaño o la huella no coinciden, genera el nombre definitivo, comprueba el tipo por contenido y no por extensión, y encola el análisis. Los archivos comprimidos se descomprimen en el trabajo diferido con tope de salida. Compara con el original en tres casos: una conexión que cae, 50 subidas simultáneas y un nombre con `..`.

## Ejemplo

Ejemplo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sección «Ejemplo mínimo»):

El fragmento calcula una huella por trozos y la compara con la de un bloque. Antes de ejecutarlo, predice si coinciden.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El servidor se queda sin memoria con pocas subidas** — causa: se lee el cuerpo completo. Corrección: procesar por trozos y limitar subidas simultáneas. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))
- **Una caída obliga a empezar de cero** — causa: subida sin reanudación. Corrección: trozos confirmados y consulta del desplazamiento. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))
- **Un archivo pequeño llena el disco al descomprimir** — causa: sin tope de salida. Corrección: descomprimir por trozos con tope. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Para calcular una huella o guardar un archivo no hace falta tenerlo entero: se lee un trozo, se actualiza el hash o se escribe, y se continúa. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Almacenamiento temporal](../a/almacenamiento-temporal.md), [Bloque en memoria](../b/bloque-en-memoria.md), [Bomba de descompresión](../b/bomba-de-descompresion.md), [Desplazamiento](../d/desplazamiento.md), [Flujo](../f/flujo.md), [Huella](../h/huella.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

**También se usa en** (10 clases más lo mencionan; las que más):

[SE-214](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-214-documentacion-para-humanos-maquinas-y-llm/README.md), [SE-105](../../../classes/part-08-entornos-herramientas-y-depuracion/se-105-reproduccion-de-errores-y-reduccion-de-casos/README.md), [SE-230](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-230-javascript-dom-y-eventos-del-navegador/README.md), [SE-262](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-262-firma-sandbox-y-seguridad-del-cliente/README.md), [SE-271](../../../classes/part-22-embedded-iot-y-tiempo-real/se-271-actualizaciones-ota-y-recuperacion/README.md), [SE-385](../../../classes/part-32-concurrencia-y-sistemas-distribuidos/se-385-concurrencia-paralelismo-y-asincronia/README.md), [SE-496](../../../classes/part-41-observabilidad-sre-e-incidentes/se-496-trazas-distribuidas-y-contexto/README.md), [SE-074](../../../classes/part-06-paradigmas-de-programacion/se-074-programacion-procedural-y-descomposicion-funcional/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — huellas calculadas por trozos; autoridad: Python Software Foundation.
- [Python: tracemalloc](https://docs.python.org/3/library/tracemalloc.html) — medición de memoria asignada; autoridad: Python Software Foundation.
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html) — directorios temporales con limpieza; autoridad: Python Software Foundation.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — longitud del contenido y solicitudes parciales; autoridad: IETF.
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación y límites de entrada; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Troncal](./troncal.md) · [Trunk-based development →](./trunk-based-development.md)
