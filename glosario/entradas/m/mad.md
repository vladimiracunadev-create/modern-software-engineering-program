# MAD

[↑ Glosario](../../README.md) · [← M/M/1](./m-m-1.md) · [Maestro dorado →](./maestro-dorado.md)

> **Tipo:** sigla · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** E — Diseño, arquitectura, datos e integración · **Primera aparición:** [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md)

## Definición

Desviación absoluta mediana, medida de dispersión robusta.

Definición de trabajo de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md).

## Por qué importa

La clase donde se define, [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md), existe con este propósito: la clase existe para que sepas cuándo un dato es incorrecto antes de que lo descubra quien toma una decisión con él.

## Cómo funciona

Según [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

El umbral fijo (menos de 8 000 o más de 12 000 filas) vio los cuatro incidentes y dio 32 falsas alarmas: cada fin de semana dispara. El z-score sobre los 14 días anteriores no dio falsas alarmas y vio solo dos de los cuatro incidentes: la caída semanal le enseñó una desviación grande y absorbió la carga parcial del lunes y la del sábado. La mediana del mismo día de la semana en las cuatro semanas anteriores, con una tolerancia de seis veces la desviación absoluta mediana (MAD) o el 15 % de la mediana, vio los cuatro y no dio falsas alarmas.

## Ejemplo

La clase no ilustra este término por separado; el ejemplo de su tema está en la sección «Ejemplo profesional» de [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md):

*Escenario ilustrativo: las cifras y los resultados que aparecen en este ejemplo son supuestos de la narración, no mediciones.*

## Errores y confusiones comunes

Las clases no registran errores específicos de este término.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La mediana del mismo día de la semana en las cuatro semanas anteriores, con una tolerancia de seis veces la desviación absoluta mediana (MAD) o el 15 % de la mediana, vio los cuatro y no dio falsas alarmas. ([SE-365](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-364](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-364-transformacion-y-orquestacion-idempotente-con-backfills/README.md), [SE-497](../../../classes/part-41-observabilidad-sre-e-incidentes/se-497-sli-slo-sla-y-presupuestos-de-error/README.md), [SE-498](../../../classes/part-41-observabilidad-sre-e-incidentes/se-498-alertas-accionables-y-fatiga/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Desviación](../d/desviacion.md), [Dispersión](../d/dispersion.md), [Medida](./medida.md), [Comprobación de calidad](../c/comprobacion-de-calidad.md), [Deriva de distribución](../d/deriva-de-distribucion.md), [Frescura](../f/frescura.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-365 — Calidad y observabilidad de datos](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/se-365-calidad-y-observabilidad-de-datos/README.md) — [Parte 30](../../../classes/part-30-ingenieria-de-datos-y-plataformas-de-datos/README.md), Ingeniería de datos y plataformas de datos.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Las fuentes de este concepto están en las clases enlazadas (sección «Fuentes» de cada clase).

---

[↑ Glosario](../../README.md) · [← M/M/1](./m-m-1.md) · [Maestro dorado →](./maestro-dorado.md)
