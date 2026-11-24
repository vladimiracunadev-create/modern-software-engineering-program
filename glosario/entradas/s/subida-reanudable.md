# Subida reanudable

[↑ Glosario](../../README.md) · [← Subcomando](./subcomando.md) · [Subproblemas superpuestos →](./subproblemas-superpuestos.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** D — Superficies y formas de software · **Primera aparición:** [Parte 20](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)

## Definición

Una **subida reanudable** (*resumable upload*) es un protocolo que permite continuar una subida interrumpida desde el último desplazamiento confirmado. Es el sentido de [SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md) (archivos, streaming y cargas extensas). No es una subida «más rápida»: es una subida que sobrevive a cortes sin repetir lo ya recibido.

## Por qué importa

Con caídas frecuentes (redes móviles, archivos grandes), reiniciar multiplica los datos enviados; reanudar los repite solo hasta el último trozo confirmado. Para quien sube un archivo de cientos de megabytes por una red inestable, es la diferencia entre completar o abandonar.

## Cómo funciona

[SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md): si la conexión cae al 80 %, reiniciar descarta 80 MiB ya enviados. En una subida reanudable:

1. El cliente **divide el archivo en trozos.**
2. El servidor **recuerda cuántos bytes recibió** (el desplazamiento confirmado).
3. Tras un corte, el cliente **pregunta el desplazamiento** y continúa desde ahí.

Lo que se repite es, como máximo, el trozo en curso. El tamaño del trozo es un intercambio: un trozo grande repite más al fallar; uno pequeño exige más confirmaciones y más sobrecarga. La clase cita como ejemplo publicado de este diseño el protocolo **tus**, un protocolo abierto para subidas reanudables sobre HTTP.

Dos requisitos de diseño que se derivan: el servidor debe **persistir** el desplazamiento (si lo pierde, no hay reanudación) y debe **verificar la integridad** al final (una suma o huella del archivo completo), porque un trozo mal ensamblado no se vería en el desplazamiento.

## Ejemplo

Ilustración numérica propia con la cifra de la clase: un archivo de 100 MiB, con corte al 80 %. Sin reanudación, el reintento envía otros 100 MiB y el total llega a 180 MiB. Con trozos de 5 MiB, el cliente consulta el desplazamiento (80 MiB) y envía los 20 MiB restantes; en el peor caso repite 5 MiB.

## Errores y confusiones comunes

- **El servidor se queda sin memoria con pocas subidas:** lee el cuerpo completo. Corrección: procesar por trozos y limitar subidas simultáneas ([SE-248](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-248-archivos-streaming-y-cargas-extensas/README.md)).
- **Una caída obliga a empezar de cero:** falta el protocolo de reanudación.
- **No verificar la integridad del archivo ensamblado.**
- **Dejar sesiones de subida abiertas indefinidamente,** que consumen almacenamiento.

## Límites y cuándo no aplica

Para archivos pequeños la sobrecarga de confirmaciones no compensa. Requiere estado en el servidor (sesiones de subida) y una política de caducidad de las incompletas. No resuelve la autorización ni la validación del contenido subido.

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
