# Hallazgo

[↑ Glosario](../../README.md) · [← Habilidad](./habilidad.md) · [Handler idempotente →](./handler-idempotente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** compuesta desde las clases · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Observación de un incumplimiento con su criterio, lugar, reproducción, afectados, gravedad y evidencia.

Definición de trabajo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md).

El programa usa el término con matices según la clase; el sentido principal es el anterior y los demás lo precisan:

- En [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md): Coincidencia de una regla del verificador con un patrón de riesgo.
- En [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md): Relación estructurada entre evidencia, interpretación y siguiente prueba.

## Por qué importa

En [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), el tema «Hallazgos con criterio, gravedad y evidencia» importa porque convierte una observación en algo que se pueda arreglar y comprobar.

## Cómo funciona

Según [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md):

Un hallazgo registra el criterio incumplido, dónde ocurre, cómo se reproduce, a quién afecta, su gravedad (una escala fija y escrita) y la evidencia (captura, fragmento, descripción). Un hallazgo vago («mejorar accesibilidad») no se puede reparar ni comprobar. La gravedad no es solo técnica: un bloqueo total del proceso para quien usa teclado es más grave que un título genérico, aunque ambos sean fallos de criterio.

Según [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md):

En la plataforma, la auditoría de un flujo parte de un alcance firmado (pasos, estados y entornos), usa el auditor en cada cambio y una lista manual por criterio con responsable y fecha. Los hallazgos viven en un registro con criterio, gravedad, afectados estimados y esfuerzo; el orden de reparación se discute con la tabla de valor por hora y la lista de bloqueos totales. Cada reparación incluye la prueba que fallaba antes y pasa después, y una revisión con una persona que usa tecnologías de apoyo cierra los hallazgos graves.

## Ejemplo

Ejemplo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sección «Ejemplo mínimo»):

El fragmento cuenta hallazgos de un formulario con dos reglas. Antes de ejecutarlo, predice cuántos hallazgos produce.

## Errores y confusiones comunes

Errores que las clases asocian con este término (síntoma → causa → corrección):

- **Se declara el flujo accesible con cero hallazgos** — causa: se confundió «las reglas no encuentran nada» con accesibilidad. Corrección: declarar alcance, revisión humana y lo no comprobado. ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md))
- **Se arreglan los hallazgos baratos y los bloqueos esperan** — causa: orden por facilidad. Corrección: comparar órdenes con personas bloqueadas y esfuerzo. ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md))
- **El verificador llega a cero y hay un incidente** — causa: se confió en la ausencia de hallazgos. Corrección: lista de lo que no ve y revisión humana. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Límites y cuándo no aplica

Lo que las clases dicen sobre dónde deja de valer este término:

- Un hallazgo vago («mejorar accesibilidad») no se puede reparar ni comprobar. ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md))
- Los hallazgos del taller son las respuestas concretas a la segunda pregunta: texto de terceros insertado en un script, código de terceros descargado y ejecutado, eventos que dan privilegios a código no revisado. ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md))

## Relación con otros conceptos

- **Prerrequisito:** [Reproducción](../r/reproduccion.md).
- **Ver también:** [Evidencia](../e/evidencia.md), [Gravedad](../g/gravedad.md), [Interpretación](../i/interpretacion.md), [Observación](../o/observacion.md), [Adaptador](../a/adaptador.md), [Alcance de la auditoría](../a/alcance-de-la-auditoria.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-036 — Proyecto: kit de diagnóstico multiplataforma](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md) — [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md), Sistemas operativos, terminal y automatización base.
- [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.
- [SE-491 — Taller: endurecer un pipeline vulnerable](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md) — [Parte 40](../../../classes/part-40-ci-cd-iac-y-platform-engineering/README.md), CI/CD, IaC y platform engineering.

**También se usa en** (165 clases más lo mencionan; las que más):

[SE-465](../../../classes/part-38-seguridad-privacidad-y-cumplimiento/se-465-vulnerabilidades-divulgacion-y-respuesta/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md), [SE-511](../../../classes/part-42-ingenieria-del-caos/se-511-game-days-y-ejercicios-de-respuesta-a-incidentes/README.md), [SE-566](../../../classes/part-47-spec-agentes-y-ciclo-de-vida-agentic/se-566-constitucion-specify-clarify-plan-y-tasks/README.md), [SE-011](../../../classes/part-00-ingenieria-de-software-como-profesion/se-011-taller-anatomia-verificable-de-un-producto-real/README.md), [SE-504](../../../classes/part-41-observabilidad-sre-e-incidentes/se-504-proyecto-operacion-observable-y-recuperable/README.md), [SE-180](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-180-proyecto-prototipo-accesible-evaluado-con-usuarios/README.md), [SE-429](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-429-pruebas-exploratorias-y-sesiones/README.md).

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [Python: `collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter) — recuento de hallazgos por categoría.
- [W3C: WCAG-EM, metodología de evaluación de conformidad](https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/) — alcance, muestra, auditoría y reporte; autoridad: W3C.
- [W3C: Comprender 3.3.2 Etiquetas o instrucciones](https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html) — etiquetas en la entrada de datos; autoridad: W3C.
- [W3C: Comprender 3.3.7 Entrada redundante](https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html) — no pedir dos veces lo mismo; autoridad: W3C.
- [W3C: Comprender 3.3.8 Autenticación accesible (mínimo)](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html) — autenticación sin pruebas cognitivas; autoridad: W3C.

---

[↑ Glosario](../../README.md) · [← Habilidad](./habilidad.md) · [Handler idempotente →](./handler-idempotente.md)
