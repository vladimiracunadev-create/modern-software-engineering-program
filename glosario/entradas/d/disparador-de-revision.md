# Disparador de revisión

[↑ Glosario](../../README.md) · [← Disparador](./disparador.md) · [Dispersión →](./dispersion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Condición medible (métrica, umbral y duración) que reabre la decisión.

Definición de trabajo de [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md): Condición (un cambio, un incidente) que obliga a revisar el paquete.

## Por qué importa

En [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md), el tema «Disparador de revisión» importa porque hace que la decisión caduque.

## Cómo funciona

Según [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md):

Se definieron once criterios que un analizador puede comprobar: siete secciones presentes (contexto, decisión, alternativas consideradas, consecuencias, reversibilidad, disparador de revisión y evidencia) y cuatro propiedades de contenido (al menos dos alternativas, cada una con su motivo de descarte; al menos una consecuencia negativa declarada; algún criterio medible, es decir, un número con su unidad; y un disparador de revisión con un número). Se aplicaron a tres registros de ejemplo. El ADR-A (monolito modular con extracción del módulo de avisos si el p99 supera 200 ms) cumplió 11 de 11. El ADR-B («Usar microservicios… porque son la mejor práctica») cumplió 3 de 11: tiene contexto, decisión y consecuencias, pero ninguna alternativa, ninguna consecuencia negativa, ningún número, reversibilidad, disparador ni evidencia.

Según [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md):

El paquete se actualiza con cada cambio de requisitos, diseño, entorno o uso, y con cada incidente. La integración continua ejecuta el comprobador y falla si hay huecos nuevos o evidencia obsoleta sin una decisión registrada. Los disparadores de revisión están escritos (un cambio de proveedor del sensor, una actualización de una biblioteca, un incidente). Un paquete que se hizo una vez para una auditoría es el equivalente del archivo de riesgos que nunca se actualizó (`SE-449`).

## Ejemplo

Ejemplo de [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) (sección «Preguntas frecuentes»):

Con cada cambio de requisitos, diseño, entorno o uso, con cada incidente y cuando vence un disparador de revisión. La integración continua comprueba huecos y obsolescencia en cada cambio.

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Con cada cambio de requisitos, diseño, entorno o uso, con cada incidente y cuando vence un disparador de revisión. ([SE-456](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-332](../../../classes/part-27-arquitectura-de-software-y-dominio/se-332-fitness-functions-y-arquitectura-evolutiva/README.md), [SE-333](../../../classes/part-27-arquitectura-de-software-y-dominio/se-333-trade-offs-adr-y-evaluacion-de-alternativas/README.md), [SE-337](../../../classes/part-28-estilos-arquitectonicos/se-337-estilos-como-respuestas-a-fuerzas-de-calidad/README.md), [SE-347](../../../classes/part-28-estilos-arquitectonicos/se-347-taller-seleccionar-un-estilo-con-escenarios-de-calidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Condición](../c/condicion.md), [Incidente](../i/incidente.md), [Métrica](../m/metrica.md), [Paquete](../p/paquete.md), [ADR](../a/adr.md), [Consecuencia negativa](../c/consecuencia-negativa.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-348 — Proyecto: decisión arquitectónica defendida con ADR](../../../classes/part-28-estilos-arquitectonicos/se-348-proyecto-decision-arquitectonica-defendida-con-adr/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.
- [SE-456 — Proyecto: paquete de aseguramiento de un controlador](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-456-proyecto-paquete-de-aseguramiento-de-un-controlador/README.md) — [Parte 37](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/README.md), Sistemas críticos, tiempo real y normas de seguridad.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-187](../../../classes/part-15-procesos-planificacion-y-estimacion/se-187-riesgos-supuestos-issues-y-decisiones/README.md), [SE-450](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-450-casos-de-seguridad-y-trazabilidad/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-012](../../../classes/part-00-ingenieria-de-software-como-profesion/se-012-proyecto-mapa-profesional-y-contrato-personal-de-aprendizaje/README.md), [SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Disparador](./disparador.md) · [Dispersión →](./dispersion.md)
