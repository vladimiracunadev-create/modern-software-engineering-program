# Base

[↑ Glosario](../../README.md) · [← Barrido por etiqueta](./barrido-por-etiqueta.md) · [Base rate →](./base-rate.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md)

## Definición

Cantidad de dígitos y pesos de una notación posicional.

Definición de trabajo de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md).

## Por qué importa

En [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md), el tema «Base posicional» importa porque pesos por potencia

## Cómo funciona

Según [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md):

En base `b`, cada dígito pesa una potencia de `b`. `1011₂` vale `1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11`. Hexadecimal agrupa cuatro bits por dígito y facilita inspección: `0x0B` expresa el mismo valor. Convertir no cambia el valor; cambia la notación. Verifica reconstruyendo la suma, no mediante memoria visual.

## Ejemplo

Ejemplo de [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) (sección «Práctica guiada»):

Usa como base el laboratorio ejecutable de la [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md); trabaja sobre una copia o conserva tus salidas en el directorio `work/SE-014/`.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md)) son:

- **conversión aprendida de memoria** — causa: falta modelo posicional. Corrección: reconstruye pesos y suma.
- **overflow no aparece en Python** — causa: entero arbitrario oculta ancho. Corrección: valida rango o usa serialización fija.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La conversión entre bases es mecánica; lo que no es mecánico es saber qué formato aplica. ([SE-014](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-013](../../../classes/part-01-computadores-y-representacion-de-informacion/se-013-arquitectura-basica-de-un-computador-moderno/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Bit](./bit.md), [Byte](./byte.md), [Endianess](../e/endianess.md), [Overflow](../o/overflow.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-014 — Bits, bytes, bases numéricas y representación](../../../classes/part-01-computadores-y-representacion-de-informacion/se-014-bits-bytes-bases-numericas-y-representacion/README.md) — [Parte 01](../../../classes/part-01-computadores-y-representacion-de-informacion/README.md), Computadores y representación de información.

**También se usa en** (367 clases más lo mencionan; las que más):

[SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md), [SE-605](../../../classes/part-50-machine-learning-en-produccion-y-mlops/se-605-ajuste-fino-adaptacion-y-costo/README.md), [SE-153](../../../classes/part-12-ingenieria-de-requisitos/se-153-gestion-de-cambios-y-lineas-base/README.md), [SE-318](../../../classes/part-26-patrones-de-diseno-empresariales-y-de-resiliencia/se-318-repository-unit-of-work-y-active-record/README.md), [SE-356](../../../classes/part-29-datos-persistencia-y-recuperacion/se-356-caches-y-consistencia-entre-capas/README.md), [SE-250](../../../classes/part-20-backend-apis-y-procesamiento-asincrono/se-250-health-readiness-y-shutdown-ordenado/README.md), [SE-328](../../../classes/part-27-arquitectura-de-software-y-dominio/se-328-capas-hexagonal-clean-y-ports-and-adapters/README.md), [SE-427](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-427-dobles-virtualizacion-y-entornos-de-prueba/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Uber](../../../casos/exito/uber.md), [Mercado Libre](../../../casos/exito/mercado-libre.md), [Amazon](../../../casos/exito/amazon.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Barrido por etiqueta](./barrido-por-etiqueta.md) · [Base rate →](./base-rate.md)
