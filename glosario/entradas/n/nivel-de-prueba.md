# Nivel de prueba

[↑ Glosario](../../README.md) · [← Nivel de integridad](./nivel-de-integridad.md) · [Nivel de riesgo →](./nivel-de-riesgo.md)

> **Tipo:** concepto · **Nivel:** apoyo · **Profundidad:** compuesta desde las clases · **Familia:** F — Calidad, seguridad y entrega · **Primera aparición:** [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md)

## Definición

Alcance y costo con los que se comprueba el sistema: unidad, contrato, integración, extremo a extremo, carga, exploración.

Definición de trabajo de [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md).

## Por qué importa

La clase donde se define, [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md), existe con este propósito: la clase existe para que decidas qué probar, con qué nivel de prueba y cuánto esfuerzo a partir del riesgo que cada componente representa, y para que declares por escrito qué no vas a probar y por qué.

## Cómo funciona

[SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) usa este término dentro de otro tema, sin una sección propia. El contexto en que aparece: Las definiciones son operativas para esta clase y no sustituyen el vocabulario de las normas citadas en las fuentes.

## Ejemplo

Caso medido en la sección «Qué nivel de prueba puede ver qué fallo» de [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md):

El resultado es el conjunto unitaria + contrato + extremo a extremo + carga, con 91,1 minutos por ejecución. Las pruebas unitarias solas cubren dos de ocho clases; sumar integración y contrato eleva la cobertura a cuatro. Lo notable es que las cuatro clases restantes (recorrido de usuario, concurrencia, rendimiento y accesibilidad) solo las ven niveles caros, de modo que una estrategia con miles de pruebas unitarias y ninguna de carga no tiene cobertura de rendimiento aunque sus números parezcan altos.

## Errores y confusiones comunes

Ningún error de las clases nombra este término; estos son los errores frecuentes del tema donde se enseña ([SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)) son:

- **«Probamos todo» y aun así hay incidentes en producción** — causa: se confunde cobertura de líneas con detección de defectos. Corrección: medir con mutantes y listar qué clases de fallo no tienen nivel asignado.
- **El reparto cambia cada trimestre sin explicación** — causa: las estimaciones viven en la cabeza de alguien. Corrección: documentar p, impacto y su fuente; reestimar tras un incidente.

## Límites y cuándo no aplica

Ninguna clase fija un límite propio para este término; estos son los límites del tema donde se enseña ([SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md)) son: Las definiciones son operativas para esta clase y no sustituyen el vocabulario de las normas citadas en las fuentes. Se ejecutaron tres experimentos con modelos del autor y datos sintéticos en Windows y Ubuntu (WSL2) con salidas idénticas. No se midió ningún sistema real, equipo ni defecto: probabilidad, impacto, dificultad, costos por nivel y la forma exponencial de la detección son supuestos. El conjunto mínimo de niveles es una consecuencia de la matriz que escribí, no un resultado empírico.

## Relación con otros conceptos

- **Prerrequisito:** las clases previas [SE-335](../../../classes/part-27-arquitectura-de-software-y-dominio/se-335-taller-revisar-una-arquitectura-contra-escenarios/README.md) (sin término del glosario que lo sustituya).
- **Ver también:** [Alcance](../a/alcance.md), [Contrato](../c/contrato.md), [Costo](../c/costo.md), [Exploración](../e/exploracion.md), [Exclusión](../e/exclusion.md), [Pérdida residual](../p/perdida-residual.md).
- **Se confunde con:** las clases no registran una confusión específica; contrasta su definición con la de los conceptos de «Ver también».

## Dónde se enseña

**Se define o se desarrolla en:**

- [SE-421 — Calidad por riesgo y propósito de las pruebas](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-421-calidad-por-riesgo-y-proposito-de-las-pruebas/README.md) — [Parte 35](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/README.md), Estrategia y técnicas de prueba.

**También se usa en** (2 clases más lo mencionan; las que más):

[SE-305](../../../classes/part-25-diseno-patrones-y-refactorizacion/se-305-patrones-funcionales-reactivos-y-concurrentes/README.md), [SE-432](../../../classes/part-35-estrategia-y-tecnicas-de-prueba/se-432-proyecto-estrategia-ejecutable-por-riesgo/README.md).

## Sinónimos y traducción

El programa no registra sinónimos ni traducciones distintas de la forma del título.

## Fuentes

Fuentes de las clases donde se enseña (cada una respalda el mecanismo que su clase indica):

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) — atributos de calidad del producto; autoridad: ISO/IEC.
- [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/pubs/sp/800/30/r1/final) — evaluación de riesgos; autoridad: NIST.
- [Martin Fowler, «TestPyramid»](https://martinfowler.com/bliki/TestPyramid.html) — reparto por nivel; autoridad: autor del texto.
- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — costo de las pruebas lentas; autoridad: equipo de pruebas de Google.
- [Inozemtseva y Holmes, «Coverage is not strongly correlated with test suite effectiveness»](https://doi.org/10.1145/2568225.2568271) — cobertura y eficacia; autoridad: artículo revisado de ICSE 2014.

---

[↑ Glosario](../../README.md) · [← Nivel de integridad](./nivel-de-integridad.md) · [Nivel de riesgo →](./nivel-de-riesgo.md)
