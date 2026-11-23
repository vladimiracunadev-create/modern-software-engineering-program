# Inquilino venenoso

[↑ Glosario](../../README.md) · [← Inquilino](./inquilino.md) · [Instalación atómica →](./instalacion-atomica.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Inquilino cuya petición provoca un fallo repetible en el recurso que la atiende.

Definición de trabajo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md).

## Por qué importa

La clase donde se define, [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md), existe con este propósito: la clase existe para que puedas tratar el radio de impacto de un fallo como una propiedad que se diseña y se mide, no como un resultado de la suerte.

## Cómo funciona

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

Con 1 000 inquilinos asignados a las 8 celdas por hash por encuentro, el inquilino venenoso quedó en una celda con otros 108, de modo que el fallo afectó a 109 de 1 000 (10,9 %), alrededor de un octavo y distinto de 12,5 % porque el reparto no es exacto. En la flota compartida, con el supuesto de que los reintentos recorren todos los trabajadores, el fallo alcanza a 1 000 de 1 000. La celda no evitó el incidente; lo acotó a una fracción que el diseño fija de antemano. La pregunta de seguimiento es siempre la misma: ¿cuántos inquilinos caben en una celda sin que el fallo de una sea inaceptable y sin que el costo de tener muchas sea excesivo?

Según [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md):

Es una alternativa más barata cuando el riesgo es un número pequeño de inquilinos venenosos y la protección parcial es aceptable. No ofrece aislamiento de datos ni de despliegue, y se debilita con varios inquilinos defectuosos.

## Ejemplo

Ejemplo de [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) (sección «Preguntas frecuentes»):

Es una alternativa más barata cuando el riesgo es un número pequeño de inquilinos venenosos y la protección parcial es aceptable. No ofrece aislamiento de datos ni de despliegue, y se debilita con varios inquilinos defectuosos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con 1 000 inquilinos asignados a las 8 celdas por hash por encuentro, el inquilino venenoso quedó en una celda con otros 108, de modo que el fallo afectó a 109 de 1 000 (10,9 %), alrededor de un octavo y distinto de 12,5 % porque el reparto no es exacto. ([SE-344](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Inquilino](./inquilino.md).
- **Ver también:** [Recurso](../r/recurso.md), [Celda](../c/celda.md), [Enrutador](../e/enrutador.md), [Enrutador de celdas](../e/enrutador-de-celdas.md), [Fragmentación aleatoria](../f/fragmentacion-aleatoria.md), [Hash por encuentro](../h/hash-por-encuentro.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-344 — Arquitectura celular y radio de impacto](../../../classes/part-28-estilos-arquitectonicos/se-344-arquitectura-celular-y-radio-de-impacto/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Inquilino](./inquilino.md) · [Instalación atómica →](./instalacion-atomica.md)
