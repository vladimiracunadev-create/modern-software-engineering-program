# Situación peligrosa

[↑ Glosario](../../README.md) · [← Site Reliability Engineer](./site-reliability-engineer.md) · [Sketches y aproximación →](./sketches-y-aproximacion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Circunstancia en la que personas, bienes o el ambiente se exponen a un peligro.

Definición de trabajo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Por qué importa

La clase donde se define, [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), existe con este propósito: la clase existe para que entiendas cómo se organiza el desarrollo de software de un dispositivo médico y por qué su decisión central, la **clase de seguridad del software**, es una afirmación sobre qué puede causar el software y qué lo limita desde fuera, y no sobre cuán complejo es.

## Cómo funciona

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

La clase se asigna a cada elemento de software según lo que su fallo podría causar: la clase A si no puede contribuir a una situación peligrosa; la B si puede contribuir y el daño posible no es grave; la C si puede contribuir y el daño posible es la muerte o una lesión grave. En la edición consolidada de 2015, esa evaluación puede tener en cuenta **medidas de control de riesgo externas al software** (un límite mecánico, una alarma independiente); si reducen el riesgo de forma verificada, la clase puede bajar. El detalle de los criterios es de la norma; la idea que se transfiere es que la clase es una conclusión de un análisis y no una elección del equipo.

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

Una startup desarrolla la aplicación móvil de un monitor de glucosa. El equipo asume que la aplicación es clase A porque «solo muestra los datos del sensor». Un revisor pregunta qué pasa si la aplicación muestra un valor equivocado y la persona usa esa lectura para decidir una dosis. La conclusión cambia: la aplicación puede contribuir a una situación peligrosa y la clase efectiva es mayor. El equipo evalúa dos caminos: segregar el módulo de cálculo y alarma y verificarlo con rigor (clase mayor, módulo pequeño), o rediseñar para que la lectura crítica la muestre siempre el dispositivo físico y la aplicación sea solo informativa (con un control externo verificado). Eligen el primero porque el segundo exige cambiar hardware.

## Ejemplo

Ejemplo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) (sección «Ejemplo profesional»):

Una startup desarrolla la aplicación móvil de un monitor de glucosa. El equipo asume que la aplicación es clase A porque «solo muestra los datos del sensor». Un revisor pregunta qué pasa si la aplicación muestra un valor equivocado y la persona usa esa lectura para decidir una dosis. La conclusión cambia: la aplicación puede contribuir a una situación peligrosa y la clase efectiva es mayor. El equipo evalúa dos caminos: segregar el módulo de cálculo y alarma y verificarlo con rigor (clase mayor, módulo pequeño), o rediseñar para que la lectura crítica la muestre siempre el dispositivo físico y la aplicación sea solo informativa (con un control externo verificado).

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La clase se asigna a cada elemento de software según lo que su fallo podría causar: la clase A si no puede contribuir a una situación peligrosa; la B si puede contribuir y el daño posible no es grave; la C si puede contribuir y el daño posible es la muerte o una lesión grave. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))
- No necesariamente: si su fallo (mostrar un valor erróneo) puede llevar a una decisión clínica peligrosa, puede contribuir a una situación peligrosa. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Peligro](../p/peligro.md).
- **Ver también:** [Análisis de impacto](../a/analisis-de-impacto.md), [Archivo de gestión de riesgos](../a/archivo-de-gestion-de-riesgos.md), [Clase de seguridad del software](../c/clase-de-seguridad-del-software.md), [Medida de control de riesgo](../m/medida-de-control-de-riesgo.md), [Segregación](./segregacion.md), [SOUP](./soup.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Site Reliability Engineer](./site-reliability-engineer.md) · [Sketches y aproximación →](./sketches-y-aproximacion.md)
