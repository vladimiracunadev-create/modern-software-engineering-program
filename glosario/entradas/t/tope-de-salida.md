# Tope de salida

[↑ Glosario](../../README.md) · [← Tope de iteraciones](./tope-de-iteraciones.md) · [Tope de solicitudes en curso →](./tope-de-solicitudes-en-curso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Límite de bytes que una descompresión puede producir antes de abortarse.

Definición de trabajo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md).

## Por qué importa

La clase donde se define, [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), existe con este propósito: la clase existe para que trates los archivos como flujos y no como bloques en memoria, midas cuánta memoria retiene cada diseño de lectura, reanudes una subida interrumpida repitiendo lo mínimo, detectes un archivo truncado y pongas límites a nombres, tamaños y descompresión.

## Cómo funciona

Según [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

Un archivo comprimido puede ser mucho menor que su contenido: 10 MB de ceros ocupan 9,7 kB (razón 1 027:1) y una «bomba» de 200 MB, 194 kB. Descomprimir sin límite permite agotar disco o memoria. La defensa es descomprimir por trozos con un **tope de salida** y abortar al superarlo; el límite de entrada no basta.

Según [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

La plataforma recibe archivos de hasta 500 MiB por trozos de 5 MiB. Cada subida tiene un identificador, un desplazamiento consultable y un plazo de 24 horas; el cliente envía la huella al empezar. El servidor escribe en un directorio temporal, calcula la huella en flujo, rechaza la subida si el tamaño o la huella no coinciden, genera el nombre definitivo, comprueba el tipo por contenido y no por extensión, y encola el análisis. Los archivos comprimidos se descomprimen en el trabajo diferido con tope de salida. Compara con el original en tres casos: una conexión que cae, 50 subidas simultáneas y un nombre con `..`.

## Ejemplo

Ejemplo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (sección «Ejemplo profesional»):

La plataforma recibe archivos de hasta 500 MiB por trozos de 5 MiB. Cada subida tiene un identificador, un desplazamiento consultable y un plazo de 24 horas; el cliente envía la huella al empezar. El servidor escribe en un directorio temporal, calcula la huella en flujo, rechaza la subida si el tamaño o la huella no coinciden, genera el nombre definitivo, comprueba el tipo por contenido y no por extensión, y encola el análisis. Los archivos comprimidos se descomprimen en el trabajo diferido con tope de salida. Compara con el original en tres casos: una conexión que cae, 50 subidas simultáneas y un nombre con `..`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un archivo pequeño llena el disco al descomprimir** — causa: sin tope de salida. Corrección: descomprimir por trozos con tope. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La defensa es descomprimir por trozos con un **tope de salida** y abortar al superarlo; el límite de entrada no basta. ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Byte](../b/byte.md), [Límite](../l/limite.md), [Almacenamiento temporal](../a/almacenamiento-temporal.md), [Bloque en memoria](../b/bloque-en-memoria.md), [Bomba de descompresión](../b/bomba-de-descompresion.md), [Desplazamiento](../d/desplazamiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) — [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md), Backend, APIs y procesamiento asíncrono.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: tracemalloc](https://docs.python.org/3/library/tracemalloc.html) — medición de memoria asignada; autoridad: Python Software Foundation.
- [Python: hashlib](https://docs.python.org/3/library/hashlib.html) — huellas calculadas por trozos; autoridad: Python Software Foundation.
- [Python: tempfile](https://docs.python.org/3/library/tempfile.html) — directorios temporales con limpieza; autoridad: Python Software Foundation.
- [HTTP Semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110) — longitud del contenido y solicitudes parciales; autoridad: IETF.
- [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html) — validación y límites de entrada; autoridad: OWASP.

---

[↑ Glosario](../../README.md) · [← Tope de iteraciones](./tope-de-iteraciones.md) · [Tope de solicitudes en curso →](./tope-de-solicitudes-en-curso.md)
