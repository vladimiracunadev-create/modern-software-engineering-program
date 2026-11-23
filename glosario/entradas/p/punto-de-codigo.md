# Punto de código

[↑ Glosario](../../README.md) · [← Punto de captura](./punto-de-captura.md) · [Punto de compromiso →](./punto-de-compromiso.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Valor del espacio Unicode.

Definición de trabajo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Por qué importa

En [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), el tema «Modelo Unicode» importa porque asigna puntos de código a caracteres abstractos

## Cómo funciona

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Un carácter abstracto pertenece al repertorio Unicode. Un **punto de código** es su número. Una **unidad de código** es una unidad de una forma como UTF-16. Un **grafema** es una unidad que una persona percibe como carácter y puede reunir varios puntos. Por eso `len()` depende del modelo del lenguaje y no siempre cuenta símbolos percibidos.

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Porque cuentan unidades distintas. Python cuenta puntos de código y el emoji es uno; las cadenas de JavaScript se indexan por unidades UTF-16, y el emoji ocupa dos. Cuando una frontera entre sistemas usa índices o longitudes, hay que fijar qué se cuenta (puntos, unidades o bytes) o los cortes caerán en mitad de un carácter.

## Ejemplo

Ejemplo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) (sección «Ejemplo mínimo»):

`'í'.encode('utf-8').hex()` devuelve `c3ad`. Decodificar esos bytes como latin-1 crea dos puntos de código; volver a codificar no recupera significado sin conocer el error.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)) son:

- **`len()` se interpreta como caracteres visibles** — causa: puntos y grafemas confundidos. Corrección: declara la unidad que cuentas.
- **texto “arreglado” con reemplazos** — causa: se atacó apariencia. Corrección: reconstruye codificación y conserva original.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- UTF-8 reparte el número de un punto de código en uno a cuatro bytes con un esquema que permite reconocer, mirando solo los primeros bits, qué papel cumple cada byte: ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Valor](../v/valor.md), [Codificación](../c/codificacion.md), [Grafema](../g/grafema.md), [Mojibake](../m/mojibake.md), [Normalización](../n/normalizacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (7 clases más lo mencionan; las que más):

[SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md), [SE-023](../../../classes/part-01-computadores-y-representacion-de-informacion/se-023-taller-observar-un-programa-desde-el-codigo-hasta-la-maquina/README.md), [SE-522](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-522-migraciones-de-runtime-lenguaje-y-framework/README.md), [SE-066](../../../classes/part-05-fundamentos-de-programacion/se-066-colecciones-y-transformacion-de-datos/README.md), [SE-090](../../../classes/part-07-estructuras-de-datos-y-algoritmos/se-090-busqueda-ordenamiento-y-seleccion/README.md), [SE-221](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-221-tui-terminales-y-accesibilidad/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Punto de captura](./punto-de-captura.md) · [Punto de compromiso →](./punto-de-compromiso.md)
