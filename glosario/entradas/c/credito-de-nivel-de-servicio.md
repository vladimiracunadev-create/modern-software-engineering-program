# Crédito de nivel de servicio

[↑ Glosario](../../README.md) · [← Credencial efímera](./credencial-efimera.md) · [Crédito de servicio →](./credito-de-servicio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** G — Operación, evolución y liderazgo · **Primera aparición:** [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md)

## Definición

Devolución parcial de la cuota que establece un contrato cuando el servicio incumple su objetivo.

Definición de trabajo de [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md).

## Por qué importa

La clase donde se define, [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md), existe con este propósito: la clase existe para que decidas si construir, comprar o adoptar un componente con un proceso que se pueda auditar, y para que evalúes a un proveedor con evidencia en vez de con una presentación comercial.

## Cómo funciona

Según [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md):

Un servicio que depende en serie de varios servicios no puede ser más disponible que el producto de sus disponibilidades. Cinco proveedores al 99,9 % dan una cadena del 99,5 %, cercana a cuarenta y cuatro horas de caída al año. La redundancia en el eslabón más débil (dos proveedores independientes) mejora esa cifra, y su costo debe pesarse. El **acuerdo de nivel de servicio** (SLA) define un compromiso y una compensación; el **objetivo** (SLO) y el **indicador** (SLI) los distingue la práctica de SRE. Un crédito de nivel de servicio es una devolución parcial de la cuota, no una compensación por la pérdida: sirve como señal contractual y no sustituye la tolerancia al fallo en el diseño.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md):

Escenario hipotético, construido para la clase y sin datos reales. El equipo define cuatro puertas (cifrado en reposo, almacenamiento en la región acordada, exportación completa con metadatos, evidencia de seguridad revisable); un proveedor queda fuera por la exportación. Con los cuatro restantes construye la matriz ponderada con pesos acordados con la dirección, hace una prueba de concepto con datos sintéticos que imitan las actas y puntúa a partir de ella.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md)) son:

- **El proveedor elegido incumple un requisito legal** — causa: requisito tratado como preferencia. Corrección: convertirlo en puerta con evidencia.
- **La elección cambia con otro grupo de pesos** — causa: diferencias pequeñas entre opciones. Corrección: prueba de sensibilidad y criterio de desempate.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un crédito de nivel de servicio es una devolución parcial de la cuota, no una compensación por la pérdida: sirve como señal contractual y no sustituye la tolerancia al fallo en el diseño. ([SE-535](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-534](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-534-gestion-de-riesgos-y-decisiones-ejecutivas/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Contrato](./contrato.md), [Cuota](./cuota.md), [Servicio](../s/servicio.md), [Disponibilidad compuesta](../d/disponibilidad-compuesta.md), [Evaluación ponderada](../e/evaluacion-ponderada.md), [Plan de salida](../p/plan-de-salida.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-535 — Compras, proveedores y evaluación técnica](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/se-535-compras-proveedores-y-evaluacion-tecnica/README.md) — [Parte 44](../../../classes/part-44-gestion-liderazgo-y-practica-profesional/README.md), Gestión, liderazgo y práctica profesional.

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/final) — gestión de riesgos de la cadena de suministro; autoridad: NIST.
- [OpenSSF Scorecard](https://scorecard.dev/) — comprobaciones de prácticas de seguridad de proyectos abiertos; autoridad: Open Source Security Foundation.
- [SLSA](https://slsa.dev/) — niveles de garantía de construcción y distribución; autoridad: proyecto SLSA.
- [Google SRE, «Service Level Objectives»](https://sre.google/sre-book/service-level-objectives/) — indicadores, objetivos y acuerdos; autoridad: equipo de SRE de Google.
- [Google SRE, «Embracing Risk»](https://sre.google/sre-book/embracing-risk/) — disponibilidad y costo; autoridad: equipo de SRE de Google.

---

[↑ Glosario](../../README.md) · [← Credencial efímera](./credencial-efimera.md) · [Crédito de servicio →](./credito-de-servicio.md)
