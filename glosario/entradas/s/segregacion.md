# Segregación

[↑ Glosario](../../README.md) · [← Segmento inicial](./segmento-inicial.md) · [Seguimiento de cambios →](./seguimiento-de-cambios.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Separación argumentada y verificada entre elementos que permite asignar clases distintas.

Definición de trabajo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Por qué importa

En [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), el tema «Segregación» importa porque acota el esfuerzo si es verificable.

## Cómo funciona

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

Un módulo de clase A que comparte proceso, memoria o dependencias con uno de clase C puede alterar su comportamiento: un puntero perdido, un uso de CPU, una excepción. Si no se demuestra lo contrario, hereda la clase. En el laboratorio, con las dependencias de doce módulos, sin segregación la clase C se propaga de control de dosis a validador, bomba, calibración, y por dependencia a registro y almacén: seis módulos en C y dos en A; el esfuerzo (actividades de verificación con pesos del autor) es 90. Con una segregación documentada —un proceso separado para el control con una interfaz mínima— quedan 4, 4 y 4, y el esfuerzo es 76.

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

**Diagnóstico paso a paso.** (1) La biblioteca de comunicaciones corría en el mismo proceso que el control de dosis. (2) El argumento de segregación decía «módulos separados» pero no había aislamiento de proceso ni de memoria. (3) Un defecto de la biblioteca consumió la memoria compartida y la tarea de control fue reiniciada por el vigilante. (4) La biblioteca figuraba como SOUP sin análisis de anomalías conocidas.

## Ejemplo

Ejemplo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) (sección «Ejemplo mínimo»):

Sin segregación, todo lo que usa un módulo de clase C pasa a clase C. El laboratorio aplica exactamente esta regla a doce módulos.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- En el laboratorio, con las dependencias de doce módulos, sin segregación la clase C se propaga de control de dosis a validador, bomba, calibración, y por dependencia a registro y almacén: seis módulos en C y dos en A; el esfuerzo (actividades de verificación con pesos del autor) es 90. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))
- Clasifica provisionalmente cada módulo, propaga la clase por las dependencias y marca los que podrían bajar con una segregación. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Análisis de impacto](../a/analisis-de-impacto.md), [Archivo de gestión de riesgos](../a/archivo-de-gestion-de-riesgos.md), [Clase de seguridad del software](../c/clase-de-seguridad-del-software.md), [Medida de control de riesgo](../m/medida-de-control-de-riesgo.md), [Situación peligrosa](./situacion-peligrosa.md), [SOUP](./soup.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Segmento inicial](./segmento-inicial.md) · [Seguimiento de cambios →](./seguimiento-de-cambios.md)
