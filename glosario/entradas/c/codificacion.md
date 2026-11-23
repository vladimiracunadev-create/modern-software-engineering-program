# Codificación

[↑ Glosario](../../README.md) · [← Code unit](./code-unit.md) · [Codificación de salida →](./codificacion-de-salida.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Transformación entre texto modelado y unidades binarias.

Definición de trabajo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Por qué importa

La clase donde se define, [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), existe con este propósito: la clase existe para distinguir carácter, punto de código, unidades de código, bytes y glifo al diagnosticar texto.

## Cómo funciona

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

**Cómo leer la figura.** Cada fila lleva un carácter desde su número Unicode hasta los bytes de dos codificaciones. `A` ocupa un byte en UTF-8, idéntico a ASCII; `í` ocupa dos; `€`, tres; y el emoji, cuatro. En UTF-16 los tres primeros caben en una unidad de 16 bits, pero el emoji, que supera U+FFFF, necesita un *par sustituto* de dos unidades (`D83D DE00`). Por eso «Unicode de 16 bits» es una frase incorrecta: Unicode no tiene ancho; las codificaciones sí. **Dónde deja de valer:** los valores corresponden a las formas de codificación UTF-8 y UTF-16 big-endian; UTF-16 little-endian invierte los bytes de cada unidad, y UTF-32 usa siempre cuatro bytes por punto.

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Normalmente no. El BOM en UTF-8 es la secuencia `EF BB BF` y solo sirve como firma, ya que UTF-8 no tiene orden de bytes. Algunos programas lo exigen para reconocer la codificación y otros lo muestran como un carácter extraño al inicio del archivo. Decide según el consumidor y declara la decisión; Python lo maneja con la codificación `utf-8-sig`.

## Ejemplo

Ejemplo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) (sección «Preguntas frecuentes»):

Normalmente no. El BOM en UTF-8 es la secuencia `EF BB BF` y solo sirve como firma, ya que UTF-8 no tiene orden de bytes. Algunos programas lo exigen para reconocer la codificación y otros lo muestran como un carácter extraño al inicio del archivo. Decide según el consumidor y declara la decisión; Python lo maneja con la codificación `utf-8-sig`.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **texto “arreglado” con reemplazos** — causa: se atacó apariencia. Corrección: reconstruye codificación y conserva original. ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los valores corresponden a las formas de codificación UTF-8 y UTF-16 big-endian; ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Grafema](../g/grafema.md), [Mojibake](../m/mojibake.md), [Normalización](../n/normalizacion.md), [Punto de código](../p/punto-de-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (52 clases más lo mencionan; las que más):

[SE-236](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-236-seguridad-del-navegador-y-politicas-de-contenido/README.md), [SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), [SE-460](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-460-validacion-codificacion-y-clases-de-inyeccion/README.md), [SE-452](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-452-codificacion-segura-misra-y-cert/README.md), [SE-113](../../../classes/part-09-bibliotecas-paquetes-sdk-y-automatizacion/se-113-cli-flags-configuracion-y-codigos-de-salida/README.md), [SE-234](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-234-navegacion-routing-y-urls-durables/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md), [SE-441](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-441-compatibilidad-portabilidad-e-interoperabilidad/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Code unit](./code-unit.md) · [Codificación de salida →](./codificacion-de-salida.md)
