# Silo y pool

[↑ Glosario](../../README.md) · [← SIL](./sil.md) · [Silo, puente, pool →](./silo-puente-pool.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md)

## Definición

Recursos dedicados a un inquilino frente a recursos compartidos entre varios.

Definición de trabajo de [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md).

## Por qué importa

La clase donde se define, [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md), existe con este propósito: la clase existe para que puedas decidir cómo se aísla a los clientes entre sí en un sistema que los atiende a todos, y para que sepas qué cuesta cada nivel de aislamiento.

## Cómo funciona

[SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: consulta la clase para el mecanismo completo.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md)) son: Las consultas, los datos y la simulación son construcciones del autor; SQLite no se comporta como un motor cliente-servidor, y el costo de operar un entorno por inquilino en producción incluye conexiones, memoria, respaldos y orquestación que no se midieron. No se evaluó ninguna plataforma multi-inquilino.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-341](../../../classes/part-28-estilos-arquitectonicos/se-341-bff-api-gateway-y-service-mesh/README.md), [SE-439](../../../classes/part-36-calidad-rendimiento-y-resiliencia/se-439-circuit-breakers-bulkheads-y-degradacion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Inquilino](../i/inquilino.md), [Recurso](../r/recurso.md), [Aislamiento de datos](../a/aislamiento-de-datos.md), [Barrera independiente](../b/barrera-independiente.md), [Barrera independiente de la consulta](../b/barrera-independiente-de-la-consulta.md), [Multi-tenancy](../m/multi-tenancy.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-342 — Multi-tenancy y aislamiento](../../../classes/part-28-estilos-arquitectonicos/se-342-multi-tenancy-y-aislamiento/README.md) — [Parte 28](../../../classes/part-28-estilos-arquitectonicos/README.md), Estilos arquitectónicos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← SIL](./sil.md) · [Silo, puente, pool →](./silo-puente-pool.md)
