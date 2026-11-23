# Costo de demora

[↑ Glosario](../../README.md) · [← Costo de construir](./costo-de-construir.md) · [Costo de operar y mantener →](./costo-de-operar-y-mantener.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Pérdida por unidad de tiempo que se retrasa la entrega de una iniciativa.

Definición de trabajo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

## Por qué importa

En [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), el tema «Costo de demora y orden» importa porque el orden de ejecución cambia el costo de esperar.

## Cómo funciona

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

El **costo de demora** de una iniciativa es lo que se pierde por cada unidad de tiempo que tarda en entregarse (ingresos que no llegan, multas que se pagan, riesgo que se mantiene). Con una sola capacidad de ejecución, el orden importa: el costo total de esperar es la suma, para cada iniciativa, de su costo de demora por el tiempo hasta terminarla. Smith demostró en 1956 que se minimiza ejecutando primero las de mayor razón entre costo de demora y duración. Es la lógica de la priorización por **costo de demora dividido por tamaño** que usan marcos como WSJF y que Reinertsen hizo central en el desarrollo de producto.

Según [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo estima el costo de demora de sus doce iniciativas con quienes las piden: la que evita una multa semanal vale 40 por semana y dura dos semanas; otra, un rediseño de portal, vale 6 por semana y dura ocho. La razón entre costo y duración (20 y 0,75) coloca la primera al inicio, aunque la dirección había pedido el rediseño primero. Calcula el costo de la espera del orden por llegada frente al propuesto y lo presenta como rango, porque las estimaciones son inciertas.

## Ejemplo

Ejemplo de [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) (sección «Ejemplo profesional»):

Escenario hipotético, construido para la clase y sin datos reales. El equipo estima el costo de demora de sus doce iniciativas con quienes las piden: la que evita una multa semanal vale 40 por semana y dura dos semanas; otra, un rediseño de portal, vale 6 por semana y dura ocho. La razón entre costo y duración (20 y 0,75) coloca la primera al inicio, aunque la dirección había pedido el rediseño primero. Calcula el costo de la espera del orden por llegada frente al propuesto y lo presenta como rango, porque las estimaciones son inciertas.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se ejecutan primero las iniciativas más antiguas** — causa: orden por llegada. Corrección: ordenar por costo de demora entre duración. ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El **costo de demora** de una iniciativa es lo que se pierde por cada unidad de tiempo que tarda en entregarse (ingresos que no llegan, multas que se pagan, riesgo que se mantiene). ([SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-536](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-536-propiedad-intelectual-contratos-y-etica/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [CAPEX y OPEX](./capex-y-opex.md), [Punto de equilibrio](../p/punto-de-equilibrio.md), [Tasa interna de retorno](../t/tasa-interna-de-retorno.md), [Valor presente neto](../v/valor-presente-neto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-537 — Economía del software y costo total](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

**También se usa en** (1 clases más lo mencionan; las que más):

[SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Reinertsen, *The Principles of Product Development Flow*](https://openlibrary.org/isbn/9781935401001) — costo de demora como base económica; autoridad: libro de referencia.
- [SAFe, WSJF](https://scaledagileframework.com/wsjf/) — priorización por costo de demora entre tamaño; autoridad: Scaled Agile.
- [Smith, «Various optimizers for single-stage production»](https://doi.org/10.1002/nav.3800030106) — orden óptimo por razón entre peso y duración; autoridad: Naval Research Logistics Quarterly.
- [Brealey, Myers y Allen, *Principles of Corporate Finance*](https://openlibrary.org/isbn/9781260013900) — valor presente neto y retorno; autoridad: libro de texto de referencia.
- [FinOps Framework](https://www.finops.org/framework/) — gestión del costo de la nube; autoridad: FinOps Foundation.

---

[↑ Glosario](../../README.md) · [← Costo de construir](./costo-de-construir.md) · [Costo de operar y mantener →](./costo-de-operar-y-mantener.md)
