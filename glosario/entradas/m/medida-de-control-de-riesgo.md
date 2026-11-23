# Medida de control de riesgo

[↑ Glosario](../../README.md) · [← Medida de contrapeso](./medida-de-contrapeso.md) · [Medida de la respuesta →](./medida-de-la-respuesta.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Acción o elemento que reduce el riesgo, dentro o fuera del software.

Definición de trabajo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Por qué importa

La clase donde se define, [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), existe con este propósito: la clase existe para que entiendas cómo se organiza el desarrollo de software de un dispositivo médico y por qué su decisión central, la **clase de seguridad del software**, es una afirmación sobre qué puede causar el software y qué lo limita desde fuera, y no sobre cuán complejo es.

## Cómo funciona

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

La clase se asigna a cada elemento de software según lo que su fallo podría causar: la clase A si no puede contribuir a una situación peligrosa; la B si puede contribuir y el daño posible no es grave; la C si puede contribuir y el daño posible es la muerte o una lesión grave. En la edición consolidada de 2015, esa evaluación puede tener en cuenta **medidas de control de riesgo externas al software** (un límite mecánico, una alarma independiente); si reducen el riesgo de forma verificada, la clase puede bajar. El detalle de los criterios es de la norma; la idea que se transfiere es que la clase es una conclusión de un análisis y no una elección del equipo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En la edición consolidada de 2015, esa evaluación puede tener en cuenta **medidas de control de riesgo externas al software** (un límite mecánico, una alarma independiente); si reducen el riesgo de forma verificada, la clase puede bajar. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Riesgo](../r/riesgo.md).
- **Ver también:** [Análisis de impacto](../a/analisis-de-impacto.md), [Archivo de gestión de riesgos](../a/archivo-de-gestion-de-riesgos.md), [Clase de seguridad del software](../c/clase-de-seguridad-del-software.md), [Segregación](../s/segregacion.md), [Situación peligrosa](../s/situacion-peligrosa.md), [SOUP](../s/soup.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Medida de contrapeso](./medida-de-contrapeso.md) · [Medida de la respuesta →](./medida-de-la-respuesta.md)
