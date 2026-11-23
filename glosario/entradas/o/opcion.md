# Opción

[↑ Glosario](../../README.md) · [← Omisión coordinada](./omision-coordinada.md) · [Opción de refactorizar →](./opcion-de-refactorizar.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md)

## Definición

Derecho, no obligación, de continuar una inversión tras observar información de una etapa previa.

Definición de trabajo de [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md).

## Por qué importa

En [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md), el tema «Opciones y etapas» importa porque una etapa barata compra información y permite no gastar el resto si el resultado es malo.

## Cómo funciona

Según [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md):

Invertir por etapas es comprar una opción: se paga un piloto y se decide continuar o detenerse según su resultado. La opción tiene valor cuando el piloto es suficientemente informativo y cuando detenerse evita pérdidas mayores que el costo del piloto. Un piloto no informativo (exactitud de azar) solo agrega costo. Para un valor esperado negativo, el piloto puede hacer positiva la inversión si distingue bien.

## Ejemplo

Contexto concreto en el que aparece el término, de la sección «Ejemplo profesional» de [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md):

En la plataforma, `portfolio-log.md` registra cada iniciativa con costo, rango de retorno, dependencias y responsable, la cartera elegida con las alternativas descartadas, la medida de robustez (veces que es la mejor, arrepentimiento) y la regla de revisión. El contrato es que ninguna cartera se aprueba sin sus alternativas y sin la fecha en que se revisará. Esa estructura permite que otra persona vea qué se descartó y por qué.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md)) son:

- **El comité cree que la cartera «ganará»** — causa: se informó solo el valor esperado. Corrección: informar arrepentimiento y retorno neto p5.
- **Se compromete todo el presupuesto en una iniciativa** — causa: no se evaluó un piloto. Corrección: calcular el valor por etapas y la exactitud mínima.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Por debajo, el piloto gasta 20 y la opción de detenerse no compensa; por encima, el piloto vale. ([SE-141](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-140](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-140-finops-de-producto-y-costo-por-resultado/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Derecho](../d/derecho.md), [Arrepentimiento](../a/arrepentimiento.md), [Dependencia](../d/dependencia.md), [Portafolio](../p/portafolio.md), [Secuencia](../s/secuencia.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-141 — Portafolio, opciones y secuenciación de inversión](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/se-141-portafolio-opciones-y-secuenciacion-de-inversion/README.md) — [Parte 11](../../../classes/part-11-economia-metricas-y-decisiones-de-producto/README.md), Economía, métricas y decisiones de producto.

**También se usa en** (160 clases más lo mencionan; las que más):

[SE-309](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-309-complejidad-accidental-y-esencial/README.md), [SE-132](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-132-proyecto-product-brief-respaldado-por-evidencia/README.md), [SE-207](../../../classes/part-17-documentacion-y-conocimiento-tecnico/se-207-readme-instalacion-y-primer-exito/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-008](../../../classes/part-00-ingenieria-de-software-como-profesion/se-008-restricciones-riesgos-y-compromisos-entre-atributos/README.md), [SE-217](../../../classes/part-18-cli-tui-servicios-y-automatizacion/se-217-diseno-de-interfaces-de-linea-de-comandos/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-303](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-303-composicion-herencia-y-delegacion/README.md).

**Aparece en los casos de estudio:** [Netflix](../../../casos/exito/netflix.md), [WhatsApp](../../../casos/exito/whatsapp.md), [Airbnb](../../../casos/exito/airbnb.md), [TSB Bank](../../../casos/fallo/tsb.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [HM Treasury: The Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-governent/the-green-book-2020) — evaluación de opciones y sensibilidad; autoridad: HM Treasury (Reino Unido).
- [GOV.UK Service Manual: How the alpha phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-alpha-phase-works) — prototipos para probar incertidumbres antes de construir y decisión de continuar; autoridad: Government Digital Service (Reino Unido).
- [GOV.UK Service Manual: How the beta phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-beta-phase-works) — construcción por etapas con evidencia de cada una; autoridad: Government Digital Service.
- [GOV.UK Service Manual: How the discovery phase works](https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works) — fase inicial que decide si avanzar; autoridad: Government Digital Service.
- [SWEBOK Guide v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) — economía de la ingeniería de software; autoridad: IEEE Computer Society.

---

[↑ Glosario](../../README.md) · [← Omisión coordinada](./omision-coordinada.md) · [Opción de refactorizar →](./opcion-de-refactorizar.md)
