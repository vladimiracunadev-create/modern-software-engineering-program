# QM

[↑ Glosario](../../README.md) · [← QA / Test Automation Engineer](./qa-test-automation-engineer.md) · [Quality gate →](./quality-gate.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Nivel que solo requiere la gestión de calidad ordinaria, sin medidas específicas de seguridad.

Definición de trabajo de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md).

## Por qué importa

En [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), el tema «ASIL y QM» importa porque marca qué requiere proceso de seguridad y qué no.

## Cómo funciona

Según [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

Hay cuatro niveles de integridad, de A (menos exigente) a D (más exigente), y un nivel QM para lo que no requiere medidas de seguridad especiales más allá de la calidad habitual. El nivel pide más rigor de métodos, de verificación independiente y de métricas de hardware a medida que sube. La **descomposición** permite satisfacer un requisito de nivel alto con dos elementos redundantes de nivel menor, si de verdad son independientes; la norma exige demostrar esa independencia. Es la misma idea de causa común de `SE-445` y `SE-446`: la descomposición es válida solo en la medida en que no comparten una causa de fallo, y la mayoría de los fracasos del argumento están ahí.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Hay cuatro niveles de integridad, de A (menos exigente) a D (más exigente), y un nivel QM para lo que no requiere medidas de seguridad especiales más allá de la calidad habitual. ([SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Seguridad](../s/seguridad.md).
- **Ver también:** [Medida](../m/medida.md), [ASIL](../a/asil.md), [Cobertura de diagnóstico](../c/cobertura-de-diagnostico.md), [Descomposición](../d/descomposicion.md), [Fallo latente](../f/fallo-latente.md), [FIT](../f/fit.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-447 — Automoción: ISO 26262 y niveles ASIL](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← QA / Test Automation Engineer](./qa-test-automation-engineer.md) · [Quality gate →](./quality-gate.md)
