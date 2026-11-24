# Costo de oportunidad

[↑ Glosario](../../README.md) · [← Costo de operar y mantener](./costo-de-operar-y-mantener.md) · [Costo de reversión →](./costo-de-reversion.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

El **costo de oportunidad** es el valor de la mejor alternativa a la que se renuncia al elegir una opción ([SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md)). No aparece en ninguna factura: no es un gasto sino lo que se deja de ganar. Cada opción elegida es una opción no elegida, y su costo es lo mejor de lo descartado.

## Por qué importa

Hace visible lo que una evaluación de costos suele ocultar. Un proyecto con valor presente positivo puede ser una mala decisión si la alternativa vale más: las personas que construyen la primera versión no construyen otra cosa, y el capital invertido no rinde en otro uso. Cambia el criterio de aprobación: no basta que el proyecto gane dinero; debe ganar más que lo que se deja de hacer.

## Cómo funciona

[SE-134](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) sitúa el concepto junto al costo de construir. Para usarlo se **nombra la alternativa descartada** y se la **estima**, aunque sea con un rango. El método es comparar: se calcula el valor de la mejor alternativa realista (otro proyecto, otra inversión, o simplemente mantener la capacidad libre) y se compara con el de la opción elegida. La diferencia es el valor neto frente a la alternativa.

Hay una regla de higiene importante: el costo de oportunidad solo importa para recursos **escasos**. Si el equipo tiene capacidad ociosa, hacer algo no cuesta oportunidad; si cada persona está asignada a algo de valor, cada decisión de asignar a alguien a un proyecto deja sin hacer otro. Por eso un portafolio de proyectos se evalúa como conjunto: el criterio relevante es qué hacer con una capacidad limitada.

El costo de oportunidad se conecta con el costo de construir (el costo visible) y con el costo de propiedad (el de seguir): los tres son partes de una decisión completa. También con el coste del retraso: un trabajo que espera deja de generar valor y esa pérdida es un costo de oportunidad por unidad de tiempo.

## Ejemplo

Un equipo de cuatro personas puede construir (A) un panel de seguimiento con valor presente estimado de 80 en un rango de 40 a 120, o (B) la recuperación de borradores con valor de 100 en un rango de 60 a 140. Elegir A no cuesta solo su inversión: cuesta también 100 de lo que B habría aportado. Si A vale 80 y B 100, A tiene valor presente positivo pero un costo de oportunidad mayor que su beneficio. (Cifras ilustrativas de unidades de valor.)

## Errores y confusiones comunes

- **Aprobar por valor presente positivo sin mirar alternativas.**
- **Presupuesto que alcanza para construir y no para seguir**: se aprobó solo la construcción; corrección: aprobar un costo de propiedad a cinco años con intervalo.
- **Contar el costo de oportunidad con capacidad ociosa.**
- **Confundirlo con costo hundido**: el hundido ya se gastó; la oportunidad es lo que se deja de ganar.

## Límites y cuándo no aplica

Estimar la mejor alternativa es difícil y tiene incertidumbre; se hace con rangos. Con una sola opción realista, el concepto aporta poco. No sustituye el análisis de riesgo: una alternativa más valiosa pero más arriesgada puede no ser mejor.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Opción](../o/opcion.md), [Valor](../v/valor.md), [Costo de construir](./costo-de-construir.md), [Costo de operar y mantener](./costo-de-operar-y-mantener.md), [Estimación con incertidumbre](../e/estimacion-con-incertidumbre.md), [Valor presente neto](../v/valor-presente-neto.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-134 — Costos de construcción, operación y oportunidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-134-costos-de-construccion-operacion-y-oportunidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (3 clases más lo mencionan; las que más):

[SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-537](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-537-economia-del-software-y-costo-total/README.md).

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

[↑ Glosario](../../README.md) · [← Costo de operar y mantener](./costo-de-operar-y-mantener.md) · [Costo de reversión →](./costo-de-reversion.md)
