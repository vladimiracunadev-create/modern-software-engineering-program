# Hallazgo

[↑ Glosario](../../README.md) · [← Habilidad](./habilidad.md) · [Handler idempotente →](./handler-idempotente.md)

> **Tipo:** concepto · **Nivel:** troncal · **Profundidad:** desarrollada · **Familia:** A — Fundamentos de la profesión · **Primera aparición:** [Parte 02](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/README.md)

## Definición

Un **hallazgo** es la observación de un incumplimiento con su criterio, lugar, reproducción, afectados, gravedad y evidencia ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)). Otros usos en el programa: la coincidencia de una regla del verificador con un patrón de riesgo ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md)) y la relación estructurada entre evidencia, interpretación y siguiente prueba ([SE-036](../../../classes/part-02-sistemas-operativos-terminal-y-automatizacion-base/se-036-proyecto-kit-de-diagnostico-multiplataforma/README.md)). Lo común es que un hallazgo es un registro accionable, no una impresión.

## Por qué importa

Una auditoría sin hallazgos bien formados no se puede reparar ni comprobar. [SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) lo dice con claridad: «mejorar accesibilidad» es un hallazgo vago. Con campos completos, el equipo puede priorizar, asignar y verificar el cierre. Además, decide la lectura de cero hallazgos: no significa «cumple», significa «las reglas no encontraron nada».

## Cómo funciona

Un hallazgo ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)) registra:

- el **criterio** incumplido;
- **dónde** ocurre y **cómo se reproduce**;
- **a quién afecta**;
- su **gravedad**, en una escala fija y escrita;
- la **evidencia** (captura, fragmento, descripción).

La gravedad no es solo técnica: un bloqueo total del proceso para quien usa teclado es más grave que un título genérico, aunque ambos sean fallos de criterio. Los hallazgos viven en un registro con criterio, gravedad, afectados estimados y esfuerzo; el orden de reparación se discute con la tabla de valor por hora y la lista de bloqueos totales. Cada reparación incluye la prueba que fallaba antes y pasa después, y una revisión con una persona que use tecnologías de apoyo cierra los hallazgos graves.

## Ejemplo

```text
H-014 | criterio: operable por teclado | lugar: paso 3, enviar entrega
reproducción: Tab no alcanza "Enviar" | afectados: usuarios de teclado
gravedad: bloqueo total | evidencia: captura + secuencia de teclas
```

En [SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md), un hallazgo de un verificador de workflows puede ser texto de terceros insertado en un script, o código de terceros descargado y ejecutado.

## Errores y confusiones comunes

- **Declarar accesible un flujo con cero hallazgos.** Causa: se confundió «las reglas no encuentran nada» con accesibilidad; corrección: declarar alcance, revisión humana y lo no comprobado ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)).
- **Arreglar los baratos y dejar esperar los bloqueos.** Causa: orden por facilidad; corrección: comparar órdenes con personas bloqueadas y esfuerzo ([SE-179](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)).
- **Verificador en cero y hay un incidente.** Causa: se confió en la ausencia de hallazgos; corrección: lista de lo que no ve y revisión humana ([SE-491](../../../classes/part-40-ci-cd-iac-y-platform-engineering/se-491-taller-endurecer-un-pipeline-vulnerable/README.md)).

## Límites y cuándo no aplica

Un hallazgo es tan bueno como su alcance: lo que la auditoría no cubrió no genera hallazgos. Las escalas de gravedad son convenciones del equipo, no medidas objetivas. Y los hallazgos automáticos pueden ser falsos positivos: requieren comprobación antes de convertirse en trabajo.

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

**Aparece en los casos de estudio:** [HealthCare.gov](../../../casos/fallo/healthcare-gov.md), [CrowdStrike](../../../casos/fallo/crowdstrike.md), [Ariane 5, vuelo 501](../../../casos/fallo/ariane-5-vuelo-501.md), [Boeing 737 MAX y MCAS](../../../casos/fallo/boeing-737-max-mcas.md), [Post Office Horizon](../../../casos/fallo/post-office-horizon.md).

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
