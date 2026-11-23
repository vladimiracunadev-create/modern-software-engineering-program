# Tiempo de llegada

[↑ Glosario](../../README.md) · [← Tiempo de ciclo o plazo](./tiempo-de-ciclo-o-plazo.md) · [Tiempo de ocurrencia / de procesamiento →](./tiempo-de-ocurrencia-de-procesamiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Instante en que el sistema lo recibió.

Definición de trabajo de [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md).

## Por qué importa

La clase donde se define, [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md), existe con este propósito: la clase existe para que elijas cómo entra un dato a la plataforma sabiendo qué compra y qué cuesta cada opción, y no por la moda de «tiempo real».

## Cómo funciona

[SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md)) son: La mezcla de retrasos, el 3 % de tardíos y el 2 % de reentregas son construcciones del autor; la simulación procesa los eventos en orden de llegada con ventanas de una hora y no reproduce un motor de flujo con estado, activadores ni ventanas por sesión. No se midió ninguna fuente real ni ningún corredor de mensajes.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-361](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-361-del-dato-operacional-al-analitico/README.md), [SE-376](../../../classes/part-31-integracion-eventos-y-mensajeria/se-376-entrega-orden-duplicacion-y-semanticas/README.md), [SE-377](../../../classes/part-31-integracion-eventos-y-mensajeria/se-377-outbox-inbox-sagas-y-compensacion/README.md), [SE-436](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-436-latencia-throughput-saturacion-y-capacidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Instante](../i/instante.md), [Dato tardío](../d/dato-tardio.md), [Entrega al menos una vez](../e/entrega-al-menos-una-vez.md), [Idempotencia](../i/idempotencia.md), [Marca de agua](../m/marca-de-agua.md), [Tiempo del evento](./tiempo-del-evento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-362 — Ingesta batch y streaming](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-362-ingesta-batch-y-streaming/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-290](../../../classes/part-24-software-especializado-y-dominios/se-290-ingenieria-de-datos-y-procesamiento-analitico/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Tiempo de ciclo o plazo](./tiempo-de-ciclo-o-plazo.md) · [Tiempo de ocurrencia / de procesamiento →](./tiempo-de-ocurrencia-de-procesamiento.md)
