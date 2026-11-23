# Prototipo

[↑ Glosario](../../README.md) · [← Protocolos de mensajes](./protocolos-de-mensajes.md) · [Prototipo desechable →](./prototipo-desechable.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Versión mínima de un producto que permite comprobar decisiones de diseño con personas y con pruebas.

Definición de trabajo de [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md).

## Por qué importa

En [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), el tema «Del requisito al prototipo» importa porque convierte las decisiones de la parte en algo que se puede abrir y comprobar.

## Cómo funciona

Según [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md):

El prototipo es un archivo HTML con estructura semántica (región principal, encabezado, etiquetas, botón nativo), estados (vacío, carga, éxito, error y recuperación), mensajes en texto, un esquema de colores con contraste calculado y una maquetación que no desborda a 320 px. Cada decisión referencia el hallazgo, la clase o el criterio que la motiva, y una prueba la comprueba. Un prototipo sin trazabilidad no se puede revisar.

Según [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md):

En la plataforma, el paquete del proyecto tiene el prototipo del formulario de entrega (un HTML con sus estados), `accessibility.md` con la tabla de criterios y su política de lo no probado, `usability-notes.md` con el plan de evaluación y sus resultados, y un registro de hallazgos y decisiones. La evaluación con personas usa cuotas por modalidad, consentimiento informado y compensación; el acuerdo entre dos evaluadores se informa con kappa y prevalencia. La declaración dice qué se evaluó, cómo, cuántas personas, qué criterios quedaron sin probar y quién los revisará.

## Ejemplo

Ejemplo de [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) (sección «Ejemplo profesional»):

En la plataforma, el paquete del proyecto tiene el prototipo del formulario de entrega (un HTML con sus estados), `accessibility.md` con la tabla de criterios y su política de lo no probado, `usability-notes.md` con el plan de evaluación y sus resultados, y un registro de hallazgos y decisiones. La evaluación con personas usa cuotas por modalidad, consentimiento informado y compensación; el acuerdo entre dos evaluadores se informa con kappa y prevalencia. La declaración dice qué se evaluó, cómo, cuántas personas, qué criterios quedaron sin probar y quién los revisará.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **El prototipo no se puede revisar** — causa: sin trazabilidad entre decisión, criterio y prueba. Corrección: registro de decisiones con enlace al hallazgo y a la prueba. ([SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- El prototipo es un archivo HTML con estructura semántica (región principal, encabezado, etiquetas, botón nativo), estados (vacío, carga, éxito, error y recuperación), mensajes en texto, un esquema de colores con contraste calculado y una maquetación que no desborda a 320 px. ([SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-169](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-169-diseno-centrado-en-personas-y-tareas/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Producto](./producto.md), [Versión](../v/version.md), [Declaración de conformidad](../d/declaracion-de-conformidad.md), [Kappa de Cohen](../k/kappa-de-cohen.md), [Modalidad de uso](../m/modalidad-de-uso.md), [Política de lo no probado](./politica-de-lo-no-probado.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-180 — Proyecto: prototipo accesible evaluado con usuarios](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (39 clases más lo mencionan; las que más):

[SE-557](../../../classes/part-46-desarrollo-de-software-asistido-por-ia/se-557-prototipado-scaffolding-y-exploracion-de-alternativas/README.md), [SE-127](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-127-prototipos-experimentos-y-reduccion-de-incertidumbre/README.md), [SE-255](../../../classes/part-21-software-movil-escritorio-y-multiplataforma/se-255-nativo-hibrido-web-wrapper-y-cross-platform/README.md), [SE-526](../../../classes/part-43-mantenimiento-y-modernizacion-legacy/se-526-economia-de-reescribir-frente-a-evolucionar/README.md), [SE-126](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-126-segmentacion-mercado-y-alternativas-existentes/README.md), [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), [SE-181](../../../classes/part-15-procesos-planificacion-y-estimacion/se-181-modelos-predictivos-iterativos-e-incrementales/README.md), [SE-128](../../../classes/part-10-descubrimiento-y-estrategia-de-producto/se-128-priorizacion-por-valor-riesgo-y-aprendizaje/README.md).

**Aparece en los casos de estudio:** [Uber](../../../casos/exito/uber.md), [Therac-25](../../../casos/fallo/therac-25.md), [Quibi](../../../casos/fallo/quibi.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: WCAG-EM, metodología de evaluación de conformidad](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) — alcance, muestra y reporte; autoridad: W3C.
- [W3C: Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) — criterios de éxito y niveles; autoridad: W3C.
- [Cohen, «A coefficient of agreement for nominal scales» (Educational and Psychological Measurement, 1960)](https://doi.org/10.1177/001316446002000104) — kappa; autoridad: Educational and Psychological Measurement.
- [Landis y Koch, «The measurement of observer agreement for categorical data» (Biometrics, 1977)](https://doi.org/10.2307/2529310) — interpretación convencional de kappa; autoridad: Biometrics.
- [Virzi, «Refining the test phase of usability evaluation» (Human Factors, 1992)](https://doi.org/10.1177/001872089203400407) — tamaño de muestra y problemas hallados; autoridad: Human Factors.

---

[↑ Glosario](../../README.md) · [← Protocolos de mensajes](./protocolos-de-mensajes.md) · [Prototipo desechable →](./prototipo-desechable.md)
