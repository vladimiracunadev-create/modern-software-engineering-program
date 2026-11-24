# Costo de construir

[↑ Glosario](../../README.md) · [← Costo cuadrático del bucle](./costo-cuadratico-del-bucle.md) · [Costo de demora →](./costo-de-demora.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

El **costo de construir** es el gasto necesario para dejar el producto en uso: diseño, desarrollo, pruebas, migración inicial y documentación mínima. Es el sentido de [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), donde se distingue de dos costos hermanos: el de operar (mantener, alojar, dar soporte) y el de oportunidad (lo que se deja de hacer por hacer esto). Es el costo visible, el que se aprueba en un presupuesto.

## Por qué importa

Cambia qué se aprueba. Según [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md), el costo de construir pesa menos de lo que se cree en el costo de propiedad: un presupuesto que cubre la construcción y no la operación alcanza para llegar y no para seguir. Por eso la clase propone aprobar un costo de propiedad a cinco años con intervalo, no una cifra de construcción aislada.

## Cómo funciona

Se estima por trabajo y por insumos, y casi siempre se subestima porque se estima lo conocido. Dos reglas lo corrigen. Primero, su rango debe incluir lo que el equipo todavía no sabe (integraciones, requisitos que cambian), de modo que se expresa con mínimo, moda y máximo y no con un número único. Segundo, se declara quién estimó y cuándo, para poder comparar con el costo real y mejorar el siguiente rango.

Combinar estimaciones exige cuidado. Si un plan de «100 días» se retrasa casi siempre, la causa que da [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) es que se sumaron medianas: la suma de medianas no es la mediana de la suma cuando las partes son asimétricas y están correlacionadas. La corrección es prometer el percentil 80 del plan y declarar la correlación que se supuso.

## Ejemplo

En la plataforma de entregas, `cost-model.md` contiene una fila por rubro (construcción, mantenimiento, infraestructura, soporte, otro) con mínimo, moda, máximo, quién estimó, fecha y fuente de comparación. El total se calcula siempre desde las filas y ningún total se informa sin su percentil 80. Cuando existan costos reales, cada fila se compara con su estimación.

## Errores y confusiones comunes

- **El presupuesto alcanza para construir y no para seguir.** Se aprobó solo la construcción; aprobar el costo de propiedad a cinco años con intervalo.
- **Sumar medianas.** El plan se retrasa casi siempre; prometer el percentil 80.
- **Un número sin rango.** Oculta la incertidumbre y se lee como compromiso.
- **Estimar solo lo conocido.** Las integraciones y requisitos cambiantes son justo lo que no se ve.

## Límites y cuándo no aplica

Las cifras de [SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) provienen de experimentos con datos sintéticos: no se midió el costo de ninguna plataforma real, y la distribución lognormal y la correlación única son supuestos de la clase. Sirve para comparar y decidir bajo incertidumbre, no para predecir un costo concreto. Y no basta por sí solo: sin los costos de operación y de oportunidad, decide con una parte del cuadro.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Migración](../m/migracion.md), [Producto](../p/producto.md), [Costo de operar y mantener](./costo-de-operar-y-mantener.md), [Costo de oportunidad](./costo-de-oportunidad.md), [Estimación con incertidumbre](../e/estimacion-con-incertidumbre.md), [Valor presente neto](../v/valor-presente-neto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (6 clases más lo mencionan; las que más):

[SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-568](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-568-greenfield-brownfield-bug-fixing-e-idea-assessment/README.md), [SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md), [SE-144](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-144-proyecto-caso-de-viabilidad-tecnico-economica/README.md), [SE-302](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-302-solid-y-sus-limites/README.md), [SE-310](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-310-deuda-tecnica-interes-y-opciones/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones, descuento y corrección del sesgo de optimismo; autoridad: HM Treasury (Reino Unido).
- [AWS Well-Architected: Cost Optimization Pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) — el costo incluye la operación continua y se gestiona con prácticas de medición; autoridad: Amazon Web Services (documentación de un proveedor).
- [FinOps Foundation: What is FinOps](https://www.finops.org/introduction/what-is-finops/) — práctica de gestión del gasto en la nube con responsabilidad compartida; autoridad: FinOps Foundation (Linux Foundation).
- [GOV.UK Service Manual: Measuring cost per transaction](https://www.gov.uk/service-manual/measuring-success/measuring-cost-per-transaction) — cómo calcular el costo por transacción incluyendo costos de operación; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Costo cuadrático del bucle](./costo-cuadratico-del-bucle.md) · [Costo de demora →](./costo-de-demora.md)
