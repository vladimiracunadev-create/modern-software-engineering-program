# Archivo de gestión de riesgos

[↑ Glosario](../../README.md) · [← Archivo de bloqueo](./archivo-de-bloqueo.md) · [Archivo de instrucciones para agentes →](./archivo-de-instrucciones-para-agentes.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Conjunto de registros del análisis y control de riesgos del dispositivo.

Definición de trabajo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Por qué importa

La clase donde se define, [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), existe con este propósito: la clase existe para que entiendas cómo se organiza el desarrollo de software de un dispositivo médico y por qué su decisión central, la **clase de seguridad del software**, es una afirmación sobre qué puede causar el software y qué lo limita desde fuera, y no sobre cuán complejo es.

## Cómo funciona

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

El software cambia después de la entrega: correcciones, mejoras, parches de SOUP. Cada cambio necesita un análisis de impacto sobre los riesgos y las pruebas, y la configuración (qué versión de cada elemento está en cada unidad) debe ser reproducible. La relación con la gestión de riesgos es bidireccional: un peligro nuevo puede generar un requisito de software, y un cambio de software puede cambiar un riesgo. Un archivo de gestión de riesgos que se hizo al principio y nunca se actualizó es una pieza de museo.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md)) son: El dispositivo, los módulos, las clases y los pesos son ficticios y del autor; el modelo de error de entrada es de un solo tipo; las normas de pago no se reproducen y no se afirma conformidad regulatoria ni revisión por una autoridad. El siguiente paso, `SE-450`, organiza toda la evidencia de las clases anteriores como un caso de seguridad: un argumento estructurado con trazabilidad.

## Relación con otros conceptos

- **Prerrequisito:** [Riesgo](../r/riesgo.md).
- **Ver también:** [Análisis](./analisis.md), [Conjunto](../c/conjunto.md), [Control](../c/control.md), [Dispositivo](../d/dispositivo.md), [Análisis de impacto](./analisis-de-impacto.md), [Clase de seguridad del software](../c/clase-de-seguridad-del-software.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Archivo de bloqueo](./archivo-de-bloqueo.md) · [Archivo de instrucciones para agentes →](./archivo-de-instrucciones-para-agentes.md)
