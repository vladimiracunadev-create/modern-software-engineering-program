# Grafema

[↑ Glosario](../../README.md) · [← Graduador](./graduador.md) · [Grafo →](./grafo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Unidad aproximada percibida por una persona.

Definición de trabajo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Por qué importa

La clase donde se define, [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), existe con este propósito: la clase existe para distinguir carácter, punto de código, unidades de código, bytes y glifo al diagnosticar texto.

## Cómo funciona

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Un carácter abstracto pertenece al repertorio Unicode. Un **punto de código** es su número. Una **unidad de código** es una unidad de una forma como UTF-16. Un **grafema** es una unidad que una persona percibe como carácter y puede reunir varios puntos. Por eso `len()` depende del modelo del lenguaje y no siempre cuenta símbolos percibidos.

Según [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Repite con emoji compuesto y una escritura no latina; identifica puntos, grafema y bytes.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Una importación recibe CSV sin charset. En vez de probar hasta “verse bien”, se obtiene metadato del productor, se conserva original, se valida muestra multilingüe y se rechazan secuencias inválidas con informe de fila.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **`len()` se interpreta como caracteres visibles** — causa: puntos y grafemas confundidos. Corrección: declara la unidad que cuentas. ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- **Dónde deja de valer:** los conteos de grafemas siguen las reglas de segmentación de Unicode (Anexo 29), que varían con la versión del estándar y con el soporte de fuentes y sistemas; un mismo emoji compuesto puede mostrarse como uno o como varios símbolos según el entorno. ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))
- Repite con emoji compuesto y una escritura no latina; identifica puntos, grafema y bytes. ([SE-015](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Cohesión](../c/cohesion.md), [Codificación](../c/codificacion.md), [Mojibake](../m/mojibake.md), [Normalización](../n/normalizacion.md), [Punto de código](../p/punto-de-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-177](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-177-internacionalizacion-localizacion-y-formatos-culturales/README.md), [SE-233](../../../classes/part-19-web-frontend-y-aplicaciones-progresivas/se-233-formularios-validacion-y-experiencia-de-error/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Graduador](./graduador.md) · [Grafo →](./grafo.md)
