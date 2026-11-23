# Integridad referencial

[↑ Glosario](../../README.md) · [← Integrador](./integrador.md) · [Integridad y dependency confusion →](./integridad-y-dependency-confusion.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Cada clave extranjera apunta a una fila existente.

Definición de trabajo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

## Por qué importa

En [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), el tema «Integridad referencial» importa porque detecta claves huérfanas tras una unión.

## Cómo funciona

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

Volumen: ¿llegaron las filas esperadas? Unicidad: ¿hay claves repetidas? Nulos: ¿falta lo que debería estar? Integridad referencial: ¿cada clave extranjera apunta a algo? Frescura: ¿es reciente el dato más nuevo? Distribución: ¿se parecen los valores a lo habitual? En el laboratorio, una tabla de 5 000 pedidos recibió seis variantes defectuosas. La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. La variante limpia no falló ninguna. Ninguna comprobación vio más de dos variantes: su ceguera es tan importante como su vista.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La carga parcial falló el volumen; los duplicados fallaron volumen y unicidad; los nulos en el cliente, la comprobación de nulos; los clientes huérfanos, la integridad referencial; los datos atrasados, la frescura; los importes multiplicados por cien (un cambio de unidad) solo fallaron la distribución. ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Comprobación de calidad](../c/comprobacion-de-calidad.md), [Deriva de distribución](../d/deriva-de-distribucion.md), [Frescura](../f/frescura.md), [MAD](../m/mad.md), [Observabilidad de datos](../o/observabilidad-de-datos.md), [Volumen](../v/volumen.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← Integrador](./integrador.md) · [Integridad y dependency confusion →](./integridad-y-dependency-confusion.md)
