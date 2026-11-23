# Evidencia obsoleta

[↑ Glosario](../../README.md) · [← Evidencia negativa](./evidencia-negativa.md) · [Evidencia trazable →](./evidencia-trazable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md)

## Definición

Evidencia que ya no corresponde a la versión revisada de lo que verifica.

Definición de trabajo de [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md).

## Por qué importa

En [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md), el tema «Evidencia obsoleta» importa porque un cambio invalida pruebas sin hacer ruido.

## Cómo funciona

Según [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md):

El paquete se actualiza con cada cambio de requisitos, diseño, entorno o uso, y con cada incidente. La integración continua ejecuta el comprobador y falla si hay huecos nuevos o evidencia obsoleta sin una decisión registrada. Los disparadores de revisión están escritos (un cambio de proveedor del sensor, una actualización de una biblioteca, un incidente). Un paquete que se hizo una vez para una auditoría es el equivalente del archivo de riesgos que nunca se actualizó (`SE-449`).

Según [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md):

Las ideas de trazar peligros a pruebas y detectar evidencia obsoleta sirven en cualquier sistema; el rigor, la independencia de la revisión y el costo se ajustan al riesgo. En un blog personal, un manifiesto sería excesivo; en un sistema que maneja dinero o salud, no.

## Ejemplo

Ejemplo de [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) (sección «Preguntas frecuentes»):

Las ideas de trazar peligros a pruebas y detectar evidencia obsoleta sirven en cualquier sistema; el rigor, la independencia de la revisión y el costo se ajustan al riesgo. En un blog personal, un manifiesto sería excesivo; en un sistema que maneja dinero o salud, no.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La integración continua ejecuta el comprobador y falla si hay huecos nuevos o evidencia obsoleta sin una decisión registrada. ([SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-168](../../../classes/part-13-especificaciones-contratos-y-modelos/se-168-proyecto-paquete-de-especificaciones-trazables/README.md), [SE-276](../../../classes/part-22-embedded-iot-y-tiempo-real/se-276-proyecto-dispositivo-simulado-operable-y-actualizable/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Evidencia](./evidencia.md), [Versión](../v/version.md), [Disparador de revisión](../d/disparador-de-revision.md), [Hueco de contenido](../h/hueco-de-contenido.md), [Manifiesto](../m/manifiesto.md), [Mantenimiento](../m/mantenimiento.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-455](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-455-taller-analizar-un-fallo-real-frente-a-las-normas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Evidencia negativa](./evidencia-negativa.md) · [Evidencia trazable →](./evidencia-trazable.md)
