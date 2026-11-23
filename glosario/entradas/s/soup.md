# SOUP

[↑ Glosario](../../README.md) · [← Sorpresa](./sorpresa.md) · [Span →](./span.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Software de origen desconocido, usado sin conocer sus procesos de desarrollo.

Definición de trabajo de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Por qué importa

En [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), el tema «SOUP» importa porque software de terceros sin desarrollo conocido.

## Cómo funciona

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

Una biblioteca, un sistema operativo o un controlador desarrollados por terceros sin los procesos de la norma se llaman SOUP. La norma no prohíbe usarlos; pide identificarlos, especificar qué se requiere de ellos, evaluar sus anomalías conocidas publicadas y verificar que funcionan en el contexto. La pregunta práctica es qué se hace cuando una biblioteca publica un defecto: debe haber un proceso que lo evalúe contra los peligros del dispositivo. Un proyecto con cientos de dependencias y sin lista de SOUP no puede responder si un aviso lo afecta.

Según [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

**Diagnóstico paso a paso.** (1) La biblioteca de comunicaciones corría en el mismo proceso que el control de dosis. (2) El argumento de segregación decía «módulos separados» pero no había aislamiento de proceso ni de memoria. (3) Un defecto de la biblioteca consumió la memoria compartida y la tarea de control fue reiniciada por el vigilante. (4) La biblioteca figuraba como SOUP sin análisis de anomalías conocidas.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Una biblioteca, un sistema operativo o un controlador desarrollados por terceros sin los procesos de la norma se llaman SOUP. ([SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-159](../../../classes/part-13-especificaciones-contratos-y-modelos/se-159-contratos-invariantes-y-diseno-por-contrato/README.md), [SE-295](../../../classes/part-24-software-especializado-y-dominios/se-295-salud-datos-sensibles-y-sistemas-regulados/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Origen](../o/origen.md), [Proceso](../p/proceso.md), [Análisis de impacto](../a/analisis-de-impacto.md), [Archivo de gestión de riesgos](../a/archivo-de-gestion-de-riesgos.md), [Clase de seguridad del software](../c/clase-de-seguridad-del-software.md), [Medida de control de riesgo](../m/medida-de-control-de-riesgo.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-449 — Dispositivos médicos: IEC 62304](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Sorpresa](./sorpresa.md) · [Span →](./span.md)
