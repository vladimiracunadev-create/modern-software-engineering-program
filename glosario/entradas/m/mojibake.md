# Mojibake

[↑ Glosario](../../README.md) · [← Módulo, paquete e importación](./modulo-paquete-e-importacion.md) · [Monitor →](./monitor.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Texto ilegible por interpretación incompatible de bytes.

Definición de trabajo de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md).

## Por qué importa

En [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md), el tema «Mojibake» importa porque bytes se decodifican con contrato incorrecto

## Cómo funciona

[SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Caso medido en la sección «Mojibake conserva un rastro causal» de [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md):

Si bytes UTF-8 `C3 AD` se decodifican como Windows-1252 aparecen `Ã­`. Si ese texto se guarda en UTF-8, nace una segunda capa. Reparar exige conocer o inferir con evidencia la cadena; aplicar sustituciones globales puede dañar texto legítimo. Se conserva copia, se prueba en muestra y se valida round-trip.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)) son:

- **`len()` se interpreta como caracteres visibles** — causa: puntos y grafemas confundidos. Corrección: declara la unidad que cuentas.
- **texto “arreglado” con reemplazos** — causa: se atacó apariencia. Corrección: reconstruye codificación y conserva original.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md)) son: No cubre segmentación completa ni seguridad de identificadores. `SE-016` estudia números y precisión.

## Relación con otros conceptos

- **Prerrequisito:** [Byte](../b/byte.md).
- **Ver también:** [Interpretación](../i/interpretacion.md), [Codificación](../c/codificacion.md), [Grafema](../g/grafema.md), [Normalización](../n/normalizacion.md), [Punto de código](../p/punto-de-codigo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-015 — Texto, Unicode, codificaciones y mojibake](../../../classes/part-01-computadores-y-representacion-de-informacion/se-015-texto-unicode-codificaciones-y-mojibake/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-067](../../../classes/part-05-fundamentos-de-programacion/se-067-entrada-salida-y-serializacion/README.md), [SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), [SE-016](../../../classes/part-01-computadores-y-representacion-de-informacion/se-016-enteros-coma-flotante-precision-y-errores-numericos/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Módulo, paquete e importación](./modulo-paquete-e-importacion.md) · [Monitor →](./monitor.md)
