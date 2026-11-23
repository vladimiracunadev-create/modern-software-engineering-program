# Subida reanudable

[↑ Glosario](../../README.md) · [← Subcomando](./subcomando.md) · [Subproblemas superpuestos →](./subproblemas-superpuestos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Protocolo que permite continuar una subida interrumpida desde el último desplazamiento confirmado.

Definición de trabajo de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md).

## Por qué importa

En [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), el tema «Subida reanudable» importa porque con caídas frecuentes, reiniciar multiplica los datos enviados; reanudar los repite solo hasta el último trozo confirmado.

## Cómo funciona

Según [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md), en la sección «Subida reanudable»:

Si la conexión cae al 80 %, reiniciar descarta 80 MiB ya enviados. En una subida **reanudable** el cliente divide el archivo en trozos y el servidor recuerda cuántos bytes recibió; tras un corte, el cliente pregunta el desplazamiento y continúa. Lo que se repite es, como máximo, el trozo en curso. Un trozo grande repite más; uno pequeño exige más confirmaciones. El protocolo tus es un ejemplo publicado de este diseño.

## Ejemplo

Caso medido en la sección «Subida reanudable» de [SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md):

Si la conexión cae al 80 %, reiniciar descarta 80 MiB ya enviados. En una subida **reanudable** el cliente divide el archivo en trozos y el servidor recuerda cuántos bytes recibió; tras un corte, el cliente pregunta el desplazamiento y continúa. Lo que se repite es, como máximo, el trozo en curso. Un trozo grande repite más; uno pequeño exige más confirmaciones. El protocolo tus es un ejemplo publicado de este diseño.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)) son:

- **El servidor se queda sin memoria con pocas subidas** — causa: se lee el cuerpo completo. Corrección: procesar por trozos y limitar subidas simultáneas.
- **Una caída obliga a empezar de cero** — causa: subida sin reanudación. Corrección: trozos confirmados y consulta del desplazamiento.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-248 — Archivos, streaming y cargas extensas](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con una historia técnica más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2): resultados idénticos salvo los tiempos y los nombres con barra invertida. No se usó ningún formato real de archivo ni se midió a ninguna persona: el archivo, la tasa de caídas y los nombres son construcciones del autor. La siguiente clase protege el servicio de la avalancha de solicitudes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-247](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-247-jobs-colas-y-procesamiento-diferido/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Desplazamiento](../d/desplazamiento.md), [Almacenamiento temporal](../a/almacenamiento-temporal.md), [Bloque en memoria](../b/bloque-en-memoria.md), [Bomba de descompresión](../b/bomba-de-descompresion.md), [Flujo](../f/flujo.md), [Huella](../h/huella.md).
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

[↑ Glosario](../../README.md) · [← Subcomando](./subcomando.md) · [Subproblemas superpuestos →](./subproblemas-superpuestos.md)
