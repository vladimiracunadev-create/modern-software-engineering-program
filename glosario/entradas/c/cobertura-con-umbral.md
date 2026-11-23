# Cobertura con umbral

[↑ Glosario](../../README.md) · [← Cobertura combinatoria](./cobertura-combinatoria.md) · [Cobertura de condiciones →](./cobertura-de-condiciones.md)

> **Tipo:** métrica · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** H — Ingeniería de software nativa con IA · **Primera aparición:** [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md)

## Definición

Fracción de solicitudes que el enrutador acepta por su confianza.

Definición de trabajo de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md).

## Por qué importa

La clase donde se define, [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md), existe con este propósito: la clase existe para que construyas workflows con modelos de lenguaje a partir de tres piezas pequeñas y medibles:

## Cómo funciona

Según [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md):

**Cómo leer la figura.** El eje horizontal es el ruido en el texto y el vertical el acierto o la cobertura; la línea coral son las palabras clave, la verde azulada el clasificador por trigramas y la dorada la cobertura del clasificador con umbral, que acierta el 100 % de lo que acepta. Mira cómo cae la línea coral y cómo el umbral compra acierto a costa de cobertura. Lo deseable es que la cobertura con umbral sea alta sin perder el acierto.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md):

*Escenario ilustrativo: las cifras de este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Lo deseable es que la cobertura con umbral sea alta sin perder el acierto. ([SE-590](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-589](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-589-workflows-frente-a-agentes-cuando-no-usar-un-agente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Confianza](./confianza.md), [Enrutador](../e/enrutador.md), [Encadenado](../e/encadenado.md), [Puerta](../p/puerta.md), [Seccionamiento](../s/seccionamiento.md), [Votación](../v/votacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-590 — Encadenado, enrutamiento y paralelización](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/se-590-encadenado-enrutamiento-y-paralelizacion/README.md) — [Parte 49](../../../classes/part-49-patrones-agenticos-y-sistemas-con-llm/README.md), Patrones agénticos y sistemas con LLM.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Cobertura combinatoria](./cobertura-combinatoria.md) · [Cobertura de condiciones →](./cobertura-de-condiciones.md)
