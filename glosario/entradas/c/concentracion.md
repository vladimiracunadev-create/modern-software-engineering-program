# Concentración

[↑ Glosario](../../README.md) · [← Cómputo de entrenamiento](./computo-de-entrenamiento.md) · [Concentración de conocimiento →](./concentracion-de-conocimiento.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Parte del ingreso que aportan los mayores clientes; el índice de Herfindahl-Hirschman es la suma de los cuadrados de las participaciones.

Definición de trabajo de [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md).

## Por qué importa

En [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md), el tema «Concentración y dependencia» importa porque pocos clientes grandes convierten una salida en una crisis; el promedio no lo muestra.

## Cómo funciona

Según [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md):

**Cómo leer la figura.** Las barras verdes son centros parecidos; las coral, centros muy desiguales. **Dónde deja de valer:** la lognormal es una forma común de describir tamaños desiguales, no la distribución de tus clientes. La concentración mide dependencia, no riesgo: un cliente grande con contrato de cinco años puede ser menos riesgoso que cinco medianos que renuevan cada mes.

## Ejemplo

Ejemplo de [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) (sección «Caso conductor»):

La plataforma de entregas de tareas es el caso conductor de la [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md). Esta clase deja el primer artefacto: un modelo con supuestos y rangos, una razón con adquisición expresada como intervalo y una medida de concentración. `SE-134` descompondrá los costos que aquí entraron como un solo número; `SE-135` y `SE-136` definirán qué se mide para saber si los supuestos de uso y abandono se cumplen. Cambia después un solo supuesto —por ejemplo, el abandono— y revisa qué conclusiones del registro cambian.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Un cliente se va y el equipo descubre que era 13 % del ingreso** — causa: nadie midió la concentración. Corrección: informar participación de los mayores clientes y revisarla cada trimestre. ([SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La concentración mide dependencia, no riesgo: un cliente grande con contrato de cinco años puede ser menos riesgoso que cinco medianos que renuevan cada mes. ([SE-133](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Índice](../i/indice.md), [Margen de contribución](../m/margen-de-contribucion.md), [Modelo de ingreso](../m/modelo-de-ingreso.md), [Pagador, usuario y decisor](../p/pagador-usuario-y-decisor.md), [Valor de vida y costo de adquisición](../v/valor-de-vida-y-costo-de-adquisicion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-133 — Modelos de negocio y sostenibilidad](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-133-modelos-de-negocio-y-sostenibilidad/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (13 clases más lo mencionan; las que más):

[SE-200](../../../classes/part-16-git-colaboracion-y-codigo-abierto/se-200-contribucion-gobernanza-y-comunidades-abiertas/README.md), [SE-481](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-481-integracion-continua-y-feedback-temprano/README.md), [SE-215](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-215-taller-reconstruir-conocimiento-perdido/README.md), [SE-331](../../../classes/part-27-arquitectura-de-software-y-dominio/se-331-arquitecturas-serverless-edge-y-peer-to-peer/README.md), [SE-005](../../../classes/part-00-ingenieria-de-software-como-profesion/se-005-roles-especialidades-y-colaboracion-interdisciplinaria/README.md), [SE-268](../../../classes/part-22-embedded-iot-y-tiempo-real/se-268-sistemas-de-tiempo-real-y-deadlines/README.md), [SE-273](../../../classes/part-22-embedded-iot-y-tiempo-real/se-273-edge-gateways-y-procesamiento-local/README.md), [SE-299](../../../classes/part-24-software-especializado-y-dominios/se-299-taller-comparar-riesgos-entre-dominios/README.md).

**Aparece en los casos de estudio:** [WhatsApp](../../../casos/exito/whatsapp.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Open Source Guides: Getting paid for open source work](https://opensource.guide/getting-paid/) — decisiones de financiación y sostenimiento de un proyecto; autoridad: GitHub, con contribuciones de la comunidad.
- [Strategyzer: The Business Model Canvas](https://www.strategyzer.com/library/the-business-model-canvas) — descripción de un modelo de negocio por bloques; autoridad: Strategyzer (Osterwalder y Pigneur).
- [Why Business Models Matter (Harvard Business Review, 2002)](https://hbr.org/2002/05/why-business-models-matter) — qué es un modelo de negocio y por qué debe poder contrastarse; autoridad: Harvard Business Review (artículo parcialmente de pago).
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software y medición; autoridad: IEEE Computer Society.
- [GOV.UK Service Manual: Measuring success](https://www.gov.uk/service-manual/measuring-success) — cómo medir si un servicio cumple su propósito; autoridad: Government Digital Service (Reino Unido).

---

[↑ Glosario](../../README.md) · [← Cómputo de entrenamiento](./computo-de-entrenamiento.md) · [Concentración de conocimiento →](./concentracion-de-conocimiento.md)
