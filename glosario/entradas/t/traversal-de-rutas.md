# Traversal de rutas

[↑ Glosario](../../README.md) · [← Traspaso](./traspaso.md) · [Traza →](./traza.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Uso de componentes como `..` para alcanzar archivos fuera del directorio previsto.

Definición de trabajo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md).

## Por qué importa

La clase donde se define, [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), existe con este propósito: la clase existe para que trates los archivos como flujos y no como bloques en memoria, midas cuánta memoria retiene cada diseño de lectura, reanudes una subida interrumpida repitiendo lo mínimo, detectes un archivo truncado y pongas límites a nombres, tamaños y descompresión.

## Cómo funciona

[SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

La plataforma recibe archivos de hasta 500 MiB por trozos de 5 MiB. Cada subida tiene un identificador, un desplazamiento consultable y un plazo de 24 horas; el cliente envía la huella al empezar. El servidor escribe en un directorio temporal, calcula la huella en flujo, rechaza la subida si el tamaño o la huella no coinciden, genera el nombre definitivo, comprueba el tipo por contenido y no por extensión, y encola el análisis. Los archivos comprimidos se descomprimen en el trabajo diferido con tope de salida.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)) son:

- **El servidor se queda sin memoria con pocas subidas** — causa: se lee el cuerpo completo. Corrección: procesar por trozos y limitar subidas simultáneas.
- **Una caída obliga a empezar de cero** — causa: subida sin reanudación. Corrección: trozos confirmados y consulta del desplazamiento.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): resultados idénticos salvo los tiempos y los nombres con barra invertida. No se usó ningún formato real de archivo ni se midió a ninguna persona: el archivo, la tasa de caídas y los nombres son construcciones del autor. La siguiente clase protege el servicio de la avalancha de solicitudes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Componente](../c/componente.md), [Almacenamiento temporal](../a/almacenamiento-temporal.md), [Bloque en memoria](../b/bloque-en-memoria.md), [Bomba de descompresión](../b/bomba-de-descompresion.md), [Desplazamiento](../d/desplazamiento.md), [Flujo](../f/flujo.md).
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

[↑ Glosario](../../README.md) · [← Traspaso](./traspaso.md) · [Traza →](./traza.md)
