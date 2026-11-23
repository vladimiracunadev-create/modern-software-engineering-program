# Gravedad

[↑ Glosario](../../README.md) · [← GraphQL](./graphql.md) · [Gravedad de los datos →](./gravedad-de-los-datos.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Escala escrita que mide el impacto de un hallazgo sobre la capacidad de completar la tarea.

Definición de trabajo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md).

## Por qué importa

En [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), el tema «Hallazgos con criterio, gravedad y evidencia» importa porque convierte una observación en algo que se pueda arreglar y comprobar.

## Cómo funciona

Según [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md):

Un hallazgo registra el criterio incumplido, dónde ocurre, cómo se reproduce, a quién afecta, su gravedad (una escala fija y escrita) y la evidencia (captura, fragmento, descripción). Un hallazgo vago («mejorar accesibilidad») no se puede reparar ni comprobar. La gravedad no es solo técnica: un bloqueo total del proceso para quien usa teclado es más grave que un título genérico, aunque ambos sean fallos de criterio.

Según [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md):

En la plataforma, la auditoría de un flujo parte de un alcance firmado (pasos, estados y entornos), usa el auditor en cada cambio y una lista manual por criterio con responsable y fecha. Los hallazgos viven en un registro con criterio, gravedad, afectados estimados y esfuerzo; el orden de reparación se discute con la tabla de valor por hora y la lista de bloqueos totales. Cada reparación incluye la prueba que fallaba antes y pasa después, y una revisión con una persona que usa tecnologías de apoyo cierra los hallazgos graves.

## Ejemplo

Ejemplo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sección «Ejemplo profesional»):

En la plataforma, la auditoría de un flujo parte de un alcance firmado (pasos, estados y entornos), usa el auditor en cada cambio y una lista manual por criterio con responsable y fecha. Los hallazgos viven en un registro con criterio, gravedad, afectados estimados y esfuerzo; el orden de reparación se discute con la tabla de valor por hora y la lista de bloqueos totales. Cada reparación incluye la prueba que fallaba antes y pasa después, y una revisión con una persona que usa tecnologías de apoyo cierra los hallazgos graves.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)) son:

- **Se declara el flujo accesible con cero hallazgos** — causa: se confundió «las reglas no encuentran nada» con accesibilidad. Corrección: declarar alcance, revisión humana y lo no comprobado.
- **Se arreglan los hallazgos baratos y los bloqueos esperan** — causa: orden por facilidad. Corrección: comparar órdenes con personas bloqueadas y esfuerzo.

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- La gravedad no es solo técnica: un bloqueo total del proceso para quien usa teclado es más grave que un título genérico, aunque ambos sean fallos de criterio. ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md))

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Capacidad](../c/capacidad.md), [Hallazgo](../h/hallazgo.md), [Impacto](../i/impacto.md), [Sobre](../s/sobre.md), [Alcance de la auditoría](../a/alcance-de-la-auditoria.md), [Mutación](../m/mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

**También se usa en** (21 clases más lo mencionan; las que más):

[SE-445](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-445-riesgo-peligro-y-seguridad-funcional-hara-fmea-fta-y-stpa/README.md), [SE-275](../../../classes/part-22-embedded-iot-y-tiempo-real/se-275-taller-modelar-fallos-fisicos-y-digitales/README.md), [SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), [SE-448](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-448-aviacion-do-178c-do-254-y-arp4754/README.md), [SE-405](../../../classes/part-33-cloud-plataforma-e-infraestructura/se-405-multi-cloud-hibrido-y-portabilidad-real/README.md), [SE-447](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-447-automocion-iso-26262-y-niveles-asil/README.md), [SE-449](../../../classes/part-37-sistemas-criticos-tiempo-real-y-normas-de-seguridad/se-449-dispositivos-medicos-iec-62304/README.md), [SE-457](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-457-principios-de-seguridad-y-modelos-de-amenaza/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [W3C: WCAG-EM, metodología de evaluación de conformidad](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) — alcance, muestra, auditoría y reporte; autoridad: W3C.
- [W3C: Comprender 3.3.2 Etiquetas o instrucciones](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) — etiquetas en la entrada de datos; autoridad: W3C.
- [W3C: Comprender 3.3.7 Entrada redundante](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) — no pedir dos veces lo mismo; autoridad: W3C.
- [W3C: Comprender 3.3.8 Autenticación accesible (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) — autenticación sin pruebas cognitivas; autoridad: W3C.
- [W3C: Comprender 3.1.1 Idioma de la página](https://www.w3.org/WAI/WCAG22/Understanding/language-of-page.html) — idioma declarado; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← GraphQL](./graphql.md) · [Gravedad de los datos →](./gravedad-de-los-datos.md)
