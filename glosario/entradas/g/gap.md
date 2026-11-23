# Gap

[↑ Glosario](../../README.md) · [← Gancho](./gancho.md) · [Garantía →](./garantia.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md)

## Definición

Pregunta necesaria que la evidencia disponible no responde.

Definición de trabajo de [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md).

## Por qué importa

Su importancia se desarrolla en las clases enlazadas en «Dónde se enseña».

## Cómo funciona

Según [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md):

Un **gap** no es cualquier ausencia de documentación. Es una pregunta necesaria para evaluar la capacidad que no puede resolverse con evidencia disponible. Se prioriza por consecuencia, probabilidad razonada, alcance y costo de obtener evidencia. “No conozco el color del tablero interno” puede ser desconocido y no relevante; “no sé si repetir la solicitud duplica el cobro” cambia la decisión.

Según [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md):

Elige el producto de referencia del repositorio y escribe un informe de cinco afirmaciones usando *solo* su README. A continuación contrasta cada una con el contrato (OpenAPI), la configuración y las pruebas. **Síntoma esperado:** al menos una afirmación («operación segura», «datos cifrados», «idempotente») resulta más amplia que lo que sostienen el contrato o las pruebas. **Causa:** el README expresa intención, no comportamiento verificado. **Corrección de método:** clasifica cada afirmación como observada, inferida o desconocida, sustituye la frase por una que cite ruta y versión, y registra el gap que falta cerrar. Anota también tu primera contradicción como evidencia de que el método funciona: no la escondas para que el informe parezca más sólido.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md):

En el producto de referencia, sigue la creación de una solicitud desde OpenAPI hasta requisitos, arquitectura, pruebas y runbook. Si el contrato admite reintento pero no hay idempotencia documentada, registra riesgo, no afirmes defecto ejecutado.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **ausencia de archivo se declara defecto** — causa: evidencia negativa exagerada. Corrección: registra gap y evidencia necesaria antes de concluir. ([SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un **gap** no es cualquier ausencia de documentación. ([SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-001](../../../classes/part-00-ingenieria-de-software-como-profesion/se-001-software-sistemas-y-productos-fronteras-de-la-disciplina/README.md), [SE-010](../../../classes/part-00-ingenieria-de-software-como-profesion/se-010-como-leer-estandares-documentacion-y-literatura-tecnica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](../e/evidencia.md), [Contrato](../c/contrato.md), [Evidencia negativa](../e/evidencia-negativa.md), [Flujo vertical](../f/flujo-vertical.md), [Fuente de verdad](../f/fuente-de-verdad.md), [Punto de entrada](../p/punto-de-entrada.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-011 — Taller: anatomía verificable de un producto real](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md) — [Parte 00](../../../classes/part-00-ingenieria-de-software-como-profesion/README.md), Ingeniería de software como profesión.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Gancho](./gancho.md) · [Garantía →](./garantia.md)
