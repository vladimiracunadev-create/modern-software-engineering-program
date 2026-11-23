# Alcance de la auditoría

[↑ Glosario](../../README.md) · [← Alcance](./alcance.md) · [Alcance de un cambio →](./alcance-de-un-cambio.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** C — Producto, requisitos y especificación · **Primera aparición:** [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md)

## Definición

Conjunto de pantallas, estados y entornos que se evalúan y lo que se excluye de forma explícita.

Definición de trabajo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md).

## Por qué importa

La clase donde se define, [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md), existe con este propósito: el taller existe para que recorras de principio a fin una auditoría y una reparación: encontrar las barreras de un flujo, ordenarlas por quién bloquean y cuánto cuesta arreglarlas, repararlas y proteger la reparación con pruebas, declarando lo que las pruebas no ven.

## Cómo funciona

Según [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md):

Los que existan: un conteo bajo no prueba accesibilidad y uno alto no prueba mala calidad. Lo importante es la gravedad y el alcance de cada uno, y que el alcance de la auditoría haya incluido los estados donde más se rompe.

## Ejemplo

Ejemplo de [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) (sección «Preguntas frecuentes»):

Los que existan: un conteo bajo no prueba accesibilidad y uno alto no prueba mala calidad. Lo importante es la gravedad y el alcance de cada uno, y que el alcance de la auditoría haya incluido los estados donde más se rompe.

## Errores y confusiones comunes

Las clases no registran un error exclusivo de este término. Los errores frecuentes del tema donde se enseña ([SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)) son:

- **Se declara el flujo accesible con cero hallazgos** — causa: se confundió «las reglas no encuentran nada» con accesibilidad. Corrección: declarar alcance, revisión humana y lo no comprobado.
- **Se arreglan los hallazgos baratos y los bloqueos esperan** — causa: orden por facilidad. Corrección: comparar órdenes con personas bloqueadas y esfuerzo.

## Límites y cuándo no aplica

Las clases no fijan un límite propio para este término. Los límites del tema donde se enseña ([SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md)) son: Las definiciones son operativas para la plataforma de entregas. No convierten términos con historia más amplia en sinónimos y deben contrastarse con la documentación primaria enlazada al final. Se ejecutaron tres experimentos con datos sintéticos en Windows y Ubuntu (WSL2) con resultados idénticos. No se usó ningún escáner de producción, lector de pantalla ni persona usuaria de tecnologías de apoyo, y los hallazgos, sus estimaciones, el auditor de ocho reglas y las 13 mutaciones son construcciones del autor. La siguiente clase integra todo en un prototipo evaluado con personas.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-173](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-173-accesibilidad-perceptible-operable-y-comprensible/README.md), [SE-178](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-178-investigacion-de-usabilidad-y-medicion/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Conjunto](../c/conjunto.md), [Entorno](../e/entorno.md), [Estado](../e/estado.md), [Gravedad](../g/gravedad.md), [Hallazgo](../h/hallazgo.md), [Mutación](../m/mutacion.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-179 — Taller: auditar y reparar un flujo excluyente](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/se-179-taller-auditar-y-reparar-un-flujo-excluyente/README.md) — [Parte 14](../../../classes/part-14-experiencia-accesibilidad-e-internacionalizacion/README.md), Experiencia, accesibilidad e internacionalización.

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

[↑ Glosario](../../README.md) · [← Alcance](./alcance.md) · [Alcance de un cambio →](./alcance-de-un-cambio.md)
